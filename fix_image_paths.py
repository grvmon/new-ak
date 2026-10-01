import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="assets/', 'src="/assets/')
html = html.replace("bg-[url('assets/", "bg-[url('/assets/")

with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
    f.write(html)

