from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    # The exact malformed block
    old_code = """<!-- End Native Hero Code -->
</div>
</div>
</div>
</div>
<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">"""

    new_code = """<!-- End Native Hero Code -->
</div>
</div>
<div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px] mt-16">"""

    if old_code in body:
        body = body.replace(old_code, new_code)
        
        with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
            f.write(f"---{frontmatter}---{body}")
        print("Updated successfully.")
    else:
        print("COULD NOT FIND EXACT HTML BLOB")

update()
