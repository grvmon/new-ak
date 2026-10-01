from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    comp_sec = soup.find(id='12-components')
    if comp_sec:
        
        nav_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Global Navigation (Header)</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">The primary navigation must seamlessly adapt to both Light and Dark architectural contexts while maintaining strict alignment and CTA hierarchy.</p>
            
            <div class="grid grid-cols-1 gap-12">
                
                <!-- Light Variant -->
                <div class="flex flex-col gap-4">
                    <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Light Variant (Titanium Frost)</div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-12 rounded-sm flex items-center justify-center">
                        
                        <!-- Light Navbar Mockup -->
                        <nav class="w-full max-w-4xl bg-white border-[0.5px] border-[#55555a26] h-16 flex items-center justify-between px-6 shadow-sm rounded-sm">
                            <div class="font-logo text-[1.15rem] font-semibold tracking-[-0.02em] text-[#1C1C1E]">acre&amp;key</div>
                            
                            <div class="hidden md:flex items-center gap-8 text-[0.8rem] font-bold tracking-[0.1em] uppercase text-[#55555A]">
                                <a href="#" class="hover:text-[#1C1C1E] transition-colors">Properties</a>
                                <a href="#" class="hover:text-[#1C1C1E] transition-colors">Advisory</a>
                                <a href="#" class="hover:text-[#1C1C1E] transition-colors">Intelligence</a>
                            </div>

                            <button class="bg-[#1C1C1E] text-white px-5 py-2.5 rounded-sm font-sans text-[0.75rem] font-bold uppercase tracking-[0.1em] hover:bg-black transition-colors">
                                Book Advisory
                            </button>
                        </nav>

                    </div>
                </div>

                <!-- Dark Variant -->
                <div class="flex flex-col gap-4">
                    <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Dark Variant (Obsidian)</div>
                    <div class="bg-[#1C1C1E] border-[0.5px] border-[#55555a26] p-12 rounded-sm flex items-center justify-center">
                        
                        <!-- Dark Navbar Mockup -->
                        <nav class="w-full max-w-4xl bg-[#1C1C1E]/90 backdrop-blur-md border-b-[0.5px] border-white/10 h-16 flex items-center justify-between px-6 rounded-sm">
                            <div class="font-logo text-[1.15rem] font-semibold tracking-[-0.02em] text-[#FAFAFA]">acre&amp;key</div>
                            
                            <div class="hidden md:flex items-center gap-8 text-[0.8rem] font-bold tracking-[0.1em] uppercase text-[#FAFAFA]/70">
                                <a href="#" class="hover:text-[#FAFAFA] transition-colors">Properties</a>
                                <a href="#" class="hover:text-[#FAFAFA] transition-colors">Advisory</a>
                                <a href="#" class="hover:text-[#FAFAFA] transition-colors">Intelligence</a>
                            </div>

                            <button class="bg-[#BE7555] text-white px-5 py-2.5 rounded-sm font-sans text-[0.75rem] font-bold uppercase tracking-[0.1em] hover:bg-[#9F5334] transition-colors shadow-sm">
                                Book Advisory
                            </button>
                        </nav>

                    </div>
                </div>

            </div>
        </div>
        """, 'html.parser')
        
        # Append before the final Principle block in 12-components, or just append to end
        principle_block = comp_sec.find_all('div', class_=lambda c: c and 'bg-[#1C1C1E]' in c and 'p-12' in c)
        if principle_block:
            principle_block[-1].insert_before(nav_block)
        else:
            comp_sec.append(nav_block)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
