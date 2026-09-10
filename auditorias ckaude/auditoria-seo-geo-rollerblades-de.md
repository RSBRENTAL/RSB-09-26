# Auditoría técnica SEO/GEO — Página "Inlineskates mieten in Barcelona" (DE)

**Archivo:** `index.html` → `/de/rollerblades/`
**Fecha:** 11 septiembre 2026
**Nota:** esta NO es la home — es la landing de servicio "Inlineskates" en alemán. La comparativa con la auditoría anterior es válida porque comparte plantilla/patrones con el resto del sitio.

---

## 1. Resumen ejecutivo

Esta página está en mejor forma que la home en varios puntos clave: **jerarquía de encabezados limpia, un único `@graph` de JSON-LD bien organizado, `Offer`/precio por servicio ya implementado, y tabla de precios visible en el HTML** — precisamente cosas que en la home señalé como pendientes. Eso sugiere que el equipo ya está aplicando mejoras en plantillas nuevas, pero no las ha retro-portado a la home todavía.

A cambio, tiene **un problema de rendimiento que la home no tiene** (CSS render-blocking sin optimizar) y un error de contenido/redacción real en alemán.

---

## 2. Errores idénticos a los de la home (pendientes en ambas)

Estos son los mismos gaps que señalé en la auditoría de la home y que **se repiten aquí sin cambios**:

1. **`meta robots` sin `max-snippet:-1` / `max-video-preview:-1`.** Línea 10: `content="index,follow,max-image-preview:large"`. Mismo hueco de GEO que en la home — limita cuánto texto puede citar Google en AI Overviews/snippets.
2. **Sin `skip link` de accesibilidad.** No hay ningún enlace "saltar al contenido" al inicio del `<body>`, igual que en la home.
3. **Dos bloques `<script type="application/ld+json">` separados** (uno para el `@graph` principal, otro para las reseñas) en vez de uno solo consolidado — mismo patrón que la home, aunque aquí al menos el `@graph` principal ya está bien unificado internamente.
4. **Sin fecha de "última actualización" visible en el texto**, solo en `dateModified` del JSON-LD (`2026-09-02`) — igual que en la home, el dato de frescura no llega al usuario ni a un LLM que solo lea el HTML visible.

## 3. Cosas que aquí SÍ están resueltas (y que en la home seguían pendientes)

Vale la pena que uses esta página como referencia para retro-portar a la home:

1. **Jerarquía de encabezados correcta.** Un único `<h1>`, todos los títulos de sección en `<h2>`, y subelementos (tarjetas de precio, FAQ) en `<h3>` de forma consistente. En la home, en cambio, las 6 tarjetas de servicio seguían repartidas entre `<h2>` y `<h3>` sin criterio.
2. **`Offer` con precio real por franja horaria** en el `Service` del JSON-LD (6 ofertas: 1h, 2h, 3h, día completo, 24h, día extra), con `priceCurrency`, `availability` y nombre — exactamente lo que recomendé añadir en la home y que allí seguía sin implementarse.
3. **Tabla/grid de precios visible en el HTML**, no solo en tarjetas de servicio genéricas — y los precios visibles **coinciden exactamente** con los del JSON-LD (€6/€12/€15/€18/€20/€10). Esta coincidencia dato-a-dato es justo lo que necesitas para que un motor de IA cite el precio con confianza.
4. **`BreadcrumbList` con jerarquía real** (Inicio → Inlineskates mieten), no de un solo elemento como en la home.
5. **Ningún `<h2>` envolviendo un `<a>` completo** — no aparece el antipatrón que sí seguía en el botón "Ver precios y reservar" de la home.
6. **Ninguna imagen con `aria-hidden="true"` indebido.**
7. **`srcset`/`imagesrcset` consistentes**, todo en URLs absolutas.

---

## 4. Errores/oportunidades nuevos, específicos de esta página

