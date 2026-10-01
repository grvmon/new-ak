from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])
    soup = BeautifulSoup(body, 'html.parser')
    
    # We are looking for "03. The Thoughtful Buyer"
    target = soup.find(string=re.compile("03. The Thoughtful Buyer"))
    if target:
        container = target.parent.parent.parent
        
        gradient_layer = None
        for div in container.find_all('div'):
            if 'bg-gradient-to-t' in div.get('class', []):
                gradient_layer = div
                break
                
        if gradient_layer:
            # Current: absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/90 to-transparent h-[85%] mt-auto
            # Change to: absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/60 to-transparent h-[70%] mt-auto
            classes = gradient_layer.get('class', [])
            
            if 'via-[#1C1C1E]/90' in classes:
                classes.remove('via-[#1C1C1E]/90')
                classes.append('via-[#1C1C1E]/60')
                
            if 'h-[85%]' in classes:
                classes.remove('h-[85%]')
                classes.append('h-[70%]')
                
            gradient_layer['class'] = classes

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Fixed native card gradient.")

update()
