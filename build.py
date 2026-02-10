import os
import markdown
import yaml
from pathlib import Path

# paths
ROOT = Path(__file__).parent
SOURCE = ROOT / "source"
TEMPLATES = SOURCE / "templates"
POETS_SRC = SOURCE / "pages" / "poets"
DOCS = ROOT / "docs"
POETS_OUT = DOCS / "poets"

# ensure output directories exist
POETS_OUT.mkdir(parents=True, exist_ok=True)


def load_template(name):
    """load an html template from source/templates"""
    return (TEMPLATES / name).read_text(encoding="utf-8")


def parse_markdown(path):
    """extract yaml frontmatter + markdown content"""
    raw = path.read_text(encoding="utf-8").strip()

    front = {}
    body = raw

    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[3:end]
            body = raw[end + 4:]
            front = yaml.safe_load(fm) or {}

    html = markdown.markdown(body, extensions=["fenced_code", "tables"])
    return front, html


def build_poet_pages():
    """convert each poet markdown file into a full html page"""
    poet_template = load_template("poet.html")
    poets_data = []

    for md_file in sorted(POETS_SRC.glob("*.md")):
        front, html_content = parse_markdown(md_file)

        title = front.get("title", md_file.stem.title())
        image = front.get("image", None)

        # inject into template
        page_html = poet_template.replace("{{ title }}", title)
        page_html = page_html.replace("{{ content }}", html_content)

        if image:
            page_html = page_html.replace("{{ image }}", image)
        else:
            page_html = page_html.replace("{{ image }}", "")

        # write output
        out_path = POETS_OUT / f"{md_file.stem}.html"
        out_path.write_text(page_html, encoding="utf-8")

        # store metadata for poets list
        poets_data.append({
            "title": title,
            "file": f"poets/{md_file.stem}.html",
            "frontmatter": front
        })

    return poets_data


def build_poets_list(poets_data):
    """generate the <ul> list for the hub page"""
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


def build_hub(poets_data):
    """inject poets list into hub.html"""
    hub_template = load_template("hub.html")
    poets_list_html = build_poets_list(poets_data)

    final = hub_template.replace("<!-- poets_list -->", poets_list_html)
    (DOCS / "hub.html").write_text(final, encoding="utf-8")


def build_cover():
    """copy index.html directly into docs"""
    index_template = load_template("index.html")
    (DOCS / "index.html").write_text(index_template, encoding="utf-8")


def main():
    print("Building The Poets Codex...")

    poets_data = build_poet_pages()
    build_hub(poets_data)
    build_cover()

    print("Build complete.")


if __name__ == "__main__":
    main()
