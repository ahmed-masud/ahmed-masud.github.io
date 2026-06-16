#!/usr/bin/env python3
"""
Resume & cover-letter builder for ahmed-masud.github.io.

Usage:
  python build.py new --company Acme --role "Engineering Manager" [--date 2026-06-16] [--source LinkedIn] [--url https://...]
  python build.py render ACME_2026-06-16
  python build.py render-all
  python build.py list
  python build.py status ACME_2026-06-16 interview
  python build.py export
"""

import csv
import re
import sys
from datetime import date as date_type, datetime
from pathlib import Path

import click
import frontmatter
import jinja2
import markdown as md_lib
import yaml
from rich.console import Console
from rich.table import Table

console = Console()

ROOT   = Path(__file__).parent.parent   # repo root  (ahmed-masud.github.io/)
SRC    = Path(__file__).parent          # resume-src/
MASTER = SRC / "master"
JOBS   = SRC / "jobs"
TMPL   = SRC / "templates"
OUTPUT = ROOT / "resume"
APPS   = ROOT / "applications.md"

# ── Token expansion ───────────────────────────────────────────────────────────

_TOKENS: dict | None = None

def _load_tokens() -> dict:
    with open(SRC / "tokens.yml") as f:
        return yaml.safe_load(f)

def tokens() -> dict:
    global _TOKENS
    if _TOKENS is None:
        _TOKENS = _load_tokens()
    return _TOKENS

_TOKEN_RE = re.compile(r":([a-z][a-z0-9_-]*):", re.ASCII)

def expand_tokens(text: str) -> str:
    """Replace :token: shortcodes with their display value."""
    def _sub(m: re.Match) -> str:
        key = m.group(1)
        t = tokens()
        if key in t.get("icons", {}):
            return t["icons"][key]
        if key in t.get("status", {}):
            s = t["status"][key]
            return f'{s["icon"]} {s["label"]}'
        return m.group(0)
    return _TOKEN_RE.sub(_sub, text)

def md_to_html(text: str) -> str:
    """Token-expand then render markdown → HTML (block-level)."""
    return md_lib.markdown(
        expand_tokens(text),
        extensions=["tables", "fenced_code"],
    )

def md_inline(text: str) -> str:
    """Token-expand, render markdown, strip wrapping <p> tags for inline use."""
    html = md_lib.markdown(expand_tokens(text))
    html = re.sub(r"^\s*<p>", "", html.strip())
    html = re.sub(r"</p>\s*$", "", html.strip())
    return html

# ── Jinja2 environment ────────────────────────────────────────────────────────

def jinja_env() -> jinja2.Environment:
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TMPL)),
        autoescape=jinja2.select_autoescape(["html"]),
        keep_trailing_newline=True,
    )
    env.filters["md"]        = md_to_html
    env.filters["md_inline"] = md_inline
    env.filters["tokens"]    = expand_tokens
    return env

# ── Data loading ──────────────────────────────────────────────────────────────

def load_master() -> dict:
    post = frontmatter.load(MASTER / "resume.md")
    data = dict(post.metadata)
    data["_body"] = post.content
    return data

def load_job(job_id: str) -> tuple[dict, str]:
    path = JOBS / f"{job_id}.md"
    if not path.exists():
        raise click.ClickException(f"Job file not found: {path}")
    post = frontmatter.load(path)
    return dict(post.metadata), post.content

def extract_md_section(content: str, heading: str) -> str:
    """Extract the markdown body of a ## Heading section."""
    pat = rf"(?m)^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"
    m = re.search(pat, content, re.DOTALL)
    return m.group(1).strip() if m else ""

# ── Context assembly ──────────────────────────────────────────────────────────

def _format_date(d) -> str:
    if isinstance(d, date_type):
        return d.strftime("%-d %B %Y")
    return datetime.strptime(str(d), "%Y-%m-%d").strftime("%-d %B %Y")

