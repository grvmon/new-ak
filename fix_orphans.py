from bs4 import BeautifulSoup

def fix():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    components_sec = soup.find(id='12-components')
    templates_sec = soup.find(id='29-templates')

    # Find all h3 tags in the main container
    main_container = soup.find('div', class_=lambda c: c and 'max-w-[1280px]' in c)
    
    for h3 in main_container.find_all('h3'):
        text = h3.get_text(strip=True)
        # Skip if already properly nested
        parent = h3.parent
        if parent == components_sec or parent == templates_sec:
            continue
            
        # Is it in an orphaned section?
        if parent.name in ['section', 'div'] and parent.parent == main_container and not parent.find('h2'):
            # It's an orphaned container!
            # Let's decide where it belongs based on text
            if any(t in text for t in ["Editorial Data", "Editorial Process", "Executive Team", "Cinematic Gallery", "Advisory Calculator"]):
                # Move to templates
                if templates_sec:
                    templates_sec.append(parent.extract())
            elif any(t in text for t in ["Token Map", "Comprehensive Type", "Grid Architecture", "Section Theming", "Spatial & Layout"]):
                # Already in foundations (04, 05, 06)
                pass 
            elif "5.5 Iconography" in text:
                pass
            else:
                # Move to components
                if components_sec:
                    components_sec.append(parent.extract())

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

fix()
