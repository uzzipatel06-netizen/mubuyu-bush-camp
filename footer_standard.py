import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def standardize_footer(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Define the consistent footer sections or styles here
    # This is a placeholder for standardizing the footer across the site
    
    # Example: Ensure all footers have the same background or padding
    # (Matches what was in update_footer_bg.py but generalized)
    
    footer_bg_style = ' style="background: linear-gradient(rgba(62, 44, 30, 0.95), rgba(62, 44, 30, 0.95)), url(\'img/footer-lodge.jpg\') center center no-repeat; background-size: cover;"'
    
    if footer_bg_style not in content:
        content = re.sub(
            r'(<(div|footer) class="container-fluid footer[^">]*)',
            r'\1' + footer_bg_style,
            content
        )

    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        standardize_footer(file)
    print("Footer standardization complete.")
