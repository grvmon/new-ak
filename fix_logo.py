from bs4 import BeautifulSoup

def update_logo():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    logo_sec = soup.find(id='03-logo')
    if logo_sec:
        logo_sec.clear()
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">03. Logo &amp; Identity</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The typographic mark must maintain strict aesthetic authority across all environments. We enforce a <strong>Strict Monochrome Architecture</strong> to prevent the mark from feeling like a startup. Nobody should ever have to guess how to place this logo.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Rules & Spatial Dimensions -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Ampersand & Version -->
                <div class="border-[0.5px] border-[#55555a26] bg-[#FAFAFA] p-8 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">The Typographic Mark</div>
                    <div class="font-serif text-4xl text-[#1C1C1E] tracking-tighter mb-8 border-b-[0.5px] border-[#55555a26] pb-8">acre&amp;key</div>
                    <ul class="text-[0.95rem] text-[#55555A] space-y-4">
                        <li><strong class="text-[#1C1C1E] block">The Ampersand Rule:</strong> The ampersand is the structural hinge of the brand. It is never colorized, never bolded, and never italicized. It strictly follows the monochrome color of the surrounding letters.</li>
                    </ul>
                </div>

                <!-- Clear Space & Size -->
                <div class="border-[0.5px] border-[#55555a26] bg-[#FAFAFA] p-8 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Spatial Architecture</div>
                    <div class="grid grid-cols-2 gap-8">
                        <div>
                            <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Clear Space</div>
                            <div class="text-[0.9rem] text-[#55555A] leading-relaxed">The protective boundary around the logo is defined by the height of the letter <strong class="text-[#1C1C1E] font-serif">"k"</strong>. No UI elements or typography may enter this zone.</div>
                        </div>
                        <div>
                            <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Minimum Size</div>
                            <div class="text-[0.9rem] text-[#55555A] leading-relaxed">
                                <span class="block mb-1"><strong>Digital:</strong> 120px width</span>
                                <span class="block mb-1"><strong>Print:</strong> 30mm width</span>
                                <span class="block"><strong>Favicon:</strong> Use the standalone 'a&amp;k' monogram.</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Contextual Environments -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Approved Canvas Environments</div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <!-- Light -->
                    <div class="h-[160px] bg-[#FAFAFA] border-[0.5px] border-[#55555a26] flex flex-col items-center justify-center relative rounded-sm">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-[#55555A]">Titanium Frost</div>
                        <div class="font-serif text-2xl text-[#1C1C1E] tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Dark -->
                    <div class="h-[160px] bg-[#1C1C1E] flex flex-col items-center justify-center relative rounded-sm">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/50">Obsidian Black</div>
                        <div class="font-serif text-2xl text-white tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Copper -->
                    <div class="h-[160px] bg-[#9F5334] flex flex-col items-center justify-center relative rounded-sm">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/60">Primary Copper</div>
                        <div class="font-serif text-2xl text-white tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Image/Video -->
                    <div class="h-[160px] relative flex flex-col items-center justify-center rounded-sm overflow-hidden">
                        <div class="absolute inset-0 bg-[#1C1C1E]"></div>
                        <div class="absolute inset-0 opacity-40 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center grayscale contrast-[1.2]"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E]/80 to-transparent"></div>
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/80 z-10">Image / Video</div>
                        <div class="font-serif text-2xl text-white tracking-tighter z-10">acre&amp;key</div>
                    </div>
                </div>
            </div>

            <!-- Banned Usage -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#8B3A3A] mb-6">Incorrect Usage (Zero Tolerance)</div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <!-- Colorizing Ampersand -->
                    <div class="h-[160px] bg-white border-[0.5px] border-[#8B3A3A]/30 flex flex-col items-center justify-center relative rounded-sm group">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-[#8B3A3A]">Don't Colorize</div>
                        <div class="font-serif text-2xl text-[#1C1C1E] tracking-tighter line-through opacity-70">acre<span class="text-[#804526]">&amp;</span>key</div>
                    </div>
                    <!-- Stretching -->
                    <div class="h-[160px] bg-white border-[0.5px] border-[#8B3A3A]/30 flex flex-col items-center justify-center relative rounded-sm group">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-[#8B3A3A]">Don't Stretch</div>
                        <div class="font-serif text-2xl text-[#1C1C1E] tracking-tighter line-through opacity-70 scale-y-150">acre&amp;key</div>
                    </div>
                    <!-- Low Contrast/Raw Image -->
                    <div class="h-[160px] relative flex flex-col items-center justify-center rounded-sm overflow-hidden border-[0.5px] border-[#8B3A3A]/30">
                        <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center"></div>
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white bg-[#8B3A3A] px-2 py-0.5 rounded-sm z-10">Don't overlay raw images</div>
                        <div class="font-serif text-2xl text-[#1C1C1E] tracking-tighter z-10 shadow-sm opacity-90 line-through">acre&amp;key</div>
                    </div>
                    <!-- Generic Luxury Gold -->
                    <div class="h-[160px] bg-[#1C1C1E] border-[0.5px] border-[#8B3A3A]/30 flex flex-col items-center justify-center relative rounded-sm group">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-[#8B3A3A]">No "Luxury" Gold</div>
                        <div class="font-serif text-2xl text-[#D4AF37] tracking-tighter line-through opacity-90">acre&amp;key</div>
                    </div>
                </div>
            </div>

        </div>
        """, 'html.parser')
        logo_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update_logo()
