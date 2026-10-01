import re
from bs4 import BeautifulSoup

def review_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    findings = []
    
    # Check 1: Icon-only buttons need aria-label
    # For each button, if no text and no aria-label, flag
    for button in soup.find_all('button'):
        text = button.get_text(strip=True)
        aria = button.get('aria-label')
        if not text and not aria:
            findings.append(("Icon-only button missing aria-label", str(button)[:100]))

    # Check 2: Form controls need label or aria-label
    for input_tag in soup.find_all('input'):
        aria = input_tag.get('aria-label')
        # simple check: if no label wrapping or associated by id, and no aria-label
        # checking htmlFor is complex, we just check aria-label or wrapped in label
        if not aria and not input_tag.find_parent('label'):
            # Also look for a <label> nearby, but since we are doing simple regex, let's just see if there's an id
            if not input_tag.get('id'):
                findings.append(("Input missing id/aria-label/label wrapper", str(input_tag)[:100]))
                
    # Check 3: Images need alt
    for img in soup.find_all('img'):
        if not img.has_attr('alt'):
            findings.append(("Image missing alt attribute", str(img)[:100]))
            
    # Check 4: Images need explicit width/height
    for img in soup.find_all('img'):
        if not img.has_attr('width') or not img.has_attr('height'):
            findings.append(("Image missing explicit width/height", str(img)[:100]))
            
    # Check 5: ... vs …
    if '...' in html:
        findings.append(("Uses '...' instead of '…' (ellipsis)", "Found '...' in the file"))
        
    # Check 6: " outline-none " or "outline: none"
    if 'outline-none' in html:
        findings.append(("Uses 'outline-none' without verifying focus replacement", "Found 'outline-none'"))
        
    # Check 7: autocomplete
    for input_tag in soup.find_all('input'):
        if input_tag.get('type') in ['text', 'email', 'tel'] and not input_tag.has_attr('autocomplete'):
            findings.append(("Input missing autocomplete attribute", str(input_tag)[:100]))
            
    # Check 8: SVGs as icons might need aria-hidden="true" if decorative
    for svg in soup.find_all('svg'):
        if not svg.has_attr('aria-hidden') and not svg.has_attr('aria-label'):
            findings.append(("SVG might need aria-hidden='true'", str(svg)[:100]))
            
    # output
    for finding in findings:
        print(f"{finding[0]}: {finding[1]}")

review_file('src/pages/styleguide.astro')
