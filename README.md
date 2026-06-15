# ahmed-masud.github.io

Personal website for Ahmed Masud — Enterprise Architect, AI Security Pioneer,
Founder of [saf.ai](https://safai-labs.github.io) and Trustifier.

Live at: **https://ahmed-masud.github.io**

## Stack

Pure static HTML/CSS/JS — no build step, no framework, no dependencies.
Hosted on GitHub Pages with `.nojekyll` to bypass Jekyll processing.

## Structure

```
index.html          — single-page site
public/
  css/
    style.css       — all styles + 4 themes
    fonts.css       — Google Fonts import
  favicon.ico
_posts/             — legacy blog posts (kept for reference)
```

## Themes

The site ships with four themes switchable via the toolbar:

| Theme | Description |
|-------|-------------|
| Moody | Default — deep purple-dark, gold accents |
| Dark | Near-black, blue accents |
| Light | Clean minimal, generous whitespace |
| High Contrast | WCAG AA+ — pure black/white, 17px body, underlined links |

Theme preference is persisted in `localStorage` and respects `prefers-color-scheme`.

## Accessibility

- Semantic HTML5 landmarks (`<header>`, `<main>`, `<footer>`, `<nav>`, `<section>`, `<article>`, `<aside>`)
- Skip-to-main-content link
- `aria-live` region for theme change announcements
- All interactive elements have visible `focus-visible` rings
- Decorative elements marked `aria-hidden="true"`
- External links include `rel="noopener noreferrer"` and `aria-label` noting new tab
- `<time datetime="">` elements for machine-readable dates
- `<dl>/<dt>/<dd>` for contact and metrics
- WCAG AA+ contrast in High Contrast theme

## Development

No build step needed. Open `index.html` directly in a browser, or serve locally:

```bash
python3 -m http.server 4000
# then visit http://localhost:4000
```

## License

Content © 2026 Ahmed Masud. All rights reserved.
