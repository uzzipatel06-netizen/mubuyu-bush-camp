import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def luxury_naming(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Rename common terms to more luxurious ones
    content = content.replace('Our Services', 'The Experience')
    content = content.replace('Services', 'Experiences')
    content = content.replace('Our Animals', 'Wildlife')
    content = content.replace('Book Now', 'Inquire Today')
    content = content.replace('Read More', 'Explore More')
    content = content.replace('Specialist', 'Expert Guide')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        luxury_naming(file)
    print("Luxury naming applied.")
