# Anand's Blog — Hugo + GitHub Pages

A personal blog built with [Hugo](https://gohugo.io/) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, hosted for free on GitHub Pages.

---

## 🚀 Setup Instructions

### Step 1: Install Hugo
- Mac: `brew install hugo`
- Windows: `winget install Hugo.Hugo.Extended`
- Linux: `sudo snap install hugo`

### Step 2: Set up the GitHub repo
1. Create a new repo on GitHub (e.g. `my-blog`)
2. Push this folder to the `main` branch
3. Add PaperMod as a submodule:
   ```bash
   git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
   ```

### Step 3: Enable GitHub Pages
1. Go to your repo → **Settings → Pages**
2. Set **Source** to **GitHub Actions**

### Step 4: Update `hugo.toml`
- Change `baseURL` to your domain (or `https://yourusername.github.io/my-blog/`)
- Update your name, social links, and description

### Step 5: Connect your custom domain (optional)
1. Buy a domain from [Porkbun](https://porkbun.com) or [Cloudflare](https://cloudflare.com/products/registrar/)
2. In your GitHub repo → Settings → Pages → Custom domain, enter your domain
3. Add a CNAME record in your DNS pointing to `yourusername.github.io`

---

## ✍️ Writing a New Blog Post

```bash
hugo new posts/my-new-post.md
```

Edit the file in `content/posts/my-new-post.md`, set `draft: false` when ready, then push to GitHub. It goes live automatically!

---

## 🗂️ Project Structure

```
anand-blog/
├── content/
│   ├── posts/          ← Your blog posts go here
│   └── about.md        ← About page
├── themes/PaperMod/    ← Theme (git submodule)
├── .github/workflows/  ← Auto-deploy on push
├── hugo.toml           ← Site configuration
└── archetypes/         ← Post templates
```

---

## 💰 Cost
| Item | Cost |
|------|------|
| Hugo | Free |
| GitHub Pages hosting | Free |
| PaperMod theme | Free |
| Custom domain | ~$10/year |
| **Total** | **~$10/year** |
