from bs4 import BeautifulSoup
import re

def fix():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')

    # 1. Fix the Iconography section
    h3_icon = soup.find('h3', string=lambda t: t and '5.5 Iconography Guidelines' in t)
    if h3_icon:
        h3_icon.name = 'h2'
        h3_icon.string = "10. Iconography"
        h3_icon['class'] = ['font-serif', 'text-2xl', 'font-normal', 'text-[#1C1C1E]', 'mb-2']
        
        parent_div = h3_icon.parent
        if parent_div.name == 'div':
            parent_div.name = 'section'
            parent_div['class'] = ['scroll-mt-16', 'mb-24', 'pb-16', 'border-b-[0.5px]', 'border-[#55555a26]']
            parent_div['id'] = '10-iconography'

        paragraphs = parent_div.find_all('p')
        for p in paragraphs:
            if 'Icons must be purely functional' in p.get_text():
                icons_container = p.find_next_sibling('div')
                if icons_container:
                    icons_container['class'] = ['flex', 'flex-wrap', 'gap-12', 'mt-12', 'p-8', 'border-[0.5px]', 'border-[#55555a26]', 'bg-white', 'rounded-sm']
                    for icon_div in icons_container.find_all('div', recursive=False):
                        icon_div['class'] = ['flex', 'flex-col', 'items-center', 'justify-center', 'gap-4', 'min-w-[80px]']
                        span = icon_div.find('span')
                        if span:
                            span['class'] = ['font-sans', 'text-[0.75rem]', 'uppercase', 'tracking-[0.12em]', 'text-[#55555A]', 'font-bold']
    
    # 2. Add Missing Components to Component Library (Section 12)
    lib_sec = soup.find(id='12-components')
    if lib_sec:
        new_components = BeautifulSoup("""
        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-16 mb-4">Architectural Map (Google Maps)</h3>
        <p class="font-sans text-[0.95rem] text-[#55555A] mb-8 leading-relaxed">Map embeds must be completely desaturated via CSS filters to maintain the editorial aesthetic. No bright primary colors.</p>
        <div class="w-full h-[400px] border-[0.5px] border-[#55555a26] bg-[#FAFAFA] rounded-sm overflow-hidden grayscale contrast-[1.05] relative flex items-center justify-center">
            <!-- Simulated Map -->
            <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#1C1C1E 1px, transparent 1px); background-size: 20px 20px;"></div>
            <div class="z-10 flex flex-col items-center gap-2">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--obsidian-black)" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <span class="font-sans text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] bg-white px-3 py-1 border-[0.5px] border-[#55555a26]">Project Site</span>
            </div>
        </div>

        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-16 mb-4">Diligence Endorsements (Testimonials)</h3>
        <p class="font-sans text-[0.95rem] text-[#55555A] mb-8 leading-relaxed">Reject generic bubbly quote cards. Endorsements are formatted as editorial citations with hairline borders and strict typography.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="p-8 border-[0.5px] border-[#55555a26] bg-white rounded-sm">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--primary-copper)" stroke-width="1.5" class="mb-6"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"></path><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.99c1.031 0 1.01 0 1.01 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"></path></svg>
                <p class="font-serif text-[1.1rem] leading-relaxed text-[#1C1C1E] mb-8">"The level of transparency in their diligence report completely redefined my understanding of the asset. No fluff, just pure architectural facts."</p>
                <div class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#55555A]">
                    <strong class="text-[#1C1C1E]">Director, </strong> Tier-1 Bank
                </div>
            </div>
        </div>

        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-16 mb-4">Titles &amp; Section Separators</h3>
        <p class="font-sans text-[0.95rem] text-[#55555A] mb-8 leading-relaxed">Sections are separated strictly by a 0.5px neutral hairline. The title must be anchored flush-left.</p>
        <div class="w-full border-t-[0.5px] border-[#55555a26] pt-12 mt-12">
            <div class="font-sans text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">02. The Architecture</div>
            <h4 class="font-serif text-2xl font-normal text-[#1C1C1E]">Structural Layouts</h4>
        </div>
        
        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-16 mb-4">Minimalist Social Icons</h3>
        <p class="font-sans text-[0.95rem] text-[#55555A] mb-8 leading-relaxed">No generic blue Facebook logos. Social links use our strict 2px uncoated SVG strokes.</p>
        <div class="flex gap-6">
            <a href="#" class="text-[#55555A] hover:text-[#804526] transition-colors"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
            <a href="#" class="text-[#55555A] hover:text-[#804526] transition-colors"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
            <a href="#" class="text-[#55555A] hover:text-[#804526] transition-colors"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
        </div>
        """, 'html.parser')
        lib_sec.append(new_components)
        
    main_container = soup.find('div', class_=lambda c: c and 'max-w-[1280px]' in c)
    sections_to_sort = []
    
    for h2 in main_container.find_all('h2'):
        text = h2.get_text(strip=True)
        match = re.search(r'^(\d+)\.', text)
        if match:
            num = int(match.group(1))
            parent = h2.parent
            if parent.name in ['section', 'div']:
                parent.extract()
                sections_to_sort.append((num, text, parent))

    sections_to_sort.sort(key=lambda x: x[0])
    
    for num, text, node in sections_to_sort:
        main_container.append(node)

    nav = soup.find('nav', class_=lambda c: c and 'sticky' in c)
    if nav:
        nav.clear()
        foundations = []
        systems = []
        for num, text, node in sections_to_sort:
            href_id = node.get('id')
            if not href_id:
                href_id = f"section-{num}"
                node['id'] = href_id
                
            link = (f"#{href_id}", text)
            if num <= 6:
                foundations.append(link)
            else:
                systems.append(link)
                
        if foundations:
            group_div = soup.new_tag('div', attrs={'class': 'mt-6 mb-2 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]'})
            group_div.string = "Foundations"
            nav.append(group_div)
            for href, text in foundations:
                a = soup.new_tag('a', href=href, attrs={'class': 'block py-2 text-[0.85rem] text-[#55555A] hover:text-[#804526] transition-colors'})
                a.string = text
                nav.append(a)

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
