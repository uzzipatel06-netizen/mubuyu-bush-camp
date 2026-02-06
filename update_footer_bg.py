import os
import re

files = ['about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

footer_bg_style = ' style="background: linear-gradient(rgba(62, 44, 30, 0.95), rgba(62, 44, 30, 0.95)), url(\'img/footer-lodge.jpg\') center center no-repeat; background-size: cover;"'

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Add background image to footer (for div-based footers)
    content = re.sub(
        r'(<div class="container-fluid footer bg-dark text-light footer mt-5 pt-5 wow fadeIn" data-wow-delay="0\.1s")>',
        r'\1' + footer_bg_style + '>',
        content
    )
    
    # Also handle footer tags (like in index.html)
    content = re.sub(
        r'(<footer class="container-fluid footer bg-dark text-light mt-5 pt-5 wow fadeIn" data-wow-delay="0\.1s")',
        r'\1' + footer_bg_style,
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

for file in files:
    update_file(file)

print("\nAll footer backgrounds updated!")
