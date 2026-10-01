from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # 1. Update Typography Section with "Text on Obsidian Black"
    typo_sec = soup.find(id='05-typography')
    if typo_sec:
        # We will insert the new rules right after the "Text on Surfaces" header
        # or we can just append it before "Text on Images"
        
        obsidian_rule = BeautifulSoup("""
        <div class="mt-16 bg-[#1C1C1E] p-10 border-[0.5px] border-[#55555a26] rounded-sm text-white">
            <h4 class="font-serif text-[1.25rem] text-[#FAFAFA] mb-2">Text on Obsidian Black</h4>
            <p class="text-[0.95rem] text-[#FAFAFA]/70 leading-relaxed mb-8 max-w-2xl font-sans">Obsidian Black is an editorial canvas, not a surface on which every text element should be rendered at maximum contrast. The hierarchy must come primarily from typeface, size, weight, spacing, and position. Color is reserved for emphasis.</p>
            
            <div class="bg-white/5 border-[0.5px] border-white/10 rounded-sm overflow-hidden mb-8">
                <table class="w-full text-left font-sans">
                    <tbody class="divide-y divide-white/10">
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Kicker / Overline</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Manrope · 700</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#BE7555]">Copper</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">H1 / H2</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Marcellus · 400</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#FAFAFA]">Titanium Frost</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Body</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Manrope · 400</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#FAFAFA]/70">Titanium Frost (controlled opacity)</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Supporting text</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Manrope · 400</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Neutral / muted</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Data / Key value</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Manrope · 600</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#FAFAFA]">Titanium Frost</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Selected emphasis</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Marcellus/Manrope · 400-600</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#BE7555]">Copper</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 text-[0.85rem] font-bold text-[#FAFAFA]">Principle / Quote</td>
                            <td class="py-3 px-4 text-[0.85rem] text-white/50">Marcellus · 400</td>
                            <td class="py-3 px-4 text-[0.85rem] text-[#FAFAFA]">Titanium Frost</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div>
                    <h5 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#BE7555] mb-3">The Key Rule</h5>
                    <ul class="text-[0.85rem] text-white/70 space-y-2 list-disc list-inside font-sans">
                        <li class="font-bold text-[#FAFAFA]">Titanium Frost is the primary text color. Copper is the accent.</li>
                        <li>Do not make multiple lines of a headline copper.</li>
                        <li>Do not use copper for ordinary body copy.</li>
                        <li>Do not use three or four competing text colors.</li>
                    </ul>
                </div>
                <div>
                    <h5 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#BE7555] mb-3">Opacity Hierarchy</h5>
                    <ul class="text-[0.85rem] text-white/70 space-y-2 font-sans">
                        <li><span class="text-[#FAFAFA]">Primary:</span> 100% Titanium Frost</li>
                        <li><span class="text-[#FAFAFA]/80">Secondary:</span> ~72–80% Titanium Frost</li>
                        <li><span class="text-[#FAFAFA]/60">Tertiary:</span> ~55–64% Titanium Frost</li>
                        <li><span class="text-[#FAFAFA]/40">Disabled:</span> ~40–48% Titanium Frost</li>
                    </ul>
                </div>
            </div>

            <div class="border-t-[0.5px] border-white/10 pt-6 text-center">
                <span class="font-bold text-[1.1rem] text-[#BE7555] font-sans">On Obsidian, typography creates hierarchy. Copper creates emphasis.</span>
            </div>
        </div>
        """, 'html.parser')
        
        # Insert after "1. Text on Dark Units" block
        dark_units_header = typo_sec.find(lambda t: t.name == 'div' and '1. Text on Dark Units' in t.text)
        if dark_units_header:
            # The parent of the header is the grid col. Its parent is the grid.
            dark_units_grid = dark_units_header.parent.parent
            dark_units_grid.insert_after(obsidian_rule)
    
    # 2. Re-style ALL "Decision Rule" / "The Brand Test" blocks.
    # Look for div.bg-[#1C1C1E] text-white
    dark_blocks = soup.find_all('div', class_=re.compile(r'bg-\[\#1C1C1E\].*text-white.*'))
    
    for block in dark_blocks:
        text_content = block.get_text()
        if 'Brand Test' in text_content:
            block.clear()
            block.append(BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-8">The Brand Test</div>
                <p class="text-[20px] text-[#FAFAFA] font-normal leading-relaxed mb-10 max-w-2xl">Before approving any design, copy, interaction, or campaign, ask:</p>
                <div class="space-y-6 mb-12">
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-6 shrink-0 pt-0.5">01</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does this make acre&amp;key feel more independent, intelligent, precise, and trustworthy?</div>
                    </div>
                </div>
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-3xl leading-[1.3]">If it makes the brand feel promotional, decorative, generic, or sales-led, reconsider it.</div>
            </div>
            """, 'html.parser'))
        
        elif 'Logo Decision Rule' in text_content:
            block.clear()
            block.append(BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-8">Logo Decision Rule</div>
                <p class="text-[20px] text-[#FAFAFA] font-normal leading-relaxed mb-10 max-w-2xl">When there is uncertainty:</p>
                <div class="space-y-6 mb-12">
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-6 shrink-0 pt-0.5">01</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Use the approved Josefin Sans master logo, in one approved color, with maximum legibility and sufficient clear space.</div>
                    </div>
                </div>
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-3xl leading-[1.3]">The logo should feel quiet, controlled, precise, and permanent — never decorative, fashionable, or promotional.</div>
            </div>
            """, 'html.parser'))
            
        elif 'Color Decision Rule' in text_content:
            block.clear()
            block.append(BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-8">Color Decision Rule</div>
                <p class="text-[20px] text-[#FAFAFA] font-normal leading-relaxed mb-10 max-w-2xl">Before introducing a color, ask:</p>
                <div class="space-y-6 mb-12">
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">01</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it have a defined semantic role?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">02</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it already exist as a token?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">03</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it meet the required contrast against its intended surface?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">04</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it reinforce the acre&amp;key visual language?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">05</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Is it necessary?</div>
                    </div>
                </div>
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-3xl leading-[1.3]">If the answer to the final question is no, do not add the color.</div>
            </div>
            """, 'html.parser'))
            
        elif 'Layout Decision Rule' in text_content:
            block.clear()
            block.append(BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-8">Layout Decision Rule</div>
                <p class="text-[20px] text-[#FAFAFA] font-normal leading-relaxed mb-10 max-w-2xl">Before introducing a new layout pattern, ask:</p>
                <div class="space-y-6 mb-12 max-w-3xl">
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">01</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does an existing grid structure solve the requirement?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">02</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does the composition align to the core grid?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">03</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it use approved spacing tokens?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">04</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it remain coherent across desktop, tablet, and mobile?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">05</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Is the asymmetry intentional?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">06</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does the whitespace improve hierarchy or merely create emptiness?</div>
                    </div>
                </div>
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">The grid should be invisible in the final experience, but obvious in the discipline behind it.</div>
            </div>
            """, 'html.parser'))
            
        elif 'Final System Principle' in text_content:
            block.clear()
            block.append(BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-3xl leading-[1.3]">Text should never be colored because it looks better. It should be colored because it has a defined role.</div>
            </div>
            """, 'html.parser'))

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
