def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    bad_block = """<!-- Final Principle -->
<div class="bg-[#1C1C1E] text-white p-12 rounded-sm mt-12 text-center">
<div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans">
<div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
<div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-3xl leading-[1.3]">Text should never be colored because it looks better. It should be colored because it has a defined role.</div>
</div>
</div>"""

    good_block = """<!-- Final Principle -->
<div class="bg-[#1C1C1E] p-12 rounded-sm mt-12 flex flex-col font-sans text-left border-[0.5px] border-[#55555a26]">
<div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-4">The Principle</div>
<div class="font-serif text-[32px] text-[#FAFAFA] font-normal max-w-4xl leading-[1.3]">Text should never be colored because it looks better. It should be colored because it has a defined role.</div>
</div>"""

    if bad_block in html:
        html = html.replace(bad_block, good_block)
        with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated successfully.")
    else:
        print("COULD NOT FIND EXACT HTML BLOB")

update()
