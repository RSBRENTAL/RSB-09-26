# Auditoría técnica SEO/GEO — Artículo de blog "Guide till inlines" (SV) — `/sv/blog/inline-skates/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Es un artículo de blog en sueco sobre cómo alquilar patines en línea. Es, con diferencia, **la página con mejor trato del contenido tipo "guía"** de todas las auditadas: tiene `BlogPosting` con fechas de publicación/actualización, **fecha de actualización visible en el propio texto** ("Uppdaterad 27 juli 2026" — justo lo que llevo pidiendo desde la auditoría de la home), rutas concretas, tabla de precios, y FAQ con 7 preguntas bien alineadas con el schema.

El hallazgo más importante de esta ronda **no es de esta página en particular, sino que confirma un patrón sitewide**: el mismo bug de clase `home-page` colada en el `<body>` que vimos en la página de contacto polaca también aparece aquí, lo que sugiere que **no es un despiste aislado sino un problema de plantilla base que probablemente afecta a la mayoría de páginas no-home del sitio**.

---

## 2. Confirmación del bug sitewide: `home-page` en el `<body>`

```html
<body class="home-page blog-page article-page inline-skates-blog-page">
```

Igual que en `/pl/location-contact/`, el `<body>` incluye `home-page` además de las clases propias de la plantilla de blog. Como esta página también usa profusamente `class="card-elevated"` (todas las tarjetas `post-card` del artículo), es muy probable que le esté aplicando la misma regla `!important` pensada solo para la home:

```css
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
```

No puedo confirmar el efecto visual final sin ver `stylesBlog.css` (que sí podría sobreescribirlo con su propio `!important`, pero sería casualidad, no diseño intencional), así que lo marco como "a verificar visualmente" — pero dado que ya lo hemos visto en dos plantillas distintas (contacto y blog), **recomiendo revisar el `<body class="...">` de todas las páginas del sitio que no sean la home** y quitar `home-page` de las que no lo son. Es probable que este bug esté presente en scooter, rollerblades, prices y el resto de páginas de servicio que no hemos inspeccionado el `<body>` directamente.

---

## 3. Nuevo hallazgo: dimensiones declaradas de la imagen del hero no coinciden con la imagen real

```html
<img ... height="900" ... src="...rsb-inline-skates-rental-barcelona-vila-olimpica-800.webp" width="1600" .../>
```

El `<img>` del hero declara `width="1600" height="900"` (ratio 16:9), pero los metadatos `og:image:width`/`og:image:height` de esta misma imagen indican `800×533` (ratio ~3:2, y el propio nombre de archivo termina en "-800", el mismo patrón de nomenclatura que en el resto del sitio usan para la variante de 800px de ancho). Es decir: el navegador reserva espacio para una imagen con una relación de aspecto que no es la real.

Esto importa porque los atributos `width`/`height` existen precisamente para que el navegador calcule el `aspect-ratio` y reserve el hueco correcto antes de que la imagen cargue, evitando saltos de layout (CLS). Con datos incorrectos, en el mejor caso el navegador corrige silenciosamente con el CSS de `object-fit`, pero en el peor caso genera un salto de layout visible o un recorte de imagen distinto al esperado. Es fácil de arreglar: poner `width="800" height="533"` (o las dimensiones reales del archivo servido).

*(Nota: la imagen tampoco tiene `srcset` responsive — mismo patrón ya señalado en las páginas de scooter FR y contacto PL.)*

---

## 4. Hallazgo menor: coordenadas GPS ligeramente distintas en enlaces `sameAs`

En el JSON-LD de esta página, el enlace de Apple Maps usa `coordinate=41.390577%2C2.198362`, mientras que el resto de la ficha (meta `geo.position`, `GeoCoordinates` del schema, y las mismas páginas anteriores auditadas) usa consistentemente `41.3906488,2.1984312`. Es la misma ubicación con menos decimales — no rompe nada funcionalmente, pero es un pequeño síntoma de que estos bloques de datos se copian/pegan manualmente entre páginas en vez de generarse desde una única fuente de verdad. Vale la pena unificarlo por higiene de datos (NAP consistency).

---

## 5. Lo que está muy bien en esta página (para replicar en el resto del sitio)

1. **Fecha de actualización visible en el texto** ("Uppdaterad 27 juli 2026" en el propio hero) — esto es exactamente lo que recomendé añadir en la home y que en el resto de páginas de servicio sigue faltando. Cópialo al resto de plantillas.
2. **`BlogPosting` completo**: `datePublished`, `dateModified`, `author`, `publisher`, `articleSection`, `keywords`, `articleBody` — nivel de detalle superior al de cualquier otra página vista hasta ahora.
3. Tabla de precios visible + coincide con lo que probablemente está en la página de precios real.
4. Enlaces internos a otros artículos relacionados y a las páginas de conversión (precios, contacto, rollerblades) — buena arquitectura de enlazado interno para SEO y para que un LLM pueda "saltar" de este artículo informativo a la página transaccional.
5. `FAQPage` con 7 preguntas, todas presentes también en el HTML visible y coincidentes.

---

## 6. Patrones sistémicos ya vistos, confirmados también aquí

1. `meta robots` sin `max-snippet:-1`.
2. Sin skip link de accesibilidad.
3. Dos bloques `<script type="application/ld+json">` sin consolidar.
4. CSS render-blocking: 3 hojas de estilo síncronas (fonts, `stylesHome.css`, `blog/stylesBlog.css`), sin el patrón de precarga de la home real.
5. Imagen de cabecera sin `srcset` responsive.

---

## 7. Checklist priorizado (específico de esta página + acción sitewide)

**Acción sitewide (la más importante de esta ronda):**
1. Auditar el `<body class="...">` de todas las plantillas no-home del sitio y quitar `home-page` donde no corresponda. Confirmarlo visualmente comparando el color de fondo de las tarjetas `.card-elevated` en una página de servicio/blog/contacto contra la home.

**Alto impacto, específico de esta página:**
2. Corregir `width`/`height` del `<img>` del hero para que coincidan con las dimensiones reales del archivo (800×533).

**Medio impacto:**
3. Añadir `srcset` responsive a la imagen del hero.
4. Unificar las coordenadas GPS usadas en los enlaces `sameAs` con las del resto del schema.

**Ya cubierto por el fix sistémico pendiente:**
5. `max-snippet:-1`, skip link, consolidar JSON-LD, CSS crítico.
