# Auditoría técnica SEO/GEO — Página "Fietsverhuur" (NL) — `/nl/bike/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Landing de alquiler de bicicletas en neerlandés. Es la página **más limpia de contenido** de todo el lote: no encontré errores de traducción, `srcset` roto, ni discrepancias de precio entre el schema y las tarjetas visibles. Estructuralmente es idéntica al resto de páginas de servicio (scooter FR, skateboard PT, rollerblades DE): jerarquía de encabezados correcta, 6 `Offer` con precio, breadcrumb real, footer de contacto correcto.

Su único aporte a esta auditoría es servir de **cuarta confirmación** del bug sitewide de la clase `home-page`, y de paso confirma que ese bug **no depende del idioma ni del volumen de contenido** — aparece igual en una página bien ejecutada que en una con errores de traducción.

---

## 2. Confirmación (4ª vez) del bug sitewide `home-page`

```html
<body class="home-page service-page bike-service-page">
```

Mismo patrón exacto que en skateboard (PT), con el mismo origen probable: el `<h1>` usa `class="home-hero-title"` (línea 683), heredando el hero visual de la home. Ya son cuatro plantillas distintas confirmadas con este problema (contacto, blog, skateboard, bici) — a estas alturas doy por hecho que **está presente en todas las páginas de servicio del sitio** (scooter, rollerblades, quads, skateboard, longboard, bike) más las de contacto y blog. Solo la home real y, aparentemente, la página de precios (que usa su propia plantilla `Prices/prices.css`) podrían no tener este problema — valdría la pena que el equipo de desarrollo haga una búsqueda global de `home-page` en las plantillas y decida en qué páginas debe quedarse y en cuáles no.

No repito aquí el detalle de la causa raíz ni la recomendación de arreglo — son las mismas que ya describí en el informe de la página de skateboard.

---

## 3. Resto de comprobaciones — todo en línea, sin sorpresas

- Jerarquía de encabezados limpia (H1 único, H2 por sección, H3 consistente en las 6 tarjetas de precio y en las 8 preguntas de FAQ).
- 6 `Offer` con precio en el JSON-LD, coincidiendo con las tarjetas visibles (1h/4h/día completo/24h/2 días/día extra).
- `srcset` de todas las imágenes correctamente formado, sin entradas duplicadas ni tamaños repetidos (a diferencia de la página de skateboard).
- Contenido en neerlandés gramaticalmente correcto y completo — sin frases a medias ni palabras sin traducir.
- 4 hojas de estilo render-blocking (mismo patrón que skateboard PT), sin `max-snippet:-1` en robots, sin skip link, JSON-LD en dos scripts — los mismos pendientes sistémicos de siempre.

---

## 4. Conclusión de esta ronda

Con 8 páginas ya auditadas, el panorama está bastante completo. Te propongo, si quieres, que en el próximo paso en lugar de seguir auditando página por página, preparemos **un documento único de "plan de corrección"** que agrupe todos los hallazgos por tipo de arreglo (plantilla compartida vs. específico de cada página) para que el equipo de desarrollo pueda priorizar el trabajo de una sola vez en vez de ir plantilla a plantilla.
