from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # Find the H3 containing 'Navigation & Menu States'
    nav_h3 = soup.find(lambda tag: tag.name == 'h3' and 'Navigation & Menu States' in tag.get_text())
    
    if nav_h3:
        # The structure is: <h3> -> <p> -> <div> (containing the 2 menus) -> closing </div>
        parent_div = nav_h3.parent
        
        # We will clear this parent div and reconstruct it
        parent_div.clear()
        
        new_content = BeautifulSoup("""
        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-12 mb-4">Global Navigation (Light &amp; Dark)</h3>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The global header must feel like an editorial index. It relies on crisp Manrope typography, generous spacing, the Josefin Sans wordmark, and a clinical Copper CTA. No bulky background hovers.</p>
        
        <div class="space-y-12">
            
            <!-- Light Menu -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Titanium Frost (Light) Navigation</div>
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-sm flex items-center justify-between px-8 py-4">
                    
                    <!-- Logo -->
                    <div class="font-josefin text-2xl text-[#1C1C1E] tracking-tighter cursor-pointer">
                        acre&amp;key
                    </div>

                    <!-- Links -->
                    <nav class="hidden md:flex items-center gap-8 font-sans text-[0.85rem] font-semibold text-[#55555A]">
                        <a href="#" class="text-[#1C1C1E] transition-colors">Advisory</a>
                        <a href="#" class="hover:text-[#1C1C1E] transition-colors">Dossiers</a>
                        <a href="#" class="hover:text-[#1C1C1E] transition-colors">Framework</a>
                        <a href="#" class="hover:text-[#1C1C1E] transition-colors">About Us</a>
                    </nav>

                    <!-- CTA -->
                    <div class="flex items-center gap-6">
                        <a href="#" class="hidden lg:block font-sans text-[0.8rem] font-bold uppercase tracking-[0.1em] text-[#1C1C1E] hover:text-[#804526] transition-colors">Sign In</a>
                        <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-5 py-2.5 rounded-sm font-sans text-[0.8rem] font-semibold transition-colors">
                            Request consultation
                        </button>
                    </div>
                </div>
            </div>

            <!-- Dark Menu -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Obsidian Black (Dark) Navigation</div>
                <div class="bg-[#1C1C1E] border-[0.5px] border-[#55555a26] rounded-sm flex items-center justify-between px-8 py-4">
                    
                    <!-- Logo -->
                    <div class="font-josefin text-2xl text-[#FAFAFA] tracking-tighter cursor-pointer">
                        acre&amp;key
                    </div>

                    <!-- Links -->
                    <nav class="hidden md:flex items-center gap-8 font-sans text-[0.85rem] font-semibold text-[#FAFAFA]/70">
                        <a href="#" class="text-[#FAFAFA] transition-colors">Advisory</a>
                        <a href="#" class="hover:text-[#FAFAFA] transition-colors">Dossiers</a>
                        <a href="#" class="hover:text-[#FAFAFA] transition-colors">Framework</a>
                        <a href="#" class="hover:text-[#FAFAFA] transition-colors">About Us</a>
                    </nav>

                    <!-- CTA -->
                    <div class="flex items-center gap-6">
                        <a href="#" class="hidden lg:block font-sans text-[0.8rem] font-bold uppercase tracking-[0.1em] text-[#FAFAFA]/90 hover:text-[#BE7555] transition-colors">Sign In</a>
                        <button class="bg-[#BE7555] hover:bg-[#9F5334] text-white px-5 py-2.5 rounded-sm font-sans text-[0.8rem] font-semibold transition-colors">
                            Request consultation
                        </button>
                    </div>
                </div>
            </div>

        </div>
        """, 'html.parser')
        parent_div.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
