/* SFVedas — Main JavaScript */

// ── Theme Toggle ──────────────────────────────────────────
const themeToggle = document.getElementById('themeToggle');
const themeIcon   = themeToggle?.querySelector('.theme-icon');
const body        = document.body;

let currentTheme = localStorage.getItem('sfvedas-theme') || 'light';

function applyTheme(theme) {
  body.classList.remove('dark-mode', 'salesforce-mode', 'light-mode');
  
  if (theme === 'dark') {
    body.classList.add('dark-mode');
    if (themeIcon) themeIcon.textContent = '☾';
  } else if (theme === 'salesforce') {
    body.classList.add('salesforce-mode');
    if (themeIcon) themeIcon.textContent = '☁';
  } else {
    body.classList.add('light-mode');
    if (themeIcon) themeIcon.textContent = '☀';
  }
  
  localStorage.setItem('sfvedas-theme', theme);
  currentTheme = theme;
}

// Initialise theme
applyTheme(currentTheme);

themeToggle?.addEventListener('click', () => {
  if (currentTheme === 'light') {
    applyTheme('dark');
  } else if (currentTheme === 'dark') {
    applyTheme('salesforce');
  } else {
    applyTheme('light');
  }
});

// ── Navbar Scroll ─────────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar?.classList.add('scrolled');
  } else {
    navbar?.classList.remove('scrolled');
  }
}, { passive: true });

// ── Mobile Menu ───────────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const navMobile = document.getElementById('navMobile');
hamburger?.addEventListener('click', () => {
  navMobile?.classList.toggle('open');
});

// ── Newsletter ────────────────────────────────────────────
// Sign up at formspree.io, create a form, and paste your endpoint below.
const NEWSLETTER_ENDPOINT = 'https://formspree.io/f/xzdweppl';

async function handleNewsletter(e) {
  e.preventDefault();
  const form  = e.target;
  const email = form.querySelector('input[type="email"]').value.trim();
  const btn   = form.querySelector('button');

  btn.textContent = 'Subscribing…';
  btn.disabled = true;

  try {
    const res = await fetch(NEWSLETTER_ENDPOINT, {
      method:  'POST',
      headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
      body:    JSON.stringify({ email })
    });

    if (res.ok) {
      btn.textContent = '✓ You\'re in!';
      btn.style.background = '#2D7D52';
      form.querySelector('input').value = '';
      setTimeout(() => {
        btn.textContent = 'Subscribe — it\'s free';
        btn.style.background = '';
        btn.disabled = false;
      }, 4000);
    } else {
      throw new Error('Submit failed');
    }
  } catch {
    btn.textContent = 'Try again';
    btn.style.background = '#c0392b';
    btn.disabled = false;
    setTimeout(() => {
      btn.textContent = 'Subscribe — it\'s free';
      btn.style.background = '';
    }, 3000);
  }
}

// ── Scroll Reveal ─────────────────────────────────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.pillar, .tutorial-card, .path-card, .pf-item, .course-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  revealObserver.observe(el);
});

// ── Active Nav Link ───────────────────────────────────────
function normalizePath(p) {
  if (!p) return '';
  if (!p.startsWith('/')) p = '/' + p;
  if (p.endsWith('/')) p += 'index.html';
  if (p === '/' || p === '') return '/index.html';
  return p;
}

const currentPath = normalizePath(window.location.pathname);
document.querySelectorAll('.nav-link').forEach(link => {
  const linkPath = normalizePath(link.pathname || link.getAttribute('href') || '');
  
  // Exact match or parent-child category section match (e.g. active parent folder when inside sub-tutorials)
  const isExact = (linkPath === currentPath);
  const isSection = (linkPath !== '/index.html' && currentPath.startsWith(linkPath.substring(0, linkPath.lastIndexOf('/') + 1)));
  
  if (isExact || isSection) {
    link.classList.add('active');
  } else {
    link.classList.remove('active');
  }
});


// ── Filter Buttons ────────────────────────────────────────
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const tag = btn.dataset.tag;
    document.querySelectorAll('.tutorial-card').forEach(card => {
      if (tag === 'all' || card.dataset.tag === tag) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// ── TOC Highlight ─────────────────────────────────────────
const tocLinks = document.querySelectorAll('.toc-list a');
if (tocLinks.length) {
  const headings = document.querySelectorAll('.tutorial-body h2, .tutorial-body h3');
  const tocObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        tocLinks.forEach(l => l.style.color = '');
        const active = document.querySelector(`.toc-list a[href="#${entry.target.id}"]`);
        if (active) active.style.color = 'var(--saffron)';
      }
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  headings.forEach(h => {
    if (h.id) tocObserver.observe(h);
  });
}
