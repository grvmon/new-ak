import re
from bs4 import BeautifulSoup

def convert_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Strip all <style> blocks
    for s in soup.find_all('style'):
        s.decompose()
        
    layout = soup.find('div', class_='ds-layout')
    
    # aggressive class mapping
    class_map = {
        'ds-layout': 'flex flex-col lg:flex-row min-h-screen bg-[#FAFAFA] text-[#1C1C1E]',
        'ds-nav': 'hidden lg:block w-64 shrink-0 border-r-[0.5px] border-[#55555a26] h-screen sticky top-0 p-8 overflow-y-auto bg-white',
        'ds-main-content': 'flex-1 min-w-0 p-8 lg:p-16',
        'ds-container': 'max-w-5xl mx-auto',
        'ds-nav-group': 'text-[0.75rem] font-bold tracking-widest uppercase text-[#804526] mt-8 mb-2',
        'ds-section': 'mb-24 pb-16 border-b-[0.5px] border-[#55555a26]',
        'ds-section-title': 'font-serif text-3xl text-[#1C1C1E] mb-4',
        'ds-section-desc': 'font-sans text-[1.1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed',
        'ds-table': 'w-full text-left border-collapse font-sans mb-12',
        'ds-swatch-grid': 'grid grid-cols-2 md:grid-cols-5 gap-6',
        'ds-swatch': 'rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] bg-white',
        'ds-swatch-color': 'h-32 w-full',
        'ds-swatch-meta': 'p-4',
        'ds-swatch-name': 'font-sans font-bold text-[0.95rem] text-[#1C1C1E] mb-1',
        'ds-swatch-hex': 'font-sans text-[0.8rem] text-[#55555A] tracking-wide',
        'ds-banned': 'text-[#55555A] line-through',
        'ds-approved': 'text-[#804526] font-bold',
        'ds-bible-header': 'bg-[#1C1C1E] text-[#FAFAFA] py-24 px-8 text-center',
    }
    
    for el in soup.find_all(class_=True):
        classes = el['class']
        new_classes = []
        for c in classes:
            if c in class_map:
                new_classes.extend(class_map[c].split())
            else:
                new_classes.append(c)
        el['class'] = new_classes
        
    for a in soup.find_all('a'):
        if 'ds-nav' in (a.parent.get('class', []) if a.parent else []):
            a['class'] = a.get('class', []) + ['block', 'py-2', 'text-[0.85rem]', 'text-[#55555A]', 'hover:text-[#804526]', 'transition-colors']
            
    # Strip all inline styles
    for el in soup.find_all(style=True):
        del el['style']

    with open('src/pages/documentation.astro', 'w', encoding='utf-8') as f:
        f.write("---\n// Completely Native Tailwind Documentation Page\n---\n")
        f.write(str(soup))

convert_html('live_site.html')
