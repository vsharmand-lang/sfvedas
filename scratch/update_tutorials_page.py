import os
import re
import ast

def main():
    file_path = r"c:\Users\vshar\OneDrive\Desktop\SFVedas_Website\sfvedas\tutorials\index.html"
    print(f"Reading {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Parse TUTORIALS list
    # Let's locate the TUTORIALS block:
    # const TUTORIALS = [ ... ];
    tutorials_match = re.search(r"const TUTORIALS = \[\s*([\s\S]*?)\s*\];", content)
    if not tutorials_match:
        print("Error: Could not find TUTORIALS array in index.html!")
        return

    tutorials_str = tutorials_match.group(1)
    
    # We can parse the individual lines of the TUTORIALS array to get objects
    tutorials = []
    # Each item looks like: {id:'ARCH-001',tag:'architecture',title:'If Salesforce Were Built Today — Would They Still Choose Multi-Tenant Architecture?',readTime:25,slug:'arch-001',available:true},
    # Let's parse each line using regex
    line_pattern = r"\{\s*id:\s*'(.*?)'\s*,\s*tag:\s*'(.*?)'\s*,\s*title:\s*'(.*?)'\s*,\s*readTime:\s*(\d+)\s*,\s*slug:\s*'(.*?)'\s*,\s*available:\s*(true|false)\s*\}"
    for line in tutorials_str.split("\n"):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        match = re.search(line_pattern, line)
        if match:
            tid, tag, title, read_time, slug, available = match.groups()
            tutorials.append({
                "id": tid,
                "tag": tag,
                "title": title.replace("\\'", "'"),
                "readTime": int(read_time),
                "slug": slug,
                "available": available == "true"
            })
            
    print(f"Parsed {len(tutorials)} tutorials from JS array.")

    # Let's define the Tag Labels mapping
    tag_labels = {
        'architecture': 'Architecture',
        'platform-technical': 'Platform & Technical',
        'integration-data': 'Integration & Data',
        'enterprise-strategy': 'Enterprise Strategy',
        'ai-future': 'AI & Future',
        'delivery-management': 'Delivery Management',
        'crm-comparison': 'CRM Comparison',
        'security-compliance': 'Security & Compliance',
        'licensing-commercial': 'Licensing & Commercial',
        'change-management': 'Change Management'
    }

    # 2. Build the noscript HTML block
    noscript_cards = []
    for t in tutorials:
        tag_label = tag_labels.get(t['tag'], t['tag'])
        meta = f"""
          <div class="card-meta">
            <span class="card-id">{t['id']}</span>
            <span class="card-tag">{tag_label}</span>
            <span class="card-read">{t['readTime']} min</span>
          </div>
          <h3 class="card-title">{t['title']}</h3>
          <div class="card-footer">
            <div class="card-author">
              <div class="author-avatar">VS</div>
              <span>Vishal Sharma</span>
            </div>
            {"<span class=\"card-link\">Read →</span>" if t['available'] else "<span class=\"card-soon\">Coming Soon</span>"}
          </div>"""
        
        if t['available']:
            card = f'        <a href="{t["slug"]}/" class="tutorial-card" data-tag="{t["tag"]}">{meta}\n        </a>'
        else:
            card = f'        <article class="tutorial-card card--coming-soon" data-tag="{t["tag"]}">{meta}\n        </article>'
        noscript_cards.append(card)

    noscript_html = f"""<div id="tutorialsGrid">
        <noscript>
          <div class="noscript-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px;">
{chr(10).join(noscript_cards)}
          </div>
        </noscript>
      </div>"""

    # Replace <div id="tutorialsGrid"></div> with the noscript fallback
    grid_pattern = r'<div id="tutorialsGrid">\s*</div>'
    if not re.search(grid_pattern, content):
        # Maybe it already has noscript or a different spacing
        print("Warning: Standard empty tutorialsGrid not found, let's look for any tutorialsGrid block")
        grid_pattern = r'<div id="tutorialsGrid">[\s\S]*?</div>'
        
    content = re.sub(grid_pattern, noscript_html, content)
    print("Injected <noscript> grid into index.html successfully.")

    # 3. Add History Synchronization logic and search load parameter logic to index.html JS
    # Let's locate applyFilters definition and insert updateURL() at its end
    # We want to insert the updateURL function and call it.
    
    # Let's see: we want to find the end of applyFilters. The function ends with grid.innerHTML = ... join(''); }
    apply_filters_end_pattern = r"(grid\.innerHTML = filtered\.map[\s\S]*?join\(''\);\s*\})"
    apply_filters_replacement = r"""\1

  function updateURL() {
    const params = new URLSearchParams();
    if (currentTag && currentTag !== 'all') {
      params.set('tag', currentTag);
    }
    if (currentSearch && currentSearch.trim() !== '') {
      params.set('search', currentSearch.trim());
    }
    const queryString = params.toString();
    const newUrl = queryString ? `?${queryString}` : window.location.pathname;
    history.replaceState(null, '', newUrl);
  }"""
    
    if "function updateURL()" not in content:
        content = re.sub(apply_filters_end_pattern, apply_filters_replacement, content)
        print("Injected updateURL() definition.")

    # Also, we should call updateURL() inside applyFilters() right before the final closing brace.
    # Wait, the end of applyFilters is:
    #     grid.innerHTML = filtered.map(t => { ... }).join('');
    #     updateURL();
    #   }
    # Let's find:
    #     grid.innerHTML = filtered.map(t => {
    #       ...
    #     }).join('');
    #   }
    
    # Let's do a replace for the end of the applyFilters function:
    # search:
    #     grid.innerHTML = filtered.map(t => {
    #       ...
    #     }).join('');
    #   }
    # replace with:
    #     grid.innerHTML = filtered.map(t => {
    #       ...
    #     }).join('');
    #     updateURL();
    #   }
    
    # To be extremely safe, let's look for:
    #     grid.innerHTML = filtered.map(t => {
    #       ...
    #     }).join('');
    #   }
    # and put updateURL() right before the closing brace of applyFilters.
    # In index.html, it is:
    #     grid.innerHTML = filtered.map(t => {
    #       ...
    #     }).join('');
    #   }
    
    # We can match:
    #     : `<article class="tutorial-card card--coming-soon" ${tag}>${meta}</article>`;
    #     }).join('');
    #   }
    
    target_end_apply = """: `<article class="tutorial-card card--coming-soon" ${tag}>${meta}</article>`;
    }).join('');
  }"""

    replacement_end_apply = """: `<article class="tutorial-card card--coming-soon" ${tag}>${meta}</article>`;
    }).join('');
    updateURL();
  }"""

    content = content.replace(target_end_apply, replacement_end_apply)
    print("Injected updateURL() call at the end of applyFilters().")

    # 4. Update the bottom section that handles initial parameters load to also support search parameters
    # The existing block:
    #   // Handle ?tag= URL parameter
    #   const urlTag = new URLSearchParams(window.location.search).get('tag');
    #   if (urlTag && urlTag !== 'all') {
    #     const matchBtn = document.querySelector(`.tut-filter[data-tag="${urlTag}"]`);
    #     if (matchBtn) {
    #       document.querySelectorAll('.tut-filter').forEach(b => b.classList.remove('active'));
    #       matchBtn.classList.add('active');
    #       currentTag = urlTag;
    #     }
    #   }
    #   applyFilters();
    
    url_param_pattern = r"// Handle \?tag= URL parameter[\s\S]*?applyFilters\(\);"
    url_param_replacement = """// Handle ?tag= and ?search= URL parameters on initial load
  const urlParams = new URLSearchParams(window.location.search);
  const urlTag = urlParams.get('tag');
  const urlSearch = urlParams.get('search');

  if (urlTag && urlTag !== 'all') {
    const matchBtn = document.querySelector(`.tut-filter[data-tag="${urlTag}"]`);
    if (matchBtn) {
      document.querySelectorAll('.tut-filter').forEach(b => b.classList.remove('active'));
      matchBtn.classList.add('active');
      currentTag = urlTag;
    }
  }
  if (urlSearch) {
    const searchInput = document.getElementById('tutorialSearch');
    if (searchInput) {
      searchInput.value = urlSearch;
      currentSearch = urlSearch;
    }
  }
  applyFilters();"""

    content = re.sub(url_param_pattern, url_param_replacement, content)
    print("Updated initial load URL parameter parsing logic.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote modified index.html!")

if __name__ == "__main__":
    main()
