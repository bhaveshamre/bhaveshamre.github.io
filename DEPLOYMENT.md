# Deployment Guide

## Overview

This guide explains how to deploy your portfolio to various platforms so it's accessible online.

## 🚀 GitHub Pages (Recommended - Free)

GitHub Pages is the easiest and most popular option for hosting portfolio websites.

### Prerequisites
- GitHub account
- Repository named `yourusername.github.io`
- Git installed locally

### Steps

1. **Create Repository**
   - Go to https://github.com/new
   - Repository name: `bhaveshamre.github.io` (exact format)
   - Make it Public
   - Click "Create repository"

2. **Push Code to GitHub**
   ```bash
   # Navigate to your project
   cd bhaveshamre.github.io
   
   # Initialize git (if not already done)
   git init
   
   # Add all files
   git add .
   
   # Commit changes
   git commit -m "Initial portfolio commit"
   
   # Add remote origin
   git remote add origin https://github.com/bhaveshamre/bhaveshamre.github.io.git
   
   # Push to GitHub
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "GitHub Pages" section
   - Select branch: `main`
   - Click "Save"
   - Your site is now live at: `https://bhaveshamre.github.io`

4. **Verify Deployment**
   - Wait 1-2 minutes
   - Visit your URL
   - Portfolio should be live!

### Custom Domain (Optional)
   - Go to Settings → GitHub Pages
   - Add your custom domain
   - Update DNS records with your domain provider
   - GitHub will show CNAME record details

---

## 🌐 Netlify (Drag & Drop - Free)

Netlify offers easy deployment with continuous updates.

### Steps

1. **Sign Up**
   - Go to https://www.netlify.com
   - Sign up with GitHub/Email

2. **Deploy**
   - Click "Add new site"
   - Choose "Deploy manually"
   - Drag and drop your project folder
   - Wait for deployment to complete

3. **Get URL**
   - Your site is live at generated URL
   - You can customize the subdomain

4. **Connect to GitHub (Recommended)**
   - Go to Site settings
   - Connect repository for auto-deployment
   - Every push to GitHub deploys automatically

---

## ⚡ Vercel (GitHub Integration - Free)

Vercel specializes in deploying static sites with CI/CD.

### Steps

1. **Sign Up**
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Import Project**
   - Click "New Project"
   - Select your GitHub repository
   - Click "Import"

3. **Deploy**
   - Vercel automatically builds and deploys
   - Your site is live instantly
   - URL: `yourproject.vercel.app`

4. **Auto-Deploy**
   - Every push to GitHub triggers automatic deployment
   - View deployment logs in dashboard

---

## 🔥 Firebase Hosting (Google - Free)

Firebase provides enterprise-grade hosting with Firebase services integration.

### Prerequisites
- Google Account
- Firebase CLI installed

### Steps

1. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   ```

2. **Initialize Firebase**
   ```bash
   firebase login
   firebase init hosting
   ```

3. **Configure**
   - Select "Use an existing project" or create new
   - Set public directory to current directory
   - Choose not to rewrite URLs (for static site)

4. **Deploy**
   ```bash
   firebase deploy
   ```

5. **Get URL**
   - Firebase provides hosting URL
   - Link shows in console

---

## ☁️ AWS S3 + CloudFront

AWS provides scalable hosting with CDN integration.

### Prerequisites
- AWS Account
- AWS CLI installed

### Steps

1. **Create S3 Bucket**
   ```bash
   aws s3 mb s3://bhaveshamre-portfolio
   ```

2. **Upload Files**
   ```bash
   aws s3 sync . s3://bhaveshamre-portfolio
   ```

3. **Enable Static Website Hosting**
   - Go to S3 bucket settings
   - Enable "Static website hosting"
   - Set index.html as index document

4. **Make Public**
   - Update bucket policy to allow public access

5. **Set Up CloudFront**
   - Create CloudFront distribution
   - Point to S3 bucket
   - Get CloudFront URL

---

## 🐳 Docker + Any Host

Deploy using Docker for consistency across environments.

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM nginx:latest
   COPY . /usr/share/nginx/html
   EXPOSE 80
   ```

2. **Build Docker Image**
   ```bash
   docker build -t bhavesh-portfolio .
   ```

3. **Run Locally**
   ```bash
   docker run -p 8080:80 bhavesh-portfolio
   ```

4. **Deploy to Hosting**
   - Push to Docker Hub
   - Deploy on DigitalOcean, Heroku, AWS ECS, etc.

---

## 📊 Domain Setup

### For Custom Domain

1. **Purchase Domain**
   - GoDaddy, Namecheap, Google Domains, etc.

2. **Update DNS Records**
   - For GitHub Pages:
     ```
     A record: 185.199.108.153
     A record: 185.199.109.153
     A record: 185.199.110.153
     A record: 185.199.111.153
     CNAME: www -> bhaveshamre.github.io
     ```

3. **Configure in Hosting**
   - Add domain in platform settings
   - Wait for DNS propagation (24-48 hours)

---

## 🔒 SSL/HTTPS

Most platforms provide free SSL certificates:
- ✅ GitHub Pages: Automatic
- ✅ Netlify: Automatic with Let's Encrypt
- ✅ Vercel: Automatic
- ✅ Firebase: Automatic
- ✅ AWS: Use ACM certificate

---

## 📈 Performance Tips

1. **Minify CSS/JS**
   - Use online minifiers
   - Reduce file sizes

2. **Compress Images**
   - Use ImageMagick or online tools
   - Smaller images = faster loading

3. **Enable Caching**
   - Set cache headers
   - Browsers cache assets locally

4. **Use CDN**
   - CloudFront, CloudFlare, etc.
   - Serve from nearest location

5. **Lazy Loading**
   - Defer loading offscreen images
   - Improves initial load time

---

## 🔍 SEO Optimization

### Add Meta Tags
```html
<meta name="description" content="Java Backend Engineer Portfolio">
<meta name="keywords" content="Java, Backend, Engineer, Portfolio">
<meta name="author" content="Bhavesh Amre">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta property="og:title" content="Bhavesh Amre Portfolio">
<meta property="og:description" content="Professional Java Backend Engineer">
<meta property="og:image" content="URL to preview image">
```

### Create Sitemap
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://bhaveshamre.github.io</loc>
    <lastmod>2026-11-02</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

### Add robots.txt
```
User-agent: *
Allow: /
Sitemap: https://bhaveshamre.github.io/sitemap.xml
```

---

## 🚨 Troubleshooting

### Site not deploying
- Check file structure
- Verify index.html exists
- Check for build errors

### DNS not resolving
- Wait 24-48 hours for propagation
- Verify DNS records are correct
- Check with `nslookup` or `dig`

### HTTPS not working
- Verify SSL certificate installed
- Wait for certificate generation
- Check domain in certificate settings

### Performance issues
- Optimize image sizes
- Enable caching
- Use CDN
- Minify CSS/JS

---

## 📚 Useful Resources

- [GitHub Pages Documentation](https://pages.github.com/)
- [Netlify Documentation](https://docs.netlify.com/)
- [Vercel Documentation](https://vercel.com/docs)
- [Firebase Hosting Guide](https://firebase.google.com/docs/hosting)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Let's Encrypt SSL](https://letsencrypt.org/)

---

**Version**: 1.0  
**Last Updated**: November 2, 2026
