#!/usr/bin/env python3
import json, sys
from pathlib import Path
from html import escape as esc
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chrome import (
    T, CANON, PHONE_DISP, PHONE_TEL, LEGAL, BRAND, ADDR1, CITY, MAPS,
    wrap_page, page_banner, crumbs_html,
)

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = []

def write(path, html, sitemap=True):
    dest = ROOT / path.lstrip("/")
    if path.endswith("/"):
        dest = dest / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    if sitemap:
        SITEMAP.append(path if path.endswith("/") or path.endswith(".html") else path + "/")

def pjoin(ps):
    return "\n".join("            <p>%s</p>" % p for p in ps)

def aside(lang, links, heading=None):
    t = T[lang]
    items = "\n".join('          <li><a href="%s">%s</a></li>' % (h, esc(n)) for n, h in links)
    return (
        '        <aside class="aside-box">\n'
        "          <h2>%s</h2>\n"
        "          <ul>\n%s\n          </ul>\n"
        "        </aside>"
    ) % (heading or t["related"], items)

def related_grid(items):
    cards = []
    for n, h, d in items:
        cards.append('          <a href="%s"><h3>%s</h3><p>%s</p></a>' % (h, esc(n), d))
    return '<div class="related">\n' + "\n".join(cards) + "\n        </div>"

def interior_body(lang, crumbs, h1, lead, photo, paras, links, related, aside_h=None):
    t = T[lang]
    contact = "/contact/" if lang == "en" else "/es/contacto/"
    body = page_banner(lang, crumbs, h1, lead, photo)
    body += (
        '\n    <section class="section section--rule">\n'
        '      <div class="wrap content-grid">\n'
        '        <div class="prose">\n%s\n        </div>\n%s\n'
        "      </div>\n    </section>"
    ) % (pjoin(paras), aside(lang, links, aside_h))
    if related:
        body += (
            '\n    <section class="section section--stone">\n'
            '      <div class="wrap">\n'
            '        <p class="section-kicker">%s</p>\n'
            "        <h2>%s</h2>\n        %s\n"
            "      </div>\n    </section>"
        ) % (t["on_this"], t["related"], related_grid(related))
    body += (
        '\n    <section class="section section--ink">\n'
        '      <div class="wrap cta-band">\n'
        "        <h2>%s</h2>\n"
        '        <div class="hero-actions">\n'
        '          <a class="btn btn-primary" href="tel:%s">%s</a>\n'
        '          <a class="btn btn-ghost" href="%s">%s</a>\n'
        "        </div>\n      </div>\n    </section>"
    ) % (PHONE_DISP, PHONE_TEL, t["call_now"], contact, t["contact_cta"])
    return body

def build_from_json():
    pages = json.loads((Path(__file__).parent / "pages.json").read_text())["pages"]
    for pg in pages:
        if pg["en_path"] == "/about/":
            continue
        en, es = pg["en"], pg["es"]
        write(pg["en_path"], wrap_page(
            "en", pg["en_path"], pg["es_path"], pg["nav"], en["title"], en["desc"],
            interior_body("en", pg["crumbs_en"], en["h1"], en["lead"], pg["photo"], en["paras"], en["links"], en.get("related"), en.get("aside_h")),
        ))
        write(pg["es_path"], wrap_page(
            "es", pg["es_path"], pg["en_path"], pg["nav"], es["title"], es["desc"],
            interior_body("es", pg["crumbs_es"], es["h1"], es["lead"], pg["photo"], es["paras"], es["links"], es.get("related"), es.get("aside_h")),
        ))

