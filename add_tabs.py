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
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-2">Tabs (Top &amp; Side)</h3>
            <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Tabs are constructed using pure typography and hairline indicators. No chunky background boxes.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-start bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                
                <!-- Horizontal Tabs (Top) -->
                <div>
                    <!-- Tab List -->
                    <div class="flex gap-8 border-b-[0.5px] border-[#55555a26]">
                        <button class="pb-3 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] border-b-2 border-[#BE7555] translate-y-[1px]">Financials</button>
                        <button class="pb-3 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] hover:text-[#1C1C1E] border-b-2 border-transparent transition-colors">Masterplan</button>
                        <button class="pb-3 text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] hover:text-[#1C1C1E] border-b-2 border-transparent transition-colors">Diligence</button>
                    </div>
                    <!-- Tab Content Panel -->
                    <div class="mt-6 border-[0.5px] border-[#55555a26] rounded-sm p-8 min-h-[150px] flex items-center justify-center bg-white shadow-sm">
                        <span class="text-[0.85rem] text-[#55555A]">Horizontal tab content dynamically loads here.</span>
                    </div>
                </div>

                <!-- Vertical Tabs (Side) -->
                <div class="flex gap-8">
                    <!-- Tab List -->
                    <div class="flex flex-col gap-6 border-r-[0.5px] border-[#55555a26] w-32 shrink-0 relative">
                        <button class="text-left text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] transition-colors relative">
                            Overview
                            <div class="absolute right-[-1px] top-0 bottom-0 w-[2px] bg-[#BE7555]"></div>
                        </button>
                        <button class="text-left text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] hover:text-[#1C1C1E] transition-colors">Specs</button>
                        <button class="text-left text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#55555A] hover:text-[#1C1C1E] transition-colors">Gallery</button>
                    </div>
                    <!-- Tab Content Panel -->
                    <div class="border-[0.5px] border-[#55555a26] rounded-sm p-8 min-h-[200px] w-full flex items-center justify-center bg-white shadow-sm">
                        <span class="text-[0.85rem] text-[#55555A]">Vertical tab content dynamically loads here.</span>
                    </div>
                </div>

            </div>
        </div>
        """, 'html.parser')
        
        # We append to the space-y-16 container inside comp_sec if it exists, otherwise to comp_sec
        space_y = comp_sec.find('div', class_=lambda c: c and 'space-y-16' in c)
        if space_y:
            space_y.append(new_block)
        else:
            comp_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Tabs component injected successfully.")

update()
