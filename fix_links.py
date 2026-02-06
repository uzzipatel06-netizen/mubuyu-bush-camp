import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Fix services.html -> service.html
    content = content.replace('services.html', 'service.html')
    
    # Fix wildlife.html -> animal.html (since we have animal.html for wildlife)
    content = content.replace('wildlife.html', 'animal.html')
    content = content.replace('>Wildlife<', '>Our Animals<')
    
    # Fix gallery.html -> index.html#gallery (or just remove it)
    content = content.replace('gallery.html', 'index.html')
    
    # Fix booking.html -> contact.html (since booking page doesn't exist, contact is the next best option)
    content = content.replace('booking.html', 'contact.html')
    content = content.replace('>Booking<', '>Contact<')

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

for file in files:
    update_file(file)

print("\nAll broken links fixed!")
