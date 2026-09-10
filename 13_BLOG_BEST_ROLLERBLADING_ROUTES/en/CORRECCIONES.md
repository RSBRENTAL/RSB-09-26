# 13_BLOG_BEST_ROLLERBLADING_ROUTES · en — correcciones pendientes

URL: https://rentalscooterbarcelona.com/blog/best-rollerblading-routes-barcelona/

HTML original sin modificar. SHA-256: `faced90774d505d18e73f0a9fd000f115443a85ecef5070de0d2066d6ace8200`. Las líneas se refieren a este index.html.

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

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
