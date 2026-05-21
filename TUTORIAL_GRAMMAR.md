# SFVedas Tutorial Grammar File
> Reference document for creating new tutorials. Every new tutorial MUST follow this structure exactly.
> Last updated against: `tutorials/arch-001/index.html` (canonical reference)

---

## 1. File Naming & Location

```
tutorials/[prefix]-[NNN]/index.html
```

Each tutorial lives in its own subdirectory so GitHub Pages serves it at a clean URL:
`https://sfvedas.com/tutorials/arch-001/`

Number is zero-padded to 3 digits: `arch-001`, `ent-024`.

| Prefix | Category | Tag |
|--------|----------|-----|
| `arch` | Architecture | `architecture` |
| `plat` | Platform & Technical | `platform-technical` |
| `intg` | Integration & Data | `integration-data` |
| `ent` | Enterprise Strategy | `enterprise-strategy` |
| `ai` | AI & Future | `ai-future` |
| `del` | Delivery Management | `delivery-management` |
| `crm` | CRM Comparison | `crm-comparison` |
| `sec` | Security & Compliance | `security-compliance` |
| `rpt` | Reporting & Analytics | `reporting-analytics` |
| `ind` | Industry-Specific | `industry-specific` |
| `tal` | Team & Talent | `team-talent` |
| `lic` | Licensing & Commercial | `licensing-commercial` |
| `cha` | Change Management | `change-management` |
| `rfp` | RFP | `rfp` |

---

## 2. Complete HTML Template

Replace every `{{PLACEHOLDER}}` before saving.

