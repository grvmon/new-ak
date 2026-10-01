from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    sec = soup.find(id='17-social')
    if sec:
        sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">17. Social Media</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Social media extends the acre&amp;key design system. It does not introduce a separate visual language. All social assets must inherit the approved color, typography, logo, grid, and spacing systems. Platform specifications can change, but our DNA remains absolute.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Master Tokens & Safe Areas -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-8">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">17.01 Master Social Tokens</h3>
                    <div class="space-y-6">
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-3">Typography Map</div>
                            <ul class="text-[0.8rem] space-y-2 text-[#55555A] font-mono">
                                <li class="flex justify-between border-b-[0.5px] border-[#55555a26] pb-2"><span>Display / Headline</span> <span class="text-[#1C1C1E]">Marcellus 400</span></li>
                                <li class="flex justify-between border-b-[0.5px] border-[#55555a26] pb-2"><span>Body / Subcopy</span> <span class="text-[#1C1C1E]">Manrope 400/500</span></li>
                                <li class="flex justify-between border-b-[0.5px] border-[#55555a26] pb-2"><span>Kicker / Overline</span> <span class="text-[#1C1C1E]">Manrope 700</span></li>
                                <li class="flex justify-between pb-2"><span>Data / CTA</span> <span class="text-[#1C1C1E]">Manrope 600/700</span></li>
                            </ul>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-2">The Dark-Surface Rule</div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Typography creates hierarchy. Copper creates emphasis. Titanium Frost is the primary text color on Obsidian Black. Copper is restricted strictly to Kickers, Key Numbers, and CTAs. Do not use Copper for body copy.</p>
                        </div>
                    </div>
                </div>

                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-sm p-8">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">17.02 Safe-Area System</h3>
                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">Critical content (Logo, Headlines, CTAs, Faces) must never touch the edges or sit under platform UI.</p>
                    
                    <div class="space-y-4">
                        <div class="border-[0.5px] border-[#55555a26] bg-white p-4 rounded-sm">
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Standard (1080px wide)</div>
                            <div class="font-mono text-[0.8rem] text-[#BE7555]">80px minimum on all sides</div>
                        </div>
                        <div class="border-[0.5px] border-[#55555a26] bg-white p-4 rounded-sm">
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Vertical Reels/Stories (9:16)</div>
                            <div class="grid grid-cols-2 gap-2 font-mono text-[0.75rem] text-[#55555A]">
                                <div><span class="text-[#1C1C1E] font-bold">Left/Right:</span> 96px</div>
                                <div><span class="text-[#1C1C1E] font-bold">Top:</span> 250px</div>
                                <div><span class="text-[#1C1C1E] font-bold">Bottom:</span> 350px</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Master Size Matrix -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">17.13 Master Size Matrix</h3>
                <div class="overflow-x-auto border-[0.5px] border-[#55555a26] rounded-sm">
                    <table class="w-full text-[0.8rem] text-left">
                        <thead class="bg-[#FAFAFA] border-b-[0.5px] border-[#55555a26] font-bold tracking-[0.05em] uppercase text-[#1C1C1E] text-[0.7rem]">
                            <tr>
                                <th class="py-4 px-6">Platform</th>
                                <th class="py-4 px-6">Asset Type</th>
                                <th class="py-4 px-6">Master Size</th>
                                <th class="py-4 px-6">Ratio</th>
                                <th class="py-4 px-6">A&amp;K Safe Area</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y-[0.5px] divide-[#55555a26] text-[#55555A] font-mono">
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Instagram / FB</td>
                                <td class="py-4 px-6 font-sans">Primary Feed / Carousel</td>
                                <td class="py-4 px-6">1080 × 1350px</td>
                                <td class="py-4 px-6">4:5</td>
                                <td class="py-4 px-6 text-[#BE7555]">80px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Instagram / FB</td>
                                <td class="py-4 px-6 font-sans">Story / Reel</td>
                                <td class="py-4 px-6">1080 × 1920px</td>
                                <td class="py-4 px-6">9:16</td>
                                <td class="py-4 px-6 text-[#BE7555]">96 / 250 / 96 / 350px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">LinkedIn</td>
                                <td class="py-4 px-6 font-sans">PDF / Document</td>
                                <td class="py-4 px-6">2480 × 3508px</td>
                                <td class="py-4 px-6">A4</td>
                                <td class="py-4 px-6 text-[#BE7555]">80-100px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">LinkedIn</td>
                                <td class="py-4 px-6 font-sans">Link Preview</td>
                                <td class="py-4 px-6">1200 × 627px</td>
                                <td class="py-4 px-6">1.91:1</td>
                                <td class="py-4 px-6 text-[#BE7555]">60px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">X (Twitter)</td>
                                <td class="py-4 px-6 font-sans">Primary Feed</td>
                                <td class="py-4 px-6">1080 × 1440px</td>
                                <td class="py-4 px-6">3:4</td>
                                <td class="py-4 px-6 text-[#BE7555]">80px</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Master Template Library -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">17.12 Master Template Library</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">The social system uses six definitive templates. Do not invent dozens of random layouts.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-[#1C1C1E] border-[0.5px] border-[#55555a26] rounded-sm p-6 flex flex-col justify-between h-[280px]">
                        <div>
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-4">01 — Dark Editorial</div>
                            <div class="font-serif text-[1.5rem] text-[#FAFAFA] leading-tight mb-2">Institutional Intelligence.</div>
                            <div class="font-sans text-[0.8rem] text-[#FAFAFA]/70">Obsidian background, Copper kicker, Titanium Marcellus headline.</div>
                        </div>
                        <div class="font-logo text-[#FAFAFA] text-[0.9rem]">acre&amp;key</div>
                    </div>
                    
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-6 flex flex-col justify-between h-[280px]">
                        <div>
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-4">02 — Light Editorial</div>
                            <div class="font-serif text-[1.5rem] text-[#1C1C1E] leading-tight mb-2">Market Analysis.</div>
                            <div class="font-sans text-[0.8rem] text-[#55555A]">Titanium Frost background, Obsidian Marcellus headline.</div>
                        </div>
                        <div class="font-logo text-[#1C1C1E] text-[0.9rem]">acre&amp;key</div>
                    </div>

                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-6 flex flex-col justify-between h-[280px] relative overflow-hidden group">
                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_pool_evening.webp')] bg-cover bg-center grayscale opacity-80 mix-blend-multiply group-hover:grayscale-0 transition-all duration-700"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] to-transparent h-[60%] mt-auto"></div>
                        <div class="relative z-10 flex flex-col justify-between h-full">
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-white drop-shadow-md mb-4">03 — Photography</div>
                            <div>
                                <div class="font-serif text-[1.25rem] text-white leading-tight mb-1">Architectural Restraint.</div>
                                <div class="font-sans text-[0.7rem] text-white/80">Full-bleed image, Copper accent.</div>
                                <div class="font-logo text-white text-[0.9rem] mt-4">acre&amp;key</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Social QA Checklist -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">17.14 Social QA</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Brand &amp; Composition Enforcements</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-3">
                            <li class="flex gap-2"><span class="text-[#8B3A3A] font-bold">✕</span> No gold, champagne, or fake luxury aesthetics.</li>
                            <li class="flex gap-2"><span class="text-[#8B3A3A] font-bold">✕</span> No exclamation marks or fake urgency ("Act Now!").</li>
                            <li class="flex gap-2"><span class="text-[#2C4C3B] font-bold">✓</span> One idea per slide/frame. If it reads like a webpage, it's too dense.</li>
                            <li class="flex gap-2"><span class="text-[#2C4C3B] font-bold">✓</span> Every meaningful visual must have structural alt-text.</li>
                        </ul>
                    </div>
                    
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">The Final Brand Test</div>
                        <p class="text-[0.9rem] text-[#1C1C1E] leading-relaxed italic border-l-[2px] border-[#1C1C1E] pl-4">
                            "Remove the logo. If the asset still looks recognizably like acre&amp;key, the social system is working. The platform changes. acre&amp;key does not."
                        </p>
                    </div>
                </div>
            </div>

        </div>
        """, 'html.parser')
        sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
