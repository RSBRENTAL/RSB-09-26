# Plan de corrección consolidado — RSB Rental Scooter Barcelona
**Basado en 8 páginas auditadas:** Home (ES), Rollerblades (DE), Prices (IT), Scooter (FR), Location-contact (PL), Blog inline-skates (SV), Skateboard (PT), Bike (NL)
**Fecha:** 11 septiembre 2026

---

## Cómo usar este documento

Está organizado en tres bloques:

1. **Arreglos de plantilla compartida** — se corrigen una vez y se propagan solos a todas las páginas que usan esa plantilla. Son los de mayor ROI: mismo esfuerzo, máxima cobertura.
2. **Arreglos específicos de cada página** — bugs de contenido/HTML que solo afectan a la página donde se detectaron.
3. **Imágenes que hay que volver a exportar** — la lista que pediste, con el tamaño/formato recomendado para cada una. Indico en cada caso si además hace falta tocar una línea de HTML (`srcset`) para que el navegador llegue a usar el archivo nuevo, ya que una imagen nueva sin esa línea no se serviría.

---

## 1. Arreglos de plantilla compartida (máxima prioridad)

### 1.1 Clase `home-page` colada en el `<body>` — confirmado en 4 plantillas
**Afecta a:** contacto (PL), blog (SV), skateboard (PT), bike (NL) — y muy probablemente al resto de páginas de servicio (scooter, rollerblades, quads, longboard) que no llegamos a comprobar el `<body>` directamente, ya que comparten la misma estructura de hero.

**Qué pasa:** el `<body>` lleva `class="home-page service-page ..."` (o `blog-page`, `location-contact-page`, etc.) a la vez. La regla `.home-page .card-elevated{background:#cfe4ff !important}`, pensada solo para la home, se activa igualmente en todas esas páginas porque también usan `.card-elevated` en sus tarjetas.

**Causa probable:** estas páginas reutilizan el componente de hero de la home (`<h1 class="home-hero-title">`), y alguien añadió `home-page` al `<body>` solo para heredar ese estilo de hero — sin darse cuenta de que arrastra también la regla de fondo azul.

**Arreglo recomendado:** separar las dos cosas.
- Mover el estilo de `.home-hero-title` a un selector que no dependa de `.home-page` (o darle su propia clase, p. ej. `.hero-title-shared`).
- Cambiar `.home-page .card-elevated{...}` por un selector más estrecho que solo afecte a las tarjetas de servicio reales de la home, p. ej. `.home-page .home-service-card` en vez de `.card-elevated` (clase genérica reutilizada en todo el sitio).
- Una vez desacoplado, quitar `home-page` del `<body>` de todas las páginas que no sean la home.

**Verificación:** después del cambio, compara visualmente el color de fondo de las tarjetas en una página de servicio/blog/contacto contra la home — deberían dejar de verse azuladas si antes lo estaban.

---

### 1.2 `meta robots` sin `max-snippet:-1` — confirmado en las 8 páginas
```html
<meta content="index,follow,max-image-preview:large" name="robots"/>
```
Cambiar a:
```html
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"/>
```
Impacto directo en GEO: sin `max-snippet:-1`, Google limita cuánto texto puede citar en AI Overviews y fragmentos de búsqueda. Al vivir en el `<head>` compartido, un solo cambio de plantilla lo arregla en todo el sitio.

---

### 1.3 Sin skip link de accesibilidad — confirmado en las 8 páginas
Ninguna página tiene un enlace "saltar al contenido" al inicio del `<body>`. Es un componente de layout compartido (header), así que se añade una vez y queda resuelto en todo el sitio.

---

### 1.4 JSON-LD partido en dos `<script>` en vez de uno — confirmado en las 8 páginas
Todas las páginas cargan el `@graph` principal en un `<script>` y las reseñas (`Review`) en otro `<script data-rsb-review-entities>` aparte. Es válido, pero el parseo de Rich Results es más fiable con un único bloque `@graph` consolidado. Cambio de plantilla, no de contenido.

---

