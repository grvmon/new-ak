from bs4 import BeautifulSoup
import re

def qc_reorder():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')

    # Mapping of old H2 text to new H2 text (based on 30-point mandate)
    h2_map = {
        "0. Governance & Versioning": "00. Governance",
        "14. Governance & Contribution": "DELETE",  # duplicate
        "01. Brand Foundation (P0)": "01. Brand Foundation",
        "2. Clinical Lexicon & Tone": "02. Verbal Identity",
        "4. Identity & Logo Architecture": "03. Logo & Identity",
        "3. WCAG AAA Color Palette": "04. Color",
        "5. Typography Hierarchy & Guidelines": "05. Typography",
        "4. Layout & Spacing": "06. Grid & Layout",
        "8. Photographic Art Direction": "08. Photography & Art Direction",
        "7. Geometry & Motion Physics": "11. Motion",
        "9. Components & Inputs": "12. Component Library",
        "8. Data & Tools": "15. Data Visualization",
        "11. Templates & Patterns": "29. Page Templates",
        "12. Accessibility Standards": "23. Accessibility",
        "13. Trust & Compliance": "24. Trust & Compliance"
    }

    # First, handle deletions
    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        if text in h2_map and h2_map[text] == "DELETE":
            parent = h2.parent
            if parent and parent.name == 'section':
                parent.decompose()
            else:
                h2.decompose()

    # Second, rename everything
    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        if text in h2_map and h2_map[text] != "DELETE":
            h2.string = h2_map[text]
            
        # Also clean up the random sub-sections that use H2 instead of H3
        elif "Clinical Badges" in text or "Cinematic Modals" in text or "Text-on-Image" in text or "Editorial Card" in text or "Inline Link" in text or "Accordions" in text or "Button Hierarchy" in text or "Tabs" in text or "Progress Bars" in text or "Lists &" in text or "Hero Architecture" in text or "Forms:" in text or "Alerts" in text or "Pagination" in text or "Gallery &" in text or "Global Header" in text or "Video &" in text or "Loading &" in text or "Global Footer" in text or "Editorial Data" in text or "Editorial Process" in text or "Executive Team" in text or "Cinematic Gallery Player" in text:
            # Demote to H3
            h2.name = 'h3'
            h2['class'] = ['font-serif', 'text-[1.25rem]', 'font-bold', 'text-[#1C1C1E]', 'mt-12', 'mb-4']

    # Third, fix the sidebar navigation to match exactly
    nav = soup.find('nav', class_=lambda c: c and 'sticky' in c)
    if nav:
        nav.clear()
        
        links = [
            ("Foundations", [
                ("#00-governance", "00. Governance"),
                ("#01-brand", "01. Brand Foundation"),
                ("#02-verbal", "02. Verbal Identity"),
                ("#03-logo", "03. Logo & Identity"),
                ("#04-color", "04. Color"),
                ("#05-typography", "05. Typography"),
                ("#06-grid", "06. Grid & Layout")
            ]),
            ("Systems", [
                ("#08-photography", "08. Photography"),
                ("#11-motion", "11. Motion"),
                ("#12-components", "12. Component Library"),
                ("#15-data", "15. Data Visualization"),
                ("#23-accessibility", "23. Accessibility"),
                ("#24-trust", "24. Trust & Compliance"),
                ("#29-templates", "29. Page Templates")
            ])
        ]
        
        for group_name, items in links:
            group_div = soup.new_tag('div', attrs={'class': 'mt-6 mb-2 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]'})
            group_div.string = group_name
            nav.append(group_div)
            for href, text in items:
                a = soup.new_tag('a', href=href, attrs={'class': 'block py-2 text-[0.85rem] text-[#55555A] hover:text-[#804526] transition-colors'})
                a.string = text
                nav.append(a)

    # Fourth, assign the correct IDs to the sections so the links actually work
    id_map = {
        "00. Governance": "00-governance",
        "01. Brand Foundation": "01-brand",
        "02. Verbal Identity": "02-verbal",
        "03. Logo & Identity": "03-logo",
        "04. Color": "04-color",
        "05. Typography": "05-typography",
        "06. Grid & Layout": "06-grid",
        "08. Photography & Art Direction": "08-photography",
        "11. Motion": "11-motion",
        "12. Component Library": "12-components",
        "15. Data Visualization": "15-data",
        "23. Accessibility": "23-accessibility",
        "24. Trust & Compliance": "24-trust",
        "29. Page Templates": "29-templates"
    }

    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        if text in id_map:
            parent = h2.parent
            if parent.name == 'section' or parent.name == 'div':
                parent['id'] = id_map[text]

    # Convert soup back to string and write
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

qc_reorder()
