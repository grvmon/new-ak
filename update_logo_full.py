from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    # We will inject the Google Font for Josefin Sans in the head if it's not there
    if 'Josefin Sans' not in html:
        # We can add it dynamically in the section or via a style tag just for safety.
        # But for now, we'll just add an inline style block to the section.
        pass

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    logo_sec = soup.find(id='03-logo')
    if logo_sec:
        logo_sec.clear()
        
        # We embed the font directly in the section to ensure it loads
        new_content = BeautifulSoup("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;700&display=swap');
            .font-josefin { font-family: 'Josefin Sans', sans-serif; }
        </style>
        
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">03. Logo &amp; Identity</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">The acre&key logo is a controlled typographic identity designed to communicate <strong>precision, restraint, and authority</strong>.</p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">It must remain consistent across digital, print, social, advertising, photography, and video.</p>
        <p class="font-sans text-[1rem] text-[#1C1C1E] font-bold max-w-3xl mb-12 leading-relaxed">The logo is never recreated or interpreted. It is a fixed brand asset.</p>
        
        <div class="space-y-16 font-sans">
            
            <!-- The Typographic Mark & Ampersand Rule -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- Logo Typeface -->
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">The Typographic Mark</div>
                    <div class="font-josefin text-5xl text-[#1C1C1E] tracking-tighter mb-8 border-b-[0.5px] border-[#55555a26] pb-8">acre&amp;key</div>
                    
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Logo Typeface</h3>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-4">The acre&key wordmark must always use Josefin Sans.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">No other typeface may be used to recreate, approximate, substitute, or modify the wordmark. This rule applies across Website, Social media, Advertising, Presentations, Print, Video, Signage, and Favicons.</p>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed mb-2">Brand typography and logo typography are separate systems.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">The logo remains locked to Josefin Sans, regardless of the typography used elsewhere in the brand system.</p>
                </div>

                <!-- Ampersand Rule -->
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">The Ampersand Rule</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-6">The <strong>&amp;</strong> is the structural hinge of the identity.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">It must:</p>
                    <ul class="text-[0.95rem] text-[#1C1C1E] space-y-2 mb-6">
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Remain in Josefin Sans</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Remain the same weight as the surrounding wordmark</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Remain the same color as the complete wordmark</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Never be independently colorized</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Never be bolded or italicized</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Never be enlarged or reduced independently</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Never be replaced with another style</li>
                    </ul>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">The ampersand is an integral part of the logo, not a separate graphic element.</p>
                </div>
            </div>

            <!-- Spatial Architecture & Color Architecture -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Spatial -->
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Spatial Architecture</div>
                    
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-2">Clear Space</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">The minimum clear space around the logo is defined by the height of the lowercase <strong>k</strong>. No typography, UI element, graphic, image detail, or other logo may enter this area. Maintain the defined clear space on all four sides. When in doubt, use more space rather than less.</p>
                    
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-2 mt-8">Minimum Size</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">The logo must remain legible at every application size.</p>
                    <ul class="text-[0.95rem] text-[#1C1C1E] space-y-2 mb-4">
                        <li><strong>Digital:</strong> 120px minimum width</li>
                        <li><strong>Print:</strong> 30mm minimum width</li>
                        <li><strong>Favicon / App Icon:</strong> Use the approved <strong>a&k monogram</strong></li>
                    </ul>
                    <p class="text-[0.95rem] text-[#8B3A3A] font-bold leading-relaxed">Do not reduce the full wordmark below these minimum sizes.</p>
                </div>

                <!-- Color -->
                <div class="bg-[#FAFAFA] p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Color Architecture</div>
                    <p class="text-[0.95rem] text-[#1C1C1E] leading-relaxed mb-6">The logo follows a <strong>monochrome logo architecture</strong>. The complete logo must always appear in <strong>one approved color</strong>.</p>
                    
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Approved Logo Colors</h3>
                    <div class="grid grid-cols-1 gap-4 mb-8">
                        <div class="flex items-center gap-4">
                            <span class="w-6 h-6 bg-[#1C1C1E] rounded-sm border-[0.5px] border-[#55555a26]"></span>
                            <div>
                                <div class="text-[0.85rem] font-bold text-[#1C1C1E]">Obsidian Black</div>
                                <div class="text-[0.75rem] text-[#55555A]">For light backgrounds.</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-4">
                            <span class="w-6 h-6 bg-[#FAFAFA] rounded-sm border-[0.5px] border-[#55555a26]"></span>
                            <div>
                                <div class="text-[0.85rem] font-bold text-[#1C1C1E]">Titanium Frost</div>
                                <div class="text-[0.75rem] text-[#55555A]">For dark backgrounds.</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-4">
                            <span class="w-6 h-6 bg-[#9F5334] rounded-sm border-[0.5px] border-[#55555a26]"></span>
                            <div>
                                <div class="text-[0.85rem] font-bold text-[#1C1C1E]">Primary Copper</div>
                                <div class="text-[0.75rem] text-[#55555A]">For approved accent applications.</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white border-[0.5px] border-[#8B3A3A] p-4 rounded-sm">
                        <div class="text-[0.85rem] text-[#8B3A3A] font-bold uppercase tracking-[0.1em] mb-1">Core Rule</div>
                        <div class="text-[1.1rem] text-[#1C1C1E] font-serif mb-2">One logo. One typeface. One color.</div>
                        <div class="text-[0.85rem] text-[#55555A]">Never create a multicolor logo. Copper must never be combined with another color within the logo.</div>
                    </div>
                </div>

            </div>

            <!-- Contextual Environments -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Approved Canvas Environments</div>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <!-- Light -->
                    <div class="h-[160px] bg-[#FAFAFA] border-[0.5px] border-[#55555a26] flex flex-col items-center justify-center relative rounded-sm">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-[#55555A]">Titanium Frost</div>
                        <div class="font-josefin text-3xl text-[#1C1C1E] tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Dark -->
                    <div class="h-[160px] bg-[#1C1C1E] flex flex-col items-center justify-center relative rounded-sm border-[0.5px] border-[#55555a26]">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/50">Obsidian Black</div>
                        <div class="font-josefin text-3xl text-[#FAFAFA] tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Copper -->
                    <div class="h-[160px] bg-[#9F5334] flex flex-col items-center justify-center relative rounded-sm border-[0.5px] border-[#55555a26]">
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/60">Primary Copper</div>
                        <div class="font-josefin text-3xl text-[#FAFAFA] tracking-tighter">acre&amp;key</div>
                    </div>
                    <!-- Image/Video -->
                    <div class="h-[160px] relative flex flex-col items-center justify-center rounded-sm overflow-hidden border-[0.5px] border-[#55555a26]">
                        <div class="absolute inset-0 bg-[#1C1C1E]"></div>
                        <div class="absolute inset-0 opacity-40 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80')] bg-cover bg-center grayscale contrast-[1.2]"></div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E]/80 to-transparent"></div>
                        <div class="absolute top-3 left-3 text-[0.65rem] uppercase tracking-[0.1em] text-white/80 z-10">Image / Video</div>
                        <div class="font-josefin text-3xl text-[#FAFAFA] tracking-tighter z-10">acre&amp;key</div>
                    </div>
                </div>
            </div>

            <!-- Incorrect Usage List -->
            <div class="border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#8B3A3A] mb-8">Incorrect Usage — Zero Tolerance</div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-12 gap-x-8">
                    
                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Change Typeface
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed"><strong>Josefin Sans is mandatory.</strong> Never recreate the logo using Marcellus, Cormorant, Inter, Helvetica, or any other typeface.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Colorize
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never apply multiple colors to individual letters or the ampersand.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Stretch
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never distort the logo horizontally or vertically.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Recreate
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never manually type or redraw the logo. Always use the approved master artwork.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Modify
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never alter letter spacing, proportions, weight, alignment, character shapes, ampersand, or baseline.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Add Effects
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never use gradients, drop shadows, glow, outlines, 3D effects, texture, or decorative treatments.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Place Over Complex Images
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never place the logo over a busy or low-contrast image.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Use Luxury Gold
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never introduce gold, metallic gold, champagne, or similar luxury-brand treatments.</p>
                    </div>

                    <div>
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2 flex items-center gap-2">
                            <span class="text-[#8B3A3A]">✕</span> Do Not Enclose or Rotate
                        </div>
                        <p class="text-[0.9rem] text-[#55555A] leading-relaxed">Never place the logo inside an unapproved badge, pill, box, or circle. The logo must always remain horizontally aligned.</p>
                    </div>

                </div>
            </div>

            <!-- Decision Rule -->
            <div class="bg-[#1C1C1E] text-white p-12 rounded-sm mt-12">
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Logo Decision Rule</div>
                <p class="text-[0.95rem] text-white/80 leading-relaxed mb-6">When there is uncertainty:</p>
                <div class="font-serif text-2xl leading-relaxed mb-8">Use the approved Josefin Sans master logo, in one approved color, with maximum legibility and sufficient clear space.</div>
                <p class="text-[0.95rem] text-[#804526] font-bold leading-relaxed">The logo should feel quiet, controlled, precise, and permanent — never decorative, fashionable, or promotional.</p>
            </div>

        </div>
        """, 'html.parser')
        logo_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
