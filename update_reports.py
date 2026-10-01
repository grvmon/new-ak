from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    reports_sec = soup.find(id='21-reports')
    if reports_sec:
        reports_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">21. Reports &amp; Dossiers</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Our offline documents (PDFs, print) carry as much weight as our digital product. They are not marketing brochures. They are institutional-grade intelligence briefings. Every report must mirror the strict typographic and visual logic of the website.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Report Typology Matrix -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">The Intelligence Suite</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Buyer Analysis (Intake)</strong> Mapping family lifestyle, commute radii, and absolute non-negotiables.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Property Dossier</strong> The comprehensive teardown of a specific asset (Floorplans, loading %, specs).</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Diligence Report</strong> Legal, infrastructural, and RERA compliance risks (Groundwater, titles).</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Pricing &amp; Market Report</strong> Deep micro-market yield analysis, CAGR projections, and macro inventory tracking.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Comparison Matrix</strong> Side-by-side tabular teardowns of shortlisted assets against specific buyer criteria.</li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm flex flex-col justify-center">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Print Typography Rule</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-4">Screen typography does not perfectly translate to print. Ensure standard A4 rendering follows this architectural scale:</p>
                    <ul class="text-[0.85rem] text-[#1C1C1E] space-y-2 font-mono bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm">
                        <li>H1 (Cover): Marcellus 42pt</li>
                        <li>H2 (Section): Marcellus 24pt</li>
                        <li>Body Text: Manrope 10pt (1.5 line height)</li>
                        <li>Footnotes: Manrope 7.5pt</li>
                    </ul>
                </div>
            </div>

            <!-- Page Anatomy & Formatting -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Report Anatomy</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-3">Cover Architecture</div>
                        <p class="text-[0.8rem] text-[#55555A] leading-relaxed">No generic stock imagery. Covers rely on stark Obsidian typography, a strict grid, the acre&amp;key logo in the top-left, and a specific date/dossier ID at the bottom-right.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-3">Header &amp; Page Numbers</div>
                        <p class="text-[0.8rem] text-[#55555A] leading-relaxed">Every page features a 0.5px Obsidian hairline across the top. Page numbers format as "01 / 14" in Copper (Manrope 600) aligned right.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-3">Footnotes &amp; Sources</div>
                        <p class="text-[0.8rem] text-[#55555A] leading-relaxed">Data must be cited at the bottom of the exact page it appears. Footnotes use a 0.5px divider, 7.5pt Manrope, and absolute URL references where applicable.</p>
                    </div>
                </div>
            </div>

            <!-- Data & Risk Representation -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Data &amp; Risk Formatting</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                    <div>
                        <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm mb-6 shadow-sm">
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Tabular Data &amp; Charts</div>
                            <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                                <li><strong>No background colors</strong> in table cells. Use strict 0.5px hairlines.</li>
                                <li>Use <code class="bg-black/5 px-1 rounded-sm">tabular-nums</code> equivalents for print alignment.</li>
                                <li>Charts must remain strictly 2D. No drop shadows. Primary data line in Copper, market baselines in Titanium Frost.</li>
                            </ul>
                        </div>
                        <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Disclaimers &amp; Liability</div>
                            <p class="text-[0.8rem] text-[#55555A] leading-relaxed">Every dossier must append the standard legal disclaimer block on the interior cover page. Do not bury it. Transparency builds institutional trust.</p>
                        </div>
                    </div>
                    
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-6">Risk Indicator Scale</div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-6">Risk is not conveyed with red exclamation marks. We use a strict geometric indicator matrix.</p>
                        
                        <div class="space-y-4">
                            <!-- Low Risk -->
                            <div class="flex items-center justify-between border-b-[0.5px] border-[#55555a26] pb-3">
                                <div class="flex items-center gap-3">
                                    <div class="flex gap-0.5">
                                        <div class="w-3 h-3 bg-[#1C1C1E] rounded-sm"></div>
                                        <div class="w-3 h-3 border-[0.5px] border-[#1C1C1E] rounded-sm"></div>
                                        <div class="w-3 h-3 border-[0.5px] border-[#1C1C1E] rounded-sm"></div>
                                    </div>
                                    <span class="text-[0.85rem] font-bold text-[#1C1C1E]">Tier 1 (Cleared)</span>
                                </div>
                                <span class="text-[0.75rem] text-[#55555A]">Standard market risk</span>
                            </div>
                            
                            <!-- Medium Risk -->
                            <div class="flex items-center justify-between border-b-[0.5px] border-[#55555a26] pb-3">
                                <div class="flex items-center gap-3">
                                    <div class="flex gap-0.5">
                                        <div class="w-3 h-3 bg-[#BE7555] rounded-sm"></div>
                                        <div class="w-3 h-3 bg-[#BE7555] rounded-sm"></div>
                                        <div class="w-3 h-3 border-[0.5px] border-[#1C1C1E] rounded-sm"></div>
                                    </div>
                                    <span class="text-[0.85rem] font-bold text-[#1C1C1E]">Tier 2 (Advisory)</span>
                                </div>
                                <span class="text-[0.75rem] text-[#55555A]">Action required pre-purchase</span>
                            </div>

                            <!-- High Risk -->
                            <div class="flex items-center justify-between pb-1">
                                <div class="flex items-center gap-3">
                                    <div class="flex gap-0.5">
                                        <div class="w-3 h-3 bg-[#8B3A3A] rounded-sm"></div>
                                        <div class="w-3 h-3 bg-[#8B3A3A] rounded-sm"></div>
                                        <div class="w-3 h-3 bg-[#8B3A3A] rounded-sm"></div>
                                    </div>
                                    <span class="text-[0.85rem] font-bold text-[#1C1C1E]">Tier 3 (Flagged)</span>
                                </div>
                                <span class="text-[0.75rem] text-[#55555A]">Critical non-compliance</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">A printed acre&amp;key dossier sitting on a client’s desk should carry the same gravitas and visual authority as a prospectus from Goldman Sachs.</div>
            </div>

        </div>
        """, 'html.parser')
        reports_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
