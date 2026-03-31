import os
import yaml
import markdown
from pathlib import Path
from jinja2 import Template
import shutil  # ← ADDED

# paths
ROOT = Path(__file__).parent
SOURCE = ROOT / "source"
TEMPLATES = SOURCE / "templates"
POETS_SRC = SOURCE / "pages" / "poets"
DOCS = ROOT / "docs"
POETS_OUT = DOCS / "poets"

ASSETS_SRC = SOURCE / "assets"        # ← ADDED
ASSETS_OUT = DOCS / "assets"          # ← ADDED

# ensure output directories exist
POETS_OUT.mkdir(parents=True, exist_ok=True)


def load_template(name):
    """Load an HTML template from source/templates."""
    return (TEMPLATES / name).read_text(encoding="utf-8")


def parse_markdown(path):
    """
    Extract YAML frontmatter + markdown body.
    Supports both:
    ---
    yaml
    ---
    body
    and pure YAML-only files (your current format).
    """
    raw = path.read_text(encoding="utf-8").strip()

    # If file starts with '---', treat it as fenced frontmatter
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
        # Pure YAML-only file (your current poet format)
        try:
            front = yaml.safe_load(raw) or {}
        except Exception:
            front = {}
        body = ""

    # Convert markdown body to HTML (not used for poets anymore)
    html = markdown.markdown(body, extensions=["fenced_code", "tables"])
    return front, html


def build_poet_pages():
    """Convert each poet markdown file into a full HTML page."""
    poet_template = Template(load_template("poet.html"))
    poets_data = []

    for md_file in sorted(POETS_SRC.glob("*.md")):
        front, _ = parse_markdown(md_file)

        title = front.get("title", md_file.stem.title())
        image = front.get("image")

        # Render template with updated YAML fields
        page_html = poet_template.render(
            title=title,
            image=image,
            introduction=front.get("introduction"),
            poetry=front.get("poetry"),
            suggested_reading=front.get("suggested_reading")
        )

        # Write output
        out_path = POETS_OUT / f"{md_file.stem}.html"
        out_path.write_text(page_html, encoding="utf-8")

        # Store metadata for contents list
        poets_data.append({
            "title": title,
            "file": f"poets/{md_file.stem}.html",
            "frontmatter": front
        })

    return poets_data


def build_poets_list(poets_data):
    """Generate the <ul> list for contents.html."""
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

        label = ", ".join(label_parts)
        items.append(f'<li><a href="{poet["file"]}">{label}</a></li>')

    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def build_contents(poets_data):
    """Inject poets list into contents.html."""
    contents_template = load_template("contents.html")
    poets_list_html = build_poets_list(poets_data)

    final = contents_template.replace("<!-- poets_list -->", poets_list_html)
    (DOCS / "contents.html").write_text(final, encoding="utf-8")


def build_preface():
    """Copy preface.html directly into docs."""
    preface_template = load_template("preface.html")
    (DOCS / "preface.html").write_text(preface_template, encoding="utf-8")


def build_cover():
    """Copy index.html directly into docs."""
    index_template = load_template("index.html")
    (DOCS / "index.html").write_text(index_template, encoding="utf-8")


# -----------------------------
# ADDED: Copy assets directory
# -----------------------------
def copy_assets():
    if ASSETS_SRC.exists():
        shutil.copytree(ASSETS_SRC, ASSETS_OUT, dirs_exist_ok=True)


def main():
    print("Building The Poets Codex...")

    poets_data = build_poet_pages()
    build_contents(poets_data)
    build_preface()
    build_cover()
    copy_assets()   # ← ADDED

    print("Build complete.")


if __name__ == "__main__":
    main()
