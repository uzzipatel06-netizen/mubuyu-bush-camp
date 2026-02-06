import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Remove membership.html links
    content = re.sub(r'\s*<a href="membership\.html" class="dropdown-item">Membership</a>\s*', '', content)
    
    # Remove visiting.html links from dropdown
    content = re.sub(r'\s*<a href="visiting\.html" class="dropdown-item">Visiting Hours</a>\s*', '', content)
    
    # Remove 404.html links
    content = re.sub(r'\s*<a href="404\.html" class="dropdown-item">404 Page</a>\s*', '', content)
    
    # Remove visiting hours from footer links (testimonial.html has this)
    content = re.sub(r'\s*<a class="btn btn-link" href="visiting\.html">Visiting Hours</a>\s*', '', content)
    
    # Change "Buy Ticket" to "Book Now" (case insensitive)
    content = re.sub(r'Buy Ticket', 'Book Now', content, flags=re.IGNORECASE)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

for file in files:
    update_file(file)

print("\nAll files updated successfully!")
