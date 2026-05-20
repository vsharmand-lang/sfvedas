"""
Idempotent fix: clean up all tutorials to exactly match ENT-002 structure.
Handles files in any state (original, partially converted, or double-converted).
"""
import os
import re

TUTORIALS_DIR = os.path.join(os.path.dirname(__file__), 'tutorials')

AREA_MAP = {
    'arch': {'tag': 'architecture',            'name': 'Architecture',             'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',    'border': 'rgba(232,147,10,0.2)'},
    'plat': {'tag': 'platform-technical',      'name': 'Platform &amp; Technical', 'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',    'border': 'rgba(0,112,210,0.2)'},
    'intg': {'tag': 'integration-data',        'name': 'Integration &amp; Data',   'color': 'rgba(45,125,82,0.08)',   'text': 'var(--sage-green)', 'border': 'rgba(45,125,82,0.2)'},
    'ent':  {'tag': 'enterprise-strategy',     'name': 'Enterprise Strategy',      'color': 'rgba(45,125,82,0.08)',   'text': 'var(--sage-green)', 'border': 'rgba(45,125,82,0.2)'},
    'ai':   {'tag': 'ai-future',               'name': 'AI &amp; Future',          'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',    'border': 'rgba(0,112,210,0.2)'},
    'del':  {'tag': 'delivery-management',     'name': 'Delivery Management',      'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',    'border': 'rgba(232,147,10,0.2)'},
    'crm':  {'tag': 'crm-comparison',          'name': 'CRM Comparison',           'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',    'border': 'rgba(0,112,210,0.2)'},
    'sec':  {'tag': 'security-compliance',     'name': 'Security &amp; Compliance','color': 'rgba(229,62,62,0.08)',  'text': '#E53E3E',           'border': 'rgba(229,62,62,0.2)'},
    'rpt':  {'tag': 'reporting-analytics',     'name': 'Reporting &amp; Analytics','color': 'rgba(45,125,82,0.08)',  'text': 'var(--sage-green)', 'border': 'rgba(45,125,82,0.2)'},
    'ind':  {'tag': 'industry-specific',       'name': 'Industry-Specific',        'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',    'border': 'rgba(232,147,10,0.2)'},
    'tal':  {'tag': 'team-talent',             'name': 'Team &amp; Talent',        'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',    'border': 'rgba(0,112,210,0.2)'},
    'lic':  {'tag': 'licensing-commercial',    'name': 'Licensing &amp; Commercial','color': 'rgba(45,125,82,0.08)', 'text': 'var(--sage-green)', 'border': 'rgba(45,125,82,0.2)'},
    'cha':  {'tag': 'change-management',       'name': 'Change Management',        'color': 'rgba(232,147,10,0.08)',  'text': 'var(--saffron)',    'border': 'rgba(232,147,10,0.2)'},
    'rfp':  {'tag': 'rfp',                     'name': 'RFP',                      'color': 'rgba(0,112,210,0.08)',   'text': 'var(--sf-blue)',    'border': 'rgba(0,112,210,0.2)'},
}

AREA_CTA = {
    'arch': ('Master Salesforce Architecture',
             'One of 27 architecture deep-dives — built for architects and senior tech leaders.',
             '../pages/tutorials.html?tag=architecture', 'View All Architecture Tutorials →'),
    'plat': ('Platform & Technical Mastery',
             'Deep dives into Salesforce platform internals, APIs, and technical patterns.',
             '../pages/tutorials.html?tag=platform-technical', 'View All Platform Tutorials →'),
    'intg': ('Integration & Data Expertise',
             'Master Salesforce integration patterns and data architecture.',
             '../pages/tutorials.html?tag=integration-data', 'View All Integration Tutorials →'),
    'ent':  ('Enterprise Strategy',
             'Strategic Salesforce decision-making for senior leaders.',
             '../pages/tutorials.html?tag=enterprise-strategy', 'View All Strategy Tutorials →'),
    'ai':   ('AI & Future Readiness',
             'Stay ahead of AI and emerging Salesforce capabilities.',
             '../pages/tutorials.html?tag=ai-future', 'View All AI Tutorials →'),
    'del':  ('Delivery Excellence',
             'Master Salesforce delivery from planning to go-live.',
             '../pages/tutorials.html?tag=delivery-management', 'View All Delivery Tutorials →'),
    'crm':  ('CRM Strategy & Comparison',
             'Make informed CRM platform decisions with expert analysis.',
             '../pages/tutorials.html?tag=crm-comparison', 'View All CRM Tutorials →'),
    'sec':  ('Security & Compliance',
             'Protect your Salesforce org and meet compliance requirements.',
             '../pages/tutorials.html?tag=security-compliance', 'View All Security Tutorials →'),
    'rpt':  ('Reporting & Analytics',
             'Turn Salesforce data into strategic business insights.',
             '../pages/tutorials.html?tag=reporting-analytics', 'View All Reporting Tutorials →'),
    'ind':  ('Industry-Specific Expertise',
             'Salesforce implementation patterns by industry vertical.',
             '../pages/tutorials.html?tag=industry-specific', 'View All Industry Tutorials →'),
    'tal':  ('Team & Talent',
             'Build and lead high-performing Salesforce teams.',
             '../pages/tutorials.html?tag=team-talent', 'View All Team Tutorials →'),
    'lic':  ('Licensing & Commercial',
             'Optimise Salesforce licensing costs and commercial terms.',
             '../pages/tutorials.html?tag=licensing-commercial', 'View All Licensing Tutorials →'),
    'cha':  ('Change Management',
             'Drive adoption and manage change on Salesforce programmes.',
             '../pages/tutorials.html?tag=change-management', 'View All Change Tutorials →'),
    'rfp':  ('RFP Excellence',
             'Craft and evaluate Salesforce RFPs with confidence.',
             '../pages/tutorials.html?tag=rfp', 'View All RFP Tutorials →'),
}

