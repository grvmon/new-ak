from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    photo_sec = soup.find(id='08-photography')
    if photo_sec:
        photo_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">08. Photography &amp; Art Direction</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">As a premium real estate brand, we do not use dark, moody, or desaturated images. Our visual signature is <strong class="text-[#1C1C1E]">Extreme Luxury and Brilliance</strong>. Spaces must look expansive, light-filled, and pristine, while still maintaining strict 7.0:1 (AAA) contrast zones for typography.</p>
        
        <div class="space-y-16 font-sans">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Lighting &amp; Grading</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Brilliant Natural Light</strong> Shoot at golden hour or high-noon for brilliant, expansive lighting. Do not crush the shadows. Spaces should look inviting and vast.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Vibrant but Refined</strong> No grayscale. Images must be slightly bumped in brightness and saturation (<code class="bg-black/5 px-1 rounded-sm">brightness-[1.05] saturate-[1.1]</code>) to feel alive.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Color Temperature</strong> Lean slightly warm (golden/copper undertones) rather than cold/blue to match our Copper brand accent.</li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Subject Matter Rules</h3>
                    <div class="space-y-4">
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Architecture</div>
                            <p class="text-[0.85rem] text-[#55555A]">Perfect verticals. Expansive skies. Emphasize scale and light.</p>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Interiors</div>
                            <p class="text-[0.85rem] text-[#55555A]">Windows must be blown out slightly to emphasize daylight. Avoid dark, moody cave-like rooms.</p>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">People</div>
                            <p class="text-[0.85rem] text-[#55555A]">Aspirational, in-motion, elegant. People exist to show scale and livability.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- The AAA Contrast Rule -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">The 7AAA Contrast Paradox</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">How do we overlay white text on bright, luxury images? We use <strong class="text-[#1C1C1E]">anchored gradient zones</strong>. The image remains 90% brilliant, but the specific corner holding text fades smoothly into Obsidian to guarantee WCAG Level AAA compliance (7.0:1).</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                    <div>
                        <div class="bg-white p-4 border-[0.5px] border-[#55555a26] rounded-sm mb-6 inline-block shadow-sm">
                            <div class="font-bold text-[0.85rem] text-[#2C4C3B] mb-1">✓ Correct AAA Handling</div>
                            <div class="text-[0.8rem] text-[#55555A]">Bright Image + Localized Obsidian Fade</div>
                        </div>
                        <ul class="text-[0.85rem] space-y-3">
                            <li class="flex items-start gap-2"><span class="text-[#1C1C1E] font-bold mt-0.5">1.</span> <span class="text-[#55555A]">The subject matter stays brilliantly lit.</span></li>
                            <li class="flex items-start gap-2"><span class="text-[#1C1C1E] font-bold mt-0.5">2.</span> <span class="text-[#55555A]">We do not put a heavy black overlay over the *entire* image.</span></li>
                            <li class="flex items-start gap-2"><span class="text-[#1C1C1E] font-bold mt-0.5">3.</span> <span class="text-[#55555A]">Typography sits safely in the gradient pocket, scoring >7.0:1 contrast.</span></li>
                        </ul>
                    </div>
                    
                    <div class="relative w-full h-[300px] rounded-sm overflow-hidden shadow-xl border-[0.5px] border-[#1C1C1E]">
                        <!-- Bright Luxury Image -->
                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_tower_facade_day.webp')] bg-cover bg-center brightness-[1.05] saturate-[1.1] contrast-[1.05]"></div>
                        <!-- Localized Gradient (Bottom only) -->
                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/80 to-transparent h-[60%] mt-auto"></div>
                        
                        <div class="absolute bottom-6 left-6 right-6">
                            <div class="font-serif text-[1.5rem] text-[#FAFAFA] leading-tight mb-2">Expansive Light &amp; Luxury</div>
                            <div class="font-sans text-[0.85rem] text-[#FAFAFA]/90">Text reads perfectly at AAA standards while the tower above remains brilliantly lit.</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Banned Styles -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Zero Tolerance — Banned Styles</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="bg-white border-[0.5px] border-[#8B3A3A]/40 p-4 rounded-sm border-t-[4px] border-t-[#8B3A3A]">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-2 flex items-center gap-2">✕ Moody / Grayscale</div>
                        <p class="text-[0.8rem] text-[#55555A]">We are not a gothic architecture firm. Do not desaturate or darken the asset.</p>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#8B3A3A]/40 p-4 rounded-sm border-t-[4px] border-t-[#8B3A3A]">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-2 flex items-center gap-2">✕ Blanket Black Overlays</div>
                        <p class="text-[0.8rem] text-[#55555A]">Do not slap a 50% black square over a beautiful image just to make text readable. Use anchored gradients.</p>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#8B3A3A]/40 p-4 rounded-sm border-t-[4px] border-t-[#8B3A3A]">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-2 flex items-center gap-2">✕ HDR Real Estate</div>
                        <p class="text-[0.8rem] text-[#55555A]">No unnatural shadow lifting or glowing windows.</p>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#8B3A3A]/40 p-4 rounded-sm border-t-[4px] border-t-[#8B3A3A]">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-2 flex items-center gap-2">✕ Ultra-Wide Lenses</div>
                        <p class="text-[0.8rem] text-[#55555A]">No 10mm distortion making small rooms look massive.</p>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Luxury is light, space, and clarity. The photography must reflect the extreme premium nature of the assets, without compromising textual legibility.</div>
            </div>
            
        </div>
        """, 'html.parser')
        photo_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