def build_context(job_id: str) -> dict:
    master = load_master()
    job, job_body = load_job(job_id)

    # Assemble experience list: select by order, apply per-entry overrides
    master_exp = {e["id"]: e for e in master.get("experience", [])}
    order      = job.get("experience_order", list(master_exp.keys()))
    overrides  = job.get("experience_overrides", {})

    experience = []
    for eid in order:
        if eid not in master_exp:
            console.print(f"[yellow]Warning:[/] experience id '{eid}' not found in master resume")
            continue
        entry = dict(master_exp[eid])
        if eid in overrides:
            entry.update(overrides[eid])
        experience.append(entry)

    # Patent desc: job can override the note on the first patent
    patents = [dict(p) for p in master.get("patents", [])]
    if "patent_note_override" in job and patents:
        patents[0]["desc"] = job["patent_note_override"].strip()

    # Cover letter date: job CL metadata or auto-format from application date
    cl_meta    = job.get("cover_letter", {})
    cl_date    = cl_meta.get("date", "") or _format_date(job["date"])
    cl_body_md = extract_md_section(job_body, "Cover Letter")

    date_val = job["date"]

    return {
        # Application identity
        "job_id":      job_id,
        "company":     job["company"],
        "role":        job["role"],
        "date_iso":    str(date_val),
        "date_display": _format_date(date_val),
        "status":      job.get("status", ":draft:"),
        "source":      job.get("source", ""),
        "url":         job.get("url", ""),

        # Header
        "name":     master["name"],
        "title":    job.get("title_override",    master["title"]),
        "location": job.get("location_override", master["location"]),
        "contact":  master["contact"],

        # Summary block
        "summary":    job.get("summary_override", master.get("summary", "")).strip(),
        "highlights": job.get("highlights",       master.get("highlights", [])),

        # Section ordering / selection
        "sections":       job.get("sections", ["summary", "experience", "patents", "education", "skills", "clearances"]),
        "expand_first_n": job.get("expand_first_n", 1),

        # Content blocks
        "skills":         job.get("skills_override", master.get("skills", {})),
        "experience":     experience,
        "patents":        patents,
        "awards":         master.get("awards", []),
        "education":      master.get("education", []),
        "certifications": master.get("certifications", []),
        "clearances":     master.get("clearances", ""),

        # Cover letter
        "cl_salutation":  cl_meta.get("salutation", "Dear Hiring Team,"),
        "cl_date_display": cl_date,
        "cl_body":        cl_body_md,

        # Asset paths (relative from resume/JOB_ID/)
        "css_root":  "../../public/css",
        "icon_root": "../../public",
    }

# ── Rendering ─────────────────────────────────────────────────────────────────

def render_file(tmpl_name: str, ctx: dict, out_path: Path) -> None:
    env  = jinja_env()
    tmpl = env.get_template(tmpl_name)
    html = tmpl.render(**ctx)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")

def render_job(job_id: str) -> Path:
    ctx = build_context(job_id)
    out = OUTPUT / job_id
    render_file("resume.html.j2",       ctx, out / "resume.html")
    render_file("cover-letter.html.j2", ctx, out / "cover-letter.html")
    render_file("index.html.j2",        ctx, out / "index.html")
    return out

# ── Applications index ────────────────────────────────────────────────────────

def update_index() -> None:
    rows = []
    for jf in sorted(JOBS.glob("*.md"), reverse=True):
        meta, _ = load_job(jf.stem)
        rows.append({
            "id":      jf.stem,
            "company": meta.get("company", ""),
            "role":    meta.get("role", ""),
            "date":    str(meta.get("date", "")),
            "status":  expand_tokens(str(meta.get("status", ":draft:"))),
            "url":     meta.get("url", ""),
        })

    lines = [
        "# Applications\n",
        "| Date | Company | Role | Status | Links |",
        "|------|---------|------|--------|-------|",
    ]
    for r in rows:
        resume_lnk = f"[resume](resume/{r['id']}/resume.html)"
        cl_lnk     = f"[CL](resume/{r['id']}/cover-letter.html)"
        jd_lnk     = f"[JD]({r['url']})" if r["url"] else ""
        links      = " · ".join(x for x in [resume_lnk, cl_lnk, jd_lnk] if x)
        lines.append(f"| {r['date']} | {r['company']} | {r['role']} | {r['status']} | {links} |")

    lines.append("")
    APPS.write_text("\n".join(lines), encoding="utf-8")

# ── CLI ───────────────────────────────────────────────────────────────────────

@click.group()
def cli():
    """Resume & cover-letter builder for ahmed-masud.github.io."""

