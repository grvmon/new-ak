from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    # FIX 1: Dossier Terminology
    body = body.replace('14. Property Design System', '14. Digital Property Pages')
    body = body.replace('21. Reports & Dossiers', '21. Print & PDF Intelligence Reports')

    # FIX 2: Focus States in Forms
    # The previous rule was: "Focus State Inputs do not glow blue. Focus relies on a strict 1.5px Obsidian (#1C1C1E) border."
    # Change to: "Focus State Inputs do not glow blue. Focus relies on the global 2px Obsidian outline offset (ring-2 ring-offset-2)."
    body = body.replace(
        'Focus relies on a strict 1.5px Obsidian (#1C1C1E) border.',
        'Focus relies on the global 2px Obsidian outline offset (focus-visible:ring-2 focus-visible:ring-offset-2).'
    )

    # FIX 3: Geometry Axioms
    # In section 13 Forms: "Architecture 0.5px borders. 4px radius. Generous 48px height minimum."
    # Change to: "Architecture Inherits the global 0.5px borders and 4px micro-edge radius. Generous 48px height minimum."
    body = body.replace(
        '<strong class="text-[#1C1C1E] block mb-1">Architecture</strong> <code class="bg-black/5 px-1 rounded-sm text-[#804526]">0.5px</code> borders. <code class="bg-black/5 px-1 rounded-sm">4px</code> radius.',
        '<strong class="text-[#1C1C1E] block mb-1">Architecture</strong> Inherits global <code class="bg-black/5 px-1 rounded-sm text-[#804526]">0.5px</code> borders and <code class="bg-black/5 px-1 rounded-sm">4px</code> radius.'
    )
    
    # In Section 11 Motion: "Strictly 4px border radiuses and 0.5px hairlines. All movement runs on Acre&Key Motion Physics..."
    # We already have it there. We will add a Master Geometry Axiom to Section 12.
    soup = BeautifulSoup(body, 'html.parser')
    
    sec_12 = soup.find(id='12-components')
    if sec_12:
        # Find "Master Component Inventory"
        master_heading = sec_12.find(string=re.compile("Master Component Inventory"))
        if master_heading:
            axiom_block = BeautifulSoup("""
            <div class="bg-[#1C1C1E] p-8 rounded-sm mb-12 border-[0.5px] border-[#55555a26]">
                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-2">Master Geometry Axiom</div>
                <p class="text-[0.9rem] text-[#FAFAFA]/90 leading-relaxed font-sans">Every component in the system is strictly bound to a <strong class="text-white">4px border radius</strong> and <strong class="text-white">0.5px hairlines</strong>. Pill shapes and thick borders are permanently banned. This rule overrides any local component styles.</p>
            </div>
            """, 'html.parser')
            master_heading.parent.parent.insert_before(axiom_block)

    # FIX 4: Design Tokens (Section 25)
    sec_25 = soup.find(id='25-dev-tokens')
    if sec_25:
        sec_25.clear()
        sec_25.append(BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">25. Developer Design Tokens</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">No abstracted CSS classes (e.g. <code class="bg-black/5 px-1 rounded-sm">bg-obsidian</code>). Developers must use native Tailwind hex codes directly inline to maintain parity with Section 04 (Color).</p>
        
        <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-[4px] shadow-sm">
            <h3 class="font-bold text-[0.85rem] tracking-[0.1em] uppercase text-[#1C1C1E] mb-6">Approved Raw Tokens</h3>
            <ul class="text-[0.85rem] text-[#55555A] space-y-4 font-mono">
                <li><code class="bg-black/5 px-2 py-1 rounded-sm text-[#1C1C1E]">bg-[#1C1C1E]</code> / <code class="bg-black/5 px-2 py-1 rounded-sm text-[#1C1C1E]">text-[#1C1C1E]</code> (Obsidian Black)</li>
                <li><code class="bg-black/5 px-2 py-1 rounded-sm text-[#55555A]">bg-[#FAFAFA]</code> / <code class="bg-black/5 px-2 py-1 rounded-sm text-[#55555A]">text-[#FAFAFA]</code> (Titanium Frost)</li>
                <li><code class="bg-black/5 px-2 py-1 rounded-sm text-[#BE7555]">bg-[#BE7555]</code> / <code class="bg-black/5 px-2 py-1 rounded-sm text-[#BE7555]">text-[#BE7555]</code> (Copper Emphasis)</li>
                <li><code class="bg-black/5 px-2 py-1 rounded-sm text-[#55555A]">text-[#55555A]</code> (Muted Neutral Text)</li>
            </ul>
        </div>
        """, 'html.parser'))
        
    # Re-serialize
    body = str(soup)

    # FIX 5: Information Parity (Section 26)
    # Remove the duplicate explanation, leave just technical.
    body = body.replace(
        '<strong class="text-[#1C1C1E]">Information Parity:</strong> Never use <code class="bg-black/5 px-1 rounded-sm">hidden md:block</code> to hide data just to save space on mobile. Reformat the layout instead.',
        '<strong class="text-[#1C1C1E]">Information Parity:</strong> Never use <code class="bg-black/5 px-1 rounded-sm">hidden md:block</code>. Refer to Section 07 for strict responsive data parity rules.'
    )

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{body}")
    print("QC fixes applied.")

update()