def st(s):
    return re.sub(r'<[^>]+>', '', s).strip()

def find_div_end(html, start):
    """Return the index just after the </div> that closes the <div at `start`."""
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
            depth -= 1
            if depth == 0:
                return c + 6
            i = c + 6
    return len(html)

# ─── Standard blocks ────────────────────────────────────────────────────────

FONTS = ('  <link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>')

NAV = ('  <div class="reading-progress" id="readingProgress"></div>\n\n'
       '  <nav class="navbar" id="navbar">\n'
       '    <div class="nav-inner">\n'
       '      <a href="../index.html" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>\n'
       '      <ul class="nav-links">\n'
       '        <li><a href="../index.html" class="nav-link">Home</a></li>\n'
       '        <li><a href="../pages/tutorials.html" class="nav-link active">Tutorials</a></li>\n'
       '        <li><a href="../pages/learning-paths.html" class="nav-link">Learning Paths</a></li>\n'
       '        <li><a href="../pages/about.html" class="nav-link">About</a></li>\n'
       '      </ul>\n'
       '      <div class="nav-actions">\n'
       '        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"><span class="theme-icon">☀</span></button>\n'
       '        <button class="nav-hamburger" id="hamburger"><span></span><span></span><span></span></button>\n'
       '      </div>\n'
       '    </div>\n'
       '    <div class="nav-mobile" id="navMobile">\n'
       '      <a href="../index.html" class="nav-link">Home</a>\n'
       '      <a href="../pages/tutorials.html" class="nav-link">Tutorials</a>\n'
       '      <a href="../pages/learning-paths.html" class="nav-link">Learning Paths</a>\n'
       '      <a href="../pages/about.html" class="nav-link">About</a>\n'
       '    </div>\n'
       '  </nav>')

FOOTER = ('  <footer class="footer">\n'
          '    <div class="container">\n'
          '      <div class="footer-inner">\n'
          '        <div class="footer-brand">\n'
          '          <a href="../index.html" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>\n'
          '          <p class="footer-tagline">Deep Salesforce Knowledge<br/>for Tech Leaders</p>\n'
          '          <p class="footer-domain">sfvedas.com</p>\n'
          '        </div>\n'
          '        <div class="footer-links">\n'
          '          <div class="footer-col"><h4>Learn</h4><a href="../pages/tutorials.html">All Tutorials</a><a href="../pages/learning-paths.html">Learning Paths</a></div>\n'
          '          <div class="footer-col"><h4>About</h4><a href="../pages/about.html">Our Story</a></div>\n'
          '          <div class="footer-col"><h4>Topics</h4><a href="../pages/tutorials.html">Architecture</a><a href="../pages/tutorials.html">Delivery</a></div>\n'
          '        </div>\n'
          '      </div>\n'
          '      <div class="footer-bottom">\n'
          '        <p>© 2026 SFVedas · Vishal Sharma · sfvedas.com</p>\n'
          '        <p class="footer-philosophy">Ancient wisdom. Modern Salesforce.</p>\n'
          '      </div>\n'
          '    </div>\n'
          '  </footer>')

