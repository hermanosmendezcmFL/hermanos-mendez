from html import escape as esc
from chrome import T, BRAND, ADDR1, CITY, PHONE_DISP, PHONE_TEL, MAPS, PHOTO_ALT


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
            "h1": "Problem Solvers Who Get Results",
            "lead": "Expertise on Demand. We help at any phase, on any challenge, and we work inside your team until the job is finished correctly.",
            "pos": "Expertise on Demand",
            "knowledge": "The Knowledge, Skills, and Abilities to Impact Change",
            "title": "Problem Solvers Who Get Results | About HMCM Tampa Bay",
            "desc": "HMCM is a Tampa Bay construction consulting and management practice: expertise on demand, help at any phase, an extensive professional network, and problem solvers who get results.",
            "sections": [
                {
                    "id": "expertise",
                    "style": "section section--ink",
                    "k": "Expertise",
                    "h": "Our Expertise",
                    "paras": [
                        "Hermanos Mendez Construction Management is a Tampa Bay practice built on construction judgment. Twenty-six years in the business and more than $300 million in completed projects are the scale behind that judgment, not a line on a brochure. We are hired as consultants, as construction managers, and as project managers. The assignment can be a commercial site, a multi-family building, a custom home, or the land-development work that has to land before anyone frames. What does not change is the posture: we sit on the owner's side of the table, and we are here to solve the problem in front of you.",
                        "That expertise covers the full construction lifecycle. Land development, new construction, renovation, and demolition. Permitting, inspections, stormwater, and land clearing. Design-build when design and construction move together. Takeoff, contract review, purchasing, and the operating systems a job actually needs. We do not publish a roster of named projects on this site. The proof is the practice: the same questions asked on time, the same discipline held in the field, and a single accountable contact who keeps cost and the site in the same conversation.",
                        "Owners, developers, institutions, and investment groups hire that depth because construction problems are rarely only technical. They are sequence, cost, approvals, people, and time, all at once. Our team has the knowledge, skills, and abilities to impact change where you need it most, and to do it without taking the project away from you.",
                    ],
                },
                {
                    "id": "phase",
                    "style": "section section--stone",
                    "k": "Timing",
                    "h": "Any Phase, Any Challenge",
                    "paras": [
                        "Owners do not all call at the same moment, and we do not require them to. Some bring us in before land is purchased, to understand the true cost to build and whether the site will support the use. Some call with a set of drawings and a budget that have not yet met the field. Some are already in construction and need the work brought back under control. Some have a job that has stalled, a permit that will not clear, a trade sequence that collapsed, or an asset that is not performing. We step in at the phase you are in.",
                        "The challenge can be technical, commercial, or both. A drainage answer the municipality will actually accept. A renovation that has to happen while the building stays in use. A ground-up schedule that assumed a finished site the earthwork has not delivered. A custom home that slipped a season. A commercial shell that needs a construction reading before anyone signs. A distressed or stalled project that still has a path, if someone will write it down and then run it. Whatever is blocking progress, the job is the same: a professional assessment, a sequence you can act on, and the advisory or field support required to move it.",
                        "If the engagement starts as consulting and the work then needs field coordination or full cost-and-schedule control, we transition into construction management or project management without starting over. You do not re-explain the drawings, the constraints, or your objectives to a new firm. The people who already understand the job stay on it.",
                    ],
                },
                {
                    "id": "team",
                    "style": "section",
                    "k": "How We Work",
                    "h": "How We Work With Your Team",
                    "paras": [
                        "We work as a true extension of your business. That is not a courtesy title. It means we plug into the team you already have (owners, developers, architects, engineers, lenders, contractors) without installing a second chain of command. Decisions, schedule, and the field route through one accountable contact at HMCM, so nothing depends on two parties agreeing later about who was supposed to be watching it.",
                        "Maximum results come from that integration. We sit in your meetings, read your drawings, walk your site, and tell you the truth while there is still time to use it. When a decision is required, it arrives with the cost, the schedule impact, and a recommendation attached, not as a question left on your desk. We budget with purpose before anyone mobilizes, and we execute with discipline so the field follows that budget: sequence, hold points, long-lead items ordered against the date they are actually needed, and quality measured against the specification.",
                        "The people who pick up the phone are the people who will walk the site. Call the office and you talk to HMCM. There is no account executive between you and the person reading your plans, and no handoff to a team that does not know the job once the agreement is signed. That is how a small, experienced practice produces outsized results: one team, one reading of the facts, and enough seniority in the room to make the next move.",
                    ],
                },
                {
                    "id": "network",
                    "style": "section section--ink",
                    "k": "Network",
                    "h": "An Extensive Professional Network",
                    "paras": [
                        "No single office holds every specialty a Tampa Bay job can require. What we do hold is an extensive network of professionals (architects, engineers, specialty consultants, contractors, and subcontractors) that can be called in when a problem needs a specific reading or a specific pair of hands. We source and coordinate those professionals to our standards, so you are not left assembling a team from a list of names you have never worked with.",
                        "That network is how we take on any issue without pretending we personally perform every trade. Survey, geotechnical, structural, civil, mechanical, electrical, plumbing, environmental, cost, and the trades that actually build the work: when the job needs them, we know who to bring and how to hold them accountable inside the same sequence. You get the depth of a much larger bench, with one practice responsible for the result.",
                        "Calling the network is not a delay tactic. It is how a problem gets the right specialist on it quickly, under our coordination, without you having to become the general contractor of your own consultants. We stay the single point of contact. They assist. You still have one team to call.",
                    ],
                },
                {
                    "id": "results",
                    "style": "section section--dark",
                    "k": "Results",
                    "h": "We Are Problem Solvers Who Get Results",
                    "paras": [
                        "The main point is simple. We are problem solvers who get results. Expertise on Demand means we arrive with the knowledge, skills, and abilities to impact change where you need it most, stay long enough to finish the work, and leave your operation stronger than we found it.",
                        "Whether you need a construction reading before you buy, a partner from concept through completion, dedicated field oversight of a job that is already designed and budgeted, or immediate help on a site that has gone sideways, the measure is the same: the obstacle is removed, the sequence is restored, and the project moves. That is the difference we bring to the table.",
                        "Call the Tampa office when you are ready to put that to work.",
                    ],
                },
            ],
        }
    return {
        "h1": "Solucionamos problemas y obtenemos resultados",
        "lead": "Expertise on Demand. Ayudamos en cualquier fase, ante cualquier reto, y trabajamos dentro de su equipo hasta que la obra se termine bien.",
        "pos": "Expertise on Demand",
        "knowledge": "El conocimiento, las habilidades y las aptitudes para impulsar el cambio",
        "title": "Solucionamos problemas y obtenemos resultados | Sobre HMCM Tampa Bay",
        "desc": "HMCM es una práctica de consultoría y gerencia de construcción en Tampa Bay: experiencia a demanda, apoyo en cualquier fase, una red amplia de profesionales y un equipo que resuelve problemas y obtiene resultados.",
        "sections": [
            {
                "id": "expertise",
                "style": "section section--ink",
                "k": "Experiencia",
                "h": "Nuestra experiencia",
                "paras": [
                    "Hermanos Mendez Construction Management es una práctica en Tampa Bay construida sobre el criterio constructivo. Veintiséis años en el negocio y más de $300 millones en proyectos completados son la escala detrás de ese criterio, no una línea de folleto. Se nos contrata como consultores, como gerentes de construcción y como gerentes de proyectos. El encargo puede ser un sitio comercial, un edificio multifamiliar, una casa a medida o la obra de desarrollo de terrenos que tiene que aterrizar antes de que nadie arme estructura. Lo que no cambia es la postura: nos sentamos del lado del propietario y estamos aquí para resolver el problema que tiene delante.",
                    "Esa experiencia cubre el ciclo completo de la construcción. Desarrollo de terrenos, nueva construcción, renovación y demolición. Permisos, inspecciones, aguas pluviales y despeje. Diseño-construcción cuando el diseño y la obra avanzan juntos. Takeoff, revisión de contratos, compras y los sistemas operativos que una obra de verdad necesita. Este sitio no publica una lista de obras con nombre. La prueba es la práctica: las mismas preguntas hechas a tiempo, la misma disciplina sostenida en campo y un solo contacto responsable que mantiene el costo y el sitio en la misma conversación.",
                    "Propietarios, desarrolladores, instituciones y grupos de inversión contratan esa profundidad porque los problemas de construcción casi nunca son solo técnicos. Son secuencia, costo, aprobaciones, gente y tiempo, todo a la vez. Nuestro equipo tiene el conocimiento, las habilidades y las aptitudes para impulsar el cambio donde más lo necesita, y para hacerlo sin quitarle el proyecto.",
                ],
            },
            {
                "id": "phase",
                "style": "section section--stone",
                "k": "Momento",
                "h": "Cualquier fase, cualquier reto",
                "paras": [
                    "No todos los propietarios llaman en el mismo momento, y no exigimos que lo hagan. Algunos nos incorporan antes de comprar el terreno, para entender el costo real de construir y si el predio sostendrá el uso. Otros llegan con un juego de planos y un presupuesto que todavía no han tocado el campo. Otros ya están en construcción y necesitan que el trabajo vuelva a estar bajo control. Otros tienen una obra detenida, un permiso que no sale, una secuencia de gremios que se vino abajo o un activo que no rinde. Entramos en la fase en la que usted está.",
                    "El reto puede ser técnico, comercial, o ambos. Una respuesta de drenaje que el municipio realmente acepte. Una renovación que tiene que ocurrir con el edificio en uso. Un cronograma de obra nueva que dio por hecho un sitio terminado que el movimiento de tierras no ha entregado. Una casa a medida que se corrió una temporada. Un cascarón comercial que necesita una lectura constructiva antes de firmar. Un proyecto en dificultades o detenido que todavía tiene camino, si alguien lo escribe y después lo dirige. Sea lo que esté bloqueando el avance, el trabajo es el mismo: una evaluación profesional, una secuencia que usted puede ejecutar y el apoyo de asesoría o de campo necesario para moverlo.",
                    "Si el encargo empieza como consultoría y la obra entonces necesita coordinación de campo o control completo de costo y plazo, pasamos a gerencia de construcción o de proyectos sin empezar de cero. Usted no vuelve a explicar los planos, las restricciones ni sus objetivos a otra firma. Quienes ya entienden el trabajo se quedan en él.",
                ],
            },
            {
                "id": "team",
                "style": "section",
                "k": "Método",
                "h": "Cómo trabajamos con su equipo",
                "paras": [
                    "Trabajamos como una verdadera extensión de su negocio. Eso no es un título de cortesía. Significa que nos integramos al equipo que usted ya tiene (propietarios, desarrolladores, arquitectos, ingenieros, prestamistas, contratistas) sin instalar una segunda cadena de mando. Las decisiones, el programa y el campo pasan por un solo contacto responsable en HMCM, de modo que nada dependa de que dos partes se pongan de acuerdo después sobre quién debía estar vigilándolo.",
                    "Los resultados máximos salen de esa integración. Entramos a sus reuniones, leemos sus planos, recorremos su sitio y le decimos la verdad mientras todavía hay tiempo de usarla. Cuando hay que decidir, la decisión llega con el costo, el impacto en el cronograma y una recomendación, no como una pregunta dejada en su escritorio. Presupuestamos con propósito antes de movilizar a nadie, y ejecutamos con disciplina para que el campo siga ese presupuesto: secuencia, puntos de control, materiales de entrega larga pedidos contra la fecha en que de verdad se necesitan y calidad medida contra la especificación.",
                    "Quienes contestan el teléfono son quienes recorren el sitio. Llame a la oficina y habla con HMCM. No hay un ejecutivo de cuenta entre usted y la persona que lee sus planos, ni una entrega a un equipo que no conoce la obra una vez firmado el contrato. Así es como una práctica pequeña y experimentada produce resultados de otro tamaño: un solo equipo, una sola lectura de los hechos y suficiente experiencia en la sala para dar el siguiente paso.",
                ],
            },
            {
                "id": "network",
                "style": "section section--ink",
                "k": "Red",
                "h": "Una red amplia de profesionales",
                "paras": [
                    "Ninguna oficina reúne por sí sola cada especialidad que una obra en Tampa Bay puede exigir. Lo que sí tenemos es una red amplia de profesionales (arquitectos, ingenieros, consultores especializados, contratistas y subcontratistas) a los que se puede llamar cuando un problema necesita una lectura concreta o un par de manos concreto. Los seleccionamos y los coordinamos según nuestros estándares, para que usted no tenga que armar un equipo a partir de una lista de nombres con los que nunca ha trabajado.",
                    "Esa red es cómo asumimos cualquier asunto sin pretender que ejecutamos cada gremio en persona. Topografía, geotecnia, estructura, civil, mecánico, eléctrico, plomería, ambiental, costos y los gremios que de verdad construyen: cuando la obra los necesita, sabemos a quién traer y cómo exigirles cuentas dentro de la misma secuencia. Usted obtiene la profundidad de un banco mucho más grande, con una sola práctica responsable del resultado.",
                    "Llamar a la red no es una táctica para ganar tiempo. Es cómo un problema recibe rápido al especialista correcto, bajo nuestra coordinación, sin que usted tenga que convertirse en el contratista general de sus propios consultores. Seguimos siendo el único punto de contacto. Ellos asisten. Usted sigue teniendo un solo equipo a quien llamar.",
                ],
            },
            {
                "id": "results",
                "style": "section section--dark",
                "k": "Resultados",
                "h": "Resolvemos problemas y obtenemos resultados",
                "paras": [
                    "El punto principal es simple. Resolvemos problemas y obtenemos resultados. Expertise on Demand significa que llegamos con el conocimiento, las habilidades y las aptitudes para impulsar el cambio donde más lo necesita, nos quedamos el tiempo suficiente para terminar el trabajo y dejamos su operación más fuerte de como la encontramos.",
                    "Ya sea que necesite una lectura constructiva antes de comprar, un socio del concepto a la entrega, supervisión de campo dedicada de una obra ya diseñada y presupuestada, o ayuda inmediata en un sitio que se torció, la medida es la misma: se quita el obstáculo, se restaura la secuencia y el proyecto avanza. Esa es la diferencia que aportamos.",
                    "Llame a la oficina en Tampa cuando esté listo para ponerlo a trabajar.",
                ],
            },
        ],
    }


