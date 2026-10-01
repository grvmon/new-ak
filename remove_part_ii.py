from bs4 import BeautifulSoup

def remove_part_ii():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # Search for the exact text and extract its parent container
    for div in soup.find_all('div', attrs={'role': 'heading'}):
        if 'Part II: The Component Library' in div.get_text():
            parent = div.parent
            if parent:
                parent.extract()
            else:
                div.extract()

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

remove_part_ii()
