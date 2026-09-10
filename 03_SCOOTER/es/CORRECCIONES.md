# 03_SCOOTER · es — correcciones pendientes

URL: https://rentalscooterbarcelona.com/es/scooter/

HTML original sin modificar. SHA-256: `f65eb76170abc6e02ae2fdec0a8e648c9e740ce6bf447f4337c51d5416c01ee3`. Las líneas se refieren a este index.html.

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** WebPage https://rentalscooterbarcelona.com/es/scooter/#webpage

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Una sola fecha de última modificación real, pendiente de fuente canónica.

**Motivo:** Los dos bloques JSON-LD aportan valores diferentes a la misma propiedad del mismo @id. No son dos páginas ni dos reseñas: se está describiendo dos veces la última modificación de una única página.

**Impacto:** Ambigüedad sobre la fecha de actualización en el grafo; no invalida el JSON ni demuestra un problema de indexación.

**Estado:** FECHA REAL PENDIENTE. Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada.

Línea 216 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 635 del HTML original:

```html
"dateModified": "2026-08-24"
```

Ver también [mejoras de la página](../MEJORAS.md) y [plan del grupo](../00_CORRECCIONES_POR_PRIORIDAD.md). Imágenes y tamaños: pendientes para la siguiente fase.
