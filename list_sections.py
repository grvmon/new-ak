import re
with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    text = f.read()
for match in re.findall(r'<h2[^>]*>(.*?)</h2>', text):
    print(match)
