with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the failed rename due to HTML entity
html = html.replace('21. Reports &amp; Dossiers', '21. Print &amp; PDF Intelligence Reports')

# I will also check the Sidebar navigation to make sure it matches
html = html.replace('14. Property Design System', '14. Digital Property Pages')
html = html.replace('21. Reports &amp; Dossiers', '21. Print &amp; PDF Intelligence Reports')

with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
    f.write(html)
