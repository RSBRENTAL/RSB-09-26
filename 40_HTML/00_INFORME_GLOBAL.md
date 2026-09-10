# RSB — Auditoría de los 40 HTML

**Auditoría terminada. Ningún HTML modificado.** Se revisaron las 4 páginas en los 10 idiomas, exclusivamente a partir de los adjuntos. No se consultó Internet ni GitHub.

| Página | HTML revisados | Incidencias demostradas | Archivos afectados |
| --- | --- | --- | --- |
| HOME | 10 | P2: un resto de frase en alemán | DE |
| PRICES | 10 | Ninguna demostrada | — |
| SCOOTER | 10 | P1: dos fechas dateModified para la misma WebPage | Los 10 idiomas |
| ROLLERBLADES | 10 | P3: frases incompletas DE/NL; P4: repetición en SV | DE, NL, SV |

**Balance: 1 hallazgo MEDIO y 3 BAJOS, agrupados por causa; 14 HTML afectados. Ningún error CRÍTICO o ALTO demostrado.** Las mejoras de claridad, cobertura Schema y accesibilidad no se suman a las incidencias.

P1 aparece en los dos bloques JSON-LD de cada SCOOTER: `dateModified: 2026-07-30` y `dateModified: 2026-08-24` para el mismo `@id`. Hay que conservar un dato coherente con la fecha real, que CANONICAL no establece. No se ha inventado una fecha de sustitución.

Se verificaron 80 bloques JSON-LD válidos; 351 pares de FAQ visible/Schema coincidentes; 170 reseñas con autor y texto presentes en la tarjeta visible; 450 comparaciones de precios/ofertas sin discrepancia. Canonical, hreflang, identidad, NAP, coordenadas y horarios coinciden en las comprobaciones ejecutadas. La segunda pasada independiente repitió 840 comprobaciones: solo detectó la divergencia de fechas de SCOOTER.

Los cuatro informes por página contienen las secciones A–W exigidas, matrices de los 10 idiomas, evidencias literales con líneas y propuestas exactas. Los CSV permiten filtrar todas las filas; los JSON conservan la extracción y pruebas. Leer primero el informe de la página que quieras corregir.

## Incidencias y correcciones propuestas

### P1 — MEDIO — Dos dateModified distintos para la misma WebPage

Los dos bloques JSON-LD aportan valores diferentes a la misma propiedad del mismo @id. No son dos páginas ni dos reseñas: se está describiendo dos veces la última modificación de una única página.

Impacto: Ambigüedad sobre la fecha de actualización en el grafo; no invalida el JSON ni demuestra un problema de indexación.

CANONICAL: CANONICAL.md §8 no define fechas dateModified; REQUIERE FUENTE CANÓNICA para elegir la fecha real.

Corrección recomendada: Dejar un único dateModified con la fecha comprobada. No elegir automáticamente la fecha más reciente ni la fecha de esta auditoría.

| Archivo completo dentro del ZIP | Idioma | Elemento | Línea(s) | Valor actual / evidencia | Valor recomendado | Modificaciones previstas |
| --- | --- | --- | --- | --- | --- | --- |
| SCOOTER-main (1)(1)/SCOOTER-main/scooter/index.html | EN | WebPage https://rentalscooterbarcelona.com/scooter/#webpage | [219,641] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/es/scooter/index.html | ES | WebPage https://rentalscooterbarcelona.com/es/scooter/#webpage | [216,635] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/fr/scooter/index.html | FR | WebPage https://rentalscooterbarcelona.com/fr/scooter/#webpage | [148,530] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/it/scooter/index.html | IT | WebPage https://rentalscooterbarcelona.com/it/scooter/#webpage | [147,529] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/de/scooter/index.html | DE | WebPage https://rentalscooterbarcelona.com/de/scooter/#webpage | [187,576] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/nl/scooter/index.html | NL | WebPage https://rentalscooterbarcelona.com/nl/scooter/#webpage | [200,585] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/pt/scooter/index.html | PT | WebPage https://rentalscooterbarcelona.com/pt/scooter/#webpage | [161,554] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/cat/scooter/index.html | CA | WebPage https://rentalscooterbarcelona.com/cat/scooter/#webpage | [147,529] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/sv/scooter/index.html | SV | WebPage https://rentalscooterbarcelona.com/sv/scooter/#webpage | [161,546] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |
| SCOOTER-main (1)(1)/SCOOTER-main/pl/scooter/index.html | PL | WebPage https://rentalscooterbarcelona.com/pl/scooter/#webpage | [180,602] | 2026-07-30 / 2026-08-24 | Una sola fecha de última modificación real, pendiente de fuente canónica. | Si se conserva una de las fechas existentes: 1 sustitución o eliminación de propiedad por HTML; 10 en total. Si ninguna es real, el número depende de la consolidación aprobada. |

