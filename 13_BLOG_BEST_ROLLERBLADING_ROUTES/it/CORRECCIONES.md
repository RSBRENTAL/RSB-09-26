# 13_BLOG_BEST_ROLLERBLADING_ROUTES · it — correcciones pendientes

URL: https://rentalscooterbarcelona.com/it/blog/best-rollerblading-routes-barcelona/

HTML original sin modificar. SHA-256: `3a77a2518fb26911a99ba08a92023408e4a0307d3cd236dbb21749e50f75b685`. Las líneas se refieren a este index.html.

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 99 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 290 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
