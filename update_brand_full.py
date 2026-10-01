from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    brand_sec = soup.find(id='01-brand')
    if brand_sec:
        brand_sec.clear()
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">01. Brand Foundation</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-4 leading-relaxed">The foundational DNA of acre&amp;key.</p>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Anyone working on the brand should understand these principles before creating any design, copy, interface, or campaign.</p>
        
        <div class="space-y-12 font-sans">
            
            <!-- Central Idea -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">The Central Brand Idea</div>
                <div class="font-serif text-4xl md:text-5xl font-normal tracking-[-0.02em] text-[#1C1C1E] leading-tight mb-4">
                    Find. Check. Inspect.<br/>Negotiate. Decide.
                </div>
                <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Every acre&amp;key experience should help a buyer move from uncertainty to a well-informed decision.</p>
            </div>

            <!-- Positioning & Promise -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Positioning</div>
                    <div class="text-[1.1rem] font-serif text-[#1C1C1E] mb-4">acre&amp;key is an independent home-buying concierge.</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">We help buyers find, evaluate, inspect, and negotiate residential property with an independent, buyer-first perspective.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">We bring <strong>clarity, diligence, and disciplined decision-making</strong> to one of the largest purchases a person can make.</p>
                </div>
                <div class="bg-white p-8 border-[0.5px] border-[#55555a26] rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Brand Promise</div>
                    <div class="text-[1.1rem] font-serif text-[#1C1C1E] mb-4">We help you buy with clarity and confidence.</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">acre&amp;key gives buyers an independent perspective, rigorous evaluation, and expert negotiation support &mdash; so they can make a better-informed decision before committing their capital.</p>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed">We don't sell you a home. We help you decide on one.</p>
                </div>
            </div>

            <!-- Audience & Core Principles -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Audience -->
                <div class="md:col-span-1">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Audience</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-6">Sophisticated home buyers in Bengaluru, including HNI and premium-segment buyers, who value:</p>
                    <ul class="text-[0.95rem] text-[#1C1C1E] space-y-2 mb-6">
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Time</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Privacy</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Data</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Independent thinking</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Rigorous evaluation</li>
                        <li class="flex items-center gap-3"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span> Efficient decision-making</li>
                    </ul>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">They do not need more properties pushed at them.</p>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed">They need better information, better evaluation, and better decision-making before committing capital.</p>
                </div>

                <!-- Principles -->
                <div class="md:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Data Over Emotion</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">Separate the property from the pitch.</p>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Prioritize verifiable facts, financial implications, location fundamentals, construction quality, documentation, and long-term considerations over promotional claims.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Buyer-First Independence</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">Built around the buyer's interests and decision-making process.</p>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">We are not a builder, and our communication should never feel like inventory-led selling.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Rigorous Diligence</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">Look beyond the brochure.</p>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Evaluate the property, location, documentation, infrastructure, pricing, construction, and relevant risks before the buyer commits.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Clarity Over Complexity</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">The buyer should never need to decode the process.</p>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Complex information should be researched, structured, and presented clearly so the buyer can make the decision.</p>
                    </div>
                    <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm md:col-span-2">
                        <div class="font-serif text-[#1C1C1E] text-[1.1rem] mb-2">Precision Over Persuasion</div>
                        <p class="text-[0.85rem] text-[#1C1C1E] font-bold mb-2">acre&amp;key does not need to convince the buyer to buy.</p>
                        <p class="text-[0.85rem] text-[#55555A] leading-relaxed">Our role is to provide the information, analysis, and negotiation support required for the buyer to decide.</p>
                    </div>
                </div>
            </div>

            <!-- Feel Check & Brand Test -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                <div class="md:col-span-1 space-y-8">
                    <div>
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">The Brand Should Feel</div>
                        <div class="grid grid-cols-2 gap-y-2 text-[0.9rem] text-[#1C1C1E]">
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Institutional</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Editorial</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Architectural</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Intelligent</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Calm</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Precise</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Independent</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>High-trust</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Data-informed</div>
                            <div class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-[#804526] rounded-sm"></span>Understated</div>
                        </div>
                    </div>
                    <div>
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#55555A] mb-4">It Must NEVER Feel</div>
                        <div class="grid grid-cols-1 gap-y-2 text-[0.9rem] text-[#55555A] opacity-80">
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Like a property portal</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Like a builder website</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Like a conventional real-estate broker</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Like a generic luxury brand</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Flashy, gold-heavy, or status-driven</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Like a SaaS or fintech dashboard</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Over-designed</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Sales-driven or Promotional</div>
                            <div class="flex items-center gap-2 line-through"><span class="w-1 h-1 bg-[#55555A] rounded-full"></span>Cheap or templated</div>
                        </div>
                    </div>
                </div>
                
                <div class="md:col-span-2">
                    <div class="bg-[#1C1C1E] text-white p-12 rounded-sm h-full flex flex-col justify-center">
                        <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">The Brand Test</div>
                        <p class="text-[0.95rem] text-white/80 leading-relaxed mb-6">Before approving any design, copy, interaction, or campaign, ask:</p>
                        <div class="font-serif text-2xl leading-relaxed mb-8">"Does this make acre&amp;key feel more independent, intelligent, precise, and trustworthy?"</div>
                        <p class="text-[0.95rem] text-[#804526] font-bold leading-relaxed">If it makes the brand feel promotional, decorative, generic, or sales-led, reconsider it.</p>
                    </div>
                </div>
            </div>

        </div>
        """, 'html.parser')
        brand_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
