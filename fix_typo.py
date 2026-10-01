from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    typo_sec = soup.find(id='05-typography')
    if typo_sec:
        # We want to replace the first large div containing the H1, H2, Kicker, Body, Data
        # that comes before the "Text on Surfaces" block.
        # Let's find the first direct child div inside typo_sec that has the text "Display Title"
        for div in typo_sec.find_all('div', recursive=False):
            if "Display Title (H1)" in div.text:
                div.clear()
                
                new_typo = BeautifulSoup("""
                <div class="space-y-12">
                    <!-- H1 Display -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 border-b-[0.5px] border-[#55555a26] pb-12">
                        <div class="lg:col-span-4 flex flex-col gap-2">
                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Display Title (H1)</div>
                            <div class="font-mono text-[0.75rem] text-[#804526] bg-[#804526]/5 w-fit px-2 py-1 rounded-sm">Marcellus • 400 • LH: 1.1 • LS: -0.02em</div>
                        </div>
                        <div class="lg:col-span-8 flex flex-col gap-4">
                            <div class="font-serif text-[clamp(2.5rem,4vw,3.5rem)] leading-[1.1] tracking-[-0.02em] text-[#1C1C1E]">
                                The Architecture of Wealth
                            </div>
                            <p class="font-sans text-[0.85rem] text-[#55555A] leading-relaxed max-w-2xl">
                                <strong class="text-[#1C1C1E]">Usage:</strong> Strictly reserved for Hero sections. Must use <code class="bg-black/5 px-1 rounded-sm">clamp()</code> for fluid responsive scaling without breakpoints.
                            </p>
                        </div>
                    </div>

                    <!-- H2 Section -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 border-b-[0.5px] border-[#55555a26] pb-12">
                        <div class="lg:col-span-4 flex flex-col gap-2">
                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Section Heading (H2/H3)</div>
                            <div class="font-mono text-[0.75rem] text-[#804526] bg-[#804526]/5 w-fit px-2 py-1 rounded-sm">Marcellus • 400 • LH: 1.2 • LS: 0</div>
                        </div>
                        <div class="lg:col-span-8 flex flex-col gap-4">
                            <div class="font-serif text-[2rem] leading-[1.2] text-[#1C1C1E]">
                                Institutional Grade diligence.
                            </div>
                            <p class="font-sans text-[0.85rem] text-[#55555A] leading-relaxed max-w-2xl">
                                <strong class="text-[#1C1C1E]">Usage:</strong> Section dividers, grid headers, and primary content breaks. Never uppercase.
                            </p>
                        </div>
                    </div>

                    <!-- Kicker / Overline -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 border-b-[0.5px] border-[#55555a26] pb-12">
                        <div class="lg:col-span-4 flex flex-col gap-2">
                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Overline Kicker</div>
                            <div class="font-mono text-[0.75rem] text-[#804526] bg-[#804526]/5 w-fit px-2 py-1 rounded-sm">Manrope • 700 • Uppercase • LH: 1.2 • LS: 0.15em</div>
                        </div>
                        <div class="lg:col-span-8 flex flex-col gap-4">
                            <div class="font-sans text-[0.75rem] font-bold uppercase tracking-[0.15em] leading-[1.2] text-[#BE7555]">
                                Micro-Market Analysis
                            </div>
                            <p class="font-sans text-[0.85rem] text-[#55555A] leading-relaxed max-w-2xl">
                                <strong class="text-[#1C1C1E]">Usage:</strong> Eyebrows above headings, category tags, and data pillar labels. Provides structural metadata.
                            </p>
                        </div>
                    </div>

                    <!-- Body / Lead -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 border-b-[0.5px] border-[#55555a26] pb-12">
                        <div class="lg:col-span-4 flex flex-col gap-2">
                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Body &amp; Lead Text</div>
                            <div class="font-mono text-[0.75rem] text-[#804526] bg-[#804526]/5 w-fit px-2 py-1 rounded-sm">Manrope • 400/500 • LH: 1.6 • LS: 0</div>
                        </div>
                        <div class="lg:col-span-8 flex flex-col gap-4">
                            <p class="font-sans text-[1.1rem] leading-[1.6] text-[#55555A] max-w-3xl">
                                We filter out [X]% of the noise in the market to bring you absolute clarity. Our independent advisory evaluates the opportunity, uncovers the risks, and negotiates entirely on your behalf.
                            </p>
                            <p class="font-sans text-[0.85rem] text-[#55555A] leading-relaxed max-w-2xl">
                                <strong class="text-[#1C1C1E]">Usage:</strong> All paragraph text. Use 1.1rem for lead paragraphs (like above), 0.95rem for standard card reading.
                            </p>
                        </div>
                    </div>

                    <!-- Data & Microcopy -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 pb-12">
                        <div class="lg:col-span-4 flex flex-col gap-2">
                            <div class="font-sans text-[0.7rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Data &amp; Microcopy</div>
                            <div class="font-mono text-[0.75rem] text-[#804526] bg-[#804526]/5 w-fit px-2 py-1 rounded-sm">Manrope • 600/700 • LH: 1.4 • LS: 0</div>
                        </div>
                        <div class="lg:col-span-8 flex flex-col gap-4">
                            <div class="font-sans text-[0.85rem] font-bold leading-[1.4] text-[#1C1C1E]">Deliverable: Buyer Mandate Brief</div>
                            <div class="font-sans text-[0.75rem] font-semibold leading-[1.4] text-[#55555A]">Updated 12 hours ago</div>
                            <p class="font-sans text-[0.85rem] text-[#55555A] leading-relaxed max-w-2xl mt-2">
                                <strong class="text-[#1C1C1E]">Usage:</strong> UI elements, footnotes, card tags, timestamps, and utility links.
                            </p>
                        </div>
                    </div>
                </div>
                """, 'html.parser')
                
                div.append(new_typo)
                break

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
