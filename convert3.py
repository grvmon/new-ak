import re
from bs4 import BeautifulSoup

def convert_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Strip all <style> blocks
    for s in soup.find_all('style'):
        s.decompose()
        
    class_map = {
        'ds-layout': 'flex flex-col lg:flex-row min-h-screen bg-[#FAFAFA] text-[#1C1C1E]',
        'ds-nav': 'hidden lg:block w-[250px] shrink-0 border-r-[0.5px] border-[#55555a26] h-screen sticky top-0 p-8 overflow-y-auto bg-white font-sans',
        'ds-main-content': 'flex-1 min-w-0',
        'ds-nav-group': 'mt-6 mb-2 text-[0.75rem] font-bold tracking-[0.15em] uppercase text-[#804526]',
        'ds-menu-light': '',
        'ds-menu-dark': '',
        'ak-pan-container': 'overflow-hidden rounded-sm group relative',
        'ak-image-pan': 'w-full h-full object-cover transition-transform duration-700 ease-in-out group-hover:scale-105',
        'demo-blur-backdrop': 'absolute inset-0 bg-transparent backdrop-blur-none transition-all duration-500 flex items-center justify-center pointer-events-none group-hover:bg-[#0A0A0B]/75 group-hover:backdrop-blur-md',
        'demo-blur-modal': 'bg-white p-8 rounded-sm opacity-0 translate-y-2 transition-all duration-500 group-hover:opacity-100 group-hover:translate-y-0 pointer-events-auto',
        'demo-blur-container': 'relative group',
        'ds-top-tab': 'font-sans text-[0.85rem] font-bold text-[#55555A] uppercase tracking-[0.05em] pb-4 border-b-2 border-transparent -mb-[1px] cursor-pointer transition-colors hover:text-[#804526]',
        'ds-side-tab': 'font-sans text-[0.85rem] font-bold text-[#55555A] uppercase tracking-[0.05em] p-4 border-r-2 border-transparent cursor-pointer transition-colors -mr-[1px] hover:text-[#804526]',
        'ds-tab-panel': 'hidden',
        'ds-accordion-trigger': 'w-full bg-transparent border-none py-6 cursor-pointer flex justify-between items-center text-left hover:text-[#804526]',
        'ds-accordion-content': 'hidden pb-8',
        'ak-btn-ghost': 'block text-center p-4 border-[0.5px] border-[#804526] rounded-sm font-sans text-[0.85rem] font-bold text-[#804526] uppercase tracking-[0.05em] transition-colors hover:bg-[#804526] hover:text-white',
        'ak-range-slider': 'appearance-none w-full h-[2px] bg-[#55555a33] outline-none rounded-sm my-4 cursor-pointer',
        'ds-bible-header': 'bg-[#1C1C1E] text-[#FAFAFA] py-24 px-8 text-center',
        'ds-container': 'max-w-[1280px] mx-auto px-8 py-16 pb-32',
        'ds-section': 'scroll-mt-16 mb-24 pb-16 border-b-[0.5px] border-[#55555a26]',
        'ds-section-title': 'font-serif text-2xl font-normal text-[#1C1C1E] mb-2',
        'ds-section-desc': 'font-sans text-[1rem] text-[#55555A] max-w-3xl mb-12 leading-relaxed',
        'ds-swatch-grid': 'grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6',
        'ds-swatch': 'rounded-sm overflow-hidden border-[0.5px] border-[#55555a1a] bg-white flex flex-col',
        'ds-swatch-color': 'relative flex items-end py-3 px-4 h-[120px] w-full',
        'ds-swatch-meta': 'p-5 flex-1',
        'ds-swatch-name': 'font-sans font-bold text-[0.95rem] text-[#1C1C1E] mb-1',
        'ds-swatch-hex': 'font-sans text-[0.8rem] text-[#55555A] tabular-nums mb-2 tracking-[0.02em]',
        'ds-swatch-badge': 'font-sans text-[0.7rem] text-[#804526] bg-[#804526]/10 border-[0.5px] border-[#804526]/20 rounded-sm px-2 py-1 inline-block tracking-[0.03em] font-semibold',
        'ds-swatch-role': 'font-sans text-[0.7rem] font-semibold tracking-[0.08em] uppercase text-white drop-shadow-md',
        'ds-table': 'w-full border-collapse font-sans mb-8',
        'ds-banned': 'text-[#55555A] line-through font-normal',
        'ds-approved': 'text-[#804526] font-bold',
        'ds-type-row': 'mb-8 pb-8 border-b-[0.5px] border-dashed border-[#55555a1a]',
        'ds-type-meta': 'font-sans text-[0.75rem] uppercase tracking-[0.15em] text-[#804526] mb-2',
        'ds-card-demo': 'grid grid-cols-1 md:grid-cols-2 gap-8',
        'ds-card': 'bg-white rounded-sm border-[0.5px] border-[#55555a26] p-8 transition-colors duration-300 cursor-pointer hover:bg-[#FAFAFA] hover:border-[#55555a4d]',
        'ds-card-title': 'font-serif text-[1.15rem] font-normal text-[#1C1C1E] mb-4',
        'ds-card-btn': 'bg-gradient-to-r from-[#be7555] to-[#9f5334] text-white border-none rounded-sm px-6 py-3 font-sans text-[0.85rem] font-normal cursor-pointer transition-opacity duration-300 hover:opacity-90',
        'ds-photo-grid': 'grid grid-cols-1 md:grid-cols-2 gap-8',
        'ds-photo-wrapper': 'relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26]',
        'img-filtered': 'contrast-[1.05] saturate-[0.85]',
        'ds-photo-label': 'absolute top-4 left-4 bg-[#0A0A0B]/85 text-white font-sans text-[0.75rem] px-3 py-1 rounded-sm tracking-[0.12em]',
        'h1-demo': 'font-serif text-3xl md:text-5xl font-normal mb-4 tracking-[-0.02em]'
    }
    
    for el in soup.find_all(class_=True):
        classes = el.get('class', [])
        new_classes = []
        for c in classes:
            if c in class_map:
                if class_map[c]:  # only extend if not empty
                    new_classes.extend(class_map[c].split())
            else:
                new_classes.append(c)
        el['class'] = new_classes

    # Handle tags specific cases (like ds-nav a, ds-table th/td)
    # Nav links
    nav = soup.find('nav', class_=lambda c: c and 'sticky' in c)
    if nav:
        for a in nav.find_all('a'):
            a['class'] = a.get('class', []) + ['block', 'py-2', 'text-[0.85rem]', 'text-[#55555A]', 'hover:text-[#804526]', 'transition-colors']
            if a.get('aria-current') == 'true':
                a['class'] = a.get('class', []) + ['font-bold', 'text-[#804526]']

    # Table TH/TD
    for th in soup.find_all('th'):
        th['class'] = th.get('class', []) + ['text-left', 'py-4', 'px-4', 'border-b-[0.5px]', 'border-[#55555a26]', 'text-[0.85rem]', 'uppercase', 'tracking-[0.12em]', 'text-[#55555A]']
    for td in soup.find_all('td'):
        td['class'] = td.get('class', []) + ['text-left', 'py-4', 'px-4', 'border-b-[0.5px]', 'border-[#55555a26]', 'text-[0.95rem]', 'text-[#1C1C1E]']

    # Strip inline styles and translate color blocks
    for el in soup.find_all(style=True):
        style = el['style']
        
        # Swatch colors
        if 'background: var(--obsidian-black)' in style:
            el['class'] = el.get('class', []) + ['bg-[#1C1C1E]']
        elif 'background: var(--titanium-frost)' in style:
            el['class'] = el.get('class', []) + ['bg-[#FAFAFA]']
        elif 'background: linear-gradient(135deg, #be7555 0%, #9f5334 100%)' in style or 'background: linear-gradient' in style and '#be7555' in style:
            el['class'] = el.get('class', []) + ['bg-gradient-to-br', 'from-[#be7555]', 'to-[#9f5334]']
        elif 'background: var(--text-copper-aaa)' in style:
            el['class'] = el.get('class', []) + ['bg-[#804526]']
        elif 'background: var(--neutral-grey)' in style:
            el['class'] = el.get('class', []) + ['bg-[#55555A]']
        
        # Remove the style attribute completely!
        del el['style']
        
    # Write to styleguide.astro directly
    with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
        f.write("---\n// 100% Native Tailwind Documentation Port\n---\n")
        f.write("<!DOCTYPE html>\n")
        f.write(str(soup))

convert_html('live_site.html')
