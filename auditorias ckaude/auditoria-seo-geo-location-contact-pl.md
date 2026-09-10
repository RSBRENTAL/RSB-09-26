# Auditoría técnica SEO/GEO — Página "Kontakt i lokalizacja" (PL) — `/pl/location-contact/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Esta es la página de ubicación/contacto en polaco. Tiene un **bug de CSS con impacto visual real** que no había aparecido en las 4 páginas anteriores, más un error de traducción parcial (texto en inglés mezclado sin traducir dentro del polaco). El resto de fundamentos (schema, jerarquía de encabezados, breadcrumb, FAQ) está en línea con lo ya visto en las páginas de servicio.

---

## 2. Bug nuevo más importante: clase de plantilla equivocada en `<body>`

```html
<body class="home-page location-contact-page">
```

El `<body>` lleva **las dos clases a la vez**: `home-page` (que debería aplicar solo a la página de inicio) y `location-contact-page` (la correcta para esta página). El problema no es solo semántico: en el `<head>` hay un bloque CSS con el selector

```css
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
```

Como esta página sí contiene elementos `.card-elevated` (las tarjetas de dirección, teléfono, email, horario, las de reseñas y las de FAQ), esa regla **se está aplicando aquí aunque no debería** — todas esas tarjetas reciben un fondo azul clarito (#cfe4ff) pensado únicamente para las tarjetas de servicio de la home. Es un `!important`, así que no hay forma de que se sobreescriba accidentalmente por otra regla más específica.

Además, hay otros ~80 líneas de CSS con selectores `.home-page .home-service-card`, `.home-page .home-cta-row`, `.home-page .highlight-bar`, etc. (líneas 376–456) que no encuentran elementos correspondientes en esta página y que se cargan sin ningún efecto — peso muerto en el HTML.

**Prioridad: alta.** Es un cambio de una palabra (quitar `home-page` del `class` del `<body>`) con impacto visual inmediato y visible para cualquier usuario que visite la página.

---

## 3. Error de traducción parcial (contenido)

Línea 764:
> *"Convenient base dla nadmorskie trasy i central Barcelona."*

Es una frase con **palabras en inglés sin traducir mezcladas con polaco** ("Convenient base" en vez de algo como "Wygodna baza"), y además con concordancia gramatical incorrecta en la parte polaca ("dla nadmorskie trasy" debería llevar declinación, algo como "dla tras nadmorskich"). Es el tercer error de contenido/traducción que encontramos en esta ronda de auditorías (después de la frase incompleta en alemán y la dirección duplicada en italiano) — sugiere que vale la pena una revisión de QA lingüística específica en las versiones no españolas del sitio, más allá de los aspectos técnicos.

---

## 4. Lo que está bien / en línea con el resto del sitio

- Jerarquía de encabezados limpia: un único `<h1>`, `<h2>` por sección, `<h3>` para las subtarjetas — sin duplicar el H1 en el primer H2.
- `FAQPage` con schema presente y coincide con las 4 preguntas visibles en la página.
- `BreadcrumbList` con jerarquía real (2 niveles).
- El formulario de contacto (`#rsbContactForm`) es una idea sólida para GEO/UX: arma el mensaje y lo abre directamente en WhatsApp por JS. Único matiz: si el usuario tiene JavaScript desactivado o bloqueado, el formulario no tiene `action`/`method` de respaldo, así que se quedaría sin hacer nada útil al enviarse. No es probable que afecte a muchos usuarios reales, pero es fácil de blindar con un `action="mailto:info@rentalscooterbarcelona.com"` como fallback.

---

## 5. Patrones ya vistos, confirmados también aquí

1. **`meta robots` sin `max-snippet:-1`.**
2. **Sin skip link de accesibilidad.**
3. **Dos bloques `<script type="application/ld+json">` sin consolidar.**
4. **Imagen del hero sin `srcset` responsive real** — igual que en la página de scooter en francés: el `preload` y la imagen solo tienen un tamaño (1200w), sin variantes para móvil.
5. **CSS render-blocking**: aunque esta página carga `stylesHome.css` (la hoja de la home), no usa el patrón de `preload` + `onload` que sí tiene la home real — se carga de forma síncrona igual que en las páginas de servicio.

---

## 6. Checklist priorizado (específico de esta página)

**Alto impacto:**
1. Quitar la clase `home-page` del `<body>` (o, si de verdad se necesita compartir algún estilo puntual, aislarlo con un selector propio en vez de reutilizar las reglas de la home).
2. Corregir la frase con inglés sin traducir (línea 764).
3. Añadir `srcset` responsive a la imagen del hero.

**Ya cubierto por el fix sistémico pendiente (visto en las 5 páginas):**
4. `max-snippet:-1` en robots, skip link, consolidar JSON-LD, aplicar el patrón de CSS crítico de la home real a esta plantilla.

**Bajo impacto:**
5. Añadir `action="mailto:..."` como fallback del formulario de contacto para el caso sin JavaScript.
