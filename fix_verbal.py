from bs4 import BeautifulSoup

def update_verbal():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    verbal_sec = soup.find(id='02-verbal')
    if verbal_sec:
        verbal_sec.clear()
        new_content = BeautifulSoup("""
        <h2 class="font-serif text-2xl font-normal text-[#1C1C1E] mb-2">02. Verbal Identity</h2>
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">HNI buyers ignore marketing jargon. Our voice is that of a fiduciary, private-bank advisor: clinical, precise, and objective. Two different copywriters must sound like the exact same institutional entity.</p>
        
        <div class="space-y-16 font-sans">

            <!-- Voice & Tone -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Voice &amp; Tone</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="border-[0.5px] border-[#8B3A3A] bg-[#8B3A3A]/5 p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#8B3A3A] mb-4">BAD: Salesy &amp; Emotional</div>
                        <p class="text-[0.95rem] text-[#1C1C1E] italic mb-4">"Don't miss out on this breathtaking, ultra-luxury masterpiece in Whitefield! Perfect for your dream lifestyle!"</p>
                        <p class="text-[0.85rem] text-[#55555A]">Why it fails: Sounds like every generic broker in the city. Reeks of desperation.</p>
                    </div>
                    <div class="border-[0.5px] border-[#2C4C3B] bg-[#2C4C3B]/5 p-6 rounded-sm">
                        <div class="text-[0.75rem] font-bold tracking-[0.1em] uppercase text-[#2C4C3B] mb-4">GOOD: Clinical &amp; Objective</div>
                        <p class="text-[0.95rem] text-[#1C1C1E] italic mb-4">"A Grade-A asset in the Whitefield micro-market. Strong capital appreciation fundamentals supported by Phase 2 metro connectivity."</p>
                        <p class="text-[0.85rem] text-[#55555A]">Why it works: Objective, data-driven, and emotionally detached.</p>
                    </div>
                </div>
            </div>

            <!-- Formatting Rules -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">Mechanics: Numbers, Currency &amp; Capitalization</div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="border-[0.5px] border-[#55555a26] bg-white p-6 rounded-sm">
                        <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Currency &amp; Pricing</h4>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                            <li><strong class="text-[#1C1C1E] block">Rule:</strong> Always use the Indian Rupee symbol with spaces. Use 'Cr' and 'L' for abbreviations. Always include decimals for precision.</li>
                            <li><span class="text-[#8B3A3A] line-through">Bad: 3.1Cr, Rs 3.10 Cr, 3,10,00,000</span></li>
                            <li><span class="text-[#2C4C3B] font-bold">Good: ₹ 3.10 Cr</span></li>
                        </ul>
                    </div>
                    <div class="border-[0.5px] border-[#55555a26] bg-white p-6 rounded-sm">
                        <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Area &amp; Measurements</h4>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                            <li><strong class="text-[#1C1C1E] block">Rule:</strong> Use Title Case for abbreviations with periods. Always use commas for numbers over 999.</li>
                            <li><span class="text-[#8B3A3A] line-through">Bad: 3150 sqft, 3,150 Sqft</span></li>
                            <li><span class="text-[#2C4C3B] font-bold">Good: 3,150 Sq.Ft.</span></li>
                        </ul>
                    </div>
                    <div class="border-[0.5px] border-[#55555a26] bg-white p-6 rounded-sm">
                        <h4 class="font-serif text-[1.1rem] text-[#1C1C1E] mb-4">Headlines &amp; Body</h4>
                        <ul class="text-[0.9rem] text-[#55555A] space-y-4">
                            <li><strong class="text-[#1C1C1E] block">Rule:</strong> Headlines strictly use Sentence case. Never use exclamation marks.</li>
                            <li><span class="text-[#8B3A3A] line-through">Bad: Secure Your Asset Today!</span></li>
                            <li><span class="text-[#2C4C3B] font-bold">Good: Schedule a clinical analysis.</span></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Master Lexicon -->
            <div>
                <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-6">The Master Lexicon (Approved vs Banned)</div>
                <table class="w-full border-collapse bg-white">
                    <thead>
                        <tr>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Banned Marketing Fluff</th>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Approved Clinical Terminology</th>
                            <th class="text-left py-4 px-4 border-[0.5px] border-[#55555a26] bg-[#FAFAFA] text-[0.85rem] uppercase tracking-[0.12em] text-[#55555A]">Context / Usage</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="text-[#8B3A3A] line-through text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Buy Now" / "Submit"</td>
                            <td class="text-[#2C4C3B] font-bold text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Request Advisory Call"</td>
                            <td class="text-[#55555A] text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem]">CTA Language. We do not sell; we advise.</td>
                        </tr>
                        <tr>
                            <td class="text-[#8B3A3A] line-through text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Luxury" / "Premium"</td>
                            <td class="text-[#2C4C3B] font-bold text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Institutional-Grade" / "A-Grade"</td>
                            <td class="text-[#55555A] text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem]">Real estate descriptors. Luxury is cheap.</td>
                        </tr>
                        <tr>
                            <td class="text-[#8B3A3A] line-through text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Features" / "Amenities"</td>
                            <td class="text-[#2C4C3B] font-bold text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Asset Fundamentals"</td>
                            <td class="text-[#55555A] text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem]">Describing the physical property.</td>
                        </tr>
                        <tr>
                            <td class="text-[#8B3A3A] line-through text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Best" / "Perfect"</td>
                            <td class="text-[#2C4C3B] font-bold text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.95rem]">"Objective Evaluation"</td>
                            <td class="text-[#55555A] text-left py-4 px-4 border-[0.5px] border-[#55555a26] text-[0.9rem]">Avoid superlatives. Present data instead.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
        """, 'html.parser')
        verbal_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update_verbal()
