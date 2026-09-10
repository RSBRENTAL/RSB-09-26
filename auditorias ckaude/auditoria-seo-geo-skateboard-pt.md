# Auditoría técnica SEO/GEO — Página "Aluguer de skateboard" (PT) — `/pt/skateboard/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Landing de servicio de skateboard en portugués. Sigue la misma estructura sana que las demás páginas de servicio (scooter FR, rollerblades DE): jerarquía de encabezados limpia, 6 `Offer` con precio, breadcrumb real. **Confirma por tercera vez el bug sitewide de la clase `home-page`** — y esta vez encontré probablemente su causa raíz. También aparece un `srcset` roto con una entrada duplicada/incorrecta.

---

## 2. Bug sitewide confirmado por tercera vez — y posible causa raíz

```html
<body class="home-page service-page skateboard-service-page">
```

Tercera plantilla distinta (después de contacto en polaco y blog en sueco) con `home-page` colado en el `<body>`. Con tres familias de plantilla afectadas, esto ya no es una hipótesis: **es un problema sitewide**.

**Pista sobre el origen del bug**: en esta página, el `<h1>` del hero usa literalmente la clase `home-hero-title` — la misma que usa el `<h1>` de la home real:
```html
<h1 class="home-hero-title" id="skateboard-business-facts-title-pt">Aluguer de skateboard em Barcelona</h1>
```
Es decir, esta página de servicio **reutiliza el componente de hero visual de la home** (mismo tipo de letra/tamaño degradado), y probablemente por eso alguien añadió `home-page` al `<body>`: para activar ese estilo de hero. El problema es que la regla `.home-page .card-elevated{background:#cfe4ff !important}` vive bajo el mismo selector `home-page` y no tiene nada que ver con el hero — se activa como efecto secundario no intencionado.

**Recomendación concreta** (más específica que en la ronda anterior): en vez de quitar `home-page` sin más — lo que podría romper el estilo del hero en las páginas que sí lo reutilizan —, lo correcto es **desacoplar las dos cosas**: mover las reglas de `home-hero-title` a un selector independiente que no dependa de `.home-page`, y limitar `.home-page .card-elevated` a un selector más específico (p. ej. `.home-page .home-service-card` en vez de `.card-elevated` genérico, ya que esta última clase se reutiliza en decenas de componentes de todas las plantillas).

---

## 3. `srcset` con entrada duplicada/incorrecta (bug nuevo)

Línea 793, imagen de la sección "O que está incluído":
```html
<img ... width="1200" height="675"
     src="...vila-olimpica-800.webp"
     srcset="...vila-olimpica-800.webp 800w, ...vila-olimpica-800.webp 1200w" .../>
```

El mismo archivo (`-800.webp`) aparece **dos veces en el `srcset`**, una vez etiquetado como `800w` y otra como `1200w`. Es un error de datos: el navegador cree que existe una variante de 1200px de ancho, pero en realidad recibe el mismo archivo de 800px con otra etiqueta. En el mejor caso no pasa nada (el navegador deduplica), en el peor, en pantallas de alta densidad el navegador "elige" la variante de 1200w esperando más nitidez y no la obtiene.

Además, el propio `width="1200" height="675"` (ratio 16:9) declarado en el `<img>` no coincide con las dimensiones reales de esa imagen según los metadatos `og:image` de la página (1200×800, ratio 3:2) — el mismo tipo de discrepancia de aspect-ratio que señalé en la imagen del artículo de blog sueco. Parece un patrón recurrente: **las imágenes secundarias de contenido (no las del hero) tienden a llevar `width`/`height` mal calculados**, mientras que las imágenes de hero sí están bien resueltas en todas las páginas vistas hasta ahora.

---

## 4. Resto de comprobaciones: en línea con el patrón ya visto

- Jerarquía de encabezados correcta (H1 único, H2 por sección, H3 consistente en las 6 tarjetas de precio y en el FAQ).
- 6 `Offer` con precio en el JSON-LD + `BreadcrumbList` real — coherente con el resto de páginas de servicio.
- Footer de contacto correcto, sin el bug de duplicación visto en la página de precios italiana.
- Imagen del hero **sí** tiene `srcset` responsive completo y bien formado (480/800/1200/1600w, todo absoluto) — a diferencia de la de scooter en francés. Es la sección de contenido secundario la que falla, no el hero.
- 4 hojas de estilo render-blocking (fuentes + `styles.css` + `stylesHome.css` + `scooter/styles41.css`) — de hecho una más que las otras páginas de servicio, precisamente porque esta plantilla mezcla componentes de home y de servicio (coherente con el punto 2).
- `meta robots` sin `max-snippet:-1`, sin skip link, JSON-LD en dos scripts — los mismos tres pendientes de siempre.

---

## 5. Checklist priorizado

**Alto impacto (sitewide):**
1. Desacoplar el hero tipo "home" de la clase de página `home-page` (ver sección 2) — con esto se arreglaría el bug de fondo azul en tres plantillas de golpe (contacto, blog, y todas las páginas de servicio que reutilicen este hero).

**Alto impacto (esta página):**
2. Corregir la entrada duplicada del `srcset` de la imagen "incluido" y ajustar su `width`/`height` a las dimensiones reales.

**Ya cubierto por el fix sistémico pendiente:**
3. `max-snippet:-1`, skip link, consolidar JSON-LD.
