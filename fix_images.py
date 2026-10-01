import re

with open('src/pages/styleguide.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove `grayscale` completely
content = content.replace('grayscale ', '')
content = content.replace('grayscale', '')

# 2. Make gradients tighter and ensure AAA contrast. 
# For gradients that were via-[#1C1C1E]/80 to-transparent, ensure they don't cover the whole image.
# Usually, I used `h-[65%] mt-auto` or `w-3/4`. Let's keep the gradients but make the image pop.
# Let's also ensure the base filter is `saturate-[0.9] contrast-[1.05] brightness-[1.05]` for that extreme luxury pop.
content = re.sub(r'contrast-\[1\.1\]', 'contrast-[1.05] saturate-[1.1] brightness-[1.05]', content)
content = re.sub(r'contrast-\[1\.05\] saturate-\[0\.85\]', 'contrast-[1.05] saturate-[1.1] brightness-[1.05]', content)

with open('src/pages/styleguide.astro', 'w', encoding='utf-8') as f:
    f.write(content)
