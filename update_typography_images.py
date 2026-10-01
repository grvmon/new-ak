from bs4 import BeautifulSoup
import re

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
                # We need to replace the container of this block, not the whole layout.
                # Assuming the immediate parent or the parent of the parent is just the block, not the section.
                # Let's find the div that contains "Text must sit inside a controlled contrast zone."
                contrast_p = typo_sec.find(lambda t: t.name == 'p' and 'Text must sit inside a controlled contrast zone.' in t.text)
                if contrast_p:
                    block_container = contrast_p.parent
                    block_container.clear()
                    
                    new_content = BeautifulSoup("""
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">2. Text on Images</div>
                        <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-4 max-w-3xl">Text over photography is permitted only when the image has been deliberately composed for text. <strong class="text-[#8B3A3A]">Text must sit inside a controlled contrast zone.</strong></p>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
                            <div>
                                <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Contrast zones can be achieved through:</h4>
                                <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside mb-6">
                                    <li>Natural negative space</li>
                                    <li>Dark image area</li>
                                    <li>Controlled gradient overlay</li>
                                    <li>Image crop designed around the text</li>
                                    <li>Dedicated text-safe area</li>
                                </ul>
                            </div>
                            <div>
                                <div class="bg-[#8B3A3A]/5 border-[0.5px] border-[#8B3A3A]/20 p-6 rounded-sm h-full flex flex-col justify-center">
                                    <h4 class="font-serif text-[1.1rem] text-[#8B3A3A] mb-2">Important Image Rule</h4>
                                    <p class="text-[0.85rem] text-[#8B3A3A] font-bold leading-relaxed">Never use text color alone to solve a bad image composition.</p>
                                    <p class="text-[0.85rem] text-[#1C1C1E] leading-relaxed mt-2">If text requires a heavy black overlay simply to remain readable, change the crop or image first.</p>
                                </div>
                            </div>
                        </div>

                        <div class="space-y-16">
                            <!-- Example 1: Editorial Image Card -->
                            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                                <div class="lg:col-span-5">
                                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Editorial Image Card Hierarchy</h4>
                                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">This card structure is the canonical example of how to build hierarchy on an image. The contrast zone is controlled natively by the gradient overlay at the bottom.</p>
                                    
                                    <ul class="text-[0.85rem] space-y-3 font-sans">
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#BE7555] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Kicker:</span> <span class="text-[#55555A]">Copper</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Headline:</span> <span class="text-[#55555A]">Titanium Frost (Marcellus)</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Body:</span> <span class="text-[#55555A]">Titanium Frost (Manrope)</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#BE7555] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Emphasis:</span> <span class="text-[#55555A]">Copper (used sparingly for the closing brand statement)</span></li>
                                    </ul>
                                </div>
                                <div class="lg:col-span-7 flex justify-center">
                                    <img src="/assets/thoughtful-buyer-card.jpg" alt="Thoughtful Buyer Card Example" class="max-h-[500px] w-auto shadow-xl rounded-sm border-[0.5px] border-[#1C1C1E]" />
                                </div>
                            </div>

                            <!-- Example 2: Large Hero -->
                            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                                <div class="lg:col-span-5 lg:order-2">
                                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Hero Composition Hierarchy</h4>
                                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">For large hero imagery, the image remains the visual anchor. Typography must sit within a controlled contrast zone on the left rather than fighting the subject matter on the right.</p>
                                    
                                    <div class="bg-white p-4 border-[0.5px] border-[#55555a26] rounded-sm mb-6">
                                        <div class="font-bold text-[0.85rem] text-[#2C4C3B] mb-1">✓ Correct Layering</div>
                                        <div class="text-[0.8rem] text-[#55555A]">Image → contrast zone → typography</div>
                                    </div>
                                    
                                    <ul class="text-[0.85rem] space-y-3 font-sans">
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Headline:</span> <span class="text-[#55555A]">Titanium Frost</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#BE7555] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">Emphasis:</span> <span class="text-[#55555A]">Copper used for semantic emphasis, not decoration.</span></li>
                                        <li class="flex items-center gap-3"><span class="w-2 h-2 bg-[#BE7555] rounded-sm"></span> <span class="text-[#1C1C1E] font-bold w-20">CTA:</span> <span class="text-[#55555A]">Primary Copper button.</span></li>
                                    </ul>
                                </div>
                                <div class="lg:col-span-7 lg:order-1 flex justify-center">
                                    <img src="/assets/hero-example.png" alt="Hero Composition Example" class="w-full h-auto shadow-xl rounded-sm border-[0.5px] border-[#1C1C1E]" />
                                </div>
                            </div>
                        </div>
                    """, 'html.parser')
                    
                    block_container.append(new_content)
                break

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
