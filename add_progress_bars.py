from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # We find the Analytical Tables section
    tables_heading = soup.find(string=re.compile("Analytical Tables"))
    if tables_heading:
        # parent of heading is h3, parent of h3 is div
        tables_block = tables_heading.parent.parent
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12 mb-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Progress Bars &amp; Counters</h3>
            <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-12 max-w-3xl">Avoid thick, colorful progress bars. Use ultra-thin (2px) tracks. Counters must pair massive serif numerals with tiny, tracked-out sans-serif labels.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 md:p-12 rounded-sm items-center">
                
                <!-- Counters (Left) -->
                <div class="flex gap-16">
                    <div>
                        <div class="font-serif text-[3.5rem] md:text-[4.5rem] text-[#1C1C1E] leading-none mb-4">69</div>
                        <div class="font-sans text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555]">Diligence Checks</div>
                    </div>
                    <div>
                        <div class="font-serif text-[3.5rem] md:text-[4.5rem] text-[#1C1C1E] leading-none mb-4 flex items-baseline">14<span class="text-[1.75rem] md:text-[2.25rem] text-[#55555A] ml-1">%</span></div>
                        <div class="font-sans text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555]">Target Cagr</div>
                    </div>
                </div>

                <!-- Progress Bars (Right) -->
                <div class="flex flex-col justify-center gap-10 w-full max-w-md ml-auto">
                    <!-- Bar 1 -->
                    <div>
                        <div class="flex justify-between items-end mb-3">
                            <span class="font-sans text-[0.8rem] font-bold text-[#1C1C1E]">Project Completion</span>
                            <span class="font-sans text-[0.8rem] text-[#55555A]">85%</span>
                        </div>
                        <div class="w-full h-[2px] bg-[#55555a26] relative rounded-full">
                            <div class="absolute left-0 top-0 bottom-0 w-[85%] bg-[#BE7555] rounded-full transition-all duration-[1500ms] ease-out"></div>
                        </div>
                    </div>
                    <!-- Bar 2 -->
                    <div>
                        <div class="flex justify-between items-end mb-3">
                            <span class="font-sans text-[0.8rem] font-bold text-[#1C1C1E]">Inventory Sold</span>
                            <span class="font-sans text-[0.8rem] text-[#55555A]">40%</span>
                        </div>
                        <div class="w-full h-[2px] bg-[#55555a26] relative rounded-full">
                            <div class="absolute left-0 top-0 bottom-0 w-[40%] bg-[#BE7555] rounded-full transition-all duration-[1500ms] ease-out"></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        """, 'html.parser')
        
        tables_block.insert_before(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
