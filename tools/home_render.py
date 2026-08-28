from html import escape as esc
from chrome import T, BRAND, ADDR1, CITY, PHONE_DISP, PHONE_TEL, MAPS


def proof_html(lang):
    if lang == "en":
        a_fig, a_h = "26", "26 Years in the Business"
        b_fig, b_h = "$300 million", "Over $300 Million in Completed Projects"
        label = "Proof"
    else:
        a_fig, a_h = "26", "26 años en el negocio"
        b_fig, b_h = "$300 millones", "Más de $300 millones en proyectos completados"
        label = "Trayectoria"
    return (
        '    <section class="proof" id="proof" aria-label="%s">\n'
        '      <div class="wrap proof-grid">\n'
        "        <article>\n"
        '          <p class="proof-figure">%s</p>\n'
        "          <h2>%s</h2>\n"
        "        </article>\n"
        "        <article>\n"
        '          <p class="proof-figure">%s</p>\n'
        "          <h2>%s</h2>\n"
        "        </article>\n"
        "      </div>\n"
        "    </section>\n"
    ) % (esc(label), esc(a_fig), esc(a_h), esc(b_fig), esc(b_h))


def story_copy(lang):
    if lang == "en":
        return {
            "team_k": "Team",
            "team_h": "Our Team",
            "team": [
                "Owners hire a practice, not a rotating cast. Hermanos Mendez Construction Management is the Tampa office that will advise the job and stay on it.",
                "The people who pick up the phone are the people who will walk the site. Call the office and you talk to HMCM.",
            ],
            "exp_k": "Expertise",
            "exp_h": "Our Expertise",
            "exp": [
                "The practice is built around consulting for commercial and residential work, construction management, and project management.",
                "We plan and run land development, new construction, renovation, and demolition.",
            ],
            "bud_k": "Method",
            "bud_h": "Budget with Purpose and Execute with Discipline",
            "bud": [
                "A budget with purpose is written before anyone mobilizes. Quantities, allowances, and buyout are set so cost has a reason, not a hope.",
                "Execute with discipline means the field follows that budget: sequence, hold points, and a single contact who keeps cost and the site in the same conversation.",
            ],
            "diff_k": "Difference",
            "diff_h": "The Difference We Bring to the Table",
            "ext_h": "A True Extension of Your Business",
            "part_h": "Expert Partners When You Need Them",
            "diff": [
                "We sit on the owner\u2019s side of the table. Decisions, schedule, and the field route through one accountable contact.",
                "HMCM works as a true extension of your business: expert partners when you need them, without a split chain of command.",
            ],
        }
    return {
        "team_k": "Equipo",
        "team_h": "Nuestro equipo",
        "team": [
            "Los propietarios contratan una pr\u00e1ctica, no un elenco rotativo. Hermanos Mendez Construction Management es la oficina en Tampa que asesora la obra y se queda en ella.",
            "Quienes contestan el tel\u00e9fono son quienes recorren el sitio. Llame a la oficina y habla con HMCM.",
        ],
        "exp_k": "Experiencia",
        "exp_h": "Nuestra experiencia",
        "exp": [
            "La pr\u00e1ctica se centra en la consultor\u00eda comercial y residencial, la gerencia de construcci\u00f3n y la gerencia de proyectos.",
            "Planeamos y dirigimos desarrollo de terrenos, nueva construcci\u00f3n, renovaci\u00f3n y demolici\u00f3n.",
        ],
        "bud_k": "M\u00e9todo",
        "bud_h": "Presupuestar con prop\u00f3sito y ejecutar con disciplina",
        "bud": [
            "Un presupuesto con prop\u00f3sito se escribe antes de movilizar a nadie. Las cantidades, las partidas y el buyout se fijan para que el costo tenga una raz\u00f3n, no una esperanza.",
            "Ejecutar con disciplina significa que el campo sigue ese presupuesto: secuencia, puntos de control y un solo contacto que mantiene el costo y el sitio en la misma conversaci\u00f3n.",
        ],
        "diff_k": "Diferencia",
        "diff_h": "La diferencia que aportamos",
        "ext_h": "Una verdadera extensi\u00f3n de su negocio",
        "part_h": "Socios expertos cuando los necesita",
        "diff": [
            "Nos sentamos del lado del propietario. Las decisiones, el programa y el campo pasan por un solo responsable.",
            "HMCM trabaja como una verdadera extensi\u00f3n de su negocio: socios expertos cuando los necesita, sin una cadena de mando partida.",
        ],
    }