def build_contact():
    embed = "https://www.google.com/maps?q=28.0402677,-82.4727936&z=17&output=embed"
    hours = {
        "en": [("Monday","8:00 AM-5:00 PM"),("Tuesday","8:00 AM-5:00 PM"),("Wednesday","8:00 AM-5:00 PM"),("Thursday","8:00 AM-5:00 PM"),("Friday","8:00 AM-5:00 PM"),("Saturday","Closed"),("Sunday","Closed")],
        "es": [("Lunes","8:00 a. m.-5:00 p. m."),("Martes","8:00 a. m.-5:00 p. m."),("Miercoles","8:00 a. m.-5:00 p. m."),("Jueves","8:00 a. m.-5:00 p. m."),("Viernes","8:00 a. m.-5:00 p. m."),("Sabado","Cerrado"),("Domingo","Cerrado")],
    }
    # use proper accents in ES via unicode
    hours["es"] = [
        ("Lunes", "8:00 a. m.-5:00 p. m."),
        ("Martes", "8:00 a. m.-5:00 p. m."),
        ("Mi\u00e9rcoles", "8:00 a. m.-5:00 p. m."),
        ("Jueves", "8:00 a. m.-5:00 p. m."),
        ("Viernes", "8:00 a. m.-5:00 p. m."),
        ("S\u00e1bado", "Cerrado"),
        ("Domingo", "Cerrado"),
    ]
    for lang, path, pair, title, desc, h1, lead, p1 in [
        ("en","/contact/","/es/contacto/","Contact HMCM in Tampa | (813) 323-4648",
         "Contact Hermanos Mendez Construction Management: 10002 N Forest Hills Dr, Tampa, FL 33612. (813) 323-4648. Monday-Friday 8:00 AM-5:00 PM.",
         "Get in Touch",
         "Call the office. We are in Tampa, with free on-site parking.",
         "Call <a href=\"tel:%s\">%s</a>. There is no email published on this website." % (PHONE_TEL, PHONE_DISP)),
        ("es","/es/contacto/","/contact/","Contacto HMCM en Tampa | (813) 323-4648",
         "Contacto de Hermanos Mendez Construction Management: 10002 N Forest Hills Dr, Tampa, FL 33612. (813) 323-4648. Lunes a viernes, 8:00 a. m. a 5:00 p. m.",
         "P\u00f3ngase en contacto",
         "El telefono es la via principal. La oficina esta en Tampa, con estacionamiento gratuito en el sitio.",
         "Llame al <a href=\"tel:%s\">%s</a>. En este sitio no se publica correo electronico." % (PHONE_TEL, PHONE_DISP)),
    ]:
        t = T[lang]
        crumbs = [("Home","/"),("Contact", None)] if lang=="en" else [("Inicio","/es/"),("Contacto", None)]
        if lang == "es":
            h1 = "P\u00f3ngase en contacto"
            lead = "Llame a la oficina. Estamos en Tampa, con estacionamiento gratuito en el sitio."
            p1 = "Llame al <a href=\"tel:%s\">%s</a>. En este sitio no se publica correo electr\u00f3nico." % (PHONE_TEL, PHONE_DISP)
        lis = "\n".join("            <li><span>%s</span><span>%s</span></li>" % (d,h) for d,h in hours[lang])
        hours_h = "Hours" if lang=="en" else "Horario"
        map_t = "Map" if lang=="en" else "Mapa"
        body = page_banner(lang, crumbs, h1, lead, "tampa.jpg")
        body += (
            '\n    <section class="section section--rule">\n'
            '      <div class="wrap contact-strip">\n'
            '        <div class="prose">\n'
            "          <p>%s</p>\n"
            '          <address class="addr">%s<br>%s<br>%s</address>\n'
            '          <p><a class="map-link" href="%s" rel="noopener noreferrer" target="_blank">%s</a></p>\n'
            "          <p>%s</p>\n"
            '          <p><a class="btn btn-ink" href="tel:%s">%s</a></p>\n'
            "        </div>\n        <div>\n"
            "          <h2>%s</h2>\n"
            '          <ul class="hours-list">\n%s\n          </ul>\n'
            "        </div>\n      </div>\n    </section>\n"
            '    <section class="section section--stone">\n'
            '      <div class="wrap">\n'
            '        <iframe class="map-embed" title="%s" src="%s" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
            "      </div>\n    </section>"
        ) % (p1, BRAND, ADDR1, CITY, MAPS, t["maps"], t["parking"], PHONE_TEL, PHONE_DISP, hours_h, lis, map_t, embed)
        write(path, wrap_page(lang, path, pair, "contact", title, desc, body))

