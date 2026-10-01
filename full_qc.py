from bs4 import BeautifulSoup
import re

def run_qc():
    with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    issues = []

    # 1. Check for hardcoded heights that might break on mobile text wrapping
    for div in soup.find_all('div'):
        classes = div.get('class', [])
        for c in classes:
            if re.match(r'^h-\[\d+px\]$', c):
                issues.append(f"Hardcoded height found: {c}. Consider min-h to prevent overflow on mobile. Element: {str(div)[:50]}")

    # 2. Check for flex without flex-col on mobile (flex gap-x without md:flex-row)
    for div in soup.find_all('div'):
        classes = div.get('class', [])
        if 'flex' in classes and not any(c.startswith('flex-col') or c.startswith('flex-wrap') for c in classes):
            # It's a row by default. Are there too many items for a small screen?
            if len(div.find_all(recursive=False)) > 2:
                if not any(c.startswith('md:flex-col') or c.startswith('lg:flex-col') or c.startswith('sm:flex-col') or 'flex-wrap' in classes or 'md:flex-row' in classes for c in classes):
                    issues.append(f"Possible mobile overflow in flex row with >2 items. Element: {str(div)[:50]}")

    # 3. Look for remaining placeholder texts or TODOs
    if 'TODO' in html or 'Lorem ipsum' in html:
        issues.append("Found 'TODO' or 'Lorem ipsum' placeholder text.")

    # 4. Check images for missing src or common missing assets
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src:
            issues.append(f"Image missing src: {str(img)[:50]}")
            
    # 5. Check missing links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href == '#' or href == '':
            issues.append(f"Empty or placeholder link found: {str(a)[:50]}")

    if not issues:
        print("No critical structural issues found.")
    else:
        for i, issue in enumerate(set(issues)):
            print(f"{i+1}. {issue}")

run_qc()
