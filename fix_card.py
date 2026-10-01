from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    kicker = soup.find(string=re.compile("Copper Kicker"))
    # The kicker we want is the one that says "Headline in Titanium Frost"
    for heading in soup.find_all(string=re.compile("Headline in Titanium Frost")):
        # Get the container
        container = heading.parent.parent.parent
        
        # We find the image layer
        # <div class="absolute inset-0 opacity-60 bg-[url('...')]...">
        # We need to remove opacity-60 and let it be 100%
        # The background #1C1C1E layer can stay as a fallback, but image should be opacity-100
        
        image_layer = None
        for div in container.find_all('div'):
            if 'bg-[url' in div.get('class', []):
                pass
            if any('bg-[url' in c for c in div.get('class', [])):
                image_layer = div
                break
                
        if image_layer:
            classes = image_layer.get('class', [])
            if 'opacity-60' in classes:
                classes.remove('opacity-60')
                image_layer['class'] = classes
                
        # We find the gradient layer
        # <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent"></div>
        gradient_layer = None
        for div in container.find_all('div'):
            if 'bg-gradient-to-t' in div.get('class', []):
                gradient_layer = div
                break
                
        if gradient_layer:
            # Change classes to make it cover only bottom 85% and be darker
            classes = gradient_layer.get('class', [])
            classes.append('h-[85%]')
            classes.append('mt-auto')
            
            # replace via-[#1C1C1E]/50 with via-[#1C1C1E]/80 for better text readability
            if 'via-[#1C1C1E]/50' in classes:
                classes.remove('via-[#1C1C1E]/50')
                classes.append('via-[#1C1C1E]/90')
            gradient_layer['class'] = classes

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Fixed image card.")

update()