**All paths are absolute** — tutorials live two levels deep (`/tutorials/slug/`), so never use `../` relative paths.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <link rel="canonical" href="https://sfvedas.com/tutorials/{{SLUG}}/"/>
  <link rel="icon" type="image/svg+xml" href="/images/favicon.svg"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{{TUTORIAL_ID}}: {{FULL_TITLE}} — SFVedas</title>
  <meta name="description" content="{{META_DESCRIPTION}}"/>
  <meta property="og:title" content="{{TUTORIAL_ID}}: {{FULL_TITLE}} — SFVedas"/>
  <meta property="og:description" content="{{META_DESCRIPTION}}"/>
  <meta property="og:type" content="article"/>
  <meta property="og:url" content="https://sfvedas.com/tutorials/{{SLUG}}/"/>
  <meta property="og:image" content="https://sfvedas.com/images/og-default.png"/>
  <meta property="og:site_name" content="SFVedas"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="{{TUTORIAL_ID}}: {{FULL_TITLE}} — SFVedas"/>
  <meta name="twitter:description" content="{{META_DESCRIPTION}}"/>
  <meta name="twitter:image" content="https://sfvedas.com/images/og-default.png"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link rel="dns-prefetch" href="https://www.googletagmanager.com"/>
  <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com"/>
  <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin/>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"/>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" media="print" onload="this.media='all'"/>
  <noscript><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/></noscript>
  <link rel="stylesheet" href="/css/main.css"/>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-99QW4K310Y"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-99QW4K310Y');
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"/>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{{TUTORIAL_ID}}: {{FULL_TITLE}} — SFVedas",
    "description": "{{META_DESCRIPTION}}",
    "url": "https://sfvedas.com/tutorials/{{SLUG}}/",
    "mainEntityOfPage": "https://sfvedas.com/tutorials/{{SLUG}}/",
    "author": {
      "@type": "Person",
      "name": "Vishal Sharma",
      "url": "https://sfvedas.com/about/"
    },
    "publisher": {
      "@type": "Organization",
      "name": "SFVedas",
      "url": "https://sfvedas.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://sfvedas.com/images/logo.svg"
      }
    },
    "image": "https://sfvedas.com/images/og-default.png"
  }
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4584420180521124" crossorigin="anonymous"></script>
</head>
<body class="light-mode">

  <div class="reading-progress" id="readingProgress"></div>

  <!-- ── NAVBAR (identical across all tutorial pages — do not modify) ── -->
  <nav class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
      <ul class="nav-links">
        <li><a href="/" class="nav-link">Home</a></li>
        <li><a href="/tutorials/" class="nav-link active">Tutorials</a></li>
        <li><a href="/learning-paths/" class="nav-link">Learning Paths</a></li>
        <li><a href="/about/" class="nav-link">About</a></li>
        <li><a href="/advertise/" class="nav-link">Advertise</a></li>
      </ul>
      <div class="nav-actions">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"><span class="theme-icon">☀</span></button>
        <button class="nav-hamburger" id="hamburger"><span></span><span></span><span></span></button>
      </div>
    </div>
    <div class="nav-mobile" id="navMobile">
      <a href="/" class="nav-link">Home</a>
      <a href="/tutorials/" class="nav-link">Tutorials</a>
      <a href="/learning-paths/" class="nav-link">Learning Paths</a>
      <a href="/about/" class="nav-link">About</a>
      <a href="/advertise/" class="nav-link">Advertise</a>
    </div>
  </nav>

  <!-- ── TUTORIAL HEADER ── -->
  <section style="background: var(--bg-secondary); border-bottom: 1px solid var(--border); padding: 56px 0 40px;">
    <div class="container">
      <div style="margin-bottom: 16px;">
        <a href="/tutorials/?tag={{TAG}}" style="font-family:var(--font-ui);font-size:0.8rem;color:var(--sage-green);text-decoration:none;">← Back to {{CATEGORY_NAME}}</a>
      </div>
      <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">
        <span class="card-id">{{TUTORIAL_ID}}</span>
        <span class="card-tag" style="background:rgba(232,147,10,0.08);color:var(--saffron);border-color:rgba(232,147,10,0.2);">{{CATEGORY_NAME}}</span>
        <span class="card-read">{{READ_TIME}} min read</span>
        <span style="font-family:var(--font-ui);font-size:0.78rem;color:var(--text-secondary);">For: {{AUDIENCE}}</span>
      </div>
      <h1 style="font-family:var(--font-display);font-size:clamp(1.8rem,4vw,2.8rem);font-weight:700;color:var(--text-primary);line-height:1.2;max-width:820px;margin-bottom:16px;">
        {{FULL_TITLE}}
      </h1>
      <p style="font-family:var(--font-body);font-size:1.05rem;color:var(--text-secondary);max-width:700px;line-height:1.75;margin-bottom:24px;">
        {{SUBTITLE}}
      </p>
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="author-avatar" style="width:40px;height:40px;font-size:0.85rem;">VS</div>
        <div>
          <p style="font-family:var(--font-ui);font-size:0.85rem;font-weight:600;color:var(--text-primary);margin:0;">Vishal Sharma</p>
          <p style="font-family:var(--font-ui);font-size:0.75rem;color:var(--text-secondary);margin:0;">{{AUTHOR_ROLE}} · Updated {{MONTH_YEAR}}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── AD UNIT (one per page, placed here only) ── -->
  <div class="ad-unit">
    <ins class="adsbygoogle"
         style="display:block;text-align:center;"
         data-ad-layout="in-article"
         data-ad-format="fluid"
         data-ad-client="ca-pub-4584420180521124"
         data-ad-slot=""></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
  </div>

  <!-- ── MAIN LAYOUT ── -->
  <div class="container">
    <div class="tutorial-layout">

      <article class="tutorial-body" id="tutorialContent">

        <!-- SECTION SUMMARY — always first inside article -->
        <div class="section-summary">
          <span class="ss-label">What you will learn in this tutorial</span>
          <ul>
            <li>{{LEARNING_POINT_1}}</li>
            <li>{{LEARNING_POINT_2}}</li>
            <li>{{LEARNING_POINT_3}}</li>
            <li>{{LEARNING_POINT_4}}</li>
            <li>{{LEARNING_POINT_5}}</li>
            <!-- add 6th or 7th bullet if needed; 5–7 is the target range -->
          </ul>
        </div>

        <!-- CONTENT SECTIONS — repeat as needed, h2 IDs must match TOC -->
        <h2 id="s1">{{SECTION_1_HEADING}}</h2>
        <p>{{PARAGRAPH}}</p>
        <p>{{PARAGRAPH}}</p>

        <!-- CALLOUT — choose ONE variant per callout (see Section 4) -->
        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>{{CALLOUT_LABEL}}</strong>
            <p>{{CALLOUT_TEXT}}</p>
          </div>
        </div>

        <h2 id="s2">{{SECTION_2_HEADING}}</h2>
        <p>{{PARAGRAPH}}</p>

        <!-- CODE BLOCK — use correct language class for Prism.js syntax highlighting -->
        <pre><code class="language-java">{{CODE}}</code></pre>

        <h2 id="s3">{{SECTION_3_HEADING}}</h2>
        <p>{{PARAGRAPH}}</p>

        <!-- KEY TAKEAWAYS — always the second-to-last content block -->
        <div class="key-takeaways">
          <h2>Key Takeaways</h2>
          <ul>
            <li>{{TAKEAWAY_1}}</li>
            <li>{{TAKEAWAY_2}}</li>
            <li>{{TAKEAWAY_3}}</li>
            <li>{{TAKEAWAY_4}}</li>
            <li>{{TAKEAWAY_5}}</li>
            <!-- minimum 5; add more if needed -->
          </ul>
        </div>

        <!-- QUIZ — always the last content block before related tutorials -->
        <!-- Each question has exactly 4 options (1 correct, 3 wrong) -->
        <div class="quiz-section" id="quiz">
          <h2>Checkpoint: Test Your Understanding</h2>

          <div class="quiz-question" id="q1">
            <p>1. {{QUESTION_1}}</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q1','right')">B. {{CORRECT_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">C. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. {{WRONG_OPTION}}</div>
            </div>
          </div>

          <div class="quiz-question" id="q2">
            <p>2. {{QUESTION_2}}</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">B. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q2','right')">C. {{CORRECT_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. {{WRONG_OPTION}}</div>
            </div>
          </div>

          <div class="quiz-question" id="q3">
            <p>3. {{QUESTION_3}}</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. {{WRONG_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q3','right')">C. {{CORRECT_OPTION}}</div>
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. {{WRONG_OPTION}}</div>
            </div>
          </div>
        </div>

        <!-- RELATED TUTORIALS — always after quiz, before closing article tag -->
        <!-- Links are relative to the current slug directory: ../other-slug/ -->
        <div class="related-tutorials">
          <h2>Continue Reading</h2>
          <div class="related-grid">
            <a href="../{{RELATED_1_SLUG}}/" class="related-card">
              <span class="card-id">{{RELATED_1_ID}}</span>
              <h4>{{RELATED_1_TITLE}}</h4>
            </a>
            <a href="../{{RELATED_2_SLUG}}/" class="related-card">
              <span class="card-id">{{RELATED_2_ID}}</span>
              <h4>{{RELATED_2_TITLE}}</h4>
            </a>
            <a href="../{{RELATED_3_SLUG}}/" class="related-card">
              <span class="card-id">{{RELATED_3_ID}}</span>
              <h4>{{RELATED_3_TITLE}}</h4>
            </a>
          </div>
        </div>

      </article>

      <!-- ── SIDEBAR ── -->
      <aside class="tutorial-sidebar">
        <div class="sidebar-toc">
          <h4>In This Tutorial</h4>
          <ul class="toc-list">
            <li><a href="#s1">{{SECTION_1_HEADING}}</a></li>
            <li><a href="#s2">{{SECTION_2_HEADING}}</a></li>
            <li><a href="#s3">{{SECTION_3_HEADING}}</a></li>
            <!-- add one <li> per h2 in the article, in order -->
            <li><a href="#quiz">Key Takeaways</a></li>
            <li><a href="#quiz">Checkpoint: Test Your Understanding</a></li>
          </ul>
        </div>
        <div class="sidebar-progress">
          <h4>Reading Progress</h4>
          <div class="progress-track"><div class="progress-fill" id="sidebarProgress"></div></div>
          <span class="progress-pct" id="progressPct">0%</span>
        </div>
        <!-- NEXT TUTORIAL — omit entire block if this is the last in the series -->
        <div class="sidebar-next">
          <h4>Next Tutorial</h4>
          <a href="../{{NEXT_SLUG}}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{{NEXT_ID}}</span>
            <span class="sidebar-next-title">{{NEXT_TITLE}}</span>
            <span class="sidebar-next-arrow">&#8594;</span>
          </a>
        </div>
        <!-- PREVIOUS TUTORIAL — omit entire block if this is the first in the series -->
        <div class="sidebar-next">
          <h4>Previous Tutorial</h4>
          <a href="../{{PREV_SLUG}}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{{PREV_ID}}</span>
            <span class="sidebar-next-title">{{PREV_TITLE}}</span>
            <span class="sidebar-next-arrow">&#8592;</span>
          </a>
        </div>
      </aside>

    </div>
  </div>

  <!-- ── FOOTER (identical across all tutorial pages — do not modify) ── -->
  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="/" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
          <p class="footer-tagline">Deep Salesforce Knowledge<br/>for Tech Leaders</p>
          <p class="footer-domain">sfvedas.com</p>
        </div>
        <div class="footer-links">
          <div class="footer-col"><h4>Learn</h4><a href="/tutorials/">All Tutorials</a><a href="/learning-paths/">Learning Paths</a></div>
          <div class="footer-col"><h4>About</h4><a href="/about/">Our Story</a></div>
          <div class="footer-col"><h4>Topics</h4><a href="/tutorials/">Architecture</a><a href="/tutorials/">Delivery</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 SFVedas · Vishal Sharma · sfvedas.com</p>
        <p class="footer-philosophy">Deep knowledge. For the decisions that matter.</p>
      </div>
    </div>
  </footer>

  <!-- ── SCRIPTS (identical across all tutorial pages — do not modify) ── -->
  <script>
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
  <script src="/js/main.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js" defer></script>
</body>
</html>
```

---

## 3. Placeholder Reference

| Placeholder | Example | Notes |
|---|---|---|
| `{{SLUG}}` | `arch-004` | Lowercase, matches directory name under `tutorials/` |
| `{{TUTORIAL_ID}}` | `ARCH-004` | Uppercase, matches entry in `tutorials/index.html` |
| `{{FULL_TITLE}}` | `Salesforce Metadata Model: What It Is and Why It Shapes Everything` | No trailing period |
| `{{META_DESCRIPTION}}` | `Understanding the Salesforce metadata model and how it drives multi-tenancy, DevOps, and org architecture.` | 140–160 chars |
| `{{SUBTITLE}}` | One sentence that frames the SO WHAT for a senior reader. Not a repetition of the title. | Max 30 words |
| `{{TAG}}` | `architecture` | See naming table in Section 1 |
| `{{CATEGORY_NAME}}` | `Architecture` | Human-readable label for breadcrumb |
| `{{READ_TIME}}` | `18` | Integer minutes. 18–25 is the target range |
| `{{AUDIENCE}}` | `Solution Architects` | Options: CTOs · Solution Architects · Delivery Managers · Tech Leaders · Senior Practitioners |
| `{{AUTHOR_ROLE}}` | `Salesforce Architecture Specialist` | See Section 5 |
| `{{MONTH_YEAR}}` | `May 2026` | Month Year format |
| `{{NEXT_SLUG}}` / `{{PREV_SLUG}}` | `arch-005` | Matches the directory name; used as `../arch-005/` |
| `{{NEXT_ID}}` / `{{PREV_ID}}` | `ARCH-005` | Uppercase |
| `{{NEXT_TITLE}}` / `{{PREV_TITLE}}` | Full tutorial title as it appears in `tutorials/index.html` | No truncation |

---

## 4. Content Blocks Reference

### 4a. Callout Variants

Four types. Pick the right one — do not mix them arbitrarily.
The callout body uses a `<strong>Label</strong>` on its own line followed by `<p>text</p>`, not a colon-appended label.

```html
<!-- Insight: adds a non-obvious angle or reframe -->
<div class="callout callout--insight">
  <div class="callout-icon">💡</div>
  <div class="callout-body">
    <strong>Insight</strong>
    <p>Text.</p>
  </div>
</div>

<!-- Key point: the single most important fact in a section -->
<div class="callout callout--key">
  <div class="callout-icon">🔑</div>
  <div class="callout-body">
    <strong>Key Concept</strong>
    <p>Text.</p>
  </div>
</div>

<!-- Tip / Leader Perspective: practical actionable guidance -->
<div class="callout callout--tip">
  <div class="callout-icon">✅</div>
  <div class="callout-body">
    <strong>Leader Perspective</strong>
    <p>Text.</p>
  </div>
</div>

<!-- Warning: a common mistake or real risk -->
<div class="callout callout--warning">
  <div class="callout-icon">⚠️</div>
  <div class="callout-body">
    <strong>Warning for Architects</strong>
    <p>Text.</p>
  </div>
</div>
```

### 4b. Code Block Languages (Prism.js)

| `class=` value | Use for |
|---|---|
| `language-java` | Apex code |
| `language-javascript` | JavaScript / LWC |
| `language-sql` | SOQL / SOSL |
| `language-json` | JSON / sfdx-project.json |
| `language-bash` | CLI commands / shell |
| `language-xml` | Metadata XML |
| `language-html` | HTML / Visualforce |

### 4c. Inline Strong Text Patterns

Use `<strong>Term:</strong>` to introduce a named concept mid-paragraph:
```html
<p><strong>Multi-tenancy</strong> means that multiple customers share the same infrastructure.</p>
```

Use `<em>` for terminology being introduced for the first time:
```html
<p>This differs from <em>single-tenancy</em>, where each customer gets a dedicated stack.</p>
```

### 4d. Unordered Lists for Enumerated Facts

Use plain `<ul><li>` inside the article body for bulleted lists (Governor Limits, feature lists, etc.):
```html
<ul>
  <li><strong>Apex CPU time</strong> — 10,000ms per synchronous transaction</li>
  <li><strong>Heap size</strong> — 6MB synchronous, 12MB asynchronous</li>
</ul>
```

### 4e. Sub-headings Within Sections

Use `<h3>` for sub-topics within an `<h2>` section. `<h3>` does NOT get an `id` and does NOT appear in the TOC.

### 4f. Comparison / Decision Tables

For side-by-side comparisons use the `.comparison-table` class:
```html
<div class="comparison-table">
  <table>
    <thead>
      <tr><th>Option A</th><th>Option B</th></tr>
    </thead>
    <tbody>
      <tr><td>...</td><td>...</td></tr>
    </tbody>
  </table>
</div>
```

---

## 5. Author Role by Category

| Category | `{{AUTHOR_ROLE}}` value |
|---|---|
| Architecture | `Salesforce Architecture Specialist` |
| Platform & Technical | `Salesforce Platform Specialist` |
| Integration & Data | `Salesforce Integration Specialist` |
| Enterprise Strategy | `Salesforce Enterprise Strategist` |
| AI & Future | `Salesforce AI Specialist` |
| Delivery Management | `Salesforce Delivery Specialist` |
| CRM Comparison | `CRM Strategy Specialist` |
| Security & Compliance | `Salesforce Security Specialist` |
| Reporting & Analytics | `Salesforce Analytics Specialist` |
| Industry-Specific | `Salesforce Industry Specialist` |
| Team & Talent | `Salesforce Talent Specialist` |
| Licensing & Commercial | `Salesforce Commercial Specialist` |
| Change Management | `Salesforce Change Management Specialist` |
| RFP | `Salesforce Commercial Specialist` |

---

## 6. Section Structure Rules

- **Minimum 4 h2 sections**, maximum 8. Each gets an `id="sN"` (s1, s2, s3…).
- **Section summary** must list exactly what the tutorial covers — 5–7 bullet points.
- **Key Takeaways** — minimum 5 bullets. Each takeaway must be a complete, standalone sentence. No "see above" references.
- **Quiz** — exactly 3 questions. Each question has exactly 4 options (1 correct, 3 wrong), labelled A/B/C/D. Questions test genuine comprehension, not recall of exact wording.
- **Related tutorials** — exactly 3 cards. Should include the immediate next tutorial plus 2 thematically related ones from any series.
- **One callout per section** maximum. Not every section needs one.
- **Code blocks** — only include when the concept genuinely benefits from seeing code. Do not force code into strategy or management tutorials.

---

## 7. TOC Rule

Every `<h2 id="sN">` in the article body must have a matching `<li><a href="#sN">` in the sidebar TOC. The last two TOC items are always:
```html
<li><a href="#takeaways">Key Takeaways</a></li>
<li><a href="#quiz">Checkpoint: Test Your Understanding</a></li>
```

Note: add `id="takeaways"` to the `<div class="key-takeaways">` so the TOC link resolves correctly.

---

## 8. tutorials/index.html Registration

After creating the file, add an entry to the `TUTORIALS` array in `tutorials/index.html`. New entries go at the end of their category block:

```javascript
{id:'{{TUTORIAL_ID}}', tag:'{{TAG}}', title:'{{FULL_TITLE}}', readTime:{{READ_TIME}}, slug:'{{SLUG}}', available:true},
```

- `available:true` — only set this when the HTML file exists and is complete.
- Omit `available` (or set `available:false`) for planned-but-not-written tutorials.

---

## 9. Content Tone Guidelines

- **Audience:** Senior practitioners (architects, delivery managers, tech leaders, CTOs). Never explain basics.
- **Voice:** Direct, opinionated, precise. First person is acceptable. No hedging ("might", "could possibly").
- **Length:** 1,800–2,500 words of body text (excluding code blocks). 18–25 minute read.
- **Structure:** Each section answers one question. The h2 heading names the question or the answer.
- **No filler:** Every paragraph must add something not already stated. Cut summaries that repeat a prior paragraph.
- **British English spelling:** organisation, licence (noun), behaviour, programme, optimise.
- **Analytical depth:** Assume the reader is intelligent and time-poor. Lead with the insight, then support it. Don't build to a conclusion across three paragraphs when you could open with it.

---

## 10. Pre-publish Checklist

- [ ] All `{{PLACEHOLDERS}}` replaced — none left in the file
- [ ] File created at `tutorials/{{SLUG}}/index.html` (not `tutorials/{{SLUG}}.html`)
- [ ] `<link rel="canonical" href="https://sfvedas.com/tutorials/{{SLUG}}/"/>`
- [ ] `<title>` tag: `{{TUTORIAL_ID}}: {{FULL_TITLE}} — SFVedas` (em dash, not pipe)
- [ ] OG and Twitter meta tags match title and description; image is `og-default.png`
- [ ] JSON-LD headline and description match title and meta; URLs are clean (no `.html`)
- [ ] Breadcrumb links to `/tutorials/?tag={{TAG}}`
- [ ] TOC entries match every h2 id in the article body
- [ ] Quiz has 3 questions, each with exactly 4 options (1 `'right'`, 3 `'wrong'`) labelled A–D
- [ ] Related tutorials use `href="../{{SLUG}}/"` format (relative, clean)
- [ ] Sidebar Next/Prev slugs and titles are correct and match `tutorials/index.html`
- [ ] Ad unit has empty `data-ad-slot=""` (do not fill in)
- [ ] Entry added to `TUTORIALS` array in `tutorials/index.html` with `available:true`
- [ ] No duplicate ad units — exactly one `<div class="ad-unit">` per page
- [ ] All internal links use absolute paths (`/css/main.css`, `/js/main.js`, `/tutorials/`, etc.)
