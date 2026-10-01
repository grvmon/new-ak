from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # 19. Video Identity
    sec_19 = soup.find(id='19-video')
    if sec_19:
        sec_19.clear()
        sec_19.append(BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">19. Video Identity</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Video must feel like an institutional documentary, not a real estate vlog. We prioritize slow, deliberate pacing and architectural precision over manufactured excitement.</p>
        
        <div class="space-y-12">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-[4px]">
                    <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">The Pace &amp; Framing</div>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-3">
                        <li><strong class="text-[#1C1C1E]">Cinematic Gravity:</strong> Slow, deliberate pans and drone reveals. No rapid-fire jump cuts.</li>
                        <li><strong class="text-[#1C1C1E]">Talking Heads:</strong> Off-center interview framing (Rule of Thirds) with deep depth-of-field.</li>
                        <li><strong class="text-[#1C1C1E]">Transitions:</strong> Hard cuts or 0.6s cross-fades only. Banned: light leaks, glitch effects, or wipes.</li>
                    </ul>
                </div>
                <div class="bg-[#1C1C1E] border-[0.5px] border-[#55555a26] p-8 rounded-[4px]">
                    <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#BE7555] mb-4">Typography &amp; Audio</div>
                    <ul class="text-[0.85rem] text-[#FAFAFA]/80 space-y-3">
                        <li><strong class="text-white">Title Cards:</strong> Solid Obsidian backgrounds with Marcellus typography. No text over chaotic video.</li>
                        <li><strong class="text-white">Lower Thirds:</strong> Strict 0.5px white hairlines anchoring Manrope text.</li>
                        <li><strong class="text-white">Score:</strong> Minimalist, tension-driven ambient or neo-classical strings. No generic corporate ukulele tracks.</li>
                    </ul>
                </div>
            </div>
        </div>
        """, 'html.parser'))

    # 20. Editorial System
    sec_20 = soup.find(id='20-editorial')
    if sec_20:
        sec_20.clear()
        sec_20.append(BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">20. Editorial System</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The editorial system governs macro-market reports and long-form analysis. It is designed for focused reading and cognitive retention.</p>
        
        <div class="bg-white border-[0.5px] border-[#55555a26] p-12 rounded-[4px] shadow-sm">
            <h3 class="font-serif text-[2.5rem] text-[#1C1C1E] mb-4 leading-tight max-w-2xl">The Micro-Market Dynamics of Whitefield</h3>
            <div class="flex items-center gap-4 border-b-[0.5px] border-[#55555a26] pb-6 mb-8">
                <span class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#BE7555]">Market Analysis</span>
                <span class="text-[#55555a26]">|</span>
                <span class="text-[0.75rem] font-sans text-[#55555A]">October 2026</span>
            </div>
            
            <div class="max-w-[65ch] space-y-6">
                <p class="font-sans text-[1.05rem] text-[#1C1C1E] leading-relaxed">
                    <span class="float-left text-[3.5rem] font-serif leading-[0.8] mr-4 text-[#BE7555] mt-2">W</span>
                    e measure infrastructural velocity against absorption rates to determine true asset value. Reading lengths are strictly restricted to 65 characters per line to prevent eye fatigue.
                </p>
                <p class="font-sans text-[1.05rem] text-[#55555A] leading-relaxed">
                    Paragraphs remain dense and authoritative. Pull quotes are extracted using sharp 2px Obsidian left-borders to anchor the reader's attention to critical data points without disrupting the visual flow.
                </p>
                
                <blockquote class="border-l-[2px] border-[#1C1C1E] pl-6 my-10 py-2">
                    <p class="font-serif italic text-[1.35rem] text-[#1C1C1E] leading-relaxed">
                        "Capital follows infrastructure, but yield follows execution. Analyzing the gap between the two is where alpha is generated."
                    </p>
                </blockquote>
            </div>
        </div>
        """, 'html.parser'))
        
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")
    print("Injected 19 and 20 successfully.")

update()
