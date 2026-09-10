# Auditoría técnica SEO/GEO — RSB Rental Scooter Barcelona (index.html)

**Fecha de auditoría:** 10 septiembre 2026
**Archivo analizado:** `index.html` (versión `/es/`, 1291 líneas)
**Alcance:** SEO técnico, datos estructurados, GEO/AEO (motores de respuesta IA), accesibilidad, rendimiento y seguridad.

---

## 1. Resumen ejecutivo

La base es sólida: title, meta description, hreflang, Open Graph, Twitter Cards, y un `@graph` de Schema.org con Organization, WebSite, WebPage, LocalBusiness, FAQPage, ItemList y Review están todos presentes y en general bien formados. Esto ya te pone por delante de la mayoría de webs de alquiler locales.

Dicho esto, hay **3 errores reales que hay que corregir** (no opiniones, son bugs), y una decena de mejoras de prioridad alta/media que marcan la diferencia entre "SEO correcto" y "optimizado también para IA generativa" (AI Overviews de Google, Copilot de Bing, ChatGPT, Perplexity, Claude, etc.).

---

## 2. Errores reales (prioridad crítica)

### 2.1 Anidación incorrecta de `<section>`
Al final del documento (líneas ~1190–1212), la sección de reseñas (`id="reviews"`) queda **anidada dentro** de la sección "Horario e información práctica" en lugar de ser un hermano al mismo nivel:

```html
<section class="section-padding bg-muted">      <!-- Horario -->
  ...
  <section class="section-padding bg-muted" id="reviews">   <!-- Reseñas, anidada -->
    ...
  </section>
</section></div></section></div></main>
```

Esto no es solo un tema de limpieza: rompe la jerarquía semántica del documento (landmarks para lectores de pantalla, y la forma en que los crawlers/LLMs segmentan el contenido por bloques temáticos). **Corrígelo separando ambas secciones como hermanas.**

### 2.2 URLs mezcladas (absolutas/relativas) en el mismo `srcset`
En el `<link rel="preload">` del `<head>` (línea 59) y en el `<img>` del hero (línea 689), el `srcset` mezcla una URL relativa con el resto absolutas:

```
...beach-480-v1.webp 480w, /images/rsb-barcelona-rental-hero-group-beach-720-v2.webp 720w, ...beach-800-v1.webp 800w...
```

Es válido técnicamente (el navegador resuelve la relativa contra el dominio actual), pero es inconsistente y frágil: si esta página se sirve alguna vez desde otro host/subdominio (staging, CDN, preview), esa imagen concreta se romperá mientras las demás no. Además, el nombre de archivo de esa imagen (`-v2`) no sigue el patrón de versión (`-v1`) del resto — probablemente un resto de una actualización de imagen no propagada del todo. Unifica todo a absoluto.

### 2.3 Encabezado `<h2>` usado como enlace completo (antipatrón)
Línea 926:
```html
<h2 style="...">
  <a href="https://rentalscooterbarcelona.com/es/Prices/" style="color:inherit;text-decoration:none">Ver precios y reservar</a>
</h2>
```
Convertir un `<h2>` entero en un enlace de navegación es un antipatrón: mezcla "estructura de contenido" con "call-to-action", diluye el texto ancla real de la página para SEO temático, y es confuso para lectores de pantalla (anuncia "encabezado de nivel 2, enlace" en vez de un titular). Usa un `<h2>` de texto plano seguido de un `<a class="btn">` separado, tal como ya haces en el resto de la página.

---

## 3. Jerarquía de encabezados (H1–H3)

