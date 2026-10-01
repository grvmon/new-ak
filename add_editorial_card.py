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
        # Find the Global Footer Architecture to insert before
        footer_heading = comp_sec.find(string=re.compile("Global Footer Architecture"))
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12 mb-12">
            <h3 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-2">Editorial Data Cards (Checklists)</h3>
            <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Used for feature lists or diligence breakdowns. <strong class="text-[#1C1C1E]">Crucial Rule:</strong> The overlapping badge must strictly use the 4px micro-edge geometry. Circular pill badges are banned in the HNI architecture.</p>
            
            <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 md:p-12 rounded-sm flex justify-center items-center">
                
                <!-- Editorial Data Card -->
                <div class="w-full max-w-[400px] bg-white border-[0.5px] border-[#55555a26] rounded-[4px] shadow-sm overflow-hidden flex flex-col">
                    
                    <!-- Top Image Section -->
                    <div class="relative h-[200px] w-full bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center">
                        <!-- Overlapping Badge -->
                        <div class="absolute -bottom-4 left-6 bg-[#BE7555] text-white text-[0.75rem] font-bold tracking-[0.1em] px-3 py-1.5 rounded-[4px] border-2 border-white shadow-sm z-10">
                            01.
                        </div>
                    </div>
                    
                    <!-- Body Section -->
                    <div class="pt-10 px-8 pb-8 relative z-0">
                        <h4 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-1">Location</h4>
                        <p class="font-sans text-[0.85rem] text-[#55555A] mb-8">Connectivity, Security &amp; Demand</p>
                        
                        <ul class="space-y-4 font-sans text-[0.85rem] text-[#1C1C1E]">
                            <li class="flex items-start gap-3">
                                <span class="text-[#BE7555] font-bold mt-0.5"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                                <span class="leading-relaxed">Employment &amp; IT corridor connectivity</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="text-[#BE7555] font-bold mt-0.5"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                                <span class="leading-relaxed">Metro line progress &amp; road widening realities</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="text-[#BE7555] font-bold mt-0.5"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg></span>
                                <span class="leading-relaxed">Ground-water security &amp; social infra data</span>
                            </li>
                        </ul>
                    </div>
                    
                    <!-- Footer Section -->
                    <div class="bg-[#FAFAFA] border-t-[0.5px] border-[#55555a26] px-8 py-6">
                        <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">Questions We Answer</div>
                        <p class="font-sans text-[0.85rem] text-[#55555A] mb-2">Is long-term demand <strong class="text-[#1C1C1E]">sustainable?</strong></p>
                        <p class="font-sans text-[0.85rem] text-[#55555A]">Is infrastructure <strong class="text-[#1C1C1E]">keeping pace?</strong></p>
                    </div>
                    
                </div>
                
            </div>
        </div>
        """, 'html.parser')
        
        if footer_heading:
            footer_block = footer_heading.parent.parent
            footer_block.insert_before(new_block)
        else:
            comp_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
