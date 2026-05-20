"""
Convert all tutorials to match ENT-002 structure exactly.
"""
import os
import re

TUTORIALS_DIR = os.path.join(os.path.dirname(__file__), 'tutorials')

AREA_MAP = {
    'arch': {'tag': 'architecture',         'name': 'Architecture',           'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',     'border': 'rgba(232,147,10,0.2)'},
    'plat': {'tag': 'platform-technical',   'name': 'Platform &amp; Technical','color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',     'border': 'rgba(0,112,210,0.2)'},
    'intg': {'tag': 'integration-data',     'name': 'Integration &amp; Data', 'color': 'rgba(45,125,82,0.08)',   'text': 'var(--sage-green)',  'border': 'rgba(45,125,82,0.2)'},
    'ent':  {'tag': 'enterprise-strategy',  'name': 'Enterprise Strategy',    'color': 'rgba(45,125,82,0.08)',   'text': 'var(--sage-green)',  'border': 'rgba(45,125,82,0.2)'},
    'ai':   {'tag': 'ai-future',            'name': 'AI &amp; Future',        'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',     'border': 'rgba(0,112,210,0.2)'},
    'del':  {'tag': 'delivery-management',  'name': 'Delivery Management',    'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',     'border': 'rgba(232,147,10,0.2)'},
    'crm':  {'tag': 'crm-comparison',       'name': 'CRM Comparison',         'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',     'border': 'rgba(0,112,210,0.2)'},
    'sec':  {'tag': 'security-compliance',  'name': 'Security &amp; Compliance','color':'rgba(229,62,62,0.08)',  'text': '#E53E3E',            'border': 'rgba(229,62,62,0.2)'},
    'rpt':  {'tag': 'reporting-analytics',  'name': 'Reporting &amp; Analytics','color':'rgba(45,125,82,0.08)', 'text': 'var(--sage-green)',  'border': 'rgba(45,125,82,0.2)'},
    'ind':  {'tag': 'industry-specific',    'name': 'Industry-Specific',      'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',     'border': 'rgba(232,147,10,0.2)'},
    'tal':  {'tag': 'team-talent',          'name': 'Team &amp; Talent',      'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',     'border': 'rgba(0,112,210,0.2)'},
    'lic':  {'tag': 'licensing-commercial', 'name': 'Licensing &amp; Commercial','color':'rgba(45,125,82,0.08)','text': 'var(--sage-green)',  'border': 'rgba(45,125,82,0.2)'},
    'cha':  {'tag': 'change-management',    'name': 'Change Management',      'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',     'border': 'rgba(232,147,10,0.2)'},
    'rfp':  {'tag': 'rfp',                  'name': 'RFP',                    'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',     'border': 'rgba(0,112,210,0.2)'},
}

STANDARD_NAV = """  <div class="reading-progress" id="readingProgress"></div>

  <nav class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="../index.html" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
      <ul class="nav-links">
        <li><a href="../index.html" class="nav-link">Home</a></li>
        <li><a href="../pages/tutorials.html" class="nav-link active">Tutorials</a></li>
        <li><a href="../pages/learning-paths.html" class="nav-link">Learning Paths</a></li>
        <li><a href="../pages/about.html" class="nav-link">About</a></li>
      </ul>
      <div class="nav-actions">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"><span class="theme-icon">☀</span></button>
        <button class="nav-hamburger" id="hamburger"><span></span><span></span><span></span></button>
      </div>
    </div>
    <div class="nav-mobile" id="navMobile">
      <a href="../index.html" class="nav-link">Home</a>
      <a href="../pages/tutorials.html" class="nav-link">Tutorials</a>
      <a href="../pages/learning-paths.html" class="nav-link">Learning Paths</a>
      <a href="../pages/about.html" class="nav-link">About</a>
    </div>
  </nav>"""

