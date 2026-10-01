from bs4 import BeautifulSoup
import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('---')
body = '---'.join(parts[2:])
soup = BeautifulSoup(body, 'html.parser')

# 1. Get all Table of Contents links
toc_links = {}
toc_nav = soup.find('nav') # Assuming TOC is in a <nav> or a specific div
if toc_nav:
    links = toc_nav.find_all('a', href=True)
else:
    # Fallback to finding links that start with #
    links = soup.find_all('a', href=re.compile('^#'))

for link in links:
    href = link['href']
    if href.startswith('#'):
        # Store the text of the link
        toc_links[href[1:]] = link.get_text(strip=True)

# 2. Get all Sections (by ID) and check content
sections = {}
for element in soup.find_all(id=True):
    el_id = element['id']
    # Look for the first h2 or h3 inside or as the element itself
    heading = None
    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        heading = element.get_text(strip=True)
    else:
        h = element.find(['h1', 'h2', 'h3', 'h4'])
        if h:
            heading = h.get_text(strip=True)
            
    # Check if content is placeholder or empty
    text_content = element.get_text(strip=True).lower()
    is_empty = False
    if "content coming soon" in text_content or "to be defined" in text_content or len(text_content) < 100:
        is_empty = True
        
    sections[el_id] = {
        'heading': heading,
        'is_empty': is_empty,
        'text_length': len(text_content)
    }

print("=== TABLE OF CONTENTS vs SECTIONS ===")
broken_links = []
unlinked_sections = []
empty_sections = []

for toc_id, toc_text in toc_links.items():
    if toc_id not in sections:
        broken_links.append(f"Broken Link in TOC: '{toc_text}' -> #{toc_id} (Section does not exist)")
    else:
        if sections[toc_id]['is_empty']:
            empty_sections.append(f"Empty/Placeholder Section: '{toc_text}' (#{toc_id})")

for sec_id, data in sections.items():
    # Only care about major sections like '01-', '02-', etc.
    if re.match(r'^\d{2}-', sec_id):
        if sec_id not in toc_links:
            unlinked_sections.append(f"Unlinked Section in Document: '{data['heading']}' (#{sec_id})")
        if data['is_empty'] and f"Empty/Placeholder Section: '{data['heading']}' (#{sec_id})" not in empty_sections:
            empty_sections.append(f"Empty/Placeholder Section: '{data['heading']}' (#{sec_id})")

print("\n--- BROKEN LINKS (In TOC but missing in document) ---")
for x in broken_links: print(x)

print("\n--- UNLINKED SECTIONS (In document but missing in TOC) ---")
for x in unlinked_sections: print(x)

print("\n--- EMPTY / PLACEHOLDER SECTIONS ---")
for x in empty_sections: print(x)

