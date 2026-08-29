"""Shared chrome for the HMCM static site generator."""
from html import escape as esc
import json

CANON = "https://hmcmfl.com"
PHONE_DISP = "(813) 323-4648"
PHONE_TEL = "+18133234648"
LEGAL = "Hermanos Mendez Construction Management, LLC"
BRAND = "Hermanos Mendez Construction Management"
ADDR1 = "10002 N Forest Hills Dr"
CITY = "Tampa, FL 33612"
MAPS = (
    "https://www.google.com/maps/place/Hermanos+Mendez+Construction+Management/"
    "@28.0402677,-82.4727936,17z/data=!3m1!4b1!4m6!3m5!1s0x88c2c767a36add95:"
    "0x2d8aed95d58b19cb!8m2!3d28.0402677!4d-82.4727936!16s%2Fg%2F11sxx79tct"
)
LAT = 28.0402677
LNG = -82.4727936
OG = f"{CANON}/assets/og.png"

T = {
    "en": {
        "skip": "Skip to content",
        "menu": "Menu",
        "primary": "Primary",
        "lang": "Language",
        "call": f"Call {PHONE_DISP}",
        "home": "Home",
        "about_us": "About Us",
        "services": "Services",
        "consulting": "Consulting",
        "overview": "Overview",
        "commercial": "Commercial",
        "residential": "Residential",
        "other_group": "Other Consulting Services",
        "specialized_group": "Specialized Consulting Services",
        "partner_solutions": "Partner Solutions",
        "cm": "Construction Management",
        "pm": "Project Management",
        "specialties": "Specialties",
        "industries": "Industries",
        "contact": "Contact",
        "company": "Company",
        "about": "About",
        "hours": "Monday–Friday 8:00 AM–5:00 PM. Saturday–Sunday closed.",
        "hours_short": "Mon–Fri 8:00 AM–5:00 PM",
        "maps": "Open in Google Maps",
        "parking": "Free on-site parking",
        "domain": "HMCMFL.com",
        "es_label": "Español",
        "copy": "© 2026 HMCM",
        "see": "View",
        "cta_services": "See Services",
        "related": "Related",
        "on_this": "More",
        "call_now": "Call Now",
        "contact_cta": "Get in Touch",
        "visit": "Visit the office",
        "breadcrumb": "Breadcrumb",
        "other_items": [
            ("Efficiency Evaluations and Implementations", "/consulting/other/efficiency-evaluations/"),
            ("Systems Evaluations and Implementations", "/consulting/other/systems-evaluations/"),
            ("Business Development", "/consulting/other/business-development/"),
            ("Special Projects", "/consulting/other/special-projects/"),
            ("Takeoff Support and Contract Negotiations", "/consulting/other/takeoff-support/"),
            ("Purchasing Assistance", "/consulting/other/purchasing-assistance/"),
            ("SOP and Employee Management", "/consulting/other/sop-employee-management/"),
        ],
        "specialized_items": [
            ("Failing Asset Evaluation", "/consulting/other/failing-asset-evaluation/"),
            ("Special Projects", "/consulting/other/special-projects/"),
            ("Distress & Stalled Project Support", "/consulting/other/distress-stalled-project-support/"),
        ],
        "specs": [
            ("Land Development", "/specialties/land-development/"),
            ("New Construction", "/specialties/new-construction/"),
            ("Renovation", "/specialties/renovation/"),
            ("Demolition", "/specialties/demolition/"),
        ],
        "inds": [
            ("Commercial", "/industries/commercial/"),
            ("Multi-Family", "/industries/multi-family/"),
            ("SFR (Single-Family Residential)", "/industries/sfr/"),
            ("Custom Build", "/industries/custom-build/"),
            ("Land Clearing", "/industries/land-clearing/"),
            ("Stormwater Mitigation", "/industries/stormwater-mitigation/"),
            ("Permitting", "/industries/permitting/"),
            ("Inspections", "/industries/inspections/"),
            ("Design-Build", "/industries/design-build/"),
        ],
    },
    "es": {
        "skip": "Saltar al contenido",
        "menu": "Menú",
        "primary": "Principal",
        "lang": "Idioma",
        "call": f"Llamar {PHONE_DISP}",
        "home": "Inicio",
        "about_us": "Empresa",
        "services": "Servicios",
        "consulting": "Consultoría",
        "overview": "Resumen",
        "commercial": "Comercial",
        "residential": "Residencial",
        "other_group": "Otros servicios de consultoría",
        "specialized_group": "Consultoría especializada",
        "partner_solutions": "Soluciones para socios",
        "cm": "Gerencia de construcción",
        "pm": "Gerencia de proyectos",
        "specialties": "Especialidades",
        "industries": "Industrias",
        "contact": "Contacto",
        "company": "Empresa",
        "about": "Empresa",
        "hours": "Lunes a viernes, 8:00 a. m. a 5:00 p. m. Sábado y domingo cerrado.",
        "hours_short": "Lun–vie 8:00 a. m.–5:00 p. m.",
        "maps": "Abrir en Google Maps",
        "parking": "Estacionamiento gratuito en el sitio",
        "domain": "HMCMFL.com",
        "es_label": "English",
        "copy": "© 2026 HMCM",
        "see": "Ver",
        "cta_services": "Ver servicios",
        "related": "Relacionado",
        "on_this": "Más",
        "call_now": "Llamar ahora",
        "contact_cta": "Póngase en contacto",
        "visit": "Visitar la oficina",
        "breadcrumb": "Miga de pan",
        "other_items": [
            ("Evaluaciones e implementaciones de eficiencia", "/es/consultoria/otros/evaluaciones-de-eficiencia/"),
            ("Evaluaciones e implementaciones de sistemas", "/es/consultoria/otros/evaluaciones-de-sistemas/"),
            ("Desarrollo de negocios", "/es/consultoria/otros/desarrollo-de-negocios/"),
            ("Proyectos especiales", "/es/consultoria/otros/proyectos-especiales/"),
            ("Soporte de takeoff y negociación de contratos", "/es/consultoria/otros/soporte-de-estimacion/"),
            ("Asistencia en compras", "/es/consultoria/otros/asistencia-en-compras/"),
            ("SOP y gestión de empleados", "/es/consultoria/otros/sop-gestion-de-empleados/"),
        ],
        "specialized_items": [
            ("Evaluación de activos en deterioro", "/es/consultoria/otros/evaluacion-de-activos-en-deterioro/"),
            ("Proyectos especiales", "/es/consultoria/otros/proyectos-especiales/"),
            ("Apoyo a proyectos en dificultades o detenidos", "/es/consultoria/otros/apoyo-a-proyectos-en-dificultades/"),
        ],
        "specs": [
            ("Desarrollo de terrenos", "/es/especialidades/desarrollo-de-terrenos/"),
            ("Nueva construcción", "/es/especialidades/nueva-construccion/"),
            ("Renovación", "/es/especialidades/renovacion/"),
            ("Demolición", "/es/especialidades/demolicion/"),
        ],
        "inds": [
            ("Comercial", "/es/industrias/comercial/"),
            ("Multifamiliar", "/es/industrias/multifamiliar/"),
            ("Residencial unifamiliar (SFR)", "/es/industrias/sfr/"),
            ("Construcción a medida", "/es/industrias/construccion-a-medida/"),
            ("Despeje de terrenos", "/es/industrias/despeje-de-terrenos/"),
            ("Mitigación de aguas pluviales", "/es/industrias/mitigacion-de-aguas-pluviales/"),
            ("Permisos", "/es/industrias/permisos/"),
            ("Inspecciones", "/es/industrias/inspecciones/"),
            ("Diseño-construcción", "/es/industrias/diseno-construccion/"),
        ],
    },
}

