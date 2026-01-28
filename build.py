import os
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

# Load templates
env = Environment(loader=FileSystemLoader("source/templates"))

# ---------------------------------------------------------
# Robust YAML front‑matter parser
# ---------------------------------------------------------
def parse_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    front = {}
    body = raw

    # Detect front matter safely
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm = raw[3:end]               # YAML block
            body = raw[end + 4:]          # skip closing '---\n'
            front = yaml.safe_load(fm) or {}

    html = markdown.markdown(body)
    return front, html


# ---------------------------------------------------------
# Build normal pages (index, about, etc.)
# ---------------------------------------------------------
def build_page(src, dest, template_name="page.html"):
    front, html = parse_markdown(f"source/pages/{src}")
    title = front.get("title") or src.replace(".md", "").title()

    template = env.get_template(template_name)
    rendered = template.render(
        title=title,
        content=html,
        template=template_name
    )

    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(rendered)


# ---------------------------------------------------------
# Build individual poet pages + collect metadata
# ---------------------------------------------------------
def build_poets():
    poets = []
    poets_src = "source/pages/poets"

    for filename in os.listdir(poets_src):
        if not filename.endswith(".md"):
            continue

        # Skip index.md inside poets/
        if filename == "index.md":
            continue

        poet_id = filename.replace(".md", "")
        src_path = os.path.join(poets_src, filename)

        front, html = parse_markdown(src_path)

        title = front.get("title", poet_id.title())
        image = front.get("image")
        palette = front.get("palette", [])

        poets.append({
            "id": poet_id,
            "name": title,
            "image": image,
            "palette": palette
        })

        template = env.get_template("poet.html")
        rendered = template.render(
            title=title,
            content=html,
            image=image,
            palette=palette,
            template="poet.html"
        )

        dest = f"docs/poets/{poet_id}/index.html"
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(rendered)

    return poets


# ---------------------------------------------------------
# Build poets index page
# ---------------------------------------------------------
def build_poets_index(poets):
    template = env.get_template("poets.html")
    rendered = template.render(
        title="Poets",
        poets=poets,
        template="poets.html"
    )

    dest = "docs/poets/index.html"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(rendered)


# ---------------------------------------------------------
# Main build
# ---------------------------------------------------------
def main():
    print("Building pages...")

    build_page("index.md", "docs/index.html")
    build_page("about.md", "docs/about/index.html")

    poets = build_poets()
    build_poets_index(poets)

    print("Build complete.")


if __name__ == "__main__":
    main()
