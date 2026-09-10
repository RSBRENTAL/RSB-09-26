# 08_LONGBOARD · nl — correcciones pendientes

URL: https://rentalscooterbarcelona.com/nl/longboard/

HTML original sin modificar. SHA-256: `4243c3ff9011c1a52e08165abf8222b54c1a41f0394914466b5a01c56fc7c61d`. Las líneas se refieren a este index.html.

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/longboard/#webpage.dateModified

**Actual:** ["2026-07-30", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 151 del HTML original:

```html
"2026-07-30"
```

Línea 521 del HTML original:

```html
"2026-08-24"
```

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de información práctica

**Actual:** gids voor longboardverhuur in Barcelona&lt;/a&gt;.&lt;/p&gt;

**Corrección propuesta:** gids voor longboardverhuur in Barcelona&lt;/a&gt; lezen.&lt;/p&gt;

**Motivo:** La frase que remite a la guía termina tras el objeto del verbo modal; falta el infinitivo leer (lesen/lezen).

**Impacto:** Error gramatical visible. El enlace y su destino localizado son correctos.

**Estado:** CORRECCIÓN DEFINIDA. 1 sustitución en DE y 1 en NL; total 2.

Línea 805 del HTML original:

```html
gids voor longboardverhuur in Barcelona</a>.</p>
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
