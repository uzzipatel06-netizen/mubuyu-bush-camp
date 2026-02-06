import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def refine_bullets(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Replace standard checkmarks with something more elegant or ensure consistent color
    content = content.replace('fa fa-check text-primary me-3', 'fa fa-check text-secondary me-2')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        refine_bullets(file)
    print("Bullets refined.")
