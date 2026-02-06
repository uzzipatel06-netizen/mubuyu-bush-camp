import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

old_fonts = r'<link href="https://fonts\.googleapis\.com/css2\?family=Open\+Sans:wght@400;500&family=Quicksand:wght@600;700&display=swap" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Outfit:wght@100..900&display=swap" rel="stylesheet">'

def refactor_html(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update Fonts in Head
    content = re.sub(old_fonts, new_fonts, content)
    
    # 2. Update display classes for better hierarchy
    # (Optional: can do more specific display class replacements if needed)

    # 3. Ensure section spacing is consistent
    # We already overrode .py-5 in CSS, so no need to change class names, 
    # but we can remove unnecessary 'mb-5' or 'mt-5' that might conflict.
    
    # 4. Refine Topbar and Navbar branding
    content = content.replace('class="m-0 text-primary">Mubuyu Bush Camp</h1>', 'class="m-0 text-primary" style="font-family: var(--serif); font-weight: 800; letter-spacing: -0.02em;">Mubuyu Bush Camp</h1>')

    # 5. Clean up buttons (removing rounded classes if any, though our CSS already overrides border-radius)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Refactor step 1 complete for {filepath}")

for file in files:
    refactor_html(file)