JS = ('  <script>\n'
      '    function updateProgress() {\n'
      '      const article = document.getElementById(\'tutorialContent\');\n'
      '      const bar = document.getElementById(\'readingProgress\');\n'
      '      const sidebar = document.getElementById(\'sidebarProgress\');\n'
      '      const pct = document.getElementById(\'progressPct\');\n'
      '      if (!article) return;\n'
      '      const rect = article.getBoundingClientRect();\n'
      '      const scrolled = Math.max(0, -rect.top);\n'
      '      const total = article.offsetHeight - window.innerHeight;\n'
      '      const progress = total > 0 ? Math.min(100, Math.round((scrolled / total) * 100)) : 0;\n'
      '      if (bar) bar.style.width = progress + \'%\';\n'
      '      if (sidebar) sidebar.style.width = progress + \'%\';\n'
      '      if (pct) pct.textContent = progress + \'%\';\n'
      '    }\n'
      '    window.addEventListener(\'scroll\', updateProgress, { passive: true });\n'
      '    updateProgress();\n\n'
      '    function answer(el, questionId, result) {\n'
      '      const question = document.getElementById(questionId);\n'
      '      question.querySelectorAll(\'.quiz-option\').forEach(opt => {\n'
      '        opt.classList.remove(\'correct\', \'incorrect\');\n'
      '        opt.style.pointerEvents = \'none\';\n'
      '      });\n'
      '      el.classList.add(result === \'right\' ? \'correct\' : \'incorrect\');\n'
      '      if (result === \'wrong\') {\n'
      '        question.querySelectorAll(\'.quiz-option\').forEach(opt => {\n'
      '          if (opt.getAttribute(\'onclick\') && opt.getAttribute(\'onclick\').includes("\'right\'")) {\n'
      '            opt.classList.add(\'correct\');\n'
      '          }\n'
      '        });\n'
      '      }\n'
      '    }\n'
      '  </script>\n'
      '  <script src="../js/main.js"></script>')

# ─── Step 1: extract tutorial metadata from the page ────────────────────────

