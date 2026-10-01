from bs4 import BeautifulSoup
with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    c = soup.find(id='03-logo')
    if c:
        print(str(c))
