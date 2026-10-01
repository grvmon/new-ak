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
        pag_heading = comp_sec.find(string=re.compile("Pagination"))
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12 mb-12">
            <h3 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-2">Global Footer Architecture</h3>
            <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">The footer acts as the anchor. Links are strictly organized in grid columns without bulky separators.</p>
            
            <div class="border-[0.5px] border-[#55555a26] rounded-sm overflow-hidden bg-white p-8">
                
                <footer class="bg-[#1C1C1E] text-white py-16 px-10 rounded-sm">
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 lg:gap-8">
                        
                        <!-- Col 1: Brand -->
                        <div class="lg:col-span-2 flex flex-col justify-between">
                            <div>
                                <div class="font-logo text-[1.5rem] font-semibold tracking-[-0.02em] text-[#FAFAFA] mb-4">acre&amp;key</div>
                                <p class="font-sans text-[0.85rem] text-[#FAFAFA]/70 leading-relaxed max-w-sm">
                                    Institutional-grade real estate advisory. <br/>Evaluating risk and structure before capital.
                                </p>
                            </div>
                            
                            <div class="mt-8 flex items-center gap-4">
                                <a href="#" class="w-8 h-8 rounded-full bg-white/5 border-[0.5px] border-white/10 flex items-center justify-center text-white/70 hover:text-white hover:bg-white/10 transition-colors">
                                    <span class="sr-only">LinkedIn</span>
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                                </a>
                            </div>
                        </div>

                        <!-- Col 2: Properties -->
                        <div>
                            <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-6">Properties</div>
                            <ul class="flex flex-col gap-4 font-sans text-[0.85rem]">
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">North Bengaluru</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Whitefield</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Central Business District</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">South Bengaluru</a></li>
                            </ul>
                        </div>

                        <!-- Col 3: Intelligence -->
                        <div>
                            <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-6">Intelligence</div>
                            <ul class="flex flex-col gap-4 font-sans text-[0.85rem]">
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Macro Reports</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Risk Assessment Framework</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Pricing Analytics</a></li>
                            </ul>
                        </div>

                        <!-- Col 4: Corporate -->
                        <div>
                            <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-6">Corporate</div>
                            <ul class="flex flex-col gap-4 font-sans text-[0.85rem]">
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">About Us</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">The Partnership</a></li>
                                <li><a href="#" class="text-[#FAFAFA]/70 hover:text-white transition-colors">Careers</a></li>
                            </ul>
                        </div>

                    </div>

                    <!-- Bottom Bar -->
                    <div class="mt-16 pt-8 border-t-[0.5px] border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">
                        <div class="font-sans text-[0.75rem] text-[#FAFAFA]/50">
                            &copy; 2026 acre&amp;key. All rights reserved.
                        </div>
                        <div class="flex items-center gap-6 font-sans text-[0.75rem]">
                            <a href="#" class="text-[#FAFAFA]/50 hover:text-[#FAFAFA]/80 transition-colors">Privacy Policy</a>
                            <a href="#" class="text-[#FAFAFA]/50 hover:text-[#FAFAFA]/80 transition-colors">Terms of Service</a>
                        </div>
                    </div>
                </footer>
                
            </div>
        </div>
        """, 'html.parser')
        
        if pag_heading:
            pag_block = pag_heading.parent.parent
            pag_block.insert_after(new_block)
        else:
            comp_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
