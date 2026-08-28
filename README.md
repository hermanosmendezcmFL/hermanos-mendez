# Hermanos Mendez Construction Management, LLC

Static website for **HMCM** — consulting, construction management, and project management for land development and construction in Tampa Bay.

Canonical host: **https://hmcmfl.com**

This repo is portable HTML, CSS, JavaScript, and assets. There is no build step.

## Local preview

Serve the folder (root-relative URLs need a local server, not `file://`):

```bash
python3 -m http.server 8080 --directory .
```

Then open http://localhost:8080

## Deploy

Upload the repository contents (keep the folder structure) to any static host — GoDaddy, cPanel, Netlify, Cloudflare Pages, S3, etc. `index.html` must sit at the host’s site root so `https://hmcmfl.com/` serves the home page.

Pages:

- `/` English home
- `/about/`, `/services/`, `/services/consulting/`, `/services/construction-management/`, `/services/project-management/`, `/contact/`
- `/es/` Spanish home and matching routes (`/es/empresa/`, `/es/servicios/`, `/es/contacto/`, …)

`robots.txt` and `sitemap.xml` use `https://hmcmfl.com/` URLs. Point the domain’s DNS at your host when you are ready (not in this repo).

## SEO on this site

On-page: unique titles and meta descriptions, canonical + hreflang, Open Graph, JSON-LD LocalBusiness, semantic HTML, internal links between pages.

**Off-site (not in this repo):** Google Business Profile, citations, and real inbound links from other sites. Those have to be managed separately.

## Contact (Google listing)

- Hermanos Mendez Construction Management
- 10002 N Forest Hills Dr, Tampa, FL 33612
- (813) 323-4648
- Monday–Friday 8:00 AM–5:00 PM; Saturday–Sunday closed
