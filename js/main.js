/* SFVedas — Main JavaScript */

// ── Theme Toggle ──────────────────────────────────────────
const themeToggle = document.getElementById('themeToggle');
const themeIcon   = themeToggle?.querySelector('.theme-icon');
const body        = document.body;

const savedTheme = localStorage.getItem('sfvedas-theme') || 'light';
if (savedTheme === 'dark') {
  body.classList.add('dark-mode');
  if (themeIcon) themeIcon.textContent = '☾';
}

themeToggle?.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  const isDark = body.classList.contains('dark-mode');
  if (themeIcon) themeIcon.textContent = isDark ? '☾' : '☀';
  localStorage.setItem('sfvedas-theme', isDark ? 'dark' : 'light');
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
function handleNewsletter(e) {
  e.preventDefault();
  const form  = e.target;
  const email = form.querySelector('input[type="email"]').value;
  const btn   = form.querySelector('button');
  btn.textContent = '✓ Subscribed!';
  btn.style.background = '#2D7D52';
  btn.disabled = true;
  form.querySelector('input').value = '';
  setTimeout(() => {
    btn.textContent = 'Subscribe Free';
    btn.style.background = '';
    btn.disabled = false;
  }, 3000);
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
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link').forEach(link => {
  const href = link.getAttribute('href')?.split('/').pop();
  if (href === currentPage) {
    link.classList.add('active');
  }
});

// ── Quiz Functionality ────────────────────────────────────
function initQuiz() {
  const quizForms = document.querySelectorAll('.quiz-form');
  quizForms.forEach(form => {
    const submit = form.querySelector('.quiz-submit');
    const result = form.querySelector('.quiz-result');
    submit?.addEventListener('click', () => {
      const questions = form.querySelectorAll('.quiz-question');
      let correct = 0; let total = 0;
      questions.forEach(q => {
        total++;
        const options   = q.querySelectorAll('.quiz-option');
        const selected  = q.querySelector('.quiz-option.selected');
        const correctAns = q.dataset.correct;
        options.forEach(o => {
          if (o.dataset.value === correctAns) o.classList.add('correct');
        });
        if (selected?.dataset.value === correctAns) {
          correct++;
        } else if (selected) {
          selected.classList.add('incorrect');
        }
      });
      if (result) {
        result.classList.add('show');
        const pct = Math.round((correct / total) * 100);
        if (pct >= 70) {
          result.classList.add('pass');
          result.textContent = `✓ Well done! You scored ${correct}/${total} (${pct}%). You've grasped the key concepts.`;
        } else {
          result.classList.add('fail');
          result.textContent = `✗ You scored ${correct}/${total} (${pct}%). Review the tutorial and try again.`;
        }
        submit.disabled = true;
      }
    });
    form.querySelectorAll('.quiz-option').forEach(opt => {
      opt.addEventListener('click', () => {
        const q = opt.closest('.quiz-question');
        q.querySelectorAll('.quiz-option').forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');
        opt.style.borderColor = 'var(--saffron)';
        opt.style.background  = 'rgba(232,147,10,0.08)';
        q.querySelectorAll('.quiz-option').forEach(o => {
          if (!o.classList.contains('selected')) {
            o.style.borderColor = '';
            o.style.background  = '';
          }
        });
      });
    });
  });
}
initQuiz();

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
