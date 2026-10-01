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
        # Find the very last div of 05-typography, or just append to it
        
        new_block = BeautifulSoup("""
        <div class="mt-16">
            <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">3. Text on Buttons</div>
            <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-8 max-w-3xl">Buttons are functional UI and follow stricter rules than editorial text. Typography inside interactive elements must be uncompromisingly legible and free from marketing desperation.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
                
                <!-- Primary CTA -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Primary CTA</h4>
                    
                    <div class="mb-6 flex justify-center py-6 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-sm">
                        <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-6 py-3 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors flex items-center gap-2 shadow-sm">
                            Book advisory call <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
                        </button>
                    </div>

                    <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                        <li>Copper background + high-contrast white text.</li>
                        <li>Use <strong class="text-[#1C1C1E]">Manrope</strong> at <strong class="text-[#1C1C1E]">600 weight</strong>.</li>
                        <li>Sentence case. No uppercase CTA copy unless specifically required.</li>
                        <li>No exclamation marks.</li>
                        <li>Do not use Marcellus inside buttons.</li>
                        <li>Icon (if present) must be subordinate to the label (1.5px stroke).</li>
                    </ul>
                </div>

                <!-- Secondary Button -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Secondary Button</h4>
                    
                    <div class="mb-6 flex justify-center py-6 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-sm gap-4 flex-wrap">
                        <button class="bg-[#1C1C1E] hover:bg-black text-white px-6 py-3 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors shadow-sm">
                            View analysis
                        </button>
                        <button class="bg-transparent border-[1px] border-[#1C1C1E] text-[#1C1C1E] hover:bg-black/5 px-6 py-3 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors">
                            Compare assets
                        </button>
                    </div>

                    <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                        <li>Use a restrained outlined or tonal treatment (Obsidian fill).</li>
                        <li>No unnecessary fill colors (no grey or blue).</li>
                        <li>No decorative gradients.</li>
                        <li>Border and text must maintain AAA contrast.</li>
                        <li>Must remain visually subordinate to the primary CTA.</li>
                    </ul>
                </div>
            </div>

            <!-- Button Copy Rules -->
            <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Button Copy Rules</h4>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#2C4C3B] mb-4 flex items-center gap-2">
                            <span class="bg-[#2C4C3B] text-white w-4 h-4 rounded-sm flex items-center justify-center">✓</span> Prefer (Advisory Tone)
                        </div>
                        <ul class="text-[0.9rem] text-[#1C1C1E] space-y-3 font-semibold">
                            <li>Book advisory call</li>
                            <li>Request consultation</li>
                            <li>View analysis</li>
                            <li>Explore properties</li>
                            <li>See the assessment</li>
                            <li>Speak with an advisor</li>
                        </ul>
                    </div>
                    <div>
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-4 flex items-center gap-2">
                            <span class="bg-[#8B3A3A] text-white w-4 h-4 rounded-sm flex items-center justify-center">✕</span> Avoid (Broker Tone)
                        </div>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-3 line-through">
                            <li>BUY NOW</li>
                            <li>ACT NOW</li>
                            <li>DON'T MISS OUT</li>
                            <li>GET STARTED!!!</li>
                            <li>GRAB THIS DEAL</li>
                        </ul>
                    </div>
                </div>
            </div>
            
        </div>
        """, 'html.parser')
        
        # Append just before the end of the section
        typo_sec.append(new_block)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
