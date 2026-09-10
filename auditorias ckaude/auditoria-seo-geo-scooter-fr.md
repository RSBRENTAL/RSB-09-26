# Auditoría técnica SEO/GEO — Página "Location de scooter" (FR) — `/fr/scooter/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Esta página (landing de scooter en francés) sigue el mismo patrón sano que las otras páginas de servicio ya auditadas (rollerblades DE, prices IT): jerarquía de encabezados limpia, `Offer` con precio en JSON-LD, `BreadcrumbList` real, sin duplicación H1/H2, sin el antipatrón del `<h2>` como enlace. El footer de contacto **está correcto aquí** (no tiene el bug de dirección duplicada que sí vimos en la página de precios italiana).

El hallazgo nuevo más importante es de **rendimiento**: la imagen del hero **no es responsive** — se sirve una única imagen de 1536px de ancho a todos los dispositivos, sin `srcset` con tamaños más pequeños para móvil. Es justo lo contrario de lo que hacían bien las otras 3 páginas.

---

## 2. Bug nuevo y específico de esta página

### 🟠 Imagen del hero sin `srcset` responsive (rendimiento)

Tanto el `preload` como el `<img>` real del hero usan una única imagen fija:

```html
<link as="image" fetchpriority="high" href="...hero-group-v1-1536.webp"
      imagesizes="100vw"
      imagesrcset="...hero-group-v1-1536.webp 1536w" rel="preload"/>
...
<img ... sizes="100vw" src="...hero-group-v1-1536.webp" width="1536" height="864"/>
```

No hay ningún `srcset` con tamaños intermedios (480w/800w, como sí tienen la home, la página de rollerblades y la de precios). Esto significa que un móvil descarga la misma imagen de 1536px que un monitor de escritorio — peso innecesario en la conexión más lenta y probablemente el mayor candidato a penalizar el LCP de esta página en concreto. Es el problema inverso al que señalé en la primera auditoría de la home (ahí el bug era una URL mal formada dentro de un `srcset` que sí existía; aquí directamente no hay `srcset`).

Curiosamente, la propia página incluye un bloque de estilos dedicado a corregir problemas de LCP/CLS (`<style id="scooter4-lcp-cls-fixes">`, líneas 48–60, con `min-height` reservados para evitar saltos de layout) — se nota que ya han trabajado el rendimiento de esta plantilla, pero se les pasó justo la palanca más importante para el LCP: la imagen responsive.

### 🟡 Frase de aclaración duplicada casi literal en el hero (contenido, menor)
Líneas 785–786:
> *"Nous louons uniquement des scooters essence 50cc et 125cc, pas de trottinettes électriques ni d'e-scooters."*
> *"Nous louons uniquement des scooters essence 50cc et 125cc. Nous ne louons pas de trottinettes électriques, d'e-scooters ni de vélos électriques."*

Es la misma idea repetida casi palabra por palabra en dos párrafos consecutivos del hero. La intención es buena y muy recomendable para GEO — desambiguar explícitamente "scooter de gasolina" vs. "patinete eléctrico" es justo el tipo de frase que una IA generativa puede citar directamente para responder "¿alquilan patinetes eléctricos?" — pero no hace falta decirlo dos veces seguidas; con una vez el mensaje ya queda claro y se libera espacio para otra idea.

---

## 3. Confirmación de patrones ya vistos (positivos y pendientes)

**Se mantiene correcto**, igual que en rollerblades (DE) y prices (IT):
- Jerarquía H1 → H2 → H3 consistente, sin duplicar el H1 en el primer H2.
- `Offer` con precio real para las 5 franjas de scooter (día, 24h, 2 días, 3 días, día extra), coincidiendo con las tarjetas visibles.
- `BreadcrumbList` con jerarquía real.
- Sin el antipatrón del `<h2>` envolviendo un `<a>`.
- Footer de contacto correcto (sin el bug de la página de precios italiana).

**Sigue pendiente**, igual que en las otras tres páginas — mismo fix de plantilla compartida:
1. `meta robots` sin `max-snippet:-1` / `max-video-preview:-1`.
2. Sin skip link de accesibilidad.
3. Dos bloques `<script type="application/ld+json">` sin consolidar.
4. CSS render-blocking sin optimizar (misma cadena de 3 hojas de estilo síncronas: fonts, `styles.css`, `scooter/styles41.css` — igual que en rollerblades y prices).
5. Sin fecha de "última actualización" visible en el texto.

---

## 4. Tabla comparativa acumulada (4 páginas)

| Aspecto | Home (ES) | Rollerblades (DE) | Prices (IT) | Scooter (FR) |
|---|---|---|---|---|
| H1/H2 duplicados | ⚠️ Sí | ✅ No | ✅ No | ✅ No |
| `<h2>` con `<a>` envuelto | ⚠️ Sí | ✅ No | ✅ No | ✅ No |
| `Offer`/precio en schema | ⚠️ No | ✅ Sí | ✅ Sí | ✅ Sí |
| `BreadcrumbList` real | ⚠️ 1 nivel | ✅ 2 niveles | ✅ 2 niveles | ✅ 2 niveles |
| Imagen hero responsive (`srcset`) | ✅ Sí | ✅ Sí | ✅ Sí | 🔴 No |
| CSS crítico optimizado | ✅ Sí | ⚠️ No | ⚠️ No | ⚠️ No |
| Bug de contenido propio | — | Frase incompleta (DE) | Dirección duplicada footer | Frase repetida en hero |
| `max-snippet` en robots | ⚠️ No | ⚠️ No | ⚠️ No | ⚠️ No |
| Skip link | ⚠️ No | ⚠️ No | ⚠️ No | ⚠️ No |

La conclusión se refuerza con esta cuarta muestra: **hay dos familias de plantilla** (home vs. páginas de servicio) que evolucionaron cada una optimizando cosas distintas, y **ninguna de las dos páginas de servicio revisadas hasta ahora tiene el CSS optimizado de la home**, mientras que la home es la única sin `Offer`/breadcrumb completo. El fix de `max-snippet` y el skip link son, con diferencia, los cambios más baratos y con mayor cobertura: al vivir en el `<head>`/layout compartido, corrigiéndolos una vez posiblemente se arreglan en las cinco páginas a la vez.

---

## 5. Checklist priorizado (específico de esta página)

**Alto impacto:**
1. Añadir `srcset` responsive real a la imagen del hero (480w/800w/1536w como mínimo), tanto en el `preload` como en el `<img>`.

**Medio impacto:**
2. Recortar la frase de aclaración duplicada del hero a una sola aparición.

**Ya cubierto por el fix sistémico pendiente (ver sección 3):**
3. `max-snippet:-1` en robots, skip link, consolidar JSON-LD, CSS bloqueante.
