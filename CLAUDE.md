# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based GitHub Pages personal blog for Ahmed Masud, focused on open source projects. It uses the Hyde theme (built on Poole).

## Development Commands

```bash
# Install dependencies (first time)
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build the site
bundle exec jekyll build
```

The site is served at `http://localhost:4000` by default.

## Architecture

- `_config.yml` — site-wide settings (title, tagline, URL, pagination, markdown engine)
- `_layouts/` — page templates: `default.html` (base), `post.html`, `page.html`
- `_includes/` — reusable partials: `head.html`, `sidebar.html`
- `_posts/` — blog posts in Markdown, named `YYYY-MM-DD-title.markdown`
- `public/css/` — Hyde theme stylesheets (`poole.css`, `hyde.css`, `syntax.css`)
- `atom.xml` — Atom feed for the blog
- `index.html` — homepage with paginated post list

## Adding Content

New blog posts go in `_posts/` following the filename convention `YYYY-MM-DD-slug.markdown` with Jekyll front matter:

```yaml
---
layout: post
title: "Post Title"
---
```
