import re
from bs4 import BeautifulSoup, NavigableString

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()
        
    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])
    
    soup = BeautifulSoup(body, 'html.parser')
    pattern = re.compile(r'(?i)acre\s*(?:&|&amp;)\s*key')
    
    # We collect nodes first to avoid modifying the tree while iterating
    target_nodes = []
    for text_node in soup.find_all(string=pattern):
        parent = text_node.parent
        if parent is None:
            continue
        if parent.name in ['title', 'style', 'script', 'code']:
            continue
        if parent.name == 'span' and 'font-logo' in parent.get('class', []):
            if str(text_node).strip().lower() != 'acre&key':
                # Replace content of span safely
                pass # We'll handle this in string replace later
            continue
        target_nodes.append(text_node)
        
    for text_node in target_nodes:
        # We replace the text node with parsed HTML containing the span
        replaced_str = pattern.sub(r'<span class="font-logo lowercase">acre&amp;key</span>', str(text_node))
        new_soup = BeautifulSoup(replaced_str, 'html.parser')
        text_node.replace_with(new_soup)

    # Convert back to string and ensure any existing <span class="font-logo">Acre&Key</span> are lowercased
    final_body = str(soup)
    # Just in case there are <span class="font-logo">Acre&amp;Key</span>
    
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{final_body}")
    print("Replaced successfully.")

update()
