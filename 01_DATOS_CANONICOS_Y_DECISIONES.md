# Datos canónicos conocidos y decisiones pendientes

## Ya definidos: no hace falta volver a confirmarlos

El archivo `CANONICAL.md` se ha copiado byte a byte del adjunto actual, que coincide con el usado en las dos auditorías. Es la referencia declarada por el usuario; no una verificación externa de la situación actual.

| Dato | Valor conocido |
| --- | --- |
| Nombre / alternativo | RSB Rental Scooter Barcelona / RSB |
| Raíz global | https://rentalscooterbarcelona.com/ |
| IDs globales | Raíz + #organization / #website / #business |
| Teléfono / WhatsApp | +34 640 559 468 / +34640559468 / https://wa.me/34640559468 |
| Correo | info@rentalscooterbarcelona.com |
| Dirección | Carrer de Salvador Espriu, 63; 08005 Barcelona; Catalonia; ES |
| Zona | Vila Olímpica del Poblenou |
| Coordenadas | 41.3906488, 2.1984312 |
| Google CID | 912877649802486634 |
| Apple Place ID | IA5C7938C1925731A |
| Bing YPID | YND84466019C726C1 |
| Horario | Todos los días: 10:30–13:30 y 16:30–20:00 |
| Rating / reseñas | 4.6 / 226; escala 1–5 |
| Moneda | EUR |
| Scooter | 2 cascos; seguro a terceros; depósito reembolsable; devolución fuera de horario previo contacto; hotel gratis desde 3 días; sin protecciones de patinaje. |
| Bicicleta | Casco infantil y candado incluidos; sin depósito ni protecciones de patinaje. |
| Patines, skateboards y longboards | Sin depósito; casco infantil, muñequeras, rodilleras y coderas incluidos. |

## U03: qué falta exactamente

No falta saber la fecha actual ni escoger una de las fechas por ser mayor. Falta identificar la última modificación real de cada HTML/entidad WebPage. Los archivos aportan dos valores incompatibles para el mismo dato y no contienen el historial que permitiría decidir. El nombre del ZIP, su fecha de creación o el valor repetido 2026-08-24 no prueban por sí solos la última actualización del contenido.

| Grupo | HTML | Valores existentes en dateModified | Dato a fijar |
| --- | --- | --- | --- |
| 03_SCOOTER | 10 | ["\"2026-07-30 / 2026-08-24\""] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 08_LONGBOARD | 10 | ["[\"2026-07-30\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 12_BLOG_BEGINNER_INLINE_SKATING | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 14_BLOG_BIKE | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 15_BLOG_HOURLY_INLINE_SKATE_RENTAL | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-07-26\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 16_BLOG_INLINE_SKATES | 10 | ["[\"2026-07-27\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 17_BLOG_LONGBOARD | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 18_BLOG_ROLLER_SKATES | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 19_BLOG_SCOOTER | 10 | ["[\"2026-07-27\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |
| 20_BLOG_SKATEBOARD | 10 | ["[\"2026-07-27\", \"2026-08-24\"]", "[\"2026-06-29\", \"2026-08-24\"]"] | Fecha real por idioma, o una fecha común solo si el historial acredita actualización conjunta. |

El detalle exacto por archivo y las líneas de ambas fechas están en `MATRICES/fechas_por_confirmar.csv` y en cada `CORRECCIONES.md`. Si se conserva una de las fechas ya existentes, se puede igualar o suprimir la propiedad redundante sin reformatear; antes debe determinarse qué valor conservar. No se inventan 130 fechas ni se cambia a hoy.

## U04: una solución concreta ya preparada

Se han comprobado los 32 HTML: en todos la fecha visible coincide con `BlogPosting.datePublished`. Por tanto, la propuesta A conserva fecha y JSON-LD y cambia únicamente «actualizado» por «publicado» en el idioma correspondiente. Cada sustitución exacta está preparada en el plan por archivo y en `MATRICES/etiquetas_publicacion.csv`. Esto resuelve la contradicción de la etiqueta respecto al Schema existente sin inventar una fecha. No certifica externamente que datePublished sea una fecha histórica auténtica.

Si prefieres que la etiqueta siga indicando actualización, entonces debe fijarse esa fecha real; es una alternativa a la propuesta A, no un cambio adicional a aplicar a la vez.

## Detalles comerciales no definidos por CANONICAL

No bloquean U01, U02, U04-propuesta A ni U05–U07. El importe del depósito y sus posibles excepciones; porcentajes de reserva, cancelaciones o redondeo del alquiler por horas; edades y requisitos legales completos; disponibilidad y tallas no se establecen en CANONICAL. Si se decide ampliar esas condiciones como mejora, debe usarse una instrucción operativa vigente. No se convierten importes de reseñas ni recuerdos de otras conversaciones en datos autorizados de estos archivos.

Los precios presentes se han contrastado entre los HTML en las auditorías; no están definidos por CANONICAL como tarifa comercial vigente. No se solicita reconfirmarlos para cambiar coordenadas, URLs o gramática.

## Ampliación: BIKE, QUADS y SKATEBOARD

En sus 30 HTML, WebPage.dateModified contiene 2026-07-30 y 2026-08-24 para el mismo @id. Se añaden al punto U03: 130 HTML en total. Falta únicamente la fecha real respaldada por el historial para resolver ese punto. CONTACT no presenta esta duplicidad contradictoria.

Los 30 cruces de tarifas nuevas contra PRICES coinciden: BIKE 4/8/10/12/20/8 EUR; QUADS y SKATEBOARD 6/12/15/18/20/10 EUR, en el orden de las seis duraciones documentadas. El asiento infantil BIKE de 3 EUR se mantiene separado de las tarifas base. Estos valores se documentan, no se modifican ni se convierten en nuevas reglas canónicas.
