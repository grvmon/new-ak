from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    grid_sec = soup.find(id='06-grid')
    if grid_sec:
        grid_sec.clear()
        
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">06. Grid &amp; Layout</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">The acre&key layout system is built around <strong>precision, proportion, whitespace, and alignment</strong>.</p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">Layouts should feel architectural rather than decorative. Every page should have a visible underlying grid, even when the grid itself is not visible.</p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The system is based on a <strong>4px spacing unit</strong> and responsive column structures.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Container & Grid Framework -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- Container -->
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm flex flex-col justify-between">
                    <div>
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Container Architecture</div>
                        <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-6">All primary content sits within a centered responsive container.</p>
                        
                        <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-2">Maximum Width</h3>
                        <div class="font-serif text-3xl text-[#1C1C1E] mb-2">1440px</div>
                        <div class="bg-[#FAFAFA] p-4 rounded-sm border-[0.5px] border-[#55555a26] mb-4 font-mono text-[0.8rem] text-[#55555A]">max-width: 1440px<br/>margin-inline: auto</div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-8">The container should not expand indefinitely on large displays.</p>
                    </div>
                    
                    <div>
                        <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Outer Margins</h3>
                        <table class="w-full border-collapse">
                            <thead>
                                <tr>
                                    <th class="text-left py-2 border-b-[0.5px] border-[#55555a26] text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A]">Viewport</th>
                                    <th class="text-right py-2 border-b-[0.5px] border-[#55555a26] text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A]">Horizontal Margin</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Desktop</td>
                                    <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">clamp(32px, 5vw, 80px)</td>
                                </tr>
                                <tr>
                                    <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Tablet</td>
                                    <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">32px</td>
                                </tr>
                                <tr>
                                    <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Mobile</td>
                                    <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">20px</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Grid -->
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Grid &amp; Gutters</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-6">The grid changes according to viewport size.</p>
                    
                    <table class="w-full border-collapse mb-8">
                        <thead>
                            <tr>
                                <th class="text-left py-2 border-b-[0.5px] border-[#55555a26] text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A]">Viewport</th>
                                <th class="text-right py-2 border-b-[0.5px] border-[#55555a26] text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A]">Columns</th>
                                <th class="text-right py-2 border-b-[0.5px] border-[#55555a26] text-[0.75rem] uppercase tracking-[0.1em] text-[#55555A]">Gutter</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Desktop</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] font-bold text-[#1C1C1E]">12</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">24px</td>
                            </tr>
                            <tr>
                                <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Tablet</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] font-bold text-[#1C1C1E]">8</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">20px</td>
                            </tr>
                            <tr>
                                <td class="text-left py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] text-[#1C1C1E] font-bold">Mobile</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.9rem] font-bold text-[#1C1C1E]">4</td>
                                <td class="text-right py-3 border-b-[0.5px] border-[#55555a26] text-[0.85rem] font-mono text-[#55555A]">16px</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="space-y-6">
                        <div>
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-1">Desktop (12 Columns)</div>
                            <p class="text-[0.85rem] text-[#55555A] mb-2">Primary layouts should use column spans rather than arbitrary widths.</p>
                            <p class="text-[0.85rem] text-[#55555A]">Examples: 6/6, 5/7, 7/5, 4/8, 3/9.</p>
                        </div>
                        <div>
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-1">Tablet (8 Columns)</div>
                            <p class="text-[0.85rem] text-[#55555A] mb-2">Desktop compositions should simplify rather than simply shrink.</p>
                            <p class="text-[0.85rem] text-[#55555A]">Examples: 4/4, 3/5, 5/3, 2/6.</p>
                        </div>
                        <div>
                            <div class="font-serif text-[1.1rem] text-[#1C1C1E] mb-1">Mobile (4 Columns)</div>
                            <p class="text-[0.85rem] text-[#55555A] mb-2">Complex compositions collapse into a single readable flow.</p>
                            <p class="text-[0.85rem] text-[#8B3A3A] font-bold">Avoid narrow text columns on mobile.</p>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Spacing System -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">4px Spacing System</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-6 font-bold">All spacing must derive from a 4px base unit.</p>
                        <div class="font-mono text-[0.85rem] text-[#1C1C1E] space-y-2 mb-6">
                            <div>04</div>
                            <div>08</div>
                            <div>16</div>
                            <div>24</div>
                            <div>32</div>
                            <div>48</div>
                            <div>64</div>
                            <div>96</div>
                            <div>128</div>
                        </div>
                        <p class="text-[0.85rem] text-[#55555A] mb-4">These values form the core spacing vocabulary.</p>
                        <div class="bg-[#8B3A3A]/5 border-[0.5px] border-[#8B3A3A]/20 p-4 rounded-sm">
                            <p class="text-[0.85rem] text-[#8B3A3A] font-bold mb-2">Do Not Introduce Arbitrary Values</p>
                            <p class="text-[0.8rem] font-mono text-[#8B3A3A]/80 line-through">13px, 18px, 27px, 37px, 53px</p>
                        </div>
                    </div>

                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Spacing Hierarchy</div>
                        <ul class="text-[0.9rem] space-y-3">
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">4px</span><span class="text-[#55555A]">Micro alignment</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">8px</span><span class="text-[#55555A]">Tight relationships</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">16px</span><span class="text-[#55555A]">Component spacing</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">24px</span><span class="text-[#55555A]">Component groups / cards</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">32px</span><span class="text-[#55555A]">Major internal separation</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">48px</span><span class="text-[#55555A]">Content group separation</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">64px</span><span class="text-[#55555A]">Major layout separation</span></li>
                            <li class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">96px</span><span class="text-[#55555A]">Section separation</span></li>
                            <li class="flex items-center gap-4 pb-2"><span class="font-mono font-bold w-12 text-[#1C1C1E]">128px</span><span class="text-[#55555A]">Major editorial / hero separation</span></li>
                        </ul>
                    </div>

                </div>
            </div>

            <!-- Alignment & Split Layouts -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Alignment -->
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Alignment</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-4">The default acre&key alignment is: Left-aligned.</p>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-6">Headings, body copy, metadata, navigation, cards, and data should generally align to a common grid edge.</p>
                    
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-2">Permitted Centering</h3>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-1 list-disc list-inside mb-4">
                        <li>Selected hero compositions</li>
                        <li>Short editorial statements</li>
                        <li>Certain calls to action</li>
                        <li>Deliberate visual interruptions</li>
                    </ul>
                    <p class="text-[0.85rem] text-[#8B3A3A] font-bold mb-6">Do not center content simply because the available space allows it.</p>
                    
                    <div class="bg-white border-[0.5px] border-[#1C1C1E] p-4 rounded-sm">
                        <div class="text-[0.85rem] font-bold text-[#1C1C1E] mb-1">Alignment Principle</div>
                        <p class="text-[0.85rem] text-[#55555A]">Related information should share an alignment edge. Misaligned text blocks, inconsistent card edges, and arbitrary offsets should be treated as layout errors.</p>
                    </div>
                </div>

                <!-- Full Bleed -->
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Full Bleed</div>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-4">Full-bleed content may extend beyond the primary container to the viewport edge. Full bleed should be intentional.</p>
                    <h3 class="font-serif text-[1.05rem] text-[#1C1C1E] mb-2">Approved Uses</h3>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-1 list-disc list-inside mb-6">
                        <li>Photography &amp; Video</li>
                        <li>Architectural imagery</li>
                        <li>Large background surfaces</li>
                        <li>Selected editorial compositions</li>
                    </ul>
                    <div class="bg-white border-[0.5px] border-[#1C1C1E] p-4 rounded-sm">
                        <div class="text-[0.85rem] font-bold text-[#1C1C1E] mb-2">Visuals break the container. Information stays on the grid.</div>
                        <p class="text-[0.85rem] text-[#55555A]">Text, controls, navigation, and interactive elements should return to the core grid unless specifically required otherwise.</p>
                    </div>
                </div>

            </div>

            <!-- Content Width & Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Content Width</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-4">Long-form text should not span the entire container.</p>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-4 border-[0.5px] border-[#55555a26] bg-white p-4 rounded-sm">Recommended text measure: 60–75 characters per line.</p>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Long-form editorial content should use a narrower grid span even when the overall page uses the full 1440px container.</p>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Card Grids</div>
                    <div class="grid grid-cols-3 gap-4">
                        <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm text-center">
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem] mb-1">Desktop</div>
                            <div class="text-[0.8rem] text-[#55555A]">3-column default</div>
                            <div class="text-[0.8rem] text-[#55555A] font-mono mt-2">24px gap</div>
                        </div>
                        <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm text-center">
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem] mb-1">Tablet</div>
                            <div class="text-[0.8rem] text-[#55555A]">2-column default</div>
                            <div class="text-[0.8rem] text-[#55555A] font-mono mt-2">20px gap</div>
                        </div>
                        <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm text-center">
                            <div class="font-bold text-[#1C1C1E] text-[0.95rem] mb-1">Mobile</div>
                            <div class="text-[0.8rem] text-[#55555A]">1-column default</div>
                            <div class="text-[0.8rem] text-[#55555A] font-mono mt-2">16px gap</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Rules: Do / Do Not -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#1C1C1E] mb-6">Layout Rules</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- DO -->
                    <div class="bg-white border-[0.5px] border-[#2C4C3B] p-6 rounded-sm border-t-4">
                        <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4 flex items-center gap-2">
                            <span class="text-[#2C4C3B]">✓</span> Do
                        </h3>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-2">
                            <li>&bull; Align content to the grid</li>
                            <li>&bull; Use consistent gutters</li>
                            <li>&bull; Use the 4px spacing system</li>
                            <li>&bull; Create hierarchy through proportion and whitespace</li>
                            <li>&bull; Use controlled asymmetry</li>
                            <li>&bull; Allow photography to break the container intentionally</li>
                            <li>&bull; Simplify layouts responsively</li>
                        </ul>
                    </div>
                    <!-- DO NOT -->
                    <div class="bg-white border-[0.5px] border-[#8B3A3A] p-6 rounded-sm border-t-4">
                        <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not
                        </h3>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-2">
                            <li>&bull; Use arbitrary margins or column widths</li>
                            <li>&bull; Create one-off spacing values</li>
                            <li>&bull; Center everything</li>
                            <li>&bull; Stretch content across the entire viewport</li>
                            <li>&bull; Force desktop layouts onto mobile</li>
                            <li>&bull; Use asymmetry without grid alignment</li>
                            <li>&bull; Add whitespace simply to make a page feel "luxury"</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Decision Rule -->
            <div class="bg-[#1C1C1E] text-white p-12 rounded-sm mt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Layout Decision Rule</div>
                <p class="text-[0.95rem] text-white/80 leading-relaxed mb-6">Before introducing a new layout pattern, ask:</p>
                <ol class="text-[0.95rem] text-white space-y-2 list-decimal list-inside mb-8">
                    <li>Does an existing grid structure solve the requirement?</li>
                    <li>Does the composition align to the core grid?</li>
                    <li>Does it use approved spacing tokens?</li>
                    <li>Does it remain coherent across desktop, tablet, and mobile?</li>
                    <li>Is the asymmetry intentional?</li>
                    <li>Does the whitespace improve hierarchy or merely create emptiness?</li>
                </ol>
                <div class="font-serif text-2xl text-white leading-relaxed">The grid should be invisible in the final experience but obvious in the discipline behind it.</div>
            </div>

        </div>
        """, 'html.parser')
        grid_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
