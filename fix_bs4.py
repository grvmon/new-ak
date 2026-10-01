from bs4 import BeautifulSoup

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('---')
frontmatter = parts[1]
body = '---'.join(parts[2:])

soup = BeautifulSoup(body, 'html.parser')

# The main container for "Text on Images" section
# It has a heading "2. Text on Images (Native Implementation)"
h = soup.find(string=lambda t: t and '2. Text on Images (Native Implementation)' in t)
if h:
    # h is a text node. Its parent is div.text-[0.75rem]
    left_col_content = h.parent.parent
    grid_container = left_col_content.parent # this is <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t-[0.5px] border-[#55555a26] pt-12">
    
    # Inside left_col_content, there is <div class="space-y-16">
    space_y = left_col_content.find('div', class_=lambda c: c and 'space-y-16' in c)
    
    # Outside the grid_container, somewhere down below, there is the image block
    # It has text "Copper Kicker"
    kicker = soup.find(string=lambda t: t and 'Copper Kicker' in t)
    image_block = kicker.parent.parent # this is <div class="relative rounded-sm overflow-hidden border-[0.5px] border-[#55555a26] flex flex-col justify-end min-h-[400px]">

    if space_y and image_block:
        # Extract the image block from its current location
        image_block.extract()
        
        # Extract space_y block
        space_y.extract()
        
        # Put the image block as the second child of grid_container
        grid_container.append(image_block)
        
        # Put space_y right AFTER grid_container
        grid_container.insert_after(space_y)
        
        # Add a margin to space_y so it looks good
        space_y['class'] = space_y.get('class', []) + ['mt-16']
        
        with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
            f.write(f"---{frontmatter}---\n{str(soup)}")
        print("DOM restructured successfully.")
    else:
        print("Could not find space_y or image_block.")
else:
    print("Could not find heading.")
