# Ezmanw's Lair

A tiny hub for my HTML pages, served by GitHub Pages.

- Put any `.html` file in [`pages/`](pages) (drag & drop on GitHub: **Add file → Upload files**).
- On push, a workflow indexes `pages/` and redeploys. The hub lists every page with **Open** and **Copy link**.
- Each page's link is just `https://<user>.github.io/<repo>/pages/<file>.html`.

One-time setup: **Settings → Pages → Source: GitHub Actions**.

The hub also has a drop zone: paste a GitHub token (fine-grained, *Contents: read/write* on this repo) once and dropped files are committed straight to `pages/`.