### 4.1 CSS completamente render-blocking (rendimiento — peor que la home)
```html
<link href="...fonts.googleapis.com/css2?family=..." rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
```
Cuatro hojas de estilo cargadas de forma **síncrona y bloqueante**, sin el patrón `preload` + `onload` swap ni el CSS crítico inline que sí usa la home. Esto va a penalizar el LCP/render de esta página frente a la home. Además, hay un comentario del propio desarrollador en el código (línea 43): *"Use global site styles instead of rollerblades-specific paths"* — reconoce que es una solución provisional/deuda técnica.

**También llama la atención** que una página de "Inlineskates" cargue un archivo llamado `scooter/styles41.css`. O es una hoja de estilos compartida mal nombrada, o es peso muerto innecesario para esta página — merece revisión.

### 4.2 Error de redacción en alemán (contenido)
Línea 894:
> *"Für Routenideen und praktische Tipps kannst du unseren [Guide zum Inlineskates-Verleih in Barcelona] ."*

Falta el verbo final ("...kannst du unseren Guide **lesen/ansehen/besuchen**."). Es una frase incompleta gramaticalmente en alemán — no es solo estético: afecta la calidad percibida del contenido (señal de E-E-A-T) y puede generar desconfianza en un hablante nativo. Se corrige fácil añadiendo el verbo que falta.

### 4.3 Tres `<h2>` sueltos sin encabezado de sección padre
Líneas 775, 779, 783 (*"Moderne und bequeme Skates"*, *"Alles inklusive"*, *"Lage direkt am Meer"*) son tres tarjetas de confianza, cada una con su propio `<h2>`, pero no hay ningún `<h2>` o `<p class="service-eyebrow">` que titule la sección como conjunto. No es un error grave, pero rompe ligeramente el patron consistente que sí sigue el resto de la página (eyebrow + h2 en cada bloque).

### 4.4 GA cargado de forma síncrona, sin diferir
```html
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
```
Carga con `async` estándar nada más arrancar la página, a diferencia de la home, que difiere Analytics hasta la primera interacción del usuario. Inconsistencia menor de rendimiento entre plantillas, mismo criterio que el punto 4.1.

### 4.5 Título y meta description algo cortos
- Title: *"Inlineskates mieten in Barcelona | RSB"* (~40 caracteres) — funcional, pero deja bastante margen sin usar (hasta ~60).
- Meta description: ~134 caracteres — por debajo del rango óptimo (~150-160) para maximizar el espacio de SERP.
No son errores, pero es fruta fácil: hay margen para meter más contexto/keywords secundarias sin cortarse en el listado de Google.

---

## 5. Checklist priorizado (específico de esta página)

**Alto impacto:**
1. Añadir `max-snippet:-1,max-video-preview:-1` al meta robots (mismo fix que la home — aplícalo globalmente en la plantilla compartida, no página a página).
2. Resolver el CSS render-blocking: aplicar aquí el mismo patrón de preload/critical-CSS que ya usa la home.
3. Corregir la frase incompleta en alemán (línea 894).
4. Revisar si `scooter/styles41.css` es necesario en esta página o es peso muerto.

**Medio impacto:**
5. Añadir `<h2>` de sección para las tres tarjetas de confianza (4.3).
6. Añadir skip link (aplícalo también de forma global, ya que es un componente compartido de layout).
7. Consolidar los dos scripts JSON-LD en un único `@graph`.

**Bajo impacto:**
8. Ampliar ligeramente title/meta description.
9. Añadir fecha de "última actualización de precios" visible en el bloque de precios.

---

## 6. Recomendación general

Dado que esta página ya resuelve varios de los gaps de contenido/schema que señalé en la home (jerarquía de encabezados, `Offer` con precios, breadcrumb real, tabla de precios visible), lo más eficiente sería **usar esta plantilla de servicio como referencia y retro-portar esos mismos patrones a la home**, en lugar de corregir la home de forma aislada. Por otro lado, el problema de CSS bloqueante de esta página apunta a que el patrón de rendimiento optimizado de la home **no se ha propagado** al resto de plantillas de servicio — ese sí conviene llevarlo en la dirección contraria (de home hacia el resto de páginas).
