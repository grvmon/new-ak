from bs4 import BeautifulSoup

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

typo = soup.find(id='05-typography')
if typo:
    # Just print the first 2000 characters to see how the top part is structured
    print(str(typo)[:2000])
