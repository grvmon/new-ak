from bs4 import BeautifulSoup
import re

def update():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    parts = html.split('---')
    frontmatter = parts[1]
    body = '---'.join(parts[2:])

    # Use string replacement to avoid bs4 eating up whitespace/formatting
    old_code = """<!-- NATIVE HERO CODE -->
<div class="relative w-full h-[500px] rounded-sm overflow-hidden flex items-center shadow-xl border-[0.5px] border-[#1C1C1E]">
<div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_skyline_night_aerial.webp')] bg-cover bg-center"></div>
<!-- Gradient contrast zone -->
<div class="absolute inset-0 bg-gradient-to-r from-[#1C1C1E] via-[#1C1C1E]/90 to-transparent w-3/4"></div>
<div class="relative z-10 p-12 max-w-2xl flex flex-col gap-6">"""

    new_code = """<!-- NATIVE HERO CODE -->
<div class="relative w-full min-h-[600px] md:min-h-[650px] rounded-sm overflow-hidden flex flex-col justify-center shadow-xl border-[0.5px] border-[#1C1C1E]">
<div class="absolute inset-0 bg-[url('/assets/evergreen/prestige_evergreen_hero_skyline_night_aerial.webp')] bg-cover bg-center"></div>
<!-- Gradient contrast zone -->
<div class="absolute inset-0 bg-gradient-to-r from-[#1C1C1E] via-[#1C1C1E]/90 to-transparent w-[90%] md:w-[75%]"></div>
<div class="relative z-10 p-8 md:p-16 max-w-3xl flex flex-col gap-6 my-8">"""

    if old_code in body:
        body = body.replace(old_code, new_code)
        
        with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
            f.write(f"---{frontmatter}---{body}")
        print("Updated successfully.")
    else:
        print("COULD NOT FIND EXACT HTML BLOB")

update()
