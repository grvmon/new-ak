from bs4 import BeautifulSoup

def fix_styleguide():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    # Split frontmatter
    parts = html.split('---')
    frontmatter = parts[1]
    body = parts[2]

    soup = BeautifulSoup(body, 'html.parser')

    # 1. Fix Governance
    gov = soup.find('h2', string=lambda text: text and '0. Governance' in text).parent
    # Inject new rules
    new_gov = BeautifulSoup("""
    <div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-8 font-sans">
        <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
            <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Token Ownership</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Design tokens (Colors, Typography, Spacing) are owned strictly by the Design Authority. Developers must reference tokens from <code class="bg-[#1C1C1E]/5 px-2 py-1 rounded-sm text-[#804526]">global.css</code> and never hardcode HEX values.</p>
        </div>
        <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
            <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Deprecation Process</h3>
            <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Components slated for deprecation remain in the system for 1 major release cycle. They will be marked with a <span class="bg-[#804526]/10 text-[#804526] px-2 py-1 rounded-sm text-[0.7rem] font-bold uppercase tracking-[0.05em]">Deprecated</span> badge.</p>
        </div>
    </div>
    """, 'html.parser')
    gov.append(new_gov)

    # 2. Fix Foundations
    brand = soup.find('h2', string=lambda text: text and '1. Master Foundations' in text).parent
    brand.find('h2').string = '01. Brand Foundation (P0)'
    brand_content = BeautifulSoup("""
    <div class="mb-16">
        <h3 class="font-serif text-3xl md:text-5xl font-normal mb-6 tracking-[-0.02em] text-[#1C1C1E]">Find. Check. Inspect. Negotiate. Decide.</h3>
        <p class="font-sans text-[1.15rem] text-[#55555A] max-w-3xl leading-relaxed mb-8">acre&key is an independent home-buying concierge for sophisticated/HNI home buyers in Bengaluru. The buyer should feel that acre&key brings clarity, diligence and independent thinking to a major purchase decision.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 mt-12 pt-12 border-t-[0.5px] border-[#55555a26]">
            <div>
                <div class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#804526] mb-4">The Brand Should Feel</div>
                <ul class="font-sans text-[0.95rem] text-[#1C1C1E] space-y-3">
                    <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Institutional & Editorial</li>
                    <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Architectural & Intelligent</li>
                    <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Calm & Precise</li>
                    <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Independent & Understated</li>
                    <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> High-trust & Data-driven</li>
                </ul>
            </div>
            <div>
                <div class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#55555A] mb-4">It Must NOT Feel</div>
                <ul class="font-sans text-[0.95rem] text-[#55555A] space-y-3 opacity-80">
                    <li class="flex items-center gap-3 line-through">Like a property portal</li>
                    <li class="flex items-center gap-3 line-through">Like a builder website</li>
                    <li class="flex items-center gap-3 line-through">Like a real-estate broker</li>
                    <li class="flex items-center gap-3 line-through">Like a generic luxury brand</li>
                    <li class="flex items-center gap-3 line-through">Flashy or Salesy</li>
                </ul>
            </div>
        </div>
    </div>
    """, 'html.parser')
    brand.insert(2, brand_content)

    # 3. Typography Scale
    type_sec = soup.find('h2', string=lambda text: text and '5. Typography Hierarchy' in text).parent
    type_scale = BeautifulSoup("""
    <div class="mt-16 w-full text-left border-collapse font-sans mb-12">
        <h3 class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#804526] mb-4 border-b-[0.5px] border-[#55555a26] pb-4">Comprehensive Type Scale</h3>
        <table class="w-full">
            <thead>
                <tr>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Token</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Family</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Weight & Size (Fluid)</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Usage</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold">H1 Display</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Marcellus</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">400 / clamp(2rem, 1.5rem + 2.5vw, 3.5rem)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Hero headlines</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold">H2 Section</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Marcellus</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">400 / clamp(1.5rem, 1.25rem + 1vw, 2rem)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Major dividers</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold">Lead Paragraph</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Manrope</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">400 / 1.1rem (1.7 LH)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Hero intros, mission statements</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold">Base Body</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Manrope</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">400 / 0.95rem (1.6 LH)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Standard readable text</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E] font-bold">Overline Kicker</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Manrope</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">700 / 0.75rem (0.15em space)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Section micro-labels</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, 'html.parser')
    type_sec.append(type_scale)

    # 4. Grid & Layout - Add Explicit Math
    layout = soup.find('h2', string=lambda text: text and 'Layout & Spacing' in text).parent
    grid_math = BeautifulSoup("""
    <div class="mt-16 w-full text-left border-collapse font-sans mb-12">
        <h3 class="font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#804526] mb-4 border-b-[0.5px] border-[#55555a26] pb-4">Grid Architecture</h3>
        <table class="w-full">
            <thead>
                <tr>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Breakpoint</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Container Width</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Columns</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Gutter</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Margins</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Desktop (≥1024px)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">1280px</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">12</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">24px</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">48px (px-12)</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Tablet (≥768px)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">100%</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">8</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">24px</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">32px (px-8)</td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Mobile (<768px)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">100%</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">4</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">16px</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">24px (px-6)</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, 'html.parser')
    layout.append(grid_math)

    # Convert soup back to string and write
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

fix_styleguide()
