# 16_BLOG_INLINE_SKATES — plan por idioma y prioridad

10 HTML originales. Correcciones propuestas; ninguna aplicada.

| Idioma | HTML | Puntos pendientes |
| --- | --- | --- |
| ca | [ca/index.html](cat/index.html) | U01, U03 |
| de | [de/index.html](de/index.html) | U01, U03 |
| en | [en/index.html](en/index.html) | U01, U03 |
| es | [es/index.html](es/index.html) | U01, U03 |
| fr | [fr/index.html](fr/index.html) | U01, U03 |
| it | [it/index.html](it/index.html) | U01, U03 |
| nl | [nl/index.html](nl/index.html) | U01, U03 |
| pl | [pl/index.html](pl/index.html) | U01, U02, U03 |
| pt | [pt/index.html](pt/index.html) | U01, U03 |
| sv | [sv/index.html](sv/index.html) | U01, U03 |

## ca

[Detalle de correcciones](cat/CORRECCIONES.md)

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

Línea 250 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/cat/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 353 del HTML original:

```html
"2026-07-27"
```

Línea 465 del HTML original:

```html
"2026-08-24"
```

## de

[Detalle de correcciones](de/CORRECCIONES.md)

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

## en

[Detalle de correcciones](en/CORRECCIONES.md)

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

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 367 del HTML original:

```html
"2026-07-27"
```

Línea 489 del HTML original:

```html
"2026-08-24"
```

## es

[Detalle de correcciones](es/CORRECCIONES.md)

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

**Elemento:** https://rentalscooterbarcelona.com/es/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 361 del HTML original:

```html
"2026-07-27"
```

Línea 485 del HTML original:

```html
"2026-08-24"
```

## fr

[Detalle de correcciones](fr/CORRECCIONES.md)

### U01 · Prioridad 1 · MEDIO

Coordenadas antiguas en Apple Maps

**Elemento:** Organization.sameAs / LocalBusiness.sameAs

**Actual:** coordinate=41.390577%2C2.198362

**Corrección propuesta:** coordinate=41.3906488%2C2.1984312

**Motivo:** Dos sameAs por HTML usan las coordenadas antiguas prohibidas por CANONICAL §2, aunque geo.position, ICBM y GeoCoordinates ya usan las definitivas.

**Impacto:** Incoherencia GEO entre las referencias de la misma empresa. No se ha comprobado que Apple Maps ubique mal el negocio, pues conserva su Place ID.

**Estado:** CORRECCIÓN DEFINIDA. 2 sustituciones del par codificado por HTML; 200 en total (400 valores numéricos).

Línea 100 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 251 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/fr/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 354 del HTML original:

```html
"2026-07-27"
```

Línea 468 del HTML original:

```html
"2026-08-24"
```

## it

[Detalle de correcciones](it/CORRECCIONES.md)

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

Línea 250 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/it/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 353 del HTML original:

```html
"2026-07-27"
```

Línea 465 del HTML original:

```html
"2026-08-24"
```

## nl

[Detalle de correcciones](nl/CORRECCIONES.md)

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

Línea 261 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 364 del HTML original:

```html
"2026-07-27"
```

Línea 479 del HTML original:

```html
"2026-08-24"
```

## pl

[Detalle de correcciones](pl/CORRECCIONES.md)

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

**Elemento:** https://rentalscooterbarcelona.com/pl/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 367 del HTML original:

```html
"2026-07-27"
```

Línea 489 del HTML original:

```html
"2026-08-24"
```

## pt

[Detalle de correcciones](pt/CORRECCIONES.md)

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

Línea 261 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pt/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 364 del HTML original:

```html
"2026-07-27"
```

Línea 479 del HTML original:

```html
"2026-08-24"
```

## sv

[Detalle de correcciones](sv/CORRECCIONES.md)

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

Línea 261 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/sv/blog/inline-skates/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 364 del HTML original:

```html
"2026-07-27"
```

Línea 479 del HTML original:

```html
"2026-08-24"
```

