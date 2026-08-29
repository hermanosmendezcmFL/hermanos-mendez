# Landing-page copy removed 28 August 2026

Ryan’s Word brief asked that everything below come off the homepage. It is banked here verbatim (English and Spanish) so it can be reused on other pages.

Source of truth at removal: `tools/home_render.py` (`_home()`, `story_copy()`, `story_sections()`). These blocks lived on `/` and `/es/` only. Inner pages (About, Consulting, etc.) were not stripped.

The homepage after this change is: header, hero (new copy + two buttons), proof stats, contact strip, footer.

---

## 1. Our Team

**Where it lived:** Homepage section `#team` (kicker “Team” / “Equipo”), after the proof strip.

### English

**Kicker:** Team

**Heading:** Our Team

Owners hire a practice, not a rotating cast. Hermanos Mendez Construction Management is the Tampa office that will advise the job and stay on it.

The people who pick up the phone are the people who will walk the site. Call the office and you talk to HMCM.

### Spanish

**Kicker:** Equipo

**Heading:** Nuestro equipo

Los propietarios contratan una práctica, no un elenco rotativo. Hermanos Mendez Construction Management es la oficina en Tampa que asesora la obra y se queda en ella.

Quienes contestan el teléfono son quienes recorren el sitio. Llame a la oficina y habla con HMCM.

---

## 2. Our Expertise + three tiles

**Where it lived:** Homepage section `#expertise` (kicker “Expertise” / “Experiencia”), immediately after Our Team. The three numbered tiles sat under the two intro paragraphs.

### English

**Kicker:** Expertise

**Heading:** Our Expertise

The practice is built around consulting for commercial and residential work, construction management, and project management.

We plan and run land development, new construction, renovation, and demolition.

**Tiles**

01 — Consulting
Advisory for commercial and residential work: scoping, planning, and the consulting owners ask for before and during a job.
Link: /consulting/
Photo: consulting.jpg
CTA: View

02 — Construction Management
Field coordination of trades, schedule, and site so the work moves with a single point of contact.
Link: /construction-management/
Photo: construction-mgmt.jpg
CTA: View

03 — Project Management
Oversight of scope, cost, and timeline from preconstruction through closeout.
Link: /project-management/
Photo: project-mgmt.jpg
CTA: View

### Spanish

**Kicker:** Experiencia

**Heading:** Nuestra experiencia

La práctica se centra en la consultoría comercial y residencial, la gerencia de construcción y la gerencia de proyectos.

Planeamos y dirigimos desarrollo de terrenos, nueva construcción, renovación y demolición.

**Tiles**

01 — Consultoría
Asesoría comercial y residencial: alcance, planificación y la consultoría que se pide antes y durante la obra.
Link: /es/consultoria/
Photo: consulting.jpg
CTA: Ver

02 — Gerencia de construcción
Coordinación de gremios, programa y sitio de obra, con un solo punto de contacto.
Link: /es/gerencia-de-construccion/
Photo: construction-mgmt.jpg
CTA: Ver

03 — Gerencia de proyectos
Control de alcance, costo y plazo desde la preconstrucción hasta el cierre.
Link: /es/gerencia-de-proyectos/
Photo: project-mgmt.jpg
CTA: Ver

---

## 3. Budget with Purpose and Execute with Discipline

**Where it lived:** Homepage section `#method` (kicker “Method” / “Método”), after Our Expertise.

### English

**Kicker:** Method

**Heading:** Budget with Purpose and Execute with Discipline

A budget with purpose is written before anyone mobilizes. Quantities, allowances, and buyout are set so cost has a reason, not a hope.

Execute with discipline means the field follows that budget: sequence, hold points, and a single contact who keeps cost and the site in the same conversation.

### Spanish

**Kicker:** Método

**Heading:** Presupuestar con propósito y ejecutar con disciplina

Un presupuesto con propósito se escribe antes de movilizar a nadie. Las cantidades, las partidas y el buyout se fijan para que el costo tenga una razón, no una esperanza.

Ejecutar con disciplina significa que el campo sigue ese presupuesto: secuencia, puntos de control y un solo contacto que mantiene el costo y el sitio en la misma conversación.

---

## 4. The Difference We Bring to the Table

**Where it lived:** Homepage section `#difference` (kicker “Difference” / “Diferencia”), after Method. Included the two position lines “A True Extension of Your Business” and “Expert Partners When You Need Them”.

### English

**Kicker:** Difference

**Heading:** The Difference We Bring to the Table

A True Extension of Your Business

Expert Partners When You Need Them

We sit on the owner’s side of the table. Decisions, schedule, and the field route through one accountable contact.

HMCM works as a true extension of your business: expert partners when you need them, without a split chain of command.

### Spanish

**Kicker:** Diferencia

**Heading:** La diferencia que aportamos

Una verdadera extensión de su negocio

