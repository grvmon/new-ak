from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    data_sec = soup.find(id='15-data')
    if data_sec:
        data_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">15. Data Visualization</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">acre&key is an intelligence firm. Data must feel like institutional research, not a gamified SaaS dashboard. It must look credible, calm, and analytical. We present facts; we do not try to make them entertaining.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Number Formatting & Citations -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Number Formatting</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Tabular Numerals</strong>
                            When displaying tables, charts, or financial grids, use <code class="bg-black/5 px-1 rounded-sm text-[#804526]">tabular-nums</code> so that decimal points and digits align perfectly vertically.
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Currency (INR)</strong>
                            Always use the ₹ symbol. Use Crores (Cr) and Lakhs (L) for large figures. <br/>
                            <span class="text-[#2C4C3B] font-bold">✓ ₹ 3.14 Cr</span> <span class="text-[#8B3A3A] font-bold ml-4">✕ Rs 3.14 Crores</span>
                        </li>
                        <li>
                            <strong class="text-[#1C1C1E] block mb-1">Percentages &amp; Yield</strong>
                            Always show one decimal place for accuracy (e.g., <code class="bg-black/5 px-1 rounded-sm">7.4%</code>, not just <code class="bg-black/5 px-1 rounded-sm">7%</code>).
                        </li>
                    </ul>
                </div>

                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm space-y-6">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Sources &amp; Dates</h3>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-4">Data without a source is an opinion. Every chart, price, and comparable table must include a time-stamp and a citation.</p>
                    
                    <!-- Live Source Component -->
                    <div class="border-[0.5px] border-[#1C1C1E]/20 bg-[#FAFAFA] p-4 rounded-sm flex items-center justify-between">
                        <div class="text-[0.7rem] uppercase tracking-[0.1em] text-[#55555A] font-bold">
                            Data Source: <span class="text-[#1C1C1E]">Karnataka RERA Database</span>
                        </div>
                        <div class="text-[0.7rem] uppercase tracking-[0.1em] text-[#55555A] font-mono">
                            UPDATED: OCT 2026
                        </div>
                    </div>
                </div>
            </div>

            <!-- Institutional KPI Cards -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Institutional KPI Architecture</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">KPI cards do not use heavy shadows, bubbly 3D icons, or glowing green/red text. They rely on severe 0.5px borders, strict alignment, and restrained Copper emphasis.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- KPI 1 -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm flex flex-col justify-between h-[140px]">
                        <div class="text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#55555A]">Projected CAGR (5Y)</div>
                        <div>
                            <div class="font-sans text-[2rem] text-[#1C1C1E] font-medium tracking-tight" style="font-variant-numeric: tabular-nums;">12.4<span class="text-[1.25rem] text-[#55555A]">%</span></div>
                            <div class="text-[0.75rem] text-[#2C4C3B] font-bold mt-1 flex items-center gap-1"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline></svg> +2.1% vs micro-market</div>
                        </div>
                    </div>
                    
                    <!-- KPI 2 -->
                    <div class="bg-[#1C1C1E] border-[0.5px] border-[#55555a26] p-6 rounded-sm flex flex-col justify-between h-[140px]">
                        <div class="text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#FAFAFA]/60">Current Pricing (Carpet)</div>
                        <div>
                            <div class="font-sans text-[2rem] text-[#FAFAFA] font-medium tracking-tight" style="font-variant-numeric: tabular-nums;"><span class="text-[1.25rem] text-[#FAFAFA]/60 mr-1">₹</span>14,250<span class="text-[1rem] text-[#FAFAFA]/60 ml-1">/sq.ft</span></div>
                            <div class="text-[0.75rem] text-[#FAFAFA]/60 mt-1">Inclusive of PLC &amp; Floor Rise</div>
                        </div>
                    </div>

                    <!-- KPI 3 -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm flex flex-col justify-between h-[140px]">
                        <div class="text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#55555A]">Rental Yield</div>
                        <div>
                            <div class="font-sans text-[2rem] text-[#BE7555] font-medium tracking-tight" style="font-variant-numeric: tabular-nums;">4.2<span class="text-[1.25rem] text-[#BE7555]">%</span></div>
                            <div class="text-[0.75rem] text-[#55555A] mt-1">Based on Phase 1 lease data</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Analytical Tables -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Analytical Tables</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Tables do not use zebra-striping. They rely on generous padding, clear left/right alignment rules, and strict 0.5px borders. <strong class="text-[#1C1C1E]">Text aligns left. Numbers align right.</strong></p>
                
                <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden overflow-x-auto">
                    <table class="w-full text-left font-sans min-w-[600px]">
                        <thead class="bg-[#FAFAFA] border-b-[0.5px] border-[#55555a26]">
                            <tr>
                                <th class="py-4 px-6 text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#55555A]">Asset / Competitor</th>
                                <th class="py-4 px-6 text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#55555A] text-right">Launch Date</th>
                                <th class="py-4 px-6 text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#55555A] text-right">Carpet Price / Sq.Ft</th>
                                <th class="py-4 px-6 text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#55555A] text-right">Density (Units/Acre)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y-[0.5px] divide-[#55555a26]" style="font-variant-numeric: tabular-nums;">
                            <tr class="bg-[#BE7555]/5">
                                <td class="py-4 px-6 text-[0.9rem] font-bold text-[#1C1C1E] flex items-center gap-2">
                                    <span class="w-1.5 h-1.5 bg-[#BE7555] rounded-sm shrink-0"></span> Prestige Evergreen
                                </td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">Sep 2024</td>
                                <td class="py-4 px-6 text-[0.9rem] font-bold text-[#1C1C1E] text-right">₹ 14,250</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">54.2</td>
                            </tr>
                            <tr>
                                <td class="py-4 px-6 text-[0.9rem] font-medium text-[#1C1C1E]">Sobha Oneworld</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">Jan 2024</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#1C1C1E] text-right">₹ 13,800</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">62.0</td>
                            </tr>
                            <tr>
                                <td class="py-4 px-6 text-[0.9rem] font-medium text-[#1C1C1E]">Sattva Songbird</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">Aug 2024</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#1C1C1E] text-right">₹ 12,900</td>
                                <td class="py-4 px-6 text-[0.9rem] text-[#55555A] text-right">48.5</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Data should end an argument, not start one. If a chart requires a legend to be understood, it is too complex. Keep it calm, clear, and perfectly cited.</div>
            </div>

        </div>
        """, 'html.parser')
        data_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
