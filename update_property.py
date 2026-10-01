from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    prop_sec = soup.find(id='14-property')
    if prop_sec:
        prop_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">14. Property Design System</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The property page must never feel like a builder's brochure. It must feel like an objective <strong class="text-[#1C1C1E]">Asset Dossier</strong>—a buyer decision document that rigorously evaluates the opportunity, uncovers the risks, and presents verifiable data.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Overall Page Architecture -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-white">
                <div class="lg:col-span-5">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">The Dossier Architecture</h3>
                    <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">A property page follows a strict sequential logic, moving the buyer from macro-context (location, price) down into micro-diligence (floorplans, legal risks).</p>
                    
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm">
                        <div class="font-bold text-[0.75rem] tracking-[0.1em] uppercase text-[#8B3A3A] mb-2">Banned Marketing Fluff</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2">
                            <li><span class="text-[#8B3A3A]">✕</span> "Unparalleled Luxury Living"</li>
                            <li><span class="text-[#8B3A3A]">✕</span> "Book Now &amp; Save"</li>
                            <li><span class="text-[#8B3A3A]">✕</span> Hiding prices behind "Call for Price"</li>
                        </ul>
                    </div>
                </div>
                
                <div class="lg:col-span-7 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                    <h4 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-4 border-b-[0.5px] border-[#55555a26] pb-2">Mandatory Page Sequence</h4>
                    <div class="space-y-1">
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">01</span> <strong>Hero &amp; Executive Summary</strong> (Price, RERA, Typology)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">02</span> <strong>Financials &amp; Pricing</strong> (Base price vs Total landed cost)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">03</span> <strong>Location &amp; Infrastructure</strong> (Hard distances, not "minutes away")</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">04</span> <strong>Masterplan &amp; Typology</strong> (Objective architectural analysis)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">05</span> <strong>Floorplans &amp; Efficiency</strong> (Carpet area vs Super Built-up)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">06</span> <strong>Diligence &amp; Risks</strong> (Legal status, water supply, builder track record)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">07</span> <strong>Market Comparables</strong> (Data vs competitors)</div>
                        <div class="flex items-center gap-4 text-[0.85rem] text-[#55555A] py-1"><span class="w-6 font-mono text-[#1C1C1E]">08</span> <strong>Advisory CTA</strong> (Institutional intake form)</div>
                    </div>
                </div>
            </div>

            <!-- Deep Dive: Critical Components -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-8">Asset Dossier Component Specifications</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
                    <!-- Diligence & Risks -->
                    <div class="bg-[#8B3A3A]/5 border-[0.5px] border-[#8B3A3A]/20 p-8 rounded-sm">
                        <div class="font-bold text-[1.05rem] text-[#8B3A3A] mb-3 border-b-[0.5px] border-[#8B3A3A]/20 pb-2">Diligence &amp; Risk Matrix</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] leading-relaxed mb-4">Every property must feature a section evaluating risk. If a property has no listed risks, the dossier is biased and invalid.</p>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>Approval Status (RERA, BDA, BBMP)</li>
                            <li>Land Title clarity</li>
                            <li>Groundwater reliance vs Kaveri water</li>
                            <li>High-tension wires or railway proximity</li>
                        </ul>
                    </div>

                    <!-- Pricing & Financials -->
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <div class="font-bold text-[1.05rem] text-[#1C1C1E] mb-3 border-b-[0.5px] border-[#55555a26] pb-2">Financials &amp; Pricing</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] leading-relaxed mb-4">Builders quote "Base Price" to hide costs. acre&amp;key dossiers must expose the <strong class="text-[#804526]">Total Landed Cost</strong>.</p>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>Always show Carpet Area pricing natively.</li>
                            <li>Explicitly list Car Park, Club House, and PLC charges.</li>
                            <li>Break down Registration &amp; Stamp Duty.</li>
                        </ul>
                    </div>

                    <!-- Floorplans & Efficiency -->
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <div class="font-bold text-[1.05rem] text-[#1C1C1E] mb-3 border-b-[0.5px] border-[#55555a26] pb-2">Floorplans &amp; Masterplan</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] leading-relaxed mb-4">Do not just upload the builder's image. The system must overlay analytical data.</p>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>Calculate and display <strong class="text-[#1C1C1E]">Loading Percentage</strong>.</li>
                            <li>Highlight dead space (long corridors).</li>
                            <li>Analyze ventilation and light using compass orientations.</li>
                        </ul>
                    </div>

                    <!-- Market Comparables -->
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <div class="font-bold text-[1.05rem] text-[#1C1C1E] mb-3 border-b-[0.5px] border-[#55555a26] pb-2">Market Comparables</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] leading-relaxed mb-4">Properties do not exist in a vacuum. The dossier must include a strict data table comparing the asset to 2-3 alternatives.</p>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>Compare Price per Sq.Ft (Carpet).</li>
                            <li>Compare Density (Units per acre).</li>
                            <li>Compare Delivery Timelines.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- The Final Visual Output Mockup -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: The Asset Dossier Card</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">This is the canonical listing card used across the platform. It strips away marketing adjectives and focuses entirely on location, typology, financials, and RERA compliance.</p>
                
                <div class="flex justify-center bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-12 rounded-sm">
                    
                    <!-- LIVE PROPERTY CARD COMPONENT -->
                    <div class="w-full max-w-[400px] bg-white border-[0.5px] border-[#55555a26] rounded-sm shadow-xl flex flex-col group overflow-hidden">
                        <!-- Image Container -->
                        <div class="relative h-[240px] w-full overflow-hidden">
                            <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_pool_evening.webp')] bg-cover bg-center grayscale contrast-[1.1] group-hover:scale-105 transition-transform duration-[800ms] ease-out"></div>
                            
                            <!-- Badges -->
                            <div class="absolute top-4 left-4 flex gap-2 z-10">
                                <div class="bg-white/90 backdrop-blur-md px-2 py-1 rounded-sm text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] border-[0.5px] border-[#1C1C1E]/20">A-Grade Asset</div>
                                <div class="bg-white/90 backdrop-blur-md px-2 py-1 rounded-sm text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#2C4C3B] border-[0.5px] border-[#2C4C3B]/30 flex items-center gap-1">
                                    <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"></path></svg> RERA Approved
                                </div>
                            </div>

                            <!-- Image Gradient Anchors Name -->
                            <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/60 to-transparent h-[70%] mt-auto z-0"></div>
                            
                            <div class="absolute bottom-4 left-4 z-10">
                                <div class="font-serif text-[1.25rem] text-[#FAFAFA] mb-1">Prestige Evergreen</div>
                                <div class="font-sans text-[0.75rem] text-[#FAFAFA]/80 flex items-center gap-1.5">
                                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                    Whitefield, Bengaluru
                                </div>
                            </div>
                        </div>

                        <!-- Data Area -->
                        <div class="p-6">
                            <div class="grid grid-cols-2 gap-y-4 gap-x-8 mb-6">
                                <div>
                                    <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Typology</div>
                                    <div class="text-[0.9rem] font-semibold text-[#1C1C1E]">3 &amp; 4 BHK</div>
                                </div>
                                <div>
                                    <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Base Price</div>
                                    <div class="text-[0.9rem] font-semibold text-[#1C1C1E]">₹ 3.14 Cr <span class="text-[#55555A] font-normal text-[0.75rem]">onwards</span></div>
                                </div>
                                <div>
                                    <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Timeline</div>
                                    <div class="text-[0.9rem] font-semibold text-[#1C1C1E]">Dec 2028 <span class="text-[#804526] text-[0.75rem] bg-[#804526]/10 px-1 py-0.5 rounded-sm ml-1">U/C</span></div>
                                </div>
                                <div>
                                    <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-1">Density</div>
                                    <div class="text-[0.9rem] font-semibold text-[#1C1C1E]">54 Units/Acre</div>
                                </div>
                            </div>
                            
                            <button class="w-full border-[1px] border-[#1C1C1E] text-[#1C1C1E] hover:bg-black/5 py-3 rounded-sm font-sans text-[0.8rem] font-bold tracking-[0.1em] uppercase transition-colors">
                                View Asset Dossier
                            </button>
                        </div>
                    </div>
                    <!-- END LIVE COMPONENT -->

                </div>
            </div>
            
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If a property page reads like a sales brochure, we have failed our mandate. We are advisors, not brokers.</div>
            </div>

        </div>
        """, 'html.parser')
        prop_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
