# Hermanos Mendez Construction Management (HMCM)

Static website. Canonical host: **https://hmcmfl.com**

No build step. Do **not** open `index.html` by double-clicking it. Paths are rooted at `/`, so a local server is required.

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

## Deploy

Upload the folder contents to any static host with `index.html` at the site root. This repo does not configure GitHub Pages, CNAME, or DNS.

## Contact

- 10002 N Forest Hills Dr, Tampa, FL 33612
- (813) 323-4648
- Monday–Friday 8:00 AM–5:00 PM
