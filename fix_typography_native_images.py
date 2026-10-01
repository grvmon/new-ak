from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    typo_sec = soup.find(id='05-typography')
    if typo_sec:
        # Find the specific div containing "2. Text on Images" text
        for div in typo_sec.find_all('div'):
            if div.get_text(strip=True).startswith("2. Text on Images"):
                contrast_p = typo_sec.find(lambda t: t.name == 'p' and 'Text must sit inside a controlled contrast zone.' in t.text)
                if contrast_p:
                    block_container = contrast_p.parent
                    block_container.clear()
                    
                    new_content = BeautifulSoup("""
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">2. Text on Images (Native Implementation)</div>
                        <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-4 max-w-3xl">Text over photography is permitted only when the image has been deliberately composed for text. <strong class="text-[#8B3A3A]">Text must sit inside a controlled contrast zone.</strong></p>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
                            <div>
                                <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Contrast zones can be achieved through:</h4>
                                <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside mb-6">
                                    <li>Natural negative space</li>
                                    <li>Dark image area</li>
                                    <li>Controlled gradient overlay</li>
                                    <li>Image crop designed around the text</li>
                                </ul>
                            </div>
                            <div>
                                <div class="bg-[#8B3A3A]/5 border-[0.5px] border-[#8B3A3A]/20 p-6 rounded-sm h-full flex flex-col justify-center">
                                    <h4 class="font-serif text-[1.1rem] text-[#8B3A3A] mb-2">Important Image Rule</h4>
                                    <p class="text-[0.85rem] text-[#8B3A3A] font-bold leading-relaxed">Never use text color alone to solve a bad image composition.</p>
                                </div>
                            </div>
                        </div>

                        <div class="space-y-16">
                            <!-- Native Example 1: Editorial Image Card -->
                            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                                <div class="lg:col-span-5">
                                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Editorial Image Card Hierarchy</h4>
                                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">This is a live native implementation of the Thoughtful Buyer card. The contrast zone is built using a CSS gradient overlay anchoring the bottom.</p>
                                    
                                    <ul class="text-[0.85rem] space-y-3 font-sans">
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#BE7555] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Kicker:</span> <span class="text-[#55555A]">Copper (Manrope 700)</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Headline:</span> <span class="text-[#55555A]">Titanium Frost (Marcellus 400)</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Body:</span> <span class="text-[#55555A]">Titanium Frost (Manrope 400)</span></li>
                                    </ul>
                                </div>
                                <div class="lg:col-span-7 flex justify-center">
                                    <!-- NATIVE CARD CODE -->
                                    <div class="relative w-full max-w-[400px] h-[550px] rounded-sm overflow-hidden flex flex-col justify-end group shadow-xl">
                                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_pool_evening.webp')] bg-cover bg-center grayscale contrast-[1.1] group-hover:scale-105 transition-transform duration-[800ms] ease-out"></div>
                                        <!-- Gradient contrast zone -->
                                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/80 to-transparent h-[65%] mt-auto"></div>
                                        
                                        <div class="relative z-10 p-8 flex flex-col gap-4">
                                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#BE7555]">03. The Thoughtful Buyer</div>
                                            <div class="font-serif text-[1.75rem] text-[#FAFAFA] leading-[1.2]">You want an honest opinion, not another sales pitch.</div>
                                            <p class="font-sans text-[0.95rem] text-[#FAFAFA]/80 leading-relaxed">For buyers who want to understand the numbers, plans, specifications and trade-offs before committing significant capital to a home.</p>
                                            <div class="font-sans text-[0.95rem] text-[#BE7555] italic mt-2">If something doesn't stand up to scrutiny, we tell you.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Native Example 2: Large Hero -->
                            <div class="grid grid-cols-1 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                                <div class="w-full">
                                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Hero Composition Hierarchy</h4>
                                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">A live native implementation of the Hero. A horizontal gradient anchors the text to the left, allowing the image to breathe on the right without sacrificing AAA readability.</p>
                                    
                                    <!-- NATIVE HERO CODE -->
                                    <div class="relative w-full h-[500px] rounded-sm overflow-hidden flex items-center shadow-xl border-[0.5px] border-[#1C1C1E]">
                                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_skyline_night_aerial.webp')] bg-cover bg-center"></div>
                                        <!-- Gradient contrast zone -->
                                        <div class="absolute inset-0 bg-gradient-to-r from-[#1C1C1E] via-[#1C1C1E]/90 to-transparent w-3/4"></div>
                                        
                                        <div class="relative z-10 p-12 max-w-2xl flex flex-col gap-6">
                                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#FAFAFA]/70">Home Buyer Concierge</div>
                                            <h1 class="font-serif text-[2.5rem] md:text-[3.25rem] text-[#FAFAFA] leading-[1.1]">
                                                Anyone can give options.<br>
                                                We help you buy <span class="text-[#BE7555]">the right home.</span>
                                            </h1>
                                            <p class="font-sans text-[1rem] md:text-[1.1rem] text-[#FAFAFA]/80 leading-relaxed max-w-lg">Independent home buying advisory to evaluate the opportunity, uncover the risks, and negotiate on your behalf.</p>
                                            
                                            <div class="flex gap-12 mt-4 border-t-[0.5px] border-white/20 pt-6">
                                                <div>
                                                    <div class="font-sans text-[1.5rem] text-[#FAFAFA] mb-1">69</div>
                                                    <div class="font-sans text-[0.8rem] text-[#FAFAFA]/60">Due Diligence Checks</div>
                                                </div>
                                                <div>
                                                    <div class="font-sans text-[1.5rem] text-[#FAFAFA] mb-1">₹0</div>
                                                    <div class="font-sans text-[0.8rem] text-[#FAFAFA]/60">Buyer Advisory Fee</div>
                                                </div>
                                            </div>
                                            
                                            <div class="mt-4">
                                                <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-6 py-3 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors flex items-center gap-3 w-fit">
                                                    Book Advisory Call 
                                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- End Native Hero Code -->
                                </div>
                            </div>
                        </div>
                    """, 'html.parser')
                    
                    block_container.append(new_content)
                break

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
