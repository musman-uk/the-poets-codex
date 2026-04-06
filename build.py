import os
import yaml
import markdown
from pathlib import Path
from jinja2 import Template
import shutil 

# Project paths (kept explicit rather than relative inside functions
# to avoid repeated resolution and to ensure predictable build structure)
ROOT = Path(__file__).parent
SOURCE = ROOT / "source"
TEMPLATES = SOURCE / "templates"
POETS_SRC = SOURCE / "pages" / "poets"
DOCS = ROOT / "docs"
POETS_OUT = DOCS / "poets"

# Assets copied verbatim so the build output is self-contained
ASSETS_SRC = SOURCE / "assets"
ASSETS_OUT = DOCS / "assets"

# Ensure output directories exist before writing generated files
POETS_OUT.mkdir(parents=True, exist_ok=True)


def load_template(name):
    """Load an HTML template from source/templates."""
    return (TEMPLATES / name).read_text(encoding="utf-8")


def parse_markdown(path):
    """
    Extract YAML frontmatter and optional markdown body.

    Supports:
    - fenced frontmatter (--- yaml --- body)
    - YAML-only files (used for poets)

    The dual format allows flexibility without requiring separate parsers.
    """
    raw = path.read_text(encoding="utf-8").strip()

    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[3:end]
            body = raw[end + 4:]
            front = yaml.safe_load(fm) or {}
        else:
            front = {}
            body = raw
    else:
        # Poet files are YAML-only; failure falls back to empty metadata
        try:
            front = yaml.safe_load(raw) or {}
        except Exception:
            front = {}
        body = ""

    # Markdown conversion retained for future extensibility
    html = markdown.markdown(body, extensions=["fenced_code", "tables"])
    return front, html


def build_poet_pages():
    """
    Render each poet's YAML file into a standalone HTML page.

    Templates are rendered individually so each poet page remains static
    and does not depend on runtime JavaScript or external data.
    """
    poet_template = Template(load_template("poet.html"))
    poets_data = []

    for md_file in sorted(POETS_SRC.glob("*.md")):
        front, _ = parse_markdown(md_file)

        title = front.get("title", md_file.stem.title())
        image = front.get("image")

        page_html = poet_template.render(
            title=title,
            image=image,
            introduction=front.get("introduction"),
            poetry=front.get("poetry"),
            suggested_reading=front.get("suggested_reading"),
        )

        out_path = POETS_OUT / f"{md_file.stem}.html"
        out_path.write_text(page_html, encoding="utf-8")

        # Store metadata for Contents page generation
        poets_data.append({
            "title": title,
            "file": f"poets/{md_file.stem}.html",
            "frontmatter": front
        })

    return poets_data


def build_poets_list(poets_data):
    """
    Build the <ul> list for contents.html.

    Labels combine title, years, and origin when available.
    This keeps the Contents page lightweight without extra logic in templates.
    """
    items = []

    for poet in poets_data:
        title = poet["title"]
        fm = poet["frontmatter"]

        years = fm.get("years")
        origin = fm.get("origin")

        label_parts = [title]
        if years:
            label_parts.append(f"({years})")
        if origin:
            label_parts.append(origin)

        label = " ".join(label_parts)
        items.append(f'<li><a href="{poet["file"]}">{label}</a></li>')

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def build_contents(poets_data):
    """
    Inject the generated poets list into contents.html.

    Using a placeholder avoids mixing template logic with build logic
    and keeps the HTML template clean and static.
    """
    contents_template = load_template("contents.html")
    poets_list_html = build_poets_list(poets_data)

    final = contents_template.replace("<!-- poets_list -->", poets_list_html)
    (DOCS / "contents.html").write_text(final, encoding="utf-8")


def build_preface():
    """
    Preface is static HTML; copied directly to output.
    This avoids unnecessary template rendering.
    """
    preface_template = load_template("preface.html")
    (DOCS / "preface.html").write_text(preface_template, encoding="utf-8")


def build_cover():
    """
    Cover page (index.html) is also static and copied as-is.
    """
    index_template = load_template("index.html")
    (DOCS / "index.html").write_text(index_template, encoding="utf-8")


# Copy assets so the docs/ output is fully self-contained.
# dirs_exist_ok=True ensures incremental builds do not fail.
def copy_assets():
    if ASSETS_SRC.exists():
        shutil.copytree(ASSETS_SRC, ASSETS_OUT, dirs_exist_ok=True)


def main():
    print("Building The Poets Codex...")

    poets_data = build_poet_pages()

    # Sorting by birth year keeps the Contents page historically coherent
    poets_data.sort(key=lambda p: p["frontmatter"].get("years", ""))
   
    build_contents(poets_data)
    build_preface()
    build_cover()
    copy_assets()

    print("Build complete.")


if __name__ == "__main__":
    main()
