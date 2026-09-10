# 20_BLOG_SKATEBOARD · pl — correcciones pendientes

URL: https://rentalscooterbarcelona.com/pl/blog/skateboard/

HTML original sin modificar. SHA-256: `cfdd36a6a4de4c82b07f8c73c2181f9ab8c1de690a073b1afb8139e76aa619f7`. Las líneas se refieren a este index.html.

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 110 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 301 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U02 · Prioridad 1 · MEDIO

URLs de Organization y WebSite localizadas

**Elemento:** Organization.url

**Actual:** https://rentalscooterbarcelona.com/pl/

**Corrección propuesta:** https://rentalscooterbarcelona.com/

**Motivo:** Las entidades globales conservan sus @id globales, pero su url apunta a /pl/ en lugar de la raíz definida por CANONICAL §§1 y 4.

**Impacto:** Desalineación de la identidad global entre idiomas. No afecta al canonical de la página, que sí es propio.

**Estado:** CORRECCIÓN DEFINIDA. 1 propiedad; 2 por HTML afectado, 18 en total.

Línea 100 del HTML original:

```html
"https://rentalscooterbarcelona.com/pl/"
```

### U02 · Prioridad 1 · MEDIO

URLs de Organization y WebSite localizadas

**Elemento:** WebSite.url

**Actual:** https://rentalscooterbarcelona.com/pl/

**Corrección propuesta:** https://rentalscooterbarcelona.com/

**Motivo:** Las entidades globales conservan sus @id globales, pero su url apunta a /pl/ en lugar de la raíz definida por CANONICAL §§1 y 4.

**Impacto:** Desalineación de la identidad global entre idiomas. No afecta al canonical de la página, que sí es propio.

**Estado:** CORRECCIÓN DEFINIDA. 1 propiedad; 2 por HTML afectado, 18 en total.

Línea 168 del HTML original:

```html
"https://rentalscooterbarcelona.com/pl/"
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pl/blog/skateboard/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 367 del HTML original:

```html
"2026-07-27"
```

Línea 470 del HTML original:

```html
"2026-08-24"
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
