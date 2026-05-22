import os
import re

def clean_file(file_path):
    print(f"Checking {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the pattern to search for
    # We want to match:
    #     const saved = localStorage.getItem('sfvedas-theme');
    #     if (saved === 'dark') document.body.classList.add('dark');
    #     document.getElementById('themeToggle').addEventListener('click', () => {
    #       document.body.classList.toggle('dark');
    #       localStorage.setItem('sfvedas-theme', document.body.classList.contains('dark') ? 'dark' : 'light');
    #     });
    pattern = r"\s*const saved = localStorage\.getItem\('sfvedas-theme'\);[\s\S]*?localStorage\.setItem\('sfvedas-theme',\s*document\.body\.classList\.contains\('dark'\)\s*\?\s*'dark'\s*:\s*'light'\);\s*\}\);"
    
    match = re.search(pattern, content)
    if match:
        print(f"Found match in {file_path}:")
        print(match.group(0))
        cleaned_content = re.sub(pattern, "", content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        print(f"Successfully cleaned {file_path}")
        return True
    else:
        print(f"No match found in {file_path}")
        return False

def main():
    base_dir = r"c:\Users\vshar\OneDrive\Desktop\SFVedas_Website\sfvedas\tutorials"
    
    # 22 targets: ai-001 to ai-010, ent-012 to ent-023
    folders = []
    for i in range(1, 11):
        folders.append(f"ai-{i:03d}")
    for i in range(12, 24):
        folders.append(f"ent-{i:03d}")
        
    cleaned_count = 0
    for folder in folders:
        file_path = os.path.join(base_dir, folder, "index.html")
        if os.path.exists(file_path):
            if clean_file(file_path):
                cleaned_count += 1
        else:
            print(f"Warning: Path does not exist: {file_path}")
            
    print(f"\nDone! Cleaned {cleaned_count} files.")

if __name__ == "__main__":
    main()
