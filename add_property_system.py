from bs4 import BeautifulSoup
import re

def add_property_system():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    main_container = soup.find('div', class_=lambda c: c and 'max-w-[1280px]' in c)
    
    if main_container:
        # Create the new section 14
        new_sec = soup.new_tag('section', attrs={'class': 'scroll-mt-16 mb-24 pb-16 border-b-[0.5px] border-[#55555a26]', 'id': '14-property'})
        
        content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">14. Property Design System</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The Asset Dossier is the core of the acre&amp;key experience. It must reject the generic "property listing" format in favor of a rigorous, private-banking style investment memo. We highlight risks just as clearly as benefits.</p>
        
        <div class="space-y-16">
            <!-- Dossier Anatomy -->
            <div>
                <div class="font-sans text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Anatomy of an Asset Dossier</div>
                <div class="border-[0.5px] border-[#55555a26] bg-white p-8 rounded-sm font-sans text-[0.85rem] text-[#55555A]">
                    <ol class="space-y-4 list-decimal list-inside">
                        <li><strong class="text-[#1C1C1E]">Cinematic Hero:</strong> Heavily desaturated architectural render (no blue skies), anchored gradient, minimal text.</li>
                        <li><strong class="text-[#1C1C1E]">Objective Overview:</strong> 3-paragraph maximum. Data-heavy. No marketing fluff ("breathtaking views").</li>
                        <li><strong class="text-[#1C1C1E]">Financials &amp; Typology:</strong> Clean slate tables. Pricing must include all hidden costs.</li>
                        <li><strong class="text-[#1C1C1E]">Architectural Blueprints:</strong> Floorplans and Masterplans behind a gated "Advisory" blur.</li>
                        <li><strong class="text-[#1C1C1E]">Diligence &amp; Risks:</strong> The most important section. RERA status, legal title history, and known infrastructure delays.</li>
                        <li><strong class="text-[#1C1C1E]">Advisory CTA:</strong> Fixed bottom bar or prominent card to schedule a clinical consultation.</li>
                    </ol>
                </div>
            </div>

            <!-- Diligence & Risk Framing -->
            <div>
                <div class="font-sans text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">The Diligence &amp; Risk Framework</div>
                <p class="text-[0.95rem] mb-6 leading-relaxed">Unlike broker portals, we actively display negative signals. Risk factors use our Architectural Semantic Palette to maintain a calm, clinical tone.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="border-[0.5px] border-[#55555a26] p-6 bg-white rounded-sm">
                        <div class="flex items-center gap-3 mb-4">
                            <span class="w-2 h-2 rounded-sm bg-[#8B3A3A]"></span>
                            <span class="font-bold text-[#8B3A3A] uppercase tracking-[0.1em] text-[0.75rem]">Risk Factor Identified</span>
                        </div>
                        <div class="text-[0.95rem] text-[#1C1C1E] font-serif mb-2">Upcoming Infrastructure Delay</div>
                        <div class="text-[0.85rem]">The proposed metro expansion (Phase 3) is currently facing land acquisition hurdles, potentially delaying completion by 18-24 months.</div>
                    </div>
                    <div class="border-[0.5px] border-[#55555a26] p-6 bg-white rounded-sm">
                        <div class="flex items-center gap-3 mb-4">
                            <span class="w-2 h-2 rounded-sm bg-[#A88944]"></span>
                            <span class="font-bold text-[#A88944] uppercase tracking-[0.1em] text-[0.75rem]">Diligence Pending</span>
                        </div>
                        <div class="text-[0.95rem] text-[#1C1C1E] font-serif mb-2">A-Khata Certification</div>
                        <div class="text-[0.85rem]">Legal team is currently verifying the final conversion documents from the BDA. Approval expected within 14 days.</div>
                    </div>
                </div>
            </div>
            
            <!-- Floorplan UI -->
            <div>
                <div class="font-sans text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Floorplan &amp; Typology UI</div>
                <p class="text-[0.95rem] mb-6 leading-relaxed">Floorplans are sensitive intellectual property. They are displayed with a heavy <code>8px</code> blur until the user authenticates.</p>
                <div class="relative w-full h-[300px] border-[0.5px] border-[#55555a26] bg-[#FAFAFA] rounded-sm overflow-hidden flex items-center justify-center group">
                    <div class="absolute inset-0 bg-transparent backdrop-blur-[8px] bg-[#FAFAFA]/50 z-10 flex items-center justify-center">
                        <div class="text-center p-6 bg-white border-[0.5px] border-[#55555a26] shadow-sm max-w-[300px]">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--obsidian-black)" stroke-width="1.5" class="mx-auto mb-4"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Authentication Required</div>
                            <div class="font-sans text-[0.8rem] text-[#55555A] mb-4">Please verify your credentials to access detailed architectural layouts.</div>
                            <button class="w-full py-2 bg-[#1C1C1E] text-white text-[0.75rem] uppercase tracking-[0.1em] hover:bg-[#804526] transition-colors">Request Access</button>
                        </div>
                    </div>
                    <!-- Fake Blueprint background -->
                    <div class="absolute inset-0 opacity-10" style="background-image: linear-gradient(#1C1C1E 1px, transparent 1px), linear-gradient(90deg, #1C1C1E 1px, transparent 1px); background-size: 40px 40px;"></div>
                </div>
            </div>
        </div>
        """, 'html.parser')
        
        new_sec.append(content)
        main_container.append(new_sec)
        
    # Re-sort and re-build navigation
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

add_property_system()
