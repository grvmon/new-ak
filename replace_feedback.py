from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    feedback_heading = soup.find(string=re.compile("System Feedback States"))
    if feedback_heading:
        feedback_block = feedback_heading.parent.parent
        
        new_block = BeautifulSoup("""
        <div class="border-t-[0.5px] border-[#55555a26] pt-12">
            <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-2">Alerts &amp; Tooltips</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Success messages and tooltips must avoid standard green/red blocks. We use architectural boxes with sharp copper anchor lines.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-8 md:p-12 rounded-sm items-center">
                
                <!-- Alert Box -->
                <div class="bg-white border-y-[0.5px] border-r-[0.5px] border-[#55555a26] border-l-[3px] border-l-[#BE7555] p-6 rounded-r-sm shadow-sm flex items-start gap-4 w-full">
                    <div class="text-[#BE7555] font-serif italic text-lg leading-none pt-0.5">i</div>
                    <div>
                        <h4 class="font-bold text-[0.95rem] text-[#1C1C1E] mb-1">Report Dispatched</h4>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">The 69-point buyer analysis has been securely emailed to your registered address.</p>
                    </div>
                </div>

                <!-- Tooltip -->
                <div class="flex flex-col items-center justify-center min-h-[150px]">
                    <div class="relative group cursor-help">
                        <!-- Tooltip Box (Appears on Hover) -->
                        <div class="absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-[220px] bg-[#1C1C1E] text-center p-3 rounded-sm shadow-lg opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-[300ms] ease-out pointer-events-none z-10">
                            <p class="text-[0.75rem] text-[#FAFAFA]/90 leading-relaxed">A highly specific definition of a complex real estate term.</p>
                            <!-- Triangle point -->
                            <div class="absolute top-full left-1/2 -translate-x-1/2 border-[6px] border-transparent border-t-[#1C1C1E]"></div>
                        </div>
                        
                        <!-- Trigger Text -->
                        <span class="font-sans text-[0.9rem] font-bold text-[#1C1C1E] border-b-[1.5px] border-dotted border-[#BE7555]">Hover for Definition</span>
                    </div>
                </div>
                
            </div>
        </div>
        """, 'html.parser')
        
        feedback_block.replace_with(new_block)
            
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Replaced successfully.")

update()
