# Project Overview

This is a personal portfolio and blog built using **Zola** (a static site generator written in Rust) and **Tailwind CSS v4**. It showcases the professional profile, blog posts, code-related articles, and projects of **Jorge Alarcon**.

## Tech Stack
- **Static Site Generator:** [Zola](https://www.getzola.org/)
- **Styling:** [Tailwind CSS v4](https://tailwindcss.com/) with `@tailwindcss/typography`
- **Theme:** Catppuccin (supporting both light and dark modes)
- **Runtime:** Node.js (for Tailwind CLI and build scripts)

# Building and Running

The project uses `npm` scripts to manage the build process and development server.

### Development
To start the development server with live reloading for both Zola and Tailwind CSS:
```bash
npm run serve
```
This command runs `zola serve` and `npx @tailwindcss/cli` in watch mode concurrently.

### Build
To generate the final static site:
```bash
npm run build
```
This command:
1. Runs `zola build` to generate the HTML.
2. Compiles and minifies Tailwind CSS from `static/input.css` to `docs/style.css`.

**Note:** The output directory is configured as `docs/` in `zola.toml`, making it compatible with GitHub Pages.

# Development Conventions

### Content Structure
Content is organized into sections within the `content/` directory:
- `blog/`: General blog posts.
- `posts/`: Technical or code-related articles.
- `projects/`: Showcases of personal or professional projects.

Each section has an `_index.md` file that defines its metadata, sorting (usually by date), and templates.

### Templates
Templates are written in Tera (Zola's templating engine) and located in `templates/`:
- `base.html`: The core layout containing the `<head>`, navbar, and footer.
- `index.html`: The homepage.
- `partials/`: Reusable components like `navbar.html`, `footer.html`, and `theme_toggle.html`.
- Subdirectories for sections (e.g., `blog/`, `posts/`, `projects/`) contain `list.html` and `single.html` templates.

### Styling
- **Tailwind v4:** Styling is managed through `static/input.css` using the new `@theme` block to define custom tokens and `@layer base` for global styles.
- **Theme Toggling:** The site supports light and dark modes via a `data-theme` attribute on the `<html>` element, managed by `templates/partials/theme_toggle.html` and a small script in `base.html`.
- **Typography:** The `@tailwindcss/typography` plugin is used for styling Markdown content via the `.prose-catppuccin` class.

### Assets
- Static assets (icons, global CSS) are in `static/`.
- Content-specific assets (images for posts) can be placed directly in the post's directory (e.g., `content/posts/hello_world/meme_1.png`).
