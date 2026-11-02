# Setup Instructions

## Prerequisites

Before setting up the portfolio locally, ensure you have:
- A modern web browser (Chrome, Firefox, Safari, Edge)
- A text editor (VS Code, Sublime Text, etc.)
- Optional: Git for version control
- Optional: Node.js for running local servers

## Installation Methods

### Method 1: Using Live Server (Easiest)

1. **Install VS Code Live Server Extension**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Click "Install" on the extension by Ritwick Dey

2. **Open the Portfolio**
   - Open the project folder in VS Code
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - Your portfolio will open in your browser automatically

### Method 2: Using Python

```bash
# Navigate to project directory
cd bhaveshamre.github.io

# Python 3.x
python -m http.server 8000

# Or Python 2.x
python -m SimpleHTTPServer 8000

# Open browser and go to
# http://localhost:8000
```

### Method 3: Using Node.js HTTP Server

```bash
# Install http-server globally (one-time)
npm install -g http-server

# Run server
http-server

# Open browser and go to
# http://localhost:8080
```

### Method 4: Using Git Clone

```bash
# Clone the repository
git clone https://github.com/bhaveshamre/bhaveshamre.github.io.git

# Navigate to directory
cd bhaveshamre.github.io

# Open index.html in your browser
# Double-click index.html or open it with your browser
```

## Customization Guide

### 1. Update Personal Information

Open `index.html` and modify:

```html
<!-- Header - Logo -->
<div class="logo">YOUR_INITIALS</div>

<!-- Hero Section -->
<h1>Hi, I'm <span>Your Name</span></h1>
<p>Your professional tagline here</p>

<!-- About Section -->
<h3>Your Title</h3>
<p>Your bio and description</p>
```

### 2. Update Contact Information

Find the contact section and update:
```html
<a href="mailto:your-email@example.com" class="contact-link">
    <i class="fas fa-envelope"></i> Email
</a>
```

### 3. Add Your Projects

Update the projects grid section:
```html
<div class="project-card">
    <div class="project-header">📱</div>
    <div class="project-content">
        <h3 class="project-title">Your Project Name</h3>
        <p class="project-description">Project description</p>
        <!-- Add project links -->
    </div>
</div>
```

### 4. Update Skills

Modify the skills section:
```html
<div class="skill-category">
    <h4>Your Category</h4>
    <div class="skill-list">
        <span class="skill-tag">Skill 1</span>
        <span class="skill-tag">Skill 2</span>
    </div>
</div>
```

### 5. Change Theme Colors

Edit CSS variables in the `<style>` section:
```css
:root {
    --primary: #0066ff;        /* Main blue */
    --secondary: #00d4ff;      /* Cyan accent */
    --accent: #10b981;         /* Green accent */
    --dark-bg: #0a0e27;        /* Dark background */
    --text-light: #e0e0e0;     /* Light text */
}
```

## File Structure Explanation

```
bhaveshamre.github.io/
│
├── index.html                 # Main portfolio file (all-in-one)
├── README.md                  # Repository documentation
├── SETUP.md                   # This setup guide
├── LICENSE                    # MIT License
│
├── assets/                    # Static assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── docs/                      # Documentation
│   ├── DEPLOYMENT.md         # How to deploy
│   └── STRUCTURE.md          # Detailed structure
│
└── projects/                  # Project details (optional)
    ├── urban-radius.md
    ├── agentsdr.md
    └── apache-ranger.md
```

## Browser Compatibility

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+

## Mobile Testing

Test on different devices using:
- Browser DevTools (F12 → Device Toolbar)
- Chrome Remote Desktop
- Physical devices
- BrowserStack or similar services

### Responsive Breakpoints
- Desktop: 1200px and above
- Tablet: 768px - 1199px
- Mobile: 480px - 767px
- Small Mobile: Below 480px

## Performance Optimization

1. **Minify CSS**: Use online minifiers for production
2. **Optimize Images**: Compress images before uploading
3. **Lazy Loading**: Implement for images and sections
4. **Caching**: Configure browser caching for faster loads

## Troubleshooting

### Issue: Images not loading
- **Solution**: Check image paths are correct relative to index.html
- Use `./` for relative paths

### Issue: Styles not applying
- **Solution**: Hard refresh browser (Ctrl+Shift+R)
- Clear browser cache
- Check CSS syntax for errors

### Issue: Links not working
- **Solution**: Verify href attributes are correct
- Use absolute URLs for external links

### Issue: Mobile menu not working
- **Solution**: Check JavaScript console for errors
- Ensure Font Awesome icons are loading

## Deployment

### Deploy to GitHub Pages (Free)

1. Push your code to GitHub:
```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

2. Go to repository settings
3. Enable GitHub Pages
4. Your portfolio is live at: `https://yourusername.github.io`

### Deploy to Other Platforms

- **Netlify**: Drag and drop the folder
- **Vercel**: Connect your GitHub repository
- **Firebase**: Follow Firebase hosting guide
- **AWS S3**: Upload HTML files to S3 bucket

## Getting Help

- Check browser console for errors (F12)
- Review the README.md for overview
- Check HTML comments in code
- Search Stack Overflow for similar issues
- Create an issue on GitHub repository

## Version History

- **v2.0** (Nov 2, 2026) - Modern responsive redesign
- **v1.0** (Original) - Initial portfolio release

---

**Need help?** Contact: amrebhavesh@gmail.com
