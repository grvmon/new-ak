from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])
    
    # Replace simple ellipses in text
    body = body.replace('...', '…')
    
    # Replace focus outline stuff in Tailwind classes
    body = body.replace('focus:outline-none focus:border-[#1C1C1E] focus:ring-0', 'outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#1C1C1E]')
    body = body.replace('focus:outline-none focus:border-[#8B3A3A]', 'outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#8B3A3A]')

    soup = BeautifulSoup(body, 'html.parser')

    # Add aria-hidden to decorative SVGs
    for svg in soup.find_all('svg'):
        if not svg.has_attr('aria-label') and not svg.has_attr('aria-labelledby'):
            svg['aria-hidden'] = 'true'
            
    # Fix forms - id/for and autocomplete
    for i, input_tag in enumerate(soup.find_all('input')):
        if input_tag.get('type') == 'checkbox': continue
        
        # Give it an ID
        in_id = f"input-gen-{i}"
        input_tag['id'] = in_id
        
        # Find the preceding label
        label = input_tag.find_previous('label')
        if label:
            label['for'] = in_id
            
        # Add autocomplete
        if 'Legal Name' in (label.get_text() if label else ''):
            input_tag['autocomplete'] = 'name'
        elif 'Phone' in (label.get_text() if label else ''):
            input_tag['autocomplete'] = 'tel'
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Vercel Guideline fixes applied.")

update()