STANDARD_FOOTER = """  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="../index.html" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
          <p class="footer-tagline">Deep Salesforce Knowledge<br/>for Tech Leaders</p>
          <p class="footer-domain">sfvedas.com</p>
        </div>
        <div class="footer-links">
          <div class="footer-col"><h4>Learn</h4><a href="../pages/tutorials.html">All Tutorials</a><a href="../pages/learning-paths.html">Learning Paths</a></div>
          <div class="footer-col"><h4>About</h4><a href="../pages/about.html">Our Story</a></div>
          <div class="footer-col"><h4>Topics</h4><a href="../pages/tutorials.html">Architecture</a><a href="../pages/tutorials.html">Delivery</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 SFVedas · Vishal Sharma · sfvedas.com</p>
        <p class="footer-philosophy">Ancient wisdom. Modern Salesforce.</p>
      </div>
    </div>
  </footer>"""

STANDARD_JS = """  <script>
    function updateProgress() {
      const article = document.getElementById('tutorialContent');
      const bar = document.getElementById('readingProgress');
      const sidebar = document.getElementById('sidebarProgress');
      const pct = document.getElementById('progressPct');
      if (!article) return;
      const rect = article.getBoundingClientRect();
      const scrolled = Math.max(0, -rect.top);
      const total = article.offsetHeight - window.innerHeight;
      const progress = total > 0 ? Math.min(100, Math.round((scrolled / total) * 100)) : 0;
      if (bar) bar.style.width = progress + '%';
      if (sidebar) sidebar.style.width = progress + '%';
      if (pct) pct.textContent = progress + '%';
    }
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();

    function answer(el, questionId, result) {
      const question = document.getElementById(questionId);
      question.querySelectorAll('.quiz-option').forEach(opt => {
        opt.classList.remove('correct', 'incorrect');
        opt.style.pointerEvents = 'none';
      });
      el.classList.add(result === 'right' ? 'correct' : 'incorrect');
      if (result === 'wrong') {
        question.querySelectorAll('.quiz-option').forEach(opt => {
          if (opt.getAttribute('onclick') && opt.getAttribute('onclick').includes("'right'")) {
            opt.classList.add('correct');
          }
        });
      }
    }
  </script>
  <script src="../js/main.js"></script>"""

FONTS_BLOCK = """  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>"""


def strip_tags(html_fragment):
    return re.sub(r'<[^>]+>', '', html_fragment).strip()


def find_div_end(html, start):
    """Find position after the closing </div> that matches the <div> at start."""
    depth = 0
    i = start
    while i < len(html):
        o = html.find('<div', i)
        c = html.find('</div>', i)
        if c == -1:
            return len(html)
        if o != -1 and o < c:
            depth += 1
            i = o + 4
        else:
            if depth == 0:
                return c + 6
            depth -= 1
            i = c + 6
    return len(html)


# ── 1. Body tag ──────────────────────────────────────────────────────────────

def fix_body_tag(html):
    return re.sub(r'<body\b[^>]*>', '<body class="light-mode">', html)


# ── 2. Head: ensure Google Fonts ─────────────────────────────────────────────

def fix_head(html):
    if 'fonts.googleapis.com' in html:
        return html
    # Insert fonts before the main.css link (flexible spacing)
    html = re.sub(
        r'(\s*<link[^>]*href=["\']\.\.\/css\/main\.css["\'][^>]*>)',
        '\n' + FONTS_BLOCK + r'\1',
        html,
        count=1
    )
    return html


# ── 3. Nav + reading progress ────────────────────────────────────────────────

def replace_nav_and_progress(html):
    # Remove reading-progress-bar wrapper (plat- style) — consume both inner and outer closing tags
    html = re.sub(
        r'\s*<div class="reading-progress-bar">\s*<div class="reading-progress-fill"[^>]*></div>\s*</div>',
        '',
        html
    )
    # Remove single reading-progress div (arch- style already correct, but strip it so we re-add)
    html = re.sub(r'\s*<div class="reading-progress"[^>]*></div>', '', html)

    # Remove the entire nav element
    html = re.sub(r'\s*<nav\b[^>]*>.*?</nav>', '', html, count=1, flags=re.DOTALL)

    # Insert standard nav+progress right after <body ...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + STANDARD_NAV, html)
    return html


