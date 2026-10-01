from bs4 import BeautifulSoup
import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('---')
body = '---'.join(parts[2:])
soup = BeautifulSoup(body, 'html.parser')

print("--- TOC LINKS ---")
links = soup.find_all('a', href=re.compile('^#'))
for link in links:
    href = link['href']
    if re.match(r'^#\d{2}-', href):
        print(f"TOC: {href} -> {link.get_text(strip=True)}")

print("\n--- ACTUAL SECTIONS ---")
for element in soup.find_all(id=re.compile(r'^\d{2}-')):
    el_id = element['id']
    h2 = element.find('h2')
    heading = h2.get_text(strip=True) if h2 else "NO H2 FOUND"
    print(f"SEC: #{el_id} -> {heading}")

