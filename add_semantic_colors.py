from bs4 import BeautifulSoup

def add_semantic_colors():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')

    color_sec = soup.find(id='04-color')
    if color_sec:
        semantic_html = BeautifulSoup("""
        <h3 class="font-serif text-[1.25rem] font-bold text-[#1C1C1E] mt-16 mb-4">Architectural Semantic Palette</h3>
        <p class="font-sans text-[0.95rem] text-[#55555A] mb-8 leading-relaxed">Standard web-safe Red/Green/Yellow destroys our editorial vibe. We use muted, architectural equivalents for UI states (Success, Error, Warning) to maintain a calm, high-end feel.</p>
        
        <table class="w-full mt-8 border-collapse">
            <thead>
                <tr>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Role</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Token Name</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Hex</th>
                    <th class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Preview</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Success (Verified/Approved)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]"><code>--pine-success</code></td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">#2C4C3B</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26]">
                        <div class="flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-[#2C4C3B]"></span>
                            <span class="text-[0.75rem] font-bold text-[#2C4C3B] uppercase tracking-[0.1em]">Desaturated Pine</span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Error (Risk/Rejected)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]"><code>--terracotta-error</code></td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">#8B3A3A</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26]">
                        <div class="flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-[#8B3A3A]"></span>
                            <span class="text-[0.75rem] font-bold text-[#8B3A3A] uppercase tracking-[0.1em]">Deep Terracotta</span>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">Warning (Caution/Pending)</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]"><code>--brass-warning</code></td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26] text-[0.95rem] text-[#1C1C1E]">#A88944</td>
                    <td class="text-left py-4 px-4 border-b-[0.5px] border-[#55555a26]">
                        <div class="flex items-center gap-3">
                            <span class="w-6 h-6 rounded-sm bg-[#A88944]"></span>
                            <span class="text-[0.75rem] font-bold text-[#A88944] uppercase tracking-[0.1em]">Muted Brass</span>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
        """, 'html.parser')
        color_sec.append(semantic_html)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

add_semantic_colors()
