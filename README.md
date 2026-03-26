# The Poets Codex

This repository contains an in‑development project called The Poets Codex, which is a website aiming to bring together a curated set of esteemed poets.

---

## Project Contents

A short summary of what each part of the project contains:

- `.github/workflows/` – automated workflow that runs the build process  
- `docs/` – the generated static site ready for deployment  
- `releases/` – optional snapshots of the site for versioned or archived builds  
- `source/` – Markdown pages and HTML templates used to generate the site  
- `.gitignore` – patterns specifying files and directories excluded from version control  
- `RECORD.md` – consolidated technical record of design style, development process, milestones, and roadmap  
- `README.md` – high‑level overview of the project, including purpose, structure, and development approach  
- `build.py` – Python build script that compiles Markdown and templates into static HTML  
- `requirements.txt` – Python dependencies required for the build process

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
