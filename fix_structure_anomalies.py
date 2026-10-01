from bs4 import BeautifulSoup

def fix_anomalies():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')

    # Fix 1: Structural Pollution (Mock content using H2/H3)
    # 1a. The rogue H2 in Typography
    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        # Any H2 that doesn't start with digits (our strict convention) is mock content
        if not text[0].isdigit():
            h2.name = 'div'
            h2['class'] = h2.get('class', []) + ['text-2xl', 'font-serif'] # Keep visual styling

    # 1b. The rogue H3s in Components and Templates
    # List of known mock content strings that are currently H3s
    mock_h3s = [
        "You know what you want. You just don't have the time to find it.",
        "Location",
        "Clarify",
        "Meet The Team",
        "Floorplan Access",
        "Protected Legibility",
        "Township Data"
    ]
    
    for h3 in soup.find_all('h3'):
        text = h3.get_text(strip=True)
        if text in mock_h3s:
            h3.name = 'div'
            h3['class'] = h3.get('class', []) + ['text-xl', 'font-serif']

    # Fix 2: Misplaced Data (Move Token Map to Color section)
    brand_sec = soup.find(id='01-brand')
    color_sec = soup.find(id='04-color')
    
    if brand_sec and color_sec:
        # Find the H3 for Token Map
        token_h3 = brand_sec.find('h3', string=lambda t: t and 'Token Map & Contrast Matrix' in t)
        if token_h3:
            # The token map is inside a div, or maybe it's just an H3 followed by a table.
            # Let's find its parent if it's wrapped, or extract siblings.
            # Usually my convert script wrapped them in a div.
            parent = token_h3.parent
            if parent.name == 'div' and parent != brand_sec:
                # It's wrapped in a div, move the whole div
                color_sec.insert(2, parent.extract()) # Insert right after the H2 and intro P
            else:
                # Not wrapped, let's extract the H3 and the following table
                table = token_h3.find_next_sibling('table')
                if table:
                    wrapper = soup.new_tag('div', attrs={'class': 'mb-12 mt-12'})
                    wrapper.append(token_h3.extract())
                    wrapper.append(table.extract())
                    color_sec.insert(2, wrapper)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

fix_anomalies()
