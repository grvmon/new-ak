from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    comp_sec = soup.find(id='12-components')
    if comp_sec:
        comp_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">12. Component Library</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The acre&key component library is a strict, atomic design system. A developer should be able to build the website entirely by composing these approved components instead of inventing new UI. Every component must pass the AAA accessibility threshold and respect the 4px geometry rule.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- System Status & Inventory -->
            <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Master Component Inventory</h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b-[0.5px] border-[#55555a26]">
                                <th class="py-3 px-4 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]">Component</th>
                                <th class="py-3 px-4 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]">Purpose</th>
                                <th class="py-3 px-4 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]">Status</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y-[0.5px] divide-[#55555a26] text-[0.85rem] text-[#55555A]">
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Global Header &amp; Nav</td>
                                <td class="py-4 px-4">Primary wayfinding, branding, and global CTA.</td>
                                <td class="py-4 px-4"><span class="bg-[#2C4C3B]/10 text-[#2C4C3B] px-2 py-1 rounded-sm text-[0.75rem] font-bold">LOCKED</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Buttons (CTA)</td>
                                <td class="py-4 px-4">Primary, Secondary, Ghost, and Outline actions.</td>
                                <td class="py-4 px-4"><span class="bg-[#2C4C3B]/10 text-[#2C4C3B] px-2 py-1 rounded-sm text-[0.75rem] font-bold">LOCKED</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Cards (Property &amp; Editorial)</td>
                                <td class="py-4 px-4">Displaying assets or methodologies using the 16:9 cinematic ratio.</td>
                                <td class="py-4 px-4"><span class="bg-[#2C4C3B]/10 text-[#2C4C3B] px-2 py-1 rounded-sm text-[0.75rem] font-bold">LOCKED</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Tabs (Top &amp; Side)</td>
                                <td class="py-4 px-4">Navigating sibling content views without reloading.</td>
                                <td class="py-4 px-4"><span class="bg-[#8B3A3A]/10 text-[#8B3A3A] px-2 py-1 rounded-sm text-[0.75rem] font-bold">REVISION REQUIRED</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Accordions (Dossier Specs)</td>
                                <td class="py-4 px-4">Collapsing dense technical specs and FAQs.</td>
                                <td class="py-4 px-4"><span class="bg-[#8B3A3A]/10 text-[#8B3A3A] px-2 py-1 rounded-sm text-[0.75rem] font-bold">REVISION REQUIRED</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Alerts &amp; Tooltips</td>
                                <td class="py-4 px-4">Providing context or system success/error feedback.</td>
                                <td class="py-4 px-4"><span class="bg-[#804526]/10 text-[#804526] px-2 py-1 rounded-sm text-[0.75rem] font-bold">MISSING STATES</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Badges &amp; Tags</td>
                                <td class="py-4 px-4">RERA status, typology, and metric tagging.</td>
                                <td class="py-4 px-4"><span class="bg-[#804526]/10 text-[#804526] px-2 py-1 rounded-sm text-[0.75rem] font-bold">MISSING STATES</span></td>
                            </tr>
                            <tr>
                                <td class="py-4 px-4 font-bold text-[#1C1C1E]">Modals / Dialogs</td>
                                <td class="py-4 px-4">Focus-trapping high-intent flows (e.g., Lead Capture).</td>
                                <td class="py-4 px-4"><span class="bg-black/5 text-[#55555A] px-2 py-1 rounded-sm text-[0.75rem] font-bold">PENDING ARCHITECTURE</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Global Component State Matrix -->
            <div>
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Global State &amp; Anatomy Rules</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Every interactive component in the system must account for the following states. If a component does not explicitly define these states, it cannot be shipped.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-2 flex justify-between items-center">Default <span>⌘</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">The baseline aesthetic. Contrast must meet AAA accessibility. Typography is Manrope 600 or 700.</p>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm shadow-sm ring-1 ring-[#1C1C1E]/5">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-2 flex justify-between items-center">Hover <span>↗</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Background colors shift 1-2 stops darker (e.g., Copper to Dark Copper). Cursor shifts to pointer. Transition duration is 150ms.</p>
                    </div>
                    <div class="bg-white border-[2px] border-[#1C1C1E] p-6 rounded-sm">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-2 flex justify-between items-center">Focus <span>⇥</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Critical for accessibility. A strict 2px Obsidian outline offset by 2px from the element. Never hide focus rings.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm opacity-90 scale-[0.98] transition-transform">
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-2 flex justify-between items-center">Active / Pressed <span>↓</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">The component physically reacts to touch. Scale down to 98% and increase background darkness momentarily.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm opacity-50 cursor-not-allowed">
                        <div class="font-bold text-[#55555A] text-[1.05rem] mb-2 flex justify-between items-center">Disabled <span>⨯</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Opacity drops to 40-50%. Pointer-events are set to none. Copper is desaturated to neutral grey.</p>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-r from-transparent via-[#FAFAFA] to-transparent animate-[shimmer_1.5s_infinite] opacity-50"></div>
                        <div class="font-bold text-[#1C1C1E] text-[1.05rem] mb-2 flex justify-between items-center relative z-10">Loading <span>⟳</span></div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed relative z-10">No spinning wheels. The component maintains its geometry but fills with a Titanium Frost shimmer skeleton.</p>
                    </div>
                </div>
            </div>

            <!-- Specific Component Deep Dive: Buttons -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: The Button System</h3>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm mb-8">
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-8 items-center">
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-4">Primary</div>
                            <button class="w-full bg-[#BE7555] hover:bg-[#9F5334] text-white px-5 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors flex items-center justify-center gap-2">
                                Book Call <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
                            </button>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-4">Secondary (Dark)</div>
                            <button class="w-full bg-[#1C1C1E] hover:bg-[#1C1C1E]/80 text-white px-5 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors flex items-center justify-center gap-2">
                                View Dossier
                            </button>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-4">Outline</div>
                            <button class="w-full bg-transparent border-[0.5px] border-[#1C1C1E] text-[#1C1C1E] hover:bg-black/5 px-5 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors flex items-center justify-center gap-2">
                                Download Map
                            </button>
                        </div>
                        <div>
                            <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] mb-4">Ghost (Text)</div>
                            <button class="w-full bg-transparent text-[#BE7555] hover:bg-[#BE7555]/10 px-5 py-3 rounded-sm font-sans text-[0.85rem] font-semibold transition-colors flex items-center justify-center gap-2">
                                Read more <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M9 18l6-6-6-6"></path></svg>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="font-bold text-[0.95rem] text-[#1C1C1E] mb-3">Anatomy &amp; Rules</h4>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li><strong class="text-[#1C1C1E]">Height:</strong> Minimum 44px on mobile, 40px on desktop.</li>
                            <li><strong class="text-[#1C1C1E]">Radius:</strong> Global 4px micro-edge. No pill buttons.</li>
                            <li><strong class="text-[#1C1C1E]">Typography:</strong> Manrope 600 or 700. Sentence case preferred.</li>
                            <li><strong class="text-[#1C1C1E]">Icons:</strong> Strict 1.5px stroke width. Usually placed on the right.</li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-bold text-[0.95rem] text-[#1C1C1E] mb-3">Responsive Behavior</h4>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-2 list-disc list-inside">
                            <li>On Desktop/Tablet: Buttons fit their content with generous horizontal padding (px-6).</li>
                            <li>On Mobile: Primary CTAs must span <code class="bg-black/5 px-1 rounded-sm">w-full</code> to ensure thumb-reachability. Secondary buttons may remain inline if placed side-by-side.</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If a component is built as a one-off custom element, it is technical debt. Build it centrally, or do not build it.</div>
            </div>

        </div>
        """, 'html.parser')
        comp_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