### 1.5 CSS render-blocking en páginas de servicio/blog/contacto
**Afecta a:** todas menos la home real (ES), que sí usa un patrón optimizado (`<style data-rsb-critical>` inline + `preload`/`onload` swap para el resto).

Las demás páginas cargan 3-4 hojas de estilo de forma síncrona y bloqueante (`fonts`, `styles.css`, `stylesHome.css`, `scooter/styles41.css`, `blog/stylesBlog.css`, `Prices/prices.css` según la página). Recomendación: llevar el patrón de precarga optimizado de la home real al resto de plantillas. Es el arreglo de mayor esfuerzo de esta lista, pero también el de mayor impacto en Core Web Vitals / LCP en móvil.

---

### 1.6 Fecha de "última actualización" no visible en el texto
**Excepción que confirma la regla:** la página de blog en sueco sí la muestra ("Uppdaterad 27 juli 2026") y es la única. Recomiendo llevar ese mismo patrón (un pill/etiqueta visible con la fecha) a las páginas de servicio y a la home, ya que hoy esa fecha solo vive oculta en el `dateModified` del JSON-LD.

---

## 2. Arreglos específicos de cada página (contenido/HTML, no imágenes)

| Página | Bug | Detalle |
|---|---|---|
| Home (ES) | H1/H2 duplicados | El primer `<h2>` tras el hero repite el `<h1>` casi literalmente. Reescribir el H2. |
| Home (ES) | `<h2>` envolviendo un `<a>` completo | Botón "Ver precios y reservar" — separar el texto del H2 del enlace. |
| Home (ES) | Jerarquía inconsistente | Las 6 tarjetas de servicio mezclan `<h2>`/`<h3>` sin criterio; igualar todas a `<h3>`. |
| Home (ES) | Sin `Offer`/precio en JSON-LD | El `ItemList` de servicios no tiene precios; añadir `Offer` como en el resto de páginas. |
| Home (ES) | `BreadcrumbList` de 1 solo elemento | Sin utilidad así; completar o retirar. |
| Prices (IT) | Dirección corrupta en el footer | Falta el icono de ubicación y "100 m da Port Olímpic" está duplicado dos veces en vez de decir "Vila Olímpica del Poblenou". Revisar si se repite en otros idiomas de `/Prices/`. |
| Scooter (FR) | Frase repetida en el hero | La aclaración "solo alquilamos scooters de gasolina, no eléctricos" aparece casi literal dos veces seguidas; dejar solo una. |
| Contacto (PL) | Frase con inglés sin traducir | "Convenient base dla nadmorskie trasy..." — falta traducir y corregir la declinación en polaco. |
| Rollerblades (DE) | Frase incompleta | Falta el verbo final en "...kannst du unseren [Guide]." |
| Skateboard (PT) | `srcset` con entrada duplicada | El mismo archivo `-800.webp` aparece listado como `800w` y como `1200w` — ver sección 3, punto 3.4 (requiere también una línea de HTML). |
| Blog (SV) | Coordenadas GPS con menos decimales en `sameAs` (Apple Maps) | `41.390577,2.198362` en vez de `41.3906488,2.1984312` usado en el resto del schema. Homogeneizar. |

---

## 3. Imágenes a revisar/reexportar

Aquí está lo que pediste. Para cada imagen indico **qué está mal**, **el tamaño recomendado**, y si el arreglo es **solo de imagen** (puedes cambiar el archivo tal cual, sin tocar nada más) o si **también hace falta una línea de HTML** (porque el archivo nuevo no se llegaría a usar si no se referencia).

### 3.1 Hero de Scooter (FR) — falta versión responsive
**Archivo actual:** `rsb-scooter-rental-barcelona-hero-group-v1-1536.webp` (único tamaño servido a todos los dispositivos)
**Recomendación:** exportar también:
- `...-480.webp` (480px de ancho)
- `...-800.webp` (800px de ancho)
- Mantener la de 1536px para escritorio.

