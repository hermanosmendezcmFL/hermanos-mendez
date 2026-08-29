# Industries landing copy removed 28 August 2026

Ryan’s Industries overview brief asked that everything below come off the Industries landing page (`/industries/` and `/es/industrias/`). It is banked here verbatim (English and Spanish) so it can be reused on other pages.

Source of truth at removal: `tools/pages.json` (page `en_path` `/industries/`). The same strings were rendered by `tools/build.py` (`interior_body()`). Global nav/footer generators in `tools/chrome.py` were not stripped; the Industries dropdown and footer Industries list stay as they were.

The Industries landing after this change is: header, banner (new H1 + lead), new body, Our Markets sidebar (five market links), contact CTA, footer. The lower Related / More card bar stays gone (already stripped globally). Destination pages for Land Clearing, Stormwater Mitigation, Permitting, Inspections, Design-Build, and the old `/industries/residential/` hub were not deleted — they are simply no longer listed on this landing.

---

## 1. H1

**Where it lived:** Industries landing `.page-banner h1` on `/industries/` and `/es/industrias/`.

### English

Industries and markets we serve

### Spanish

Industrias y mercados que atendemos

---

## 2. Lead

**Where it lived:** Industries landing `.page-banner p.lead` on `/industries/` and `/es/industrias/`.

### English

Markets we advise and manage in Tampa Bay.

### Spanish

Mercados que asesoramos y gerenciamos en Tampa Bay.

---

## 3. Title and meta description

**Where it lived:** `<title>` and `meta name="description"` on `/industries/` and `/es/industrias/`.

### English

**Title:** Industries | Commercial, Multi-Family, SFR, Design-Build | HMCM

**Description:** Industries and markets HMCM serves in Tampa Bay: commercial, multi-family, SFR, custom build, land clearing, stormwater mitigation, permitting, inspections, and design-build.

### Spanish

**Title:** Industrias | Comercial, multifamiliar, SFR, diseño-construcción | HMCM

**Description:** Industrias y mercados que HMCM atiende en Tampa Bay: comercial, multifamiliar, SFR, construcción a medida, despeje, aguas pluviales, permisos, inspecciones y diseño-construcción.

---

## 4. Body paragraphs

**Where it lived:** Industries landing `.prose` in the first content section on `/industries/` and `/es/industrias/`.

### English

Industries describe who the owner is and what kind of asset is on the ground.

We work these markets as a consultant, construction manager, or project manager.

### Spanish

Las industrias describen quién es el propietario y qué tipo de bien hay en el terreno.

Trabajamos estos mercados como consultor, gerente de construcción o gerente de proyectos.

---

## 5. Sidebar heading and links removed from this page

**Where it lived:** Industries landing `aside.aside-box` (heading was “Related” / “Relacionado”).

The heading word itself was replaced by Our Markets / Nuestros mercados. These **links** were removed from this sidebar (destination pages were not deleted):

### English

**Heading:** Related

- Land Clearing — /industries/land-clearing/
- Stormwater Mitigation — /industries/stormwater-mitigation/
- Permitting — /industries/permitting/
- Inspections — /industries/inspections/
- Design-Build — /industries/design-build/
- Contact — /contact/

No Overview leftover was present on this sidebar at removal.

Kept (still listed, now under Our Markets) and not banked as removed: Commercial, Multi-Family, SFR (Single-Family Residential), Custom Build.

Added on this sidebar (was not listed here before): Residential — /consulting/residential/ (same URL as the header Industries dropdown).

### Spanish

**Heading:** Relacionado

- Despeje de terrenos — /es/industrias/despeje-de-terrenos/
- Mitigación de aguas pluviales — /es/industrias/mitigacion-de-aguas-pluviales/
- Permisos — /es/industrias/permisos/
- Inspecciones — /es/industrias/inspecciones/
- Diseño-construcción — /es/industrias/diseno-construccion/
- Contacto — /es/contacto/

No Resumen leftover was present on this sidebar at removal.

Kept (not banked as removed): Comercial, Multifamiliar, Residencial unifamiliar (SFR), Construcción a medida.

Added: Residencial — /es/consultoria/residencial/.

---

## 6. Lower Related / More card bar leftover (pages.json `related[]`)

**Where it lived:** Industries landing `en.related` / `es.related` in `tools/pages.json`. The HTML card bar (kicker “More” / “Más”, heading “Related” / “Relacionado”, `.related` cards in `.section.section--stone`) was already stripped globally by `interior_body()` and was not rendered on this page at removal. The leftover card data is banked here so it is not lost.

### English (`en.related`)

**Commercial** — /industries/commercial/
Consultoría y gerencia de construcción comercial en Tampa Bay

**Multi-Family** — /industries/multi-family/
Consultoría y gerencia en construcción multifamiliar

**SFR (Single-Family Residential)** — /industries/sfr/
Consultoría y gerencia en residencial unifamiliar (SFR)

### Spanish (`es.related`)

**Comercial** — /es/industrias/comercial/
Commercial buildings, sites, and owner-side delivery — advised and managed, not listed as a portfolio of named jobs.

**Multifamiliar** — /es/industrias/multifamiliar/
Residential buildings with more than one dwelling — planned and coordinated as construction, not as a real-estate brochure.

**Residencial unifamiliar (SFR)** — /es/industrias/sfr/
Houses — new, added-onto, or renovated — with permitting, inspections, and site work in the same conversation.
