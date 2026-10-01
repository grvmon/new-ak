from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    trust_sec = soup.find(id='24-trust')
    if trust_sec:
        trust_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">24. Trust &amp; Compliance</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">acre&amp;key operates on absolute institutional transparency. We do not make generic marketing claims. Every number, projection, and render must be rigorously sourced, explicitly dated, and legally compliant. Trust is mathematical, not emotional.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Compliance Vectors -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Regulatory Integrity</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">RERA Mandate</strong> The exact RERA registration number must sit immediately beneath the primary property title on every asset dossier. Never hide it in the footer.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">DPDP Act Privacy</strong> Under India's Digital Personal Data Protection Act, consent must be granular. "I agree to the Terms" is illegal. We must explicitly list the exact purpose of data collection (e.g., WhatsApp Dossier Updates) with a clear opt-out.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Builder Renders vs Reality</strong> Any image provided by a developer that is not an actual photograph must bear a permanent, visible watermark or overlay stating: <code class="bg-black/5 px-1 rounded-sm">ARTISTIC IMPRESSION</code>.</li>
                    </ul>
                </div>
                
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Data Traceability Rules</h3>
                    <div class="space-y-4">
                        <div class="flex items-start gap-3">
                            <span class="text-[#8B3A3A] font-bold mt-0.5">✕</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Numerical Claims</div>
                                <p class="text-[0.85rem] text-[#55555A]">Banned: "Highest returns in Whitefield!"</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <span class="text-[#2C4C3B] font-bold mt-0.5">✓</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Verifiable Projections</div>
                                <p class="text-[0.85rem] text-[#55555A]">Required: "7.2% average rental yield over 5 years. (Source: acre&amp;key Analytics, Q3 2025)"</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 mt-4 pt-4 border-t-[0.5px] border-[#55555a26]">
                            <span class="text-[#8B3A3A] font-bold mt-0.5">✕</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Testimonials</div>
                                <p class="text-[0.85rem] text-[#55555A]">Banned: "Best real estate agency ever! - Anonymous"</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <span class="text-[#2C4C3B] font-bold mt-0.5">✓</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Verified Case Studies</div>
                                <p class="text-[0.85rem] text-[#55555A]">Required: Documented timelines of execution (e.g., "Negotiated 4% below base price for a 3BHK in Prestige Evergreen, Aug 2025").</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Investment Disclaimers Component -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: The Investment Disclaimer</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Disclaimers must never be hidden in 6pt font at the bottom of the screen. We proudly surface them within the data flow, using a strictly architected Copper bounding box.</p>
                
                <div class="flex justify-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                    
                    <div class="w-full max-w-2xl bg-white border-l-[4px] border-[#BE7555] p-6 rounded-r-sm shadow-sm">
                        <div class="flex items-center gap-2 mb-3">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#BE7555" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                            <span class="text-[0.75rem] font-bold uppercase tracking-[0.1em] text-[#1C1C1E]">Forward-Looking Data Disclaimer</span>
                        </div>
                        <p class="text-[0.8rem] text-[#55555A] leading-relaxed">
                            Projected capital appreciation and rental yields are analytical estimates based on historical micro-market velocity (Q2 2023 - Q4 2025). Real estate investments are subject to macroeconomic volatility. These figures do not constitute a guaranteed financial return. 
                        </p>
                    </div>

                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If a claim cannot be sourced, dated, and legally defended, it does not belong on acre&amp;key.</div>
            </div>

        </div>
        """, 'html.parser')
        trust_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
