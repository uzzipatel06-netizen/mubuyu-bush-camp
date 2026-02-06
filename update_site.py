import os
import re

files = ['index.html', 'about.html', 'service.html', 'contact.html', 'testimonial.html', 'animal.html', 'accommodation.html', 'gallery.html']

phone_number = "+260 977 875573"
email = "mubuyubushcamp@gmail.com"
facebook_url = "https://www.facebook.com/p/Mubuyu-Bush-Camp-100071736289644/"
instagram_url = "https://www.instagram.com/mubuyu.bush.camp/"

social_icons_topbar = f'''<a class="btn btn-sm-square bg-white text-primary me-1" href="{facebook_url}"><i class="fab fa-facebook-f"></i></a>
                    <a class="btn btn-sm-square bg-white text-primary me-0" href="{instagram_url}"><i class="fab fa-instagram"></i></a>'''

social_icons_footer = f'''<a class="btn btn-outline-light btn-social" href="{facebook_url}"><i class="fab fa-facebook-f"></i></a>
                        <a class="btn btn-outline-light btn-social" href="{instagram_url}"><i class="fab fa-instagram"></i></a>'''

# Regex patterns for common placeholders
phone_patterns = [
    r'\+260 XX XXX XXXX',
    r'\+260 123 456 789',
    r'\+260 97 123 4567',
    r'012 345 6789'
]

email_pattern = r'info@mubuyubushcamp\.com|info@example\.com'

# Footer credit pattern
footer_credit_pattern = r'Designed By <a class="border-bottom" href="https://htmlcodex\.com">HTML Codex</a>'

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    print(f"Updating {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()

    # Update Phone Numbers
    for pat in phone_patterns:
        content = re.sub(pat, phone_number, content)
    
    # Update Email
    content = re.sub(email_pattern, email, content)
    
    # Remove Footer Credit
    content = re.sub(footer_credit_pattern, '', content)

    # Topbar Social Icons Replacement
    topbar_regex = r'(<div class="h-100 d-inline-flex align-items-center">\s*)(<a.*?)(?=\s*</div>)'
    if re.search(topbar_regex, content, flags=re.DOTALL):
        content = re.sub(topbar_regex, f'\\1{social_icons_topbar}', content, flags=re.DOTALL)
    
    # Footer Social Icons Replacement
    footer_regex = r'(<div class="d-flex pt-2">\s*)(<a.*?)(?=\s*</div>)'
    if re.search(footer_regex, content, flags=re.DOTALL):
        content = re.sub(footer_regex, f'\\1{social_icons_footer}', content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Successfully updated {filepath}")

if __name__ == "__main__":
    for file in files:
        update_file(file)
    print("\nSite-wide update complete.")
