# Hermanos Mendez Construction Management (HMCM)

Static website. Canonical host: **https://hmcmfl.com**

Upload the folder contents to any static host with `index.html` at the site root. This repo does not configure GitHub Pages, CNAME, or DNS.

Do **not** open `index.html` by double-clicking it. Paths are rooted at `/`, so a local server is required.

## Preview on your computer

1. Unzip the site (or clone this repo) so you can see `index.html` in the folder.
2. Open a terminal **in that folder**.
3. Start a server:

```bash
python3 -m http.server 8080
```

On Windows, use:

```bat
py -m http.server 8080
```

4. In a browser, open http://localhost:8080
5. Leave the terminal open while you look. Stop with Ctrl+C.

If Python is not installed, install it from https://www.python.org/downloads/ (check “Add Python to PATH” on Windows), then retry the command.

## Regenerating HTML

Pages are generated. Do not hand-edit dozens of HTML files; they will be overwritten.

From the site root:

```bash
python3 tools/build.py
```

Optional check:

```bash
python3 tools/qa.py
```

Generators:

- `tools/chrome.py` — header, footer, meta, JSON-LD, NAP
- `tools/home_render.py` — home, About, Services
- `tools/pages.json` — interior page copy, photos, sidebars
- `tools/build.py` — writes HTML, `sitemap.xml`, `robots.txt`, `.htaccess`, contact, 404, redirects, HTML site map

## NAP (source of truth: Google Maps listing)

- Hermanos Mendez Construction Management
- 10002 N Forest Hills Dr, Tampa, FL 33612
- (813) 323-4648
- Monday–Friday 8:00 AM–5:00 PM
- Maps: linked from the footer and contact page

Legal name **Hermanos Mendez Construction Management, LLC** appears in schema (`legalName`) only.

No email address is published. Phone is the contact path.

## Host security

The zip includes `.htaccess` (Apache / cPanel / many GoDaddy plans) and `_headers` (Netlify-style hosts). Those send HTTPS-only, no framing, no MIME sniffing, a tight Content-Security-Policy, and a referrer policy. Turn on HTTPS in the host panel; the rewrite only helps if the server is Apache with `mod_rewrite`. Python’s local preview server ignores both files.

## Logos

Header and footer use `/assets/logo-light.png` (white HMCM wordmark + arc, transparent). Dark lockup: `/assets/logo.png`. Open Graph and apple-touch-icon should match that wordmark.
