from bs4 import BeautifulSoup

def update():
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
        <p class="font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed">Anyone contributing to acre&amp;key must follow this governance model. It protects consistency across design, content, and implementation and ensures that the design system remains a controlled source of truth.</p>
        
        <div class="space-y-12 font-sans">
            <!-- Top Grid: Fast Facts -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 p-6 bg-white border-[0.5px] border-[#55555a26] rounded-sm">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Version</div>
                    <div class="text-[0.95rem] text-[#1C1C1E] font-serif">2.0.0 &mdash; Titanium Frost System</div>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">Owner</div>
                    <div class="text-[0.95rem] text-[#1C1C1E]">Acre&amp;Key Design Authority</div>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-2">The Non-Negotiable Principle</div>
                    <div class="text-[0.95rem] text-[#1C1C1E] font-bold">Consistency over invention.</div>
                </div>
            </div>

            <!-- Source of Truth & Changelog -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Source of Truth</div>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">The live <code class="bg-[#1C1C1E]/5 px-1 py-0.5 rounded-sm">styleguide.astro</code> implementation is the primary source of truth for the design system.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">Figma files, design explorations, screenshots, and other reference materials <strong>do not override</strong> the live system.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Any intentional deviation must be documented and approved.</p>
                </div>
                <div class="bg-[#FAFAFA] border-[0.5px] border-[#55555a26] p-6 rounded-sm">
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Changelog (2.0.0)</div>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-2 list-disc list-inside">
                        <li>Shifted visual foundation from Warm Ivory to Titanium Frost</li>
                        <li>Replaced Cormorant with Marcellus</li>
                        <li>Introduced defined accessibility contrast requirements</li>
                        <li>Standardized 4px micro-edge geometry</li>
                        <li>Consolidated design tokens and foundational components</li>
                    </ul>
                </div>
            </div>

            <!-- Core Rules Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
                
                <!-- Token Ownership -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Token Ownership</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">Design tokens &mdash; including color, typography, spacing, sizing, radius, borders, shadows, and motion &mdash; are owned by the Design Authority.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">Developers must consume tokens through the approved Tailwind utilities or <code class="bg-[#1C1C1E]/5 px-1 py-0.5 rounded-sm">global.css</code>.</p>
                    <p class="text-[0.95rem] text-[#8B3A3A] font-bold leading-relaxed mb-4">Do not hardcode design-token HEX values, spacing values, typography values, or other system primitives in components.</p>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">If a required token does not exist, propose a new token rather than creating a one-off value.</p>
                </div>

                <!-- Component Governance -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Component Governance</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">Before creating a new component:</p>
                    <ol class="text-[0.9rem] text-[#55555A] space-y-2 list-decimal list-inside mb-6">
                        <li>Check whether an existing component can solve the requirement.</li>
                        <li>Extend the existing component where appropriate.</li>
                        <li>Create a new component only when the existing system cannot reasonably support the use case.</li>
                        <li>Document the reason for introducing the new component.</li>
                    </ol>
                    <p class="text-[0.95rem] text-[#1C1C1E] font-bold leading-relaxed">The goal is to maintain a small, coherent, reusable component system rather than accumulate one-off UI patterns.</p>
                </div>

                <!-- Approval Process -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Approval Process</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">Changes affecting any of the following require Design Authority review before merging into `main`:</p>
                    <ul class="text-[0.9rem] text-[#55555A] grid grid-cols-2 gap-y-2 list-disc list-inside mb-6">
                        <li>Global CSS</li>
                        <li>Design tokens</li>
                        <li>Typography</li>
                        <li>Color system</li>
                        <li>Base components</li>
                        <li>Layout primitives</li>
                        <li>Accessibility rules</li>
                        <li>Global interaction patterns</li>
                    </ul>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Feature-level changes that use the existing system without modifying its foundations do not require separate Design Authority approval unless they introduce a new pattern.</p>
                </div>

                <!-- Accessibility -->
                <div class="bg-white p-6 border-[0.5px] border-[#55555a26] rounded-sm">
                    <h3 class="font-serif text-[1.15rem] text-[#1C1C1E] mb-4">Accessibility Minimums</h3>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed mb-4">All components must meet the accessibility requirements defined by the system:</p>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-2 list-disc list-inside mb-6">
                        <li>WCAG-compliant text and UI contrast</li>
                        <li>Visible keyboard focus states</li>
                        <li>Semantic HTML &amp; Appropriate heading hierarchy</li>
                        <li>Accessible form controls and labels</li>
                        <li>Sufficient touch/click targets</li>
                        <li>No information communicated by color alone</li>
                    </ul>
                    <p class="text-[0.95rem] text-[#55555A] leading-relaxed">Where AAA contrast is specified by a component or token, that requirement must be explicitly documented rather than assumed globally.</p>
                </div>
            </div>

            <!-- Exceptions, Deprecation, Versioning -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-12 border-t-[0.5px] border-[#55555a26]">
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Exceptions</div>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-4">Allowed only when there is a documented product, accessibility, technical, or performance requirement. Every exception must document: <strong class="text-[#1C1C1E]">What</strong> is being changed, <strong class="text-[#1C1C1E]">Why</strong>, <strong class="text-[#1C1C1E]">Scope</strong>, <strong class="text-[#1C1C1E]">Duration</strong>, <strong class="text-[#1C1C1E]">Owner</strong>, and <strong class="text-[#1C1C1E]">Removal plan</strong>.</p>
                    <p class="text-[0.9rem] text-[#8B3A3A] font-bold">Exceptions must not silently become new system patterns.</p>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Deprecation</div>
                    <p class="text-[0.9rem] text-[#55555A] leading-relaxed mb-4">Deprecated components remain available for <strong>one major release cycle</strong> unless there is a critical reason for earlier removal.</p>
                    <ul class="text-[0.85rem] text-[#55555A] space-y-1 list-disc list-inside">
                        <li>Marked <span class="bg-[#804526]/10 text-[#804526] px-1 rounded-sm uppercase tracking-wide text-[0.6rem] font-bold">Deprecated</span></li>
                        <li>Not used in new work</li>
                        <li>Identify replacement &amp; migration</li>
                        <li>Defined removal target</li>
                    </ul>
                </div>
                <div>
                    <div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526] mb-4">Semantic Versioning</div>
                    <ul class="text-[0.9rem] text-[#55555A] space-y-3">
                        <li><strong class="text-[#1C1C1E]">Major:</strong> Breaking changes to tokens, components, or behavior.</li>
                        <li><strong class="text-[#1C1C1E]">Minor:</strong> New backward-compatible components or capabilities.</li>
                        <li><strong class="text-[#1C1C1E]">Patch:</strong> Corrections, docs, or non-breaking refinements.</li>
                    </ul>
                    <p class="text-[0.85rem] text-[#55555A] mt-4 italic">Every major or minor release must include an updated changelog.</p>
                </div>
            </div>

        </div>
        """, 'html.parser')
        gov_sec.append(new_content)

    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write(f"---{frontmatter}---\n{str(soup)}")

update()
