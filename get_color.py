from bs4 import BeautifulSoup
with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    c = soup.find(id='04-color')
    if c:
        print(str(c)[:1000]) # just to confirm it's there
