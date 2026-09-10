# 06_QUADS · de — correcciones pendientes

URL: https://rentalscooterbarcelona.com/de/quads/

HTML original sin modificar. SHA-256: `34328ba3a6d728b9c6a68695a05a02eb3e4189f9a4d8842c227592d1171401e4`. Las líneas se refieren a este index.html.

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 152 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 526 del HTML original:

```html
"dateModified": "2026-08-24"
```

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de enlace a la guía

**Actual:** Geöffnet von 10:30–13:30 und 16:30–20:00 Uhr. Wir bieten stunden- und tageweise Vermietung. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren Guide zum Rollschuhe mieten in Barcelona.

**Corrección propuesta:** Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren &lt;a href="https://rentalscooterbarcelona.com/de/blog/roller-skates/"&gt;Guide zum Rollschuhe mieten in Barcelona&lt;/a&gt; lesen.&lt;/p&gt;

**Motivo:** La construcción modal queda sin infinitivo final.

**Impacto:** Frase incompleta en alemán/neerlandés.

**Estado:** CORRECCIÓN DEFINIDA. Una inserción de lesen al final del enlace; conservar URL.

Línea 809 del HTML original:

```html
Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren <a href="https://rentalscooterbarcelona.com/de/blog/roller-skates/">Guide zum Rollschuhe mieten in Barcelona</a>.</p>
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
