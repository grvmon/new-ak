from bs4 import BeautifulSoup
import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('---')
body = '---'.join(parts[2:])

soup = BeautifulSoup(body, 'html.parser')

sections = soup.find_all('section')
empty_sections = []

for sec in sections:
    sec_id = sec.get('id', 'No ID')
    # If the section has very few elements or short text
    text_content = sec.get_text(strip=True)
    if len(text_content) < 150: # Arbitrary small number, empty ones usually just have "17. Social Media"
        empty_sections.append(f"{sec_id}: {text_content}")
    elif len(sec.find_all('div')) < 2: # Also a good indicator of an un-audited section
        empty_sections.append(f"{sec_id} (Low div count): {text_content[:100]}...")

for e in empty_sections:
    print(e)

