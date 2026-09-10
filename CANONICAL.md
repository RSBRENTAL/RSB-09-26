# RSB RENTAL — DATOS CANÓNICOS GLOBALES

**Referencia de coherencia global para RSB Rental Scooter Barcelona.**

## Regla principal

Los datos globales de empresa, GEO, mapas, horarios, rating y políticas definidos en este archivo deben mantenerse coherentes en todas las páginas.

Los datos SEO propios de cada URL deben ser específicos de esa página y de su idioma.

Este archivo es una **FUENTE DE VERDAD GLOBAL** para los datos expresamente definidos aquí.  
No debe utilizarse para inventar información que no aparezca en este documento.

---

## 1. Datos globales obligatorios

| Dato | Valor canónico |
|---|---|
| Nombre | RSB Rental Scooter Barcelona |
| Nombre alternativo | RSB |
| Web global | https://rentalscooterbarcelona.com/ |
| Teléfono visible / Schema | +34 640 559 468 |
| Teléfono E.164 | +34640559468 |
| WhatsApp | https://wa.me/34640559468 |
| Email | info@rentalscooterbarcelona.com |
| Dirección | Carrer de Salvador Espriu, 63 |
| Código postal | 08005 |
| Ciudad | Barcelona |
| Región | Catalonia |
| País Schema | ES |
| Zona | Vila Olímpica del Poblenou |
| Latitud definitiva | 41.3906488 |
| Longitud definitiva | 2.1984312 |
| Rating | 4.6 |
| Review count | 226 |
| bestRating | 5 |
| worstRating | 1 |
| Moneda | EUR |

---

## 2. Mapas y coordenadas

### Coordenadas canónicas únicas

```text
41.3906488, 2.1984312
```

Estas coordenadas deben utilizarse en todas las referencias GEO equivalentes.

### Coordenadas antiguas prohibidas

```text
41.390577, 2.198362
```

No deben reaparecer como coordenadas de la entidad.

### Google Maps

**CID**

```text
912877649802486634
```

**URL**

```text
https://www.google.com/maps?cid=912877649802486634
```

### Apple Maps

**Place ID**

```text
IA5C7938C1925731A
```

**URL canónica**

```text
https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902
```

### Bing Maps

**YPID**

```text
YND84466019C726C1
```

---

## 3. Horarios canónicos

Todos los días:

```text
10:30-13:30
16:30-20:00
```

`OpeningHoursSpecification` debe representar esos dos períodos para Monday-Sunday.

---

## 4. IDs globales de Schema

### Organization

```text
https://rentalscooterbarcelona.com/#organization
```

### WebSite

```text
https://rentalscooterbarcelona.com/#website
```

### LocalBusiness

```text
https://rentalscooterbarcelona.com/#business
```

Estas entidades son globales y sus IDs no deben localizarse por idioma.

---

## 5. Datos específicos de cada página e idioma

Los siguientes elementos **NO son globales** y deben corresponder a la URL concreta auditada:

- `<title>`
- meta description
- canonical
- hreflang
- x-default
- `WebPage.url`
- `WebPage.@id`
- `og:url`
- BreadcrumbList
- H1 / H2 / contenido
- `inLanguage`
- Article / BlogPosting URL e ID cuando corresponda
- Service / Product URL cuando corresponda

No copiar valores de HOME a otras páginas.

---

## 6. Políticas y equipamiento que no pueden contradecirse

### Scooter

- 2 cascos incluidos.
- Seguro a terceros incluido.
- Depósito de seguridad reembolsable.
- Devolución fuera de horario disponible contactando previamente.
- Entrega gratuita al hotel para alquileres de 3 días o más.
- Sin muñequeras, rodilleras ni coderas.

### Bicicleta

- Casco infantil incluido.
- Candado incluido.
- Sin depósito.
- Sin muñequeras, rodilleras ni coderas.

### Inline skates / roller skates / skateboard / longboard

- Sin depósito.
- Casco infantil incluido.
- Muñequeras incluidas.
- Rodilleras incluidas.
- Coderas incluidas.

---

## 7. Reglas para auditorías Codex

Este archivo puede utilizarse como referencia únicamente para comprobar datos globales expresamente definidos en él.

Si un HTML contradice un dato definido aquí, clasificarlo como error verificado y mostrar:

- archivo;
- idioma;
- valor actual;
- valor canónico;
- contexto;
- impacto;
- corrección recomendada.

Si dos HTML contienen valores diferentes y este archivo NO define cuál es correcto:

```text
INCOHERENCIA CONFIRMADA — REQUIERE FUENTE CANÓNICA
```

No inventar el valor esperado.

Si una propiedad no existe en este archivo, no asumir que debe existir ni inventar su valor.

---

## 8. Datos no definidos por este documento

Este archivo **no establece por sí solo**:

- precios específicos de cada servicio o duración;
- política completa de reservas;
- porcentajes de pago de reserva;
- política completa de cancelación;
- edades mínimas;
- requisitos completos de licencia/documentación;
- disponibilidad concreta;
- tallas;
- fechas editoriales de artículos;
- fechas `dateModified` específicas de cada página.

Si una auditoría necesita decidir cuál de dos valores es correcto para alguno de estos puntos y no puede demostrarse desde los propios HTML:

```text
REQUIERE FUENTE CANÓNICA
```

---

## 9. Resumen compacto para agentes

```text
Nombre: RSB Rental Scooter Barcelona
Nombre alternativo: RSB
Web global: https://rentalscooterbarcelona.com/

Dirección: Carrer de Salvador Espriu, 63
Código postal: 08005
Ciudad: Barcelona
Región: Catalonia
País Schema: ES
Zona: Vila Olímpica del Poblenou

Teléfono visible / Schema: +34 640 559 468
Teléfono E.164: +34640559468
WhatsApp: https://wa.me/34640559468
Email: info@rentalscooterbarcelona.com

Coordenadas: 41.3906488, 2.1984312
NO usar: 41.390577, 2.198362

Google Maps CID: 912877649802486634
Google Maps: https://www.google.com/maps?cid=912877649802486634
Apple Maps Place ID: IA5C7938C1925731A
Bing Maps YPID: YND84466019C726C1

Horario todos los días:
10:30-13:30
16:30-20:00

Rating: 4.6
Review count: 226
bestRating: 5
worstRating: 1
Moneda: EUR

Organization @id:
https://rentalscooterbarcelona.com/#organization

WebSite @id:
https://rentalscooterbarcelona.com/#website

LocalBusiness @id:
https://rentalscooterbarcelona.com/#business
```

---

## 10. Regla final

**Datos globales definidos aquí = deben ser coherentes.**

**Datos de página = deben ser específicos de cada URL e idioma.**

**Dato no definido aquí = no inventar.**