# ── 4. Header section ────────────────────────────────────────────────────────

def build_header_section(tut_id, area_meta, title, subtitle, read_time, audience, role):
    tag   = area_meta['tag']
    name  = area_meta['name']
    color = area_meta['color']
    tc    = area_meta['text']
    bc    = area_meta['border']
    return (
        '\n  <section style="background: var(--bg-secondary); border-bottom: 1px solid var(--border); padding: 56px 0 40px;">\n'
        '    <div class="container">\n'
        '      <div style="margin-bottom: 16px;">\n'
        f'        <a href="../pages/tutorials.html?tag={tag}" style="font-family:var(--font-ui);font-size:0.8rem;color:var(--sage-green);text-decoration:none;">← Back to {name}</a>\n'
        '      </div>\n'
        '      <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">\n'
        f'        <span class="card-id">{tut_id.upper()}</span>\n'
        f'        <span class="card-tag" style="background:{color};color:{tc};border-color:{bc};">{name}</span>\n'
        f'        <span class="card-read">{read_time} min read</span>\n'
        f'        <span style="font-family:var(--font-ui);font-size:0.78rem;color:var(--text-secondary);">{audience}</span>\n'
        '      </div>\n'
        '      <h1 style="font-family:var(--font-display);font-size:clamp(1.8rem,4vw,2.8rem);font-weight:700;color:var(--text-primary);line-height:1.2;max-width:820px;margin-bottom:16px;">\n'
        f'        {title}\n'
        '      </h1>\n'
        '      <p style="font-family:var(--font-body);font-size:1.05rem;color:var(--text-secondary);max-width:700px;line-height:1.75;margin-bottom:24px;">\n'
        f'        {subtitle}\n'
        '      </p>\n'
        '      <div style="display:flex;align-items:center;gap:12px;">\n'
        '        <div class="author-avatar" style="width:40px;height:40px;font-size:0.85rem;">VS</div>\n'
        '        <div>\n'
        '          <p style="font-family:var(--font-ui);font-size:0.85rem;font-weight:600;color:var(--text-primary);margin:0;">Vishal Sharma</p>\n'
        f'          <p style="font-family:var(--font-ui);font-size:0.75rem;color:var(--text-secondary);margin:0;">{role}</p>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '  </section>'
    )


