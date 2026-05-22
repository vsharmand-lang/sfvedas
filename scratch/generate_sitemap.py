import os
import re
from datetime import datetime

def sort_key(folder_name):
    # Sort folders like ai-001, arch-010 alphabetically then numerically
    match = re.match(r"^([a-zA-Z]+)-(\d+)$", folder_name)
    if match:
        prefix, num = match.groups()
        return (prefix.lower(), int(num))
    return (folder_name.lower(), 0)

def generate():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tutorials_dir = os.path.join(base_dir, "tutorials")
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    
    # 1. Primary Pages
    primary_pages = [
        {"loc": "https://sfvedas.com/", "changefreq": "weekly", "priority": "1.0"},
        {"loc": "https://sfvedas.com/tutorials/", "changefreq": "daily", "priority": "0.9"},
        {"loc": "https://sfvedas.com/learning-paths/", "changefreq": "monthly", "priority": "0.8"},
        {"loc": "https://sfvedas.com/about/", "changefreq": "monthly", "priority": "0.7"},
        {"loc": "https://sfvedas.com/advertise/", "changefreq": "monthly", "priority": "0.5"},
    ]
    
    # 2. Scan Tutorials
    tutorial_folders = []
    for item in os.listdir(tutorials_dir):
        item_path = os.path.join(tutorials_dir, item)
        if os.path.isdir(item_path):
            index_path = os.path.join(item_path, "index.html")
            if os.path.exists(index_path):
                # Ensure it matches the typical tutorial pattern e.g., xxx-###
                if re.match(r"^[a-zA-Z]+-\d+$", item):
                    tutorial_folders.append(item)
                    
    # Sort tutorial folders
    tutorial_folders.sort(key=sort_key)
    
    # Current date in YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 3. Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    # Add primary pages
    for page in primary_pages:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{page['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{current_date}</lastmod>")
        xml_lines.append(f"    <changefreq>{page['changefreq']}</changefreq>")
        xml_lines.append(f"    <priority>{page['priority']}</priority>")
        xml_lines.append("  </url>")
        
    # Add tutorials
    for folder in tutorial_folders:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>https://sfvedas.com/tutorials/{folder}/</loc>")
        xml_lines.append(f"    <lastmod>{current_date}</lastmod>")
        xml_lines.append(f"    <changefreq>monthly</changefreq>")
        xml_lines.append(f"    <priority>0.8</priority>")
        xml_lines.append("  </url>")
        
    xml_lines.append("</urlset>")
    
    # Write to sitemap.xml
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")
        
    print(f"Successfully generated sitemap with {len(primary_pages) + len(tutorial_folders)} URLs (5 primary pages, {len(tutorial_folders)} tutorials).")

if __name__ == "__main__":
    generate()