### P2 — BAJO — Partícula sobrante en la frase alemana de HOME

La frase combina «gehe direkt zu» con un «an» final residual de «sieh … an». Ese segundo «an» no completa el verbo utilizado.

Impacto: Redacción defectuosa; los enlaces siguen apuntando a destinos correctos.

CANONICAL: NO APLICA: error textual comprobado en el HTML.

Corrección recomendada: Sustituir únicamente el fragmento indicado, conservando URL, marcado y resto del contenido.

| Archivo completo dentro del ZIP | Idioma | Elemento | Línea(s) | Valor actual / evidencia | Valor recomendado | Modificaciones previstas |
| --- | --- | --- | --- | --- | --- | --- |
| RSB_01_HOME_CORREGIDO_FINAL_VALIDATOR_FIXED(2)(4)/RSB_01_HOME_CORREGIDO_FINAL_VALIDATOR_FIXED(2)/RSB_01_HOME_CORREGIDO_FINAL_VALIDATOR_FIXED(2)/de/index.html | DE | Contenido visible | [1186] | vor deinem Besuch an.&lt;/p&gt; | vor deinem Besuch.&lt;/p&gt; | 1 |

### P3 — BAJO — Frase sin verbo final en ROLLERBLADES alemán y neerlandés

La frase termina después del enlace y deja incompletos «kannst du unseren …» y «kun je onze …». Faltan, respectivamente, los infinitivos «lesen» y «lezen».

Impacto: Instrucción editorial incompleta. El href del artículo sí corresponde a su idioma.

CANONICAL: NO APLICA: error textual comprobado en el HTML.

Corrección recomendada: Sustituir únicamente el fragmento indicado, conservando URL, marcado y resto del contenido.

| Archivo completo dentro del ZIP | Idioma | Elemento | Línea(s) | Valor actual / evidencia | Valor recomendado | Modificaciones previstas |
| --- | --- | --- | --- | --- | --- | --- |
| RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)(4)/RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)/de/rollerblades/index.html | DE | Contenido visible | [894] | Guide zum Inlineskates-Verleih in Barcelona&lt;/a&gt;.&lt;/p&gt; | Guide zum Inlineskates-Verleih in Barcelona&lt;/a&gt; lesen.&lt;/p&gt; | 1 |
| RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)(4)/RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)/nl/rollerblades/index.html | NL | Contenido visible | [906] | gids voor inline skates huren in Barcelona&lt;/a&gt;.&lt;/p&gt; | gids voor inline skates huren in Barcelona&lt;/a&gt; lezen.&lt;/p&gt; | 1 |

### P4 — BAJO — Repetición literal en la introducción sueca de ROLLERBLADES

La pregunta presenta «inlines eller inlines»: el mismo término a ambos lados de «o».

Impacto: Repetición editorial verificable; no cambia los precios ni el servicio.

CANONICAL: NO APLICA: error textual comprobado en el HTML.

Corrección recomendada: Sustituir únicamente el fragmento indicado, conservando URL, marcado y resto del contenido.

| Archivo completo dentro del ZIP | Idioma | Elemento | Línea(s) | Valor actual / evidencia | Valor recomendado | Modificaciones previstas |
| --- | --- | --- | --- | --- | --- | --- |
| RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)(4)/RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)/sv/rollerblades/index.html | SV | Contenido visible | [782] | Letar du efter att hyra inlines eller inlines i Barcelona? | Letar du efter att hyra inlines i Barcelona? | 1 |

## Mejoras no obligatorias

Aclarar el depósito condicional; repetir la condición de 3 días junto a las menciones abreviadas de entrega gratuita; delimitar el AggregateOffer de scooter cuando incluye una prolongación; asociar paneles FAQ en PRICES; identificar el idioma activo; precisar un encabezado sueco. Son recomendaciones separadas de P1–P4. No se ha aplicado ningún cambio.

## Alcance y límites

NO VERIFICABLE CON ESTE DIRECTORIO: existencia, contenido y dimensiones intrínsecas de imágenes; contenido/ejecución de CSS y JS externos; comportamiento real de menús y acordeones; contraste visual, foco y experiencia con lector de pantalla; HTTP, redirecciones, cabeceras, robots.txt, sitemap, indexación efectiva, PageSpeed y resultados enriquecidos. La presencia de una URL no prueba su disponibilidad. Tampoco se verificaron la autenticidad de las reseñas, la correspondencia externa del Google Place ID del iframe, las distancias a playas, el stock ni la validez legal real de permisos.

