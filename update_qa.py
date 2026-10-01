from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    qa_sec = soup.find(id='29-qa')
    if qa_sec:
        qa_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">29. QA &amp; Governance</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">A design system is only as strong as the governance enforcing it. This is the final launch checklist and the absolute criteria for pushing code to production. Nothing goes live without clearing this matrix.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Governance & Approvals -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">System Governance</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-6 leading-relaxed">Who approves changes, and when can a new component be added?</p>
                    <ul class="text-[0.85rem] text-[#1C1C1E] space-y-4">
                        <li class="flex items-start gap-3 border-b-[0.5px] border-[#55555a26] pb-3">
                            <span class="text-[#2C4C3B] font-bold mt-0.5">✓</span>
                            <div>
                                <strong class="block mb-1">Component Admission</strong>
                                A new component may only be added if the existing component library cannot solve the architectural requirement natively. Do not invent UI when an existing tokenized structure suffices.
                            </div>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="text-[#2C4C3B] font-bold mt-0.5">✓</span>
                            <div>
                                <strong class="block mb-1">The Approval Protocol</strong>
                                Code cannot be merged by a single developer. Visual deviations from this styleguide require approval from the Lead Designer. Functional deviations require approval from the Technical Director.
                            </div>
                        </li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">The Master Instruction</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-4 leading-relaxed">All AI-assisted development and human auditing must adhere strictly to the following mandate:</p>
                    <div class="bg-[#1C1C1E] p-4 rounded-sm border-l-[4px] border-[#BE7555] font-serif text-[1rem] text-[#FAFAFA] italic leading-[1.6]">
                        "Do not redesign or introduce a new visual direction. Audit against the existing acre&amp;key design DNA and make the minimum changes required to make the system complete, consistent, unambiguous and production-ready."
                    </div>
                </div>
            </div>

            <!-- The Final Launch Checklist -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">The Pre-Flight Matrix (Final Checklist)</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Before deploying any page to production, the engineering and QA teams must mathematically verify the following items.</p>
                
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    
                    <!-- Visual & Structural -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden">
                        <div class="bg-[#FAFAFA] px-6 py-3 border-b-[0.5px] border-[#55555a26]">
                            <span class="font-bold text-[0.75rem] tracking-[0.1em] uppercase text-[#1C1C1E]">Visual &amp; Structural QA</span>
                        </div>
                        <ul class="divide-y-[0.5px] divide-[#55555a26] text-[0.85rem]">
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Brand:</strong> Is the logo Josefin Sans, completely untampered with, and separated from brand typography?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Typography:</strong> Are all H1s Marcellus, and all Body/Data texts Manrope?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Color:</strong> Is Copper restricted strictly to accents and primary CTAs?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Spacing:</strong> Is everything scaled perfectly on the strict 4px geometry?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Responsive:</strong> Do all properties stack perfectly to mobile without hiding data?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">UX:</strong> Are all buttons functioning as Advisory Intake (vs broker "Buy Now")?</div>
                            </li>
                        </ul>
                    </div>

                    <!-- Tech & Compliance -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden">
                        <div class="bg-[#FAFAFA] px-6 py-3 border-b-[0.5px] border-[#55555a26]">
                            <span class="font-bold text-[0.75rem] tracking-[0.1em] uppercase text-[#1C1C1E]">Technical &amp; Compliance QA</span>
                        </div>
                        <ul class="divide-y-[0.5px] divide-[#55555a26] text-[0.85rem]">
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Accessibility (7AAA):</strong> Do all text overlays sit securely in localized Obsidian gradients scoring 7.0:1?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">SEO:</strong> Are metadata tags perfectly generated per asset route?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Performance:</strong> Are massive architectural renders loaded through <code class="bg-black/5 px-1 rounded-sm">next/image</code>?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">RERA &amp; DPDP:</strong> Are all registration numbers visible? Is WhatsApp consent explicitly decoupled?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Data &amp; Content:</strong> Are all numerical projections cited? Is marketing fluff removed?</div>
                            </li>
                            <li class="px-6 py-4 flex items-start gap-4 hover:bg-black/5 transition-colors">
                                <input type="checkbox" class="mt-1 accent-[#1C1C1E]" disabled checked />
                                <div><strong class="text-[#1C1C1E]">Analytics:</strong> Are lead-capture events firing cleanly into the secure backend?</div>
                            </li>
                        </ul>
                    </div>

                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Excellence is not an accident. It is the result of relentless governance. Do not ship until the matrix is cleared.</div>
            </div>

        </div>
        """, 'html.parser')
        qa_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
