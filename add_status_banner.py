import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html']

banner_html = """
    <!-- Operating Status Banner -->
    <div class="top-notice-banner container-fluid">
        <span class="status-badge status-red">Notice</span> 
        We are currently on seasonal break until April. Taking bookings for the 2026 season! 
        <a href="contact.html" class="text-primary ms-2 underline">Book Your Dates &raquo;</a>
    </div>
"""

favicon_html = '<link href="img/mubuyu-logo.png" rel="icon" type="image/png">'

def update_pages(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Add Favicon
    if 'rel="icon"' not in content:
        content = re.sub(r'</head>', f'    {favicon_html}\n</head>', content)
    
    # 2. Add Status Banner after <body>
    if 'top-notice-banner' not in content:
        content = re.sub(r'<body>', f'<body>\n{banner_html}', content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated banner and favicon in {filepath}")

for file in files:
    update_pages(file)
