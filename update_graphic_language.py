from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    sec = soup.find(id='09-graphic')
    if sec:
        sec.clear()
        
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">09. Graphic Language</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The graphic language of acre&key is derived entirely from architectural drafting and technical precision. Graphics should look unmistakably acre&key, even without the logo.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Lines, Grids & Geometry -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Structural Primitives</div>
                    <ul class="text-[0.95rem] text-[#55555A] space-y-6">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Hairlines & Dividers</strong>
                            We rely heavily on the <code class="bg-black/5 px-1 rounded-sm text-[#804526]">0.5px</code> hairline. Dividers are not decorative; they create explicit spatial relationships and structural boundaries. The standard border color is <code class="bg-black/5 px-1 rounded-sm">rgba(85,85,90,0.15)</code>.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Geometry & Radius</strong>
                            Geometry is strict. We use a global <code class="bg-black/5 px-1 rounded-sm">4px</code> micro-edge radius. Never use pill shapes, soft curves, blobs, or aggressive circles. Corners should feel machined, not soft.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Exposed Grids</strong>
                            It is acceptable, and often encouraged, to expose the underlying grid. This reinforces the institutional, data-driven nature of the brand.
                        </li>
                    </ul>
                </div>

                <!-- Visual Example: The Grid Box -->
                <div class="bg-white p-8 flex flex-col justify-center border-[0.5px] border-[#55555a26] rounded-sm relative overflow-hidden">
                    <div class="absolute inset-0 border-[0.5px] border-[#55555a26] opacity-30" style="background-image: linear-gradient(to right, rgba(85,85,90,0.15) 1px, transparent 1px), linear-gradient(to bottom, rgba(85,85,90,0.15) 1px, transparent 1px); background-size: 20px 20px;"></div>
                    <div class="relative z-10 w-full h-[120px] border-[0.5px] border-[#1C1C1E] bg-[#FAFAFA] rounded-sm flex items-center justify-center shadow-none">
                        <div class="absolute top-2 left-2 flex items-center gap-2">
                            <span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>
                            <span class="text-[0.65rem] font-mono text-[#55555A] tracking-wider">0.5PX HAIRLINE</span>
                        </div>
                        <div class="absolute bottom-2 right-2 flex items-center gap-2">
                            <span class="text-[0.65rem] font-mono text-[#55555A] tracking-wider">R: 4PX</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Maps, Blueprints & Data -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Data &amp; Technical Graphics</div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.1rem] mb-3">Maps &amp; Location</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Maps must be stripped of generic consumer details. Use high-contrast monochromatic styles (Obsidian/Titanium base). Roads and boundaries should appear as technical linework. Only highlight the asset and key infrastructure.</p>
                    </div>
                    
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.1rem] mb-3">Blueprint Graphics</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Floorplans, masterplans, and site diagrams should be stripped of builder branding, 3D furniture, and saturated colors. Redraw them if necessary using our strict 0.5px geometry and single-color fills.</p>
                    </div>
                    
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.1rem] mb-3">Data Visualization</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Charts and graphs must avoid default spreadsheet colors. Use Titanium/Obsidian as the base, and use Copper to single out the key data point. Keep axes lines ultra-thin (0.5px).</p>
                    </div>
                </div>

                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm flex flex-col md:flex-row gap-8 items-center">
                    <div class="shrink-0 flex gap-4 w-[240px] h-[120px] items-end border-b-[0.5px] border-l-[0.5px] border-[#1C1C1E] pb-2 pl-2">
                        <div class="w-8 bg-[#55555A]/20 h-[40%] rounded-sm"></div>
                        <div class="w-8 bg-[#55555A]/20 h-[60%] rounded-sm"></div>
                        <div class="w-8 bg-[#BE7555] h-[90%] rounded-sm"></div>
                        <div class="w-8 bg-[#55555A]/20 h-[50%] rounded-sm"></div>
                    </div>
                    <div>
                        <div class="text-[0.85rem] text-[#1C1C1E] font-bold mb-1">Approved Data Expression</div>
                        <div class="text-[0.85rem] text-[#55555A] max-w-lg">Notice the absence of grid lines, the 0.5px strict axes, and the fact that Copper is used exclusively to highlight the focal data point, rather than coloring every bar differently.</div>
                    </div>
                </div>
            </div>

            <!-- Decorative Elements -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Decorative Elements</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-4">Decoration is permitted only if it simulates technical metadata.</p>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Crosshairs & Registration Marks</strong>
                            Subtle 0.5px crosshairs at the corners of imagery or hero sections reinforce precision.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Coordinate Tags</strong>
                            Using exact lat/long coordinates or timestamps as microcopy in empty corners adds to the investigative/diligence aesthetic.
                        </li>
                    </ul>
                </div>
                
                <div class="relative bg-white border-[0.5px] border-[#55555a26] min-h-[200px] flex items-center justify-center p-8 rounded-sm">
                    <!-- Fake Crosshairs -->
                    <div class="absolute top-4 left-4 w-4 h-4 border-t-[0.5px] border-l-[0.5px] border-[#1C1C1E]"></div>
                    <div class="absolute top-4 right-4 w-4 h-4 border-t-[0.5px] border-r-[0.5px] border-[#1C1C1E]"></div>
                    <div class="absolute bottom-4 left-4 w-4 h-4 border-b-[0.5px] border-l-[0.5px] border-[#1C1C1E]"></div>
                    <div class="absolute bottom-4 right-4 w-4 h-4 border-b-[0.5px] border-r-[0.5px] border-[#1C1C1E]"></div>
                    
                    <div class="text-[0.65rem] font-mono text-[#55555A] uppercase tracking-[0.15em]">
                        12°58'31.8"N 77°35'15.5"E
                    </div>
                </div>
            </div>

            <!-- Prohibited Graphic Styles -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#8B3A3A] mb-6">Prohibited Graphic Styles</div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="border-t-2 border-[#8B3A3A] pt-4">
                        <div class="font-bold text-[#1C1C1E] mb-2 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Abstract Blobs</div>
                        <p class="text-[0.85rem] text-[#55555A]">No organic, curvy shapes used as background elements to fill space.</p>
                    </div>
                    <div class="border-t-2 border-[#8B3A3A] pt-4">
                        <div class="font-bold text-[#1C1C1E] mb-2 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> 3D / Isometric Art</div>
                        <p class="text-[0.85rem] text-[#55555A]">No floating 3D houses, coins, or glossy tech-startup illustrations.</p>
                    </div>
                    <div class="border-t-2 border-[#8B3A3A] pt-4">
                        <div class="font-bold text-[#1C1C1E] mb-2 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Drop Shadows</div>
                        <p class="text-[0.85rem] text-[#55555A]">Do not use drop shadows to create depth. Use solid lines and contrast.</p>
                    </div>
                    <div class="border-t-2 border-[#8B3A3A] pt-4">
                        <div class="font-bold text-[#1C1C1E] mb-2 flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Gradient Meshes</div>
                        <p class="text-[0.85rem] text-[#55555A]">No soft, blended "aurora" background gradients.</p>
                    </div>
                </div>
            </div>

            <!-- Decision Rule Slide -->
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-8">Graphic Language Rule</div>
                <p class="text-[20px] text-[#FAFAFA] font-normal leading-relaxed mb-10 max-w-2xl">Before implementing a graphic, illustration, map, or chart, ask:</p>
                <div class="space-y-6 mb-12">
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">01</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Is it structurally derived from architectural drafting or technical analysis?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">02</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Does it rely on 0.5px geometry rather than depth, shadow, or gradients?</div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="text-[#BE7555] font-bold text-[16px] w-8 shrink-0 pt-0.5">03</div>
                        <div class="text-[18px] text-[#FAFAFA]/80 leading-relaxed font-normal">Is color restricted strictly to Titanium, Obsidian, and Copper focal points?</div>
                    </div>
                </div>
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If a graphic looks like it belongs on a generic SaaS or consumer app, it does not belong on acre&amp;key.</div>
            </div>

        </div>
        """, 'html.parser')
        sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
