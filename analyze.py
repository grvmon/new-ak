from bs4 import BeautifulSoup

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("--- SECTIONS & CORE RULES ---")
for section in soup.find_all('section'):
    h2 = section.find('h2')
    if not h2: continue
    
    title = h2.get_text(strip=True)
    print(f"\n# {title}")
    
    # Extract strong text or bullet points as "rules"
    rules = section.find_all(['strong', 'li', 'h3', 'h4'])
    for r in rules[:15]: # just sample the first 15 key points per section to find duplicates
        text = r.get_text(strip=True)[:100].replace('\n', ' ')
        if len(text) > 5:
            print(f"- {text}")
