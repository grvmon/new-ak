from bs4 import BeautifulSoup

def build_skeleton():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])
    soup = BeautifulSoup(body, 'html.parser')
    main_container = soup.find('div', class_=lambda c: c and 'max-w-[1280px]' in c)

    # The definitive 30-point list mapped to groups
    structure = [
        ("Brand", [
            ("00. Governance", "00-governance"),
            ("01. Brand Foundation", "01-brand")
        ]),
        ("Language", [
            ("02. Verbal Identity", "02-verbal")
        ]),
        ("Visual Identity", [
            ("03. Logo & Identity", "03-logo"),
            ("04. Color", "04-color"),
            ("05. Typography", "05-typography")
        ]),
        ("Layout", [
            ("06. Grid & Layout", "06-grid"),
            ("07. Responsive System", "07-responsive")
        ]),
        ("Visual Assets", [
            ("08. Photography & Art Direction", "08-photography"),
            ("09. Graphic Language", "09-graphic"),
            ("10. Iconography", "10-iconography")
        ]),
        ("Interaction", [
            ("11. Motion", "11-motion")
        ]),
        ("Components", [
            ("12. Component Library", "12-components"),
            ("13. Forms & Advisory UX", "13-forms")
        ]),
        ("Business/Product", [
            ("14. Property Design System", "14-property"),
            ("15. Data Visualization", "15-data"),
            ("16. Maps & Location", "16-maps")
        ]),
        ("Content", [
            ("17. Social Media", "17-social"),
            ("18. Paid Advertising", "18-paid"),
            ("19. Video Identity", "19-video"),
            ("20. Editorial System", "20-editorial"),
            ("21. Reports & Dossiers", "21-reports")
        ]),
        ("Technical", [
            ("22. SEO Design System", "22-seo"),
            ("23. Accessibility", "23-accessibility"),
            ("24. Trust & Compliance", "24-trust"),
            ("25. Developer Design Tokens", "25-tokens"),
            ("26. Next.js / Frontend Rules", "26-nextjs"),
            ("27. CMS Architecture", "27-cms")
        ]),
        ("Templates", [
            ("28. Page Templates", "28-templates")
        ]),
        ("QA", [
            ("29. QA & Governance", "29-qa")
        ])
    ]

    # First, let's extract all EXISTING sections and store them by their prefix number
    existing_sections = {}
    for h2 in main_container.find_all('h2'):
        text = h2.get_text(strip=True)
        # Handle the fact that some might be '00.' or '01.' or '2.'
        prefix = text.split('.')[0].zfill(2) # e.g. '00', '01', '14'
        parent = h2.parent
        if parent.name in ['section', 'div']:
            parent.extract()
            existing_sections[prefix] = parent

    # Now we iterate over the exact structure and append back to main_container
    for group_name, items in structure:
        for title, id_str in items:
            prefix = title.split('.')[0] # '00', '01', '29'
            
            if prefix in existing_sections:
                # We have it! Just ensure the H2 title perfectly matches the new list and ID is correct
                node = existing_sections[prefix]
                h2 = node.find('h2')
                if h2:
                    h2.string = title
                node['id'] = id_str
                main_container.append(node)
            else:
                # We don't have it! Create a placeholder section
                new_sec = soup.new_tag('section', attrs={'class': 'scroll-mt-16 mb-24 pb-16 border-b-[0.5px] border-[#55555a26]', 'id': id_str})
                
                content = BeautifulSoup(f"""
                <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">{title}</h2>
                <div class="mt-8 p-6 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] border-dashed rounded-sm flex items-center justify-center">
                    <span class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#55555A]">System Component Pending Architecture</span>
                </div>
                """, 'html.parser')
                new_sec.append(content)
                main_container.append(new_sec)

    # Finally, rebuild the sidebar exactly according to the groups
    nav = soup.find('nav', class_=lambda c: c and 'sticky' in c)
    if nav:
        nav.clear()
        
        for group_name, items in structure:
            group_div = soup.new_tag('div', attrs={'class': 'mt-8 first:mt-2 mb-3 text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#804526] border-b-[0.5px] border-[#55555a26] pb-2'})
            group_div.string = group_name
            nav.append(group_div)
            
            for title, id_str in items:
                # Strip the number off for the sidebar to make it super clean, or keep it? 
                # The user pasted it WITH numbers. Let's keep the numbers.
                a = soup.new_tag('a', href=f"#{id_str}", attrs={'class': 'block py-1.5 text-[0.8rem] text-[#55555A] hover:text-[#804526] transition-colors truncate'})
                a.string = title
                nav.append(a)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

build_skeleton()
