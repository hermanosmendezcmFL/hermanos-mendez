from html import escape as esc
from chrome import T, BRAND, ADDR1, CITY, PHONE_DISP, PHONE_TEL, LEGAL, MAPS

def _home(lang):
    t = T[lang]
    if lang == "en":
        h1 = "Advising and managing land development and construction in Tampa Bay."
        lead = (
            "%s provides <a href='/consulting/'>consulting</a> "
            "(<a href='/consulting/commercial/'>commercial</a> and "
            "<a href='/consulting/residential/'>residential</a>), "
            "<a href='/construction-management/'>construction management</a>, and "
            "<a href='/project-management/'>project management</a> for owners and partners across Tampa Bay."
        ) % BRAND
        cta2 = "See consulting, CM, and PM"
        three = "Consulting, construction management, and project management."
        tiles = [
            ("01", "Consulting", "Commercial and residential advisory \u2014 scoping, planning, takeoff support, purchasing, and the other consulting work owners ask for before and during a job.", "/consulting/", "consulting.jpg"),
            ("02", "Construction Management", "Field coordination of trades, schedule, and site so the work moves with a single point of contact.", "/construction-management/", "construction-mgmt.jpg"),
            ("03", "Project Management", "Oversight of scope, cost, and timeline from preconstruction through closeout.", "/project-management/", "project-mgmt.jpg"),
        ]
        cons_h = "Consulting, by market"
        cons_intro = "The consulting practice is organized first by commercial and residential work, then by additional consulting services."
        com_t, com_h, com_p = "Commercial", "/consulting/commercial/", "Advisory for commercial sites, shells, tenant work, and owner-side decisions on schedule, scope, and delivery."
        res_t, res_h, res_p = "Residential", "/consulting/residential/", "Advisory for houses, custom builds, and residential renovations \u2014 planned at dwelling scale, not a commercial playbook."
        other_h = "Other consulting services"
        other_intro = "These sit inside consulting. They are not a fourth primary next to construction management or project management."
        oth_href = "/consulting/other/"
        spec_href = "/specialties/"
        ind_href = "/industries/"
        contact_href = "/contact/"
        consult_anchor = "/consulting/"
        spec_h = "Specializing in"
        spec_intro = "Land development, new construction, renovation, and demolition \u2014 the work types the practice is built around."
        ind_h = "Industries"
        ind_intro = "Markets we advise and manage in Tampa Bay. Each item is a real page."
        why_k, why_h = "How we work", "Why owners hire a CM/PM consultant."
        why = [
            ("01", "One accountable contact", "Decisions, schedule, and field questions route through consulting, construction management, or project management \u2014 not a split chain of command."),
            ("02", "Preconstruction before the field", "Scope, takeoff support, purchasing assistance, and permitting coordination happen while the job can still change."),
            ("03", "The job, not the press release", "We manage process: trades, inspections, stormwater, demolition, renovation, and new work. We do not sell awards or a project gallery."),
            ("04", "Delivery through closeout", "Project management carries cost and timeline; construction management carries the site. Both stay tied to the owner until turnover."),
        ]
        area_h = "Tampa Bay service area"
        area_p = "The office is at %s, %s, in Hillsborough County. We advise and manage land development and construction in Tampa Bay. %s %s." % (ADDR1, CITY, t["hours"], t["parking"])
        contact_h = "Call or visit"
        other_blurb = [
            "Sequence, labor, and waste \u2014 then putting changes in place.",
            "How field, office, and building systems talk, and how to tighten that.",
            "Pursuit, qualifications, and teaming support for construction work.",
            "Scopes that do not fit a standard CM or PM engagement.",
            "Quantity takeoff support and help reviewing contract terms before you sign.",
            "Buyout support, proposals, and purchase tracking.",
            "Documenting how the work is done and how people are assigned to it.",
        ]
        ind_blurb = [
            "Owner-side consulting and management for commercial buildings and sites.",
            "Multifamily planning, construction management, and coordination.",
            "Single-family residential \u2014 new houses, additions, and related site work.",
            "Custom residential work that needs closer scope and finish control.",
            "Clearing and site preparation as part of land development.",
            "Drainage and stormwater work coordinated with the rest of the site.",
            "Permit sequencing and follow-through with the agencies that have to sign off.",
            "Inspection readiness and closeout, scheduled with the rest of the job.",
            "Owner representation when design and construction move as one delivery.",
        ]
        spec_photos = ["land.jpg", "new-construction.jpg", "interior.jpg", "demolition.jpg"]
    else:
        h1 = "Asesoramos y gerenciamos el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay."
        lead = (
            "%s ofrece <a href='/es/consultoria/'>consultor\u00eda</a> "
            "(<a href='/es/consultoria/comercial/'>comercial</a> y "
            "<a href='/es/consultoria/residencial/'>residencial</a>), "
            "<a href='/es/gerencia-de-construccion/'>gerencia de construcci\u00f3n</a> y "
            "<a href='/es/gerencia-de-proyectos/'>gerencia de proyectos</a> para propietarios y socios en Tampa Bay."
        ) % BRAND
        cta2 = "Ver consultor\u00eda, CM y PM"
        three = "Consultor\u00eda, gerencia de construcci\u00f3n y gerencia de proyectos."
        tiles = [
            ("01", "Consultor\u00eda", "Asesor\u00eda comercial y residencial: alcance, planificaci\u00f3n, takeoff, compras y los dem\u00e1s servicios de consultor\u00eda que se piden antes y durante la obra.", "/es/consultoria/", "consulting.jpg"),
            ("02", "Gerencia de construcci\u00f3n", "Coordinaci\u00f3n de gremios, programa y sitio de obra, con un solo punto de contacto.", "/es/gerencia-de-construccion/", "construction-mgmt.jpg"),
            ("03", "Gerencia de proyectos", "Control de alcance, costo y plazo desde la preconstrucci\u00f3n hasta el cierre.", "/es/gerencia-de-proyectos/", "project-mgmt.jpg"),
        ]
        cons_h = "Consultor\u00eda, por mercado"
        cons_intro = "La pr\u00e1ctica de consultor\u00eda se organiza primero en comercial y residencial, y despu\u00e9s en servicios adicionales de consultor\u00eda."
        com_t, com_h, com_p = "Comercial", "/es/consultoria/comercial/", "Asesor\u00eda para predios comerciales, naves, locales y decisiones del propietario sobre programa, alcance y entrega."
        res_t, res_h, res_p = "Residencial", "/es/consultoria/residencial/", "Asesor\u00eda para viviendas, obras a medida y renovaciones residenciales, a escala de casa, no de campus comercial."
        other_h = "Otros servicios de consultor\u00eda"
        other_intro = "Forman parte de la consultor\u00eda. No son un cuarto servicio primario al lado de la gerencia de construcci\u00f3n o de proyectos."
        oth_href = "/es/consultoria/otros/"
        spec_href = "/es/especialidades/"
        ind_href = "/es/industrias/"
        contact_href = "/es/contacto/"
        consult_anchor = "/es/consultoria/"
        spec_h = "Especializaci\u00f3n"
        spec_intro = "Desarrollo de terrenos, nueva construcci\u00f3n, renovaci\u00f3n y demolici\u00f3n: los tipos de obra en los que se centra la pr\u00e1ctica."
        ind_h = "Industrias"
        ind_intro = "Mercados que asesoramos y gerenciamos en Tampa Bay. Cada rubro tiene su p\u00e1gina."
        why_k, why_h = "M\u00e9todo", "Por qu\u00e9 un propietario contrata un consultor de CM/PM."
        why = [
            ("01", "Un solo responsable", "Decisiones, programa y campo pasan por consultor\u00eda, gerencia de construcci\u00f3n o gerencia de proyectos \u2014 no por una cadena partida."),
            ("02", "Preconstrucci\u00f3n antes del campo", "Alcance, takeoff, compras y permisos se resuelven mientras la obra todav\u00eda puede cambiar."),
            ("03", "La obra, no el comunicado", "Gerenciamos proceso: gremios, inspecciones, aguas pluviales, demolici\u00f3n, renovaci\u00f3n y obra nueva. No vendemos premios ni un portafolio."),
            ("04", "Hasta el cierre", "La gerencia de proyectos sostiene costo y plazo; la de construcci\u00f3n sostiene el sitio. Ambas siguen al propietario hasta la entrega."),
        ]
        area_h = "\u00c1rea de servicio en Tampa Bay"
        area_p = "La oficina est\u00e1 en %s, %s, en el condado de Hillsborough. Asesoramos y gerenciamos desarrollo de terrenos y construcci\u00f3n en Tampa Bay. %s %s." % (ADDR1, CITY, t["hours"], t["parking"])
        contact_h = "Llame o visite"
        other_blurb = [
            "C\u00f3mo se planea y se ejecuta la obra, e implementar cambios.",
            "C\u00f3mo se comunican campo, oficina y sistemas del edificio.",
            "Persecuci\u00f3n de obra, cualificaciones y alianzas.",
            "Alcances que no caben en un encargo t\u00edpico de CM o PM.",
            "Cubicaci\u00f3n (takeoff) y revisi\u00f3n de t\u00e9rminos contractuales antes de firmar.",
            "Buyout, propuestas y seguimiento de compras.",
            "Documentar c\u00f3mo se hace el trabajo y c\u00f3mo se asigna a las personas.",
        ]
        ind_blurb = [
            "Consultor\u00eda y gerencia del lado del propietario para edificios y predios comerciales.",
            "Planificaci\u00f3n, gerencia de construcci\u00f3n y coordinaci\u00f3n en multifamiliar.",
            "Residencial unifamiliar: casas nuevas, ampliaciones y obra de sitio.",
            "Obra residencial a medida, con control m\u00e1s estrecho de alcance y acabados.",
            "Despeje y preparaci\u00f3n del predio como parte del desarrollo.",
            "Drenaje y aguas pluviales coordinados con el resto del sitio.",
            "Secuencia de permisos y seguimiento con las agencias que deben firmar.",
            "Preparaci\u00f3n para inspecciones y cierre, programados con el resto de la obra.",
            "Representaci\u00f3n del propietario cuando dise\u00f1o y construcci\u00f3n se entregan juntos.",
        ]
        spec_photos = ["land.jpg", "new-construction.jpg", "interior.jpg", "demolition.jpg"]

    tile_html = []
    for idx, name, copy, href, ph in tiles:
        tile_html.append(
            '        <a class="tile" href="%s">\n'
            '          <div class="tile__media" style="background-image:url(\'/assets/photos/%s\')" role="presentation"></div>\n'
            '          <div class="tile__body">\n'
            '            <span class="tile__index">%s</span>\n'
            "            <h3>%s</h3>\n            <p>%s</p>\n"
            '            <span class="tile-go">%s</span>\n'
            "          </div>\n        </a>" % (href, ph, idx, esc(name), copy, t["see"])
        )
    others = []
    for (name, href), blurb in zip(t["other_items"], other_blurb):
        others.append(
            '        <a class="mini-card" href="%s">\n'
            "          <h3>%s</h3>\n          <p>%s</p>\n        </a>" % (href, esc(name), blurb)
        )
    specs = []
    for (name, href), ph in zip(t["specs"], spec_photos):
        specs.append(
            '        <a class="spec-card" href="%s">\n'
            '          <div class="spec-card__media" style="background-image:url(\'/assets/photos/%s\')" role="presentation"></div>\n'
            "          <h3>%s</h3>\n        </a>" % (href, ph, esc(name))
        )
    inds = []
    for (name, href), blurb in zip(t["inds"], ind_blurb):
        inds.append(
            '        <a class="ind-card" href="%s">\n'
            "          <h3>%s</h3>\n          <p>%s</p>\n"
            '          <span class="go">%s</span>\n        </a>' % (href, esc(name), blurb, t["see"])
        )
    why_html = []
    for num, title, copy in why:
        why_html.append(
            '        <article class="process">\n'
            '          <span class="num">%s</span>\n'
            "          <h3>%s</h3>\n          <p>%s</p>\n        </article>" % (num, esc(title), copy)
        )
    return (
        '\n    <section class="hero-full">\n'
        '      <div class="hero-full__bg" style="background-image:url(\'/assets/photos/hero.jpg\')" role="presentation"></div>\n'
        '      <div class="wrap">\n'
        '        <p class="eyebrow">Tampa, Florida</p>\n'
        '        <p class="hero-tag">Construct | Renovate | Demolish</p>\n'
        "        <h1>%s</h1>\n"
        '        <p class="hero-lead">%s</p>\n'
        '        <div class="hero-actions">\n'
        '          <a class="btn btn-primary" href="tel:%s">%s</a>\n'
        '          <a class="btn btn-ghost" href="#services">%s</a>\n'
        "        </div>\n"
        '        <p class="hero-note">%s</p>\n'
        "      </div>\n    </section>\n"
        '    <section class="section section--ink" id="services">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">01 \u00b7 %s \u00b7 %s \u00b7 %s</p>\n'
        "            <h2>%s</h2>\n          </div>\n        </div>\n"
        '        <div class="tile-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
        '    <section class="section section--stone" id="consulting-markets">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">02 \u00b7 %s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s %s</a>\n        </div>\n'
        '        <div class="split-cards">\n'
        '          <a class="split-card" href="%s">\n'
        '            <div class="split-card__media" style="background-image:url(\'/assets/photos/commercial.jpg\')" role="presentation"></div>\n'
        '            <div class="split-card__body">\n              <h3>%s</h3>\n              <p>%s</p>\n            </div>\n          </a>\n'
        '          <a class="split-card" href="%s">\n'
        '            <div class="split-card__media" style="background-image:url(\'/assets/photos/custom.jpg\')" role="presentation"></div>\n'
        '            <div class="split-card__body">\n              <h3>%s</h3>\n              <p>%s</p>\n            </div>\n          </a>\n'
        "        </div>\n      </div>\n    </section>\n"
        '    <section class="section" id="other-consulting">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">%s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s</a>\n        </div>\n'
        '        <div class="mini-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
        '    <section class="section section--ink" id="specialties">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">03 \u00b7 %s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s %s</a>\n        </div>\n'
        '        <div class="spec-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
        '    <section class="section section--stone" id="industries">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">04 \u00b7 %s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s %s</a>\n        </div>\n'
        '        <div class="ind-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
        '    <section class="section section--dark">\n      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n        <h2>%s</h2>\n'
        '        <div class="process-grid" style="margin-top:1.75rem">\n%s\n        </div>\n'
        "      </div>\n    </section>\n"
        '    <section class="section">\n      <div class="wrap area-grid">\n        <div>\n'
        '          <p class="section-kicker">Tampa Bay</p>\n          <h2>%s</h2>\n'
        '          <div class="prose"><p>%s</p></div>\n        </div>\n'
        '        <div class="area-photo" style="background-image:url(\'/assets/photos/tampa.jpg\')" role="img" aria-label="Tampa Bay"></div>\n'
        "      </div>\n    </section>\n"
        '    <section class="section section--ink" id="contact-strip">\n'
        '      <div class="wrap contact-strip">\n        <div>\n'
        '          <p class="section-kicker">%s</p>\n          <h2>%s</h2>\n'
        '          <a class="phone-xl" href="tel:%s">%s</a>\n'
        '          <address class="addr">%s<br>%s<br>%s<br>\n'
        '            <a class="map-link" href="%s" rel="noopener noreferrer" target="_blank">%s</a>\n'
        "          </address>\n"
        '          <p class="hero-note" style="margin-top:1rem">%s</p>\n'
        "        </div>\n        <div>\n          <p>%s</p>\n"
        '          <p><a class="btn btn-primary" href="%s">%s</a></p>\n'
        "        </div>\n      </div>\n    </section>\n"
    ) % (
        esc(h1), lead, PHONE_TEL, PHONE_DISP, cta2, t["hours"],
        t["consulting"], t["cm"], t["pm"], esc(three), "\n".join(tile_html),
        t["consulting"], esc(cons_h), cons_intro, consult_anchor, t["see"], t["consulting"],
        com_h, esc(com_t), com_p, res_h, esc(res_t), res_p,
        t["consulting"], esc(other_h), other_intro, oth_href, t["see"], "\n".join(others),
        t["specialties"], esc(spec_h), spec_intro, spec_href, t["see"], t["specialties"], "\n".join(specs),
        t["industries"], esc(ind_h), ind_intro, ind_href, t["see"], t["industries"], "\n".join(inds),
        why_k, esc(why_h), "\n".join(why_html),
        esc(area_h), area_p,
        t["contact"], esc(contact_h), PHONE_TEL, PHONE_DISP, BRAND, ADDR1, CITY, MAPS, t["maps"], t["hours"],
        LEGAL, contact_href, t["contact"],
    )

def build_homes(write, wrap_page):
    write("/", wrap_page(
        "en", "/", "/es/", "home",
        "HMCM | Consulting, Construction Management, and Project Management in Tampa Bay",
        "Hermanos Mendez Construction Management advises and manages land development and construction in Tampa Bay: consulting (commercial and residential), construction management, and project management.",
        _home("en"),
    ))
    write("/es/", wrap_page(
        "es", "/es/", "/", "home",
        "HMCM | Consultor\u00eda, gerencia de construcci\u00f3n y gerencia de proyectos en Tampa Bay",
        "Hermanos Mendez Construction Management asesora y gerencia el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay: consultor\u00eda (comercial y residencial), gerencia de construcci\u00f3n y gerencia de proyectos.",
        _home("es"),
    ))
