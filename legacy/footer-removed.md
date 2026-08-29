# Footer link lists banked 28 August 2026

Ryan marked a footer screenshot (red strikeouts + arrows). The previous global footer link lists from `tools/chrome.py` `footer()` are banked here before the slim. Header/nav, homepage body, inner-page sidebars, and footer CSS were not part of this change.

Source of truth at banking: `tools/chrome.py` `footer()` (English and Spanish via `T`). Rendered on every page through `wrap_page()`.

Logo/contact column, Maps link, and © 2026 HMCM bar were kept and are not listed below.

---

## 1. CONSULTING column (heading kept)

Removed from the footer (not deleted as pages): Other Consulting Services / `other_group` (`/consulting/other/` · `/es/consultoria/otros/`) and every nested item. Specialized Consulting Services lived in the header dropdown, not this footer column; nested specialized items were already absent from the footer.

Commercial and Residential labels were renamed in the footer only (Commercial Services / Residential Services). Overview stayed.

### English (as rendered)

- Overview → `/consulting/`
- Commercial → `/consulting/commercial/`
- Residential → `/consulting/residential/`
- Other Consulting Services → `/consulting/other/`
- Efficiency Evaluations and Implementations → `/consulting/other/efficiency-evaluations/`
- Systems Evaluations and Implementations → `/consulting/other/systems-evaluations/`
- Business Development → `/consulting/other/business-development/`
- Special Projects → `/consulting/other/special-projects/`
- Takeoff Support and Contract Negotiations → `/consulting/other/takeoff-support/`
- Purchasing Assistance → `/consulting/other/purchasing-assistance/`
- SOP and Employee Management → `/consulting/other/sop-employee-management/`

### Spanish (as rendered)

- Resumen → `/es/consultoria/`
- Comercial → `/es/consultoria/comercial/`
- Residencial → `/es/consultoria/residencial/`
- Otros servicios de consultoría → `/es/consultoria/otros/`
- Evaluaciones e implementaciones de eficiencia → `/es/consultoria/otros/evaluaciones-de-eficiencia/`
- Evaluaciones e implementaciones de sistemas → `/es/consultoria/otros/evaluaciones-de-sistemas/`
- Desarrollo de negocios → `/es/consultoria/otros/desarrollo-de-negocios/`
- Proyectos especiales → `/es/consultoria/otros/proyectos-especiales/`
- Soporte de takeoff y negociación de contratos → `/es/consultoria/otros/soporte-de-estimacion/`
- Asistencia en compras → `/es/consultoria/otros/asistencia-en-compras/`
- SOP y gestión de empleados → `/es/consultoria/otros/sop-gestion-de-empleados/`

---

## 2. Construction Management / Project Management + Specialties (second heading)

Heading was `Construction Management / Project Management` (ES: `Gerencia de construcción / Gerencia de proyectos`), then a nested `Specialties` / `Especialidades` h2. The nested heading is gone; those items move under a single **Services** / **Servicios** column, with CM and PM at the top.

### English (as rendered)

**Construction Management / Project Management**

- Construction Management → `/construction-management/`
- Project Management → `/project-management/`

**Specialties**

- Overview → `/specialties/`
- Land Development → `/specialties/land-development/`
- New Construction → `/specialties/new-construction/`
- Renovation → `/specialties/renovation/`
- Demolition → `/specialties/demolition/`

### Spanish (as rendered)

**Gerencia de construcción / Gerencia de proyectos**

- Gerencia de construcción → `/es/gerencia-de-construccion/`
- Gerencia de proyectos → `/es/gerencia-de-proyectos/`

**Especialidades**

- Resumen → `/es/especialidades/`
- Desarrollo de terrenos → `/es/especialidades/desarrollo-de-terrenos/`
- Nueva construcción → `/es/especialidades/nueva-construccion/`
- Renovación → `/es/especialidades/renovacion/`
- Demolición → `/es/especialidades/demolicion/`

---

## 3. INDUSTRIES column (heading kept)

Dropped from the footer (pages remain): Overview, Land Clearing, Stormwater Mitigation, Permitting, Inspections, Design-Build. Kept Commercial, Multi-Family, SFR (Single-Family Residential), Custom Build. Residential was added as a new industry page.

### English (as rendered)

- Overview → `/industries/`
- Commercial → `/industries/commercial/`
- Multi-Family → `/industries/multi-family/`
- SFR (Single-Family Residential) → `/industries/sfr/`
- Custom Build → `/industries/custom-build/`
- Land Clearing → `/industries/land-clearing/`
- Stormwater Mitigation → `/industries/stormwater-mitigation/`
- Permitting → `/industries/permitting/`
- Inspections → `/industries/inspections/`
- Design-Build → `/industries/design-build/`

### Spanish (as rendered)

- Resumen → `/es/industrias/`
- Comercial → `/es/industrias/comercial/`
- Multifamiliar → `/es/industrias/multifamiliar/`
- Residencial unifamiliar (SFR) → `/es/industrias/sfr/`
- Construcción a medida → `/es/industrias/construccion-a-medida/`
- Despeje de terrenos → `/es/industrias/despeje-de-terrenos/`
- Mitigación de aguas pluviales → `/es/industrias/mitigacion-de-aguas-pluviales/`
- Permisos → `/es/industrias/permisos/`
- Inspecciones → `/es/industrias/inspecciones/`
- Diseño-construcción → `/es/industrias/diseno-construccion/`

---

## 4. COMPANY column (unchanged)

### English

- Home → `/`
- About → `/about/`
- Contact → `/contact/`
- Español → `/es/`

### Spanish

- Inicio → `/es/`
- Empresa → `/es/empresa/`
- Contacto → `/es/contacto/`
- English → `/`

