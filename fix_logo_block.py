from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    logo_sec = soup.find(id='03-logo')
    if logo_sec:
        # Find the double-nested bg-[#1C1C1E] block
        bad_blocks = logo_sec.find_all('div', class_=lambda c: c and 'bg-[#1C1C1E]' in c and 'p-12' in c)
        # Remove them
        for block in bad_blocks:
            block.decompose()
        
        # Append the correct structure
        new_blocks = BeautifulSoup("""
        <!-- Decision Rule -->
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Decision Rule</h3>
            <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm font-sans max-w-3xl">
                <p class="text-[1rem] text-[#1C1C1E] font-bold leading-relaxed mb-4">When there is uncertainty:</p>
                <div class="flex items-start gap-4">
                    <div class="text-[#BE7555] font-bold text-[1rem] w-6 shrink-0 pt-0.5">01</div>
                    <div class="text-[0.9rem] text-[#55555A] leading-relaxed">Use the approved Josefin Sans master logo, in one approved color, with maximum legibility and sufficient clear space.</div>
                </div>
            </div>
        </div>

        <!-- The Principle -->
        <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
            <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
            <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">The logo should feel quiet, controlled, precise, and permanent — never decorative, fashionable, or promotional.</div>
        </div>
        """, 'html.parser')
        
        # Find the main div to append to
        main_div = logo_sec.find('div', class_=lambda c: c and 'space-y-16' in c)
        if main_div:
            main_div.append(new_blocks)
        else:
            logo_sec.append(new_blocks)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
