with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('>23. Accessibility<', '>23. Accessibility Architecture<')
html = html.replace('>26. Next.js / Frontend Rules<', '>26. Next.js / Frontend Architecture<')

with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
    f.write(html)