def extract_meta(html, slug):
    prefix = slug.split('-')[0].lower()
    am = AREA_MAP.get(prefix, AREA_MAP['arch'])

    tut_id = slug.upper()

    tm = re.search(r'<title>(.*?)(?:\s*[|—–]\s*SFVedas)?\s*</title>', html, re.IGNORECASE | re.DOTALL)
    title = st(tm.group(1)).strip() if tm else slug.replace('-', ' ').title()
    title = re.sub(r'^[A-Z]+-\d+[\s:—–-]+', '', title).strip()
    title = re.sub(r'\s*[—–]\s*SFVedas\s*$', '', title, flags=re.IGNORECASE).strip()

    sm = re.search(r'<p style="font-family:var\(--font-body\)[^"]*color:var\(--text-secondary\)[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL)
    subtitle = st(sm.group(1)).strip() if sm else ''

    rm = re.search(r'(\d+)\s*min\s*read', html, re.IGNORECASE)
    read_time = rm.group(1) if rm else '20'

    audience = 'For: Salesforce Architects &amp; Tech Leaders'
    fm = re.search(r'For:\s*([^<"&]+?)(?:</span>|&amp;|")', html, re.IGNORECASE)
    if fm:
        raw = fm.group(1).strip()
        if not any(k in raw for k in ('Architecture', 'Platform', 'Integration', 'Enterprise', 'Delivery', 'AI')):
            audience = 'For: ' + raw

    role = 'Salesforce Architecture Specialist · Updated May 2026'

    return tut_id, am, title, subtitle, read_time, audience, role


# ─── Step 2: isolate the main content block ──────────────────────────────────

def isolate_body_content(html):
    layout_m = re.search(r'<div class="(container|tutorial-layout|tut-body)"', html)
    if not layout_m:
        return None, None, None

    container_m = re.search(r'<div class="container">\s*<div class="tutorial-layout">', html)
    if container_m:
        layout_start = container_m.start()
    else:
        tlm = re.search(r'<div class="tutorial-layout"', html)
        if tlm:
            layout_start = tlm.start()
        else:
            tbm = re.search(r'<div class="tut-body"', html)
            if tbm:
                layout_start = tbm.start()
            else:
                return None, None, None

    layout_end = find_div_end(html, layout_start)

    footer_m_full = re.search(r'<footer\b', html)
    if footer_m_full:
        footer_pos = footer_m_full.start()
        if layout_end >= footer_pos:
            # find_div_end over-ran past the footer (e.g. due to <div inside <pre><code> blocks)
            # Fall back: the real container close is the last </div> before <footer>
            pre_footer = html[:footer_pos].rstrip()
            last_close = pre_footer.rfind('</div>')
            layout_end = (last_close + 6) if last_close != -1 else footer_pos
        content_end = footer_pos
    else:
        content_end = layout_end

    return layout_start, content_end, html[layout_start:content_end]


# ─── Quiz section rebuilder ───────────────────────────────────────────────────

def _short_title(title, max_len=50):
    if len(title) <= max_len:
        return title
    for sep in [':', '—', '–', ' - ']:
        idx = title.find(sep)
        if 0 < idx <= max_len:
            return title[:idx].strip()
    return title[:max_len - 1].strip() + '…'


def rebuild_quiz_section(body_html):
    """Atomically extract and rebuild the quiz section, correcting nesting issues."""
    qs_m = re.search(r'<div class="quiz-section"[^>]*>', body_html)
    if not qs_m:
        return body_html

    qs_start = qs_m.start()
    qs_end = find_div_end(body_html, qs_start)
    qs_block = body_html[qs_start:qs_end]

    # Extract heading
    heading = 'Check Your Understanding'
    hm = re.search(r'<h2>(.*?)</h2>', qs_block, re.DOTALL)
    if hm:
        heading = hm.group(1).strip()

    # Collect ordered, deduplicated question IDs
    q_ids = []
    seen = set()
    for m in re.finditer(r'<div class="quiz-question" id="(q\d+)"', qs_block):
        qid = m.group(1)
        if qid not in seen:
            seen.add(qid)
            q_ids.append(qid)

    # For each question: extract text from its <p>, options by onclick qid
    questions_data = []
    for q_id in q_ids:
        qm2 = re.search(r'<div class="quiz-question" id="' + re.escape(q_id) + r'"', qs_block)
        if not qm2:
            continue
        pm = re.search(r'<p>(.*?)</p>', qs_block[qm2.start():], re.DOTALL)
        q_text = pm.group(1).strip() if pm else ''

        options = []
        for om in re.finditer(r'<div class="quiz-option"([^>]*)>(.*?)</div>', qs_block, re.DOTALL):
            attrs = om.group(1)
            text = om.group(2).strip()
            if f"'{q_id}'" in attrs:
                options.append((attrs, text))

        questions_data.append((q_id, q_text, options))

    # Rebuild cleanly
    out = f'<div class="quiz-section" id="quiz">\n      <h2>{heading}</h2>'
    for q_id, q_text, options in questions_data:
        out += f'\n\n      <div class="quiz-question" id="{q_id}">\n'
        out += f'        <p>{q_text}</p>\n'
        out += f'        <div class="quiz-options">\n'
        for attrs, text in options:
            out += f'          <div class="quiz-option"{attrs}>{text}</div>\n'
        out += f'        </div>\n'
        out += f'      </div>'
    out += '\n    </div>'

    return body_html[:qs_start] + out + body_html[qs_end:]


# ─── Step 3: fix article content internals ───────────────────────────────────

def fix_content(body_html):
    """Fix class names and structure inside the article content only."""

    # ── Handle original plat- format (tut-body / tut-article / sidebar)
    body_html = re.sub(r'<div class="tut-body"[^>]*>', '<div class="tutorial-layout">', body_html)
    body_html = re.sub(r'<article class="tut-article"', '<article class="tutorial-body"', body_html)
    body_html = re.sub(r'<aside class="sidebar"[^>]*>', '<aside class="tutorial-sidebar">', body_html)

    # ── Ensure article has correct class and id
    body_html = re.sub(r'class="tutorial-article"', 'class="tutorial-body"', body_html)
    body_html = re.sub(
        r'<article class="tutorial-body"(?! id=)',
        '<article class="tutorial-body" id="tutorialContent"',
        body_html
    )

    # ── Section summary
    body_html = re.sub(
        r'<h2 class="section-summary-title"[^>]*>(.*?)</h2>',
        lambda m: '<span class="ss-label">' + m.group(1) + '</span>',
        body_html, flags=re.DOTALL
    )
    body_html = re.sub(r'<ul class="section-summary-list">', '<ul>', body_html)

    # ── Callouts: plat- style (callout-title div) -> ENT-002 style
    EMOJI = {'callout--insight': '\U0001f4a1', 'callout--key': '\U0001f511',
             'callout--tip': '✅', 'callout--warning': '⚠️'}
    def fix_callout(m):
        full = m.group(0)
        if 'callout-icon' in full or 'callout-body' in full:
            return full
        cls_m = re.search(r'class="callout (callout--\w+)"', full)
        cls = cls_m.group(1) if cls_m else 'callout--key'
        emoji = EMOJI.get(cls, '\U0001f511')
        tm = re.search(r'<div class="callout-title"[^>]*>(.*?)</div>', full, re.DOTALL)
        title = st(tm.group(1)) if tm else ''
        paras = re.findall(r'<p>(.*?)</p>', full, re.DOTALL)
        ph = '\n            '.join(f'<p>{p}</p>' for p in paras)
        return (f'<div class="callout {cls}">\n'
                f'          <div class="callout-icon">{emoji}</div>\n'
                f'          <div class="callout-body">\n'
                f'            <strong>{title}</strong>\n'
                f'            {ph}\n'
                f'          </div>\n'
                f'        </div>')
    body_html = re.sub(
        r'<div class="callout callout--\w+">\s*<div class="callout-title">.*?</div>.*?</div>',
        fix_callout, body_html, flags=re.DOTALL
    )

    # ── Key takeaways
    body_html = re.sub(r'<h3 class="key-takeaways-title"[^>]*>(.*?)</h3>', r'<h2>\1</h2>', body_html, flags=re.DOTALL)
    body_html = re.sub(r'<ul class="key-takeaways-list">', '<ul>', body_html)

    # ── Quiz: normalise all formats to ENT-002 structure
    # Convert section-based quiz (plat- original format) to div-based
    body_html = re.sub(r'<section class="quiz-section"[^>]*>', '<div class="quiz-section" id="quiz">', body_html)
    # Convert any remaining <section>/<section class=...> and </section> in article content
    body_html = re.sub(r'<section\b[^>]*>', lambda m: m.group(0).replace('section', 'div', 1), body_html)
    body_html = re.sub(r'</section>', '</div>', body_html)
    # Class name fixes
    body_html = re.sub(r'<div class="quiz-q"', '<div class="quiz-question"', body_html)
    body_html = re.sub(r'<p class="quiz-prompt"[^>]*>', '<p>', body_html)
    body_html = re.sub(r'<p class="quiz-question-text"[^>]*>(.*?)</p>', r'<p>\1</p>', body_html, flags=re.DOTALL)
    # Convert <button class="quiz-option"> to <div class="quiz-option">
    body_html = re.sub(r'<button class="quiz-option"', '<div class="quiz-option"', body_html)
    body_html = re.sub(r'</button>', '</div>', body_html)
    # Other quiz fixes
    body_html = re.sub(r'<h3 class="quiz-title"[^>]*>(.*?)</h3>', r'<h2>\1</h2>', body_html, flags=re.DOTALL)
    body_html = re.sub(r'\s*<div class="quiz-feedback"[^>]*>[^<]*</div>', '', body_html)
    body_html = re.sub(r'<div class="quiz-section"(?! id)', '<div class="quiz-section" id="quiz"', body_html)
    # Rebuild quiz section atomically (fixes nesting and adds quiz-options wrapper)
    body_html = rebuild_quiz_section(body_html)

    # ── Code blocks unwrap
    body_html = re.sub(r'<div class="code-block">\s*(<pre)', r'\1', body_html, flags=re.DOTALL)
    body_html = re.sub(r'(</pre>)\s*</div>', r'\1', body_html, flags=re.DOTALL)

    # ── Related tutorials: fix heading only (cards fixed separately)
    body_html = re.sub(
        r'<h[23][^>]*>(?:Related Tutorials|Continue Reading)</h[23]>',
        '<h2>Continue Reading</h2>', body_html
    )

    # ── Strip leaked prior-run content (footer, script blocks, close tags)
    body_html = re.sub(r'\s*<footer\b.*?</footer>', '', body_html, flags=re.DOTALL)
    body_html = re.sub(r'\s*<script\b.*?</script>', '', body_html, flags=re.DOTALL)
    body_html = re.sub(r'\s*</body>.*', '', body_html, flags=re.DOTALL)

    # ── Ensure layout container structure
    if not re.search(r'<div class="container">\s*<div class="tutorial-layout">', body_html):
        body_html = re.sub(
            r'(<div class="tutorial-layout"[^>]*>)',
            r'<div class="container">\n    \1',
            body_html, count=1
        )
        body_html = re.sub(
            r'(</article>\s*</aside>\s*</div>)',
            r'\1\n  </div>',
            body_html, count=1, flags=re.DOTALL
        )

    return body_html


# ─── Step 4: fix related cards (title lookup from target files) ───────────────

_title_cache = {}

def get_tutorial_title(slug, tutorials_dir):
    if slug in _title_cache:
        return _title_cache[slug]
    target = os.path.join(tutorials_dir, f'{slug}.html')
    if os.path.exists(target):
        with open(target, encoding='utf-8') as f:
            html = f.read()
        tm = re.search(r'<title>(.*?)(?:\s*[|—–]\s*SFVedas)?\s*</title>', html, re.IGNORECASE | re.DOTALL)
        if tm:
            t = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
            t = re.sub(r'^[A-Z]+-\d+[\s:—–-]+', '', t).strip()
            t = re.sub(r'\s*[—–]\s*SFVedas\s*$', '', t, flags=re.IGNORECASE).strip()
            _title_cache[slug] = t
            return t
    _title_cache[slug] = slug.upper()
    return slug.upper()


def fix_article_div_balance(body_chunk):
    """Remove stray </div> tags inside <article> that make div depth go negative."""
    art_m = re.search(r'<article\b', body_chunk)
    art_end = body_chunk.rfind('</article>')
    if not art_m or art_end == -1:
        return body_chunk

    article = body_chunk[art_m.start():art_end]
    extra_closes = article.count('</div>') - len(re.findall(r'<div\b', article))
    if extra_closes <= 0:
        return body_chunk

    depth = 0
    result = []
    removed = 0
    i = 0
    while i < len(article):
        next_open_m = re.search(r'<div\b', article[i:])
        next_close = article.find('</div>', i)
        next_open = (next_open_m.start() + i) if next_open_m else None

        if next_open is None and next_close == -1:
            result.append(article[i:])
            break
        if next_close == -1 or (next_open is not None and next_open < next_close):
            result.append(article[i:next_open + 4])
            depth += 1
            i = next_open + 4
        else:
            result.append(article[i:next_close])
            if depth > 0:
                depth -= 1
                result.append('</div>')
            else:
                removed += 1
                if removed >= extra_closes:
                    result.append(article[next_close + 6:])
                    i = len(article)
                    break
            i = next_close + 6

    return body_chunk[:art_m.start()] + ''.join(result) + body_chunk[art_end:]


def fix_related_cards(body_html, tutorials_dir):
    """Rebuild every related-card with the correct title from the target file."""
    def fix_card(m):
        full = m.group(0)
        href_m = re.search(r'href="([^"]+)"', full)
        href = href_m.group(1) if href_m else '#'
        slug_m = re.search(r'([\w]+-\d+)\.html', href)
        if not slug_m:
            return full
        slug = slug_m.group(1)
        cid = slug.upper()
        title = get_tutorial_title(slug, tutorials_dir)
        return (f'<a href="{href}" class="related-card">\n'
                f'              <span class="card-id">{cid}</span>\n'
                f'              <h4>{title}</h4>\n'
                f'            </a>')
    return re.sub(r'<a href="[^"]*" class="related-card">.*?</a>', fix_card, body_html, flags=re.DOTALL)


# ─── Step 5: build related-tutorials section ─────────────────────────────────

def build_related_tutorials(slug, tutorials_dir):
    """Generate a related-tutorials section with up to 3 sequential neighbours."""
    m = re.match(r'^([a-z]+)-(\d+)$', slug)
    if not m:
        return ''
    prefix, num = m.group(1), int(m.group(2))

    # Preference order: next, prev, two-ahead, two-behind, three-ahead, series-start
    offsets = [+1, -1, +2, -2, +3]
    candidates = []
    for offset in offsets:
        cnum = num + offset
        if cnum < 1:
            continue
        cslug = f'{prefix}-{cnum:03d}'
        if os.path.exists(os.path.join(tutorials_dir, f'{cslug}.html')):
            candidates.append(cslug)
        if len(candidates) == 3:
            break

    # Fallback: first in series
    if len(candidates) < 3:
        first = f'{prefix}-001'
        if first != slug and first not in candidates:
            if os.path.exists(os.path.join(tutorials_dir, f'{first}.html')):
                candidates.append(first)

    # Cross-series fallback for lone tutorials (e.g. del-001)
    if len(candidates) < 3:
        for fallback_prefix in ('arch', 'plat', 'ent'):
            if fallback_prefix == prefix:
                continue
            for fn in (f'{fallback_prefix}-001', f'{fallback_prefix}-002', f'{fallback_prefix}-003'):
                if fn not in candidates and os.path.exists(os.path.join(tutorials_dir, f'{fn}.html')):
                    candidates.append(fn)
                if len(candidates) == 3:
                    break
            if len(candidates) == 3:
                break

    if not candidates:
        return ''

    cards_html = ''
    for cslug in candidates:
        ctitle = get_tutorial_title(cslug, tutorials_dir)
        cards_html += (f'            <a href="{cslug}.html" class="related-card">\n'
                       f'              <span class="card-id">{cslug.upper()}</span>\n'
                       f'              <h4>{ctitle}</h4>\n'
                       f'            </a>\n')

    return ('        <div class="related-tutorials">\n'
            '          <h2>Continue Reading</h2>\n'
            '          <div class="related-grid">\n'
            + cards_html +
            '          </div>\n'
            '        </div>')


# ─── Step 6: rebuild sidebar to exact ENT-002 structure ──────────────────────

def rebuild_sidebar(aside_html, slug, tutorials_dir=None):
    """Completely rebuild the sidebar to match ENT-002 exactly."""
    prefix = slug.split('-')[0].lower()

    # ── Extract TOC items (handle any format)
    toc_items = []
    # Format 1: <li><a href="...">text</a></li>
    for h, t in re.findall(r'<li>\s*<a href="([^"]*)"[^>]*>(.*?)</a>\s*</li>', aside_html, re.DOTALL):
        text = st(t).strip()
        if text:
            toc_items.append((h, text))
    # Format 2: <a href="..." class="toc-link">text</a>
    if not toc_items:
        for h, t in re.findall(r'<a href="([^"]*)"[^>]*class="toc-link"[^>]*>([^<]+)</a>', aside_html):
            toc_items.append((h, t.strip()))
        if not toc_items:
            for h, t in re.findall(r'<a[^>]*class="toc-link"[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', aside_html):
                toc_items.append((h, t.strip()))

    # ── Build TOC block
    if toc_items:
        lis = '\n'.join(f'            <li><a href="{h}">{t}</a></li>' for h, t in toc_items)
        toc_block = (f'        <div class="sidebar-toc">\n'
                     f'          <h4>In This Tutorial</h4>\n'
                     f'          <ul class="toc-list">\n{lis}\n          </ul>\n'
                     f'        </div>\n')
    else:
        toc_block = ''

    # ── Progress block (always standard)
    progress_block = ('        <div class="sidebar-progress">\n'
                      '          <h4>Reading Progress</h4>\n'
                      '          <div class="progress-track">'
                      '<div class="progress-fill" id="sidebarProgress"></div></div>\n'
                      '          <span class="progress-pct" id="progressPct">0%</span>\n'
                      '        </div>\n')

    # ── CTA block: "Continue Learning → Next tutorial" or area fallback
    next_slug = None
    next_title = None
    if tutorials_dir:
        m = re.match(r'^([a-z]+)-(\d+)$', slug)
        if m:
            next_num = int(m.group(2)) + 1
            ns = f'{m.group(1)}-{next_num:03d}'
            if os.path.exists(os.path.join(tutorials_dir, f'{ns}.html')):
                next_slug = ns
                next_title = _short_title(get_tutorial_title(ns, tutorials_dir))

    if next_slug and next_title:
        cta_block = (f'        <div class="sidebar-cta">\n'
                     f'          <h4>Continue Learning</h4>\n'
                     f'          <a href="{next_slug}.html" class="btn btn-primary" '
                     f'style="width:100%;text-align:center;display:block;">'
                     f'Next: {next_title} →</a>\n'
                     f'        </div>\n')
    else:
        cta_data = AREA_CTA.get(prefix, AREA_CTA['arch'])
        cta_h, cta_p, cta_href, cta_label = cta_data
        cta_block = (f'        <div class="sidebar-cta">\n'
                     f'          <h4>{cta_h}</h4>\n'
                     f'          <p>{cta_p}</p>\n'
                     f'          <a href="{cta_href}" class="btn btn-primary" '
                     f'style="width:100%;text-align:center;display:block;">{cta_label}</a>\n'
                     f'        </div>\n')

    return (f'      <aside class="tutorial-sidebar">\n'
            f'{toc_block}{progress_block}{cta_block}'
            f'      </aside>')


# ─── Step 6: build the header section ────────────────────────────────────────

def build_header(tut_id, am, title, subtitle, read_time, audience, role):
    tag, name = am['tag'], am['name']
    c, tc, bc = am['color'], am['text'], am['border']
    return (
        '  <section style="background: var(--bg-secondary); border-bottom: 1px solid var(--border); padding: 56px 0 40px;">\n'
        '    <div class="container">\n'
        '      <div style="margin-bottom: 16px;">\n'
        f'        <a href="../pages/tutorials.html?tag={tag}" style="font-family:var(--font-ui);font-size:0.8rem;color:var(--sage-green);text-decoration:none;">← Back to {name}</a>\n'
        '      </div>\n'
        '      <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">\n'
        f'        <span class="card-id">{tut_id}</span>\n'
        f'        <span class="card-tag" style="background:{c};color:{tc};border-color:{bc};">{name}</span>\n'
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
        '  </section>\n'
    )


# ─── Main processing ─────────────────────────────────────────────────────────

def process(filepath, slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    tut_id, am, title, subtitle, read_time, audience, role = extract_meta(html, slug)

    # Extract <head> content
    head_m = re.search(r'<head>(.*?)</head>', html, re.DOTALL | re.IGNORECASE)
    raw_head = head_m.group(1) if head_m else ''
    title_m = re.search(r'(<title>.*?</title>)', raw_head, re.DOTALL | re.IGNORECASE)
    desc_m  = re.search(r'(<meta name="description"[^>]*>)', raw_head, re.IGNORECASE)
    title_tag = title_m.group(1) if title_m else f'<title>{title} | SFVedas</title>'
    desc_tag  = (desc_m.group(1) + '\n  ') if desc_m else ''

    # Extract layout block
    layout_start, content_end, body_chunk = isolate_body_content(html)
    if body_chunk is None:
        raise ValueError('Could not find tutorial-layout')

    # Fix article content
    body_chunk = fix_content(body_chunk)

    # Remove stray </div> tags that break the grid (extra closes inside <article>)
    body_chunk = fix_article_div_balance(body_chunk)

    # Ensure </article> is present (may be missing if prior run leaked content)
    if re.search(r'<article\b', body_chunk) and '</article>' not in body_chunk:
        # Close article before the aside (if any), else at end of article content
        aside_pos = body_chunk.find('<aside')
        if aside_pos != -1:
            body_chunk = body_chunk[:aside_pos] + '</article>\n\n' + body_chunk[aside_pos:]
        else:
            body_chunk += '\n</article>'

    # Fix related card titles
    tutorials_dir = os.path.dirname(filepath)
    body_chunk = fix_related_cards(body_chunk, tutorials_dir)

    # Remove any existing related-tutorials block (we rebuild from scratch below)
    rt_m = re.search(r'<div class="related-tutorials">', body_chunk)
    if rt_m:
        rt_end = find_div_end(body_chunk, rt_m.start())
        body_chunk = body_chunk[:rt_m.start()].rstrip() + '\n' + body_chunk[rt_end:].lstrip()

    # Insert freshly generated related-tutorials section before </article>
    related_html = build_related_tutorials(slug, tutorials_dir)
    if related_html:
        art_end = body_chunk.rfind('</article>')
        if art_end != -1:
            body_chunk = (body_chunk[:art_end].rstrip()
                          + '\n\n' + related_html
                          + '\n\n      </article>'
                          + body_chunk[art_end + 10:])

    # Rebuild sidebar (or build from scratch if missing)
    aside_m = re.search(r'<aside class="tutorial-sidebar">.*?</aside>', body_chunk, re.DOTALL)
    if aside_m:
        new_aside = rebuild_sidebar(aside_m.group(0), slug, tutorials_dir)
        body_chunk = body_chunk[:aside_m.start()] + new_aside + body_chunk[aside_m.end():]
    else:
        # No sidebar — extract TOC from article h2 headings and build one
        toc_li = ''
        toc_items = []
        for hm in re.finditer(r'<h2[^>]*>(.*?)</h2>', body_chunk, re.DOTALL):
            text = re.sub(r'<[^>]+>', '', hm.group(1)).strip()
            if text and text not in ('Continue Reading', 'Check Your Understanding'):
                toc_items.append(text)
        if toc_items:
            toc_li = '\n'.join(f'<li><a href="#">{t}</a></li>' for t in toc_items)
        bare_aside = (f'<aside class="tutorial-sidebar">'
                      f'<div class="sidebar-toc"><h4>In This Tutorial</h4>'
                      f'<ul class="toc-list">{toc_li}</ul></div>'
                      f'</aside>')
        new_aside = rebuild_sidebar(bare_aside, slug, tutorials_dir)
        # Append after </article> if present, else at end
        art_end = body_chunk.rfind('</article>')
        if art_end != -1:
            body_chunk = body_chunk[:art_end + 10] + '\n\n' + new_aside + body_chunk[art_end + 10:]
        else:
            body_chunk += '\n\n' + new_aside

    # Assemble final file
    out = ('<!DOCTYPE html>\n'
           '<html lang="en">\n'
           '<head>\n'
           '  <meta charset="UTF-8"/>\n'
           '  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
           f'  {title_tag}\n'
           f'  {desc_tag}'
           f'{FONTS}\n'
           '  <link rel="stylesheet" href="../css/main.css"/>\n'
           '</head>\n'
           '<body class="light-mode">\n\n'
           + NAV + '\n\n'
           + build_header(tut_id, am, title, subtitle, read_time, audience, role)
           + '\n  <div class="container">\n'
           + '    <div class="tutorial-layout">\n\n'
           )

    # Strip outer container/layout wrappers from body_chunk, keep inner content
    inner = body_chunk
    inner = re.sub(r'^\s*<div class="container">\s*<div class="tutorial-layout"[^>]*>', '', inner, flags=re.DOTALL).strip()
    inner = re.sub(r'^\s*<div class="tutorial-layout"[^>]*>', '', inner, flags=re.DOTALL).strip()
    inner = re.sub(r'</div>\s*</div>\s*$', '', inner.rstrip(), flags=re.DOTALL).strip()
    inner = re.sub(r'</div>\s*$', '', inner.rstrip(), flags=re.DOTALL).strip()

    out += inner + '\n\n'
    out += '    </div>\n  </div>\n\n'
    out += FOOTER + '\n\n'
    out += JS + '\n'
    out += '</body>\n</html>\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(out)


def main():
    files = sorted(f for f in os.listdir(TUTORIALS_DIR)
                   if f.endswith('.html') and f != 'ent-002.html')
    print(f'Processing {len(files)} files...')
    # Pre-warm title cache from ENT-002 so related cards to it resolve correctly
    get_tutorial_title('ent-002', TUTORIALS_DIR)
    ok = err = 0
    for fname in files:
        slug = fname.replace('.html', '')
        try:
            process(os.path.join(TUTORIALS_DIR, fname), slug)
            print(f'  OK  {fname}')
            ok += 1
        except Exception as e:
            import traceback
            print(f'  ERR {fname}: {e}')
            traceback.print_exc()
            err += 1
    print(f'\nDone: {ok} OK, {err} errors')


if __name__ == '__main__':
    main()
