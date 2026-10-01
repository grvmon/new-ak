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
        # Find the tabs component to append after
        tabs_heading = comp_sec.find(string=re.compile("Tabs \(Top & Side\)"))
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12 mt-12 mb-12">
            <h3 class="font-serif text-[1.5rem] text-[#1C1C1E] mb-8">Lists &amp; Breadcrumbs</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start bg-[#FAFAFA] p-8 md:p-12 border-[0.5px] border-[#55555a26] rounded-sm">
                
                <!-- Breadcrumbs (Left) -->
                <div>
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#55555A] mb-8">Breadcrumb Path</div>
                    <div class="flex items-center gap-3 text-[0.85rem] font-sans">
                        <a href="#" class="text-[#55555A] hover:text-[#1C1C1E] transition-colors">Home</a>
                        <span class="text-[#55555a26]">/</span>
                        <a href="#" class="text-[#55555A] hover:text-[#1C1C1E] transition-colors">Advisory</a>
                        <span class="text-[#55555a26]">/</span>
                        <span class="text-[#1C1C1E] font-bold">Prestige Evergreen</span>
                    </div>
                </div>

                <!-- Architectural Lists (Right) -->
                <div>
                    <div class="text-[0.65rem] font-bold tracking-[0.15em] uppercase text-[#55555A] mb-8">Architectural Lists</div>
                    <ul class="space-y-5 font-sans text-[0.9rem] text-[#55555A]">
                        <li class="flex items-start gap-4">
                            <span class="w-1.5 h-1.5 bg-[#BE7555] mt-[0.4rem] shrink-0"></span>
                            <span>Title deeds verified against RERA database.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="w-1.5 h-1.5 bg-[#BE7555] mt-[0.4rem] shrink-0"></span>
                            <span>Masterplan audited for hyper-density risk metrics.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="w-1.5 h-1.5 bg-[#BE7555] mt-[0.4rem] shrink-0"></span>
                            <span>Comparative pricing analysis completed.</span>
                        </li>
                    </ul>
                </div>
                
            </div>
        </div>
        """, 'html.parser')
        
        if tabs_heading:
            tabs_block = tabs_heading.parent.parent
            tabs_block.insert_after(new_block)
        else:
            comp_sec.append(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected successfully.")

update()
