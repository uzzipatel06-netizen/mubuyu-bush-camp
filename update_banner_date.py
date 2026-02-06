import os
import glob

def update_banner_date():
    # Target phrase
    target = "seasonal break until April"
    replacement = "seasonal break until March"
    
    # Get all HTML files
    html_files = glob.glob("*.html")
    
    updated_files = []
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            new_content = content.replace(target, replacement)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            updated_files.append(file_path)
            print(f"Updated: {file_path}")
        else:
            print(f"Skipped (target not found): {file_path}")

    print(f"\nTotal files updated: {len(updated_files)}")

if __name__ == "__main__":
    update_banner_date()
