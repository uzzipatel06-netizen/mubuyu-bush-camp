import os

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

whatsapp_html = """
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/260977875573" class="whatsapp-float" target="_blank">
        <i class="fab fa-whatsapp"></i>
    </a>
"""

def add_whatsapp(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    if 'whatsapp-float' in content:
        print(f"Already added to {filepath}")
        return

    # Insert before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', f'{whatsapp_html}\n</body>')
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Added WhatsApp button to {filepath}")
    else:
        print(f"Could not find </body> tag in {filepath}")

for file in files:
    add_whatsapp(file)
