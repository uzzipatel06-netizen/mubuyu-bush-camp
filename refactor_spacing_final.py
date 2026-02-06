import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def refine_spacing_and_sections(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Standardize section headers and labels
    content = content.replace('<p><span class="text-primary me-2">#</span>', '<p class="text-primary text-uppercase fw-bold mb-2" style="letter-spacing: 0.2em;">')
    
    # 2. Add bg-light-alt to select sections for diversity
    # We'll use a simple alternating approach or target specific sections
    
    if 'accommodation.html' in filepath:
        content = content.replace('class="container-xxl py-5 bg-light"', 'class="container-xxl bg-light-alt py-5"')
        
    if 'service.html' in filepath:
        # Alternating services? No, maybe just the section header?
        # Let's make the Whole Service section bg-light-alt if it's the main thing.
        pass

    # 3. Increase internal spacing for rows that might be tight
    content = content.replace('class="row g-5"', 'class="row g-5 py-5"') # Add internal padding to large rows
    
    # 4. Clean up the 'Facts' section globally if it exists
    content = content.replace('class="container-xxl facts py-5"', 'class="container-xxl facts bg-light-alt py-5"')

    with open(filepath, 'w') as f:
        f.write(content)

for file in files:
    refine_spacing_and_sections(file)
