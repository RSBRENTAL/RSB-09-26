# 14_BLOG_BIKE · es — correcciones pendientes

URL: https://rentalscooterbarcelona.com/es/blog/bike/

HTML original sin modificar. SHA-256: `606a5b4fc5269d639445a4dcd9fb0c7dfdead4e4977a4ce4b04ddf4c44b66bd3`. Las líneas se refieren a este index.html.

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 107 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 258 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/es/blog/bike/#webpage.dateModified

**Actual:** ["2026-06-29", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 361 del HTML original:

```html
"2026-06-29"
```

Línea 468 del HTML original:

```html
"2026-08-24"
```

### U04 · Prioridad 2 · MEDIO

Fecha visible de publicación rotulada como actualización

**Elemento:** Fecha visible de actualización ↔ BlogPosting.dateModified

**Actual:** {"visible": "Actualizado el 12 de abril de 2026", "iso_visible": "2026-04-12", "schema": ["2026-06-29"]}

**Corrección propuesta:** Publicado el 12 de abril de 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 579 del HTML original:

```html
Actualizado el 12 de abril de 2026
```

Línea 380 del HTML original:

```html
"2026-06-29"
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
