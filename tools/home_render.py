from html import escape as esc
from chrome import T, BRAND, ADDR1, CITY, PHONE_DISP, PHONE_TEL, MAPS


def proof_html(lang):
    if lang == "en":
        a_fig, a_h = "26", "26 Years in the Business"
        b_fig, b_h = "$300+ million", "Over $300 Million in Completed Projects"
        label = "Proof"
    else:
        a_fig, a_h = "26", "26 años en el negocio"
        b_fig, b_h = "$300+ millones", "Más de $300 millones en proyectos completados"
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
        PHONE_DISP, PHONE_TEL, t["call_now"], contact, t["contact_cta"],
    )
    return body


def _home(lang):
    t = T[lang]
    if lang == "en":
        h1 = "Qualified Professionals You Can Count On to Assist You in Achieving Your Objectives Throughout Tampa Bay."
        position = "Expertise on Demand – When You Need It"
        knowledge = "Our Team Has the Knowledge, Skills, and Abilities to Impact Change Where You Need It Most."
        lead = (
            "Hermanos Mendez Construction Management provides a wide array of services "
            "to perform as an extension of our client partners' business — driving maximum "
            "impact at a streamlined cost."
        )
        cta_services = "What We Do"
        cta_about = "Experience the Difference"
        services_href = "/services/"
        about_href = "/about/"
        contact_href = "/contact/"
        contact_h = "Call or Visit"
    else:
        h1 = "Profesionales calificados en quienes puede confiar para ayudarle a alcanzar sus objetivos en todo Tampa Bay."
        position = "Experiencia a demanda — cuando la necesita"
        knowledge = "Nuestro equipo tiene el conocimiento, las habilidades y las aptitudes para impulsar el cambio donde más lo necesita."
        lead = (
            "Hermanos Mendez Construction Management ofrece una amplia gama de servicios "
            "para actuar como una extensión del negocio de nuestros socios clientes — "
            "máximo impacto a un costo ágil."
        )
        cta_services = "Qué hacemos"
        cta_about = "Conozca la diferencia"
        services_href = "/es/servicios/"
        about_href = "/es/empresa/"
        contact_href = "/es/contacto/"
        contact_h = "Llame o visite"

    hero = (
        "\n    <section class=\"hero-full\">\n"
        "      <div class=\"hero-full__bg\" style=\"background-image:url('/assets/photos/hero.jpg')\" role=\"presentation\"></div>\n"
        "      <div class=\"wrap\">\n"
        "        <p class=\"eyebrow\">Tampa, Florida</p>\n"
        "        <p class=\"hero-tag\">Construct | Renovate | Demolish</p>\n"
        "        <h1>%s</h1>\n"
        "        <p class=\"hero-position\">%s</p>\n"
        "        <p class=\"hero-sub\">%s</p>\n"
        "        <p class=\"hero-lead\">%s</p>\n"
        "        <div class=\"hero-actions\">\n"
        "          <a class=\"btn btn-primary\" href=\"tel:%s\">%s</a>\n"
        "          <a class=\"btn btn-ghost\" href=\"%s\">%s</a>\n"
        "          <a class=\"btn btn-ghost\" href=\"%s\">%s</a>\n"
        "        </div>\n"
        "      </div>\n    </section>\n"
    ) % (
        esc(h1), esc(position), esc(knowledge), lead,
        PHONE_TEL, PHONE_DISP, services_href, esc(cta_services), about_href, esc(cta_about),
    )

    contact = (
        "    <section class=\"section section--ink\" id=\"contact-strip\">\n"
        "      <div class=\"wrap contact-strip\">\n        <div>\n"
        "          <p class=\"section-kicker\">%s</p>\n          <h2>%s</h2>\n"
        "          <a class=\"phone-xl\" href=\"tel:%s\">%s</a>\n"
        "          <address class=\"addr\">%s<br>%s<br>%s<br>\n"
        "            <a class=\"map-link\" href=\"%s\" rel=\"noopener noreferrer\" target=\"_blank\">%s</a>\n"
        "          </address>\n"
        "          <p class=\"hero-note\" style=\"margin-top:1rem\">%s</p>\n"
        "        </div>\n        <div>\n"
        "          <p><a class=\"btn btn-primary\" href=\"%s\">%s</a></p>\n"
        "        </div>\n      </div>\n    </section>\n"
    ) % (
        t["contact"], esc(contact_h), PHONE_TEL, PHONE_DISP, BRAND, ADDR1, CITY, MAPS, t["maps"], t["hours"],
        contact_href, t["contact_cta"],
    )

    return hero + proof_html(lang) + contact


