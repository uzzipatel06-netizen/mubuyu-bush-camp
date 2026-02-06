import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def final_polish_1(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Increase letter spacing on headings for a premium feel
    content = content.replace('class="display-', 'style="letter-spacing: 0.02em;" class="display-')
    
    # Ensure all section titles have a consistent bottom margin
    content = content.replace('mb-5', 'mb-5 pb-3')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        final_polish_1(file)
    print("Final polish 1 complete.")
