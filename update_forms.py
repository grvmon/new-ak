from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    forms_sec = soup.find(id='13-forms')
    if forms_sec:
        forms_sec.clear()
        
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">13. Forms &amp; Advisory UX</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The experience must feel like a private advisory intake, not a lead-generation landing page. We do not demand data; we ask for context to provide rigorous analysis.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Core Form Primitives -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Input Primitives</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Architecture</strong> <code class="bg-black/5 px-1 rounded-sm text-[#804526]">0.5px</code> borders. <code class="bg-black/5 px-1 rounded-sm">4px</code> radius. Generous 48px height minimum.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Focus State</strong> Inputs do not glow blue. Focus relies on a strict 1.5px Obsidian (#1C1C1E) border.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Typography</strong> Labels are <code class="bg-black/5 px-1 rounded-sm">0.75rem uppercase tracking-widest</code> to feel like documentation. Input text is large and legible (16px minimum).</li>
                    </ul>
                </div>

                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm space-y-6 flex flex-col justify-center">
                    
                    <!-- Default Input -->
                    <div>
                        <label class="block text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#55555A] mb-2">Full Legal Name</label>
                        <input type="text" placeholder="e.g. Jonathan Doe" class="w-full bg-[#FAFAFA] border-[0.5px] border-[#55555a26] text-[#1C1C1E] px-4 py-3 rounded-sm font-sans focus:outline-none focus:border-[#1C1C1E] focus:ring-0 transition-colors placeholder:text-[#55555A]/40" />
                    </div>

                    <!-- Error Input -->
                    <div>
                        <label class="block text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#8B3A3A] mb-2">Phone Number</label>
                        <div class="relative">
                            <span class="absolute left-4 top-3.5 text-[#1C1C1E] font-semibold">+91</span>
                            <input type="text" value="98765 4" class="w-full bg-[#8B3A3A]/5 border-[1px] border-[#8B3A3A]/40 text-[#1C1C1E] pl-12 pr-4 py-3 rounded-sm font-sans focus:outline-none focus:border-[#8B3A3A] transition-colors" />
                            <div class="absolute right-4 top-3.5 text-[#8B3A3A]">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                            </div>
                        </div>
                        <div class="text-[#8B3A3A] text-[0.75rem] font-medium mt-2">Mobile number must contain 10 digits.</div>
                    </div>
                </div>
            </div>

            <!-- Qualification Components (Checkboxes / Radio alternatives) -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Qualification &amp; Selection</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Standard radio buttons feel cheap. We use architectural selection tiles for acquiring context regarding budget, timeline, and typology. They must be thumb-friendly on mobile (w-full stack) and grid-aligned on desktop.</p>
                
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm mb-8">
                    <div class="text-[0.7rem] font-bold tracking-[0.15em] uppercase text-[#55555A] mb-4">Investment Horizon (Select one)</div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <!-- Unselected -->
                        <div class="border-[0.5px] border-[#55555a26] bg-white p-4 rounded-sm cursor-pointer hover:border-[#1C1C1E]/30 transition-colors flex items-center justify-between group">
                            <span class="font-sans text-[0.9rem] font-semibold text-[#55555A] group-hover:text-[#1C1C1E]">Ready to Move</span>
                            <div class="w-4 h-4 rounded-full border-[0.5px] border-[#55555a26]"></div>
                        </div>
                        <!-- Selected -->
                        <div class="border-[1.5px] border-[#1C1C1E] bg-white p-4 rounded-sm cursor-pointer shadow-sm flex items-center justify-between">
                            <span class="font-sans text-[0.9rem] font-bold text-[#1C1C1E]">Within 6 Months</span>
                            <div class="w-4 h-4 rounded-full border-[4px] border-[#1C1C1E]"></div>
                        </div>
                        <!-- Unselected -->
                        <div class="border-[0.5px] border-[#55555a26] bg-white p-4 rounded-sm cursor-pointer hover:border-[#1C1C1E]/30 transition-colors flex items-center justify-between group">
                            <span class="font-sans text-[0.9rem] font-semibold text-[#55555A] group-hover:text-[#1C1C1E]">2-3 Years (Under Construction)</span>
                            <div class="w-4 h-4 rounded-full border-[0.5px] border-[#55555a26]"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Validation & Consent -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Consent &amp; Compliance</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">No Tricks</strong> Consent to be contacted on WhatsApp or Phone must be explicitly un-checked by default or clearly stated below the CTA.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">OTP Verification</strong> The OTP input should use a 4 or 6-box segmented grid, not a single long text field, reinforcing technical security.</li>
                    </ul>
                </div>
                
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm flex flex-col justify-center">
                    <label class="flex items-start gap-3 cursor-pointer group">
                        <div class="relative flex items-start pt-0.5">
                            <input type="checkbox" checked class="peer sr-only" />
                            <div class="w-4 h-4 bg-[#FAFAFA] border-[0.5px] border-[#1C1C1E] rounded-sm peer-checked:bg-[#1C1C1E] flex items-center justify-center transition-colors">
                                <svg class="opacity-100 text-white w-3 h-3" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg>
                            </div>
                        </div>
                        <div class="text-[0.8rem] text-[#55555A] leading-relaxed">
                            I authorize acre&amp;key to send me dossier updates, floorplans, and pricing analytics via WhatsApp. I can opt-out at any time.
                        </div>
                    </label>
                </div>
            </div>

            <!-- Loading & Success -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">System Feedback States</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- Processing -->
                    <div class="bg-white border-[0.5px] border-[#1C1C1E] p-8 rounded-sm relative overflow-hidden flex flex-col items-center justify-center text-center">
                        <div class="absolute top-0 left-0 h-1 bg-[#1C1C1E] animate-[shimmer_2s_infinite] w-[30%]"></div>
                        <div class="text-[#55555A] mb-3">
                            <svg class="animate-spin text-[#1C1C1E]" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 12a9 9 0 11-6.219-8.56"></path></svg>
                        </div>
                        <h4 class="font-bold text-[1rem] text-[#1C1C1E]">Processing Request</h4>
                        <p class="text-[0.85rem] text-[#55555A] mt-2">Authenticating credentials...</p>
                    </div>

                    <!-- Success -->
                    <div class="bg-[#2C4C3B]/5 border-[0.5px] border-[#2C4C3B]/20 p-8 rounded-sm flex flex-col items-center justify-center text-center">
                        <div class="text-[#2C4C3B] mb-3">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                        </div>
                        <h4 class="font-bold text-[1rem] text-[#2C4C3B]">Intake Successful</h4>
                        <p class="text-[0.85rem] text-[#2C4C3B]/80 mt-2">An advisor will be assigned to your mandate shortly.</p>
                    </div>
                </div>
            </div>

            <!-- The Principle -->
            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If the form feels like a marketing funnel, it has failed. It must feel like an application for institutional intelligence.</div>
            </div>

        </div>
        """, 'html.parser')
        forms_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