OFFERS = [
    ("Consulting", f"{CANON}/consulting/"),
    ("Commercial consulting", f"{CANON}/consulting/commercial/"),
    ("Residential consulting", f"{CANON}/consulting/residential/"),
    ("Construction Management", f"{CANON}/construction-management/"),
    ("Project Management", f"{CANON}/project-management/"),
    ("Efficiency Evaluations and Implementations", f"{CANON}/consulting/other/efficiency-evaluations/"),
    ("Systems Evaluations and Implementations", f"{CANON}/consulting/other/systems-evaluations/"),
    ("Business Development", f"{CANON}/consulting/other/business-development/"),
    ("Special Projects", f"{CANON}/consulting/other/special-projects/"),
    ("Takeoff Support and Contract Negotiations", f"{CANON}/consulting/other/takeoff-support/"),
    ("Purchasing Assistance", f"{CANON}/consulting/other/purchasing-assistance/"),
    ("SOP and Employee Management", f"{CANON}/consulting/other/sop-employee-management/"),
    ("Failing Asset Evaluation", f"{CANON}/consulting/other/failing-asset-evaluation/"),
    ("Distress & Stalled Project Support", f"{CANON}/consulting/other/distress-stalled-project-support/"),
    ("Land Development", f"{CANON}/specialties/land-development/"),
    ("New Construction", f"{CANON}/specialties/new-construction/"),
    ("Renovation", f"{CANON}/specialties/renovation/"),
    ("Demolition", f"{CANON}/specialties/demolition/"),
]


