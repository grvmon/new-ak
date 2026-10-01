import re
from bs4 import BeautifulSoup

def qc_clean():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    # Split frontmatter
    parts = html.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = '---'.join(parts[2:])
    else:
        frontmatter = ""
        body = html

    soup = BeautifulSoup(body, 'html.parser')

    # 1. Remove duplicate h2s based on text content
    seen_h2 = set()
    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True).lower()
        if text in seen_h2:
            # Duplicate found! Let's remove the parent section if it's a section, or just the h2
            parent = h2.parent
            if parent.name == 'section' or parent.name == 'div':
                print(f"Removing duplicate section: {text}")
                parent.decompose()
            else:
                print(f"Removing duplicate h2: {text}")
                h2.decompose()
        else:
            seen_h2.add(text)

    # 2. Check for duplicate IDs in the entire document
    seen_ids = set()
    for el in soup.find_all(id=True):
        el_id = el['id']
        if el_id in seen_ids:
            print(f"Removing duplicate ID attribute: {el_id}")
            del el['id']
        else:
            seen_ids.add(el_id)

    # Convert soup back to string and write
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

qc_clean()