Socios expertos cuando los necesita

Nos sentamos del lado del propietario. Las decisiones, el programa y el campo pasan por un solo responsable.

HMCM trabaja como una verdadera extensión de su negocio: socios expertos cuando los necesita, sin una cadena de mando partida.

---

## 5. Consulting by Market

**Where it lived:** Homepage section `#consulting-markets` (kicker “Consulting” / “Consultoría”), after The Difference. Two split cards (Commercial, Residential) plus a “View Consulting” link.

### English

**Kicker:** Consulting

**Heading:** Consulting by Market

Commercial and residential work, planned before anyone mobilizes.

Link: View Consulting → /consulting/

**Commercial** — /consulting/commercial/
Photo: commercial.jpg
Advisory for commercial sites, shells, tenant work, and owner-side decisions on schedule, scope, and delivery.

**Residential** — /consulting/residential/
Photo: custom.jpg
Advisory for houses, custom builds, and residential renovations, planned at dwelling scale, not a commercial playbook.

### Spanish

**Kicker:** Consultoría

**Heading:** Consultoría por mercado

Obra comercial y residencial, planeada antes de movilizar a nadie.

Link: Ver Consultoría → /es/consultoria/

**Comercial** — /es/consultoria/comercial/
Photo: commercial.jpg
Asesoría para predios comerciales, naves, locales y decisiones del propietario sobre programa, alcance y entrega.

**Residencial** — /es/consultoria/residencial/
Photo: custom.jpg
Asesoría para viviendas, obras a medida y renovaciones residenciales, a escala de casa, no de campus comercial.

---

## 6. Other Consulting Services grid

**Where it lived:** Homepage section `#other-consulting` (kicker “Consulting” / “Consultoría”), after Consulting by Market. Mini-card grid of seven items plus a “View” link to the other-consulting hub.

### English

**Kicker:** Consulting

**Heading:** Other Consulting Services

Evaluations, takeoff, purchasing, and other defined consulting tasks.

Link: View → /consulting/other/

**Efficiency Evaluations and Implementations** — /consulting/other/efficiency-evaluations/
Sequence, labor, and waste, then putting changes in place.

**Systems Evaluations and Implementations** — /consulting/other/systems-evaluations/
How field, office, and building systems talk, and how to tighten that.

**Business Development** — /consulting/other/business-development/
Pursuit, qualifications, and teaming support for construction work.

**Special Projects** — /consulting/other/special-projects/
Scopes that do not fit a standard construction-management or project-management engagement.

**Takeoff Support and Contract Negotiations** — /consulting/other/takeoff-support/
Quantity takeoff support and help reviewing contract terms before you sign.

**Purchasing Assistance** — /consulting/other/purchasing-assistance/
Buyout support, proposals, and purchase tracking.

**SOP and Employee Management** — /consulting/other/sop-employee-management/
Documenting how the work is done and how people are assigned to it.

### Spanish

**Kicker:** Consultoría

**Heading:** Otros servicios de consultoría

Evaluaciones, takeoff, compras y otras tareas concretas de consultoría.

Link: Ver → /es/consultoria/otros/

**Evaluaciones e implementaciones de eficiencia** — /es/consultoria/otros/evaluaciones-de-eficiencia/
Cómo se planea y se ejecuta la obra, e implementar cambios.

**Evaluaciones e implementaciones de sistemas** — /es/consultoria/otros/evaluaciones-de-sistemas/
Cómo se comunican campo, oficina y sistemas del edificio.

**Desarrollo de negocios** — /es/consultoria/otros/desarrollo-de-negocios/
Persecución de obra, cualificaciones y alianzas.

**Proyectos especiales** — /es/consultoria/otros/proyectos-especiales/
Alcances que no caben en un encargo típico de gerencia de construcción o de proyectos.

**Soporte de takeoff y negociación de contratos** — /es/consultoria/otros/soporte-de-estimacion/
Cubicación (takeoff) y revisión de términos contractuales antes de firmar.

**Asistencia en compras** — /es/consultoria/otros/asistencia-en-compras/
Buyout, propuestas y seguimiento de compras.

**SOP y gestión de empleados** — /es/consultoria/otros/sop-gestion-de-empleados/
Documentar cómo se hace el trabajo y cómo se asigna a las personas.

---

## 7. Specialties grid

**Where it lived:** Homepage section `#specialties` (kicker “Specialties” / “Especialidades”), after Other Consulting Services. Four photo cards plus “View Specialties”.

### English

**Kicker:** Specialties

**Heading:** Specialties

The work types we plan and manage.

Link: View Specialties → /specialties/

- Land Development — /specialties/land-development/ — photo: land.jpg
- New Construction — /specialties/new-construction/ — photo: new-construction.jpg
- Renovation — /specialties/renovation/ — photo: interior.jpg
- Demolition — /specialties/demolition/ — photo: demolition.jpg