def jsonld(page_url, page_name, lang, crumbs=None):
    catalog = {
        "@type": "OfferCatalog",
        "name": "Services",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": u}}
            for n, u in OFFERS
        ],
    }
    business = {
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{CANON}/#business",
        "name": BRAND,
        "legalName": LEGAL,
        "alternateName": "HMCM",
        "url": f"{CANON}/",
        "telephone": "+1-813-323-4648",
        "image": OG,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDR1,
            "addressLocality": "Tampa",
            "addressRegion": "FL",
            "postalCode": "33612",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
        "hasMap": MAPS,
        "sameAs": [MAPS],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00",
            "closes": "17:00",
        }],
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Tampa Bay"},
            {"@type": "AdministrativeArea", "name": "Hillsborough County"},
        ],
        "knowsAbout": [
            "Consulting",
            "Construction management",
            "Project management",
            "Land development",
            "New construction",
            "Renovation",
            "Demolition",
        ],
        "amenityFeature": [
            {"@type": "LocationFeatureSpecification", "name": "Free parking lot", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "On-site parking", "value": True},
        ],
        "hasOfferCatalog": catalog,
    }
    graph = [
        business,
        {
            "@type": "WebSite",
            "@id": f"{CANON}/#website",
            "url": f"{CANON}/",
            "name": "HMCM",
            "inLanguage": ["en", "es"],
            "publisher": {"@id": f"{CANON}/#business"},
        },
        {
            "@type": "WebPage",
            "@id": f"{page_url}#page",
            "url": page_url,
            "name": page_name,
            "isPartOf": {"@id": f"{CANON}/#website"},
            "about": {"@id": f"{CANON}/#business"},
            "inLanguage": lang,
        },
    ]
    if crumbs:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": name, "item": f"{CANON}{href}" if href else page_url}
                for i, (name, href) in enumerate(crumbs)
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def head(lang, path, pair, title, desc, robots="index,follow"):
    page_url = f"{CANON}{path}"
    pair_url = f"{CANON}{pair}"
    en_url = page_url if lang == "en" else pair_url
    es_url = pair_url if lang == "en" else page_url
    locale = "en_US" if lang == "en" else "es_US"
    alt_locale = "es_US" if lang == "en" else "en_US"
    theme = "#171614"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="{theme}">
  <link rel="canonical" href="{page_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="es" href="{es_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/libre-baskerville-regular.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/barlow-regular.woff2" as="font" type="font/woff2" crossorigin>
  <meta property="og:site_name" content="HMCM">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{page_url}">
  <meta property="og:image" content="{OG}">
  <meta property="og:image:alt" content="HMCM — Construct | Renovate | Demolish">
  <meta property="og:locale" content="{locale}">
  <meta property="og:locale:alternate" content="{alt_locale}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{OG}">
  <link rel="stylesheet" href="/css/styles.css">
  <script type="application/ld+json">
{jsonld(page_url, title, lang)}
  </script>
</head>"""


def _nav(lang, current):
    t = T[lang]
    home = "/" if lang == "en" else "/es/"
    about = "/about/" if lang == "en" else "/es/empresa/"
    services = "/services/" if lang == "en" else "/es/servicios/"
    c_over = "/consulting/" if lang == "en" else "/es/consultoria/"
    c_com = "/consulting/commercial/" if lang == "en" else "/es/consultoria/comercial/"
    c_res = "/consulting/residential/" if lang == "en" else "/es/consultoria/residencial/"
    c_oth = "/consulting/other/" if lang == "en" else "/es/consultoria/otros/"
    cm = "/construction-management/" if lang == "en" else "/es/gerencia-de-construccion/"
    pm = "/project-management/" if lang == "en" else "/es/gerencia-de-proyectos/"
    sp = "/specialties/" if lang == "en" else "/es/especialidades/"
    ind = "/industries/" if lang == "en" else "/es/industrias/"
    ct = "/contact/" if lang == "en" else "/es/contacto/"

    def cur(key, href=None):
        return ' aria-current="page"' if current == key else ""

    def spec_cur(href):
        if "failing-asset" in href or "activos-en-deterioro" in href:
            return cur("consult-failing")
        if "special-projects" in href or "proyectos-especiales" in href:
            return cur("consult-special")
        if "distress" in href or "dificultades" in href:
            return cur("consult-distress")
        return ""
    spec_nav = "\n".join(
        f'            <a href="{href}"{spec_cur(href)}>{esc(name)}</a>' for name, href in t["specialized_items"]
    )
    spec_links = "\n".join(
        f'          <a href="{href}">{esc(name)}</a>' for name, href in t["specs"]
    )
    ind_links = "\n".join(
        f'          <a href="{href}">{esc(name)}</a>' for name, href in t["inds"]
    )
    consult_open = " is-current" if current.startswith("consult") else ""
    services_open = " is-current" if current in ("services", "cm", "pm") else ""
    specs_open = " is-current" if current.startswith("spec") else ""
    inds_open = " is-current" if current.startswith("ind") else ""

    def caret(label):
        return (
            f'<button class="nav-caret" type="button" aria-expanded="false" '
            f'aria-label="{esc(label)}: {esc(t["menu"])}"></button>'
        )

    return f"""      <nav id="site-nav" class="site-nav" aria-label="{t['primary']}">
        <a href="{home}"{cur('home')}>{t['home']}</a>
        <a href="{about}"{cur('about')}>{t['about_us']}</a>
        <div class="nav-item{services_open}">
          <a class="nav-parent" href="{services}"{cur('services')}>{t['services']}</a>
          {caret(t['services'])}
          <div class="nav-drop">
            <a href="{services}"{cur('services')}>{t['overview']}</a>
            <a href="{cm}"{cur('cm')}>{t['cm']}</a>
            <a href="{pm}"{cur('pm')}>{t['pm']}</a>
          </div>
        </div>
        <div class="nav-item{consult_open}">
          <a class="nav-parent" href="{c_over}"{cur('consulting')}>{t['consulting']}</a>
          {caret(t['consulting'])}
          <div class="nav-drop nav-drop--wide">
            <div class="nav-drop-col">
              <p class="nav-drop-label">{t['consulting']}</p>
              <a href="{c_over}"{cur('consulting')}>{t['overview']}</a>
              <a href="{c_com}"{cur('consult-commercial')}>{t['commercial']}</a>
              <a href="{c_res}"{cur('consult-residential')}>{t['residential']}</a>
            </div>
            <div class="nav-drop-col">
              <p class="nav-drop-label">{t['specialized_group']}</p>
{spec_nav}
            </div>
          </div>
        </div>
        <div class="nav-item{specs_open}">
          <a class="nav-parent" href="{sp}"{cur('specialties')}>{t['specialties']}</a>
          {caret(t['specialties'])}
          <div class="nav-drop">
            <a href="{sp}"{cur('specialties')}>{t['overview']}</a>
{spec_links}
          </div>
        </div>
        <div class="nav-item{inds_open}">
          <a class="nav-parent" href="{ind}"{cur('industries')}>{t['industries']}</a>
          {caret(t['industries'])}
          <div class="nav-drop">
            <a href="{ind}"{cur('industries')}>{t['overview']}</a>
{ind_links}
          </div>
        </div>
        <a href="{ct}"{cur('contact')}>{t['contact']}</a>
      </nav>"""


def header_full(lang, current, path, pair):
    t = T[lang]
    home = "/" if lang == "en" else "/es/"
    if lang == "en":
        en_href, es_href = path, pair
        en_cur, es_cur = ' aria-current="true"', ""
    else:
        en_href, es_href = pair, path
        en_cur, es_cur = "", ' aria-current="true"'
    return f"""<body>
  <a class="skip" href="#main">{t['skip']}</a>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="logo-link" href="{home}">
        <img src="/assets/logo-light.svg" width="240" height="90" alt="HMCM logo: Hermanos Mendez Construction Management — Construct, Renovate, Demolish">
      </a>
      <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{t['menu']}">
        <span class="nav-toggle-bars"></span>
        <span class="nav-toggle-bars"></span>
        <span class="nav-toggle-bars"></span>
      </button>
{_nav(lang, current)}
      <div class="lang-switch" role="group" aria-label="{t['lang']}">
        <a href="{en_href}" hreflang="en" lang="en"{en_cur}>EN</a>
        <span class="sep" aria-hidden="true">|</span>
        <a href="{es_href}" hreflang="es" lang="es"{es_cur}>ES</a>
      </div>
      <a class="btn-call" href="tel:{PHONE_TEL}">{t['call']}</a>
    </div>
  </header>"""


def footer(lang):
    t = T[lang]
    home = "/" if lang == "en" else "/es/"
    about = "/about/" if lang == "en" else "/es/empresa/"
    contact = "/contact/" if lang == "en" else "/es/contacto/"
    c_over = "/consulting/" if lang == "en" else "/es/consultoria/"
    c_com = "/consulting/commercial/" if lang == "en" else "/es/consultoria/comercial/"
    c_res = "/consulting/residential/" if lang == "en" else "/es/consultoria/residencial/"
    c_oth = "/consulting/other/" if lang == "en" else "/es/consultoria/otros/"
    cm = "/construction-management/" if lang == "en" else "/es/gerencia-de-construccion/"
    pm = "/project-management/" if lang == "en" else "/es/gerencia-de-proyectos/"
    sp = "/specialties/" if lang == "en" else "/es/especialidades/"
    ind = "/industries/" if lang == "en" else "/es/industrias/"
    other = "\n".join(f"            <li><a href=\"{h}\">{esc(n)}</a></li>" for n, h in t["other_items"])
    specs = "\n".join(f"            <li><a href=\"{h}\">{esc(n)}</a></li>" for n, h in t["specs"])
    inds = "\n".join(f"            <li><a href=\"{h}\">{esc(n)}</a></li>" for n, h in t["inds"])
    return f"""  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <a class="footer-logo" href="{home}">
          <img src="/assets/logo-light.svg" width="200" height="75" alt="HMCM — Hermanos Mendez Construction Management">
        </a>
        <p class="footer-meta">{ADDR1}<br>{CITY}<br>
          <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></p>
        <p class="footer-meta"><a href="{MAPS}" rel="noopener noreferrer" target="_blank">{t['maps']}</a></p>
      </div>
      <div class="footer-nav">
        <h2>{t['consulting']}</h2>
        <ul>
          <li><a href="{c_over}">{t['overview']}</a></li>
          <li><a href="{c_com}">{t['commercial']}</a></li>
          <li><a href="{c_res}">{t['residential']}</a></li>
          <li><a href="{c_oth}">{t['other_group']}</a></li>
{other}
        </ul>
      </div>
      <div class="footer-nav">
        <h2>{t['cm']} / {t['pm']}</h2>
        <ul>
          <li><a href="{cm}">{t['cm']}</a></li>
          <li><a href="{pm}">{t['pm']}</a></li>
        </ul>
        <h2 style="margin-top:1.25rem">{t['specialties']}</h2>
        <ul>
          <li><a href="{sp}">{t['overview']}</a></li>
{specs}
        </ul>
      </div>
      <div class="footer-nav">
        <h2>{t['industries']}</h2>
        <ul>
          <li><a href="{ind}">{t['overview']}</a></li>
{inds}
        </ul>
      </div>
      <div class="footer-nav">
        <h2>{t['company']}</h2>
        <ul>
          <li><a href="{home}">{t['home']}</a></li>
          <li><a href="{about}">{t['about']}</a></li>
          <li><a href="{contact}">{t['contact']}</a></li>
          <li><a href="{'/es/' if lang=='en' else '/'}">{t['es_label']}</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <span>{t['copy']}</span>
      <span><a href="{contact}">{t['contact']}</a> · <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></span>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>"""


def crumbs_html(lang, crumbs):
    t = T[lang]
    parts = []
    for i, (name, href) in enumerate(crumbs):
        last = i == len(crumbs) - 1
        if last or not href:
            parts.append(f'      <li><span aria-current="page">{esc(name)}</span></li>')
        else:
            parts.append(f'      <li><a href="{href}">{esc(name)}</a></li>')
    return f"""    <nav class="breadcrumbs" aria-label="{t['breadcrumb']}">
      <ol>
{chr(10).join(parts)}
      </ol>
    </nav>"""


def page_banner(lang, crumbs, h1, lead, photo):
    return f"""    <section class="page-banner">
      <div class="page-banner__bg" style="background-image:url('/assets/photos/{photo}')" role="presentation"></div>
      <div class="wrap">
{crumbs_html(lang, crumbs)}
        <h1>{esc(h1)}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>"""


def wrap_page(lang, path, pair, current, title, desc, body, robots="index,follow"):
    return (
        head(lang, path, pair, title, desc, robots)
        + "\n"
        + header_full(lang, current, path, pair)
        + "\n  <main id=\"main\">\n"
        + body
        + "\n  </main>\n"
        + footer(lang)
    )
