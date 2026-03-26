# The Poets Codex

This repository contains an in‑development project called The Poets Codex, which is a website aiming to bring together a curated set of esteemed poets.

---

## Project Contents

A short summary of what each part of the project contains:

- `source/` – Markdown pages and HTML templates used to generate the site  
- `docs/` – the generated static site ready for deployment  
- `assets/` – fonts, images, and supporting files  
- `RECORD.md` – consolidated technical record of design style for the project
- `README.md` – main overview of the project  
- `.github/workflows/` – automated workflow that runs the build process

---

## Development Overview

A simplified view of how the website is being developed:

| Stage        | Location               | Purpose                                                |
|--------------|------------------------|--------------------------------------------------------|
| Write        | `source/`              | Markdown pages and templates are authored and updated |
| Build        | `build.py`             | Python script applies templates and assembles pages   |
| Automate     | `.github/workflows/`   | Workflow triggers the build script upon manual dispatch     |
| Deploy       | `docs/`                | Static HTML output used for GitHub Pages deployment   |

---

## Status

Version `0.0.0` – Draft  
The project is in its earliest phase, with structure, templates, and generation logic being established.

---

<sub>© Mohammed Usman</sub>

<sub>All rights reserved. No commercial use, redistribution, or derivatives.</sub>