### Spanish

**Kicker:** Especialidades

**Heading:** Especialidades

Los tipos de obra que planeamos y gerenciamos.

Link: Ver Especialidades → /es/especialidades/

- Desarrollo de terrenos — /es/especialidades/desarrollo-de-terrenos/ — photo: land.jpg
- Nueva construcción — /es/especialidades/nueva-construccion/ — photo: new-construction.jpg
- Renovación — /es/especialidades/renovacion/ — photo: interior.jpg
- Demolición — /es/especialidades/demolicion/ — photo: demolition.jpg

---

## 8. Industries grid

**Where it lived:** Homepage section `#industries` (kicker “Markets” / “Mercados”), after Specialties. Nine industry cards plus “View Industries”.

### English

**Kicker:** Markets

**Heading:** Industries

Markets we advise and manage in Tampa Bay.

Link: View Industries → /industries/

**Commercial** — /industries/commercial/
Owner-side consulting and management for commercial buildings and sites.
CTA: View

**Multi-Family** — /industries/multi-family/
Multi-family planning, construction management, and coordination.
CTA: View

**SFR (Single-Family Residential)** — /industries/sfr/
Single-family residential: new houses, additions, and related site work.
CTA: View

**Custom Build** — /industries/custom-build/
Custom residential work that needs closer scope and finish control.
CTA: View

**Land Clearing** — /industries/land-clearing/
Clearing and site preparation as part of land development.
CTA: View

**Stormwater Mitigation** — /industries/stormwater-mitigation/
Drainage and stormwater work coordinated with the rest of the site.
CTA: View

**Permitting** — /industries/permitting/
Permit sequencing and follow-through with the agencies that have to sign off.
CTA: View

**Inspections** — /industries/inspections/
Inspection readiness and closeout, scheduled with the rest of the job.
CTA: View

**Design-Build** — /industries/design-build/
Owner representation when design-build moves as one delivery.
CTA: View

### Spanish

**Kicker:** Mercados

**Heading:** Industrias

Mercados que asesoramos y gerenciamos en Tampa Bay.

Link: Ver Industrias → /es/industrias/

**Comercial** — /es/industrias/comercial/
Consultoría y gerencia del lado del propietario para edificios y predios comerciales.
CTA: Ver

**Multifamiliar** — /es/industrias/multifamiliar/
Planificación, gerencia de construcción y coordinación en multifamiliar.
CTA: Ver

**Residencial unifamiliar (SFR)** — /es/industrias/sfr/
Residencial unifamiliar: casas nuevas, ampliaciones y obra de sitio.
CTA: Ver

**Construcción a medida** — /es/industrias/construccion-a-medida/
Obra residencial a medida, con control más estrecho de alcance y acabados.
CTA: Ver

**Despeje de terrenos** — /es/industrias/despeje-de-terrenos/
Despeje y preparación del predio como parte del desarrollo.
CTA: Ver

**Mitigación de aguas pluviales** — /es/industrias/mitigacion-de-aguas-pluviales/
Drenaje y aguas pluviales coordinados con el resto del sitio.
CTA: Ver

**Permisos** — /es/industrias/permisos/
Secuencia de permisos y seguimiento con las agencias que deben firmar.
CTA: Ver

**Inspecciones** — /es/industrias/inspecciones/
Preparación para inspecciones y cierre, programados con el resto de la obra.
CTA: Ver

**Diseño-construcción** — /es/industrias/diseno-construccion/
Representación del propietario cuando diseño y construcción se entregan juntos.
CTA: Ver

---

## 9. Tampa Bay Service Area

**Where it lived:** Homepage section after Industries (kicker “Tampa Bay”), two-column area grid with tampa.jpg. The contact strip that followed this block was **kept** on the homepage.

### English

**Kicker:** Tampa Bay

**Heading:** Tampa Bay Service Area

The office is at 10002 N Forest Hills Dr, Tampa, FL 33612, in Hillsborough County. We advise and manage land development and construction across Tampa Bay.

Photo: tampa.jpg (aria-label “Tampa Bay”)

### Spanish

**Kicker:** Tampa Bay

**Heading:** Área de servicio en Tampa Bay

La oficina está en 10002 N Forest Hills Dr, Tampa, FL 33612, en el condado de Hillsborough. Asesoramos y gerenciamos desarrollo de terrenos y construcción en Tampa Bay.

Photo: tampa.jpg (aria-label “Tampa Bay”)

---

## Also removed from the hero (not a section)

**Where it lived:** `.hero-note` under the hero buttons on `/` and `/es/`.

English: Monday–Friday 8:00 AM–5:00 PM. Saturday–Sunday closed.

Spanish: Lunes a viernes, 8:00 a. m. a 5:00 p. m. Sábado y domingo cerrado.

Hours remain on the homepage contact strip and on the Contact page.
