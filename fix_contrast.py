from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])
    soup = BeautifulSoup(body, 'html.parser')
    
    target = soup.find(string=re.compile("03. The Thoughtful Buyer"))
    if target:
        container = target.parent.parent.parent
        
        gradient_layer = None
        for div in container.find_all('div'):
            if 'bg-gradient-to-t' in div.get('class', []):
                gradient_layer = div
                break
                
        if gradient_layer:
            # Change to: bg-gradient-to-t from-[#1C1C1E] from-40% via-[#1C1C1E]/80 via-75% to-transparent h-[85%] mt-auto
            # This creates a hard contrast floor for the text, while strictly protecting the top 15-25%
            gradient_layer['class'] = "absolute inset-0 bg-gradient-to-t from-[#1C1C1E] from-40% via-[#1C1C1E]/80 via-75% to-transparent h-[85%] mt-auto".split()

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Fixed contrast gradient.")

update()