Los enlaces hacia BIKE, QUADS, SKATEBOARD, LONGBOARD, CONTACT y BLOG son referencias externas al alcance: se comprueba su construcción e idioma, pero no que esas páginas existan. CANONICAL no determina las tarifas, la edad, las tallas, los porcentajes de reserva ni las fechas editoriales. Se comprobó su coherencia interna cuando aparecen, sin usar la memoria ni otros trabajos como fuente.

Lectura byte a byte de los 40 HTML completos, decodificación UTF-8, SHA-256, HTMLParser de la biblioteca estándar y lxml. Se recorrió todo el DOM y todo el contenido de ambos bloques JSON-LD por archivo con `json.loads`, incluyendo arrays, objetos anidados, extensiones y referencias. Se conservaron los valores y los contextos completos en `evidencia/evidence.json`.

Se ejecutaron recuentos textuales de etiquetas, pila de aperturas/cierres, detección de atributos e IDs duplicados, resolución de referencias DOM/ARIA y fragmentos, inventario de todos los href, dos selectores por página, imágenes, headings, metadata, precios, horarios y políticas. Se compararon las preguntas y respuestas visibles con Schema, y los autores, textos y fechas disponibles de reseñas con su representación visible. Solo se normalizaron espacios y entidades HTML; en reseñas se retiraron las comillas de presentación exteriores.

Los 40 archivos aportan 80 bloques JSON-LD válidos. Node comprobó la sintaxis de 40 scripts ejecutables inline y 20 manejadores inline, sin ejecutarlos. Se realizaron 450 comparaciones de precios/ofertas y una segunda pasada de 840 comprobaciones desde los bytes del ZIP original con implementación separada. Las cifras son recuentos de pruebas, no una puntuación ni una garantía absoluta.

BeautifulSoup y html5lib no están instalados. Se utilizó lxml y HTMLParser; no se infirió validez solo porque lxml acepta o repara HTML. No se ejecutó Nu Validator, navegador, servidor, JavaScript externo, ni herramientas de Google. No se consultaron Internet, GitHub ni versiones anteriores.

La revisión lingüística se centró en tema, datos, políticas y errores textuales observables; no constituye una certificación nativa de estilo. La auditoría evalúa el HTML estático completo, no el aspecto final ni el funcionamiento con recursos externos.

## Integridad de los adjuntos

| Adjunto | SHA-256 inicial = final | Sin cambios |
| --- | --- | --- |
| RSB_05_ROLLERBLADES_CORREGIDO_GUIAS_FINAL(1)(5).zip | 571c830a7023d8b7531305bec0096f1279090b174a66088e52ad589e6e010e47 | SÍ |
| RSB_01_HOME_CORREGIDO_FINAL_VALIDATOR_FIXED(2)(5).zip | 95b1d3fba2e3799e682d7312ccf0d2ba73e637ea6058d850d4170aabc74764f1 | SÍ |
| .codex-upload-27ba4ba3d3ae45ebab84291c138e6c9f | c50d24d4907b0acf062b3cfe2dbe7478fcb7a6eaea3d0d697043fa582b7e28ea | SÍ |
| .codex-upload-77b98843dc0a492eb557810f534019b8 | 2a3f571f500374ed48c82c587670f8ab30a72754cd61656543153a361b130f20 | SÍ |
| SCOOTER-main (1)(2).zip | 69dc313209ca4e5468141668e224654c1c0d4aa9de14461283df806e31e0de36 | SÍ |
| .codex-upload-b3206367fa084bc88e62c7f47dcb3eef | 4809de9076543532c214ae31d6a2e603af6f080b9cef7eeb7591fe1324f09794 | SÍ |
| Pegado text(20260906-001634).txt | 9b2c54bb857fcceb2a608f04adf2eec05f297d512a4cd7ac17b0c4ef58985a9c | SÍ |
| RSB_PRICES_PT_PUNTOS_14_15_16_17_18_CORREGIDO(3)(5).zip | 40b457225964e71fe0ebaf6a6558ac9c091f976005e2ad35a51a9cbe0be497f9 | SÍ |
| CANONICAL.md | 357854bb6231f66f53208c26f95e2df60214cc541fd3272fb346b092f105b78c | SÍ |
| .codex-upload-a3fd84ba87034b1a9b7ddf844c7356e8 | 77e7e0458e53a26ef62c1503a6517430f089ca56d239df0164d3ab8d3b96a4a6 | SÍ |
| RSB_HTML_SOLO_4_DIRECTORIOS_SIN_YANDEX(1).zip | d86279df270335cc1dd0e3a0db1976c76d36660bfe78cd7483ee7d06b7302ce7 | SÍ |

El ZIP principal contiene 40 HTML; los HTML de los cuatro ZIP individuales coinciden byte a byte con ellos. Los verificadores Yandex adicionales se excluyeron. No se incluyeron HTML modificados en este paquete: contiene únicamente informes, matrices y evidencia de auditoría.