def services_body(lang):
    t = T[lang]
    if lang == "en":
        crumbs = [("Home", "/"), ("Services", None)]
        h1 = "Services"
        lead = "Construction management and project management — the two ways HMCM runs the job."
        photo = "construction-mgmt.jpg"
        intro = (
            "Hermanos Mendez Construction Management is hired two ways to run the work: "
            "construction management as an end-to-end partner, and project management as dedicated execution and field oversight of an established framework."
        )
        tiles = [
            ("01", "Construction Management",
             "Field coordination of trades, schedule, and site so the work moves with a single point of contact.",
             "/construction-management/", "construction-mgmt.jpg"),
            ("02", "Project Management",
             "Dedicated execution and field oversight for owners who already have designs, budgets, and trades in place.",
             "/project-management/", "project-mgmt.jpg"),
        ]
    else:
        crumbs = [("Inicio", "/es/"), ("Servicios", None)]
        h1 = "Servicios"
        lead = "Gerencia de construcción y gerencia de proyectos: las dos formas en que HMCM dirige la obra."
        photo = "construction-mgmt.jpg"
        intro = (
            "A Hermanos Mendez Construction Management se le contrata de dos maneras para dirigir el trabajo: "
            "gerencia de construcción como socio de principio a fin, y gerencia de proyectos como ejecución y supervisión de campo dedicadas de un marco ya establecido."
        )
        tiles = [
            ("01", "Gerencia de construcción",
             "Coordinación de gremios, programa y sitio de obra, con un solo punto de contacto.",
             "/es/gerencia-de-construccion/", "construction-mgmt.jpg"),
            ("02", "Gerencia de proyectos",
             "Ejecución y supervisión de campo dedicadas para propietarios que ya tienen diseños, presupuestos y gremios en su lugar.",
             "/es/gerencia-de-proyectos/", "project-mgmt.jpg"),
        ]

    from chrome import page_banner
    body = page_banner(lang, crumbs, h1, lead, photo)
    tile_html = []
    for idx, name, copy, href, ph in tiles:
        tile_html.append(
            "        <a class=\"tile\" href=\"%s\">\n"
            "          <div class=\"tile__media\" style=\"background-image:url('/assets/photos/%s')\" role=\"presentation\"></div>\n"
            "          <div class=\"tile__body\">\n"
            "            <span class=\"tile__index\">%s</span>\n"
            "            <h3>%s</h3>\n            <p>%s</p>\n"
            "            <span class=\"tile-go\">%s</span>\n"
            "          </div>\n        </a>" % (href, ph, idx, esc(name), copy, t["see"])
        )
    contact = "/contact/" if lang == "en" else "/es/contacto/"
    body += (
        "\n    <section class=\"section section--rule\">\n"
        "      <div class=\"wrap\">\n"
        "        <div class=\"prose story-copy\">\n"
        "          <p>%s</p>\n"
        "        </div>\n"
        "        <div class=\"tile-grid\" style=\"margin-top:2rem\">\n%s\n        </div>\n"
        "      </div>\n"
        "    </section>\n"
        "    <section class=\"section section--ink\">\n"
        "      <div class=\"wrap cta-band\">\n"
        "        <h2>%s</h2>\n"
        "        <div class=\"hero-actions\">\n"
        "          <a class=\"btn btn-primary\" href=\"tel:%s\">%s</a>\n"
        "          <a class=\"btn btn-ghost\" href=\"%s\">%s</a>\n"
        "        </div>\n"
        "      </div>\n"
        "    </section>"
    ) % (
        intro, "\n".join(tile_html),
        PHONE_DISP, PHONE_TEL, t["call_now"], contact, t["contact_cta"],
    )
    return body


def build_homes(write, wrap_page):
    write("/", wrap_page(
        "en", "/", "/es/", "home",
        "HMCM | Qualified Professionals in Tampa Bay",
        "Hermanos Mendez Construction Management provides a wide array of services as an extension of our client partners' business in Tampa Bay. Expertise on Demand.",
        _home("en"),
    ))
    write("/es/", wrap_page(
        "es", "/es/", "/", "home",
        "HMCM | Profesionales calificados en Tampa Bay",
        "Hermanos Mendez Construction Management ofrece una amplia gama de servicios como extensión del negocio de nuestros socios clientes en Tampa Bay.",
        _home("es"),
    ))


def build_services(write, wrap_page):
    write("/services/", wrap_page(
        "en", "/services/", "/es/servicios/", "services",
        "Services | Construction Management and Project Management | HMCM",
        "HMCM services in Tampa Bay: construction management and project management for land development and construction.",
        services_body("en"),
    ))
    write("/es/servicios/", wrap_page(
        "es", "/es/servicios/", "/services/", "services",
        "Servicios | Gerencia de construcción y gerencia de proyectos | HMCM",
        "Servicios de HMCM en Tampa Bay: gerencia de construcción y gerencia de proyectos para desarrollo de terrenos y construcción.",
        services_body("es"),
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
