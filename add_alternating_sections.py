from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    color_sec = soup.find(id='04-color')
    if color_sec:
        
        alt_block = BeautifulSoup("""
        <!-- Alternating Sections Architecture -->
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Alternating Section Rhythm</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Long pages (like the Homepage or Asset Dossier) must never rely on arbitrary dividing lines to separate content. Instead, we use alternating background blocks to create a structural, architectural rhythm without visual clutter.</p>
            
            <div class="grid grid-cols-1 gap-8">
                <div class="flex flex-col border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden shadow-xl">
                    
                    <!-- Section 1: White -->
                    <div class="bg-white p-12 text-center flex flex-col items-center justify-center">
                        <div class="text-[0.65rem] font-bold tracking-[0.2em] uppercase text-[#1C1C1E] mb-2 border-[0.5px] border-[#1C1C1E] px-2 py-1 rounded-sm w-fit">Layer 01</div>
                        <h4 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-2">Pure White Canvas</h4>
                        <p class="font-sans text-[0.85rem] text-[#55555A] max-w-md">The default state. Used for primary content, macro typography, and the highest-priority data matrices.</p>
                    </div>

                    <!-- Section 2: Titanium Frost -->
                    <div class="bg-[#FAFAFA] p-12 text-center flex flex-col items-center justify-center border-y-[0.5px] border-[#55555a26]">
                        <div class="text-[0.65rem] font-bold tracking-[0.2em] uppercase text-[#55555A] mb-2 border-[0.5px] border-[#55555a26] bg-white px-2 py-1 rounded-sm w-fit">Layer 02</div>
                        <h4 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-2">Titanium Frost</h4>
                        <p class="font-sans text-[0.85rem] text-[#55555A] max-w-md">A subtle shift to ground secondary content. Used for feature grids, testimonials, or dense property specifications.</p>
                    </div>

                    <!-- Section 3: Obsidian -->
                    <div class="bg-[#1C1C1E] p-12 text-center flex flex-col items-center justify-center">
                        <div class="text-[0.65rem] font-bold tracking-[0.2em] uppercase text-[#FAFAFA] mb-2 border-[0.5px] border-white/20 bg-white/5 px-2 py-1 rounded-sm w-fit">Layer 03</div>
                        <h4 class="font-serif text-[1.5rem] text-[#FAFAFA] mb-2">Obsidian Anchor</h4>
                        <p class="font-sans text-[0.85rem] text-[#FAFAFA]/70 max-w-md">The heaviest block. Used to anchor the page for major CTAs, footer structures, or high-impact closing principles.</p>
                    </div>

                </div>
            </div>
            
            <ul class="mt-8 text-[0.85rem] text-[#55555A] space-y-3 list-disc list-inside">
                <li><strong class="text-[#1C1C1E]">Rule 1:</strong> Do not stack two identical background colors sequentially unless separated by a physical <code class="bg-black/5 px-1 rounded-sm">border-t</code> divider.</li>
                <li><strong class="text-[#1C1C1E]">Rule 2:</strong> Never use Copper (<code class="bg-black/5 px-1 rounded-sm">bg-[#BE7555]</code>) as a massive full-width section background. It is an accent only.</li>
                <li><strong class="text-[#1C1C1E]">Rule 3:</strong> Obsidian sections must follow strict Dark Mode typography rules (Opacity hierarchy, no pure white text).</li>
            </ul>
        </div>
        """, 'html.parser')
        
        # Append before the final Principle block in 04-color, if it exists
        principle_block = color_sec.find_all('div', class_=lambda c: c and 'bg-[#1C1C1E]' in c and 'p-12' in c)
        if principle_block:
            principle_block[-1].insert_before(alt_block)
        else:
            color_sec.append(alt_block)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
