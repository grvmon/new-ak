from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    resp_sec = soup.find(id='07-responsive')
    if resp_sec:
        resp_sec.clear()
        
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">07. Responsive System</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The HNI user expects a seamless, uncompromised experience across devices. The system must adapt its architecture intelligently—not simply shrink to fit. <strong>Mobile is not a compromise; it is a dedicated context.</strong></p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Breakpoints -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Core Breakpoints</div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-1">Mobile Base</div>
                        <div class="font-mono text-[0.8rem] text-[#55555A] mb-4">Default (&lt; 768px)</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Single column flow. Full-width CTAs. Prioritize thumb reachability and extreme legibility.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-1">Tablet (md)</div>
                        <div class="font-mono text-[0.8rem] text-[#55555A] mb-4">768px+</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Transitional grids (2-column cards). Navigation may remain in drawer or switch to horizontal.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-1">Desktop (lg)</div>
                        <div class="font-mono text-[0.8rem] text-[#55555A] mb-4">1024px+</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Standard multi-column layouts. Sidebar active. Hover states engaged.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-1">Wide (xl/2xl)</div>
                        <div class="font-mono text-[0.8rem] text-[#55555A] mb-4">1280px+ / 1440px+</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Container max-width locks at 1440px. Gutters scale up. Do not stretch infinitely.</p>
                    </div>
                </div>
            </div>

            <!-- Behavioral Rules Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Layout & Stacking -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Stacking &amp; Visibility</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Single-Column Collapse</strong>
                            On mobile, all 2, 3, or 4-column grids must cleanly stack into a single column. Never force a 2-column layout on mobile if it squashes text.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Information Parity</strong>
                            Never "hide" critical data (pricing, risk factors, specs) on mobile just to save space. Hide decorative elements only. The mobile user requires the exact same data to make a decision.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Order Reversal</strong>
                            When collapsing split layouts (Image + Text), the Image should generally stack <em>above</em> the text on mobile to preserve visual hierarchy.
                        </li>
                    </ul>
                </div>

                <!-- Interaction & Touch -->
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Touch &amp; Interaction</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">44x44px Minimum</strong>
                            All interactive elements (buttons, links, toggles) must have a minimum physical tap target of 44x44px. Do not cluster links tightly on mobile.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Full-Width CTAs</strong>
                            Primary CTA buttons should become <code class="bg-black/5 px-1 rounded-sm text-[#804526]">w-full</code> on mobile, anchoring to the bottom of the card or viewport for easy thumb access.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">No Hover Reliance</strong>
                            Hover states do not exist on touch devices. Any information revealed on hover (tooltips, secondary actions) must be persistently visible or accessible via a deliberate tap on mobile.
                        </li>
                    </ul>
                </div>

                <!-- Typography & Media -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Typography &amp; Media</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Fluid Typography</strong>
                            Headings must scale fluidly using CSS <code class="bg-black/5 px-1 rounded-sm text-[#804526]">clamp()</code>. Never use hard media queries for font sizes that cause the text to violently jump between breakpoints.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Base Legibility</strong>
                            Body text must never drop below <code class="bg-black/5 px-1 rounded-sm">16px</code> on mobile to prevent iOS Safari auto-zooming on inputs and ensure comfortable reading.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Image Cropping</strong>
                            Use <code class="bg-black/5 px-1 rounded-sm">object-cover</code>. Images must intelligently crop from the center or focal point rather than compressing or shrinking unreadably. Provide mobile-specific crops if the architectural subject is lost.
                        </li>
                    </ul>
                </div>

                <!-- Navigation -->
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Navigation Behavior</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">The Mobile Drawer</strong>
                            Desktop horizontal navigation must collapse into a clean, full-screen takeover or structured drawer on mobile.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Sticky Headers</strong>
                            If the header is sticky, it must reduce its vertical height on mobile scroll to maximize reading canvas for the user.
                        </li>
                    </ul>
                </div>

            </div>

        </div>
        """, 'html.parser')
        resp_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
