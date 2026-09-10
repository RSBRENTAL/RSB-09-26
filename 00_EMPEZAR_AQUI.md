# Auditoría unificada — 200 HTML, 20 páginas, 10 idiomas

Paquete completo actualizado el 2026-09-09. Se conservan los 160 HTML anteriores y se añaden BIKE, QUADS, SKATEBOARD y LOCATION_CONTACT en sus 10 idiomas. Se excluye el verificador Yandex de BIKE. No falta ningún grupo numerado del 01 al 20 en el conjunto recibido. Esto no inventaría otras páginas ajenas a los archivos aportados.

Los HTML están sin modificar. 154 HTML tienen algún error demostrado; 46 no presentan errores obligatorios demostrados en estas auditorías. 288 casos de corrección, que pueden solaparse en un mismo HTML.

| Prioridad | Punto | Corrección | Casos | HTML afectados | Estado |
| --- | --- | --- | --- | --- | --- |
| 1 | U01 | Coordenadas antiguas en Apple Maps | 100 | 100 | CORRECCIÓN DEFINIDA |
| 1 | U02 | URLs de Organization y WebSite localizadas | 18 | 9 | CORRECCIÓN DEFINIDA |
| 2 | U03 | Dos dateModified para la misma WebPage | 130 | 130 | FECHA REAL PENDIENTE |
| 2 | U04 | Fecha visible de publicación rotulada como actualización | 32 | 32 | PROPUESTA DE ETIQUETA DEFINIDA |
| 3 | U05 | Falta el infinitivo en el enlace a la guía, DE/NL | 6 | 6 | CORRECCIÓN DEFINIDA |
| 3 | U06 | Partícula sobrante en HOME DE | 1 | 1 | CORRECCIÓN DEFINIDA |
| 3 | U07 | Repetición de inlines en ROLLERBLADES SV | 1 | 1 | CORRECCIÓN DEFINIDA |

## Cómo revisarlo

1. Leer 02_PLAN_COMPLETO_POR_PRIORIDAD.md.
2. Abrir PAGINAS y elegir HOME, PRICES o el grupo correspondiente.
3. Consultar 00_CORRECCIONES_POR_PRIORIDAD.md y cada idioma/CORRECCIONES.md junto al HTML original.
4. Consultar 01_DATOS_CANONICOS_Y_DECISIONES.md para distinguir datos ya fijados de fechas pendientes.

Las auditorías anteriores se conservan completas en AUDITORIAS_ORIGINALES/40_HTML y 120_HTML; la nueva auditoría A–W está en ULTIMOS_40_HTML. Las cifras 40/120/160 de documentos históricos describen sus lotes originales; el inventario vigente es MATRICES/inventario_200.csv.

Imágenes, tamaños, recortes y revisión visual quedan para la siguiente fase.

| Página | Idiomas | Errores pendientes |
| --- | --- | --- |
| 01_HOME | 10 | U06 |
| 02_PRICES | 10 | Ninguno demostrado |
| 03_SCOOTER | 10 | U03 |
| 04_BIKE | 10 | U03 |
| 05_ROLLERBLADES | 10 | U05, U07 |
| 06_QUADS | 10 | U03, U05 |
| 07_SKATEBOARD | 10 | U03, U05 |
| 08_LONGBOARD | 10 | U03, U05 |
| 09_LOCATION_CONTACT | 10 | Ninguno demostrado |
| 10_BLOG_HOME | 10 | U01, U02 |
| 11_BLOG_50CC_VS_125CC | 10 | Ninguno demostrado |
| 12_BLOG_BEGINNER_INLINE_SKATING | 10 | U01, U02, U03, U04 |
| 13_BLOG_BEST_ROLLERBLADING_ROUTES | 10 | U01, U02 |
| 14_BLOG_BIKE | 10 | U01, U02, U03, U04 |
| 15_BLOG_HOURLY_INLINE_SKATE_RENTAL | 10 | U01, U03, U04 |
| 16_BLOG_INLINE_SKATES | 10 | U01, U02, U03 |
| 17_BLOG_LONGBOARD | 10 | U01, U02, U03, U04 |
| 18_BLOG_ROLLER_SKATES | 10 | U01, U02, U03, U04 |
| 19_BLOG_SCOOTER | 10 | U01, U02, U03 |
| 20_BLOG_SKATEBOARD | 10 | U01, U02, U03, U04 |

