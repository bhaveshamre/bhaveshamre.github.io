# Contributing to Bhavesh Amre's Portfolio

Thank you for your interest in contributing to this portfolio project! Contributions, issues, and feature requests are welcome.

## 📋 How to Contribute

### 1. Reporting Issues

If you find a bug or have a suggestion, please:

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - **Title**: Clear and descriptive
   - **Description**: Detailed explanation
   - **Steps to reproduce** (for bugs)
   - **Expected vs Actual behavior**
   - **Screenshots** (if applicable)

### 2. Feature Requests

Have an idea for improvement? Please:

1. Check existing issues/discussions
2. Create an issue labeled `enhancement`
3. Describe the feature and use case
4. Provide mockups or examples (optional)

### 3. Pull Requests

Want to contribute code? Follow these steps:

#### Fork & Clone
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/bhaveshamre.github.io.git
cd bhaveshamre.github.io
```

#### Create Branch
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-name
```

#### Make Changes
- Write clean, semantic code
- Follow existing code style
- Add comments for complex logic
- Test your changes thoroughly

#### Commit Changes
```bash
# Stage files
git add .

# Commit with descriptive message
git commit -m "Add: Description of changes"

# Examples:
# git commit -m "Add: Dark/Light mode toggle"
# git commit -m "Fix: Mobile navigation menu"
# git commit -m "Update: Skills section with new technologies"
```

#### Push & Create PR
```bash
# Push to your fork
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
# Link any related issues
# Provide detailed PR description
```

## 📝 Commit Message Guidelines

Follow conventional commits format:

```
type(scope): description

[optional body]
[optional footer]
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples:
```
feat(hero): Add animated background effects
fix(mobile): Resolve hamburger menu bug
docs(setup): Update installation instructions
style(colors): Improve CSS variable organization
refactor(projects): Simplify project card component
```

## 🎨 Design Guidelines

### Colors
- Primary: `#0066ff` (Blue)
- Secondary: `#00d4ff` (Cyan)
- Accent: `#10b981` (Green)
- Dark BG: `#0a0e27`
- Text Light: `#e0e0e0`

### Typography
- Font Family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- Headings: 800 weight
- Body: 400 weight
- Code: Monaco, monospace

### Spacing
- Use consistent padding/margins
- Follow 8px grid system
- Maintain visual hierarchy

### Responsive
- Test on mobile, tablet, desktop
- Use CSS media queries properly
- Ensure touch-friendly interactive elements

## 🧪 Testing Checklist

Before submitting PR:

- [ ] Works on Chrome, Firefox, Safari, Edge
- [ ] Responsive on mobile (320px), tablet (768px), desktop (1200px+)
- [ ] No console errors or warnings
- [ ] All links work correctly
- [ ] No broken images or assets
- [ ] Performance is acceptable (< 3s load time)
- [ ] Accessibility: Can navigate with keyboard
- [ ] Accessibility: Good contrast ratios

## 📚 Code Style

### HTML
```html
<!-- Use semantic HTML5 -->
<header>
<nav>
<main>
<section>
<footer>

<!-- Use data attributes for JS hooks -->
<button class="btn" data-action="submit">Submit</button>
```

### CSS
```css
/* Use CSS variables for colors/sizes */
:root {
  --primary: #0066ff;
  --spacing-sm: 0.5rem;
}

/* Use descriptive class names (BEM-style) */
.card { }
.card__header { }
.card__content { }
.card--featured { }

/* Group related properties */
.element {
  /* Display */
  display: flex;
  
  /* Box model */
  margin: 1rem;
  padding: 1rem;
  
  /* Sizing */
  width: 100%;
  
  /* Colors */
  background: var(--primary);
  color: white;
  
  /* Typography */
  font-size: 1rem;
  font-weight: 600;
  
  /* Other */
  transition: all 0.3s ease;
}
```

### JavaScript
```javascript
// Use descriptive variable names
const menuToggle = document.getElementById('navToggle');

// Use arrow functions
document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    // Handle click
  });
});

// Add comments for complex logic
// Close mobile menu when link is clicked
document.querySelectorAll('#navMenu a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('active');
  });
});
```

## 📖 Documentation

- Update README.md for user-facing changes
- Update SETUP.md for installation/customization changes
- Add inline code comments for complex logic
- Include examples in documentation

## 🚀 Contribution Ideas

Looking for ways to contribute? Consider:

- [ ] Add blog section with articles
- [ ] Implement dark/light mode toggle
- [ ] Add contact form with email backend
- [ ] Create downloadable resume/CV
- [ ] Add testimonials/recommendations section
- [ ] Implement project filtering by technology
- [ ] Add search functionality
- [ ] Improve SEO with structured data
- [ ] Add animation effects
- [ ] Performance optimizations
- [ ] Accessibility improvements
- [ ] Internationalization (multi-language)
- [ ] Add newsletter signup
- [ ] Create admin dashboard for updates

## ✅ Review Process

1. **Automated Checks**: GitHub Actions may run tests
2. **Code Review**: Maintainer reviews your PR
3. **Feedback**: Suggestions or changes may be requested
4. **Approval**: PR is approved and merged
5. **Recognition**: Contributors are acknowledged

## 🏆 Recognition

Contributors will be recognized in:
- README.md Contributors section
- GitHub insights
- Release notes (for significant contributions)

## ❓ Questions?

- Check README.md for overview
- Read SETUP.md for technical details
- Check existing issues for similar questions
- Create a discussion/issue for questions

## 📋 Code of Conduct

### Be Respectful
- Treat everyone with respect
- Welcome different perspectives
- Listen to constructive feedback

### Be Professional
- Use professional language
- Avoid offensive content
- Focus on technical merit

### Be Collaborative
- Help other contributors
- Share knowledge
- Work together toward goals

---

**Thank you for contributing! Your efforts help make this portfolio better for everyone.** 🙏

**Made with ❤️ by Bhavesh Amre**
