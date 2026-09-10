# 08_LONGBOARD · de — correcciones pendientes

URL: https://rentalscooterbarcelona.com/de/longboard/

HTML original sin modificar. SHA-256: `4165e42de3aad195b652889d60807dd8e4e8dbb915d83970ab619eef7b465958`. Las líneas se refieren a este index.html.

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/longboard/#webpage.dateModified

**Actual:** ["2026-07-30", "2026-08-24"]

**Corrección propuesta:** Un valor real de última modificación; pendiente de fuente.

**Motivo:** Dos bloques JSON-LD describen una única página con fechas de última modificación distintas.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una fecha existente: 1 sustitución o eliminación por HTML (90). Depende de la consolidación elegida.

Línea 138 del HTML original:

```html
"2026-07-30"
```

Línea 512 del HTML original:

```html
"2026-08-24"
```

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de información práctica

**Actual:** Longboard-Verleih-Guide für Barcelona&lt;/a&gt;.&lt;/p&gt;

**Corrección propuesta:** Longboard-Verleih-Guide für Barcelona&lt;/a&gt; lesen.&lt;/p&gt;

**Motivo:** La frase que remite a la guía termina tras el objeto del verbo modal; falta el infinitivo leer (lesen/lezen).

**Impacto:** Error gramatical visible. El enlace y su destino localizado son correctos.

**Estado:** CORRECCIÓN DEFINIDA. 1 sustitución en DE y 1 en NL; total 2.

Línea 796 del HTML original:

```html
Longboard-Verleih-Guide für Barcelona</a>.</p>
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
