import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def final_polish(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove 'Animal' label from animal-text
    content = content.replace('<p class="text-white small text-uppercase mb-0">Animal</p>', '')
    
    # 2. Update Footer classes for better spacing (removing template-y classes)
    content = content.replace('footer bg-dark text-light footer mt-5 pt-5 wow fadeIn', 'footer wow fadeIn')
    content = content.replace('footer bg-dark text-light mt-5 pt-5 wow fadeIn', 'footer wow fadeIn')

    # 3. Clean up display classes
    content = content.replace('header-bg py-5 mb-5 wow fadeIn', 'header-bg wow fadeIn')
    
    with open(filepath, 'w') as f:
        f.write(content)

for file in files:
    final_polish(file)
