from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # Update 10. Iconography
    icon_sec = soup.find(id='10-iconography')
    if icon_sec:
        icon_sec.clear()
        
        new_icon = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">10. Iconography</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Icons are functional wayfinding tools, not decoration. Every icon must look like it belongs to the same system—precise, architectural, and restrained.</p>
        
        <div class="space-y-16 font-sans">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Iconography Rules</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Stroke & Weight</strong> strictly <code class="bg-black/5 px-1 rounded-sm">1.5px</code> stroke width globally. Never mix solid and outline icons.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Grid & Size</strong> Built on a strict 24x24px grid. Standard usage is 16px, 20px, or 24px.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Corners</strong> Sharp or <code class="bg-black/5 px-1 rounded-sm">1px</code> micro-radius to match the sharp geometry of the typography. No bubbly edges.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Color & State</strong> 
                            <ul class="ml-4 mt-2 list-disc space-y-1">
                                <li>Default: <code class="bg-black/5 px-1 rounded-sm">#55555A</code> (Titanium context) or <code class="bg-white/10 px-1 rounded-sm text-white">#FAFAFA/70</code> (Obsidian context)</li>
                                <li>Hover/Active: Shift to pure <code class="bg-black/5 px-1 rounded-sm">#1C1C1E</code> or <code class="bg-[#BE7555]/10 px-1 rounded-sm text-[#BE7555]">#BE7555</code> for primary actions</li>
                                <li>Disabled: <code class="bg-black/5 px-1 rounded-sm">opacity-40</code></li>
                            </ul>
                        </li>
                    </ul>
                </div>
                
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-sm p-8 flex flex-col justify-center items-center">
                    <div class="grid grid-cols-4 gap-8">
                        <div class="flex flex-col items-center gap-2">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1C1C1E" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            <span class="text-[0.65rem] font-mono text-[#55555A]">MAP_PIN</span>
                        </div>
                        <div class="flex flex-col items-center gap-2">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1C1C1E" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter"><rect x="3" y="3" width="18" height="18" rx="0"></rect><path d="M3 9h18"></path><path d="M9 21V9"></path></svg>
                            <span class="text-[0.65rem] font-mono text-[#55555A]">LAYOUT</span>
                        </div>
                        <div class="flex flex-col items-center gap-2">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1C1C1E" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
                            <span class="text-[0.65rem] font-mono text-[#55555A]">ARROW_R</span>
                        </div>
                        <div class="flex flex-col items-center gap-2">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1C1C1E" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                            <span class="text-[0.65rem] font-mono text-[#55555A]">DOSSIER</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If an icon does not directly assist navigation or data comprehension, remove it.</div>
            </div>
            
        </div>
        """, 'html.parser')
        icon_sec.append(new_icon)
        
    # Update 11. Motion
    motion_sec = soup.find(id='11-motion')
    if motion_sec:
        motion_sec.clear()
        
        new_motion = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">11. Motion</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Motion should feel intentional, controlled, and almost invisible. We are an institutional advisory firm, not a startup. We do not entertain the user; we guide them.</p>
        
        <div class="space-y-16 font-sans">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Timing &amp; Easing</h3>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-4 mb-6">
                        <li><strong class="text-[#1C1C1E] block mb-1">Micro-Interactions (Hover, Focus)</strong> Fast and crisp. <code class="bg-black/5 px-1 rounded-sm">150ms-200ms</code>. Standard ease-out.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Structural Entrances (Modals, Navigation)</strong> Controlled. <code class="bg-black/5 px-1 rounded-sm">300ms-400ms</code>. Decelerated curve (ease-out).</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Image Reveals &amp; Scroll</strong> Slow, cinematic fade-ins. <code class="bg-black/5 px-1 rounded-sm">600ms-800ms</code>. No bouncing, springing, or scaling.</li>
                        <li><strong class="text-[#1C1C1E] block mb-1">Exits</strong> Always faster than entrances. <code class="bg-black/5 px-1 rounded-sm">150ms-200ms</code>. Ease-in.</li>
                    </ul>
                </div>
                
                <div class="bg-white border-[0.5px] border-[#55555a26] p-8 rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Prohibited Motion</h3>
                    <div class="space-y-3">
                        <div class="flex items-start gap-3"><span class="text-[#8B3A3A] font-bold mt-0.5">✕</span> <span class="text-[0.85rem] text-[#55555A]">Spring animations or bouncing effects.</span></div>
                        <div class="flex items-start gap-3"><span class="text-[#8B3A3A] font-bold mt-0.5">✕</span> <span class="text-[0.85rem] text-[#55555A]">Parallax scrolling that induces nausea.</span></div>
                        <div class="flex items-start gap-3"><span class="text-[#8B3A3A] font-bold mt-0.5">✕</span> <span class="text-[0.85rem] text-[#55555A]">Hover-scaling (images or cards that zoom in significantly when hovered).</span></div>
                        <div class="flex items-start gap-3"><span class="text-[#8B3A3A] font-bold mt-0.5">✕</span> <span class="text-[0.85rem] text-[#55555A]">Complex SVG line-drawing animations.</span></div>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If the user notices the animation before the content, the animation has failed.</div>
            </div>
            
        </div>
        """, 'html.parser')
        motion_sec.append(new_motion)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
