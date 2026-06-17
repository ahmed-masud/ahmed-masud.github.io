# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development

No build step. Serve locally with:

```bash
python3 -m http.server 4000
# visit http://localhost:4000
```

The site deploys automatically to GitHub Pages on push to `main`. `.nojekyll` disables Jekyll processing so files are served as-is.

## Architecture

Pure static HTML/CSS/JS — no framework, no bundler, no dependencies beyond Google Fonts.

**Main pages:**
- `index.html` — single-page personal site
- `resume.html` — canonical resume (print-optimized, fixed light theme via `resume.css`)
- `resume/<company>/` — tailored resume/cover letter sets for specific job applications

**Stylesheets:**
- `public/css/style.css` — all site styles + four themes (moody, dark, light, access)
- `public/css/resume.css` — resume-specific layout; always uses a fixed light/print theme regardless of site theme
- `public/css/fonts.css` — Google Fonts import

## Theme System

Themes are implemented as CSS `[data-theme="<name>"]` attribute selectors on `<html>`. The four themes are `moody` (default dark), `dark`, `light`, and `access` (High Contrast, WCAG AA+). Theme preference is saved in `localStorage` and applied on load. Theme switching is done via JS toggling the `data-theme` attribute and updating `aria-pressed` on the toolbar buttons.

The main site (`index.html`) defaults to `data-theme="access"` in HTML; JS overrides this from `localStorage` or `prefers-color-scheme`. The `resume.html` page does **not** use the theme switcher — `resume.css` defines its own fixed variables.

## Tailored Resume Pages

Each company-specific application lives in `resume/<company>/` and typically contains:
- `<company>-resume.html` — tailored resume body
- `<company>-cover-letter.html` — cover letter
- `index.html` — landing/selector page
- `cl.html` — symlink or redirect to the cover letter

These pages load both `style.css` (for the theme switcher UI) and `resume.css` (for resume layout), and include `meta name="robots" content="noindex, nofollow"`.

## LLM Tailoring (`feature/llm-tailoring` branch)

`build.py tailor` uses a local Ollama model to auto-generate a tailored resume + cover letter from a job description file. Requires Ollama running locally with `mistral` or `llama3.2` (minimum 7B model — `tinyllama` is too small for structured JSON output).

```bash
# Pull a capable model first (one-time, local)
ollama pull mistral

# Local Ollama
make tailor COMPANY="Acme" ROLE="VP Engineering" JD=path/to/jd.txt

# Remote Ollama (flag or env var)
make tailor COMPANY="Acme" ROLE="VP Eng" JD=jd.txt HOST=http://gpu-box:11434
OLLAMA_HOST=http://gpu-box:11434 OLLAMA_API_KEY=secret make tailor ...

# Review/edit the generated job file, then render
make render JOB=ACME_2026-06-16
```

The LLM reads `resume-src/master/resume.md` and the JD, then outputs a fully populated `resume-src/jobs/COMPANY_DATE.md` with tailored summary, experience ordering, skills section, and cover letter paragraphs. Always review before rendering.

## Accessibility Conventions

- All interactive elements must have visible `focus-visible` rings
- Decorative elements use `aria-hidden="true"`
- External links use `rel="noopener noreferrer"` and `aria-label` noting the new tab
- Use `<time datetime="">` for machine-readable dates
- The `#theme-announce` div with `aria-live="polite"` announces theme changes to screen readers
