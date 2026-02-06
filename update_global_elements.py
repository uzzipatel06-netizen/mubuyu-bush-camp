import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

def update_global_elements(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Update Dropdown Menu
    # Matching variations in spacing
    new_dropdown = """<div class="dropdown-menu rounded-0 rounded-bottom m-0">
                        <a href="accommodation.html" class="dropdown-item">Accommodation</a>
                        <a href="animal.html" class="dropdown-item">Wildlife</a>
                        <a href="gallery.html" class="dropdown-item">Gallery</a>
                        <a href="testimonial.html" class="dropdown-item">Testimonial</a>
                    </div>"""
    
    # Regex to handle whitespace variations
    dropdown_pattern = r'<div class="dropdown-menu rounded-0 rounded-bottom m-0">.*?</div>'
    content = re.sub(dropdown_pattern, new_dropdown, content, flags=re.DOTALL)

    # 2. Update Header Button
    old_button = r'<a href="contact.html" class="btn btn-primary">Book Now<i class="fa fa-arrow-right ms-3"></i></a>'
    new_button = '<a href="https://wa.me/260977875573" class="btn btn-primary">WhatsApp Us<i class="fab fa-whatsapp ms-3"></i></a>'
    content = content.replace(old_button, new_button)

    # Update variations for active/inactive links in index.html Gallery
    content = content.replace('<a href="index.html" class="dropdown-item">Gallery</a>', '<a href="gallery.html" class="dropdown-item">Gallery</a>')

    # 3. Update Footer Quick Links
    old_footer_links = r'<div class="col-lg-3 col-md-6">\s*<h5 class="text-light mb-4">Quick Links</h5>.*?</div>'
    
    new_footer_links = """<div class="col-lg-3 col-md-6">
                    <h5 class="text-light mb-4">Discovery</h5>
                    <a class="btn btn-link" href="about.html">Our Story</a>
                    <a class="btn btn-link" href="accommodation.html">Accommodation</a>
                    <a class="btn btn-link" href="service.html">Experiences</a>
                    <a class="btn btn-link" href="animal.html">Wildlife</a>
                    <a class="btn btn-link" href="gallery.html">Gallery</a>
                </div>"""
    
    content = re.sub(old_footer_links, new_footer_links, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated global elements in {filepath}")

for file in files:
    update_global_elements(file)
