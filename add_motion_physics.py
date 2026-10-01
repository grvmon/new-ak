from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    motion_sec = soup.find(id='11-motion')
    if motion_sec:
        # Create the new block for Geometry & Motion Physics
        new_block = BeautifulSoup("""
        <div class="mt-16 border-t-[0.5px] border-[#55555a26] pt-12">
            <h3 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-4">Geometry &amp; Motion Physics</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-12 max-w-3xl">Strictly 4px border radiuses and 0.5px hairlines. All movement runs on Acre&amp;Key Motion Physics: a suite of cinematic, gravity-weighted CSS animations that avoid cheap "bouncy" effects in favor of slow, deliberate reveals.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- 1. Cinematic Reveal -->
                <div class="border-[0.5px] border-[#55555a26] rounded-sm p-8 bg-white group cursor-pointer overflow-hidden relative min-h-[300px] flex flex-col justify-end">
                    <div class="absolute inset-0 bg-[#FAFAFA] transition-colors duration-700 ease-out group-hover:bg-[#1C1C1E]"></div>
                    <div class="relative z-10">
                        <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-2 opacity-0 -translate-y-4 transition-all duration-[600ms] ease-out group-hover:opacity-100 group-hover:translate-y-0">1. Cinematic Reveal</div>
                        <h4 class="font-serif text-[1.25rem] text-[#1C1C1E] group-hover:text-[#FAFAFA] transition-colors duration-[600ms] ease-out mb-2">Hover to Reveal</h4>
                        <p class="font-sans text-[0.85rem] text-[#55555A] group-hover:text-[#FAFAFA]/70 transition-colors duration-[600ms] ease-out max-w-xs">0.6s cubic-bezier. Slow, deliberate text and color transitions that feel heavy and expensive.</p>
                    </div>
                </div>

                <!-- 2. Data Cascade -->
                <div class="border-[0.5px] border-[#55555a26] rounded-sm p-8 bg-white group cursor-pointer overflow-hidden min-h-[300px]">
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#1C1C1E] mb-6">2. Data Cascade</div>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center border-b-[0.5px] border-[#55555a26] pb-3 opacity-50 translate-x-4 transition-all duration-500 ease-out group-hover:opacity-100 group-hover:translate-x-0">
                            <span class="font-sans text-[0.85rem] text-[#55555A]">Data Row 1</span>
                            <span class="font-sans text-[0.85rem] font-bold text-[#1C1C1E]">0.0s delay</span>
                        </div>
                        <div class="flex justify-between items-center border-b-[0.5px] border-[#55555a26] pb-3 opacity-50 translate-x-4 transition-all duration-500 ease-out delay-[100ms] group-hover:opacity-100 group-hover:translate-x-0">
                            <span class="font-sans text-[0.85rem] text-[#55555A]">Data Row 2</span>
                            <span class="font-sans text-[0.85rem] font-bold text-[#1C1C1E]">0.1s delay</span>
                        </div>
                        <div class="flex justify-between items-center border-b-[0.5px] border-[#55555a26] pb-3 opacity-50 translate-x-4 transition-all duration-500 ease-out delay-[200ms] group-hover:opacity-100 group-hover:translate-x-0">
                            <span class="font-sans text-[0.85rem] text-[#55555A]">Data Row 3</span>
                            <span class="font-sans text-[0.85rem] font-bold text-[#1C1C1E]">0.2s delay</span>
                        </div>
                    </div>
                </div>

                <!-- 3. Architectural Pan -->
                <div class="border-[0.5px] border-[#1C1C1E] rounded-sm group cursor-pointer overflow-hidden relative min-h-[300px] flex flex-col justify-end">
                    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center transition-transform duration-[2000ms] ease-out group-hover:scale-110"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent opacity-80 group-hover:opacity-100 transition-opacity duration-1000"></div>
                    <div class="relative z-10 p-8">
                        <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-2">3. Architectural Pan</div>
                        <h4 class="font-serif text-[1.25rem] text-[#FAFAFA] mb-2">Hover Pan Demo</h4>
                        <p class="font-sans text-[0.85rem] text-[#FAFAFA]/70 max-w-xs">Massive 2.0s duration. The image slowly scales without distortion, simulating a slow camera dolly.</p>
                    </div>
                </div>

                <!-- 4. Focus Blur (Modal) -->
                <div class="border-[0.5px] border-[#55555a26] rounded-sm group cursor-pointer overflow-hidden relative min-h-[300px] flex items-center justify-center bg-[#FAFAFA] bg-[url('/assets/grid-pattern.svg')]">
                    <!-- Background content that gets blurred -->
                    <div class="absolute inset-0 p-8 flex flex-col gap-4 opacity-50 transition-all duration-[600ms] ease-out group-hover:blur-md group-hover:scale-[0.98]">
                        <div class="w-full h-8 bg-black/5 rounded-sm"></div>
                        <div class="w-3/4 h-8 bg-black/5 rounded-sm"></div>
                        <div class="w-full h-32 bg-black/5 rounded-sm"></div>
                    </div>
                    
                    <!-- Overlay modal -->
                    <div class="absolute inset-0 bg-[#1C1C1E]/0 transition-colors duration-[600ms] group-hover:bg-[#1C1C1E]/40 pointer-events-none"></div>
                    
                    <!-- Modal content -->
                    <div class="relative z-10 bg-white border-[0.5px] border-[#1C1C1E] p-6 rounded-sm shadow-2xl opacity-0 translate-y-8 transition-all duration-[600ms] ease-out delay-100 group-hover:opacity-100 group-hover:translate-y-0 w-3/4 text-center">
                        <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-2">4. Focus Blur</div>
                        <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-2">Modal Physics</h4>
                        <p class="font-sans text-[0.8rem] text-[#55555A]">Background recedes and blurs (0.98x scale) while the modal pushes up with gravity.</p>
                    </div>
                </div>

            </div>
        </div>
        """, 'html.parser')
        
        # Append before the closing Principle of the Motion section
        # The Motion section has a Final Principle at the end
        principle = motion_sec.find(string=re.compile("If an animation triggers motion sickness"))
        if principle:
            parent_principle = principle.parent.parent
            parent_principle.insert_before(new_block)
        else:
            motion_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
