import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def update_global_elements(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update Dropdown Menu
    new_dropdown = """<div class="dropdown-menu rounded-0 rounded-bottom m-0">
                        <a href="accommodation.html" class="dropdown-item">Accommodation</a>
                        <a href="animal.html" class="dropdown-item">Our Animals</a>
                        <a href="gallery.html" class="dropdown-item">Gallery</a>
                        <a href="testimonial.html" class="dropdown-item">Testimonial</a>
                        <a href="contact.html" class="dropdown-item">Contact</a>
                    </div>"""
    
    dropdown_pattern = r'<div class="dropdown-menu rounded-0 rounded-bottom m-0">.*?</div>'
    content = re.sub(dropdown_pattern, new_dropdown, content, flags=re.DOTALL)

    # 2. Update Header Button
    # Handle both old contact.html and new whatsapp links (to ensure consistency)
    old_button_pattern = r'<a href="(?:contact\.html|https://wa\.me/260977875573)" class="btn btn-primary">.*?</a>'
    new_button = '<a href="https://wa.me/260977875573" class="btn btn-primary">WhatsApp Us<i class="fab fa-whatsapp ms-3"></i></a>'
    content = re.sub(old_button_pattern, new_button, content)

    # 3. Update Footer Quick Links
    new_footer_links = """<div class="col-lg-3 col-md-6">
                    <h5 class="text-light mb-4">Quick Links</h5>
                    <a class="btn btn-link" href="index.html">Home</a>
                    <a class="btn btn-link" href="about.html">About</a>
                    <a class="btn btn-link" href="accommodation.html">Accommodation</a>
                    <a class="btn btn-link" href="animal.html">Our Animals</a>
                    <a class="btn btn-link" href="gallery.html">Gallery</a>
                </div>"""
    
    footer_pattern = r'<div class="col-lg-3 col-md-6">\s*<h5 class="text-light mb-4">Quick Links</h5>.*?</div>'
    content = re.sub(footer_pattern, new_footer_links, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Refreshed global elements in {filepath}")

for file in files:
    update_global_elements(file)
