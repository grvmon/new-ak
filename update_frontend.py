from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    frontend_sec = soup.find(id='26-nextjs')
    if frontend_sec:
        frontend_sec.clear()
        
        new_comp = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">26. Next.js / Frontend Architecture</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">The acre&amp;key platform is built on Next.js and Tailwind CSS. We explicitly ban CSS-in-JS libraries, complex UI frameworks (MUI/Chakra), and overly abstracted component wrappers. We write bare-metal, native Tailwind.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- Frontend Matrix -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- Architecture -->
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Core Architecture</h3>
                    <div class="space-y-4 text-[0.85rem] text-[#55555A]">
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Tailwind CSS (Tokens)</strong>
                            Zero custom CSS files. Do not write <code class="bg-black/5 px-1 rounded-sm">.css</code> or <code class="bg-black/5 px-1 rounded-sm">.scss</code> modules. Every visual decision must route through the Tailwind config and utility classes.
                        </div>
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Atomic Components</strong>
                            Do not abstract basic HTML elements unnecessarily. If a component does not carry complex state or unique business logic (e.g., a simple card), build it natively with Tailwind rather than creating a bloated <code class="bg-black/5 px-1 rounded-sm">&lt;Card&gt;</code> wrapper.
                        </div>
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Next/Image</strong>
                            All properties and architectural shots must run through the native <code class="bg-black/5 px-1 rounded-sm">next/image</code> component for WebP optimization, strict lazy loading, and exact LCP priority tagging.
                        </div>
                    </div>
                </div>

                <!-- Performance & SEO -->
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-4">Performance &amp; SEO</h3>
                    <div class="space-y-4 text-[0.85rem] text-[#55555A]">
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Server Components (RSC)</strong>
                            Maximize React Server Components. Data fetching (e.g., RERA details, Yield Data) happens on the server. Reserve <code class="bg-black/5 px-1 rounded-sm">"use client"</code> exclusively for interactive elements (Modals, Forms, Maps).
                        </div>
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Next/Font</strong>
                            Load Marcellus, Manrope, and Josefin Sans strictly through <code class="bg-black/5 px-1 rounded-sm">next/font/google</code>. Zero external stylesheet requests to Google Fonts. This guarantees zero layout shift (CLS).
                        </div>
                        <div>
                            <strong class="text-[#1C1C1E] uppercase tracking-[0.1em] text-[0.7rem] block mb-1">Metadata API</strong>
                            Every single property page and micro-market analysis must dynamically generate its <code class="bg-black/5 px-1 rounded-sm">generateMetadata()</code> tags for perfect Twitter/OpenGraph rendering.
                        </div>
                    </div>
                </div>
            </div>

            <!-- File Structure Specimen -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Component Spec: Next.js App Router Structure</h3>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-8 max-w-3xl">We utilize the Next.js App Router paradigm. Directory structures must remain shallow and conceptually grouped around business domains (e.g., properties, advisory).</p>
                
                <div class="bg-[#1C1C1E] p-8 rounded-sm shadow-xl font-mono text-[0.8rem] leading-[1.6]">
                    <div class="text-[#55555A]">src/</div>
                    <div class="pl-4 text-[#BE7555] font-bold">app/</div>
                    <div class="pl-8 text-[#FAFAFA]">layout.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// Global fonts &amp; nav</span></div>
                    <div class="pl-8 text-[#FAFAFA]">page.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// Homepage</span></div>
                    <div class="pl-8 text-[#BE7555] font-bold">properties/</div>
                    <div class="pl-12 text-[#BE7555] font-bold">[slug]/</div>
                    <div class="pl-16 text-[#FAFAFA]">page.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// The Asset Dossier</span></div>
                    <div class="pl-16 text-[#FAFAFA]">loading.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// Shimmer UI, no spinners</span></div>
                    <div class="pl-4 text-[#BE7555] font-bold mt-2">components/</div>
                    <div class="pl-8 text-[#FAFAFA]">AdvisoryForm.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// 'use client' boundary</span></div>
                    <div class="pl-8 text-[#FAFAFA]">AssetCard.tsx <span class="text-[#55555A] text-[0.7rem] ml-2">// Pure RSC, Tailwind UI</span></div>
                    <div class="pl-4 text-[#BE7555] font-bold mt-2">lib/</div>
                    <div class="pl-8 text-[#FAFAFA]">utils.ts <span class="text-[#55555A] text-[0.7rem] ml-2">// clsx + tailwind-merge</span></div>
                </div>
            </div>

            <!-- Frontend Code Discipline -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <h3 class="font-serif text-[1.25rem] text-[#1C1C1E] mb-6">Frontend Discipline</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Responsive State Rules</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-3">
                            <li><strong class="text-[#1C1C1E]">Mobile-First:</strong> Write the baseline mobile Tailwind classes first, then apply <code class="bg-black/5 px-1 rounded-sm">md:</code> and <code class="bg-black/5 px-1 rounded-sm">lg:</code> mutations.</li>
                            <li><strong class="text-[#1C1C1E]">Information Parity:</strong> Never use <code class="bg-black/5 px-1 rounded-sm">hidden md:block</code> to hide data just to save space on mobile. Reformat the layout instead.</li>
                        </ul>
                    </div>
                    <div class="bg-white border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#1C1C1E] mb-4">Accessibility Encodings</div>
                        <ul class="text-[0.85rem] text-[#55555A] space-y-3">
                            <li><strong class="text-[#1C1C1E]">Focus-Visible:</strong> Bind focus rings securely using <code class="bg-black/5 px-1 rounded-sm">focus-visible:ring-2</code> to avoid mouse-click rings.</li>
                            <li><strong class="text-[#1C1C1E]">Next.js Route Announcements:</strong> Because Next.js uses client-side routing, handle route focus shifts explicitly for screen readers.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
                <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
                <div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Speed is an aesthetic. Every kilobyte of unnecessary JavaScript dilutes the premium nature of the brand. Keep it native, keep it server-rendered, keep it exceptionally fast.</div>
            </div>

        </div>
        """, 'html.parser')
        frontend_sec.append(new_comp)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