def _paras(ps):
    return "\n".join("            <p>%s</p>" % p for p in ps)


def story_sections(lang):
    c = story_copy(lang)
    chunks = []
    for s in c["sections"]:
        extra_head = ""
        if s["id"] == "results":
            extra_head = (
                '        <p class="position-line">%s</p>\n'
                '        <p class="position-line">%s</p>\n'
            ) % (esc(c["pos"]), esc(c["knowledge"]))
        chunks.append(
            '    <section class="%s" id="%s">\n'
            '      <div class="wrap">\n'
            '        <p class="section-kicker">%s</p>\n'
            '        <h2 class="story-head">%s</h2>\n'
            '%s'
            '        <div class="prose story-copy">\n%s\n        </div>\n'
            "      </div>\n"
            "    </section>\n"
            % (s["style"], s["id"], esc(s["k"]), esc(s["h"]), extra_head, _paras(s["paras"]))
        )
    return "".join(chunks)


def about_body(lang):
    t = T[lang]
    contact = "/contact/" if lang == "en" else "/es/contacto/"
    c = story_copy(lang)
    if lang == "en":
        crumbs = [("Home", "/"), ("About", None)]
        photo = "tampa.jpg"
        kicker = "Office"
        office_h = "Tampa Bay"
        office_p = (
            "The office is at %s, %s. Phone <a href=\"tel:%s\">%s</a>. %s Free on-site parking."
            % (ADDR1, CITY, PHONE_TEL, PHONE_DISP, t["hours"])
        )
    else:
        crumbs = [("Inicio", "/es/"), ("Empresa", None)]
        photo = "tampa.jpg"
        kicker = "Oficina"
        office_h = "Tampa Bay"
        office_p = (
            "La oficina está en %s, %s. Teléfono <a href=\"tel:%s\">%s</a>. %s Estacionamiento gratuito en el sitio."
            % (ADDR1, CITY, PHONE_TEL, PHONE_DISP, t["hours"])
        )

    from chrome import page_banner
    body = page_banner(lang, crumbs, c["h1"], c["lead"], photo)
    body += (
        '\n    <section class="section section--ink" id="position">\n'
        '      <div class="wrap">\n'
        '        <p class="hero-position" style="margin-top:0">%s</p>\n'
        '        <p class="position-line">%s</p>\n'
        "      </div>\n"
        "    </section>\n"
    ) % (esc(c["pos"]), esc(c["knowledge"]))
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
        "      <img class=\"hero-full__bg\" src=\"/assets/photos/hero.jpg\" alt=\"%s\" width=\"1920\" height=\"1280\">\n"
        "      <div class=\"wrap\">\n"
        "        <p class=\"eyebrow\">Tampa, Florida</p>\n"
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
        esc(PHOTO_ALT.get('hero.jpg','Construction work in Tampa Bay')), esc(h1), esc(position), esc(knowledge), lead,
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
        h1 = "The Three Ways HMCM Is Hired"
        lead = "Consulting, construction management, and project management \u2014 matched to how much of the job you need carried."
        photo = "construction-mgmt.jpg"
        intro = [
            "Hermanos Mendez Construction Management is hired three ways, and the right one depends entirely on what already exists. Consulting brings judgment to a specific question: whether a site can carry the plan, whether the drawings can be built for the budget, or why a job has stopped. Construction management is the end-to-end engagement, from concept and preconstruction through final handover. Project management is dedicated field execution of designs, budgets, and trades that are already in place.",
            "The boundaries between them are deliberate. Project management does not reopen your design or rebuild your budget, because its value is that it executes what your team already decided. Construction management does the opposite, taking responsibility for the roadmap from the first meeting so that preconstruction decisions and field consequences stay connected. Choosing the wrong one is a common and expensive mistake, and we will tell you which one your project actually needs.",
            "Engagements also move. Consulting that grows past advice can become construction management without handing your project to a new team, and full management can narrow back to oversight once the hard part is behind you. Underneath all three, the work types are the same: land development, new construction, renovation, and demolition, described under specialties.",
        ]
        tiles = [
            ("01", "Consulting",
             "Owner-side judgment on a site, a set of drawings, a budget, or a job that has stalled \u2014 commercial, residential, and specialized.",
             "/consulting/", "consulting.jpg"),
            ("02", "Construction Management",
             "End-to-end partnership from concept and preconstruction through buyout, field oversight, and final handover.",
             "/construction-management/", "construction-mgmt.jpg"),
            ("03", "Project Management",
             "Dedicated execution and field oversight for owners who already have designs, budgets, and trades in place.",
             "/project-management/", "project-mgmt.jpg"),
            ("04", "Specialties",
             "The work types behind the services: land development, new construction, renovation, and demolition.",
             "/specialties/", "land.jpg"),
        ]
    else:
        crumbs = [("Inicio", "/es/"), ("Servicios", None)]
        h1 = "Las tres formas de contratar a HMCM"
        lead = "Consultor\u00eda, gerencia de construcci\u00f3n y gerencia de proyectos, seg\u00fan cu\u00e1nto de la obra necesite que llevemos."
        photo = "construction-mgmt.jpg"
        intro = [
            "A Hermanos Mendez Construction Management se le contrata de tres maneras, y la correcta depende por completo de lo que ya exista. La consultor\u00eda aporta criterio sobre una pregunta concreta: si un sitio puede sostener el plan, si los planos se pueden construir por el presupuesto o por qu\u00e9 se detuvo una obra. La gerencia de construcci\u00f3n es el encargo de principio a fin, desde el concepto y la preconstrucci\u00f3n hasta la entrega final. La gerencia de proyectos es ejecuci\u00f3n dedicada en campo de dise\u00f1os, presupuestos y gremios que ya est\u00e1n en su lugar.",
            "Los l\u00edmites entre ellas son deliberados. La gerencia de proyectos no reabre su dise\u00f1o ni rehace su presupuesto, porque su valor est\u00e1 en ejecutar lo que su equipo ya decidi\u00f3. La gerencia de construcci\u00f3n hace lo contrario: asume la hoja de ruta desde la primera reuni\u00f3n para que las decisiones de preconstrucci\u00f3n y sus consecuencias en campo sigan conectadas. Elegir la equivocada es un error com\u00fan y caro, y le diremos cu\u00e1l necesita realmente su proyecto.",
            "Los encargos tambi\u00e9n se mueven. Una consultor\u00eda que crece m\u00e1s all\u00e1 del consejo puede convertirse en gerencia de construcci\u00f3n sin entregar su proyecto a un equipo nuevo, y la gerencia completa puede reducirse a supervisi\u00f3n una vez superada la parte dif\u00edcil. Debajo de las tres, los tipos de obra son los mismos: desarrollo de terrenos, nueva construcci\u00f3n, renovaci\u00f3n y demolici\u00f3n, descritos en especialidades.",
        ]
        tiles = [
            ("01", "Consultor\u00eda",
             "Criterio del lado del propietario sobre un sitio, un juego de planos, un presupuesto o una obra detenida: comercial, residencial y especializada.",
             "/es/consultoria/", "consulting.jpg"),
            ("02", "Gerencia de construcci\u00f3n",
             "Sociedad de principio a fin, desde el concepto y la preconstrucci\u00f3n hasta la contrataci\u00f3n, la supervisi\u00f3n en campo y la entrega final.",
             "/es/gerencia-de-construccion/", "construction-mgmt.jpg"),
            ("03", "Gerencia de proyectos",
             "Ejecuci\u00f3n y supervisi\u00f3n de campo dedicadas para propietarios que ya tienen dise\u00f1os, presupuestos y gremios en su lugar.",
             "/es/gerencia-de-proyectos/", "project-mgmt.jpg"),
            ("04", "Especialidades",
             "Los tipos de obra detr\u00e1s de los servicios: desarrollo de terrenos, nueva construcci\u00f3n, renovaci\u00f3n y demolici\u00f3n.",
             "/es/especialidades/", "land.jpg"),
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
        "        <div class=\"prose story-copy\">\n%s\n        </div>\n"
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
        _paras(intro), "\n".join(tile_html),
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
        "Services | Consulting, Construction Management, Project Management | HMCM",
        "The three ways HMCM is hired in Tampa Bay: consulting, construction management, and project management for land development and construction.",
        services_body("en"),
        crumbs=[("Home", "/"), ("Services", None)],
    ))
    write("/es/servicios/", wrap_page(
        "es", "/es/servicios/", "/services/", "services",
        "Servicios | Consultoría, gerencia de construcción y gerencia de proyectos | HMCM",
        "Las tres formas de contratar a HMCM en Tampa Bay: consultoría, gerencia de construcción y gerencia de proyectos para desarrollo de terrenos y construcción.",
        services_body("es"),
        crumbs=[("Inicio", "/es/"), ("Servicios", None)],
    ))



def build_about(write, wrap_page):
    en = story_copy("en")
    es = story_copy("es")
    write("/about/", wrap_page(
        "en", "/about/", "/es/empresa/", "about",
        en["title"],
        en["desc"],
        about_body("en"),
        crumbs=[("Home", "/"), ("About", None)],
    ))
    write("/es/empresa/", wrap_page(
        "es", "/es/empresa/", "/about/", "about",
        es["title"],
        es["desc"],
        about_body("es"),
        crumbs=[("Inicio", "/es/"), ("Empresa", None)],
    ))
