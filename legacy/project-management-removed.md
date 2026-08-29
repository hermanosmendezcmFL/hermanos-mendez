# Project Management landing copy removed 28 August 2026

Ryan’s Project Management brief asked that everything below come off the Project Management landing page (`/project-management/` and `/es/gerencia-de-proyectos/`). It is banked here verbatim (English and Spanish) so it can be reused on other pages.

Source of truth at removal: `tools/pages.json` (page `en_path` `/project-management/`). The same strings were rendered by `tools/build.py` (`interior_body()`). Global nav/footer generators in `tools/chrome.py` were not stripped; the Services dropdown stays Overview / Construction Management / Project Management, and footer chrome is unchanged.

The Project Management landing after this change is: header, banner (new H1 + lead), new body, Service Pathways sidebar (three dedicated pages), contact CTA, footer. The lower Related / More card bar is gone.

---

## 1. H1

**Where it lived:** Project Management landing `.page-banner h1` on `/project-management/` and `/es/gerencia-de-proyectos/`.

### English

Project management from preconstruction through closeout

### Spanish

Gerencia de proyectos desde la preconstrucción hasta el cierre

---

## 2. Lead

**Where it lived:** Project Management landing `.page-banner p.lead` on `/project-management/` and `/es/gerencia-de-proyectos/`.

### English

Oversight of scope, cost, and timeline: a single point of contact for the decisions that keep a job on the rails.

### Spanish

Control de alcance, costo y plazo: un solo punto de contacto para las decisiones que mantienen la obra en rieles.

---

## 3. Body paragraphs

**Where it lived:** Project Management landing `.prose` in the first content section on `/project-management/` and `/es/gerencia-de-proyectos/`.

### English

Project management is how HMCM is hired when an owner needs someone to hold the job together from the first budget through closeout: what is in scope, what it should cost, and when it has to be done.

Preconstruction is part of the work. Drawings, quantities, purchasing, and permits are aligned so the field is not asked to invent the job.

During construction, project management stays tied to the site so schedule and cost are the same conversation as the work.

### Spanish

La gerencia de proyectos es cómo se contrata a HMCM cuando el propietario necesita a alguien que sostenga la obra desde el primer presupuesto hasta el cierre: qué entra en el alcance, cuánto debería costar y cuándo tiene que estar lista.

La preconstrucción es parte del trabajo. Se alinean planos, cantidades, compras y permisos para que el campo no tenga que inventar la obra.

Durante la construcción, la gerencia de proyectos se mantiene unida al sitio para que plazo y costo sean la misma conversación que el trabajo.

---

## 4. Sidebar heading and links removed from this page

**Where it lived:** Project Management landing `aside.aside-box` (heading was “Related” / “Relacionado”).

The heading word itself was replaced by Service Pathways / Rutas de servicio. These **links** were removed from this sidebar (destination pages were not deleted):

### English

**Heading:** Related

- Construction Management — /construction-management/
- Consulting — /consulting/
- Contact — /contact/

Kept (re-homed to Construction Management or Consulting branch URLs) and not banked as removed: Design-Build, Permitting, Takeoff Support and Contract Negotiations.

### Spanish

**Heading:** Relacionado

- Gerencia de construcción — /es/gerencia-de-construccion/
- Consultoría — /es/consultoria/
- Contacto — /es/contacto/

Kept (not banked as removed): Diseño-construcción, Permisos, Takeoff y negociación de contratos.

---

## 5. Lower Related / More card bar (entire block)

**Where it lived:** Project Management landing section `.section.section--stone` after the content grid: kicker “More” / “Más”, heading “Related” / “Relacionado”, `.related` cards. The entire bar was removed from this page only.

### English

**Kicker:** More

**Heading:** Related

**Construction Management** — /construction-management/
Field coordination of the same job.

**Permitting** — /industries/permitting/
Agency sequence as part of the timeline.

**Special Projects** — /consulting/other/special-projects/
When the job does not fit a standard box.

### Spanish

**Kicker:** Más

**Heading:** Relacionado

**Gerencia de construcción** — /es/gerencia-de-construccion/
Coordinación de campo de la misma obra.

**Permisos** — /es/industrias/permisos/
La secuencia con las agencias como parte del plazo.

**Proyectos especiales** — /es/consultoria/otros/proyectos-especiales/
Cuando la obra no cabe en una caja estándar.
