#!/usr/bin/env python3
"""
Rename all HTML files to lowercase, space-free, hyphenated names.
Update all internal links across the project.
"""

import os
import glob
import re

# Define exact mapping: old_name -> new_name
FILE_MAP = {
    "a-frame-signs.html": "a-frame-signs.html",
    "about-us.html": "about-us.html",
    "aluminium-signs.html": "aluminium-signs.html",
    "banner-flags.html": "banner-flags.html",
    "contact-us.html": "contact-us.html",
    "corflute-signs.html": "corflute-signs.html",
    "corporate-signage.html": "corporate-signage.html",
    "cut-vinyl-graphics.html": "cut-vinyl-graphics.html",
    "index.html": "index.html",
    "large-format-printing.html": "large-format-printing.html",
    "marketing-menu-signs.html": "marketing-menu-signs.html",
    "our-portfolio.html": "our-portfolio.html",
    "stickers-labels.html": "stickers-labels.html",
    "vehicle-signage.html": "vehicle-signage.html",
    "vinyl-mesh-banners.html": "vinyl-mesh-banners.html",
    "window-signs.html": "window-signs.html",
}

# Also map lowercase versions just in case some links use inconsistent casing
LOWER_MAP = {}
for old, new in FILE_MAP.items():
    LOWER_MAP[old.lower()] = new

# Reverse sorted by length (longest first) to avoid partial replacements
OLD_NAMES_SORTED = sorted(FILE_MAP.keys(), key=len, reverse=True)

def get_all_files():
    """Get all HTML and Python files in root directory."""
    files = []
    files.extend(glob.glob("*.HTML"))
    files.extend(glob.glob("*.html"))
    files.extend(glob.glob("*.py"))
    return files

def update_content(content):
    """Replace all internal file references in content."""
    updated = content
    # Replace exact old names
    for old_name in OLD_NAMES_SORTED:
        new_name = FILE_MAP[old_name]
        updated = updated.replace(old_name, new_name)
    # Also replace lowercase versions (safety net)
    for old_lower, new_name in LOWER_MAP.items():
        updated = updated.replace(old_lower, new_name)
    return updated

def main():
    os.chdir("/Users/suryateja/Downloads/AUSWEBSITE")
    
    all_files = get_all_files()
    print(f"Found {len(all_files)} files to process.")
    
    # Step 1: Read and update content for HTML files, write to new names
    for old_name, new_name in FILE_MAP.items():
        if not os.path.exists(old_name):
            print(f"WARNING: {old_name} not found, skipping.")
            continue
        
        with open(old_name, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated_content = update_content(content)
        
        with open(new_name, "w", encoding="utf-8") as f:
            f.write(updated_content)
        
        print(f"Created: {new_name} (from {old_name})")
    
    # Step 2: Update non-HTML files (Python scripts) that reference old names
    other_files = [f for f in all_files if not f.endswith(".HTML") and not f.endswith(".html")]
    for filename in other_files:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated_content = update_content(content)
        
        if updated_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated links in: {filename}")
        else:
            print(f"No changes needed in: {filename}")
    
    # Step 3: Remove old HTML files
    for old_name in FILE_MAP.keys():
        if os.path.exists(old_name):
            os.remove(old_name)
            print(f"Removed: {old_name}")
    
    print("\nDone! Updated file structure:")
    for f in sorted(os.listdir(".")):
        if os.path.isfile(f):
            print(f"  {f}")

if __name__ == "__main__":
    main()
