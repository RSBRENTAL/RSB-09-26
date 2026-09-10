# Auditoría técnica SEO/GEO — Página "Prezzi" (IT) — `/it/Prices/`

**Fecha:** 11 septiembre 2026

---

## 1. Resumen ejecutivo

Esta es, de las tres páginas auditadas hasta ahora, **la mejor construida a nivel de schema**: tiene `Offer` con precio para prácticamente cada franja horaria de las 6 categorías (scooter, patines en línea, bici, patines de 4 ruedas, skate, longboard), un `BreadcrumbList` real de 2 niveles, y **sin duplicación H1/H2** ni el antipatrón del `<h2>` como enlace que sí tenía la home.

A cambio, tiene **un bug de contenido nuevo y bastante visible**: el bloque de contacto del footer tiene datos de dirección corruptos/duplicados. Es el hallazgo más importante de esta ronda.

---

## 2. Bug nuevo y específico de esta página (no visto antes)

### 🔴 Dirección del footer corrupta (líneas 1622–1631)

```html
<li style="display:flex;gap:0.75rem;align-items:flex-start">
<span style="color:var(--primary)">Vila Olímpica del Poblenou</span>
<div>
<address style="font-style: normal;">
  Carrer de Salvador Espriu, 63<br/>
  08005 Barcelona<br/>
<span>100 m da Port Olímpic</span><br/>
<span>100 m da Port Olímpic</span>
</address>
</div>
</li>
```

Comparado con el patrón correcto que usan la home y la página de rollerblades (icono de ubicación SVG + dirección con "Vila Olímpica del Poblenou" y "100 m de Port Olímpic" como dos líneas distintas), aquí:

1. **Falta el icono SVG de ubicación** — en su lugar aparece el texto "Vila Olímpica del Poblenou" suelto, fuera de la `<address>`, donde debería ir el pin.
2. **"100 m da Port Olímpic" está duplicado dos veces** dentro de la dirección, en el lugar donde debería decir "Vila Olímpica del Poblenou" en la primera línea.

Es decir: se perdió una línea de contenido real y se duplicó otra por error, probablemente en una sustitución de plantilla/traducción. Verifiqué que el icono de ubicación **sí existe correctamente** en el header y en la sección de mapa de esta misma página (líneas 1326, 1347, 1377) — el fallo está aislado al bloque de contacto del footer. Esto afecta a NAP (Name-Address-Phone) consistency, una señal de confianza para SEO local, y además es un error visible para cualquier usuario que mire el footer.

**Prioridad: alta.** Es fácil de arreglar y probablemente sea el mismo bug de plantilla en las versiones de este footer en otros idiomas — conviene revisar el resto de páginas `/Prices/` (ES, EN, FR, etc.) por si se repite.

---

## 3. Errores que se repiten en las 3 páginas auditadas (home, rollerblades DE, prices IT)

Estos son ya un patrón sistémico de plantilla, no un despiste puntual — conviene arreglarlos una vez en el componente compartido en lugar de página por página:

1. **`meta robots` sin `max-snippet:-1` / `max-video-preview:-1`** en las tres páginas.
2. **Sin skip link de accesibilidad** en ninguna de las tres.
3. **Dos bloques `<script type="application/ld+json">` separados** (uno para `@graph` principal, otro para reseñas) en las tres páginas, en vez de consolidarlos en uno.
4. **Sin fecha de "última actualización" visible en el texto** — solo en `dateModified` del JSON-LD.

---

## 4. Comparación específica con las páginas anteriores

| Aspecto | Home (ES) | Rollerblades (DE) | Prices (IT) |
|---|---|---|---|
| H1/H2 duplicados | ⚠️ Sí | ✅ No | ✅ No |
| `<h2>` envolviendo un `<a>` | ⚠️ Sí | ✅ No | ✅ No |
| Jerarquía de encabezados de tarjetas | ⚠️ Inconsistente (h2/h3 mezclados) | ✅ Consistente | ✅ Consistente |
| `Offer`/precio en JSON-LD | ⚠️ No | ✅ Sí (6 ofertas) | ✅ Sí (muy completo, todas las categorías) |
| `BreadcrumbList` real | ⚠️ 1 solo nivel | ✅ 2 niveles | ✅ 2 niveles |
| CSS render-blocking sin optimizar | ✅ Optimizado (crítico inline) | ⚠️ Sí, bloqueante | ⚠️ Sí, bloqueante (mismo patrón) |
| Bug de contenido/dirección | — | ⚠️ Frase incompleta en alemán | 🔴 Dirección corrupta en footer |

Esto confirma el patrón que ya apuntaba en la auditoría anterior: **la home tiene el mejor rendimiento pero el peor schema/estructura de contenido; las páginas de servicio (rollerblades, prices) tienen mejor schema/estructura pero peor rendimiento.** Son dos ramas de plantilla que evolucionaron por separado y conviene unificar.

---

## 5. Otras observaciones menores de esta página

- **Consistencia dato-a-dato entre precios visibles y JSON-LD**: revisé varias franjas (scooter, patines en línea, bici) y coinciden exactamente entre lo que se ve en las tarjetas y lo que hay en el `Offer` — muy buena señal de confianza para AI Overviews/GEO, mantenlo así.
- **Verificación de Google Search Console** (`google-site-verification`) presente en esta página — confirma que ya la tienen dada de alta en GSC, así que puedes verificar directamente ahí los datos de cobertura/indexación en lugar de inferirlos solo del HTML.
- El `<h1>` de esta página menciona solo "scooter, pattini in linea e biciclette" aunque la página cubre 6 categorías — mismo patrón de título parcial que la home; no es grave pero podría ampliarse ligeramente para cubrir más términos long-tail relevantes (patines de 4 ruedas, skate, longboard) sin llegar a saturarlo.

---

## 6. Checklist priorizado (específico de esta página)

**Alto impacto:**
1. Arreglar el bloque de dirección corrupto en el footer (icono + texto duplicado).
2. Revisar si el mismo bug de footer se repite en otras versiones de idioma de `/Prices/`.

**Ya cubierto por el fix sistémico pendiente (ver sección 3):**
3. `max-snippet:-1` en robots.
4. Skip link.
5. Consolidar JSON-LD.

**Bajo impacto:**
6. Aplicar aquí el mismo patrón de CSS crítico/preload que ya usa la home, para igualar el rendimiento entre plantillas.
