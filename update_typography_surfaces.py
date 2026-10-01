from bs4 import BeautifulSoup

def append_surfaces():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    typo_sec = soup.find(id='05-typography')
    if typo_sec:
        # We append the new content
        new_content = BeautifulSoup("""
        <div class="mt-24 pt-16 border-t-[0.5px] border-[#55555a26] space-y-16 font-sans">
            
            <div class="mb-12">
                <h3 class="font-serif text-3xl text-[#1C1C1E] mb-4">Text on Surfaces</h3>
                <p class="text-[1rem] text-[#55555A] max-w-3xl leading-relaxed">acre&amp;key uses text differently depending on the surface behind it. The hierarchy must remain consistent whether the text sits on a solid dark surface, photography, or an interactive element.</p>
            </div>

            <!-- Text on Dark Boxes -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">1. Text on Dark Units</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-6">Dark surfaces use Titanium Frost as the primary text color.</p>
                    
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden mb-8">
                        <table class="w-full text-left">
                            <tbody class="divide-y divide-[#55555a26]">
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">Kicker / Overline</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Copper / approved accent</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">H2 / H3</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Titanium Frost</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">Body</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Titanium Frost at controlled opacity</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">Data / Numbers</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Titanium Frost</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">Supporting text</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Muted neutral, only where contrast remains sufficient</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">Key emphasis</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Copper Text / approved copper</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4 text-[0.85rem] font-bold text-[#1C1C1E]">CTA</td>
                                    <td class="py-3 px-4 text-[0.85rem] text-[#55555A]">Copper surface + high-contrast text</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Dark Unit Rules</h4>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                        <li>Primary headings must remain Titanium Frost.</li>
                        <li>Copper is an accent, not the default body-text color.</li>
                        <li>Do not use multiple accent colors inside one dark unit.</li>
                        <li>Do not use gradients to create text hierarchy.</li>
                        <li>Do not use low-contrast grey for important information.</li>
                        <li class="font-bold text-[#8B3A3A]">Maximum 2 text colors + 1 surface color within a single unit.</li>
                        <li>Text hierarchy should come from size, weight, spacing and placement before color.</li>
                    </ul>
                </div>
                
                <div class="bg-[#1C1C1E] p-10 rounded-sm flex flex-col justify-center border-[0.5px] border-[#55555a26]">
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-white/40 mb-8 border-b-[0.5px] border-white/10 pb-4">Correct Hierarchy Example</div>
                    
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">Copper Kicker</div>
                    <div class="font-serif text-3xl text-[#FAFAFA] mb-4">Marcellus headline in Titanium Frost</div>
                    <p class="text-[0.95rem] text-[#FAFAFA]/70 leading-relaxed mb-6 font-sans">Manrope body copy in Titanium Frost or an approved muted tone. The <span class="italic text-[#BE7555]">copper emphasis</span> should only be used where meaningfully useful.</p>
                    <div class="mt-8 border-t-[0.5px] border-white/10 pt-6">
                        <span class="text-[#FAFAFA] italic text-[0.9rem]">"If something doesn't stand up to scrutiny, we tell you."</span>
                    </div>
                </div>
            </div>

            <!-- Text on Images -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">2. Text on Images</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-4">Text over photography is permitted only when the image has been deliberately composed for text.</p>
                    <p class="text-[0.95rem] text-[#8B3A3A] font-bold leading-relaxed mb-6">Text must sit inside a controlled contrast zone.</p>
                    
                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">This can be achieved through:</h4>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside mb-8">
                        <li>Natural negative space</li>
                        <li>Dark image area</li>
                        <li>Controlled gradient overlay</li>
                        <li>Image crop designed around the text</li>
                        <li>Dedicated text-safe area</li>
                    </ul>

                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Image Overlay Rule</h4>
                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Do not place text directly over visually complex areas. If the image does not provide sufficient contrast naturally, introduce a subtle controlled overlay. The overlay should support legibility without making the photograph look artificially dark.</p>
                    <div class="bg-[#8B3A3A]/5 border-[0.5px] border-[#8B3A3A]/20 p-4 rounded-sm mb-6">
                        <p class="text-[0.85rem] text-[#8B3A3A] font-bold">Important: Never use text color alone to solve a bad image composition. If text requires a heavy overlay to remain readable, change the crop or image first.</p>
                    </div>

                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Hero Image Rule</h4>
                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-2">For large hero imagery:</p>
                    <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">✓ Image → contrast zone → typography</p>
                    <p class="text-[0.85rem] text-[#8B3A3A] line-through mb-4">✕ Image → typography → heavy overlay</p>
                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed">The image remains the visual anchor. Typography should sit within the composition rather than fight it.</p>
                </div>
                
                <div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">
                    <div class="absolute inset-0 bg-[#1C1C1E]"></div>
                    <div class="absolute inset-0 opacity-60 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center grayscale contrast-[1.2]"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent"></div>
                    
                    <div class="relative z-10 p-10">
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-3">Copper Kicker</div>
                        <div class="font-serif text-3xl text-[#FAFAFA] mb-3">Headline in Titanium Frost</div>
                        <p class="text-[0.95rem] text-[#FAFAFA]/80 leading-relaxed font-sans max-w-sm">Body in Titanium Frost. The contrast zone is controlled natively by the gradient overlay at the bottom.</p>
                    </div>
                </div>
            </div>

            <!-- Text on Buttons -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">3. Text on Buttons</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8">Buttons are functional UI and follow stricter rules than editorial text.</p>
                    
                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Primary CTA</h4>
                    <div class="mb-4">
                        <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-6 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors flex items-center gap-2">
                            Book advisory call
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M12 5l7 7-7 7"></path></svg>
                        </button>
                    </div>
                    <p class="text-[0.85rem] text-[#55555A] font-bold mb-2">Copper background + high-contrast text.</p>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-1 list-disc list-inside mb-8">
                        <li>Use Manrope.</li>
                        <li>Use 600 weight.</li>
                        <li>Sentence case.</li>
                        <li>No uppercase CTA copy unless specifically required.</li>
                        <li>No exclamation marks.</li>
                        <li>Minimum contrast must meet accessibility.</li>
                        <li>Icon, if present, should be secondary to the label.</li>
                        <li class="text-[#8B3A3A] font-bold">Do not use Marcellus inside buttons.</li>
                    </ul>

                    <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Secondary Button</h4>
                    <div class="mb-4">
                        <button class="bg-transparent border-[0.5px] border-[#55555a26] text-[#1C1C1E] hover:border-[#1C1C1E] px-6 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors">
                            View analysis
                        </button>
                    </div>
                    <p class="text-[0.85rem] text-[#55555A] font-bold mb-2">Use a restrained outlined or tonal treatment.</p>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-1 list-disc list-inside">
                        <li>No unnecessary fill.</li>
                        <li>No decorative gradients.</li>
                        <li>Border and text must maintain sufficient contrast.</li>
                        <li>Must remain visually subordinate to the primary CTA.</li>
                    </ul>
                </div>

                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Button Copy Rules</div>
                    
                    <h4 class="font-serif text-[1.1rem] text-[#2C4C3B] mb-4 flex items-center gap-2"><span class="text-[#2C4C3B]">✓</span> Prefer</h4>
                    <ul class="text-[0.9rem] text-[#1C1C1E] space-y-2 mb-8 list-disc list-inside">
                        <li>Book advisory call</li>
                        <li>Request consultation</li>
                        <li>View analysis</li>
                        <li>Explore properties</li>
                        <li>See the assessment</li>
                        <li>Speak with an advisor</li>
                    </ul>

                    <h4 class="font-serif text-[1.1rem] text-[#8B3A3A] mb-4 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Avoid</h4>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-2 list-disc list-inside line-through">
                        <li>BUY NOW</li>
                        <li>ACT NOW</li>
                        <li>DON'T MISS OUT</li>
                        <li>GET STARTED!!!</li>
                        <li>GRAB THIS DEAL</li>
                    </ul>
                </div>
            </div>

            <!-- Color Hierarchy & 60/30/10 Rule -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">4. Text Color Hierarchy</div>
                    
                    <div class="space-y-4 mb-6">
                        <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm">
                            <div class="font-bold text-[0.85rem] text-[#55555A] mb-2 uppercase tracking-wide">Light Surface</div>
                            <div class="text-[0.9rem] text-[#1C1C1E]">Obsidian → Copper Text → Neutral Grey</div>
                        </div>
                        <div class="bg-[#1C1C1E] p-4 rounded-sm">
                            <div class="font-bold text-[0.85rem] text-white/50 mb-2 uppercase tracking-wide">Dark Surface</div>
                            <div class="text-[0.9rem] text-[#FAFAFA]">Titanium Frost → Copper → Muted Neutral</div>
                        </div>
                        <div class="bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80')] bg-cover bg-center p-4 rounded-sm relative overflow-hidden border-[0.5px] border-[#55555a26]">
                            <div class="absolute inset-0 bg-[#1C1C1E]/80"></div>
                            <div class="relative z-10">
                                <div class="font-bold text-[0.85rem] text-white/60 mb-2 uppercase tracking-wide">Image Surface</div>
                                <div class="text-[0.9rem] text-[#FAFAFA]">Titanium Frost → Copper</div>
                            </div>
                        </div>
                    </div>
                    
                    <p class="text-[0.9rem] text-[#1C1C1E] font-bold mb-2">Keep the hierarchy restrained.</p>
                    <p class="text-[0.9rem] text-[#55555A]">Do not introduce a new text color simply because the background changed.</p>
                </div>
                
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">5. The 60/30/10 Rule for Text</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-6">For acre&key surfaces, a useful default is:</p>
                    
                    <div class="flex h-4 rounded-sm overflow-hidden mb-6">
                        <div class="w-[60%] bg-[#55555A]"></div>
                        <div class="w-[30%] bg-[#1C1C1E]"></div>
                        <div class="w-[10%] bg-[#804526]"></div>
                    </div>
                    <ul class="text-[0.9rem] text-[#1C1C1E] space-y-2 mb-8">
                        <li class="flex items-center gap-3"><span class="w-3 h-3 bg-[#55555A] rounded-sm"></span> 60% — primary text (Neutral)</li>
                        <li class="flex items-center gap-3"><span class="w-3 h-3 bg-[#1C1C1E] rounded-sm"></span> 30% — secondary/supporting text</li>
                        <li class="flex items-center gap-3"><span class="w-3 h-3 bg-[#804526] rounded-sm"></span> 10% — accent text (Copper)</li>
                    </ul>
                    
                    <p class="text-[0.85rem] text-[#55555A] italic mb-4">This is a hierarchy guideline, not a literal percentage requirement. The majority of information should remain neutral.</p>
                    <p class="text-[0.85rem] text-[#804526] font-bold">Copper should signal importance, not simply make the design look premium.</p>
                </div>
            </div>

            <!-- Non-Negotiable Rules -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#1C1C1E] mb-6">6. Non-Negotiable Rules</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    
                    <div class="bg-white border-[0.5px] border-[#8B3A3A] p-8 rounded-sm border-t-4">
                        <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Never</h4>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>Use copper for every heading.</li>
                            <li>Use white + copper + peach + grey + red in the same component.</li>
                            <li>Put text over a busy image without a controlled contrast zone.</li>
                            <li>Use a heavy black overlay simply to make text readable.</li>
                            <li>Use decorative text colors without a semantic purpose.</li>
                            <li>Use Marcellus for buttons, metadata, or UI controls.</li>
                            <li>Use uppercase for large headlines.</li>
                            <li>Use color as the only method of communicating meaning.</li>
                        </ul>
                    </div>

                    <div class="bg-white border-[0.5px] border-[#2C4C3B] p-8 rounded-sm border-t-4">
                        <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4 flex items-center gap-2"><span class="text-[#2C4C3B]">✓</span> Always</h4>
                        <ol class="text-[0.9rem] text-[#1C1C1E] font-bold space-y-3 mb-6 list-decimal list-inside">
                            <li>Surface first.</li>
                            <li>Contrast second.</li>
                            <li>Hierarchy third.</li>
                            <li>Accent last.</li>
                        </ol>
                        <p class="text-[0.9rem] text-[#55555A] italic border-t-[0.5px] border-[#55555a26] pt-4">The visual hierarchy should still work if all accent colors are removed.</p>
                    </div>
                </div>
            </div>

            <!-- Final Principle -->
            <div class="bg-[#1C1C1E] text-white p-12 rounded-sm mt-12 text-center">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Final System Principle</div>
                <div class="font-serif text-2xl md:text-3xl leading-relaxed mb-6 max-w-4xl mx-auto">"Text should never be colored because it looks better. It should be colored because it has a defined role."</div>
            </div>

        </div>
        """, 'html.parser')
        typo_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

append_surfaces()
