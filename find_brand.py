from bs4 import BeautifulSoup
import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Using regex to find all text nodes containing the brand name (case insensitive, ignoring spacing variations if needed)
pattern = re.compile(r'acre\s*&\s*key', re.IGNORECASE)

soup = BeautifulSoup(html, 'html.parser')
texts = soup.find_all(string=pattern)

for t in texts:
    print(repr(t))

