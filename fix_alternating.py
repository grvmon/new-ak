from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    color_sec = soup.find(id='04-color')
    if color_sec:
        # Find the h3 with text "Alternating Section Rhythm"
        h3 = color_sec.find(string=re.compile("Alternating Section Rhythm"))
        if h3:
            # We want to replace this entire block. Let's just find the parent div or clear it out.
            # Wait, the structure in the HTML is:
            # <div class="border-t-[0.5px] border-[#55555a26] pt-12">
            #   <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Alternating Section Rhythm</h3>
            #   ...
            # </div>
            parent = h3.parent.parent
            parent.clear()
            
            new_comp = BeautifulSoup("""
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Section Theming (Alternating Backgrounds)</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">To create visual pacing on long-scroll pages without relying on harsh drop shadows, we use <strong>Banded Sections</strong>. The page background must strictly alternate between these three environments to delineate different content blocks.</p>
            
            <div class="flex flex-col border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden mb-8">
                <!-- Base Canvas -->
                <div class="bg-[#FAFAFA] p-8 md:p-12">
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">Base Canvas</div>
                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-2">Titanium Frost</h4>
                    <p class="font-sans text-[0.85rem] text-[#55555A] max-w-xl">The default background for the majority of the page. Creates a soft, premium foundation.</p>
                </div>
                
                <!-- Alternating Canvas -->
                <div class="bg-white p-8 md:p-12 border-t-[0.5px] border-[#55555a26]">
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">Alternating Canvas</div>
                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-2">Pure White</h4>
                    <p class="font-sans text-[0.85rem] text-[#55555A] max-w-xl">Used for the very next section to create subtle, shadow-free separation from the Frost canvas above it.</p>
                </div>
                
                <!-- High-Impact Breakout -->
                <div class="bg-[#1C1C1E] p-8 md:p-12">
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">High-Impact Breakout</div>
                    <h4 class="font-serif text-[1.25rem] text-[#FAFAFA] mb-2">Obsidian Black</h4>
                    <p class="font-sans text-[0.85rem] text-[#FAFAFA]/70 max-w-xl">Used sparingly to break the flow. Reserved for footers, lead-generation forms, and massive value propositions.</p>
                </div>
            </div>
            
            <ul class="text-[0.85rem] text-[#55555A] space-y-3 list-disc list-inside">
                <li><strong class="text-[#1C1C1E]">Rule 1:</strong> Do not stack two identical background colors sequentially unless separated by a physical <code class="bg-black/5 px-1 rounded-sm">border-t</code> divider.</li>
                <li><strong class="text-[#1C1C1E]">Rule 2:</strong> Never use Copper (<code class="bg-black/5 px-1 rounded-sm">bg-[#BE7555]</code>) as a full-width section background. It is an accent only.</li>
            </ul>
            """, 'html.parser')
            
            parent.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
