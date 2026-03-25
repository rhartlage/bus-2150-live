from pathlib import Path
import html

repo = Path(".")
modules_dir = repo / "modules"
out_file = repo / "index.html"

cards = []
if modules_dir.exists():
    for p in sorted(modules_dir.iterdir()):
        if p.is_dir() and (p / "index.html").exists():
            name = p.name.replace("-", " ").title()
            href = f"./modules/{p.name}/"
            cards.append((name, href))

items = "\n".join(
    f'<li><a href="{html.escape(href)}">{html.escape(name)}</a></li>'
    for name, href in cards
) or "<li>No tools found yet.</li>"

html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BUS-2150 Tools</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem; }}
    h1 {{ margin-bottom: .5rem; }}
    ul {{ line-height: 2; }}
    a {{ text-decoration: none; color: #1f4fd6; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>BUS-2150 Course Tools</h1>
  <p>Select a tool:</p>
  <ul>
    {items}
  </ul>
</body>
</html>"""

out_file.write_text(html_doc, encoding="utf-8")
print(f"Generated {out_file} with {len(cards)} tool(s).")
