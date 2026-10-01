from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    motion_sec = soup.find(id='11-motion')
    if motion_sec:
        motion_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">11. Motion</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Motion should feel intentional, controlled, and almost invisible. We are an institutional advisory firm, not a startup. We do not entertain the user; we guide them.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Timing & Easing Matrix -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                
                <!-- Timing Rules -->
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm flex flex-col justify-center">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Timing &amp; Easing Tokens</h3>
                    
                    <div class="space-y-6 text-[0.85rem]">
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="font-bold text-[#1C1C1E]">Micro-Interactions</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">150ms - 200ms</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">ease-out</span>
                            </div>
                            <p class="text-[#55555A]">Fast and crisp. Used for hovers, focus rings, and active states.</p>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="font-bold text-[#1C1C1E]">Structural Entrances</span>
                                <span class="bg-[#2C4C3B]/10 text-[#2C4C3B] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">300ms - 400ms</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">ease-out</span>
                            </div>
                            <p class="text-[#55555A]">Controlled decelerated curves. Used for modals, navigation panels, and dropdowns.</p>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="font-bold text-[#1C1C1E]">Image Reveals &amp; Scroll</span>
                                <span class="bg-[#1C1C1E] text-white font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">600ms - 800ms</span>
                            </div>
                            <p class="text-[#55555A]">Slow, cinematic fade-ins. Absolutely no bouncing, springing, or scaling.</p>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="font-bold text-[#1C1C1E]">Exits</span>
                                <span class="bg-[#8B3A3A]/10 text-[#8B3A3A] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">150ms - 200ms</span>
                                <span class="bg-black/5 text-[#55555A] font-mono text-[0.7rem] px-1.5 py-0.5 rounded-sm">ease-in</span>
                            </div>
                            <p class="text-[#55555A]">Always faster than entrances to ensure the UI feels responsive.</p>
                        </div>
                    </div>
                </div>

                <!-- Banned Animations -->
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Banned Behaviors</h3>
                    <div class="space-y-4">
                        <div class="flex items-start gap-3 border-[0.5px] border-[#8B3A3A]/20 bg-white p-4 rounded-sm">
                            <span class="text-[#8B3A3A] font-bold mt-0.5">✕</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Elastic Bouncing</div>
                                <p class="text-[0.8rem] text-[#55555A]">Spring animations (`stiffness`, `damping`) make the UI feel like a toy. We use strict CSS easing curves.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 border-[0.5px] border-[#8B3A3A]/20 bg-white p-4 rounded-sm">
                            <span class="text-[#8B3A3A] font-bold mt-0.5">✕</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Card Hover Scaling</div>
                                <p class="text-[0.8rem] text-[#55555A]">Do not scale (`hover:scale-105`) the entire property card. It triggers layout recalculations and feels cheap. Scale the internal image only.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 border-[0.5px] border-[#8B3A3A]/20 bg-white p-4 rounded-sm">
                            <span class="text-[#8B3A3A] font-bold mt-0.5">✕</span>
                            <div>
                                <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">Staggered Text Reveals</div>
                                <p class="text-[0.8rem] text-[#55555A]">Do not animate text appearing word-by-word or letter-by-letter. The data must be immediately available to the reader.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Live Motion Specimens -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Interactive Reference Specimens</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">Hover over the components below to observe the precise easing curves and execution speeds mapped to the acre&amp;key design tokens.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    
                    <!-- Specimen 1: Micro-Interaction -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-6 group cursor-pointer flex flex-col justify-between h-[200px]">
                        <div>
                            <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">01. Micro-Interaction</div>
                            <div class="text-[0.75rem] font-mono text-[#55555A] mb-4">150ms • ease-out</div>
                        </div>
                        
                        <div class="flex justify-center">
                            <button class="bg-white text-[#1C1C1E] border-[1px] border-[#1C1C1E] px-6 py-3 rounded-sm font-sans text-[0.8rem] font-bold tracking-[0.1em] uppercase group-hover:bg-[#1C1C1E] group-hover:text-white transition-colors duration-150 ease-out w-full">
                                Hover Me
                            </button>
                        </div>
                    </div>

                    <!-- Specimen 2: Structural Entrance -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-6 group cursor-pointer flex flex-col h-[200px] overflow-hidden relative">
                        <div class="z-10 relative">
                            <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-1">02. Structural Reveal</div>
                            <div class="text-[0.75rem] font-mono text-[#55555A] mb-4">400ms • ease-out</div>
                        </div>
                        
                        <!-- Simulated Modal/Panel -->
                        <div class="absolute inset-x-6 bottom-0 translate-y-full opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-[400ms] ease-out bg-[#FAFAFA] border-[0.5px] border-[#55555a26] rounded-t-sm p-4 h-[100px] flex items-center justify-center">
                            <span class="text-[0.8rem] font-bold text-[#1C1C1E]">Menu Panel Revealed</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center pointer-events-none group-hover:opacity-0 transition-opacity duration-150">
                            <span class="text-[0.8rem] font-bold text-[#55555A] underline">Hover Container</span>
                        </div>
                    </div>

                    <!-- Specimen 3: Cinematic Image Reveal -->
                    <div class="bg-white border-[0.5px] border-[#55555a26] rounded-sm p-0 group cursor-pointer h-[200px] overflow-hidden relative">
                        <!-- Internal Text -->
                        <div class="absolute inset-0 p-6 z-10 pointer-events-none flex flex-col justify-between">
                            <div>
                                <div class="text-[0.65rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] group-hover:text-white transition-colors duration-[800ms] mb-1">03. Cinematic Image Reveal</div>
                                <div class="text-[0.75rem] font-mono text-[#55555A] group-hover:text-white/70 transition-colors duration-[800ms]">800ms • opacity only</div>
                            </div>
                            <div class="text-center font-bold text-[0.8rem] text-[#1C1C1E] group-hover:opacity-0 transition-opacity duration-300">
                                Hover Container
                            </div>
                        </div>
                        
                        <!-- Image that fades in -->
                        <div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_pool_evening.webp')] bg-cover bg-center opacity-0 group-hover:opacity-100 transition-opacity duration-[800ms] ease-out"></div>
                        <!-- Gradient Overlay -->
                        <div class="absolute inset-0 bg-gradient-to-b from-[#1C1C1E]/80 to-transparent h-[50%] opacity-0 group-hover:opacity-100 transition-opacity duration-[800ms] ease-out"></div>
                    </div>

                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">If an animation distracts the user from reading the data, it must be removed. Motion exists only to clarify state changes.</div>
            </div>

        </div>
        """, 'html.parser')
        motion_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