- ✅ Un único `<h1>` correcto y descriptivo: *"Alquiler de scooter y patines en línea en Barcelona"*.
- ⚠️ **Inmediatamente después**, el primer `<h2>` de la página (línea 725) repite el H1 **casi palabra por palabra**. Repetir el H1 en el H2 de apertura no ayuda al SEO temático (no añade cobertura semántica nueva) y puede leerse como sobre-optimización. Cámbialo por algo complementario, p. ej. *"Tu tienda de movilidad en Vila Olímpica, frente a la playa"*.
- ⚠️ **Inconsistencia de nivel entre tarjetas de servicio equivalentes**: Scooter y Patines en línea usan `<h2>` (líneas 751 y 780), pero Bicicleta, Patines de 4 ruedas, Skateboard y Longboard usan `<h3>` (líneas 810, 838, 866, 894). Son 6 tarjetas del mismo tipo y mismo nivel de importancia visual — deberían compartir el mismo nivel de encabezado (todas `<h3>`, colgando de un `<h2>` de sección tipo "Nuestros servicios de alquiler").
- Esto también afecta a la extracción automática de "listas de servicios" que hacen los motores de IA: una jerarquía irregular hace más difícil que agrupen correctamente los 6 servicios como elementos de la misma lista.

---

## 4. Datos estructurados (Schema.org)

### Lo que está bien
- `Organization`, `WebSite`, `WebPage`, `LocalBusiness`, `FAQPage`, `ItemList` (servicios) y `Review` están presentes y enlazados por `@id` correctamente.
- `LocalBusiness` incluye `geo`, `openingHoursSpecification`, `areaServed`, `priceRange`, `paymentAccepted`, `sameAs` (incluyendo Google Maps `cid`, Apple Maps y Bing Maps — buena cobertura multi-motor).
- `FAQPage` con 9 preguntas: esto es probablemente tu activo más valioso para aparecer en **AI Overviews de Google y respuestas de Bing Copilot/ChatGPT**, porque son bloques de pregunta-respuesta ya extraídos y listos para citar.
- Las reseñas visibles en la página (línea 1204-1206) coinciden con las del JSON-LD — correcto; Google penaliza el *review schema* que no corresponde a contenido visible.

### Qué falta o se puede mejorar
1. **Dos `<script type="application/ld+json">` distintos modificando el mismo `@id` (`#business`, `#webpage`)** en vez de un único `@graph` consolidado. Es válido, pero el parseo de fragmentos repartidos en varios `<script>` es menos fiable para Rich Results que un único bloque. **Recomendación: fusionar ambos en un solo `@graph`.**
2. **Sin `Offer`/`AggregateOffer` por servicio.** Actualmente el `ItemList` de servicios solo tiene `name` y `url`, sin precio. Añadir `offers` (con `price`, `priceCurrency: "EUR"`, `availability`) a cada `Service` permite que Google muestre precio directamente en resultados enriquecidos, y da a los motores de IA un dato factual y citable ("desde €4/hora") en lugar de tener que extraerlo del texto libre.
3. **`BreadcrumbList` con un único elemento** ("Inicio"). Un breadcrumb de un solo nivel no aporta valor real; o se completa con jerarquía real (si en el futuro hay subcategorías) o se retira de la home.
4. **Sin `SpeakableSpecification`.** Si te interesa presencia en asistentes de voz/Google Assistant, puedes marcar el bloque de FAQ como `speakable` (CSS selector), que Google usa específicamente para respuestas habladas.
5. **`Organization.logo`** no incluye `width`/`height` — no es obligatorio, pero Google lo recomienda para validación más robusta del logo en Knowledge Panel.

---

## 5. GEO / AEO — Optimización para motores de respuesta IA

Esto es lo que probablemente más te interesa dado el contexto. Los puntos anteriores de Schema.org ya son la base de GEO, pero hay factores específicos adicionales:

### 5.1 Meta robots incompleto para maximizar citación en IA
Actualmente:
```html
<meta content="index,follow,max-image-preview:large" name="robots"/>
```
Falta `max-snippet:-1` y `max-video-preview:-1`. **`max-snippet` controla explícitamente cuánto texto puede usar Google (y por extensión, los sistemas que reutilizan su índice) para generar fragmentos y respuestas de AI Overviews.** Sin `max-snippet:-1`, Google aplica un límite por defecto que puede recortar el fragmento citable. Esto es un cambio de una línea con impacto directo en GEO:
```html
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"/>
```

