# 12_BLOG_BEGINNER_INLINE_SKATING — plan por idioma y prioridad

10 HTML originales. Correcciones propuestas; ninguna aplicada.

| Idioma | HTML | Puntos pendientes |
| --- | --- | --- |
| ca | [ca/index.html](cat/index.html) | U01, U03, U04 |
| de | [de/index.html](de/index.html) | U01, U03, U04 |
| en | [en/index.html](en/index.html) | U01, U03, U04 |
| es | [es/index.html](es/index.html) | U01, U03, U04 |
| fr | [fr/index.html](fr/index.html) | U01, U03, U04 |
| it | [it/index.html](it/index.html) | U01, U03 |
| nl | [nl/index.html](nl/index.html) | U01, U03 |
| pl | [pl/index.html](pl/index.html) | U01, U02, U03, U04 |
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

**Elemento:** https://rentalscooterbarcelona.com/cat/blog/patinar-linia-barcelona-principiants/#webpage.dateModified

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

**Actual:** {"visible": "Actualitzat el 16 de juny de 2026", "iso_visible": "2026-06-16", "schema": ["2026-06-29"]}

**Corrección propuesta:** Publicat el 16 de juny de 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 593 del HTML original:

```html
Actualitzat el 16 de juny de 2026
```

Línea 397 del HTML original:

```html
"2026-06-29"
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

**Elemento:** https://rentalscooterbarcelona.com/de/blog/inlineskaten-barcelona-anfaenger/#webpage.dateModified

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

**Actual:** {"visible": "Aktualisiert am 16. Juni 2026", "iso_visible": "2026-06-16", "schema": ["2026-06-29"]}

**Corrección propuesta:** Veröffentlicht am 16. Juni 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 593 del HTML original:

```html
Aktualisiert am 16. Juni 2026
```

Línea 397 del HTML original:

```html
"2026-06-29"
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

**Elemento:** https://rentalscooterbarcelona.com/blog/beginner-inline-skating-barcelona/#webpage.dateModified

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

Línea 118 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 269 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/es/blog/patinar-en-barcelona-principiantes/#webpage.dateModified

**Actual:** ["2026-06-29", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 372 del HTML original:

```html
"2026-06-29"
```

Línea 475 del HTML original:

```html
"2026-08-24"
```

### U04 · Prioridad 2 · MEDIO

Fecha visible de publicación rotulada como actualización

**Elemento:** Fecha visible de actualización ↔ BlogPosting.dateModified

**Actual:** {"visible": "Actualizado el 18 de mayo de 2026", "iso_visible": "2026-05-18", "schema": ["2026-06-29"]}

**Corrección propuesta:** Publicado el 18 de mayo de 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 586 del HTML original:

```html
Actualizado el 18 de mayo de 2026
```

Línea 386 del HTML original:

```html
"2026-06-29"
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

**Elemento:** https://rentalscooterbarcelona.com/fr/blog/roller-en-ligne-debutants-barcelone/#webpage.dateModified

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

**Actual:** {"visible": "Mis à jour le 16 juin 2026", "iso_visible": "2026-06-16", "schema": ["2026-06-29"]}

**Corrección propuesta:** Publié le 16 juin 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 593 del HTML original:

```html
Mis à jour le 16 juin 2026
```

Línea 397 del HTML original:

```html
"2026-06-29"
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

**Elemento:** https://rentalscooterbarcelona.com/it/blog/pattinaggio-inline-principianti-barcellona/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 378 del HTML original:

```html
"2026-07-27"
```

Línea 482 del HTML original:

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

**Elemento:** https://rentalscooterbarcelona.com/nl/blog/inline-skaten-barcelona-beginners/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 378 del HTML original:

```html
"2026-07-27"
```

Línea 482 del HTML original:

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

Línea 121 del HTML original:

```html
coordinate=41.390577%2C2.198362
```

Línea 312 del HTML original:

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

Línea 111 del HTML original:

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

Línea 179 del HTML original:

```html
"https://rentalscooterbarcelona.com/pl/"
```

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pl/blog/jazda-na-rolkach-barcelona-poczatkujacy/#webpage.dateModified

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

**Actual:** {"visible": "Zaktualizowano 16 czerwca 2026", "iso_visible": "2026-06-16", "schema": ["2026-06-29"]}

**Corrección propuesta:** Opublikowano 16 czerwca 2026

**Motivo:** El texto visible está rotulado como actualizado, no como publicado, y difiere de dateModified del artículo. A menudo reproduce datePublished.

**Impacto:** El lector y los consumidores de Schema reciben fechas de actualización distintas para el artículo.

**Estado:** PROPUESTA DE ETIQUETA DEFINIDA. 1 sustitución de la etiqueta visible por HTML; conservar la fecha y todos los JSON-LD. 32 en total.

Línea 593 del HTML original:

```html
Zaktualizowano 16 czerwca 2026
```

Línea 397 del HTML original:

```html
"2026-06-29"
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

**Elemento:** https://rentalscooterbarcelona.com/pt/blog/patinagem-inline-barcelona-iniciantes/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 378 del HTML original:

```html
"2026-07-27"
```

Línea 482 del HTML original:

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

**Elemento:** https://rentalscooterbarcelona.com/sv/blog/inline-skating-barcelona-nyborjare/#webpage.dateModified

**Actual:** ["2026-07-27", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 378 del HTML original:

```html
"2026-07-27"
```

Línea 482 del HTML original:

```html
"2026-08-24"
```

