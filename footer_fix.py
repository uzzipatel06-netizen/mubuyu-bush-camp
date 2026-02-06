import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def footer_fix(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Ensure footer alignment and spacing
    content = content.replace('me-3', 'me-2') # Subtler icon spacing
    content = content.replace('mb-4 text-white', 'mb-4 text-white fw-bold') # Header weight
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        footer_fix(file)
    print("Footer fix complete.")
