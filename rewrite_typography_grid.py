def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    # Block 1: Where `space-y-16` incorrectly starts inside the left column
    bad_split = """</div>
</div>
</div>
<div class="space-y-16">
<!-- Native Example 1: Editorial Image Card -->"""

    # We want to move the "Right Column Image" to here, before `space-y-16`!
    
    right_column_image = """<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">
<div class="absolute inset-0 bg-[#1C1C1E]"></div>
<div class="absolute inset-0 opacity-60 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=80')] bg-cover bg-center contrast-[1.2]"></div>
<div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent"></div>
<div class="relative z-10 p-10">
<div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-3">Copper Kicker</div>
<div class="font-serif text-3xl text-[#FAFAFA] mb-3">Headline in Titanium Frost</div>
<p class="text-[0.95rem] text-[#FAFAFA]/80 leading-relaxed font-sans max-w-sm">Body in Titanium Frost. The contrast zone is controlled natively by the gradient overlay at the bottom.</p>
</div>
</div>"""

    # Block 2: The end of Native Example 2, where it incorrectly closes the grid and puts the right_column_image
    bad_end = """<!-- End Native Hero Code -->
</div>
</div>
</div>
</div>
<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">
<div class="absolute inset-0 bg-[#1C1C1E]"></div>
<div class="absolute inset-0 opacity-60 bg-[url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=80')] bg-cover bg-center contrast-[1.2]"></div>
<div class="absolute inset-0 bg-gradient-to-t from-[#1C1C1E] via-[#1C1C1E]/50 to-transparent"></div>
<div class="relative z-10 p-10">
<div class="text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#BE7555] mb-3">Copper Kicker</div>
<div class="font-serif text-3xl text-[#FAFAFA] mb-3">Headline in Titanium Frost</div>
<p class="text-[0.95rem] text-[#FAFAFA]/80 leading-relaxed font-sans max-w-sm">Body in Titanium Frost. The contrast zone is controlled natively by the gradient overlay at the bottom.</p>
</div>
</div>
</div>"""

    if bad_split in html and bad_end in html:
        # 1. Replace the bad split by closing the left column, inserting the right column image, closing the grid, and starting the full-width space-y-16
        new_split = f"""</div>
</div>
</div>
{right_column_image}
</div>
<div class="space-y-16 mt-16">
<!-- Native Example 1: Editorial Image Card -->"""
        html = html.replace(bad_split, new_split)

        # 2. Replace the bad end by just closing the full-width examples
        new_end = """<!-- End Native Hero Code -->
</div>
</div>
</div>"""
        html = html.replace(bad_end, new_end)
        
        with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated successfully.")
    else:
        print("Could not find blocks. Printing bad_end existence:")
        print(bad_end in html)
        print("Printing bad_split existence:")
        print(bad_split in html)

update()
