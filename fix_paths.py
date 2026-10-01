import os

def update_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace /assets/ with /new-ak/assets/
    new_content = content.replace("url('/assets/", "url('/new-ak/assets/")
    new_content = new_content.replace('url("/assets/', 'url("/new-ak/assets/')
    new_content = new_content.replace('src="/assets/', 'src="/new-ak/assets/')
    new_content = new_content.replace("src='/assets/", "src='/new-ak/assets/")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

update_file('src/pages/styleguide.astro')
update_file('src/pages/index.astro')
update_file('src/pages/[slug].astro')

# Update astro.config.mjs to use base permanently
with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    config = f.read()

config = config.replace("base: isGithubActions ? '/new-ak' : ''", "base: '/new-ak'")
with open('astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(config)

print("Paths updated.")
