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
        # Find the Lists & Breadcrumbs component to append after
        lists_heading = comp_sec.find(string=re.compile("Lists & Breadcrumbs"))
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12 mb-12">
            <h3 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-2">Pagination</h3>
            <p class="font-sans text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Minimalist progression logic for blogs and property listing pages.</p>
            
            <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-12 rounded-sm flex items-center justify-start">
                
                <nav class="flex items-center gap-6" aria-label="Pagination">
                    <!-- Previous Button -->
                    <button class="w-10 h-10 bg-white border-[0.5px] border-[#55555a26] rounded-[4px] flex items-center justify-center text-[#55555A] hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-colors" aria-label="Previous page">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"><path d="M19 12H5"></path><path d="M12 19l-7-7 7-7"></path></svg>
                    </button>
                    
                    <!-- Page Numbers -->
                    <div class="flex items-center gap-6 font-sans text-[0.95rem]">
                        <a href="#" class="font-bold text-[#1C1C1E]" aria-current="page">1</a>
                        <a href="#" class="text-[#55555A] hover:text-[#1C1C1E] transition-colors">2</a>
                        <a href="#" class="text-[#55555A] hover:text-[#1C1C1E] transition-colors">3</a>
                        <span class="text-[#55555A]">...</span>
                        <a href="#" class="text-[#55555A] hover:text-[#1C1C1E] transition-colors">8</a>
                    </div>

                    <!-- Next Button -->
                    <button class="w-10 h-10 bg-white border-[0.5px] border-[#55555a26] rounded-[4px] flex items-center justify-center text-[#55555A] hover:border-[#1C1C1E] hover:text-[#1C1C1E] transition-colors" aria-label="Next page">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
                    </button>
                </nav>
                
            </div>
        </div>
        """, 'html.parser')
        
        if lists_heading:
            lists_block = lists_heading.parent.parent
            lists_block.insert_after(new_block)
        else:
            comp_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
