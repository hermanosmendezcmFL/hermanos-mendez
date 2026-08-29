# Construction Management landing copy removed 28 August 2026

Ryan’s Construction Management brief asked that everything below come off the Construction Management landing page (`/construction-management/` and `/es/gerencia-de-construccion/`). It is banked here verbatim (English and Spanish) so it can be reused on other pages.

Source of truth at removal: `tools/pages.json` (page `en_path` `/construction-management/`). The same strings were rendered by `tools/build.py` (`interior_body()`). Global nav/footer generators in `tools/chrome.py` were not stripped; the Services dropdown stays Overview / Construction Management / Project Management, and footer chrome is unchanged.

The Construction Management landing after this change is: header, banner (new H1 + lead), new body, Explore Capabilities sidebar (four pathway pages), contact CTA, footer. The lower Related / More card bar is gone.

---

## 1. H1

**Where it lived:** Construction Management landing `.page-banner h1` on `/construction-management/` and `/es/gerencia-de-construccion/`.

### English

Construction management for land development and construction

### Spanish

Gerencia de construcción para desarrollo de terrenos y construcción

---

## 2. Lead

**Where it lived:** Construction Management landing `.page-banner p.lead` on `/construction-management/` and `/es/gerencia-de-construccion/`.

### English

Coordination of the work in the field (trades, schedule, and site) for owners who need the job run, not only advised.

### Spanish

Coordinación del trabajo en el campo (gremios, programa y sitio) para propietarios que necesitan que la obra se dirija, no solo que se asesore.

---

## 3. Body paragraphs

**Where it lived:** Construction Management landing `.prose` in the first content section on `/construction-management/` and `/es/gerencia-de-construccion/`.

### English

Construction management is the field practice: on-site coordination that keeps trades, deliveries, and inspections from colliding.

We work as the owner's construction manager. One contact for the superintendent-level questions, the daily sequence, and the site constraints that never show up cleanly on a drawing.

Call (813) 323-4648 if the job already needs someone on the site.

### Spanish

La gerencia de construcción es la práctica de campo: la coordinación en sitio para que gremios, entregas e inspecciones no choquen.

Trabajamos como gerentes de construcción del propietario. Un contacto para las preguntas de nivel superintendente, la secuencia diaria y las restricciones del predio que nunca aparecen limpias en un plano.

Llame al (813) 323-4648 si la obra ya necesita a alguien en el sitio.

---

## 4. Sidebar heading and links removed from this page

**Where it lived:** Construction Management landing `aside.aside-box` (heading was “Related” / “Relacionado”).

The heading word itself was replaced by Explore Capabilities / Explorar capacidades. These **links** were removed from this sidebar (destination pages were not deleted):

### English

**Heading:** Related

- Project Management — /project-management/
- Consulting — /consulting/
- New Construction — /specialties/new-construction/
- Demolition — /specialties/demolition/
- Industries — /industries/
- Contact — /contact/

### Spanish

**Heading:** Relacionado

- Gerencia de proyectos — /es/gerencia-de-proyectos/
- Consultoría — /es/consultoria/
- Nueva construcción — /es/especialidades/nueva-construccion/
- Demolición — /es/especialidades/demolicion/
- Industrias — /es/industrias/
- Contacto — /es/contacto/

---

## 5. Lower Related / More card bar (entire block)

**Where it lived:** Construction Management landing section `.section.section--stone` after the content grid: kicker “More” / “Más”, heading “Related” / “Relacionado”, `.related` cards. The entire bar was removed from this page only.

### English

**Kicker:** More

**Heading:** Related

**Project Management** — /project-management/
Cost, scope, and timeline control.

**Land Development** — /specialties/land-development/
Site work before the building.

**Inspections** — /industries/inspections/
Inspection-ready sequencing in the field.

### Spanish

**Kicker:** Más

**Heading:** Relacionado

**Gerencia de proyectos** — /es/gerencia-de-proyectos/
Control de costo, alcance y plazo.

**Desarrollo de terrenos** — /es/especialidades/desarrollo-de-terrenos/
Obra de sitio antes del edificio.

**Inspecciones** — /es/industrias/inspecciones/
Secuencia de campo lista para inspección.
