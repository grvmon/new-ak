from bs4 import BeautifulSoup
import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('---')
body = '---'.join(parts[2:]) if len(parts) >= 3 else html
soup = BeautifulSoup(body, 'html.parser')

print("--- H2 and H3 Outline ---")
for tag in soup.find_all(['h2', 'h3']):
    print(f"{tag.name.upper()}: {tag.get_text(strip=True)[:80]}")

print("\n--- Identifying Potential Anomalies ---")
# Check for empty sections
for sec in soup.find_all('section'):
    if not sec.get_text(strip=True):
        print(f"Empty section found: {sec.get('id', 'No ID')}")

# Check for placeholder text (lorem ipsum, etc.)
if 'lorem' in body.lower():
    print("Found 'Lorem Ipsum' placeholder text.")

# Check for broken image links or placeholder images
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'placeholder' in src or src.startswith('#') or src == '':
        print(f"Suspicious image source: {src}")