### 5.2 Verifica el acceso de los rastreadores de IA en `robots.txt`
El `index.html` no lo determina, pero es la primera cosa a comprobar fuera de este archivo: confirma que `robots.txt` **no bloquea** `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Bingbot` y `CCBot`. Si el sitio anterior (el que dices que "no es válido") tenía bloqueos genéricos de bots, es una causa muy común de invisibilidad total en ChatGPT/Perplexity aunque el SEO tradicional esté bien.

### 5.3 Contenido renderizado en servidor (correcto, mantenlo así)
El HTML ya trae el contenido principal (texto, precios, FAQ, dirección) renderizado en el HTML estático, no inyectado por JavaScript. Esto es exactamente lo que necesitas, porque la mayoría de los crawlers de IA (GPTBot, ClaudeBot, PerplexityBot) **no ejecutan JavaScript**. Es tu punto fuerte actual — no lo rompas si en el futuro migras a un framework SPA sin SSR.

### 5.4 Señales de "frescura" visibles, no solo en el schema
`dateModified: "2026-08-24"` existe en el JSON-LD, pero no hay ningún texto visible en la página tipo "Precios actualizados en [fecha]". Los motores de IA generativa priorizan fuentes con señales de actualidad explícitas y visibles al usuario, no solo en metadatos ocultos. Considera añadir una línea discreta con fecha de última actualización de precios/horarios.

### 5.5 Repetición de frases exactas ("Alquiler de X en Barcelona")
El patrón de keyword exacto se repite muy intensamente: en H1, H2, título de tarjeta, texto ancla del botón, texto del enlace del blog, y en el `ItemList` del schema — para las 6 categorías. Es un patrón común y tolerado en páginas locales, pero al ser tan literal y repetitivo en bloques tan próximos entre sí, **para un LLM que resume la página puede leerse como relleno más que como variedad temática real**. Recomendación: mantener el ancla principal 1-2 veces por bloque, y variar el resto ("scooters de 50cc y 125cc", "tienda de patines cerca de la playa", etc.) — mejora tanto SEO clásico (evita sobre-optimización) como GEO (más superficie semántica distinta para que un LLM extraiga matices, no solo la misma frase).

### 5.6 Sin tabla estructurada de precios en el HTML
Los precios existen como texto suelto ("Desde €35 /día", "Desde €6 /hora"...) repartidos en tarjetas separadas. Los LLM extraen y citan mejor datos en tablas o listas estructuradas cuando comparan varias opciones ("¿cuánto cuesta alquilar un scooter vs. una bici en Barcelona?"). Considera añadir una tabla comparativa simple con los 6 servicios y su precio desde, además de las tarjetas visuales.

---

## 6. SEO on-page general

- ✅ Title (~57 car.) y meta description (~148 car.) dentro de rango óptimo.
- ✅ Canonical y hreflang bien enlazados y con self-reference (`es` → `/es/`), correcto.
- ✅ Alt text descriptivo y con contexto geográfico en casi todas las imágenes — bien para SEO de imágenes.
- ⚠️ Imágenes de la galería (líneas 1159-1163) llevan `aria-hidden="true"` **a la vez que** un `alt` descriptivo detallado. Es contradictorio: `aria-hidden` las oculta completamente de lectores de pantalla, haciendo que ese `alt` currado no sirva para accesibilidad (sí sigue sirviendo para indexación de imágenes en Google Images, que es probablemente la intención, pero conviene ser explícito: si es solo para SEO de imágenes y la galería es puramente decorativa/redundante, está bien así; si quieres que también sea accesible, quita `aria-hidden`).
- ⚠️ Si la web pública actual "no es válida" y esta la sustituye, asegúrate de que el equipo de despliegue configure **redirecciones 301** desde las URLs indexadas actuales hacia las nuevas equivalentes. Sin esto, perderás el equity de enlaces/histórico aunque el contenido nuevo sea mejor.

---

