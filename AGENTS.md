# jorgeav527 — personal site

Static site: **Zola 0.22** + **Tailwind v4** (CSS-only, no JS bundler).

## Quick start

```sh
make setup       # npm install + download Zola binary
make dev         # zola serve + Tailwind watch (concurrent)
make build       # zola build + Tailwind minify
```

## Build quirks

- Output dir is `docs/` (not `public/`). Set in `config.toml`.
- Production CSS goes to `docs/style.css`; dev CSS to `static/style.css`.
- `compile_sass = false` in config — Tailwind v4 replaces Sass.
- Prettier formats Tera templates via `prettier-plugin-tera`.

## Deploy

- GitHub Actions on `main` push: build → commit updated `docs/` back to `main`.
- No other branches are built/deployed.

## Content

- Zola sections: `content/posts/`, `content/blog/`, `content/projects/`
- Templates in `templates/` (Tera, `.html` files)
- Custom shortcodes in `templates/shortcodes/`
- Theme: Catppuccin Mocha (dark) / Latte (light), toggled via localStorage.

## Tests

- `npm test` is a placeholder — no tests in this repo.
- No lint/typecheck step for site code.
