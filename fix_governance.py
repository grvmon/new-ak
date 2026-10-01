from bs4 import BeautifulSoup

def update_governance():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    gov_sec = soup.find(id='00-governance')
    if gov_sec:
        gov_sec.clear()
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">00. Governance</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Anyone working on acre&key must strictly adhere to this governance model. This ensures our institutional-grade architecture is never compromised by unauthorized design or code deviations.</p>
        
        <div class="mb-12 border-[0.5px] border-[#55555a26] bg-white p-6 rounded-sm font-sans">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Version</div>
                    <div class="text-[0.95rem] text-[#1C1C1E]">2.0.0 (Apple-Grade Architectural Release)</div>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Owner</div>
                    <div class="text-[0.95rem] text-[#1C1C1E]">Acre&amp;Key Design Authority</div>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Source of Truth</div>
                    <div class="text-[0.95rem] text-[#1C1C1E]">This live <code class="bg-[#1C1C1E]/5 px-1 py-0.5 rounded-sm">styleguide.astro</code> document supersedes any Figma file.</div>
                </div>
            </div>
            <div class="mt-8 pt-6 border-t-[0.5px] border-[#55555a26]">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Changelog</div>
                <div class="text-[0.95rem] text-[#55555A] leading-relaxed">Pivot from Warm Ivory to Titanium Frost, shift from Cormorant to Marcellus, implementation of strict 7.0:1 AAA contrast and 4px micro-edge geometry.</div>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 font-sans">
            <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Token Ownership</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Design tokens (Colors, Typography, Spacing) are owned strictly by the Design Authority. Developers must reference tokens natively via Tailwind utilities or from <code class="bg-[#1C1C1E]/5 px-2 py-1 rounded-sm text-[#804526]">global.css</code>. Never hardcode HEX values.</p>
            </div>
            
            <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Contribution Rules</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed">No new components may be added to fill space. If a unique UX pattern is required, an issue must be filed documenting why existing components fail to solve the user need.</p>
            </div>

            <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Approval Process</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed">All PRs affecting global CSS, base components, or design tokens require a mandatory code-review approval from the Design Authority before merging to `main`.</p>
            </div>

            <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Deprecation Process</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Components slated for deprecation remain in the system for 1 major release cycle. They must be tagged with a <span class="bg-[#804526]/10 text-[#804526] px-2 py-1 rounded-sm text-[0.7rem] font-bold uppercase tracking-[0.05em]">Deprecated</span> badge.</p>
            </div>
        </div>
        """, 'html.parser')
        gov_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update_governance()
