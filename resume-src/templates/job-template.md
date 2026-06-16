---
# ── Application metadata ──────────────────────────────────────────
id:      {{JOB_ID}}
company: {{COMPANY}}
role:    "{{ROLE}}"
date:    {{DATE}}
status:  ":draft:"
source:  "{{SOURCE}}"
url:     "{{URL}}"

# ── Header overrides (remove to use master defaults) ─────────────
# title_override:    "Engineering Manager · ..."
# location_override: "Ottawa, ON, Canada · Remote"

# ── Summary (remove to use master summary) ────────────────────────
# summary_override: |
#   Custom summary for this application...

# highlights:
#   - "Key highlight 1"
#   - "Key highlight 2"

# ── Sections (order determines render order) ─────────────────────
sections:
  - summary
  - experience
  - patents
  - education
  - skills
  # - clearances   # uncomment for defence/government roles

# ── Skills (remove to use master skills) ──────────────────────────
# skills_override:
#   Languages: "..."
#   "Web & Commerce": "..."

# ── Experience: which entries and in what order ───────────────────
# experience_order:
#   - safai
#   - trustifier
#   - googgun
#   - nrc
#   - dod        # include for defence roles
#   - remedium   # include for deep-tech / security history

expand_first_n: 1   # number of accordion entries open by default

# ── Per-entry content overrides (partial — unset fields keep master values)
# experience_overrides:
#   safai:
#     desc: |
#       Tailored description for this role...
#     bullets:
#       - "Tailored bullet 1"
#       - "Tailored bullet 2"

# ── Patent note override ──────────────────────────────────────────
# patent_note_override: |
#   Tailored patent description connecting to this role...

# ── Cover letter metadata ─────────────────────────────────────────
cover_letter:
  salutation: "Dear {{COMPANY}} Hiring Team,"
  date: ""   # leave blank to auto-format from date above
---

## Job Description

<!-- Paste the full job description here for reference -->

## Cover Letter

<!-- Write the cover letter body here in plain markdown.
     Blank lines become paragraph breaks.
     Use **bold** for emphasis, no headers needed.

Example:

Opening paragraph about why this role / company.

Paragraph connecting your experience to their problem.

Paragraph on tech/stack fit.

Paragraph on leadership style.

Closing paragraph with call to action.
-->
