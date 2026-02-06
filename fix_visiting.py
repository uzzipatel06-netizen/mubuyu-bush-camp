import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Fix visiting.html references
    content = content.replace('visiting.html', 'index.html')

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

for file in files:
    update_file(file)

print("\nAll visiting.html references fixed!")