def build_404():
    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"utf-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "  <title>Page not found | HMCM</title>\n"
        "  <meta name=\"robots\" content=\"noindex\">\n"
        "  <meta name=\"theme-color\" content=\"#171614\">\n"
        "  <link rel=\"icon\" href=\"/assets/favicon.svg\" type=\"image/svg+xml\">\n"
        "  <link rel=\"stylesheet\" href=\"/css/styles.css\">\n"
        "</head>\n<body>\n"
        "  <main id=\"main\" class=\"section\">\n    <div class=\"wrap\">\n"
        "      <p class=\"section-kicker\">404</p>\n"
        "      <h1>This page is not on HMCMFL.com.</h1>\n"
        "      <p class=\"prose\"><a href=\"/\">Home</a> \u00b7 <a href=\"/consulting/\">Consulting</a> \u00b7 "
        "<a href=\"/construction-management/\">Construction Management</a> \u00b7 "
        "<a href=\"/project-management/\">Project Management</a> \u00b7 "
        "<a href=\"/contact/\">Contact</a> \u00b7 <a href=\"/es/\">Espa\u00f1ol</a></p>\n"
        "      <p><a class=\"btn btn-ink\" href=\"tel:+18133234648\">(813) 323-4648</a></p>\n"
        "    </div>\n  </main>\n</body>\n</html>\n"
    )
    write("/404.html", html, sitemap=False)

def build_redirects():
    mapping = [
        ("/services/consulting/", "/consulting/"),
        ("/services/construction-management/", "/construction-management/"),
        ("/services/project-management/", "/project-management/"),
        ("/es/servicios/consultoria/", "/es/consultoria/"),
        ("/es/servicios/gerencia-de-construccion/", "/es/gerencia-de-construccion/"),
        ("/es/servicios/gerencia-de-proyectos/", "/es/gerencia-de-proyectos/"),
    ]
    for old, new in mapping:
        html = (
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "  <meta charset=\"utf-8\">\n"
            "  <meta http-equiv=\"refresh\" content=\"0;url=%s\">\n"
            "  <link rel=\"canonical\" href=\"%s%s\">\n"
            "  <title>Moved</title>\n"
            "  <script>location.replace(%r);</script>\n"
            "</head>\n<body>\n  <p>Moved to <a href=\"%s\">%s</a>.</p>\n</body>\n</html>\n"
        ) % (new, CANON, new, new, new, new)
        write(old, html, sitemap=False)

def build_meta():
    (ROOT / ".htaccess").write_text(
        "DirectoryIndex index.html\nErrorDocument 404 /404.html\n"
        "Redirect 301 /services/consulting/ /consulting/\n"
        "Redirect 301 /services/construction-management/ /construction-management/\n"
        "Redirect 301 /services/project-management/ /project-management/\n"
        "Redirect 301 /es/servicios/consultoria/ /es/consultoria/\n"
        "Redirect 301 /es/servicios/gerencia-de-construccion/ /es/gerencia-de-construccion/\n"
        "Redirect 301 /es/servicios/gerencia-de-proyectos/ /es/gerencia-de-proyectos/\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://hmcmfl.com/sitemap.xml\n", encoding="utf-8")
    urls = []
    seen = set()
    for pth in SITEMAP:
        if pth in seen or pth == "/404.html":
            continue
        seen.add(pth)
        urls.append(CANON + ("/" if pth == "/" else pth))
    urls = sorted(set(urls), key=lambda u: (u != CANON + "/", u))
    parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        parts += ["  <url>", "    <loc>%s</loc>" % u, "  </url>"]
    parts.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(parts) + "\n", encoding="utf-8")
    return urls

if __name__ == "__main__":
    # home imported after definition in home_render
    from home_render import build_homes, build_about, build_services
    build_homes(write, wrap_page)
    build_about(write, wrap_page)
    build_services(write, wrap_page)
    build_from_json()
    build_contact()
    build_404()
    build_redirects()
    urls = build_meta()
    print("sitemap", len(urls))
    for u in urls:
        print(u)
