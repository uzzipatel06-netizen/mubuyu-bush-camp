import os

files = ['animal.html', 'index.html']

def polish_animal(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Refine the look of animal cards (if they exist in the file)
    content = content.replace('animal-item', 'animal-item shadow-sm rounded overflow-hidden')
    content = content.replace('bg-light p-4', 'bg-white p-4')
    
    with open(filepath, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    for file in files:
        polish_animal(file)
    print("Animal polish complete.")