def extract_header_fields(html, slug):
    prefix = slug.split('-')[0].lower()
    area_meta = AREA_MAP.get(prefix, AREA_MAP['arch'])

    # Tutorial ID
    tut_id = slug.upper()
    m = re.search(r'class="tutorial-id"[^>]*>([A-Z0-9-]+)</span>', html, re.IGNORECASE)
    if m:
        tut_id = m.group(1).strip()

    # Title - from h1 with inline style or class
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    title = strip_tags(m.group(1)).strip() if m else slug.replace('-', ' ').title()

    # Subtitle - p.tutorial-subtitle or first p with inline subtitle styling
    m = re.search(r'<p[^>]*class="tutorial-subtitle"[^>]*>(.*?)</p>', html, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<p style="[^"]*font-size:1\.05rem[^"]*color:var\(--text-secondary\)[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL | re.IGNORECASE)
    subtitle = strip_tags(m.group(1)).strip() if m else ''

    # Read time
    m = re.search(r'(\d+)\s*min\s*(?:read)?', html, re.IGNORECASE)
    read_time = m.group(1) if m else '20'

    # Audience
    audience = 'For: Salesforce Architects &amp; Tech Leaders'
    # arch- style
    m = re.search(r'For:\s*([^<"]+?)(?:</span>|<br|")', html, re.IGNORECASE)
    if m:
        audience = 'For: ' + m.group(1).strip()
    else:
        # plat- style: look for spans in tutorial-stats that aren't time/area
        stats_m = re.search(r'class="tutorial-stats"[^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
        if stats_m:
            spans = re.findall(r'<span>([^<]+)</span>', stats_m.group(1))
            non_time = [s for s in spans if not re.search(r'\d+\s*min', s, re.I)]
            if non_time:
                audience = 'For: ' + ' &amp; '.join(non_time)

    # Author role
    role = 'Salesforce Architecture Specialist · Updated May 2026'
    m = re.search(r'class="author-role"[^>]*>([^<]+)</span>', html, re.IGNORECASE)
    if m:
        role = m.group(1).strip()
    else:
        m = re.search(r'class="author-title"[^>]*>([^<]+)</div>', html, re.IGNORECASE)
        if m:
            role = m.group(1).strip()

    return tut_id, area_meta, title, subtitle, read_time, audience, role


def replace_header(html, slug):
    tut_id, area_meta, title, subtitle, read_time, audience, role = extract_header_fields(html, slug)

    # Remove <header ...>...</header>
    html = re.sub(r'\s*<header\b[^>]*>.*?</header>', '', html, count=1, flags=re.DOTALL)

    new_header = build_header_section(tut_id, area_meta, title, subtitle, read_time, audience, role)
    html = html.replace('</nav>', '</nav>' + new_header, 1)
    return html


# ── 5. Stat grid ─────────────────────────────────────────────────────────────

def fix_stat_grid(html):
    """Convert arch- stat-grid-section to ENT-002 tutorial-stat-grid section."""
    m = re.search(r'<div class="stat-grid-section">', html)
    if not m:
        return html

    section_start = m.start()
    section_end = find_div_end(html, section_start)
    section_html = html[section_start:section_end]

    # Extract each stat-card using depth-aware matching
    cards = []
    search_from = 0
    while True:
        cm = re.search(r'<div class="stat-card">', section_html[search_from:])
        if not cm:
            break
        card_abs_start = search_from + cm.start()
        card_abs_end = find_div_end(section_html, card_abs_start)
        card_html = section_html[card_abs_start:card_abs_end]

        vm = re.search(r'class="stat-value"[^>]*>(.*?)</div>', card_html, re.DOTALL)
        lm = re.search(r'class="stat-label"[^>]*>(.*?)</div>', card_html, re.DOTALL)
        val = strip_tags(vm.group(1)).strip() if vm else ''
        lab = strip_tags(lm.group(1)).strip() if lm else ''
        if val or lab:
            cards.append((val, lab))
        search_from = card_abs_end

    if not cards:
        # Remove the section entirely
        html = html[:section_start] + html[section_end:]
        return html

    cards_html = '\n'.join(
        f'        <div class="tutorial-stat-card">\n          <span class="tsn">{v}</span>\n          <span class="tsl">{l}</span>\n        </div>'
        for v, l in cards
    )
    new_section = (
        '\n  <section style="padding: 0; background: var(--bg-card); border-bottom: 1px solid var(--border);">\n'
        '    <div class="container">\n'
        '      <div class="tutorial-stat-grid" style="padding: 24px 0;">\n'
        + cards_html + '\n'
        '      </div>\n'
        '    </div>\n'
        '  </section>'
    )
    html = html[:section_start] + new_section + html[section_end:]
    return html


# ── 6. Layout wrapper ────────────────────────────────────────────────────────

def fix_layout_wrapper(html):
    """Wrap tutorial-layout in .container if not already, fix article class/id."""
    # plat- style: <div class="tutorial-layout" id="tutorialContent">
    # Replace with <div class="container">\n    <div class="tutorial-layout">
    if re.search(r'<div class="tutorial-layout" id="tutorialContent">', html):
        html = html.replace(
            '<div class="tutorial-layout" id="tutorialContent">',
            '<div class="container">\n    <div class="tutorial-layout">'
        )
        # Add closing </div> for the container before <footer
        html = re.sub(
            r'(</article>\s*</aside>\s*</div>)(\s*(?=<footer|\s*<footer))',
            r'\1\n  </div>\2',
            html,
            count=1,
            flags=re.DOTALL
        )

    # tutorial-article -> tutorial-body
    html = re.sub(r'class="tutorial-article"', 'class="tutorial-body"', html)

    # Ensure article has id="tutorialContent"
    html = re.sub(
        r'<article class="tutorial-body"(?! id=)',
        '<article class="tutorial-body" id="tutorialContent"',
        html
    )
    return html


# ── 7. Section summary ───────────────────────────────────────────────────────

def fix_section_summary(html):
    html = re.sub(r'<h2 class="section-summary-title"[^>]*>(.*?)</h2>', r'<span class="ss-label">\1</span>', html, flags=re.DOTALL)
    html = re.sub(r'<ul class="section-summary-list">', '<ul>', html)
    return html


# ── 8. Callouts ──────────────────────────────────────────────────────────────

EMOJI_MAP = {
    'callout--insight': '\U0001f4a1',
    'callout--key':     '\U0001f511',
    'callout--tip':     '✅',
    'callout--warning': '⚠️',
}

def fix_callouts(html):
    """Convert plat- callout (callout-title + bare p) to ENT-002 style."""
    def replace_callout(m):
        full = m.group(0)
        # Already in ENT-002 style
        if 'callout-icon' in full or 'callout-body' in full:
            return full
        cls_m = re.search(r'class="callout (callout--\w+)"', full)
        cls = cls_m.group(1) if cls_m else 'callout--key'
        emoji = EMOJI_MAP.get(cls, '\U0001f511')
        title_m = re.search(r'<div class="callout-title"[^>]*>(.*?)</div>', full, re.DOTALL)
        title = strip_tags(title_m.group(1)).strip() if title_m else ''
        paras = re.findall(r'<p>(.*?)</p>', full, re.DOTALL)
        para_html = '\n            '.join(f'<p>{p}</p>' for p in paras)
        indent = '          '
        return (
            f'<div class="callout {cls}">\n'
            f'{indent}  <div class="callout-icon">{emoji}</div>\n'
            f'{indent}  <div class="callout-body">\n'
            f'{indent}    <strong>{title}</strong>\n'
            f'{indent}    {para_html}\n'
            f'{indent}  </div>\n'
            f'{indent}</div>'
        )

    html = re.sub(
        r'<div class="callout callout--\w+">\s*<div class="callout-title">.*?</div>.*?</div>',
        replace_callout,
        html,
        flags=re.DOTALL
    )
    return html


# ── 9. Key takeaways ─────────────────────────────────────────────────────────

def fix_key_takeaways(html):
    html = re.sub(r'<h3 class="key-takeaways-title"[^>]*>(.*?)</h3>', r'<h2>\1</h2>', html, flags=re.DOTALL)
    html = re.sub(r'<ul class="key-takeaways-list">', '<ul>', html)
    return html


# ── 10. Quiz ─────────────────────────────────────────────────────────────────

def fix_quiz(html):
    html = re.sub(r'<h3 class="quiz-title"[^>]*>(.*?)</h3>', r'<h2>\1</h2>', html, flags=re.DOTALL)
    html = re.sub(r'<p class="quiz-question-text"[^>]*>(.*?)</p>', r'<p>\1</p>', html, flags=re.DOTALL)
    html = re.sub(r'\s*<div class="quiz-feedback"[^>]*>[^<]*</div>', '', html)
    html = re.sub(r'<div class="quiz-section"(?! id)', '<div class="quiz-section" id="quiz"', html)
    return html


# ── 11. Related tutorials ────────────────────────────────────────────────────

def fix_related_tutorials(html):
    # Standardise heading
    html = re.sub(
        r'<h[23][^>]*class="related[^"]*"[^>]*>.*?</h[23]>',
        '<h2>Continue Reading</h2>',
        html, flags=re.DOTALL
    )
    # Fix individual related cards
    def fix_card(m):
        full = m.group(0)
        href_m = re.search(r'href="([^"]+)"', full)
        href = href_m.group(1) if href_m else '#'
        id_m = re.search(r'([\w]+-\d+)\.html', href)
        card_id = id_m.group(1).upper() if id_m else ''

        # plat- style: div.related-card-tag + div.related-card-title
        title_m = re.search(r'class="related-card-title"[^>]*>(.*?)</div>', full, re.DOTALL)
        if title_m:
            title = strip_tags(title_m.group(1)).strip()
            return f'<a href="{href}" class="related-card">\n              <span class="card-id">{card_id}</span>\n              <h4>{title}</h4>\n            </a>'

        # arch- style: span.related-area + span.related-title
        title_m2 = re.search(r'class="related-title"[^>]*>(.*?)</span>', full, re.DOTALL)
        if title_m2:
            title = strip_tags(title_m2.group(1)).strip()
            return f'<a href="{href}" class="related-card">\n              <span class="card-id">{card_id}</span>\n              <h4>{title}</h4>\n            </a>'

        # already ENT-002 style (has card-id + h4)
        return full

    html = re.sub(r'<a href="[^"]*" class="related-card">.*?</a>', fix_card, html, flags=re.DOTALL)
    return html


# ── 12. Sidebar ──────────────────────────────────────────────────────────────

def fix_sidebar(html):
    # Convert plat- sidebar-card divs to proper sidebar components
    def replace_sidebar_card(m):
        inner = m.group(1)
        # Extract card title
        title_m = re.search(r'class="sidebar-card-title"[^>]*>(.*?)</h3>', inner, re.DOTALL)
        title = strip_tags(title_m.group(1)).strip() if title_m else ''

        if 'Table of Contents' in title or 'Contents' in title:
            items = re.findall(r'href="([^"]*)"[^>]*class="toc-item"[^>]*>(.*?)</a>', inner, re.DOTALL)
            if not items:
                items = re.findall(r'class="toc-item"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', inner, re.DOTALL)
            li_html = '\n'.join(
                f'            <li><a href="{h}">{strip_tags(t).strip()}</a></li>'
                for h, t in items
            )
            return f'<div class="sidebar-toc">\n          <h4>In This Tutorial</h4>\n          <ul class="toc-list">\n{li_html}\n          </ul>\n        </div>'

        if 'Progress' in title or 'Reading' in title:
            return ('<div class="sidebar-progress">\n'
                    '          <h4>Reading Progress</h4>\n'
                    '          <div class="progress-track"><div class="progress-fill" id="sidebarProgress"></div></div>\n'
                    '          <span class="progress-pct" id="progressPct">0%</span>\n'
                    '        </div>')

        # Generic: keep as sidebar-download
        content_clean = re.sub(r'<h3 class="sidebar-card-title"[^>]*>.*?</h3>', '', inner, flags=re.DOTALL).strip()
        return f'<div class="sidebar-download">\n          <h4>{title}</h4>\n          {content_clean}\n        </div>'

    html = re.sub(
        r'<div class="sidebar-card">(.*?)</div>(?=\s*(?:<div class="sidebar-card"|<div class="sidebar-cta"|</aside>))',
        replace_sidebar_card,
        html,
        flags=re.DOTALL
    )

    # Fix sidebar h3 -> h4 in sidebar-toc/progress/download
    for cls in ('sidebar-toc', 'sidebar-progress', 'sidebar-download'):
        pat = re.compile(r'(<div class="' + cls + r'".*?)(</div>)', re.DOTALL)
        def fix_h(m, c=cls):
            inner = m.group(1)
            inner = re.sub(r'<h3\b', '<h4', inner)
            inner = re.sub(r'</h3>', '</h4>', inner)
            return inner + m.group(2)
        html = pat.sub(fix_h, html)

    # sidebar-cta: h3->h4, fix CTA button class
    html = re.sub(r'(<div class="sidebar-cta".*?)<h3\b', r'\1<h4', html, flags=re.DOTALL)
    html = re.sub(r'(<div class="sidebar-cta".*?)</h3>', r'\1</h4>', html, flags=re.DOTALL)
    html = re.sub(r'class="btn-cta"', 'class="btn btn-primary" style="width:100%;text-align:center;display:block;"', html)
    html = re.sub(r'class="sidebar-cta-btn"', 'class="btn btn-primary" style="width:100%;text-align:center;display:block;"', html)
    html = re.sub(r'class="sidebar-cta-title"', 'class="sidebar-cta-title"', html)  # no-op, already handled by h4

    # progress-bar-container/fill -> progress-track/fill  and id fixes
    html = re.sub(r'class="progress-bar-container"', 'class="progress-track"', html)
    html = re.sub(r'class="progress-bar-fill" id="sidebarProgress"', 'class="progress-fill" id="sidebarProgress"', html)
    html = re.sub(r'class="progress-bar-fill"', 'class="progress-fill"', html)
    html = re.sub(r'id="progressLabel"', 'id="progressPct"', html)
    html = re.sub(r'class="progress-label"', 'class="progress-pct"', html)

    # Ensure sidebarProgress id exists in progress-track
    if 'id="sidebarProgress"' not in html and 'progress-track' in html:
        html = re.sub(
            r'class="progress-fill"(?! id=)',
            'class="progress-fill" id="sidebarProgress"',
            html,
            count=1
        )
    return html


# ── 13. Footer ───────────────────────────────────────────────────────────────

def replace_footer(html):
    html = re.sub(r'<footer\b[^>]*>.*?</footer>', STANDARD_FOOTER, html, flags=re.DOTALL)
    return html


# ── 14. JS ───────────────────────────────────────────────────────────────────

def replace_js(html):
    html = re.sub(r'\s*<script(?! src)[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'\s*<script src="[^"]*main\.js"[^>]*></script>', '', html)
    html = html.replace('</body>', STANDARD_JS + '\n</body>')
    return html


# ── 15. Code blocks ──────────────────────────────────────────────────────────

def fix_code_blocks(html):
    # Unwrap <div class="code-block"> around <pre>
    html = re.sub(r'<div class="code-block">\s*(<pre)', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'(</pre>)\s*</div>', r'\1', html, flags=re.DOTALL)
    return html


# ── Main ─────────────────────────────────────────────────────────────────────

def process_file(filepath, slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = fix_body_tag(html)
    html = fix_head(html)
    html = replace_nav_and_progress(html)
    html = replace_header(html, slug)
    html = fix_stat_grid(html)
    html = fix_layout_wrapper(html)
    html = fix_section_summary(html)
    html = fix_callouts(html)
    html = fix_key_takeaways(html)
    html = fix_quiz(html)
    html = fix_related_tutorials(html)
    html = fix_sidebar(html)
    html = replace_footer(html)
    html = replace_js(html)
    html = fix_code_blocks(html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    files = sorted(f for f in os.listdir(TUTORIALS_DIR) if f.endswith('.html') and f != 'ent-002.html')
    print(f"Processing {len(files)} files...")
    ok = errors = 0
    for fname in files:
        slug = fname.replace('.html', '')
        try:
            process_file(os.path.join(TUTORIALS_DIR, fname), slug)
            print(f"  OK  {fname}")
            ok += 1
        except Exception as e:
            print(f"  ERR {fname}: {e}")
            import traceback; traceback.print_exc()
            errors += 1
    print(f"\nDone: {ok} OK, {errors} errors")


if __name__ == '__main__':
    main()
