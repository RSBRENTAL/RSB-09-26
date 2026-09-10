# 16_BLOG_INLINE_SKATES · de — correcciones pendientes

URL: https://rentalscooterbarcelona.com/de/blog/inline-skates/

HTML original sin modificar. SHA-256: `f4c8ea55071cd20d06328b81559d592ee95361322cf9a4c5abefe9a8a008a506`. Las líneas se refieren a este index.html.

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 97 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 248 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 351 del HTML original:

```html
"2026-07-27"
```

Línea 464 del HTML original:

```html
"2026-08-24"
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
