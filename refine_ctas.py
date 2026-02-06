import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def refine_ctas(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Update CTA buttons to a more modern, minimal style
    content = content.replace('btn btn-primary py-3 px-5', 'btn btn-primary px-5 py-3 rounded-pill')
    content = content.replace('btn btn-outline-light py-3 px-5', 'btn btn-outline-light px-5 py-3 rounded-pill')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        refine_ctas(file)
    print("CTAs refined.")