@cli.command()
@click.option("--company", required=True, help="Company name, e.g. Acme")
@click.option("--role",    required=True, help="Job title / role")
@click.option("--date",    "date_str",    default=None,  help="YYYY-MM-DD (default: today)")
@click.option("--source",  default="",  help="Where you found it (LinkedIn, etc.)")
@click.option("--url",     default="",  help="Job posting URL")
def new(company: str, role: str, date_str: str | None, source: str, url: str):
    """Scaffold a new job application file."""
    if date_str is None:
        date_str = str(date_type.today())

    slug   = re.sub(r"[^A-Z0-9]", "", company.upper())
    job_id = f"{slug}_{date_str}"
    out    = JOBS / f"{job_id}.md"

    if out.exists():
        raise click.ClickException(f"Already exists: {out}")

    tmpl_path = TMPL / "job-template.md"
    content   = tmpl_path.read_text()
    for k, v in [
        ("{{COMPANY}}", company),
        ("{{ROLE}}",    role),
        ("{{DATE}}",    date_str),
        ("{{JOB_ID}}", job_id),
        ("{{SOURCE}}", source),
        ("{{URL}}",    url),
    ]:
        content = content.replace(k, v)

    out.write_text(content)
    console.print(f"[green]Created[/] {out.relative_to(ROOT)}")
    console.print(f"  1. Edit the job file with tailoring notes and CL body")
    console.print(f"  2. Run: [cyan]python resume-src/build.py render {job_id}[/]")

@cli.command()
@click.argument("job_id")
def render(job_id: str):
    """Render resume + cover letter + index for one job."""
    out = render_job(job_id)
    update_index()
    console.print(f"[green]✓[/] {out.relative_to(ROOT)}/")
    console.print("  resume.html · cover-letter.html · index.html")
    console.print("[dim]  applications.md updated[/]")

@cli.command("render-all")
def render_all():
    """Re-render every job in resume-src/jobs/."""
    for jf in sorted(JOBS.glob("*.md")):
        try:
            render_job(jf.stem)
            console.print(f"[green]✓[/] {jf.stem}")
        except Exception as e:
            console.print(f"[red]✗[/] {jf.stem}: {e}")
    update_index()
    console.print("[dim]applications.md updated[/]")

@cli.command("list")
def list_cmd():
    """List all applications with status."""
    tbl = Table(show_header=True, header_style="bold cyan")
    tbl.add_column("ID",     no_wrap=True)
    tbl.add_column("Role",   max_width=42)
    tbl.add_column("Status", no_wrap=True)
    tbl.add_column("Date",   no_wrap=True)
    for jf in sorted(JOBS.glob("*.md"), reverse=True):
        meta, _ = load_job(jf.stem)
        tbl.add_row(
            jf.stem,
            meta.get("role", ""),
            expand_tokens(str(meta.get("status", ":draft:"))),
            str(meta.get("date", "")),
        )
    console.print(tbl)

@cli.command()
@click.argument("job_id")
@click.argument("new_status")
def status(job_id: str, new_status: str):
    """Update application status (e.g. interview, offer, rejected)."""
    path = JOBS / f"{job_id}.md"
    post = frontmatter.load(path)
    token = new_status if new_status.startswith(":") else f":{new_status}:"
    post.metadata["status"] = token
    with open(path, "w") as f:
        f.write(frontmatter.dumps(post))
    update_index()
    console.print(f"[green]✓[/] {job_id} → {expand_tokens(token)}")

@cli.command()
def export():
    """Export applications.csv for import into Numbers / Excel."""
    rows = []
    for jf in sorted(JOBS.glob("*.md"), reverse=True):
        meta, _ = load_job(jf.stem)
        rows.append({
            "ID":      jf.stem,
            "Company": meta.get("company", ""),
            "Role":    meta.get("role", ""),
            "Date":    str(meta.get("date", "")),
            "Status":  expand_tokens(str(meta.get("status", ":draft:"))),
            "Source":  meta.get("source", ""),
            "URL":     meta.get("url", ""),
        })

    out = ROOT / "applications.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ID", "Company", "Role", "Date", "Status", "Source", "URL"])
        w.writeheader()
        w.writerows(rows)
    console.print(f"[green]✓[/] {out.relative_to(ROOT)} ({len(rows)} row{'s' if len(rows) != 1 else ''})")

if __name__ == "__main__":
    cli()
