from bs4 import BeautifulSoup

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    soup = BeautifulSoup(body, 'html.parser')
    
    # We can use regex to just insert `</div></div>` and remove the extra ones at the end
    # But string replacement is safer.
    old_html = """</div>
</div>
</div>
<div class="space-y-16">
<!-- Native Example 1: Editorial Image Card -->"""

    new_html = """</div>
</div>
</div>
</div>
<!-- End of 2-col grid for Text on Images Rules -->

<!-- Full width Native Examples -->
<div class="space-y-16 mt-16">
<!-- Native Example 1: Editorial Image Card -->"""

    # And we must remove the trailing `</div></div>` that used to close that grid
    old_end = """<!-- End Native Hero Code -->
</div>
</div>
</div>
</div>
<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">"""

    new_end = """<!-- End Native Hero Code -->
</div>
</div>
<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px] hidden">"""

    # Wait, the `relative rounded-sm` image block with "Copper Kicker" was supposed to be in the RIGHT column!
    # If I close the grid early, that image block will now be full width, or it will be sitting outside the grid!
    # Let me restructure it properly.
