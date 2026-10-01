from bs4 import BeautifulSoup
import re

def fix():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # 1. Remove broken links completely
    for a in soup.find_all('a', href=True):
        if a['href'].endswith('.html'):
            a.decompose()
            
    # Remove any empty <p> tags or orphaned text that might have wrapped those links
    for p in soup.find_all('p'):
        if not p.get_text(strip=True):
            p.decompose()

    # 2. Extract sections and sort them
    # We find all h2s. We then take their parent (which should be the section or div).
    # We will remove them from the main container, sort them by the number in the H2, and append them back.
    
    main_container = soup.find('main')
    
    sections_to_sort = []
    
    for h2 in main_container.find_all('h2'):
        text = h2.get_text(strip=True)
        # Find the number prefix
        match = re.search(r'^(\d+)\.', text)
        if match:
            num = int(match.group(1))
            # Get the parent element that wraps this entire section
            parent = h2.parent
            # We want to extract it completely from the DOM
            parent.extract()
            sections_to_sort.append((num, text, parent))

    # Sort by the extracted number
    sections_to_sort.sort(key=lambda x: x[0])
    
    # Append them back to main_container in correct order
    for num, text, node in sections_to_sort:
        main_container.append(node)

    # 3. Update the sidemenu dynamically based on the sorted sections
    nav = soup.find('nav', class_=lambda c: c and 'sticky' in c)
    if nav:
        nav.clear()
        
        # Categorize
        foundations = []
        systems = []
        
        for num, text, node in sections_to_sort:
            href_id = node.get('id')
            if not href_id:
                # Fallback generate ID
                href_id = f"section-{num}"
                node['id'] = href_id
                
            link = (f"#{href_id}", text)
            if num <= 6:
                foundations.append(link)
            else:
                systems.append(link)
                
        # Append Foundations
        if foundations:
            group_div = soup.new_tag('div', attrs={'class': 'mt-6 mb-2 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]'})
            group_div.string = "Foundations"
            nav.append(group_div)
            for href, text in foundations:
                a = soup.new_tag('a', href=href, attrs={'class': 'block py-2 text-[0.85rem] text-[#55555A] hover:text-[#804526] transition-colors'})
                a.string = text
                nav.append(a)

        # Append Systems
        if systems:
            group_div = soup.new_tag('div', attrs={'class': 'mt-8 mb-2 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]'})
            group_div.string = "Systems"
            nav.append(group_div)
            for href, text in systems:
                a = soup.new_tag('a', href=href, attrs={'class': 'block py-2 text-[0.85rem] text-[#55555A] hover:text-[#804526] transition-colors'})
                a.string = text
                nav.append(a)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

fix()
