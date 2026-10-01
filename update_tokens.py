from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    tokens_sec = soup.find(id='25-tokens')
    if tokens_sec:
        tokens_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">25. Developer Design Tokens</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">This is the single source of truth for engineering. Absolute pixel values are banned. If a token exists for a value, the token must be used. We rely heavily on a highly customized Tailwind configuration.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Structural Tokens Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Colors -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Colors</h3>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">bg-obsidian</span> <span class="text-[#1C1C1E]">#1C1C1E</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">bg-titanium</span> <span class="text-[#1C1C1E]">#FAFAFA</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">bg-copper</span> <span class="text-[#1C1C1E]">#BE7555</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">text-neutral</span> <span class="text-[#1C1C1E]">#55555A</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">border-hairline</span> <span class="text-[#1C1C1E]">#55555a26</span></li>
                    </ul>
                </div>

                <!-- Typography -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Typography</h3>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">font-serif</span> <span class="text-[#1C1C1E]">Marcellus</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">font-sans</span> <span class="text-[#1C1C1E]">Manrope</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">font-logo</span> <span class="text-[#1C1C1E]">Josefin Sans</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">text-h1</span> <span class="text-[#1C1C1E]">clamp(2.5, 4vw, 3.5)</span></li>
                    </ul>
                </div>

                <!-- Spacing -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Spacing</h3>
                    <p class="text-[0.75rem] text-[#55555A] mb-3 font-sans">Strict 4px scaling system. Arbitrary values (e.g. 13px) are banned.</p>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">p-1</span> <span class="text-[#1C1C1E]">4px</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">p-4</span> <span class="text-[#1C1C1E]">16px</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">p-8</span> <span class="text-[#1C1C1E]">32px</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">gap-6</span> <span class="text-[#1C1C1E]">24px</span></li>
                    </ul>
                </div>

                <!-- Radius & Borders -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Radius &amp; Borders</h3>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">rounded-none</span> <span class="text-[#1C1C1E]">0px (Sharp)</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">rounded-sm</span> <span class="text-[#1C1C1E]">4px (Cards/Btns)</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">border-[0.5px]</span> <span class="text-[#1C1C1E]">0.5px Hairline</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">border</span> <span class="text-[#1C1C1E]">1px Structure</span></li>
                    </ul>
                </div>

                <!-- Breakpoints & Containers -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Breakpoints &amp; Grid</h3>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">md:</span> <span class="text-[#1C1C1E]">768px (Tablet)</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">lg:</span> <span class="text-[#1C1C1E]">1024px (Laptop)</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">max-w-[1280px]</span> <span class="text-[#1C1C1E]">Master Container</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">grid-cols-12</span> <span class="text-[#1C1C1E]">Desktop Layout</span></li>
                    </ul>
                </div>

                <!-- Motion & Z-Index -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Motion &amp; Z-Index</h3>
                    <ul class="text-[0.8rem] space-y-3 font-mono text-[#55555A]">
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">duration-150</span> <span class="text-[#1C1C1E]">Hover States</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">duration-700</span> <span class="text-[#1C1C1E]">Image Reveals</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">z-10</span> <span class="text-[#1C1C1E]">Card Overlays</span></li>
                        <li class="flex justify-between items-center"><span class="bg-black/5 px-1 rounded-sm">z-50</span> <span class="text-[#1C1C1E]">Global Nav/Modals</span></li>
                    </ul>
                </div>

            </div>

            <!-- Token Application Context -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Token Application Matrix</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                    <div>
                        <div class="bg-white p-4 border-[0.5px] border-[#55555a26] rounded-sm mb-6 shadow-sm">
                            <div class="font-bold text-[0.85rem] text-[#8B3A3A] mb-1">✕ Hardcoded (Banned)</div>
                            <div class="font-mono text-[0.7rem] text-[#55555A] break-all">style="border: 1px solid #e5e5e5; border-radius: 5px; padding: 15px;"</div>
                        </div>
                        <div class="bg-white p-4 border-[0.5px] border-[#55555a26] rounded-sm shadow-sm">
                            <div class="font-bold text-[0.85rem] text-[#2C4C3B] mb-1">✓ Tokenized (Required)</div>
                            <div class="font-mono text-[0.7rem] text-[#55555A] break-all">class="border-[0.5px] border-hairline rounded-sm p-4"</div>
                        </div>
                    </div>
                    
                    <div class="flex justify-center">
                        <div class="w-full max-w-[280px] bg-white border-[0.5px] border-[#55555a26] rounded-sm p-4 shadow-xl">
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Architectural Card</div>
                            <div class="font-sans text-[0.8rem] text-[#55555A]">Tokens enforce a perfect 0.5px hairline and strict 4px radius geometry.</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">A developer should rarely need to write a line of raw CSS. The design system lives natively inside the utility class definitions.</div>
            </div>

        </div>
        """, 'html.parser')
        tokens_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
