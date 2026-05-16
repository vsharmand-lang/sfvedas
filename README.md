# SFVedas

**Deep Salesforce Knowledge for Tech Leaders**

> "Just as the ancient Vedas were the deepest repository of knowledge in their time — SFVedas is the deepest repository of Salesforce knowledge for today's tech leaders."

## 🌐 Live Site
[sfvedas.com](https://sfvedas.com)

## 👤 Instructor & Founder
Vishal Sharma

## 📁 Site Structure

```
sfvedas/
├── index.html              ← Homepage
├── css/
│   └── main.css            ← All styles
├── js/
│   └── main.js             ← All JavaScript
├── pages/
│   ├── tutorials.html      ← Tutorials listing
│   ├── learning-paths.html ← Learning paths
│   ├── courses.html        ← Premium courses
│   └── about.html          ← About page
└── tutorials/
    ├── multi-tenant.html         ← Tutorial 1
    ├── governor-limits.html      ← Tutorial 2 (add when ready)
    └── platform-vs-product.html  ← Tutorial 3 (add when ready)
```

## 🚀 Deploy to GitHub Pages

1. Create a new GitHub repository named `sfvedas` (or your username.github.io)
2. Upload all files maintaining the folder structure above
3. Go to Settings → Pages → Source: Deploy from branch → main → / (root)
4. Your site will be live at `https://yourusername.github.io/sfvedas`
5. Add your custom domain `sfvedas.com` in Settings → Pages → Custom domain
6. Add a CNAME record in GoDaddy DNS pointing to `yourusername.github.io`

## 📝 Adding New Tutorials

1. Create a new `.html` file in the `/tutorials` folder
2. Copy the structure from `multi-tenant.html`
3. Update the content, title, meta description
4. Add the tutorial card to `pages/tutorials.html`
5. Add it to the relevant learning path in `pages/learning-paths.html`
6. Commit and push — GitHub Pages deploys automatically

## 💰 Adding Payments (Gumroad)

1. Create your course on [gumroad.com](https://gumroad.com)
2. Get your Gumroad product link
3. Replace the "Join Waitlist" buttons in `pages/courses.html` with your Gumroad link
4. Add `<script src="https://gumroad.com/js/gumroad.js"></script>` before `</body>`

## 🎨 Brand Colours

| Colour | Hex |
|--------|-----|
| Saffron Gold | `#E8930A` |
| Deep Navy | `#0D1B2A` |
| Off White | `#F8F5F0` |
| Deep Charcoal | `#1E1E2E` |
| Salesforce Blue | `#0070D2` |
| Sage Green | `#2D7D52` |

## 📖 Brand Fonts (all free via Google Fonts)

- **Display/Hero:** Fraunces
- **Section Headings:** DM Serif Display
- **Body/Tutorial:** Source Serif 4
- **Code:** JetBrains Mono
- **UI/Buttons:** DM Sans

---

*Ancient wisdom. Modern Salesforce.*
