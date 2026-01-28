# The Poets Codex

This repository contains an in‑development project called The Poets Codex, which is a website aiming to bring together a curated set of esteemed poets.

## Repository Contents

A simplified view of the project’s structure:

`content/` – Markdown files for all sections and pages  
`source/` – build script and HTML templates  
`docs/` – generated static site for deployment  
`assets/` – styles, images, and supporting files  
`README.md` – main overview of the project  
`ROADMAP.md` – planned development and future directions  
`DEVLOG.md` – notes on changes, iterations, and build progress  
`DESIGN-NOTES.md` – design philosophy, layout decisions, and rationale  
`.github/` – automated workflow that triggers the build process

## Build Process

A simplified view of the project's build pipeline:

| Stage      | Directory     | Purpose                                                |
|------------|---------------|--------------------------------------------------------|
| Write      | `content/`    | All poet folios and pages written in Markdown         |
| Build      | `source/`     | Python script applies templates and assembles pages   |
| Generate   | `.github/`    | Automated action that runs the build script           |
| Output     | `docs/`       | Final static HTML generated for deployment            |

## Status

Version `0.0.0` – Draft
