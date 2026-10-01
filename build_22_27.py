from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')

    # 22. SEO Design System
    sec_22 = soup.find(id='22-seo')
    if sec_22:
        sec_22.clear()
        sec_22.append(BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">22. SEO Design System</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Search structure dictates our digital authority. Every page must strictly adhere to the metadata architecture to ensure search engines perceive acre&key as a premium, institutional entity.</p>
        
        <div class="space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Meta Syntax -->
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-[4px]">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-6">Meta Syntax &amp; Hierarchy</h3>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-4">
                        <li><strong class="text-[#1C1C1E] block mb-1">Title Tag Formula</strong> <code class="bg-black/5 px-2 py-1 rounded-sm text-[#804526] font-mono text-[0.75rem]">[Asset / Report Name] | [Micro-market] | acre&amp;key</code></li>
                        <li><strong class="text-[#1C1C1E] block mb-1">H1/H2 Strict Rules</strong> One strict `H1` per page (Marcellus). `H2` is reserved for macro-sections. Never use heading tags for aesthetic sizing.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Alt-Text Policy</strong> Alt-text must describe the architectural intent, not keyword-stuff. (e.g. "South-facing balcony rendering at Prestige Evergreen").</li>
                    </ul>
                </div>
                
                <!-- OpenGraph (Social Cards) -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-[4px] shadow-sm flex flex-col justify-center">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">OpenGraph (Social Cards)</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-6">When a user texts a link, the preview card must immediately signal authority. It uses a strict 1200x630px Obsidian background with the brand logo centered.</p>
                    
                    <!-- OG Card Mockup -->
                    <div class="w-full aspect-[1200/630] bg-[#1C1C1E] rounded-sm relative overflow-hidden flex items-center justify-center border-[0.5px] border-[#55555a26]">
                        <span class="font-logo text-white text-[2rem] tracking-[-0.02em]">acre&amp;key</span>
                        <div class="absolute bottom-4 right-6 text-[#FAFAFA]/50 text-[0.6rem] tracking-[0.1em] uppercase">Intelligence Suite</div>
                    </div>
                </div>
            </div>
        </div>
        """, 'html.parser'))
        
    # 27. CMS Architecture
    sec_27 = soup.find(id='27-cms')
    if sec_27:
        sec_27.clear()
        sec_27.append(BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">27. CMS Architecture</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Our content is governed by a strict headless infrastructure. Visual design does not exist in the CMS; the CMS outputs pure JSON data mapped to our atomic Tailwind components.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white border-t-2 border-t-[#1C1C1E] border-x-[0.5px] border-b-[0.5px] border-[#55555a26] p-8 rounded-b-[4px]">
                <h4 class="font-bold text-[1rem] text-[#1C1C1E] mb-2">The Stack</h4>
                <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Powered by <strong class="text-[#1C1C1E]">Sanity.io</strong>. Real-time collaboration, strict document validation, and portable text to ensure typography is handled safely by the frontend.</p>
            </div>
            
            <div class="bg-white border-t-2 border-t-[#BE7555] border-x-[0.5px] border-b-[0.5px] border-[#55555a26] p-8 rounded-b-[4px]">
                <h4 class="font-bold text-[1rem] text-[#1C1C1E] mb-2">Data Models</h4>
                <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Core schemas include <code class="bg-black/5 px-1 rounded-sm">Property Dossiers</code>, <code class="bg-black/5 px-1 rounded-sm">Micro-markets</code>, and <code class="bg-black/5 px-1 rounded-sm">Advisors</code>. Structured fields ensure no content breaks the frontend layout.</p>
            </div>
            
            <div class="bg-[#FAFAFA] border-t-2 border-t-[#55555A] border-x-[0.5px] border-b-[0.5px] border-[#55555a26] p-8 rounded-b-[4px]">
                <h4 class="font-bold text-[1rem] text-[#1C1C1E] mb-2">Governance</h4>
                <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Strict character limits are enforced at the schema level (e.g. 160 char max for SEO descriptions). Only authorized editors can push changes.</p>
            </div>
        </div>
        """, 'html.parser'))
        
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected 22 and 27 successfully.")

update()
