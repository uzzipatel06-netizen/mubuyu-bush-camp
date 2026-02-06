import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def update_typography_classes(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Promote Hero/Main H1 to display-1 or display-2
    content = content.replace('class="display-4 text-light mb-4"', 'class="display-2 text-light mb-4"')
    content = content.replace('class="display-4 text-white mb-3 animated slideInDown"', 'class="display-2 text-white mb-3 animated slideInDown"')

    # 2. Section Headings (H2) to display-4
    content = content.replace('class="display-5 mb-4"', 'class="display-4 mb-4"')
    content = content.replace('class="display-5 mb-0"', 'class="display-4 mb-0"')
    content = content.replace('class="display-5 mb-5"', 'class="display-4 mb-5"')
    content = content.replace('class="display-6 text-white mb-5"', 'class="display-5 text-white mb-5"')

    # 3. Specifically for facts/counters
    content = content.replace('class="display-4 text-primary mb-2"', 'class="display-3 text-primary mb-2"')

    with open(filepath, 'w') as f:
        f.write(content)

for file in files:
    update_typography_classes(file)
