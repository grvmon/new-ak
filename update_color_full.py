from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    color_sec = soup.find(id='04-color')
    if color_sec:
        color_sec.clear()
        
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">04. Color</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">Color is a structural part of the acre&amp;key identity.</p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">The system is intentionally restrained: <strong>cool architectural neutrals, controlled copper accents, and muted semantic states.</strong></p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Color should create hierarchy and meaning &mdash; never decoration for its own sake.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Architecture & Core Palette Table -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Core Color Architecture</div>
                <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-2">The acre&key system uses a restrained core palette with a controlled semantic state palette.</p>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-6">The core palette establishes the brand. The semantic palette communicates system status. No additional colors should be introduced without Design Authority approval.</p>
                
                <table class="w-full border-collapse bg-white mb-6">
                    <thead>
                        <tr>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A] w-1/4">Role</th>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A] w-1/4">Token</th>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A] w-1/6">Value</th>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Primary Use</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#FAFAFA] border-[0.5px] border-[#55555a26] mr-2 align-middle"></span>Canvas Light</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--titanium-frost</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#FAFAFA</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Primary light canvas</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#1C1C1E] mr-2 align-middle"></span>Canvas Dark</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--obsidian-black</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#1C1C1E</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Dark canvas / anchor</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#BE7555] mr-2 align-middle"></span>Copper</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--copper</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#BE7555</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Primary accent / CTA</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#9F5334] mr-2 align-middle"></span>Copper Dark</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--copper-dark</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#9F5334</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Hover / pressed / stronger accent</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#804526] mr-2 align-middle"></span>Copper Text</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--copper-text</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#804526</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Accessible copper text</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#55555A] mr-2 align-middle"></span>Neutral Text</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--neutral-grey</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">#55555A</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Secondary text</td>
                        </tr>
                        <tr>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold"><span class="inline-block w-3 h-3 rounded-sm bg-[#55555A]/15 mr-2 align-middle"></span>Subtle Border</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">--border-subtle</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem] font-mono text-[#55555A]">rgba(85,85,90,0.15)</td>
                            <td class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem] text-[#55555A]">Dividers / borders</td>
                        </tr>
                    </tbody>
                </table>
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold mb-2">Core Principle: Obsidian + Titanium Frost establish the architecture. Copper provides controlled emphasis.</p>
                    <p class="text-[0.95rem] text-[#55555A]">Copper should never dominate the interface.</p>
                </div>
            </div>

            <!-- Primary Colors Swatch Grid -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Primary Colors</div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    
                    <!-- Obsidian Black -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-[#1C1C1E]"></div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Obsidian Black</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#1C1C1E</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">The primary dark anchor of the system.</p>
                            <ul class="text-[0.85rem] text-[#1C1C1E] space-y-1">
                                <li>&bull; Dark backgrounds</li>
                                <li>&bull; Primary dark sections</li>
                                <li>&bull; Navigation &amp; Footer</li>
                                <li>&bull; High-contrast surfaces</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Titanium Frost -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-[#FAFAFA] border-b-[0.5px] border-[#55555a26]"></div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Titanium Frost</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#FAFAFA</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">The primary light canvas.</p>
                            <ul class="text-[0.85rem] text-[#1C1C1E] space-y-1">
                                <li>&bull; Main page backgrounds</li>
                                <li>&bull; Content surfaces</li>
                                <li>&bull; Editorial layouts</li>
                                <li>&bull; Light-mode interfaces</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Copper -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-[#BE7555]"></div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Copper</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#BE7555</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">The primary brand accent.</p>
                            <ul class="text-[0.85rem] text-[#1C1C1E] space-y-1">
                                <li>&bull; Primary CTAs</li>
                                <li>&bull; Interactive elements</li>
                                <li>&bull; Key highlights</li>
                            </ul>
                            <p class="text-[0.85rem] text-[#804526] font-bold mt-4">Copper is an accent, not a background color for large areas.</p>
                        </div>
                    </div>

                    <!-- Copper Dark -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-[#9F5334]"></div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Copper Dark</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#9F5334</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">The deeper copper treatment.</p>
                            <ul class="text-[0.85rem] text-[#1C1C1E] space-y-1">
                                <li>&bull; Hover &amp; Pressed states</li>
                                <li>&bull; Stronger emphasis</li>
                                <li>&bull; Situations requiring greater contrast</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Copper Text -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-white flex items-center justify-center border-b-[0.5px] border-[#55555a26]">
                            <span class="font-serif text-3xl text-[#804526]">Copper Text</span>
                        </div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Copper Text</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#804526</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">The accessible copper text treatment. Use when copper is required as text on Titanium Frost.</p>
                            <p class="text-[0.85rem] text-[#8B3A3A] font-bold mt-4">Do not use standard Copper #BE7555 for small text where contrast is insufficient.</p>
                        </div>
                    </div>

                    <!-- Neutral Grey -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden flex flex-col">
                        <div class="h-32 bg-white flex items-center justify-center border-b-[0.5px] border-[#55555a26]">
                            <span class="font-serif text-3xl text-[#55555A]">Neutral Grey</span>
                        </div>
                        <div class="p-6 bg-white flex-1">
                            <div class="flex justify-between items-end mb-4">
                                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E]">Neutral Grey</h3>
                                <div class="font-mono text-[0.85rem] text-[#55555A]">#55555A</div>
                            </div>
                            <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Secondary text and supporting information.</p>
                            <ul class="text-[0.85rem] text-[#1C1C1E] space-y-1 mb-4">
                                <li>&bull; Metadata</li>
                                <li>&bull; Supporting copy</li>
                                <li>&bull; Secondary labels</li>
                            </ul>
                            <p class="text-[0.85rem] text-[#8B3A3A] font-bold">Do not use it for critical text.</p>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Contrast Rules -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Contrast Accessibility</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-4">Accessibility is a system requirement, not an optional refinement.</p>
                        <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Contrast must be validated according to <strong>WCAG 2.2</strong> requirements for the relevant text size and UI element.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Target: AAA</h4>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-4">Where practical, critical text should target AAA contrast. Do not label a color “AAA” globally. AAA is a relationship between foreground and background, not an inherent property of a color.</p>
                        <div class="border-l-[2px] border-[#804526] pl-4 text-[0.9rem] text-[#1C1C1E] font-serif italic mb-4">
                            "--copper-text may meet AAA against Titanium Frost, but that does not mean it meets AAA against every canvas or surface."
                        </div>
                        <p class="text-[0.9rem] text-[#1C1C1E] font-bold">Every important foreground/background pairing must be tested as a pair.</p>
                    </div>
                </div>
            </div>

            <!-- Semantic Colors -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Semantic Colors</div>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Semantic colors communicate system states while remaining visually compatible with the acre&key brand. Avoid default browser, framework, or generic dashboard colors.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    <!-- Success -->
                    <div class="bg-white border-[0.5px] border-[#2C4C3B] p-6 rounded-sm border-t-4">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="font-serif text-[1.15rem] text-[#1C1C1E]">Success</h3>
                            <div class="font-mono text-[0.8rem] text-[#55555A]">#2C4C3B</div>
                        </div>
                        <div class="font-mono text-[0.75rem] text-[#2C4C3B] mb-4">--pine-success</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-1">
                            <li>&bull; Verified</li>
                            <li>&bull; Approved</li>
                            <li>&bull; Completed</li>
                            <li>&bull; Positive validation</li>
                        </ul>
                    </div>
                    
                    <!-- Error / Risk -->
                    <div class="bg-white border-[0.5px] border-[#8B3A3A] p-6 rounded-sm border-t-4">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="font-serif text-[1.15rem] text-[#1C1C1E]">Error / Risk</h3>
                            <div class="font-mono text-[0.8rem] text-[#55555A]">#8B3A3A</div>
                        </div>
                        <div class="font-mono text-[0.75rem] text-[#8B3A3A] mb-4">--terracotta-error</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-1">
                            <li>&bull; Risk</li>
                            <li>&bull; Rejected</li>
                            <li>&bull; Failed</li>
                            <li>&bull; Critical issue</li>
                        </ul>
                    </div>
                    
                    <!-- Warning -->
                    <div class="bg-white border-[0.5px] border-[#A88944] p-6 rounded-sm border-t-4">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="font-serif text-[1.15rem] text-[#1C1C1E]">Warning</h3>
                            <div class="font-mono text-[0.8rem] text-[#55555A]">#A88944</div>
                        </div>
                        <div class="font-mono text-[0.75rem] text-[#A88944] mb-4">--brass-warning</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-1">
                            <li>&bull; Caution</li>
                            <li>&bull; Pending</li>
                            <li>&bull; Review required</li>
                            <li>&bull; Incomplete information</li>
                        </ul>
                    </div>
                </div>

                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm flex items-center justify-between gap-6">
                    <div>
                        <div class="text-[0.85rem] text-[#1C1C1E] font-bold mb-1">Semantic Rule: Semantic color must never be the only indicator of meaning.</div>
                        <div class="text-[0.85rem] text-[#55555A]">Always pair state color with text, iconography, status label, or another non-color indicator.</div>
                    </div>
                    <div class="shrink-0 flex items-center gap-2 bg-[#2C4C3B]/10 px-3 py-1.5 rounded-sm text-[#2C4C3B] font-bold text-[0.85rem] uppercase tracking-wide">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                        Verified
                    </div>
                </div>
            </div>

            <!-- Decorative & Hierarchy -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Highlight Peach -->
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Decorative Color</div>
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-12 h-12 bg-[#E5B899] rounded-sm border-[0.5px] border-[#55555a26]"></div>
                        <div>
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E]">Highlight Peach</div>
                            <div class="font-mono text-[0.8rem] text-[#55555A]">#E5B899</div>
                        </div>
                    </div>
                    <p class="text-[0.95rem] text-[#8B3A3A] font-bold mb-4">This is not a core UI color.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">If retained, it should be classified as a decorative highlight only. Permitted for editorial visual accents, photography treatment, subtle graphic details.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed"><strong>Do not use it for:</strong> Body text, Critical UI, Primary CTA, Semantic states, or Large interface surfaces.</p>
                </div>
                
                <!-- Color Hierarchy -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Color Hierarchy</div>
                    <ol class="space-y-4">
                        <li>
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem]">1. Titanium Frost / Obsidian</div>
                            <div class="text-[0.85rem] text-[#55555A]">Foundation</div>
                        </li>
                        <li>
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem]">2. Neutral Grey</div>
                            <div class="text-[0.85rem] text-[#55555A]">Information</div>
                        </li>
                        <li>
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem]">3. Copper</div>
                            <div class="text-[0.85rem] text-[#55555A]">Action</div>
                        </li>
                        <li>
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem]">4. Semantic Colors</div>
                            <div class="text-[0.85rem] text-[#55555A]">System state</div>
                        </li>
                        <li>
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem]">5. Decorative Highlight</div>
                            <div class="text-[0.85rem] text-[#55555A]">Rare accent</div>
                        </li>
                    </ol>
                    <div class="mt-6 pt-4 border-t-[0.5px] border-[#55555a26] text-[0.85rem] text-[#804526] font-bold">The brand should remain recognizable even if all accent colors are removed.</div>
                </div>
            </div>

            <!-- Prohibited -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#8B3A3A] mb-6">Prohibited Color Treatments</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <p class="text-[0.95rem] text-[#1C1C1E] mb-4">Never introduce:</p>
                        <ul class="text-[0.9rem] text-[#55555A] grid grid-cols-2 gap-y-2 mb-6">
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Luxury gold</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Metallic gold</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Champagne gradients</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Neon colors</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Default Tailwind colors</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Highly saturated colors</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Random one-off HEX</li>
                            <li class="flex items-center gap-2"><span class="text-[#8B3A3A]">✕</span> Unapproved gradients</li>
                        </ul>
                    </div>
                    <div>
                        <p class="text-[1.05rem] text-[#1C1C1E] font-serif mb-4">Do not use color simply to make an interface feel “premium.”</p>
                        <p class="text-[0.95rem] text-[#804526] font-bold leading-relaxed">Premium comes from restraint, hierarchy, typography, spacing, imagery, and precision.</p>
                    </div>
                </div>
            </div>

            <!-- Decision Rule -->
            <div class="bg-[#1C1C1E] text-white p-12 rounded-sm mt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Color Decision Rule</div>
                <p class="text-[0.95rem] text-white/80 leading-relaxed mb-6">Before introducing a color, ask:</p>
                <ol class="text-[0.95rem] text-white space-y-2 list-decimal list-inside mb-8">
                    <li>Does it have a defined semantic role?</li>
                    <li>Does it already exist as a token?</li>
                    <li>Does it meet the required contrast against its intended surface?</li>
                    <li>Does it reinforce the acre&key visual language?</li>
                    <li>Is it necessary?</li>
                </ol>
                <div class="font-serif text-2xl text-[#8B3A3A] leading-relaxed">If the answer to the final question is no, do not add the color.</div>
            </div>

        </div>
        """, 'html.parser')
        color_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
