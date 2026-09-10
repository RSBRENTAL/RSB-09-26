# 15_BLOG_HOURLY_INLINE_SKATE_RENTAL · en — correcciones pendientes

URL: https://rentalscooterbarcelona.com/blog/hourly-inline-skate-rental-barcelona/

HTML original sin modificar. SHA-256: `08ca06c1702938d97372ba2a4dce0e11bde49094dfed4ae40f7e6f81a9caca34`. Las líneas se refieren a este index.html.

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 121 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 312 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/blog/hourly-inline-skate-rental-barcelona/#webpage.dateModified

**Actual:** ["2026-06-29", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 378 del HTML original:

```html
"2026-06-29"
```

Línea 482 del HTML original:

```html
"2026-08-24"
```

### U04 · Prioridad 2 · MEDIO

Fecha visible de publicación rotulada como actualización

**Elemento:** Fecha visible de actualización ↔ BlogPosting.dateModified

**Actual:** {"visible": "Updated 16 June 2026", "iso_visible": "2026-06-16", "schema": ["2026-06-29"]}

**Corrección propuesta:** Published 16 June 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 593 del HTML original:

```html
Updated 16 June 2026
```

Línea 397 del HTML original:

```html
"2026-06-29"
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
