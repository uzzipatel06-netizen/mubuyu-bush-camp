import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'gallery.html', 'accommodation.html']

def apply_alternating_sections(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Apply alternating backgrounds to main sections
    # We'll do this carefully by finding common section starts
    
    # In index.html specifically:
    if 'index.html' in filepath:
        content = content.replace('class="container-xxl facts py-5', 'class="container-xxl facts bg-light-alt py-5')
        content = content.replace('class="container-xxl py-5">', 'class="container-xxl bg-light-alt py-5">', 1) # First one after facts is Wildlife usually
        # Actually let's look at the structure again or do it manually for index.html
        pass

    with open(filepath, 'w') as f:
        f.write(content)

# Refactor index.html manually for precision
with open('index.html', 'r') as f:
    content = f.read()

# Section 1: About (Stay Light)
# Section 2: Facts (Make Alt)
content = content.replace('class="container-xxl facts py-5', 'class="container-xxl facts bg-light-alt py-5')
# Section 3: Services (Stay Light)
# Section 4: Wildlife Gallery (Make Alt) - find the one after Services
services_end = content.find('<!-- Services Section End -->')
gallery_start = content.find('<!-- Wildlife Gallery Start -->', services_end)
if gallery_start != -1:
    content = content[:gallery_start] + content[gallery_start:].replace('class="container-xxl py-5"', 'class="container-xxl bg-light-alt py-5"', 1)

# Section 5: Booking Info (Stay Light - it's already var(--light))
# Section 6: Social Media (Make Alt)
social_start = content.find('<!-- Social Media Start -->')
if social_start != -1:
    content = content[:social_start] + content[social_start:].replace('class="container-xxl py-5"', 'class="container-xxl bg-light-alt py-5"', 1)

with open('index.html', 'w') as f:
    f.write(content)

print("Applied alternating backgrounds to index.html")
