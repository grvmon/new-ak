from bs4 import BeautifulSoup
with open('src/pages/styleguide.astro', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
sec = soup.find(id='12-components')
if sec:
    print(sec.prettify())
