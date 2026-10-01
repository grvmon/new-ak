from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    sec = soup.find(id='18-paid')
    if sec:
        sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">18. Paid Advertising</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Paid advertising extends the acre&amp;key design system into performance environments. Paid creative must remain institutional, editorial, precise, and buyer-first while communicating the proposition immediately. Performance changes the message. It does not change the brand.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Principles -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-[#1C1C1E] p-8 rounded-sm text-white">
                    <h3 class="font-serif text-[1.25rem] text-[#FAFAFA] mb-6">The Four-Question Rule</h3>
                    <p class="text-[0.85rem] text-white/70 mb-4">Every ad must answer four questions immediately without requiring the viewer to read the caption:</p>
                    <ol class="list-decimal list-inside text-[0.9rem] font-bold space-y-2 mb-6">
                        <li>What is this?</li>
                        <li>Who is it for?</li>
                        <li>Why does it matter?</li>
                        <li>What should I do next?</li>
                    </ol>
                    <div class="border-t-[0.5px] border-white/20 pt-4">
                        <div class="text-[0.7rem] uppercase tracking-[0.1em] text-[#BE7555] mb-1">Priority Hierarchy</div>
                        <div class="text-[0.85rem]">Clarity → Relevance → Trust → Action</div>
                    </div>
                </div>

                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Correct vs. Incorrect Tone</h3>
                    <div class="space-y-6">
                        <div>
                            <div class="flex items-center gap-2 mb-2">
                                <span class="text-[#2C4C3B] font-bold">✓ Correct</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-2 py-0.5 rounded-sm">Institutional</span>
                            </div>
                            <div class="border-l-[2px] border-[#2C4C3B] pl-4">
                                <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-1">BUYING A HOME IN BENGALURU?</div>
                                <div class="text-[0.8rem] text-[#55555A]">Buy with clarity. Independent evaluation before you commit.</div>
                            </div>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-2">
                                <span class="text-[#8B3A3A] font-bold">✕ Incorrect</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-2 py-0.5 rounded-sm">Broker Marketing</span>
                            </div>
                            <div class="border-l-[2px] border-[#8B3A3A] pl-4">
                                <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-1">YOUR DREAM LUXURY HOME AWAITS!</div>
                                <div class="text-[0.8rem] text-[#55555A]">EXCLUSIVE LIMITED-TIME OPPORTUNITY! BOOK NOW!!!</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Color Application Matrices -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">18.21 Color Application Samples</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    
                    <!-- Dark Modality -->
                    <div class="bg-[#1C1C1E] p-6 rounded-sm flex flex-col justify-between h-[300px]">
                        <div>
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-4">BACKGROUND: Obsidian Black</div>
                            <div class="font-serif text-[1.25rem] text-[#FAFAFA] leading-tight mb-2">Titanium Frost<br>Marcellus Headline</div>
                            <div class="font-sans text-[0.8rem] text-[#FAFAFA]/70">Titanium Frost / Manrope Body</div>
                        </div>
                        <div class="flex items-center justify-between">
                            <button class="bg-[#BE7555] text-white px-4 py-2 text-[0.7rem] font-bold uppercase tracking-[0.1em] rounded-sm">CTA Button</button>
                            <div class="font-logo text-[#FAFAFA] text-[0.9rem]">acre&amp;key</div>
                        </div>
                    </div>

                    <!-- Light Modality -->
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm flex flex-col justify-between h-[300px]">
                        <div>
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-[#804526] mb-4">BACKGROUND: Titanium Frost</div>
                            <div class="font-serif text-[1.25rem] text-[#1C1C1E] leading-tight mb-2">Obsidian Black<br>Marcellus Headline</div>
                            <div class="font-sans text-[0.8rem] text-[#55555A]">Neutral Grey / Manrope Body</div>
                        </div>
                        <div class="flex items-center justify-between">
                            <button class="bg-[#BE7555] text-white px-4 py-2 text-[0.7rem] font-bold uppercase tracking-[0.1em] rounded-sm">CTA Button</button>
                            <div class="font-logo text-[#1C1C1E] text-[0.9rem]">acre&amp;key</div>
                        </div>
                    </div>

                    <!-- Photography Modality -->
                    <div class="relative bg-white border-[0.5px] border-[#55555a26] rounded-sm p-6 flex flex-col justify-between h-[300px] overflow-hidden">
                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_pool_evening.webp')] bg-cover bg-center"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent"></div>
                        <div class="relative z-10 flex flex-col justify-between h-full">
                            <div class="text-[0.6rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-4">BACKGROUND: Controlled Image</div>
                            <div class="mt-auto">
                                <div class="font-serif text-[1.25rem] text-[#FAFAFA] leading-tight mb-2">Titanium Frost Headline</div>
                                <div class="font-sans text-[0.8rem] text-[#FAFAFA]/90 mb-4">Titanium Frost Body</div>
                                <div class="flex items-center justify-between">
                                    <button class="bg-[#BE7555] text-white px-4 py-2 text-[0.7rem] font-bold uppercase tracking-[0.1em] rounded-sm">CTA Button</button>
                                    <div class="font-logo text-[#FAFAFA] text-[0.9rem]">acre&amp;key</div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Master Size Matrix -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">18.22 Paid Master Size Matrix</h3>
                <div class="overflow-x-auto border-[0.5px] border-[#55555a26] rounded-sm">
                    <table class="w-full text-[0.8rem] text-left">
                        <thead class="bg-[#FAFAFA] border-b-[0.5px] border-[#55555a26] font-bold tracking-[0.05em] uppercase text-[#1C1C1E] text-[0.7rem]">
                            <tr>
                                <th class="py-4 px-6">Platform</th>
                                <th class="py-4 px-6">Placement</th>
                                <th class="py-4 px-6">Master</th>
                                <th class="py-4 px-6">Ratio</th>
                                <th class="py-4 px-6">Safe Area</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y-[0.5px] divide-[#55555a26] text-[#55555A] font-mono">
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Meta</td>
                                <td class="py-4 px-6 font-sans">Feed</td>
                                <td class="py-4 px-6">1080 × 1350px</td>
                                <td class="py-4 px-6">4:5</td>
                                <td class="py-4 px-6 text-[#BE7555]">80px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Meta</td>
                                <td class="py-4 px-6 font-sans">Stories / Reels</td>
                                <td class="py-4 px-6">1080 × 1920px</td>
                                <td class="py-4 px-6">9:16</td>
                                <td class="py-4 px-6 text-[#BE7555]">96 / 250 / 96 / 350</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Google</td>
                                <td class="py-4 px-6 font-sans">Landscape</td>
                                <td class="py-4 px-6">1200 × 628px</td>
                                <td class="py-4 px-6">~1.91:1</td>
                                <td class="py-4 px-6 text-[#BE7555]">80px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">Google</td>
                                <td class="py-4 px-6 font-sans">Square</td>
                                <td class="py-4 px-6">1200 × 1200px</td>
                                <td class="py-4 px-6">1:1</td>
                                <td class="py-4 px-6 text-[#BE7555]">80px</td>
                            </tr>
                            <tr class="hover:bg-black/5 transition-colors">
                                <td class="py-4 px-6 font-sans font-bold text-[#1C1C1E]">YouTube</td>
                                <td class="py-4 px-6 font-sans">Landscape</td>
                                <td class="py-4 px-6">1920 × 1080px</td>
                                <td class="py-4 px-6">16:9</td>
                                <td class="py-4 px-6 text-[#BE7555]">~10%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Naming Convention -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">18.23 Creative Naming Convention</h3>
                <div class="bg-[#1C1C1E] p-8 rounded-sm font-mono text-[0.85rem]">
                    <div class="text-[#BE7555] mb-2 font-bold uppercase tracking-[0.1em] text-[0.7rem]">Syntax</div>
                    <div class="text-white mb-6">AK_[PLATFORM]_[FORMAT]_[CAMPAIGN]_[CONCEPT]_[VERSION]</div>
                    
                    <div class="text-[#BE7555] mb-2 font-bold uppercase tracking-[0.1em] text-[0.7rem]">Correct Examples</div>
                    <ul class="text-white/70 space-y-1 mb-6">
                        <li>AK_META_4x5_BENGALURU_CLARITY_V01</li>
                        <li>AK_GDN_1x1_BUYER-FIRST_V01</li>
                        <li>AK_YT_16x9_BUY-WITH-CLARITY_V03</li>
                    </ul>

                    <div class="text-[#8B3A3A] mb-2 font-bold uppercase tracking-[0.1em] text-[0.7rem]">Banned</div>
                    <ul class="text-white/40 space-y-1 strike">
                        <li>final-final-v3-new.jpg</li>
                        <li>latest-ad.png</li>
                    </ul>
                </div>
            </div>

            <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-12 rounded-sm mt-12 flex flex-col font-sans text-center items-center justify-center">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Final Two-Second Test</div>
                <div class="font-serif text-[24px] text-[#1C1C1E] font-normal max-w-3xl leading-[1.3] italic">Paid advertising should feel like acre&amp;key first, and an advertisement second.</div>
            </div>

        </div>
        """, 'html.parser')
        sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
