from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    maps_sec = soup.find(id='16-maps')
    if maps_sec:
        maps_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">16. Maps &amp; Location</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Default Google Maps styling is banned. Maps are not just geographical utilities; they are architectural data visualizations. All mapping instances must strictly inherit the acre&amp;key color palette and typography.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Map Styling & Base Layer -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Base Map Architecture</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Color Palette</strong> All base maps must be desaturated. Landmass is <code class="bg-black/5 px-1 rounded-sm text-[#55555A]">#FAFAFA</code> or <code class="bg-black/5 px-1 rounded-sm text-[#55555A]">#F5F5F5</code>. Water bodies are <code class="bg-black/5 px-1 rounded-sm text-[#1C1C1E]">#1C1C1E</code> at 10% opacity.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Road Network</strong> Highways and arterials are rendered as strict 0.5px or 1px hairlines (Titanium or Obsidian). <strong class="text-[#8B3A3A]">Yellow or orange Google default highways are strictly prohibited.</strong></li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Micro-Market Boundaries</strong> Drawn with a 0.5px Copper or Obsidian stroke with a maximum 5% opacity fill. No heavy, opaque shapes.</li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Pins &amp; Markers</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-6">Generic teardrop map pins are banned. Markers must be geometric, technical, and precise.</p>
                    
                    <div class="grid grid-cols-3 gap-4">
                        <div class="flex flex-col items-center gap-2 text-center">
                            <div class="w-4 h-4 rounded-sm bg-[#BE7555] border-[0.5px] border-[#1C1C1E] flex items-center justify-center"></div>
                            <span class="text-[0.65rem] font-bold uppercase tracking-widest text-[#1C1C1E]">Subject Asset</span>
                        </div>
                        <div class="flex flex-col items-center gap-2 text-center">
                            <div class="w-3 h-3 rounded-full bg-[#1C1C1E]"></div>
                            <span class="text-[0.65rem] font-bold uppercase tracking-widest text-[#55555A]">Infra / Metro</span>
                        </div>
                        <div class="flex flex-col items-center gap-2 text-center">
                            <div class="w-3 h-3 rounded-full border-[1.5px] border-[#1C1C1E] bg-white"></div>
                            <span class="text-[0.65rem] font-bold uppercase tracking-widest text-[#55555A]">Social / Schools</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Route & Distance Rules -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Distance &amp; Travel Time Axioms</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#2C4C3B] mb-4 flex items-center gap-2">
                            <span class="bg-[#2C4C3B] text-white w-4 h-4 rounded-sm flex items-center justify-center">✓</span> Verifiable Data
                        </div>
                        <ul class="text-[0.9rem] text-[#1C1C1E] space-y-3 font-medium">
                            <li><span class="text-[#55555A] mr-2">Distance:</span> 4.2 km via Outer Ring Road</li>
                            <li><span class="text-[#55555A] mr-2">Drive Time:</span> 14 mins (Off-Peak)</li>
                            <li><span class="text-[#55555A] mr-2">Drive Time:</span> 35 mins (Peak Traffic)</li>
                            <li><span class="text-[#55555A] mr-2">Metro Access:</span> 450m walking distance</li>
                        </ul>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-4 flex items-center gap-2">
                            <span class="bg-[#8B3A3A] text-white w-4 h-4 rounded-sm flex items-center justify-center">✕</span> Marketing Fluff (Banned)
                        </div>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-3 line-through">
                            <li>Minutes away from everything!</li>
                            <li>Stone's throw from the airport</li>
                            <li>In the heart of the city</li>
                            <li>Close proximity to top schools</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Conceptual Map Mockup -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: The Architectural Map</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Live implementation of the mapping component. Notice the absolute lack of visual clutter. Information is surfaced via structured legend cards overlaying the map context.</p>
                
                <div class="relative w-full h-[500px] border-[0.5px] border-[#1C1C1E] rounded-sm overflow-hidden bg-[#E8E8E8] flex items-center justify-center group shadow-xl">
                    <!-- Conceptual Map Background (using grid patterns and strict colors) -->
                    <div class="absolute inset-0 opacity-20 bg-[linear-gradient(#1C1C1E_0.5px,transparent_0.5px),linear-gradient(90deg,#1C1C1E_0.5px,transparent_0.5px)] bg-[size:40px_40px]"></div>
                    
                    <!-- Simulated Road Network -->
                    <svg class="absolute inset-0 w-full h-full opacity-40" viewBox="0 0 800 500" preserveAspectRatio="none">
                        <path d="M 0,250 C 200,300 400,100 800,200" fill="none" stroke="#1C1C1E" stroke-width="2" stroke-dasharray="8 4"/>
                        <path d="M 200,0 L 300,500" fill="none" stroke="#BE7555" stroke-width="1.5" />
                        <path d="M 500,0 C 450,250 600,400 800,500" fill="none" stroke="#1C1C1E" stroke-width="1" />
                    </svg>

                    <!-- Markers -->
                    <div class="absolute top-[280px] left-[280px] flex items-center gap-2 z-10">
                        <div class="w-4 h-4 bg-[#BE7555] rounded-sm ring-4 ring-[#BE7555]/20 animate-pulse"></div>
                        <div class="bg-white px-2 py-1 border-[0.5px] border-[#1C1C1E] text-[0.65rem] font-bold uppercase tracking-widest rounded-sm text-[#1C1C1E] shadow-sm">Prestige Evergreen</div>
                    </div>
                    
                    <div class="absolute top-[180px] left-[580px] flex items-center gap-2 z-10">
                        <div class="w-3 h-3 bg-[#1C1C1E] rounded-full"></div>
                        <div class="bg-white/80 backdrop-blur-sm px-2 py-1 border-[0.5px] border-[#1C1C1E]/20 text-[0.65rem] font-semibold uppercase tracking-widest rounded-sm text-[#55555A]">Hope Farm Metro (1.2 km)</div>
                    </div>
                    
                    <div class="absolute top-[380px] left-[350px] flex items-center gap-2 z-10">
                        <div class="w-3 h-3 border-[1.5px] border-[#1C1C1E] rounded-full bg-white"></div>
                        <div class="bg-white/80 backdrop-blur-sm px-2 py-1 border-[0.5px] border-[#1C1C1E]/20 text-[0.65rem] font-semibold uppercase tracking-widest rounded-sm text-[#55555A]">Tech Park (4.2 km)</div>
                    </div>

                    <!-- Overlay Legend Card -->
                    <div class="absolute bottom-8 right-8 bg-white border-[0.5px] border-[#1C1C1E] p-6 rounded-sm shadow-xl w-[280px]">
                        <div class="font-sans text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#1C1C1E] mb-4 border-b-[0.5px] border-[#55555a26] pb-2">Location Context</div>
                        
                        <div class="space-y-4">
                            <div>
                                <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Employment Hubs</div>
                                <div class="text-[0.85rem] font-semibold text-[#1C1C1E] flex justify-between">ITPB Whitefield <span>14 mins</span></div>
                            </div>
                            <div>
                                <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Infrastructure</div>
                                <div class="text-[0.85rem] font-semibold text-[#1C1C1E] flex justify-between">Upcoming Metro <span>450 m</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Location is a matter of mathematics, not marketing. Give the user coordinates, exact radii, and peak travel times. Let the data sell the asset.</div>
            </div>

        </div>
        """, 'html.parser')
        maps_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
