from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    # Simply do a string replacement since it's a very unique string in the file
    body = body.replace('Find. Check. Inspect.<br/>Negotiate. Decide.', 'Find. Inspect.<br/>Negotiate. Decide.')

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{body}")

update()