def _paras(ps):
    return "\n".join("            <p>%s</p>" % p for p in ps)


def story_sections(lang, extra_expertise=""):
    c = story_copy(lang)
    extra = ""
    if extra_expertise:
        extra = '\n        <div class="tile-grid" style="margin-top:2rem">\n%s\n        </div>' % extra_expertise
    return (
        '    <section class="section" id="team">\n'
        '      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n'
        '        <h2 class="story-head">%s</h2>\n'
        '        <div class="prose story-copy">\n%s\n        </div>\n'
        "      </div>\n"
        "    </section>\n"
        '    <section class="section section--ink" id="expertise">\n'
        '      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n'
        '        <h2 class="story-head">%s</h2>\n'
        '        <div class="prose story-copy">\n%s\n        </div>%s\n'
        "      </div>\n"
        "    </section>\n"
        '    <section class="section section--stone" id="method">\n'
        '      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n'
        '        <h2 class="story-head">%s</h2>\n'
        '        <div class="prose story-copy">\n%s\n        </div>\n'
        "      </div>\n"
        "    </section>\n"
        '    <section class="section section--dark" id="difference">\n'
        '      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n'
        '        <h2 class="story-head">%s</h2>\n'
        '        <p class="position-line">%s</p>\n'
        '        <p class="position-line">%s</p>\n'
        '        <div class="prose story-copy">\n%s\n        </div>\n'
        "      </div>\n"
        "    </section>\n"
    ) % (
        esc(c["team_k"]), esc(c["team_h"]), _paras(c["team"]),
        esc(c["exp_k"]), esc(c["exp_h"]), _paras(c["exp"]), extra,
        esc(c["bud_k"]), esc(c["bud_h"]), _paras(c["bud"]),
        esc(c["diff_k"]), esc(c["diff_h"]), esc(c["ext_h"]), esc(c["part_h"]), _paras(c["diff"]),
    )


def about_body(lang):
    t = T[lang]
    contact = "/contact/" if lang == "en" else "/es/contacto/"
    c_over = "/consulting/" if lang == "en" else "/es/consultoria/"
    cm = "/construction-management/" if lang == "en" else "/es/gerencia-de-construccion/"
    pm = "/project-management/" if lang == "en" else "/es/gerencia-de-proyectos/"
    if lang == "en":
        crumbs = [("Home", "/"), ("About", None)]
        h1 = "About HMCM"
        lead = "Hermanos Mendez Construction Management advises and manages land development and construction in Tampa Bay."
        photo = "tampa.jpg"
        kicker = "Office"
        office_h = "Tampa Bay"
        office_p = (
            "The office is at %s, %s. Phone <a href=\"tel:%s\">%s</a>. %s Free on-site parking."
            % (ADDR1, CITY, PHONE_TEL, PHONE_DISP, t["hours"])
        )
        related = [
            ("Contact", "/contact/", "Address, hours, and map."),
            ("Consulting", "/consulting/", "Commercial and residential advisory."),
            ("Construction Management", "/construction-management/", "Field coordination of the job."),
        ]
        pos = "Expertise on Demand"
        knowledge = "The Knowledge, Skills, and Abilities to Impact Change"
    else:
        crumbs = [("Inicio", "/es/"), ("Empresa", None)]
        h1 = "Sobre HMCM"
        lead = "Hermanos Mendez Construction Management asesora y gerencia el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay."
        photo = "tampa.jpg"
        kicker = "Oficina"
        office_h = "Tampa Bay"
        office_p = (
            "La oficina est\u00e1 en %s, %s. Tel\u00e9fono <a href=\"tel:%s\">%s</a>. %s Estacionamiento gratuito en el sitio."
            % (ADDR1, CITY, PHONE_TEL, PHONE_DISP, t["hours"])
        )
        related = [
            ("Contacto", "/es/contacto/", "Direcci\u00f3n, horario y mapa."),
            ("Consultor\u00eda", "/es/consultoria/", "Asesor\u00eda comercial y residencial."),
            ("Gerencia de construcci\u00f3n", "/es/gerencia-de-construccion/", "Coordinaci\u00f3n de campo."),
        ]
        pos = "Expertise on Demand"
        knowledge = "El conocimiento, las habilidades y las aptitudes para impulsar el cambio"

    from chrome import page_banner
    body = page_banner(lang, crumbs, h1, lead, photo)
    body += (
        '\n    <section class="section section--ink" id="position">\n'
        '      <div class="wrap">\n'
        '        <p class="hero-position" style="margin-top:0">%s</p>\n'
        '        <p class="position-line">%s</p>\n'
        "      </div>\n"
        "    </section>\n"
    ) % (esc(pos), esc(knowledge))
    body += proof_html(lang)
    body += story_sections(lang)
    cards = "\n".join(
        '          <a href="%s"><h3>%s</h3><p>%s</p></a>' % (h, esc(n), d) for n, h, d in related
    )
    body += (
        '\n    <section class="section">\n'
        '      <div class="wrap area-grid">\n'
        "        <div>\n"
        '          <p class="section-kicker">%s</p>\n'
        "          <h2>%s</h2>\n"
        '          <div class="prose"><p>%s</p></div>\n'
        "        </div>\n"
        '        <div class="area-photo" style="background-image:url(\'/assets/photos/tampa.jpg\')" role="img" aria-label="Tampa Bay"></div>\n'
        "      </div>\n"
        "    </section>\n"
        '    <section class="section section--stone">\n'
        '      <div class="wrap">\n'
        '        <p class="section-kicker">%s</p>\n'
        "        <h2>%s</h2>\n"
        '        <div class="related">\n%s\n        </div>\n'
        "      </div>\n"
        "    </section>\n"
        '    <section class="section section--ink">\n'
        '      <div class="wrap cta-band">\n'
        "        <h2>%s</h2>\n"
        '        <div class="hero-actions">\n'
        '          <a class="btn btn-primary" href="tel:%s">%s</a>\n'
        '          <a class="btn btn-ghost" href="%s">%s</a>\n'
        "        </div>\n"
        "      </div>\n"
        "    </section>"
    ) % (
        esc(kicker), esc(office_h), office_p,
        t["on_this"], t["related"], cards,
        PHONE_DISP, PHONE_TEL, t["call_now"], contact, t["contact_cta"],
    )
    return body


