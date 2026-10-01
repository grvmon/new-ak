from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    a11y_sec = soup.find(id='23-accessibility')
    if a11y_sec:
        a11y_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">23. Accessibility Architecture</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Accessibility is not a checklist item for post-launch; it is a fundamental architectural requirement. Our systems must exceed WCAG 2.1 AA standards, aiming for AAA compliance across all critical advisory flows.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Global A11y Standards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Core Modalities</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Semantic HTML First</strong> Divs and Spans are not buttons. Use native <code class="bg-black/5 px-1 rounded-sm">&lt;button&gt;</code>, <code class="bg-black/5 px-1 rounded-sm">&lt;nav&gt;</code>, and <code class="bg-black/5 px-1 rounded-sm">&lt;dialog&gt;</code> elements. ARIA is a fallback, not a crutch.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Focus Management</strong> <strong class="text-[#8B3A3A]">Never use `outline: none` without a fallback.</strong> Focus states use a strict 2px Obsidian outline offset by 2px. Modals must trap focus entirely.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Contrast (7AAA Rule)</strong> Primary text (Titanium Frost on Obsidian, or Obsidian on White) must mathematically score at least 7.0:1 contrast.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Touch Targets</strong> The absolute minimum hit area on mobile devices is <code class="bg-black/5 px-1 rounded-sm">44x44px</code>. No exceptions for pagination or tiny utility links.</li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm flex flex-col justify-center">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Motion &amp; Media</h3>
                    <p class="text-[0.85rem] text-[#55555A] mb-4">Users who prefer reduced motion or rely on screen readers must receive an identical tier of intelligence.</p>
                    <ul class="text-[0.85rem] text-[#1C1C1E] space-y-3 list-disc list-inside bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-4 rounded-sm">
                        <li><code class="text-[#804526]">prefers-reduced-motion</code>: All cinematic fade-ins must instantly resolve to opacity 100%.</li>
                        <li>Alt-text is mandatory on all asset imagery, describing architectural intent (e.g., "South-facing balcony overlooking Kaveri pipeline").</li>
                        <li>Video embeds must natively support closed captions.</li>
                    </ul>
                </div>
            </div>

            <!-- Common Failures vs Final State Matrix -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component QC: Common Failures &amp; Final State</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">A strict audit of typical real estate platform failures compared to the mandated acre&amp;key final state.</p>
                
                <div class="overflow-x-auto bg-white border-[0.5px] border-[#55555a26] rounded-sm">
                    <table class="w-full text-left border-collapse min-w-[700px]">
                        <thead>
                            <tr class="bg-[#FAFAFA] border-b-[0.5px] border-[#55555a26]">
                                <th class="py-4 px-6 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E]">Vector</th>
                                <th class="py-4 px-6 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A]">Industry Failure</th>
                                <th class="py-4 px-6 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#2C4C3B]">acre&amp;key Final State</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y-[0.5px] divide-[#55555a26] text-[0.85rem] text-[#55555A]">
                            <tr>
                                <td class="py-4 px-6 font-bold text-[#1C1C1E]">Images / Gradients</td>
                                <td class="py-4 px-6">Putting thin white text over bright skies, scoring 2.1 contrast.</td>
                                <td class="py-4 px-6">Implementation of the <strong class="text-[#1C1C1E]">7AAA Anchored Gradient</strong>. Text lives exclusively in localized Obsidian zones.</td>
                            </tr>
                            <tr>
                                <td class="py-4 px-6 font-bold text-[#1C1C1E]">Form Errors</td>
                                <td class="py-4 px-6">Turning borders red without explaining the error textually.</td>
                                <td class="py-4 px-6">Strict textual validation below inputs (e.g., "Mobile number requires 10 digits").</td>
                            </tr>
                            <tr>
                                <td class="py-4 px-6 font-bold text-[#1C1C1E]">Keyboard Focus</td>
                                <td class="py-4 px-6">Hiding the focus ring because the designer thinks it's "ugly."</td>
                                <td class="py-4 px-6">Explicit 2px Obsidian outline <code class="bg-black/5 px-1 rounded-sm">focus-visible:ring-2</code> on all interactive nodes.</td>
                            </tr>
                            <tr>
                                <td class="py-4 px-6 font-bold text-[#1C1C1E]">Touch Targets</td>
                                <td class="py-4 px-6">Tiny 16px close icons on mobile modals that users cannot tap.</td>
                                <td class="py-4 px-6">Absolute enforcement of a minimum <code class="bg-black/5 px-1 rounded-sm">w-11 h-11</code> bounding box for touch interactions.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Live Screen Reader Output Example -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: The Accessible Dossier Button</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center border-[0.5px] border-[#55555a26] p-8 rounded-sm bg-[#FAFAFA]">
                    <div>
                        <div class="bg-white p-4 border-[0.5px] border-[#55555a26] rounded-sm mb-6 inline-block shadow-sm">
                            <div class="font-bold text-[0.85rem] text-[#2C4C3B] mb-1">✓ Screen Reader Output</div>
                            <div class="font-mono text-[0.8rem] text-[#1C1C1E]">"Button. Download complete dossier for Prestige Evergreen. PDF Document, 4.2 Megabytes."</div>
                        </div>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed mb-4">Notice how the visual button just says "Download Dossier," but the <code class="bg-black/5 px-1 rounded-sm">aria-label</code> provides the critical context of what exactly will be downloaded and how large the file is.</p>
                    </div>
                    
                    <div class="flex justify-center">
                        <button 
                            class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-6 py-4 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors flex items-center gap-2 shadow-sm outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#1C1C1E]"
                            aria-label="Download complete dossier for Prestige Evergreen. PDF Document, 4.2 Megabytes."
                        >
                            Download Dossier <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        </button>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If an HNI client utilizing a screen reader or keyboard navigation cannot effortlessly book a consultation, the system is fundamentally broken.</div>
            </div>

        </div>
        """, 'html.parser')
        a11y_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
