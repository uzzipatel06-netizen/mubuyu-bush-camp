import os

files = ['gallery.html', 'index.html']

def polish_gallery(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Refine gallery elements
    content = content.replace('portfolio-item', 'portfolio-item rounded overflow-hidden shadow-sm')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        polish_gallery(file)
    print("Gallery polish complete.")
