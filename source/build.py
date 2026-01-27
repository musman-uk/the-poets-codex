import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Load templates
env = Environment(loader=FileSystemLoader("source/templates"))

# Pages to generate
pages = [
    ("index.md", "docs/index.html"),
    ("about.md", "docs/about.html"),
    ("poets.md", "docs/poets/index.html"),
]

for src, dest in pages:
    # Read Markdown
    with open(f"source/content/{src}", "r", encoding="utf-8") as f:
        raw = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(raw)

    # Extract title from first heading
    title = raw.splitlines()[0].replace("#", "").strip()

    # Render using template
    template = env.get_template("page.html")
    rendered = template.render(title=title, content=html_content)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    # Write final HTML
    with open(dest, "w", encoding="utf-8") as f:
        f.write(rendered)

print("Build complete.")