## 7. Accesibilidad

- Falta un enlace "saltar al contenido" (`skip link`) al principio del `<body>` — estándar en WCAG 2.1 para usuarios de teclado/lectores de pantalla, útil sobre todo con un header fijo (`position:fixed`) como el tuyo.
- Hay un `<div class="text-muted" style="font-size:0.85rem"></div>` vacío (línea 949-950) — resto de código sin contenido, sin impacto funcional pero conviene limpiarlo.
- El resto de la accesibilidad está cuidada: `aria-label` en iconos e interactivos, `aria-expanded`/`aria-controls` en los desplegables, `aria-hidden` en SVG decorativos.

---

## 8. Rendimiento

- ✅ Buen uso de `preconnect`/`dns-prefetch` para Google Fonts y GTM.
- ✅ `fetchpriority="high"` + `preload` correctamente emparejados para la imagen LCP del hero.
- ✅ Carga diferida de Google Analytics hasta la primera interacción del usuario (o `load`) — buena técnica para no penalizar el LCP/TBT.
- ⚠️ El bloque `<style data-rsb-critical>` inline en el `<head>` es **muy extenso** (cubre prácticamente todo el layout del sitio, no solo el "above the fold"). Si además se carga íntegramente `stylesHome.css` justo después (vía preload+onload), revisa si hay duplicación real de reglas entre ambos: si el "crítico" ya cubre el 90% del CSS, el beneficio de diferir el resto es mínimo y solo añade peso.
- ⚠️ La API key de Google Maps Embed va expuesta directamente en el `src` del iframe (línea 971). No es un fallo de por sí (las claves de Maps Embed API están pensadas para ir en el cliente), pero **confirma en Google Cloud Console que esa key tiene restricciones por referrer HTTP** limitadas a tu dominio; si no las tiene, cualquiera puede reutilizarla y consumir tu cuota/facturación.

---

## 9. Checklist priorizado

**Crítico (arreglar antes de publicar):**
1. Corregir el anidamiento de `<section id="reviews">` dentro de la sección de horario.
2. Unificar URLs absolutas/relativas en el `srcset` del hero (y revisar el nombre `-v2` suelto).
3. Sacar el `<a>` fuera del `<h2>` de "Ver precios y reservar".

**Alto impacto (SEO/GEO):**
4. Añadir `max-snippet:-1,max-video-preview:-1` al meta robots.
5. Confirmar que `robots.txt` permite GPTBot, ClaudeBot, PerplexityBot, Google-Extended.
6. Igualar el nivel de encabezado de las 6 tarjetas de servicio (todas `<h3>` bajo un `<h2>` común).
7. Reescribir el primer `<h2>` para que no duplique el H1.
8. Añadir `Offer`/precio a cada `Service` del `ItemList` en el JSON-LD.
9. Consolidar los dos bloques `<script type="application/ld+json">` en un único `@graph`.

**Medio impacto:**
10. Añadir tabla comparativa de precios en HTML visible (no solo tarjetas).
11. Reducir la repetición literal de "Alquiler de X en Barcelona" variando el texto entre bloques.
12. Añadir fecha de "última actualización" visible cerca de precios/horario.
13. Añadir `skip link` de accesibilidad.
14. Revisar restricciones de la API key de Google Maps.

**Bajo impacto / limpieza:**
15. Eliminar el `<div>` vacío en la sección de contacto.
16. Decidir intención de `aria-hidden` en la galería (SEO-only vs. accesible) y ajustar consistentemente.
17. Expandir o retirar el `BreadcrumbList` de un solo elemento.
18. Añadir `SpeakableSpecification` si interesa presencia en asistentes de voz.

---

*Nota: esta auditoría se basa exclusivamente en el HTML proporcionado. No incluye análisis de Core Web Vitals reales (necesitaría el sitio en producción), `robots.txt`, `sitemap.xml`, ni la configuración de redirecciones del dominio — son las siguientes piezas a revisar una vez el archivo esté desplegado.*
