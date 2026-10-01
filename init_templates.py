from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    templates_sec = soup.find(id='28-templates')
    if templates_sec:
        # Clear out the placeholder
        templates_sec.clear()
        
        new_block = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">28. Page Templates</h2>
        
        <div class="space-y-16 font-sans mt-8">
            <div>
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-2">Hero Architecture Blueprint</h3>
                <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">The standard V2 entrance. Split layout: Editorial typography on the left, cinematically filtered architectural photography on the right.</p>
                
                <div class="grid grid-cols-1 lg:grid-cols-2 bg-white rounded-sm overflow-hidden shadow-md border-[0.5px] border-[#55555a26] min-h-[500px]">
                    
                    <!-- Left Side (Typography) -->
                    <div class="p-10 md:p-16 xl:p-20 flex flex-col justify-center">
                        <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-6">Pre-Launch Advisory</div>
                        <h1 class="font-serif text-[2.25rem] md:text-[2.75rem] text-[#1C1C1E] leading-[1.15] mb-6">
                            Institutional-Grade Assets in Whitefield.
                        </h1>
                        <p class="font-sans text-[1rem] text-[#55555A] leading-relaxed max-w-sm mb-10">
                            Access proprietary risk-assessment frameworks before allocating capital to under-construction developments.
                        </p>
                        <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-8 py-3.5 rounded-sm font-sans text-[0.9rem] font-semibold transition-colors w-fit shadow-sm">
                            Get Buyer Analysis
                        </button>
                    </div>

                    <!-- Right Side (Image) -->
                    <div class="relative min-h-[350px] lg:min-h-full overflow-hidden border-l-[0.5px] border-[#55555a26]">
                        <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80')] bg-cover bg-center contrast-[1.05] hover:scale-105 transition-transform duration-[2000ms] ease-out"></div>
                    </div>
                    
                </div>
            </div>
        </div>
        """, 'html.parser')
        
        templates_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