def _home(lang):
    t = T[lang]
    if lang == "en":
        h1 = "Advising and managing land development and construction in Tampa Bay."
        position = "Expertise on Demand"
        knowledge = "The Knowledge, Skills, and Abilities to Impact Change"
        lead = (
            "Hermanos Mendez Construction Management advises owners on land development "
            "and construction in Tampa Bay. HMCM plans the money and runs the job."
        )
        cta2 = "What We Do"
        three = "Consulting, construction management, and project management."
        tiles = [
            ("01", "Consulting", "Advisory for commercial and residential work: scoping, planning, and the consulting owners ask for before and during a job.", "/consulting/", "consulting.jpg"),
            ("02", "Construction Management", "Field coordination of trades, schedule, and site so the work moves with a single point of contact.", "/construction-management/", "construction-mgmt.jpg"),
            ("03", "Project Management", "Oversight of scope, cost, and timeline from preconstruction through closeout.", "/project-management/", "project-mgmt.jpg"),
        ]
        cons_k = "Consulting"
        spec_k = "Specialties"
        ind_k = "Markets"
        cons_h = "Consulting by Market"
        cons_intro = "Commercial and residential work, planned before anyone mobilizes."
        com_t, com_h, com_p = "Commercial", "/consulting/commercial/", "Advisory for commercial sites, shells, tenant work, and owner-side decisions on schedule, scope, and delivery."
        res_t, res_h, res_p = "Residential", "/consulting/residential/", "Advisory for houses, custom builds, and residential renovations, planned at dwelling scale, not a commercial playbook."
        other_h = "Other Consulting Services"
        other_intro = "Evaluations, takeoff, purchasing, and other defined consulting tasks."
        oth_href = "/consulting/other/"
        spec_href = "/specialties/"
        ind_href = "/industries/"
        contact_href = "/contact/"
        consult_anchor = "/consulting/"
        spec_h = "Specialties"
        spec_intro = "The work types we plan and manage."
        ind_h = "Industries"
        ind_intro = "Markets we advise and manage in Tampa Bay."
        area_h = "Tampa Bay Service Area"
        area_p = "The office is at %s, %s, in Hillsborough County. We advise and manage land development and construction across Tampa Bay." % (ADDR1, CITY)
        contact_h = "Call or Visit"
        other_blurb = [
            "Sequence, labor, and waste, then putting changes in place.",
            "How field, office, and building systems talk, and how to tighten that.",
            "Pursuit, qualifications, and teaming support for construction work.",
            "Scopes that do not fit a standard construction-management or project-management engagement.",
            "Quantity takeoff support and help reviewing contract terms before you sign.",
            "Buyout support, proposals, and purchase tracking.",
            "Documenting how the work is done and how people are assigned to it.",
        ]
        ind_blurb = [
            "Owner-side consulting and management for commercial buildings and sites.",
            "Multi-family planning, construction management, and coordination.",
            "Single-family residential: new houses, additions, and related site work.",
            "Custom residential work that needs closer scope and finish control.",
            "Clearing and site preparation as part of land development.",
            "Drainage and stormwater work coordinated with the rest of the site.",
            "Permit sequencing and follow-through with the agencies that have to sign off.",
            "Inspection readiness and closeout, scheduled with the rest of the job.",
            "Owner representation when design-build moves as one delivery.",
        ]
        spec_photos = ["land.jpg", "new-construction.jpg", "interior.jpg", "demolition.jpg"]
    else:
        h1 = "Asesoramos y gerenciamos el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay."
        position = "Expertise on Demand"
        knowledge = "El conocimiento, las habilidades y las aptitudes para impulsar el cambio"
        lead = (
            "Hermanos Mendez Construction Management asesora a propietarios en desarrollo de terrenos "
            "y construcci\u00f3n en Tampa Bay. HMCM planea el dinero y dirige la obra."
        )
        cta2 = "Qu\u00e9 hacemos"
        three = "Consultor\u00eda, gerencia de construcci\u00f3n y gerencia de proyectos."
        tiles = [
            ("01", "Consultor\u00eda", "Asesor\u00eda comercial y residencial: alcance, planificaci\u00f3n y la consultor\u00eda que se pide antes y durante la obra.", "/es/consultoria/", "consulting.jpg"),
            ("02", "Gerencia de construcci\u00f3n", "Coordinaci\u00f3n de gremios, programa y sitio de obra, con un solo punto de contacto.", "/es/gerencia-de-construccion/", "construction-mgmt.jpg"),
            ("03", "Gerencia de proyectos", "Control de alcance, costo y plazo desde la preconstrucci\u00f3n hasta el cierre.", "/es/gerencia-de-proyectos/", "project-mgmt.jpg"),
        ]
        cons_k = "Consultor\u00eda"
        spec_k = "Especialidades"
        ind_k = "Mercados"
        cons_h = "Consultor\u00eda por mercado"
        cons_intro = "Obra comercial y residencial, planeada antes de movilizar a nadie."
        com_t, com_h, com_p = "Comercial", "/es/consultoria/comercial/", "Asesor\u00eda para predios comerciales, naves, locales y decisiones del propietario sobre programa, alcance y entrega."
        res_t, res_h, res_p = "Residencial", "/es/consultoria/residencial/", "Asesor\u00eda para viviendas, obras a medida y renovaciones residenciales, a escala de casa, no de campus comercial."
        other_h = "Otros servicios de consultor\u00eda"
        other_intro = "Evaluaciones, takeoff, compras y otras tareas concretas de consultor\u00eda."
        oth_href = "/es/consultoria/otros/"
        spec_href = "/es/especialidades/"
        ind_href = "/es/industrias/"
        contact_href = "/es/contacto/"
        consult_anchor = "/es/consultoria/"
        spec_h = "Especialidades"
        spec_intro = "Los tipos de obra que planeamos y gerenciamos."
        ind_h = "Industrias"
        ind_intro = "Mercados que asesoramos y gerenciamos en Tampa Bay."
        area_h = "\u00c1rea de servicio en Tampa Bay"
        area_p = "La oficina est\u00e1 en %s, %s, en el condado de Hillsborough. Asesoramos y gerenciamos desarrollo de terrenos y construcci\u00f3n en Tampa Bay." % (ADDR1, CITY)
        contact_h = "Llame o visite"
        other_blurb = [
            "C\u00f3mo se planea y se ejecuta la obra, e implementar cambios.",
            "C\u00f3mo se comunican campo, oficina y sistemas del edificio.",
            "Persecuci\u00f3n de obra, cualificaciones y alianzas.",
            "Alcances que no caben en un encargo t\u00edpico de gerencia de construcci\u00f3n o de proyectos.",
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

    hero = (
        '\n    <section class="hero-full">\n'
        '      <div class="hero-full__bg" style="background-image:url(\'/assets/photos/hero.jpg\')" role="presentation"></div>\n'
        '      <div class="wrap">\n'
        '        <p class="eyebrow">Tampa, Florida</p>\n'
        '        <p class="hero-tag">Construct | Renovate | Demolish</p>\n'
        "        <h1>%s</h1>\n"
        '        <p class="hero-position">%s</p>\n'
        '        <p class="hero-sub">%s</p>\n'
        '        <p class="hero-lead">%s</p>\n'
        '        <div class="hero-actions">\n'
        '          <a class="btn btn-primary" href="tel:%s">%s</a>\n'
        '          <a class="btn btn-ghost" href="#expertise">%s</a>\n'
        "        </div>\n"
        '        <p class="hero-note">%s</p>\n'
        "      </div>\n    </section>\n"
    ) % (
        esc(h1), esc(position), esc(knowledge), lead,
        PHONE_TEL, PHONE_DISP, cta2, t["hours"],
    )

    supporting = (
        '    <section class="section section--stone" id="consulting-markets">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">%s</p>\n'
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
        '            <p class="section-kicker">%s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s %s</a>\n        </div>\n'
        '        <div class="spec-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
        '    <section class="section section--stone" id="industries">\n'
        '      <div class="wrap">\n        <div class="section-head">\n          <div>\n'
        '            <p class="section-kicker">%s</p>\n'
        "            <h2>%s</h2>\n"
        '            <p class="section-intro">%s</p>\n          </div>\n'
        '          <a class="link-more" href="%s">%s %s</a>\n        </div>\n'
        '        <div class="ind-grid">\n%s\n        </div>\n      </div>\n    </section>\n'
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
        "        </div>\n        <div>\n"
        '          <p><a class="btn btn-primary" href="%s">%s</a></p>\n'
        "        </div>\n      </div>\n    </section>\n"
    ) % (
        cons_k, esc(cons_h), cons_intro, consult_anchor, t["see"], t["consulting"],
        com_h, esc(com_t), com_p, res_h, esc(res_t), res_p,
        cons_k, esc(other_h), other_intro, oth_href, t["see"], "\n".join(others),
        spec_k, esc(spec_h), spec_intro, spec_href, t["see"], t["specialties"], "\n".join(specs),
        ind_k, esc(ind_h), ind_intro, ind_href, t["see"], t["industries"], "\n".join(inds),
        esc(area_h), area_p,
        t["contact"], esc(contact_h), PHONE_TEL, PHONE_DISP, BRAND, ADDR1, CITY, MAPS, t["maps"], t["hours"],
        contact_href, t["contact_cta"],
    )

    return (
        hero
        + proof_html(lang)
        + story_sections(lang, extra_expertise="\n".join(tile_html))
        + supporting
    )


def build_homes(write, wrap_page):
    write("/", wrap_page(
        "en", "/", "/es/", "home",
        "HMCM | Expertise on Demand in Tampa Bay",
        "Hermanos Mendez Construction Management advises and manages land development and construction in Tampa Bay. Expertise on Demand.",
        _home("en"),
    ))
    write("/es/", wrap_page(
        "es", "/es/", "/", "home",
        "HMCM | Expertise on Demand en Tampa Bay",
        "Hermanos Mendez Construction Management asesora y gerencia el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay. Expertise on Demand.",
        _home("es"),
    ))


def build_about(write, wrap_page):
    write("/about/", wrap_page(
        "en", "/about/", "/es/empresa/", "about",
        "About HMCM | Hermanos Mendez Construction Management in Tampa",
        "Hermanos Mendez Construction Management advises and manages land development and construction in Tampa Bay.",
        about_body("en"),
    ))
    write("/es/empresa/", wrap_page(
        "es", "/es/empresa/", "/about/", "about",
        "Sobre HMCM | Hermanos Mendez Construction Management en Tampa",
        "Hermanos Mendez Construction Management asesora y gerencia el desarrollo de terrenos y la construcci\u00f3n en Tampa Bay.",
        about_body("es"),
    ))
