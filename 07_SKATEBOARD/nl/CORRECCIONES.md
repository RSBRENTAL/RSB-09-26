# 07_SKATEBOARD · nl — correcciones pendientes

URL: https://rentalscooterbarcelona.com/nl/skateboard/

HTML original sin modificar. SHA-256: `6a1f27d342064742811201a9fcd83674195fb56eb694c3e4a7102f53b2d9dabd`. Las líneas se refieren a este index.html.

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 520 del HTML original:

```html
"dateModified": "2026-08-24"
```

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de enlace a la guía

**Actual:** Elke dag geopend: 10:30–13:30 en 16:30–20:00. We bieden verhuur per uur en per dag. Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze gids voor skateboard huren in Barcelona.

**Corrección propuesta:** Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze &lt;a href="https://rentalscooterbarcelona.com/nl/blog/skateboard/"&gt;gids voor skateboard huren in Barcelona&lt;/a&gt; lezen.&lt;/p&gt;

**Motivo:** La construcción modal queda sin infinitivo final.

**Impacto:** Frase incompleta en alemán/neerlandés.

**Estado:** CORRECCIÓN DEFINIDA. Una inserción de lezen al final del enlace; conservar URL.

Línea 804 del HTML original:

```html
Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze <a href="https://rentalscooterbarcelona.com/nl/blog/skateboard/">gids voor skateboard huren in Barcelona</a>.</p>
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