⚠️ **Necesita también HTML:** el `srcset` actual solo tiene una entrada (`1536w`). Aunque generes los archivos de 480 y 800px, el navegador no los usará hasta que se añadan al `srcset` del `<link rel="preload">` y del `<img>`. Es una línea de código — avísame si quieres que te la prepare para pasársela a quien toque el HTML.

---

### 3.2 Hero de Contacto (PL) — mismo problema
**Archivo actual:** `rsb-rental-scooter-barcelona-shop-vila-olimpica.webp` (único tamaño, 1200px)
**Recomendación:** exportar también una variante de 480px y otra de 800px, siguiendo el mismo patrón de nombres que el resto del sitio (`nombre-480.webp`, `nombre-800.webp`).

⚠️ **Necesita también HTML**, mismo motivo que el punto 3.1.

---

### 3.3 Hero del blog "Guide till inlines" (SV) — dimensiones declaradas incorrectas
**Archivo:** `rsb-inline-skates-rental-barcelona-vila-olimpica-800.webp`
**Qué está mal:** no es un problema del archivo en sí — el archivo real mide 800×533 (según los propios metadatos `og:image` de la página), pero el HTML le declara `width="1600" height="900"`, una relación de aspecto distinta (16:9 declarado vs. 3:2 real).

**No hace falta que reexportes esta imagen.** Es un error de las etiquetas `width`/`height` en el HTML, no del archivo. Si prefieres resolverlo por el lado de imagen de todas formas (para que ambos coincidan sin tocar código), tendrías que recortar la foto a 16:9 y exportarla a 1600×900 — pero perderías parte del encuadre original. Mi recomendación es la contraria: pedir que corrijan el HTML a `width="800" height="533"` en vez de tocar la imagen.

---

### 3.4 Imagen "incluido" de Skateboard (PT) — `srcset` con archivo duplicado
**Archivo:** `rsb-skateboard-rental-barcelona-vila-olimpica-800.webp`
**Qué está mal:** el HTML referencia el mismo archivo dos veces, como si fueran dos tamaños distintos (`800w` y `1200w`), cuando solo existe la versión de 800px.

**Aquí sí conviene generar un archivo nuevo real:** exporta una variante genuina de **1200px de ancho** con el mismo nombre que ya usa el patrón del sitio (`rsb-skateboard-rental-barcelona-vila-olimpica-1200.webp`).

⚠️ **Necesita también HTML:** aunque subas el archivo de 1200px, el `srcset` actual apunta dos veces al de 800px por su nombre exacto — hay que cambiar una de las dos URLs para que apunte al nuevo archivo de 1200px. Sin ese cambio, el archivo nuevo quedaría subido pero sin usarse.

---

### 3.5 Resto de imágenes hero (Home, Rollerblades DE, Prices IT, Bike NL) — sin cambios necesarios
Estas ya tienen `srcset` completo y bien formado (480w/800w/1200w/1600w, todo con archivos reales y distintos). No hace falta tocarlas.

---

## 4. Resumen ejecutivo de prioridades

| # | Arreglo | Tipo | Esfuerzo | Impacto |
|---|---|---|---|---|
| 1 | Desacoplar `home-page` del hero compartido | Plantilla | Medio | Alto (visual, 4+ páginas) |
| 2 | `max-snippet:-1` en robots | Plantilla | Muy bajo | Alto (GEO) |
| 3 | Skip link | Plantilla | Bajo | Medio (accesibilidad) |
| 4 | Exportar imágenes hero responsive (3.1, 3.2) | Imagen + HTML | Medio | Medio (rendimiento móvil) |
| 5 | Exportar imagen 1200px de skateboard (3.4) | Imagen + HTML | Bajo | Bajo |
| 6 | Corregir `width`/`height` del hero del blog SV (3.3) | Solo HTML | Muy bajo | Bajo (CLS) |
| 7 | Consolidar JSON-LD en un `@graph` | Plantilla | Medio | Bajo-medio |
| 8 | CSS crítico/preload en todas las plantillas | Plantilla | Alto | Alto (Core Web Vitals) |
| 9 | Arreglos de contenido específicos (sección 2) | Página a página | Bajo cada uno | Medio (confianza/E-E-A-T) |
