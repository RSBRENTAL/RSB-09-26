# Auditoría HTML — 07_SKATEBOARD

2026-09-09. Diez idiomas. Fuente: ZIP adjunto y CANONICAL.md. HTML original sin modificar.

## A. INVENTARIO DE ARCHIVOS

| Idioma | Archivo original | Bytes | Líneas | SHA-256 |
| --- | --- | --- | --- | --- |
| en | skateboard/index.html | 72370 | 1103 | 77c1e777c12704368bbd5683d8c007dfa53d97eb8d5e6cb0712252ea49ac00c1 |
| es | es/skateboard/index.html | 73916 | 1090 | 983e032109d220c5b6da7c2b32834909139ca4d9fc7138f468c96352c9bb6510 |
| fr | fr/skateboard/index.html | 73761 | 1033 | cf2850b43261c2a79f77d3f4f54aa5e6bfb503fa249eedb6cefdd1405788b4cb |
| it | it/skateboard/index.html | 73206 | 1042 | b6a43c4c7273f64ceb87c459095cc24d100be5d6d9c77182fc971810a2baa794 |
| de | de/skateboard/index.html | 73309 | 1064 | 156c01685892e6828d339eef25793c06b5306d3d9215eae76bd788d495b43252 |
| nl | nl/skateboard/index.html | 72203 | 1073 | 6a1f27d342064742811201a9fcd83674195fb56eb694c3e4a7102f53b2d9dabd |
| pt | pt/skateboard/index.html | 73866 | 1065 | 93b6d5e2d2a1d23e7e6c920cbcb8c3946f8361d3f243e4cf232170ae25f959d3 |
| ca | cat/skateboard/index.html | 73438 | 1049 | 7aa6800e08afad28dedbb1fab25a04ae23b4f11161a8e692f25e0ce8a2f86543 |
| sv | sv/skateboard/index.html | 71948 | 1059 | a0e07aaeeb4db861141c17ac484806a227130cb3cd215a4dfeb8b464ed1cb332 |
| pl | pl/skateboard/index.html | 74227 | 1114 | 60245c0f6cffdbd0ce8ce9ddc01b907e20acd2a161756fc960d18075399aa21a |

## B. MÉTODOS REALMENTE EJECUTADOS

Lectura completa de 10 fuentes, tokenización HTML, parser lxml, análisis de todos los JSON-LD, extracción del head, entidades, precios, FAQ, reseñas, políticas y enlaces. Segunda pasada independiente directamente sobre los ZIP originales: 23 controles por HTML. Comprobación de sintaxis del JavaScript inline, sin ejecutarlo. Cruce de tarifas con PRICES y de enlaces con los 200 HTML. Inspección de párrafos de guía DE/NL. Sin acceso al sitio publicado, validación externa de normativa o ejecución de recursos remotos.

## C. RESULTADO GLOBAL

| Idioma | Errores confirmados | Segunda pasada: controles superados |
| --- | --- | --- |
| en | U03 | 22/23 |
| es | U03 | 22/23 |
| fr | U03 | 22/23 |
| it | U03 | 22/23 |
| de | U03 | 22/23 |
| nl | U03, U05 | 22/23 |
| pt | U03 | 22/23 |
| ca | U03 | 22/23 |
| sv | U03 | 22/23 |
| pl | U03 | 22/23 |

## D. ERRORES CRÍTICOS

Ninguno demostrado en el alcance estático.

## E. ERRORES ALTOS

Ninguno demostrado en el alcance estático.

## F. ERRORES MEDIOS

#### ca

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/cat/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 136 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 503 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### de

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 137 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 511 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### en

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 169 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 569 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### es

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/es/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 166 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 563 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### fr

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/fr/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 137 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 504 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### it

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/it/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 136 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 503 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### nl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 520 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pl/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 169 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 577 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pt

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pt/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 520 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### sv

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/sv/skateboard/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 520 del HTML original:

```html
"dateModified": "2026-08-24"
```

## G. ERRORES BAJOS

#### nl

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de enlace a la guía

**Actual:** Elke dag geopend: 10:30–13:30 en 16:30–20:00. We bieden verhuur per uur en per dag. Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze gids voor skateboard huren in Barcelona.

**Corrección propuesta:** Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze &lt;a href="https://rentalscooterbarcelona.com/nl/blog/skateboard/"&gt;gids voor skateboard huren in Barcelona&lt;/a&gt; lezen.&lt;/p&gt;

**Motivo:** La construcción modal queda sin infinitivo final.

**Impacto:** Frase incompleta en alemán/neerlandés.

**Estado:** CORRECCIÓN DEFINIDA. Una inserción de lezen al final del enlace; conservar URL.

Línea 804 del HTML original:

```html
Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze <a href="https://rentalscooterbarcelona.com/nl/blog/skateboard/">gids voor skateboard huren in Barcelona</a>.</p>
```

## H. INCOHERENCIAS QUE REQUIEREN FUENTE CANÓNICA

U03: fecha de modificación real por idioma. Los dos valores están documentados; CANONICAL no permite elegir uno.

Los datos de identidad, dirección, horario, mapas y equipamiento ya están definidos: no requieren nueva confirmación. Las tarifas y tallas documentadas no equivalen a una certificación externa de vigencia.

## I. MEJORAS RECOMENDADAS

# Mejoras opcionales — 07_SKATEBOARD

Explicitar el idioma activo con aria-current en los selectores estáticos. Es una mejora de orientación; los enlaces ya apuntan al idioma correcto.

Mantener sincronizados tarjetas, resumen de tarifas, PRICES y Offer cuando cambien precios. Los importes actuales coinciden. Ampliar condiciones comerciales únicamente con información operativa autorizada.

Revisión visual, imágenes, recortes, resolución y tamaños: aplazada expresamente.

## J. OPCIONALES

Unificar plantillas de datos para evitar divergencias futuras entre idiomas y bloques JSON-LD. No fusionar IDs distintos de servicios ni localizar las entidades globales.

## K. MATRIZ COMPLETA DEL HEAD

### en

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Skateboard Rental Barcelona Near Port Olímpic | RSB</title>
<meta content="Rent skateboards and cruiser boards near Port Olímpic and Barceloneta. A children’s helmet, protective gear, free luggage storage and local tips are included." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Skateboard Rental Barcelona Near Port Olímpic | RSB" property="og:title"/>
<meta content="Rent skateboards and cruiser boards near Port Olímpic and Barceloneta. A children’s helmet, protective gear, free luggage storage and local tips are included." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Skateboard rental in Barcelona near Vila Olímpica and Barceloneta Beach" property="og:image:alt"/>
<meta content="en_GB" property="og:locale"/>
<meta content="es_ES" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="nl_NL" property="og:locale:alternate"/>
<meta content="pt_PT" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Skateboard Rental Barcelona Near Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Rent skateboards and cruiser boards near Port Olímpic and Barceloneta. A children’s helmet, protective gear, free luggage storage and local tips are included." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Skateboard rental in Barcelona near Vila Olímpica and Barceloneta Beach" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Use global site styles -->
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "booking",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "en",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/skateboard/",
      "name": "Skateboard Rental Barcelona Near Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "en",
      "description": "Rent skateboards and cruiser boards near Port Olímpic and Barceloneta. A children’s helmet, protective gear, free luggage storage and local tips are included.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "potentialAction": {
        "@type": "CommunicateAction",
        "name": "WhatsApp booking",
        "target": "https://wa.me/34640559468"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://rentalscooterbarcelona.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Skateboard rental",
          "item": "https://rentalscooterbarcelona.com/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
        "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "booking",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "brand": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#service",
      "serviceType": "Skateboard and cruiser board rental",
      "name": "Skateboard and cruiser board rental in Barcelona",
      "url": "https://rentalscooterbarcelona.com/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Rent skateboards and cruiser boards from our local shop near Barceloneta Beach and Port Olímpic. A children's helmet, wrist guards, knee pads and elbow pads are included, and our team can help you choose the right board for a relaxed ride or a casual session.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Skateboard rental price range",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Skateboard rental 1 hour",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Skateboard rental 2 hours",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Skateboard rental 3 hours",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Skateboard rental full day",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Skateboard rental 24 hours",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Skateboard rental extra day",
          "url": "https://rentalscooterbarcelona.com/skateboard/",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Do I need experience to rent a skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started."
          }
        },
        {
          "@type": "Question",
          "name": "Is protective gear included with the rental?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental."
          }
        },
        {
          "@type": "Question",
          "name": "Where can I ride a skateboard near the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby."
          }
        },
        {
          "@type": "Question",
          "name": "Do you have skateboards for beginners?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need a licence to rent a skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID."
          }
        },
        {
          "@type": "Question",
          "name": "Can I store my bag or luggage at the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride."
          }
        },
        {
          "@type": "Question",
          "name": "How do I book or contact you?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "You can book via WhatsApp, email or phone. Contact us if you want to confirm board availability or the best time to collect your skateboard."
          }
        }
      ],
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#service-list",
      "name": "Main rental services in Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Scooter rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Inline skates rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Bike rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Roller skate rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Skateboard rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Longboard rental in Barcelona",
            "url": "https://rentalscooterbarcelona.com/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7SMLHCNGK');
</script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Quick and easy! Light on the paperwork, and open on Sundays. Bikes, scooters, skateboards, rollerblades. Small shop has it all!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2018-10-11"
    }
  ]
}
</script>

```

### es

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Alquiler de skateboard en Barcelona | Cruiser | RSB</title>
<meta name="description" content="Alquiler de skateboard y tablas cruiser en Barcelona, en la Vila Olímpica. Tablas para principiantes y rutas cerca de Port Olímpic y Barceloneta.">
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/es/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta property="og:title" content="Alquiler de skateboard en Barcelona | Cruiser | RSB">
<meta property="og:description" content="Alquiler de skateboard y tablas cruiser en Barcelona, en la Vila Olímpica. Tablas para principiantes y rutas cerca de Port Olímpic y Barceloneta.">
<meta content="https://rentalscooterbarcelona.com/es/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Alquiler de skateboard en Barcelona cerca de la Vila Olímpica y la playa de la Barceloneta" property="og:image:alt"/>
<meta content="es_ES" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="nl_NL" property="og:locale:alternate"/>
<meta content="pt_PT" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="Alquiler de skateboard en Barcelona | Cruiser | RSB">
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta name="twitter:description" content="Alquiler de skateboard y tablas cruiser en Barcelona, en la Vila Olímpica. Tablas para principiantes y rutas cerca de Port Olímpic y Barceloneta.">
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Alquiler de skateboard en Barcelona cerca de la Vila Olímpica y la playa de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de skateboards, tablas cruiser, scooters, bicicletas, patines en línea, patines de 4 ruedas y longboards cerca del Port Olímpic y la playa de la Barceloneta. Casco infantil y protecciones incluidos con el alquiler de skateboard. Consigna gratuita y recomendaciones de rutas.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "booking",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "es",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/es/skateboard/",
      "name": "Alquiler de skateboard en Barcelona | Cruiser | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "es",
      "description": "Alquiler de skateboard y tablas cruiser en Barcelona, en la Vila Olímpica. Tablas para principiantes y rutas cerca de Port Olímpic y Barceloneta.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/es/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "potentialAction": {
        "@type": "CommunicateAction",
        "name": "Reserva por WhatsApp",
        "target": "https://wa.me/34640559468"
      },
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Inicio",
          "item": "https://rentalscooterbarcelona.com/es/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Alquiler de skateboard",
          "item": "https://rentalscooterbarcelona.com/es/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de skateboards, tablas cruiser, scooters, bicicletas, patines en línea, patines de 4 ruedas y longboards cerca del Port Olímpic y la playa de la Barceloneta. Casco infantil y protecciones incluidos con el alquiler de skateboard. Consigna gratuita y recomendaciones de rutas.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "booking",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#service",
      "serviceType": "Alquiler de skateboard y tablas cruiser",
      "name": "Alquiler de skateboard y tablas cruiser en Barcelona",
      "url": "https://rentalscooterbarcelona.com/es/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Alquila skateboards y tablas cruiser en nuestra tienda local cerca de la playa de la Barceloneta y el Port Olímpic. Incluimos casco infantil, hay protecciones incluidas, y nuestro equipo puede ayudarte a elegir la tabla adecuada para un paseo tranquilo o una sesión informal.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Rango de precios del alquiler de skateboard",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Alquiler de skateboard 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Alquiler de skateboard 2 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Alquiler de skateboard 3 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Alquiler de skateboard día completo",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Alquiler de skateboard 24 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Alquiler de skateboard día extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Necesito experiencia para alquilar un skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no necesitas experiencia previa. Alquilamos skateboards a principiantes y personas con experiencia, y nuestro equipo puede ayudarte a elegir una tabla cómoda para empezar."
          }
        },
        {
          "@type": "Question",
          "name": "¿Está incluido el equipo de protección?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas."
          }
        },
        {
          "@type": "Question",
          "name": "¿Dónde puedo usar un skateboard cerca de la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nuestra tienda está cerca del paseo marítimo, el Port Olímpic y zonas abiertas donde muchos visitantes empiezan con una ruta tranquila antes de explorar otros espacios aptos para skate."
          }
        },
        {
          "@type": "Question",
          "name": "¿Tenéis skateboards para principiantes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Podemos ayudarte a elegir un skateboard estable o una tabla cruiser según tu experiencia y el tipo de ruta que quieras hacer."
          }
        },
        {
          "@type": "Question",
          "name": "¿Necesito carnet para alquilar un skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido."
          }
        },
        {
          "@type": "Question",
          "name": "¿Puedo dejar mi mochila o equipaje en la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Ofrecemos consigna gratuita para chaquetas, mochilas y maletas en nuestra tienda supervisada mientras ruedas."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cómo reservo o contacto con vosotros?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard."
          }
        }
      ],
      "inLanguage": "es"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#service-list",
      "name": "Servicios de alquiler principales en Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Alquiler de scooters en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Alquiler de patines en línea en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Alquiler de bicicletas en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Alquiler de patines de 4 ruedas en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Alquiler de skateboard en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Alquiler de longboard en Barcelona",
            "url": "https://rentalscooterbarcelona.com/es/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/es/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Claudia Montes"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Excelente servicio, además está al lado del paseo marítimo, si quieres disfrutar Barcelona en ruedas aquí encuentras bicis, patines, patinetas, scooters. Tamnbien tienen patines y bicis para niños.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### fr

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Location de skateboard à Barcelone | RSB</title>
<meta content="Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/fr/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Location de Skateboard à Barcelone | Cruiser près du Port Olímpic | RSB" property="og:title"/>
<meta content="Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/fr/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Location de skateboard à Barcelone près de la Vila Olímpica et de la plage de la Barceloneta" property="og:image:alt"/>
<meta content="fr_FR" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Location de Skateboard à Barcelone | Cruiser près du Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Location de skateboard à Barcelone près de la Vila Olímpica et de la plage de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<noscript></noscript>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant des skateboards, planches cruiser, scooters, vélos, rollers en ligne, patins à roulettes et longboards près du Port Olímpic et de la plage de la Barceloneta. Casque pour enfant et protections inclus avec la location de skateboard. Consigne gratuite et recommandations d’itinéraires.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "fr"
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/fr/skateboard/",
      "name": "Location de Skateboard à Barcelone | Cruiser près du Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "fr",
      "description": "Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Accueil",
          "item": "https://rentalscooterbarcelona.com/fr/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Location de skateboard",
          "item": "https://rentalscooterbarcelona.com/fr/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant des skateboards, planches cruiser, scooters, vélos, rollers en ligne, patins à roulettes et longboards près du Port Olímpic et de la plage de la Barceloneta. Casque pour enfant et protections inclus avec la location de skateboard. Consigne gratuite et recommandations d’itinéraires.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service",
      "serviceType": "Location de skateboard et de planches cruiser",
      "name": "Location de skateboard et de planches cruiser à Barcelone",
      "url": "https://rentalscooterbarcelona.com/fr/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Location de skateboard 1 heure",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Location de skateboard 2 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Location de skateboard 3 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Location de skateboard journée complète",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Location de skateboard 24 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Location de skateboard journée supplémentaire",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Faut-il de l’expérience pour louer un skateboard ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer."
          }
        },
        {
          "@type": "Question",
          "name": "Les protections sont-elles incluses ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard."
          }
        },
        {
          "@type": "Question",
          "name": "Où puis-je faire du skateboard près de la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Notre boutique est proche de la promenade maritime, du Port Olímpic et d’espaces ouverts où beaucoup de visiteurs commencent tranquillement avant d’explorer d’autres zones adaptées au skate."
          }
        },
        {
          "@type": "Question",
          "name": "Avez-vous des skateboards pour débutants ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité."
          }
        },
        {
          "@type": "Question",
          "name": "Faut-il un permis pour louer un skateboard ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide."
          }
        },
        {
          "@type": "Question",
          "name": "Puis-je laisser mon sac ou mes bagages à la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Une consigne gratuite pour vestes, sacs à dos et bagages est disponible dans notre boutique surveillée pendant votre sortie."
          }
        },
        {
          "@type": "Question",
          "name": "Puis-je réserver ou poser des questions par WhatsApp ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait."
          }
        },
        {
          "@type": "Question",
          "name": "Comment réserver ou vous contacter ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vous pouvez réserver par WhatsApp, email ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des planches ou le meilleur moment pour récupérer votre skateboard."
          }
        }
      ],
      "inLanguage": "fr"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service-list",
      "name": "Principaux services de location à Barcelone",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Location de scooters à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Location de patins en ligne à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Location de vélos à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Location de patins à roulettes à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Location de skateboard à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Location de longboard à Barcelone",
            "url": "https://rentalscooterbarcelona.com/fr/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Claudia Montes"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Excellent service, et en plus la boutique est à côté de la promenade maritime. Si vous voulez profiter de Barcelone sur des roues, vous y trouverez des vélos, des patins, des skateboards et des scooters. Ils ont aussi des patins et des vélos pour enfants.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### it

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Noleggio skateboard a Barcellona | RSB</title>
<meta content="Noleggio skateboard a Barcellona vicino a Port Olímpic e Barceloneta. Cruiser board, casco bambino, protezioni incluse e consigli." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/it/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Noleggio Skateboard a Barcellona | Cruiser vicino al Port Olímpic | RSB" property="og:title"/>
<meta content="Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/it/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Noleggio skateboard a Barcellona vicino alla Vila Olímpica e alla spiaggia della Barceloneta" property="og:image:alt"/>
<meta content="it_IT" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Noleggio Skateboard a Barcellona | Cruiser vicino al Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Noleggio skateboard a Barcellona vicino alla Vila Olímpica e alla spiaggia della Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con skateboard, tavole cruiser, scooter, biciclette, pattini in linea, pattini a rotelle e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Casco per bambini e protezioni inclusi con il noleggio skateboard. Deposito bagagli gratuito e consigli sui percorsi.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "it"
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/it/skateboard/",
      "name": "Noleggio Skateboard a Barcellona | Cruiser vicino al Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "it",
      "description": "Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/it/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Inizio",
          "item": "https://rentalscooterbarcelona.com/it/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Noleggio skateboard",
          "item": "https://rentalscooterbarcelona.com/it/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con skateboard, tavole cruiser, scooter, biciclette, pattini in linea, pattini a rotelle e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Casco per bambini e protezioni inclusi con il noleggio skateboard. Deposito bagagli gratuito e consigli sui percorsi.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#service",
      "serviceType": "Noleggio skateboard e tavole cruiser",
      "name": "Noleggio skateboard e tavole cruiser a Barcellona",
      "url": "https://rentalscooterbarcelona.com/it/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Noleggio skateboard 1 ora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Noleggio skateboard 2 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Noleggio skateboard 3 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Noleggio skateboard giornata intera",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Noleggio skateboard 24 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Noleggio skateboard giorno extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Serve esperienza per noleggiare uno skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare."
          }
        },
        {
          "@type": "Question",
          "name": "Le protezioni sono incluse nel noleggio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse."
          }
        },
        {
          "@type": "Question",
          "name": "Dove posso andare in skateboard vicino al negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Il nostro negozio è vicino al lungomare, al Port Olímpic e a spazi aperti dove molti visitatori iniziano con un giro tranquillo prima di esplorare altri spot adatti allo skate."
          }
        },
        {
          "@type": "Question",
          "name": "Avete skateboard per principianti?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Possiamo aiutarti a scegliere uno skateboard stabile o un cruiser board in base alla tua esperienza e al tipo di giro che vuoi fare."
          }
        },
        {
          "@type": "Question",
          "name": "Serve una patente per noleggiare uno skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso lasciare borsa o bagagli in negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri."
          }
        },
        {
          "@type": "Question",
          "name": "Posso prenotare o fare domande su WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare disponibilità, fare domande o organizzare l’orario di ritiro."
          }
        },
        {
          "@type": "Question",
          "name": "Come prenoto o vi contatto?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle tavole o il momento migliore per ritirare il tuo skateboard."
          }
        }
      ],
      "inLanguage": "it"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#service-list",
      "name": "Principali servizi di noleggio a Barcellona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Noleggio scooter a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Noleggio pattini in linea a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Noleggio biciclette a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Noleggio pattini a rotelle a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Noleggio skateboard a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Noleggio longboard a Barcellona",
            "url": "https://rentalscooterbarcelona.com/it/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/it/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Claudia Montes"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Servizio eccellente, inoltre il negozio è accanto al lungomare. Se vuoi goderti Barcellona su ruote, qui trovi biciclette, pattini, skateboard e scooter. Hanno anche pattini e biciclette per bambini.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### de

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Skateboard mieten in Barcelona | RSB</title>
<meta content="Skateboard mieten in Barcelona nahe Port Olímpic und Barceloneta. Cruiserboards, Kinderhelm, Schutzausrüstung inklusive und Routentipps." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/de/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/><meta content="de_DE" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Skateboard mieten in Barcelona | Cruiserboards nahe Port Olímpic | RSB" property="og:title"/>
<meta content="Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/de/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Skateboard-Verleih in Barcelona nahe Vila Olímpica und Barceloneta-Strand" property="og:image:alt"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Skateboard mieten in Barcelona | Cruiserboards nahe Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Skateboard-Verleih in Barcelona nahe Vila Olímpica und Barceloneta-Strand" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Skateboards, Cruiserboards, Scootern, Fahrrädern, Inlineskates, Rollschuhen und Longboards nahe Port Olímpic und Barceloneta-Strand. Kinderhelm und Schutzausrüstung sind beim Skateboard-Verleih inklusive. Kostenlose Gepäckaufbewahrung und lokale Routentipps.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "Kundenservice",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "de",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/de/skateboard/",
      "name": "Skateboard mieten in Barcelona | Cruiserboards nahe Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "de",
      "description": "Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/de/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/de/skateboard/#breadcrumb"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Startseite",
          "item": "https://rentalscooterbarcelona.com/de/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Skateboard-Verleih",
          "item": "https://rentalscooterbarcelona.com/de/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Skateboards, Cruiserboards, Scootern, Fahrrädern, Inlineskates, Rollschuhen und Longboards nahe Port Olímpic und Barceloneta-Strand. Kinderhelm und Schutzausrüstung sind beim Skateboard-Verleih inklusive. Kostenlose Gepäckaufbewahrung und lokale Routentipps.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Kartenzahlung akzeptiert. PayPal für Online-Zahlungen verfügbar.",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Strand von Barceloneta"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "Kundenservice",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#service",
      "serviceType": "Skateboard- und Cruiser-Board-Verleih",
      "name": "Skateboard- und Cruiser-Board-Verleih in Barcelona",
      "url": "https://rentalscooterbarcelona.com/de/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Strand von Barceloneta"
        }
      ],
      "description": "Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Skateboard-Verleih 1 Stunde",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Skateboard-Verleih 2 Stunden",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Skateboard-Verleih 3 Stunden",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Skateboard-Verleih ganzer Tag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Skateboard-Verleih 24 Stunden",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Skateboard-Verleih Zusatztag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Brauche ich Erfahrung, um ein Skateboard zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein, du brauchst keine Vorerfahrung. Wir vermieten Skateboards an Anfänger und erfahrene Skater, und unser Team hilft dir, ein komfortables Board für den Einstieg zu wählen."
          }
        },
        {
          "@type": "Question",
          "name": "Ist Schutzausrüstung in der Miete enthalten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive."
          }
        },
        {
          "@type": "Question",
          "name": "Wo kann ich in der Nähe des Shops Skateboard fahren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Unser Shop liegt nahe der Strandpromenade, dem Port Olímpic und offenen Flächen, wo viele Besucher entspannt starten, bevor sie weitere geeignete Bereiche zum Skaten in der Nähe erkunden."
          }
        },
        {
          "@type": "Question",
          "name": "Habt ihr Skateboards für Anfänger?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Wir helfen dir, je nach Erfahrung und gewünschter Fahrt ein stabiles Skateboard oder Cruiserboard auszuwählen."
          }
        },
        {
          "@type": "Question",
          "name": "Brauche ich einen Führerschein, um ein Skateboard zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck ist in unserem betreuten Shop möglich, während du fährst."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich per WhatsApp buchen oder Fragen stellen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um die Verfügbarkeit zu bestätigen, Fragen zu stellen oder deine Abholzeit zu vereinbaren."
          }
        },
        {
          "@type": "Question",
          "name": "Wie buche ich oder kontaktiere euch?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Board-Verfügbarkeit oder den besten Abholzeitpunkt bestätigen möchtest."
          }
        }
      ],
      "inLanguage": "de"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#service-list",
      "name": "Wichtigste Verleihservices in Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Scooter-Verleih in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Inlineskates-Verleih in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Fahrradverleih in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Rollschuhe mieten in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Skateboard-Verleih in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Longboard-Verleih in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/de/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Schnell und unkompliziert! Wenig Papierkram und sonntags geöffnet. Fahrräder, Scooter, Skateboards, Inlineskates. Der kleine Laden hat alles!“\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### nl

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Skateboard huren in Barcelona | RSB</title>
<meta content="Skateboard huren in Barcelona bij Port Olímpic en Barceloneta. Cruiserboards, kinderhelm, beschermers inbegrepen en lokale routetips." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/nl/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Skateboard huren in Barcelona | Cruiserboards bij Port Olímpic | RSB" property="og:title"/>
<meta content="Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/nl/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Skateboard huren in Barcelona bij Vila Olímpica en Barceloneta" property="og:image:alt"/>
<meta content="nl_NL" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/>
<meta content="es_ES" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="pt_PT" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Skateboard huren in Barcelona | Cruiserboards bij Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Skateboard huren in Barcelona bij Vila Olímpica en Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Use global site styles -->
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met skateboards, cruiserboards, scooters, fietsen, inline skates, rolschaatsen en longboards vlak bij Port Olímpic en Barceloneta. Een kinderhelm en bescherming zijn inbegrepen bij skateboardverhuur. Gratis bagageopslag en lokale routetips.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "nl",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/nl/skateboard/",
      "name": "Skateboard huren in Barcelona | Cruiserboards bij Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "nl",
      "description": "Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://rentalscooterbarcelona.com/nl/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Skateboard huren",
          "item": "https://rentalscooterbarcelona.com/nl/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met skateboards, cruiserboards, scooters, fietsen, inline skates, rolschaatsen en longboards vlak bij Port Olímpic en Barceloneta. Een kinderhelm en bescherming zijn inbegrepen bij skateboardverhuur. Gratis bagageopslag en lokale routetips.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service",
      "serviceType": "Skateboard en cruiser board verhuur",
      "name": "Skateboard en cruiser board huren in Barcelona",
      "url": "https://rentalscooterbarcelona.com/nl/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Skateboard huren 1 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Skateboard huren 2 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Skateboard huren 3 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Skateboard huren hele dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Skateboard huren 24 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Skateboard huren extra dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Heb ik ervaring nodig om een skateboard te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, je hebt geen ervaring nodig. We verhuren skateboards aan beginners en ervaren skaters, en ons team helpt je een comfortabel board te kiezen om te starten."
          }
        },
        {
          "@type": "Question",
          "name": "Is bescherming inbegrepen bij de huur?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen."
          }
        },
        {
          "@type": "Question",
          "name": "Waar kan ik skateboarden in de buurt van de shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Onze shop ligt dicht bij de boulevard, Port Olímpic en open ruimtes waar veel bezoekers rustig beginnen voordat ze meer skatevriendelijke plekken in de buurt ontdekken."
          }
        },
        {
          "@type": "Question",
          "name": "Hebben jullie skateboards voor beginners?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. We kunnen je helpen een stabiel skateboard of cruiser board te kiezen, afhankelijk van je ervaring en het soort rit dat je wilt."
          }
        },
        {
          "@type": "Question",
          "name": "Heb ik een rijbewijs nodig om een skateboard te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID."
          }
        },
        {
          "@type": "Question",
          "name": "Kan ik mijn tas of bagage in de shop achterlaten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Gratis opslag voor jassen, rugzakken en bagage is beschikbaar in onze bewaakte shop terwijl je rijdt."
          }
        },
        {
          "@type": "Question",
          "name": "Kan ik reserveren of vragen stellen via WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken."
          }
        },
        {
          "@type": "Question",
          "name": "Hoe reserveer ik of neem ik contact met jullie op?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen."
          }
        }
      ],
      "inLanguage": "nl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service-list",
      "name": "Belangrijkste verhuurdiensten in Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Scooter huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Inline skates huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Fiets huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Rolschaatsen huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Skateboard huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Longboard huren in Barcelona",
            "url": "https://rentalscooterbarcelona.com/nl/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Snel en eenvoudig! Weinig papierwerk en open op zondag. Fietsen, scooters, skateboards, inline skates. De kleine winkel heeft alles!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### pt

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Aluguer de skateboard em Barcelona | RSB</title>
<meta content="Aluguer de skateboard em Barcelona perto de Port Olímpic e Barceloneta. Cruiser boards, capacete infantil, proteções incluídas e rotas." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pt/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Aluguer de Skateboard em Barcelona | Cruiser perto do Port Olímpic | RSB" property="og:title"/>
<meta content="Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pt/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Aluguer de skateboard em Barcelona perto da Vila Olímpica e da praia da Barceloneta" property="og:image:alt"/>
<meta content="pt_PT" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/>
<meta content="es_ES" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="nl_NL" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Aluguer de Skateboard em Barcelona | Cruiser perto do Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Aluguer de skateboard em Barcelona perto da Vila Olímpica e da praia da Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Use global site styles -->
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com skateboards, pranchas cruiser, scooters, bicicletas, patins em linha, patins de 4 rodas e longboards perto do Port Olímpic e da praia da Barceloneta. Capacete infantil e proteções incluídos no aluguer de skateboard. Serviço gratuito de guarda de bagagem e sugestões de percurso.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "pt-PT",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/pt/skateboard/",
      "name": "Aluguer de Skateboard em Barcelona | Cruiser perto do Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "pt-PT",
      "description": "Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Início",
          "item": "https://rentalscooterbarcelona.com/pt/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Aluguer de skateboard",
          "item": "https://rentalscooterbarcelona.com/pt/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com skateboards, pranchas cruiser, scooters, bicicletas, patins em linha, patins de 4 rodas e longboards perto do Port Olímpic e da praia da Barceloneta. Capacete infantil e proteções incluídos no aluguer de skateboard. Serviço gratuito de guarda de bagagem e sugestões de percurso.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service",
      "serviceType": "Aluguer de skateboard e pranchas cruiser",
      "name": "Aluguer de skateboard e pranchas cruiser em Barcelona",
      "url": "https://rentalscooterbarcelona.com/pt/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Aluguer de skateboard 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Aluguer de skateboard 2 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Aluguer de skateboard 3 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Aluguer de skateboard dia completo",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Aluguer de skateboard 24 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Aluguer de skateboard dia extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Preciso de experiência para alugar um skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar."
          }
        },
        {
          "@type": "Question",
          "name": "O equipamento de proteção está incluído?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas."
          }
        },
        {
          "@type": "Question",
          "name": "Onde posso andar de skateboard perto da loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A nossa loja fica perto do passeio marítimo, do Port Olímpic e de espaços abertos onde muitos visitantes começam com uma volta tranquila antes de explorar outros spots próximos adequados para skate."
          }
        },
        {
          "@type": "Question",
          "name": "Têm skateboards para principiantes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Podemos ajudar-te a escolher um skateboard estável ou um cruiser board conforme a tua experiência e o tipo de passeio que procuras."
          }
        },
        {
          "@type": "Question",
          "name": "Preciso de carta para alugar um skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso deixar a minha mochila ou bagagem na loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas."
          }
        },
        {
          "@type": "Question",
          "name": "Posso reservar ou fazer perguntas por WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento."
          }
        },
        {
          "@type": "Question",
          "name": "Como faço a reserva ou contacto convosco?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard."
          }
        }
      ],
      "inLanguage": "pt-PT"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service-list",
      "name": "Principais serviços de aluguer em Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Aluguer de scooters em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Aluguer de patins em linha em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Aluguer de bicicletas em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Aluguer de patins de 4 rodas em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Aluguer de skateboard em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Aluguer de longboard em Barcelona",
            "url": "https://rentalscooterbarcelona.com/pt/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Rápido e fácil! Pouca burocracia e aberto aos domingos. Bicicletas, scooters, skates, patins em linha. A pequena loja tem tudo!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### ca

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Lloguer de skateboard a Barcelona | RSB</title>
<meta content="Lloga skateboards i cruiser boards a Barcelona prop de Port Olímpic i Barceloneta. Casc infantil, proteccions incloses i rutes locals." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/cat/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Lloguer de Skateboard a Barcelona | Cruiser prop del Port Olímpic | RSB" property="og:title"/>
<meta content="Lloga skateboards i taules cruiser a Barcelona, a prop del Port Olímpic i de la platja de la Barceloneta. La nostra botiga a la Vila Olímpica ofereix taules de qualitat per a principiants i persones amb experiència, casc infantil inclòs, proteccions incloses, servei gratuït de guarda d’equipatge i consells de ruta." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/cat/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Lloguer de skateboard a Barcelona prop de la Vila Olímpica i la platja de la Barceloneta" property="og:image:alt"/>
<meta content="ca_ES" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Lloguer de Skateboard a Barcelona | Cruiser prop del Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Lloga skateboards i taules cruiser a Barcelona, a prop del Port Olímpic i de la platja de la Barceloneta. La nostra botiga a la Vila Olímpica ofereix taules de qualitat per a principiants i persones amb experiència, casc infantil inclòs, proteccions incloses, servei gratuït de guarda d’equipatge i consells de ruta." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Lloguer de skateboard a Barcelona prop de la Vila Olímpica i la platja de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de skateboards, taules cruiser, scooters, bicicletes, patins en línia, patins de 4 rodes i longboards a prop del Port Olímpic i de la platja de la Barceloneta. Casc infantil i proteccions inclosos amb el lloguer de skateboard. Servei gratuït de guarda d’equipatge i recomanacions de rutes.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "ca"
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/cat/skateboard/",
      "name": "Lloguer de Skateboard a Barcelona | Cruiser prop del Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "ca",
      "description": "Lloga skateboards i taules cruiser a Barcelona, a prop del Port Olímpic i de la platja de la Barceloneta. La nostra botiga a la Vila Olímpica ofereix taules de qualitat per a principiants i persones amb experiència, casc infantil inclòs, proteccions incloses, servei gratuït de guarda d’equipatge i consells de ruta.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Inici",
          "item": "https://rentalscooterbarcelona.com/cat/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Lloguer de skateboard",
          "item": "https://rentalscooterbarcelona.com/cat/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de skateboards, taules cruiser, scooters, bicicletes, patins en línia, patins de 4 rodes i longboards a prop del Port Olímpic i de la platja de la Barceloneta. Casc infantil i proteccions inclosos amb el lloguer de skateboard. Servei gratuït de guarda d’equipatge i recomanacions de rutes.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Credit Card, Debit Card, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "customer service",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service",
      "serviceType": "Lloguer de skateboard i taules cruiser",
      "name": "Lloguer de skateboard i taules cruiser a Barcelona",
      "url": "https://rentalscooterbarcelona.com/cat/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta Beach"
        }
      ],
      "description": "Lloga skateboards i taules cruiser a la nostra botiga local, a prop de la platja de la Barceloneta i del Port Olímpic. Incloem casc infantil, hi ha proteccions incloses, i el nostre equip et pot ajudar a triar la taula adequada per a una passejada tranquil·la o una sessió informal.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Lloguer de skateboard 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Lloguer de skateboard 2 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Lloguer de skateboard 3 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Lloguer de skateboard dia complet",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Lloguer de skateboard 24 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Lloguer de skateboard dia extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Necessito experiència per llogar un skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no necessites experiència prèvia. Lloguem skateboards a principiants i persones amb experiència, i el nostre equip pot ajudar-te a triar una taula còmoda per començar."
          }
        },
        {
          "@type": "Question",
          "name": "L’equip de protecció està inclòs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses."
          }
        },
        {
          "@type": "Question",
          "name": "On puc anar amb skateboard a prop de la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La nostra botiga és a prop del passeig marítim, el Port Olímpic i zones obertes on molts visitants comencen amb una ruta tranquil·la abans d’explorar altres espais aptes per a skate."
          }
        },
        {
          "@type": "Question",
          "name": "Teniu skateboards per a principiants?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Podem ajudar-te a triar un skateboard estable o un cruiser board segons la teva experiència i el tipus de ruta que vulguis fer."
          }
        },
        {
          "@type": "Question",
          "name": "Necessito carnet per llogar un skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid."
          }
        },
        {
          "@type": "Question",
          "name": "Puc deixar la motxilla o l’equipatge a la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes."
          }
        },
        {
          "@type": "Question",
          "name": "Puc reservar o fer preguntes per WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida."
          }
        },
        {
          "@type": "Question",
          "name": "Com reservo o contacto amb vosaltres?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar disponibilitat de taules o el millor moment per recollir el teu skateboard."
          }
        }
      ],
      "inLanguage": "ca"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service-list",
      "name": "Serveis principals de lloguer a Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Lloguer de scooters a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Lloguer de patins en línia a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Lloguer de bicicletes a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Lloguer de patins de 4 rodes a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Lloguer de skateboard a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Lloguer de longboard a Barcelona",
            "url": "https://rentalscooterbarcelona.com/cat/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Ràpid i fàcil! Poca paperassa i obert els diumenges. Bicicletes, scooters, monopatins i patins en línia. La petita botiga ho té tot!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### sv

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Hyra skateboard i Barcelona | RSB</title>
<meta content="Hyra skateboard i Barcelona nära Port Olímpic och Barceloneta. Cruiserbrädor, barnhjälm, skydd ingår och lokala ruttips." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/sv/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Hyra Skateboard i Barcelona | Cruiserboards nära Port Olímpic | RSB" property="og:title"/>
<meta content="Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/sv/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Skateboarduthyrning i Barcelona nära Vila Olímpica och Barceloneta" property="og:image:alt"/>
<meta content="sv_SE" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/>
<meta content="es_ES" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="nl_NL" property="og:locale:alternate"/>
<meta content="pt_PT" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Hyra Skateboard i Barcelona | Cruiserboards nära Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Skateboarduthyrning i Barcelona nära Vila Olímpica och Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Use global site styles -->
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Lokal uthyrning i Vila Olímpica del Poblenou, Barcelona, med skateboard, cruiserboards, scootrar, cyklar, inlines, rullskridskor och longboards nära Port Olímpic och Barceloneta. Barnhjälm och skydd ingår vid skateboarduthyrning. Gratis bagageförvaring och lokala ruttips.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "kundservice",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "sv",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/sv/skateboard/",
      "name": "Hyra Skateboard i Barcelona | Cruiserboards nära Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "sv",
      "description": "Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Hem",
          "item": "https://rentalscooterbarcelona.com/sv/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Hyra skateboard",
          "item": "https://rentalscooterbarcelona.com/sv/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokal uthyrning i Vila Olímpica del Poblenou, Barcelona, med skateboard, cruiserboards, scootrar, cyklar, inlines, rullskridskor och longboards nära Port Olímpic och Barceloneta. Barnhjälm och skydd ingår vid skateboarduthyrning. Gratis bagageförvaring och lokala ruttips.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Kortbetalning accepteras. PayPal finns för onlinebetalningar.",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta-stranden"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "kundservice",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22",
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service",
      "serviceType": "Skateboard- och cruiserboarduthyrning",
      "name": "Hyra skateboard och cruiserboards i Barcelona",
      "url": "https://rentalscooterbarcelona.com/sv/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "Barceloneta-stranden"
        }
      ],
      "description": "Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Hyra skateboard 1 timme",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Hyra skateboard 2 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Hyra skateboard 3 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Hyra skateboard heldag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Hyra skateboard 24 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Hyra skateboard extra dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Behöver jag erfarenhet för att hyra skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med."
          }
        },
        {
          "@type": "Question",
          "name": "Ingår skyddsutrustning i hyran?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår."
          }
        },
        {
          "@type": "Question",
          "name": "Var kan jag åka skateboard nära butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vår butik ligger nära strandpromenaden, Port Olímpic och öppna ytor där många besökare börjar med en lugn tur innan de utforskar fler skatevänliga platser i närheten."
          }
        },
        {
          "@type": "Question",
          "name": "Har ni skateboards för nybörjare?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Vi kan hjälpa dig att välja en stabil skateboard eller cruiserbräda beroende på din erfarenhet och vilken typ av tur du vill göra."
          }
        },
        {
          "@type": "Question",
          "name": "Behöver jag körkort för att hyra skateboard?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej. Inget körkort krävs för att hyra en skateboard."
          }
        },
        {
          "@type": "Question",
          "name": "Kan jag lämna väska eller bagage i butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Gratis förvaring för jackor, ryggsäckar och bagage finns i vår övervakade butik medan du åker."
          }
        },
        {
          "@type": "Question",
          "name": "Kan jag boka eller ställa frågor via WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid."
          }
        },
        {
          "@type": "Question",
          "name": "Hur bokar jag eller kontaktar er?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard."
          }
        }
      ],
      "inLanguage": "sv"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service-list",
      "name": "Huvudsakliga uthyrningstjänster i Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Hyra scooter i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Hyra inlines i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Hyra cykel i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Hyra rullskridskor i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Hyra skateboard i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Hyra longboard i Barcelona",
            "url": "https://rentalscooterbarcelona.com/sv/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-S7SMLHCNGK');
  </script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Snabbt och enkelt! Lite pappersarbete och öppet på söndagar. Cyklar, scootrar, skateboards och inlines. Den lilla butiken har allt!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

### pl

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Wynajem deskorolek w Barcelonie blisko Port Olímpic | RSB</title>
<meta content="Wynajmij deskorolki i cruisery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy i ochraniacze w cenie, darmowe przechowanie bagażu i lokalne wskazówki." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pl/skateboard/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/skateboard/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/skateboard/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/skateboard/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/skateboard/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/skateboard/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/skateboard/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/skateboard/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/skateboard/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/skateboard/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/skateboard/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Wynajem deskorolek w Barcelonie blisko Port Olímpic | RSB" property="og:title"/>
<meta content="Wynajmij deskorolki i cruisery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy i ochraniacze w cenie, darmowe przechowanie bagażu i lokalne wskazówki." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pl/skateboard/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Wynajem deskorolek w Barcelonie blisko Vila Olímpica i plaży Barceloneta" property="og:image:alt"/>
<meta content="pl_PL" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/>
<meta content="es_ES" property="og:locale:alternate"/>
<meta content="fr_FR" property="og:locale:alternate"/>
<meta content="it_IT" property="og:locale:alternate"/>
<meta content="de_DE" property="og:locale:alternate"/>
<meta content="nl_NL" property="og:locale:alternate"/>
<meta content="pt_PT" property="og:locale:alternate"/>
<meta content="ca_ES" property="og:locale:alternate"/>
<meta content="sv_SE" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Wynajem deskorolek w Barcelonie blisko Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Wynajmij deskorolki i cruisery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy i ochraniacze w cenie, darmowe przechowanie bagażu i lokalne wskazówki." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Wynajem deskorolek w Barcelonie blisko Vila Olímpica i plaży Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/><link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Wynajem" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Użyj globalnych stylów strony -->
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://rentalscooterbarcelona.com/#organization",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "obsługa klienta",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "rezerwacja",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://rentalscooterbarcelona.com/#website",
      "url": "https://rentalscooterbarcelona.com/",
      "name": "RSB Rental Scooter Barcelona",
      "inLanguage": "pl",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage",
      "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
      "name": "Wynajem deskorolek w Barcelonie blisko Port Olímpic",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "pl",
      "description": "Wynajmij deskorolki i cruisery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy i ochraniacze w cenie, darmowe przechowanie bagażu i lokalne wskazówki.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "potentialAction": {
        "@type": "CommunicateAction",
        "name": "WhatsApp rezerwacja",
        "target": "https://wa.me/34640559468"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Strona główna",
          "item": "https://rentalscooterbarcelona.com/pl/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Wynajem deskorolek",
          "item": "https://rentalscooterbarcelona.com/pl/skateboard/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
        "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Karta kredytowa, karta debetowa, PayPal",
      "currenciesAccepted": "EUR",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrer de Salvador Espriu, 63",
        "addressLocality": "Barcelona",
        "addressRegion": "Catalonia",
        "postalCode": "08005",
        "addressCountry": "ES"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 41.3906488,
        "longitude": 2.1984312
      },
      "hasMap": "https://www.google.com/maps?cid=912877649802486634",
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "plaża Barceloneta"
        }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "10:30",
          "closes": "13:30"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
          ],
          "opens": "16:30",
          "closes": "20:00"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "obsługa klienta",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        },
        {
          "@type": "ContactPoint",
          "telephone": "+34 640 559 468",
          "email": "info@rentalscooterbarcelona.com",
          "contactType": "rezerwacja",
          "areaServed": "ES",
          "availableLanguage": [
            "en",
            "es",
            "ca",
            "fr",
            "it",
            "de",
            "nl",
            "pt",
            "sv",
            "pl"
          ]
        }
      ],
      "sameAs": [
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "brand": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service",
      "serviceType": "Wynajem deskorolek i cruiserów",
      "name": "Wynajem deskorolek i cruiserów w Barcelonie",
      "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
      "provider": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "areaServed": [
        {
          "@type": "City",
          "name": "Barcelona"
        },
        {
          "@type": "Place",
          "name": "Vila Olímpica del Poblenou"
        },
        {
          "@type": "Place",
          "name": "Port Olímpic"
        },
        {
          "@type": "Place",
          "name": "plaża Barceloneta"
        }
      ],
      "description": "Wynajmij deskorolki i cruisery w naszej lokalnej wypożyczalni naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy oraz ochraniacze na kolana, łokcie i nadgarstki są w cenie, a nasz zespół pomoże dobrać odpowiednią deskę do spokojnej jazdy lub rekreacyjnej sesji.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Zakres cen wynajmu deskorolek",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Wynajem deskorolek 1 godzina",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Wynajem deskorolek 2 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Wynajem deskorolek 3 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Całodniowy wynajem deskorolek",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Wynajem deskorolek 24 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Dodatkowy dzień wynajmu deskorolek",
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Czy potrzebuję doświadczenia, aby wynająć deskorolkę?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy deskorolki początkującym i pewniejszym osobom, a nasz zespół pomoże wybrać wygodną deskę na start."
          }
        },
        {
          "@type": "Question",
          "name": "Czy sprzęt ochronny jest w cenie wynajmu?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę."
          }
        },
        {
          "@type": "Question",
          "name": "Gdzie mogę jeździć na deskorolce blisko wypożyczalni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym odkrywaniem pobliskich miejsc przyjaznych do jazdy."
          }
        },
        {
          "@type": "Question",
          "name": "Czy macie deskorolki dla początkujących?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Pomożemy wybrać stabilną deskorolkę lub cruisera w zależności od Twojego doświadczenia i rodzaju jazdy, którego szukasz."
          }
        },
        {
          "@type": "Question",
          "name": "Czy potrzebuję prawa jazdy, aby wynająć deskorolkę?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy."
          }
        },
        {
          "@type": "Question",
          "name": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni."
          }
        },
        {
          "@type": "Question",
          "name": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru."
          }
        },
        {
          "@type": "Question",
          "name": "Jak mogę zarezerwować lub skontaktować się z wami?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność deski albo najlepszą godzinę odbioru deskorolki."
          }
        }
      ],
      "inLanguage": "pl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service-list",
      "name": "Główne usługi wynajmu w Barcelonie",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Wynajem skuterów w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Wynajem rolek w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Wynajem rowerów w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/bike/"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "Service",
            "name": "Wynajem wrotek w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/quads/"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "Service",
            "name": "Wynajem deskorolek w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Wynajem longboardu w Barcelonie",
            "url": "https://rentalscooterbarcelona.com/pl/longboard/"
          }
        }
      ]
    }
  ]
}
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-S7SMLHCNGK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7SMLHCNGK');
</script>
<script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage",
      "dateModified": "2026-08-24"
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "sameAs": [
        "https://www.google.com/maps?cid=912877649802486634",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.6",
        "reviewCount": 226,
        "bestRating": 5,
        "worstRating": 1
      },
      "review": [
        {
          "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "TheDoctorIsIn"
      },
      "datePublished": "2018-10-11",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Szybko i łatwo! Mało formalności i otwarte w niedziele. Rowery, skutery, deskorolki i rolki. Ten mały sklep ma wszystko!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    }
  ]
}
</script>

```

## L. MATRIZ CANONICAL/HREFLANG

| Idioma | Canonical | Alternativas completas | Verificación independiente |
| --- | --- | --- | --- |
| en | https://rentalscooterbarcelona.com/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| es | https://rentalscooterbarcelona.com/es/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| fr | https://rentalscooterbarcelona.com/fr/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| it | https://rentalscooterbarcelona.com/it/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| de | https://rentalscooterbarcelona.com/de/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| nl | https://rentalscooterbarcelona.com/nl/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| pt | https://rentalscooterbarcelona.com/pt/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| ca | https://rentalscooterbarcelona.com/cat/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| sv | https://rentalscooterbarcelona.com/sv/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |
| pl | https://rentalscooterbarcelona.com/pl/skateboard/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/skateboard/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/skateboard/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/skateboard/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/skateboard/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "hreflang": "pl", "rel": "alternate"}] | True |

## M. MATRIZ SCHEMA @id + URL

| Idioma | Bloque | Ruta | Entidad completa |
| --- | --- | --- | --- |
| en | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| en | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "en", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/skateboard/", "name": "Skateboard Rental Barcelona Near Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "en", "description": "Rent skateboards and cruiser boards near Port Olímpic and Barceloneta. A children’s helmet, protective gear, free luggage storage and local tips are included.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp booking", "target": "https://wa.me/34640559468"}} |
| en | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/"}, {"@type": "ListItem", "position": 2, "name": "Skateboard rental", "item": "https://rentalscooterbarcelona.com/skateboard/"}]} |
| en | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/skateboard/#service", "serviceType": "Skateboard and cruiser board rental", "name": "Skateboard and cruiser board rental in Barcelona", "url": "https://rentalscooterbarcelona.com/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Rent skateboards and cruiser boards from our local shop near Barceloneta Beach and Port Olímpic. A children's helmet, wrist guards, knee pads and elbow pads are included, and our team can help you choose the right board for a relaxed ride or a casual session.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Skateboard rental price range", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard rental 1 hour", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard rental 2 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard rental 3 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard rental full day", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard rental 24 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard rental extra day", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}]} |
| en | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Do I need experience to rent a skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started."}}, {"@type": "Question", "name": "Is protective gear included with the rental?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental."}}, {"@type": "Question", "name": "Where can I ride a skateboard near the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby."}}, {"@type": "Question", "name": "Do you have skateboards for beginners?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want."}}, {"@type": "Question", "name": "Do I need a licence to rent a skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID."}}, {"@type": "Question", "name": "Can I store my bag or luggage at the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride."}}, {"@type": "Question", "name": "How do I book or contact you?", "acceptedAnswer": {"@type": "Answer", "text": "You can book via WhatsApp, email or phone. Contact us if you want to confirm board availability or the best time to collect your skateboard."}}], "inLanguage": "en"} |
| en | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/skateboard/#service-list", "name": "Main rental services in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter rental in Barcelona", "url": "https://rentalscooterbarcelona.com/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inline skates rental in Barcelona", "url": "https://rentalscooterbarcelona.com/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Bike rental in Barcelona", "url": "https://rentalscooterbarcelona.com/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Roller skate rental in Barcelona", "url": "https://rentalscooterbarcelona.com/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard rental in Barcelona", "url": "https://rentalscooterbarcelona.com/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard rental in Barcelona", "url": "https://rentalscooterbarcelona.com/longboard/"}}]} |
| en | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/skateboard/#webpage", "dateModified": "2026-08-24"} |
| en | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/skateboard/#google-review-1"}]} |
| en | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Quick and easy! Light on the paperwork, and open on Sundays. Bikes, scooters, skateboards, rollerblades. Small shop has it all!\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2018-10-11"} |
| es | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de skateboards, tablas cruiser, scooters, bicicletas, patines en línea, patines de 4 ruedas y longboards cerca del Port Olímpic y la playa de la Barceloneta. Casco infantil y protecciones incluidos con el alquiler de skateboard. Consigna gratuita y recomendaciones de rutas.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| es | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "es", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/es/skateboard/", "name": "Alquiler de skateboard en Barcelona \| Cruiser \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "es", "description": "Alquiler de skateboard y tablas cruiser en Barcelona, en la Vila Olímpica. Tablas para principiantes y rutas cerca de Port Olímpic y Barceloneta.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/es/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/es/skateboard/#faq"}], "dateModified": "2026-07-30", "potentialAction": {"@type": "CommunicateAction", "name": "Reserva por WhatsApp", "target": "https://wa.me/34640559468"}, "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://rentalscooterbarcelona.com/es/"}, {"@type": "ListItem", "position": 2, "name": "Alquiler de skateboard", "item": "https://rentalscooterbarcelona.com/es/skateboard/"}]} |
| es | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de skateboards, tablas cruiser, scooters, bicicletas, patines en línea, patines de 4 ruedas y longboards cerca del Port Olímpic y la playa de la Barceloneta. Casco infantil y protecciones incluidos con el alquiler de skateboard. Consigna gratuita y recomendaciones de rutas.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| es | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#service", "serviceType": "Alquiler de skateboard y tablas cruiser", "name": "Alquiler de skateboard y tablas cruiser en Barcelona", "url": "https://rentalscooterbarcelona.com/es/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Alquila skateboards y tablas cruiser en nuestra tienda local cerca de la playa de la Barceloneta y el Port Olímpic. Incluimos casco infantil, hay protecciones incluidas, y nuestro equipo puede ayudarte a elegir la tabla adecuada para un paseo tranquilo o una sesión informal.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Rango de precios del alquiler de skateboard", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/es/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Alquiler de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Alquiler de skateboard 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Alquiler de skateboard 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Alquiler de skateboard día completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Alquiler de skateboard 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Alquiler de skateboard día extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}]} |
| es | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "¿Necesito experiencia para alquilar un skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No, no necesitas experiencia previa. Alquilamos skateboards a principiantes y personas con experiencia, y nuestro equipo puede ayudarte a elegir una tabla cómoda para empezar."}}, {"@type": "Question", "name": "¿Está incluido el equipo de protección?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas."}}, {"@type": "Question", "name": "¿Dónde puedo usar un skateboard cerca de la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Nuestra tienda está cerca del paseo marítimo, el Port Olímpic y zonas abiertas donde muchos visitantes empiezan con una ruta tranquila antes de explorar otros espacios aptos para skate."}}, {"@type": "Question", "name": "¿Tenéis skateboards para principiantes?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Podemos ayudarte a elegir un skateboard estable o una tabla cruiser según tu experiencia y el tipo de ruta que quieras hacer."}}, {"@type": "Question", "name": "¿Necesito carnet para alquilar un skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido."}}, {"@type": "Question", "name": "¿Puedo dejar mi mochila o equipaje en la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Ofrecemos consigna gratuita para chaquetas, mochilas y maletas en nuestra tienda supervisada mientras ruedas."}}, {"@type": "Question", "name": "¿Cómo reservo o contacto con vosotros?", "acceptedAnswer": {"@type": "Answer", "text": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard."}}], "inLanguage": "es"} |
| es | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#service-list", "name": "Servicios de alquiler principales en Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Alquiler de scooters en Barcelona", "url": "https://rentalscooterbarcelona.com/es/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Alquiler de patines en línea en Barcelona", "url": "https://rentalscooterbarcelona.com/es/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Alquiler de bicicletas en Barcelona", "url": "https://rentalscooterbarcelona.com/es/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Alquiler de patines de 4 ruedas en Barcelona", "url": "https://rentalscooterbarcelona.com/es/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Alquiler de skateboard en Barcelona", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Alquiler de longboard en Barcelona", "url": "https://rentalscooterbarcelona.com/es/longboard/"}}]} |
| es | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#webpage", "dateModified": "2026-08-24"} |
| es | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/es/skateboard/#google-review-1"}]} |
| es | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excelente servicio, además está al lado del paseo marítimo, si quieres disfrutar Barcelona en ruedas aquí encuentras bicis, patines, patinetas, scooters. Tamnbien tienen patines y bicis para niños.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant des skateboards, planches cruiser, scooters, vélos, rollers en ligne, patins à roulettes et longboards près du Port Olímpic et de la plage de la Barceloneta. Casque pour enfant et protections inclus avec la location de skateboard. Consigne gratuite et recommandations d’itinéraires.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| fr | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "fr"} |
| fr | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/fr/skateboard/", "name": "Location de Skateboard à Barcelone \| Cruiser près du Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "fr", "description": "Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/fr/skateboard/#faq"}], "dateModified": "2026-07-30"} |
| fr | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://rentalscooterbarcelona.com/fr/"}, {"@type": "ListItem", "position": 2, "name": "Location de skateboard", "item": "https://rentalscooterbarcelona.com/fr/skateboard/"}]} |
| fr | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant des skateboards, planches cruiser, scooters, vélos, rollers en ligne, patins à roulettes et longboards près du Port Olímpic et de la plage de la Barceloneta. Casque pour enfant et protections inclus avec la location de skateboard. Consigne gratuite et recommandations d’itinéraires.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| fr | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service", "serviceType": "Location de skateboard et de planches cruiser", "name": "Location de skateboard et de planches cruiser à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Louez un skateboard ou une planche cruiser à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Location de skateboard 1 heure", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Location de skateboard 2 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Location de skateboard 3 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Location de skateboard journée complète", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Location de skateboard 24 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Location de skateboard journée supplémentaire", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}]} |
| fr | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Faut-il de l’expérience pour louer un skateboard ?", "acceptedAnswer": {"@type": "Answer", "text": "Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer."}}, {"@type": "Question", "name": "Les protections sont-elles incluses ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard."}}, {"@type": "Question", "name": "Où puis-je faire du skateboard près de la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Notre boutique est proche de la promenade maritime, du Port Olímpic et d’espaces ouverts où beaucoup de visiteurs commencent tranquillement avant d’explorer d’autres zones adaptées au skate."}}, {"@type": "Question", "name": "Avez-vous des skateboards pour débutants ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité."}}, {"@type": "Question", "name": "Faut-il un permis pour louer un skateboard ?", "acceptedAnswer": {"@type": "Answer", "text": "Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide."}}, {"@type": "Question", "name": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Une consigne gratuite pour vestes, sacs à dos et bagages est disponible dans notre boutique surveillée pendant votre sortie."}}, {"@type": "Question", "name": "Puis-je réserver ou poser des questions par WhatsApp ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait."}}, {"@type": "Question", "name": "Comment réserver ou vous contacter ?", "acceptedAnswer": {"@type": "Answer", "text": "Vous pouvez réserver par WhatsApp, email ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des planches ou le meilleur moment pour récupérer votre skateboard."}}], "inLanguage": "fr"} |
| fr | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#service-list", "name": "Principaux services de location à Barcelone", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Location de scooters à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Location de patins en ligne à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Location de vélos à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Location de patins à roulettes à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Location de skateboard à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Location de longboard à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/longboard/"}}]} |
| fr | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage", "dateModified": "2026-08-24"} |
| fr | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/fr/skateboard/#google-review-1"}]} |
| fr | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excellent service, et en plus la boutique est à côté de la promenade maritime. Si vous voulez profiter de Barcelone sur des roues, vous y trouverez des vélos, des patins, des skateboards et des scooters. Ils ont aussi des patins et des vélos pour enfants.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con skateboard, tavole cruiser, scooter, biciclette, pattini in linea, pattini a rotelle e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Casco per bambini e protezioni inclusi con il noleggio skateboard. Deposito bagagli gratuito e consigli sui percorsi.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| it | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "it"} |
| it | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/it/skateboard/", "name": "Noleggio Skateboard a Barcellona \| Cruiser vicino al Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "it", "description": "Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/it/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/it/skateboard/#faq"}], "dateModified": "2026-07-30"} |
| it | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inizio", "item": "https://rentalscooterbarcelona.com/it/"}, {"@type": "ListItem", "position": 2, "name": "Noleggio skateboard", "item": "https://rentalscooterbarcelona.com/it/skateboard/"}]} |
| it | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con skateboard, tavole cruiser, scooter, biciclette, pattini in linea, pattini a rotelle e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Casco per bambini e protezioni inclusi con il noleggio skateboard. Deposito bagagli gratuito e consigli sui percorsi.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| it | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#service", "serviceType": "Noleggio skateboard e tavole cruiser", "name": "Noleggio skateboard e tavole cruiser a Barcellona", "url": "https://rentalscooterbarcelona.com/it/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Noleggia skateboard e tavole cruiser a Barcellona, vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale alla Vila Olímpica offre tavole di qualità per principianti e rider più sicuri, casco per bambini incluso, protezioni incluse, deposito bagagli gratuito e consigli sui percorsi.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Noleggio skateboard 1 ora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Noleggio skateboard 2 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Noleggio skateboard 3 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Noleggio skateboard giornata intera", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Noleggio skateboard 24 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Noleggio skateboard giorno extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}]} |
| it | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Serve esperienza per noleggiare uno skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare."}}, {"@type": "Question", "name": "Le protezioni sono incluse nel noleggio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse."}}, {"@type": "Question", "name": "Dove posso andare in skateboard vicino al negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Il nostro negozio è vicino al lungomare, al Port Olímpic e a spazi aperti dove molti visitatori iniziano con un giro tranquillo prima di esplorare altri spot adatti allo skate."}}, {"@type": "Question", "name": "Avete skateboard per principianti?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Possiamo aiutarti a scegliere uno skateboard stabile o un cruiser board in base alla tua esperienza e al tipo di giro che vuoi fare."}}, {"@type": "Question", "name": "Serve una patente per noleggiare uno skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido."}}, {"@type": "Question", "name": "Posso lasciare borsa o bagagli in negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri."}}, {"@type": "Question", "name": "Posso prenotare o fare domande su WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare disponibilità, fare domande o organizzare l’orario di ritiro."}}, {"@type": "Question", "name": "Come prenoto o vi contatto?", "acceptedAnswer": {"@type": "Answer", "text": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle tavole o il momento migliore per ritirare il tuo skateboard."}}], "inLanguage": "it"} |
| it | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#service-list", "name": "Principali servizi di noleggio a Barcellona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Noleggio scooter a Barcellona", "url": "https://rentalscooterbarcelona.com/it/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Noleggio pattini in linea a Barcellona", "url": "https://rentalscooterbarcelona.com/it/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Noleggio biciclette a Barcellona", "url": "https://rentalscooterbarcelona.com/it/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Noleggio pattini a rotelle a Barcellona", "url": "https://rentalscooterbarcelona.com/it/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Noleggio skateboard a Barcellona", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Noleggio longboard a Barcellona", "url": "https://rentalscooterbarcelona.com/it/longboard/"}}]} |
| it | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#webpage", "dateModified": "2026-08-24"} |
| it | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/it/skateboard/#google-review-1"}]} |
| it | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Servizio eccellente, inoltre il negozio è accanto al lungomare. Se vuoi goderti Barcellona su ruote, qui trovi biciclette, pattini, skateboard e scooter. Hanno anche pattini e biciclette per bambini.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Skateboards, Cruiserboards, Scootern, Fahrrädern, Inlineskates, Rollschuhen und Longboards nahe Port Olímpic und Barceloneta-Strand. Kinderhelm und Schutzausrüstung sind beim Skateboard-Verleih inklusive. Kostenlose Gepäckaufbewahrung und lokale Routentipps.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| de | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "de", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| de | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/de/skateboard/", "name": "Skateboard mieten in Barcelona \| Cruiserboards nahe Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "de", "description": "Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/de/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/de/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/de/skateboard/#breadcrumb"}} |
| de | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://rentalscooterbarcelona.com/de/"}, {"@type": "ListItem", "position": 2, "name": "Skateboard-Verleih", "item": "https://rentalscooterbarcelona.com/de/skateboard/"}]} |
| de | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Skateboards, Cruiserboards, Scootern, Fahrrädern, Inlineskates, Rollschuhen und Longboards nahe Port Olímpic und Barceloneta-Strand. Kinderhelm und Schutzausrüstung sind beim Skateboard-Verleih inklusive. Kostenlose Gepäckaufbewahrung und lokale Routentipps.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1200-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kartenzahlung akzeptiert. PayPal für Online-Zahlungen verfügbar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| de | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#service", "serviceType": "Skateboard- und Cruiser-Board-Verleih", "name": "Skateboard- und Cruiser-Board-Verleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "description": "Miete Skateboards und Cruiserboards in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in der Vila Olímpica bietet hochwertige Boards für Anfänger und erfahrene Fahrer, Kinderhelm inklusive, Schutzausrüstung inklusive, kostenlose Gepäckaufbewahrung und Routentipps.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard-Verleih 1 Stunde", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard-Verleih 2 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard-Verleih 3 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard-Verleih ganzer Tag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard-Verleih 24 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard-Verleih Zusatztag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}]} |
| de | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Brauche ich Erfahrung, um ein Skateboard zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein, du brauchst keine Vorerfahrung. Wir vermieten Skateboards an Anfänger und erfahrene Skater, und unser Team hilft dir, ein komfortables Board für den Einstieg zu wählen."}}, {"@type": "Question", "name": "Ist Schutzausrüstung in der Miete enthalten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive."}}, {"@type": "Question", "name": "Wo kann ich in der Nähe des Shops Skateboard fahren?", "acceptedAnswer": {"@type": "Answer", "text": "Unser Shop liegt nahe der Strandpromenade, dem Port Olímpic und offenen Flächen, wo viele Besucher entspannt starten, bevor sie weitere geeignete Bereiche zum Skaten in der Nähe erkunden."}}, {"@type": "Question", "name": "Habt ihr Skateboards für Anfänger?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Wir helfen dir, je nach Erfahrung und gewünschter Fahrt ein stabiles Skateboard oder Cruiserboard auszuwählen."}}, {"@type": "Question", "name": "Brauche ich einen Führerschein, um ein Skateboard zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich."}}, {"@type": "Question", "name": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck ist in unserem betreuten Shop möglich, während du fährst."}}, {"@type": "Question", "name": "Kann ich per WhatsApp buchen oder Fragen stellen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um die Verfügbarkeit zu bestätigen, Fragen zu stellen oder deine Abholzeit zu vereinbaren."}}, {"@type": "Question", "name": "Wie buche ich oder kontaktiere euch?", "acceptedAnswer": {"@type": "Answer", "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Board-Verfügbarkeit oder den besten Abholzeitpunkt bestätigen möchtest."}}], "inLanguage": "de"} |
| de | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#service-list", "name": "Wichtigste Verleihservices in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter-Verleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inlineskates-Verleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Fahrradverleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Rollschuhe mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard-Verleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard-Verleih in Barcelona", "url": "https://rentalscooterbarcelona.com/de/longboard/"}}]} |
| de | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#webpage", "dateModified": "2026-08-24"} |
| de | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/de/skateboard/#google-review-1"}]} |
| de | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Schnell und unkompliziert! Wenig Papierkram und sonntags geöffnet. Fahrräder, Scooter, Skateboards, Inlineskates. Der kleine Laden hat alles!“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met skateboards, cruiserboards, scooters, fietsen, inline skates, rolschaatsen en longboards vlak bij Port Olímpic en Barceloneta. Een kinderhelm en bescherming zijn inbegrepen bij skateboardverhuur. Gratis bagageopslag en lokale routetips.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| nl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "nl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/nl/skateboard/", "name": "Skateboard huren in Barcelona \| Cruiserboards bij Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "nl", "description": "Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/nl/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Skateboard huren", "item": "https://rentalscooterbarcelona.com/nl/skateboard/"}]} |
| nl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met skateboards, cruiserboards, scooters, fietsen, inline skates, rolschaatsen en longboards vlak bij Port Olímpic en Barceloneta. Een kinderhelm en bescherming zijn inbegrepen bij skateboardverhuur. Gratis bagageopslag en lokale routetips.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| nl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service", "serviceType": "Skateboard en cruiser board verhuur", "name": "Skateboard en cruiser board huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Huur skateboards en cruiserboards in Barcelona, vlak bij Port Olímpic en Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica heeft kwalitatieve boards voor beginners en ervaren skaters, kinderhelm inbegrepen, beschermers inbegrepen, gratis bagageopslag en routetips.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard huren 1 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard huren 2 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard huren 3 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard huren hele dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard huren 24 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard huren extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}]} |
| nl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Heb ik ervaring nodig om een skateboard te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, je hebt geen ervaring nodig. We verhuren skateboards aan beginners en ervaren skaters, en ons team helpt je een comfortabel board te kiezen om te starten."}}, {"@type": "Question", "name": "Is bescherming inbegrepen bij de huur?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen."}}, {"@type": "Question", "name": "Waar kan ik skateboarden in de buurt van de shop?", "acceptedAnswer": {"@type": "Answer", "text": "Onze shop ligt dicht bij de boulevard, Port Olímpic en open ruimtes waar veel bezoekers rustig beginnen voordat ze meer skatevriendelijke plekken in de buurt ontdekken."}}, {"@type": "Question", "name": "Hebben jullie skateboards voor beginners?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. We kunnen je helpen een stabiel skateboard of cruiser board te kiezen, afhankelijk van je ervaring en het soort rit dat je wilt."}}, {"@type": "Question", "name": "Heb ik een rijbewijs nodig om een skateboard te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID."}}, {"@type": "Question", "name": "Kan ik mijn tas of bagage in de shop achterlaten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Gratis opslag voor jassen, rugzakken en bagage is beschikbaar in onze bewaakte shop terwijl je rijdt."}}, {"@type": "Question", "name": "Kan ik reserveren of vragen stellen via WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken."}}, {"@type": "Question", "name": "Hoe reserveer ik of neem ik contact met jullie op?", "acceptedAnswer": {"@type": "Answer", "text": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen."}}], "inLanguage": "nl"} |
| nl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#service-list", "name": "Belangrijkste verhuurdiensten in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inline skates huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Fiets huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Rolschaatsen huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/longboard/"}}]} |
| nl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage", "dateModified": "2026-08-24"} |
| nl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/nl/skateboard/#google-review-1"}]} |
| nl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Snel en eenvoudig! Weinig papierwerk en open op zondag. Fietsen, scooters, skateboards, inline skates. De kleine winkel heeft alles!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com skateboards, pranchas cruiser, scooters, bicicletas, patins em linha, patins de 4 rodas e longboards perto do Port Olímpic e da praia da Barceloneta. Capacete infantil e proteções incluídos no aluguer de skateboard. Serviço gratuito de guarda de bagagem e sugestões de percurso.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pt | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pt-PT", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/pt/skateboard/", "name": "Aluguer de Skateboard em Barcelona \| Cruiser perto do Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "pt-PT", "description": "Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/pt/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": "https://rentalscooterbarcelona.com/pt/"}, {"@type": "ListItem", "position": 2, "name": "Aluguer de skateboard", "item": "https://rentalscooterbarcelona.com/pt/skateboard/"}]} |
| pt | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com skateboards, pranchas cruiser, scooters, bicicletas, patins em linha, patins de 4 rodas e longboards perto do Port Olímpic e da praia da Barceloneta. Capacete infantil e proteções incluídos no aluguer de skateboard. Serviço gratuito de guarda de bagagem e sugestões de percurso.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| pt | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service", "serviceType": "Aluguer de skateboard e pranchas cruiser", "name": "Aluguer de skateboard e pranchas cruiser em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Aluga skateboards e pranchas cruiser em Barcelona, perto do Port Olímpic e da praia da Barceloneta. A nossa loja local na Vila Olímpica oferece pranchas de qualidade para principiantes e riders com experiência, capacete infantil incluído, proteções incluídas, serviço gratuito de guarda de bagagem, sugestões de percurso e horários flexíveis.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Aluguer de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Aluguer de skateboard 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Aluguer de skateboard 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Aluguer de skateboard dia completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Aluguer de skateboard 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Aluguer de skateboard dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}]} |
| pt | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Preciso de experiência para alugar um skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar."}}, {"@type": "Question", "name": "O equipamento de proteção está incluído?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas."}}, {"@type": "Question", "name": "Onde posso andar de skateboard perto da loja?", "acceptedAnswer": {"@type": "Answer", "text": "A nossa loja fica perto do passeio marítimo, do Port Olímpic e de espaços abertos onde muitos visitantes começam com uma volta tranquila antes de explorar outros spots próximos adequados para skate."}}, {"@type": "Question", "name": "Têm skateboards para principiantes?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Podemos ajudar-te a escolher um skateboard estável ou um cruiser board conforme a tua experiência e o tipo de passeio que procuras."}}, {"@type": "Question", "name": "Preciso de carta para alugar um skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido."}}, {"@type": "Question", "name": "Posso deixar a minha mochila ou bagagem na loja?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas."}}, {"@type": "Question", "name": "Posso reservar ou fazer perguntas por WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento."}}, {"@type": "Question", "name": "Como faço a reserva ou contacto convosco?", "acceptedAnswer": {"@type": "Answer", "text": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard."}}], "inLanguage": "pt-PT"} |
| pt | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#service-list", "name": "Principais serviços de aluguer em Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Aluguer de scooters em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Aluguer de patins em linha em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Aluguer de bicicletas em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Aluguer de patins de 4 rodas em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Aluguer de skateboard em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Aluguer de longboard em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/longboard/"}}]} |
| pt | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage", "dateModified": "2026-08-24"} |
| pt | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pt/skateboard/#google-review-1"}]} |
| pt | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Rápido e fácil! Pouca burocracia e aberto aos domingos. Bicicletas, scooters, skates, patins em linha. A pequena loja tem tudo!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de skateboards, taules cruiser, scooters, bicicletes, patins en línia, patins de 4 rodes i longboards a prop del Port Olímpic i de la platja de la Barceloneta. Casc infantil i proteccions inclosos amb el lloguer de skateboard. Servei gratuït de guarda d’equipatge i recomanacions de rutes.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| ca | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "ca"} |
| ca | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/cat/skateboard/", "name": "Lloguer de Skateboard a Barcelona \| Cruiser prop del Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "ca", "description": "Lloga skateboards i taules cruiser a Barcelona, a prop del Port Olímpic i de la platja de la Barceloneta. La nostra botiga a la Vila Olímpica ofereix taules de qualitat per a principiants i persones amb experiència, casc infantil inclòs, proteccions incloses, servei gratuït de guarda d’equipatge i consells de ruta.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/cat/skateboard/#faq"}], "dateModified": "2026-07-30"} |
| ca | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inici", "item": "https://rentalscooterbarcelona.com/cat/"}, {"@type": "ListItem", "position": 2, "name": "Lloguer de skateboard", "item": "https://rentalscooterbarcelona.com/cat/skateboard/"}]} |
| ca | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de skateboards, taules cruiser, scooters, bicicletes, patins en línia, patins de 4 rodes i longboards a prop del Port Olímpic i de la platja de la Barceloneta. Casc infantil i proteccions inclosos amb el lloguer de skateboard. Servei gratuït de guarda d’equipatge i recomanacions de rutes.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| ca | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service", "serviceType": "Lloguer de skateboard i taules cruiser", "name": "Lloguer de skateboard i taules cruiser a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Lloga skateboards i taules cruiser a la nostra botiga local, a prop de la platja de la Barceloneta i del Port Olímpic. Incloem casc infantil, hi ha proteccions incloses, i el nostre equip et pot ajudar a triar la taula adequada per a una passejada tranquil·la o una sessió informal.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Lloguer de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Lloguer de skateboard 2 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Lloguer de skateboard 3 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Lloguer de skateboard dia complet", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Lloguer de skateboard 24 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Lloguer de skateboard dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}]} |
| ca | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Necessito experiència per llogar un skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No, no necessites experiència prèvia. Lloguem skateboards a principiants i persones amb experiència, i el nostre equip pot ajudar-te a triar una taula còmoda per començar."}}, {"@type": "Question", "name": "L’equip de protecció està inclòs?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses."}}, {"@type": "Question", "name": "On puc anar amb skateboard a prop de la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "La nostra botiga és a prop del passeig marítim, el Port Olímpic i zones obertes on molts visitants comencen amb una ruta tranquil·la abans d’explorar altres espais aptes per a skate."}}, {"@type": "Question", "name": "Teniu skateboards per a principiants?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Podem ajudar-te a triar un skateboard estable o un cruiser board segons la teva experiència i el tipus de ruta que vulguis fer."}}, {"@type": "Question", "name": "Necessito carnet per llogar un skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid."}}, {"@type": "Question", "name": "Puc deixar la motxilla o l’equipatge a la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes."}}, {"@type": "Question", "name": "Puc reservar o fer preguntes per WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida."}}, {"@type": "Question", "name": "Com reservo o contacto amb vosaltres?", "acceptedAnswer": {"@type": "Answer", "text": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar disponibilitat de taules o el millor moment per recollir el teu skateboard."}}], "inLanguage": "ca"} |
| ca | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#service-list", "name": "Serveis principals de lloguer a Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Lloguer de scooters a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Lloguer de patins en línia a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Lloguer de bicicletes a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Lloguer de patins de 4 rodes a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Lloguer de skateboard a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Lloguer de longboard a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/longboard/"}}]} |
| ca | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage", "dateModified": "2026-08-24"} |
| ca | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/cat/skateboard/#google-review-1"}]} |
| ca | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ràpid i fàcil! Poca paperassa i obert els diumenges. Bicicletes, scooters, monopatins i patins en línia. La petita botiga ho té tot!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokal uthyrning i Vila Olímpica del Poblenou, Barcelona, med skateboard, cruiserboards, scootrar, cyklar, inlines, rullskridskor och longboards nära Port Olímpic och Barceloneta. Barnhjälm och skydd ingår vid skateboarduthyrning. Gratis bagageförvaring och lokala ruttips.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| sv | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "sv", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/sv/skateboard/", "name": "Hyra Skateboard i Barcelona \| Cruiserboards nära Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "sv", "description": "Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/sv/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Hem", "item": "https://rentalscooterbarcelona.com/sv/"}, {"@type": "ListItem", "position": 2, "name": "Hyra skateboard", "item": "https://rentalscooterbarcelona.com/sv/skateboard/"}]} |
| sv | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokal uthyrning i Vila Olímpica del Poblenou, Barcelona, med skateboard, cruiserboards, scootrar, cyklar, inlines, rullskridskor och longboards nära Port Olímpic och Barceloneta. Barnhjälm och skydd ingår vid skateboarduthyrning. Gratis bagageförvaring och lokala ruttips.", "image": ["https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kortbetalning accepteras. PayPal finns för onlinebetalningar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| sv | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service", "serviceType": "Skateboard- och cruiserboarduthyrning", "name": "Hyra skateboard och cruiserboards i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "description": "Hyr skateboard och cruiserboards i Barcelona nära Port Olímpic och Barceloneta. Vår lokala uthyrning i Vila Olímpica erbjuder kvalitetsbrädor för nybörjare och vana åkare, barnhjälm ingår, skydd ingår, gratis bagageförvaring, lokala ruttips.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Hyra skateboard 1 timme", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Hyra skateboard 2 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Hyra skateboard 3 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Hyra skateboard heldag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Hyra skateboard 24 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Hyra skateboard extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}]} |
| sv | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Behöver jag erfarenhet för att hyra skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med."}}, {"@type": "Question", "name": "Ingår skyddsutrustning i hyran?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår."}}, {"@type": "Question", "name": "Var kan jag åka skateboard nära butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Vår butik ligger nära strandpromenaden, Port Olímpic och öppna ytor där många besökare börjar med en lugn tur innan de utforskar fler skatevänliga platser i närheten."}}, {"@type": "Question", "name": "Har ni skateboards för nybörjare?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Vi kan hjälpa dig att välja en stabil skateboard eller cruiserbräda beroende på din erfarenhet och vilken typ av tur du vill göra."}}, {"@type": "Question", "name": "Behöver jag körkort för att hyra skateboard?", "acceptedAnswer": {"@type": "Answer", "text": "Nej. Inget körkort krävs för att hyra en skateboard."}}, {"@type": "Question", "name": "Kan jag lämna väska eller bagage i butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Gratis förvaring för jackor, ryggsäckar och bagage finns i vår övervakade butik medan du åker."}}, {"@type": "Question", "name": "Kan jag boka eller ställa frågor via WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid."}}, {"@type": "Question", "name": "Hur bokar jag eller kontaktar er?", "acceptedAnswer": {"@type": "Answer", "text": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard."}}], "inLanguage": "sv"} |
| sv | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#service-list", "name": "Huvudsakliga uthyrningstjänster i Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Hyra scooter i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Hyra inlines i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Hyra cykel i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Hyra rullskridskor i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Hyra skateboard i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Hyra longboard i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/longboard/"}}]} |
| sv | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage", "dateModified": "2026-08-24"} |
| sv | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/sv/skateboard/#google-review-1"}]} |
| sv | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Snabbt och enkelt! Lite pappersarbete och öppet på söndagar. Cyklar, scootrar, skateboards och inlines. Den lilla butiken har allt!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "name": "Wynajem deskorolek w Barcelonie blisko Port Olímpic", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "pl", "description": "Wynajmij deskorolki i cruisery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy i ochraniacze w cenie, darmowe przechowanie bagażu i lokalne wskazówki.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-skateboard-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service"}, {"@id": "https://rentalscooterbarcelona.com/pl/skateboard/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp rezerwacja", "target": "https://wa.me/34640559468"}} |
| pl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://rentalscooterbarcelona.com/pl/"}, {"@type": "ListItem", "position": 2, "name": "Wynajem deskorolek", "item": "https://rentalscooterbarcelona.com/pl/skateboard/"}]} |
| pl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Karta kredytowa, karta debetowa, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service", "serviceType": "Wynajem deskorolek i cruiserów", "name": "Wynajem deskorolek i cruiserów w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "description": "Wynajmij deskorolki i cruisery w naszej lokalnej wypożyczalni naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy oraz ochraniacze na kolana, łokcie i nadgarstki są w cenie, a nasz zespół pomoże dobrać odpowiednią deskę do spokojnej jazdy lub rekreacyjnej sesji.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Zakres cen wynajmu deskorolek", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Wynajem deskorolek 1 godzina", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Wynajem deskorolek 2 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Wynajem deskorolek 3 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Całodniowy wynajem deskorolek", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Wynajem deskorolek 24 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Dodatkowy dzień wynajmu deskorolek", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}]} |
| pl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#faq", "mainEntity": [{"@type": "Question", "name": "Czy potrzebuję doświadczenia, aby wynająć deskorolkę?", "acceptedAnswer": {"@type": "Answer", "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy deskorolki początkującym i pewniejszym osobom, a nasz zespół pomoże wybrać wygodną deskę na start."}}, {"@type": "Question", "name": "Czy sprzęt ochronny jest w cenie wynajmu?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę."}}, {"@type": "Question", "name": "Gdzie mogę jeździć na deskorolce blisko wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym odkrywaniem pobliskich miejsc przyjaznych do jazdy."}}, {"@type": "Question", "name": "Czy macie deskorolki dla początkujących?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Pomożemy wybrać stabilną deskorolkę lub cruisera w zależności od Twojego doświadczenia i rodzaju jazdy, którego szukasz."}}, {"@type": "Question", "name": "Czy potrzebuję prawa jazdy, aby wynająć deskorolkę?", "acceptedAnswer": {"@type": "Answer", "text": "Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy."}}, {"@type": "Question", "name": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni."}}, {"@type": "Question", "name": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru."}}, {"@type": "Question", "name": "Jak mogę zarezerwować lub skontaktować się z wami?", "acceptedAnswer": {"@type": "Answer", "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność deski albo najlepszą godzinę odbioru deskorolki."}}], "inLanguage": "pl"} |
| pl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#service-list", "name": "Główne usługi wynajmu w Barcelonie", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Wynajem skuterów w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Wynajem rolek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Wynajem rowerów w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Wynajem wrotek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Wynajem deskorolek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Wynajem longboardu w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/longboard/"}}]} |
| pl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage", "dateModified": "2026-08-24"} |
| pl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pl/skateboard/#google-review-1"}]} |
| pl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Szybko i łatwo! Mało formalności i otwarte w niedziele. Rowery, skutery, deskorolki i rolki. Ten mały sklep ma wszystko!\"", "publisher": {"@type": "Organization", "name": "Google"}} |

## N. MATRIZ ARTICLE/BLOGPOSTING

No hay entidades Article/BlogPosting en estas páginas de servicio/contacto; no se exige un esquema editorial. Los elementos HTML article se cuentan por separado en U.

## O. MATRIZ GEO/COORDENADAS

| Idioma | Coordenadas extraídas | IDs de mapas | Sin coordenadas antiguas |
| --- | --- | --- | --- |
| en | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 79, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 323, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| es | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 76, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 315, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| fr | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 69, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 259, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| it | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 68, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 258, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| de | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 66, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 266, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| nl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 79, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 275, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pt | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 79, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 275, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| ca | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 68, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 258, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| sv | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 79, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 275, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 79, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 323, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |

## P. MATRIZ NAP

| Idioma | Propiedad | Valor actual | Esperado | Coincide |
| --- | --- | --- | --- | --- |
| en | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| en | alternateName | RSB | RSB | True |
| en | telephone | +34 640 559 468 | +34 640 559 468 | True |
| en | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| en | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| en | addressLocality | Barcelona | Barcelona | True |
| en | addressRegion | Catalonia | Catalonia | True |
| en | postalCode | 08005 | 08005 | True |
| en | addressCountry | ES | ES | True |
| en | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| en | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| en | alternateName | RSB | RSB | True |
| en | telephone | +34 640 559 468 | +34 640 559 468 | True |
| en | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| en | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| en | addressLocality | Barcelona | Barcelona | True |
| en | addressRegion | Catalonia | Catalonia | True |
| en | postalCode | 08005 | 08005 | True |
| en | addressCountry | ES | ES | True |
| en | ratingValue | 4.6 | 4.6 | True |
| en | reviewCount | 226 | 226 | True |
| en | bestRating | 5 | 5 | True |
| en | worstRating | 1 | 1 | True |
| es | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| es | alternateName | RSB | RSB | True |
| es | telephone | +34 640 559 468 | +34 640 559 468 | True |
| es | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| es | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| es | addressLocality | Barcelona | Barcelona | True |
| es | addressRegion | Catalonia | Catalonia | True |
| es | postalCode | 08005 | 08005 | True |
| es | addressCountry | ES | ES | True |
| es | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| es | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| es | alternateName | RSB | RSB | True |
| es | telephone | +34 640 559 468 | +34 640 559 468 | True |
| es | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| es | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| es | addressLocality | Barcelona | Barcelona | True |
| es | addressRegion | Catalonia | Catalonia | True |
| es | postalCode | 08005 | 08005 | True |
| es | addressCountry | ES | ES | True |
| es | ratingValue | 4.6 | 4.6 | True |
| es | reviewCount | 226 | 226 | True |
| es | bestRating | 5 | 5 | True |
| es | worstRating | 1 | 1 | True |
| fr | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| fr | alternateName | RSB | RSB | True |
| fr | telephone | +34 640 559 468 | +34 640 559 468 | True |
| fr | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| fr | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| fr | addressLocality | Barcelona | Barcelona | True |
| fr | addressRegion | Catalonia | Catalonia | True |
| fr | postalCode | 08005 | 08005 | True |
| fr | addressCountry | ES | ES | True |
| fr | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| fr | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| fr | alternateName | RSB | RSB | True |
| fr | telephone | +34 640 559 468 | +34 640 559 468 | True |
| fr | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| fr | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| fr | addressLocality | Barcelona | Barcelona | True |
| fr | addressRegion | Catalonia | Catalonia | True |
| fr | postalCode | 08005 | 08005 | True |
| fr | addressCountry | ES | ES | True |
| fr | ratingValue | 4.6 | 4.6 | True |
| fr | reviewCount | 226 | 226 | True |
| fr | bestRating | 5 | 5 | True |
| fr | worstRating | 1 | 1 | True |
| it | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| it | alternateName | RSB | RSB | True |
| it | telephone | +34 640 559 468 | +34 640 559 468 | True |
| it | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| it | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| it | addressLocality | Barcelona | Barcelona | True |
| it | addressRegion | Catalonia | Catalonia | True |
| it | postalCode | 08005 | 08005 | True |
| it | addressCountry | ES | ES | True |
| it | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| it | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| it | alternateName | RSB | RSB | True |
| it | telephone | +34 640 559 468 | +34 640 559 468 | True |
| it | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| it | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| it | addressLocality | Barcelona | Barcelona | True |
| it | addressRegion | Catalonia | Catalonia | True |
| it | postalCode | 08005 | 08005 | True |
| it | addressCountry | ES | ES | True |
| it | ratingValue | 4.6 | 4.6 | True |
| it | reviewCount | 226 | 226 | True |
| it | bestRating | 5 | 5 | True |
| it | worstRating | 1 | 1 | True |
| de | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| de | alternateName | RSB | RSB | True |
| de | telephone | +34 640 559 468 | +34 640 559 468 | True |
| de | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| de | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| de | addressLocality | Barcelona | Barcelona | True |
| de | addressRegion | Catalonia | Catalonia | True |
| de | postalCode | 08005 | 08005 | True |
| de | addressCountry | ES | ES | True |
| de | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| de | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| de | alternateName | RSB | RSB | True |
| de | telephone | +34 640 559 468 | +34 640 559 468 | True |
| de | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| de | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| de | addressLocality | Barcelona | Barcelona | True |
| de | addressRegion | Catalonia | Catalonia | True |
| de | postalCode | 08005 | 08005 | True |
| de | addressCountry | ES | ES | True |
| de | ratingValue | 4.6 | 4.6 | True |
| de | reviewCount | 226 | 226 | True |
| de | bestRating | 5 | 5 | True |
| de | worstRating | 1 | 1 | True |
| nl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| nl | alternateName | RSB | RSB | True |
| nl | telephone | +34 640 559 468 | +34 640 559 468 | True |
| nl | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| nl | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| nl | addressLocality | Barcelona | Barcelona | True |
| nl | addressRegion | Catalonia | Catalonia | True |
| nl | postalCode | 08005 | 08005 | True |
| nl | addressCountry | ES | ES | True |
| nl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| nl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| nl | alternateName | RSB | RSB | True |
| nl | telephone | +34 640 559 468 | +34 640 559 468 | True |
| nl | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| nl | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| nl | addressLocality | Barcelona | Barcelona | True |
| nl | addressRegion | Catalonia | Catalonia | True |
| nl | postalCode | 08005 | 08005 | True |
| nl | addressCountry | ES | ES | True |
| nl | ratingValue | 4.6 | 4.6 | True |
| nl | reviewCount | 226 | 226 | True |
| nl | bestRating | 5 | 5 | True |
| nl | worstRating | 1 | 1 | True |
| pt | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pt | alternateName | RSB | RSB | True |
| pt | telephone | +34 640 559 468 | +34 640 559 468 | True |
| pt | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| pt | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| pt | addressLocality | Barcelona | Barcelona | True |
| pt | addressRegion | Catalonia | Catalonia | True |
| pt | postalCode | 08005 | 08005 | True |
| pt | addressCountry | ES | ES | True |
| pt | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pt | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pt | alternateName | RSB | RSB | True |
| pt | telephone | +34 640 559 468 | +34 640 559 468 | True |
| pt | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| pt | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| pt | addressLocality | Barcelona | Barcelona | True |
| pt | addressRegion | Catalonia | Catalonia | True |
| pt | postalCode | 08005 | 08005 | True |
| pt | addressCountry | ES | ES | True |
| pt | ratingValue | 4.6 | 4.6 | True |
| pt | reviewCount | 226 | 226 | True |
| pt | bestRating | 5 | 5 | True |
| pt | worstRating | 1 | 1 | True |
| ca | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| ca | alternateName | RSB | RSB | True |
| ca | telephone | +34 640 559 468 | +34 640 559 468 | True |
| ca | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| ca | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| ca | addressLocality | Barcelona | Barcelona | True |
| ca | addressRegion | Catalonia | Catalonia | True |
| ca | postalCode | 08005 | 08005 | True |
| ca | addressCountry | ES | ES | True |
| ca | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| ca | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| ca | alternateName | RSB | RSB | True |
| ca | telephone | +34 640 559 468 | +34 640 559 468 | True |
| ca | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| ca | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| ca | addressLocality | Barcelona | Barcelona | True |
| ca | addressRegion | Catalonia | Catalonia | True |
| ca | postalCode | 08005 | 08005 | True |
| ca | addressCountry | ES | ES | True |
| ca | ratingValue | 4.6 | 4.6 | True |
| ca | reviewCount | 226 | 226 | True |
| ca | bestRating | 5 | 5 | True |
| ca | worstRating | 1 | 1 | True |
| sv | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| sv | alternateName | RSB | RSB | True |
| sv | telephone | +34 640 559 468 | +34 640 559 468 | True |
| sv | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| sv | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| sv | addressLocality | Barcelona | Barcelona | True |
| sv | addressRegion | Catalonia | Catalonia | True |
| sv | postalCode | 08005 | 08005 | True |
| sv | addressCountry | ES | ES | True |
| sv | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| sv | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| sv | alternateName | RSB | RSB | True |
| sv | telephone | +34 640 559 468 | +34 640 559 468 | True |
| sv | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| sv | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| sv | addressLocality | Barcelona | Barcelona | True |
| sv | addressRegion | Catalonia | Catalonia | True |
| sv | postalCode | 08005 | 08005 | True |
| sv | addressCountry | ES | ES | True |
| sv | ratingValue | 4.6 | 4.6 | True |
| sv | reviewCount | 226 | 226 | True |
| sv | bestRating | 5 | 5 | True |
| sv | worstRating | 1 | 1 | True |
| pl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pl | alternateName | RSB | RSB | True |
| pl | telephone | +34 640 559 468 | +34 640 559 468 | True |
| pl | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| pl | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| pl | addressLocality | Barcelona | Barcelona | True |
| pl | addressRegion | Catalonia | Catalonia | True |
| pl | postalCode | 08005 | 08005 | True |
| pl | addressCountry | ES | ES | True |
| pl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pl | name | RSB Rental Scooter Barcelona | RSB Rental Scooter Barcelona | True |
| pl | alternateName | RSB | RSB | True |
| pl | telephone | +34 640 559 468 | +34 640 559 468 | True |
| pl | email | info@rentalscooterbarcelona.com | info@rentalscooterbarcelona.com | True |
| pl | streetAddress | Carrer de Salvador Espriu, 63 | Carrer de Salvador Espriu, 63 | True |
| pl | addressLocality | Barcelona | Barcelona | True |
| pl | addressRegion | Catalonia | Catalonia | True |
| pl | postalCode | 08005 | 08005 | True |
| pl | addressCountry | ES | ES | True |
| pl | ratingValue | 4.6 | 4.6 | True |
| pl | reviewCount | 226 | 226 | True |
| pl | bestRating | 5 | 5 | True |
| pl | worstRating | 1 | 1 | True |

## Q. MATRIZ PRECIOS

| Idioma | Tarjetas | Resumen compacto | Ofertas completas | Accesorios separados | Controles |
| --- | --- | --- | --- | --- | --- |
| en | [{"line": 757, "text": "1 hour €6 Perfect for a quick roll by the beach or trying a skateboard for the first time.", "price": 6.0}, {"line": 762, "text": "Most popular 2 hours €12 Ideal for a longer beachfront ride, Port Olímpic and open areas near Ciutadella Park.", "price": 12.0}, {"line": 768, "text": "3 hours €15 Best for combining coastal cruising with extra time to stop at local skate spots.", "price": 15.0}, {"line": 773, "text": "Full day €18 Enjoy a full day of cruising, exploring and stopping wherever the route feels right.", "price": 18.0}, {"line": 778, "text": "24 hours €20 Pick up today and return tomorrow to make the most of your Barcelona visit on a board.", "price": 20.0}, {"line": 783, "text": "Extra day €10 Extend your skateboard rental for another day at a reduced rate.", "price": 10.0}] | [{"line": 971, "text": "1 hour €6", "price": 6.0}, {"line": 975, "text": "2 hours €12", "price": 12.0}, {"line": 979, "text": "3 hours €15", "price": 15.0}, {"line": 983, "text": "Full day €18", "price": 18.0}, {"line": 987, "text": "24 hours €20", "price": 20.0}, {"line": 991, "text": "Extra day €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard rental 1 hour", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard rental 2 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard rental 3 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard rental full day", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard rental 24 hours", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard rental extra day", "url": "https://rentalscooterbarcelona.com/skateboard/", "availability": "https://schema.org/InStock"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| es | [{"line": 751, "text": "1 hora €6 Perfecto para una vuelta rápida por la playa o para probar un skateboard por primera vez.", "price": 6.0}, {"line": 756, "text": "Más popular 2 horas €12 Ideal para una ruta más larga por la playa, el Port Olímpic y zonas abiertas cerca del Parc de la Ciutadella.", "price": 12.0}, {"line": 762, "text": "3 horas €15 La mejor opción para combinar paseo junto al mar con tiempo extra para parar en zonas locales de skate.", "price": 15.0}, {"line": 767, "text": "Día completo €18 Disfruta de un día completo para rodar, explorar y parar donde te apetezca.", "price": 18.0}, {"line": 772, "text": "24 horas €20 Recoge hoy y devuelve mañana para aprovechar Barcelona sobre una tabla.", "price": 20.0}, {"line": 777, "text": "Día extra €10 Amplía tu alquiler de skateboard un día más con una tarifa reducida.", "price": 10.0}] | [{"line": 958, "text": "1 hora €6", "price": 6.0}, {"line": 962, "text": "2 horas €12", "price": 12.0}, {"line": 966, "text": "3 horas €15", "price": 15.0}, {"line": 970, "text": "Día completo €18", "price": 18.0}, {"line": 974, "text": "24 horas €20", "price": 20.0}, {"line": 978, "text": "Día extra €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Alquiler de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Alquiler de skateboard 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Alquiler de skateboard 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Alquiler de skateboard día completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Alquiler de skateboard 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Alquiler de skateboard día extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| fr | [{"line": 690, "text": "1 heure €6 Parfait pour une petite balade près de la plage ou pour essayer un skateboard pour la première fois.", "price": 6.0}, {"line": 695, "text": "Le plus populaire 2 heures €12 Idéal pour une balade plus longue en bord de mer, le Port Olímpic et les espaces ouverts près du parc de la Ciutadella.", "price": 12.0}, {"line": 701, "text": "3 heures €15 Le meilleur choix pour combiner balade côtière et pauses dans des spots de skate locaux.", "price": 15.0}, {"line": 706, "text": "Journée complète €18 Profitez d’une journée complète pour rouler, explorer et vous arrêter où vous voulez.", "price": 18.0}, {"line": 711, "text": "24 heures €20 Retirez aujourd’hui et retournez demain pour profiter de Barcelone sur une planche.", "price": 20.0}, {"line": 716, "text": "Jour supplémentaire €10 Prolongez votre location de skateboard d’une journée à tarif réduit.", "price": 10.0}] | [{"line": 901, "text": "1 heure €6", "price": 6.0}, {"line": 905, "text": "2 heures €12", "price": 12.0}, {"line": 909, "text": "3 heures €15", "price": 15.0}, {"line": 913, "text": "Journée complète €18", "price": 18.0}, {"line": 917, "text": "24 heures €20", "price": 20.0}, {"line": 921, "text": "Jour supplémentaire €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Location de skateboard 1 heure", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Location de skateboard 2 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Location de skateboard 3 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Location de skateboard journée complète", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Location de skateboard 24 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Location de skateboard journée supplémentaire", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| it | [{"line": 695, "text": "1 ora €6 Perfetto per un giro veloce vicino alla spiaggia o per provare uno skateboard per la prima volta.", "price": 6.0}, {"line": 700, "text": "Più richiesto 2 ore €12 Ideale per un giro più lungo sul lungomare, al Port Olímpic e negli spazi aperti vicino al Parc de la Ciutadella.", "price": 12.0}, {"line": 706, "text": "3 ore €15 La scelta migliore per combinare cruising sulla costa e tempo extra per fermarsi negli spot locali.", "price": 15.0}, {"line": 711, "text": "Giornata intera €18 Goditi un’intera giornata di cruising, esplorazione e soste dove preferisci.", "price": 18.0}, {"line": 716, "text": "24 ore €20 Ritira oggi e restituisci domani per goderti Barcellona sulla tavola.", "price": 20.0}, {"line": 721, "text": "Giorno extra €10 Estendi il noleggio dello skateboard per un altro giorno a tariffa ridotta.", "price": 10.0}] | [{"line": 906, "text": "1 ora €6", "price": 6.0}, {"line": 910, "text": "2 ore €12", "price": 12.0}, {"line": 914, "text": "3 ore €15", "price": 15.0}, {"line": 918, "text": "Giornata intera €18", "price": 18.0}, {"line": 922, "text": "24 ore €20", "price": 20.0}, {"line": 926, "text": "Giorno extra €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Noleggio skateboard 1 ora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Noleggio skateboard 2 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Noleggio skateboard 3 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Noleggio skateboard giornata intera", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Noleggio skateboard 24 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Noleggio skateboard giorno extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| de | [{"line": 697, "text": "1 Stunde €6 Perfekt für eine kurze Runde am Strand oder um zum ersten Mal ein Skateboard auszuprobieren.", "price": 6.0}, {"line": 702, "text": "Am beliebtesten 2 Stunden €12 Ideal für eine längere Fahrt am Strand, Port Olímpic und offene Bereiche nahe dem Parc de la Ciutadella.", "price": 12.0}, {"line": 708, "text": "3 Stunden €15 Am besten, wenn du Küstencruising mit zusätzlichen Stopps an geeigneten Bereichen zum Skaten verbinden möchtest.", "price": 15.0}, {"line": 713, "text": "Ganzer Tag €18 Genieße einen ganzen Tag zum Cruisen, Erkunden und Stoppen, wo es dir gefällt.", "price": 18.0}, {"line": 718, "text": "24 Stunden €20 Heute abholen und morgen zurückbringen, um Barcelona auf dem Board voll auszunutzen.", "price": 20.0}, {"line": 723, "text": "Zusatztag €10 Verlängere deine Skateboard-Miete um einen weiteren Tag zum reduzierten Preis.", "price": 10.0}] | [{"line": 932, "text": "1 Stunde €6", "price": 6.0}, {"line": 936, "text": "2 Stunden €12", "price": 12.0}, {"line": 940, "text": "3 Stunden €15", "price": 15.0}, {"line": 944, "text": "Ganzer Tag €18", "price": 18.0}, {"line": 948, "text": "24 Stunden €20", "price": 20.0}, {"line": 952, "text": "Zusatztag €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard-Verleih 1 Stunde", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard-Verleih 2 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard-Verleih 3 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard-Verleih ganzer Tag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard-Verleih 24 Stunden", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard-Verleih Zusatztag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| nl | [{"line": 706, "text": "1 uur €6 Perfect voor een korte rit bij het strand of om voor het eerst een skateboard te proberen.", "price": 6.0}, {"line": 711, "text": "Meest populair 2 uur €12 Ideaal voor een langere rit langs het strand, Port Olímpic en open ruimtes bij Parc de la Ciutadella.", "price": 12.0}, {"line": 717, "text": "3 uur €15 Beste keuze om cruisen langs de kust te combineren met extra tijd bij lokale skateplekken.", "price": 15.0}, {"line": 722, "text": "Hele dag €18 Geniet van een hele dag cruisen, ontdekken en stoppen waar je wilt.", "price": 18.0}, {"line": 727, "text": "24 uur €20 Vandaag ophalen en morgen terugbrengen om Barcelona optimaal op een board te beleven.", "price": 20.0}, {"line": 732, "text": "Extra dag €10 Verleng je skateboardhuur met een extra dag tegen een lager tarief.", "price": 10.0}] | [{"line": 941, "text": "1 uur €6", "price": 6.0}, {"line": 945, "text": "2 uur €12", "price": 12.0}, {"line": 949, "text": "3 uur €15", "price": 15.0}, {"line": 953, "text": "Hele dag €18", "price": 18.0}, {"line": 957, "text": "24 uur €20", "price": 20.0}, {"line": 961, "text": "Extra dag €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Skateboard huren 1 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Skateboard huren 2 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Skateboard huren 3 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Skateboard huren hele dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Skateboard huren 24 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Skateboard huren extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| pt | [{"line": 712, "text": "1 hora €6 Perfeito para uma volta rápida junto à praia ou para experimentar um skateboard pela primeira vez.", "price": 6.0}, {"line": 717, "text": "Mais popular 2 horas €12 Ideal para um passeio mais longo junto à praia, Port Olímpic e espaços abertos perto do Parc de la Ciutadella.", "price": 12.0}, {"line": 723, "text": "3 horas €15 A melhor opção para combinar cruising junto à costa com tempo extra para parar em spots locais de skate.", "price": 15.0}, {"line": 728, "text": "Dia completo €18 Desfruta de um dia completo para andar, explorar e parar onde quiseres.", "price": 18.0}, {"line": 733, "text": "24 horas €20 Levanta hoje e devolve amanhã para aproveitar Barcelona sobre uma tábua.", "price": 20.0}, {"line": 738, "text": "Dia extra €10 Prolonga o teu aluguer de skateboard por mais um dia com tarifa reduzida.", "price": 10.0}] | [{"line": 929, "text": "1 hora €6", "price": 6.0}, {"line": 933, "text": "2 horas €12", "price": 12.0}, {"line": 937, "text": "3 horas €15", "price": 15.0}, {"line": 941, "text": "Dia completo €18", "price": 18.0}, {"line": 945, "text": "24 horas €20", "price": 20.0}, {"line": 949, "text": "Dia extra €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Aluguer de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Aluguer de skateboard 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Aluguer de skateboard 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Aluguer de skateboard dia completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Aluguer de skateboard 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Aluguer de skateboard dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| ca | [{"line": 695, "text": "1 hora €6 Perfecte per fer una volta ràpida per la platja o provar un skateboard per primera vegada.", "price": 6.0}, {"line": 700, "text": "Més popular 2 hores €12 Ideal per a una ruta més llarga pel front marítim, el Port Olímpic i espais oberts prop del Parc de la Ciutadella.", "price": 12.0}, {"line": 706, "text": "3 hores €15 La millor opció per combinar una ruta vora el mar amb temps extra per parar en zones locals de skate.", "price": 15.0}, {"line": 711, "text": "Dia complet €18 Gaudeix d’un dia complet per rodar, explorar i parar on et vingui de gust.", "price": 18.0}, {"line": 716, "text": "24 hores €20 Recull avui i torna demà per aprofitar Barcelona sobre una taula.", "price": 20.0}, {"line": 721, "text": "Dia extra €10 Allarga el teu lloguer de skateboard un dia més amb una tarifa reduïda.", "price": 10.0}] | [{"line": 913, "text": "1 hora €6", "price": 6.0}, {"line": 917, "text": "2 hores €12", "price": 12.0}, {"line": 921, "text": "3 hores €15", "price": 15.0}, {"line": 925, "text": "Dia complet €18", "price": 18.0}, {"line": 929, "text": "24 hores €20", "price": 20.0}, {"line": 933, "text": "Dia extra €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Lloguer de skateboard 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Lloguer de skateboard 2 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Lloguer de skateboard 3 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Lloguer de skateboard dia complet", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Lloguer de skateboard 24 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Lloguer de skateboard dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| sv | [{"line": 708, "text": "1 timme €6 Perfekt för en snabb tur vid stranden eller för att prova skateboard för första gången.", "price": 6.0}, {"line": 713, "text": "Mest populär 2 timmar €12 Perfekt för en längre tur längs stranden, Port Olímpic och öppna ytor nära Parc de la Ciutadella.", "price": 12.0}, {"line": 719, "text": "3 timmar €15 Bäst om du vill kombinera turer längs kusten med extra tid vid lokala platser för skateboardåkning.", "price": 15.0}, {"line": 724, "text": "Heldag €18 Njut av en hel dag med åkning, upptäckter och stopp där det passar.", "price": 18.0}, {"line": 729, "text": "24 timmar €20 Hämta idag och lämna tillbaka imorgon för att få ut mer av Barcelona på bräda.", "price": 20.0}, {"line": 734, "text": "Extra dag €10 Förläng din skateboardhyra ytterligare en dag till reducerat pris.", "price": 10.0}] | [{"line": 927, "text": "1 timme €6", "price": 6.0}, {"line": 931, "text": "2 timmar €12", "price": 12.0}, {"line": 935, "text": "3 timmar €15", "price": 15.0}, {"line": 939, "text": "Heldag €18", "price": 18.0}, {"line": 943, "text": "24 timmar €20", "price": 20.0}, {"line": 947, "text": "Extra dag €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Hyra skateboard 1 timme", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Hyra skateboard 2 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Hyra skateboard 3 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Hyra skateboard heldag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Hyra skateboard 24 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Hyra skateboard extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| pl | [{"line": 765, "text": "1 godzina €6 Idealne na krótką przejażdżkę przy plaży albo pierwszą próbę jazdy na deskorolce.", "price": 6.0}, {"line": 770, "text": "Najpopularniejsze 2 godziny €12 Idealne na dłuższą jazdę przy plaży, Port Olímpic i otwartych przestrzeniach blisko parku Ciutadella.", "price": 12.0}, {"line": 776, "text": "3 godziny €15 Najlepsze do połączenia spokojnej jazdy nad morzem z dodatkowym czasem na lokalne miejsca do jazdy.", "price": 15.0}, {"line": 781, "text": "Cały dzień €18 Ciesz się całym dniem spokojnej jazdy, odkrywania okolicy i zatrzymywania się tam, gdzie trasa Ci odpowiada.", "price": 18.0}, {"line": 786, "text": "24 godziny €20 Odbierz deskę dziś i zwróć jutro, aby lepiej wykorzystać pobyt w Barcelonie.", "price": 20.0}, {"line": 791, "text": "Dodatkowy dzień €10 Przedłuż wynajem deskorolki o kolejny dzień w niższej cenie.", "price": 10.0}] | [{"line": 982, "text": "1 godzina €6", "price": 6.0}, {"line": 986, "text": "2 godziny €12", "price": 12.0}, {"line": 990, "text": "3 godziny €15", "price": 15.0}, {"line": 994, "text": "Cały dzień €18", "price": 18.0}, {"line": 998, "text": "24 godziny €20", "price": 20.0}, {"line": 1002, "text": "Dodatkowy dzień €10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Wynajem deskorolek 1 godzina", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Wynajem deskorolek 2 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Wynajem deskorolek 3 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Całodniowy wynajem deskorolek", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Wynajem deskorolek 24 godziny", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Dodatkowy dzień wynajmu deskorolek", "url": "https://rentalscooterbarcelona.com/pl/skateboard/", "availability": "https://schema.org/InStock"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |

| Idioma | Ofertas servicio | Ofertas PRICES | Coinciden tarifas base |
| --- | --- | --- | --- |
| en | [["Skateboard rental 1 hour", 6.0], ["Skateboard rental 2 hours", 12.0], ["Skateboard rental 3 hours", 15.0], ["Skateboard rental full day", 18.0], ["Skateboard rental 24 hours", 20.0], ["Skateboard rental extra day", 10.0]] | [["1 hour", 6.0], ["2 hours", 12.0], ["3 hours", 15.0], ["Full day", 18.0], ["24 hours", 20.0], ["Extra day", 10.0], ["1-hour skateboard rental in Barcelona", 6.0]] | True |
| es | [["Alquiler de skateboard 1 hora", 6.0], ["Alquiler de skateboard 2 horas", 12.0], ["Alquiler de skateboard 3 horas", 15.0], ["Alquiler de skateboard día completo", 18.0], ["Alquiler de skateboard 24 horas", 20.0], ["Alquiler de skateboard día extra", 10.0]] | [["1 hora", 6.0], ["2 horas", 12.0], ["3 horas", 15.0], ["Día completo", 18.0], ["24 horas", 20.0], ["Día extra", 10.0], ["Alquiler de skateboard 1 hora en Barcelona", 6.0]] | True |
| fr | [["Location de skateboard 1 heure", 6.0], ["Location de skateboard 2 heures", 12.0], ["Location de skateboard 3 heures", 15.0], ["Location de skateboard journée complète", 18.0], ["Location de skateboard 24 heures", 20.0], ["Location de skateboard journée supplémentaire", 10.0]] | [["1 heure", 6.0], ["2 heures", 12.0], ["3 heures", 15.0], ["Journée complète", 18.0], ["24 heures", 20.0], ["Jour supplémentaire", 10.0], ["Location de skateboard 1 heure à Barcelone", 6.0]] | True |
| it | [["Noleggio skateboard 1 ora", 6.0], ["Noleggio skateboard 2 ore", 12.0], ["Noleggio skateboard 3 ore", 15.0], ["Noleggio skateboard giornata intera", 18.0], ["Noleggio skateboard 24 ore", 20.0], ["Noleggio skateboard giorno extra", 10.0]] | [["1 ora", 6.0], ["2 ore", 12.0], ["3 ore", 15.0], ["Giornata intera", 18.0], ["24 ore", 20.0], ["Giorno extra", 10.0], ["Noleggio skateboard 1 ora a Barcellona", 6.0]] | True |
| de | [["Skateboard-Verleih 1 Stunde", 6.0], ["Skateboard-Verleih 2 Stunden", 12.0], ["Skateboard-Verleih 3 Stunden", 15.0], ["Skateboard-Verleih ganzer Tag", 18.0], ["Skateboard-Verleih 24 Stunden", 20.0], ["Skateboard-Verleih Zusatztag", 10.0]] | [["1 Stunde", 6.0], ["2 Stunden", 12.0], ["3 Stunden", 15.0], ["Ganzer Tag", 18.0], ["24 Stunden", 20.0], ["Zusätzlicher Tag", 10.0], ["Skateboard mieten – 1 Stunde in Barcelona", 6.0]] | True |
| nl | [["Skateboard huren 1 uur", 6.0], ["Skateboard huren 2 uur", 12.0], ["Skateboard huren 3 uur", 15.0], ["Skateboard huren hele dag", 18.0], ["Skateboard huren 24 uur", 20.0], ["Skateboard huren extra dag", 10.0]] | [["1 uur", 6.0], ["2 uur", 12.0], ["3 uur", 15.0], ["Hele dag", 18.0], ["24 uur", 20.0], ["Extra dag", 10.0], ["Skateboard huren voor 1 uur in Barcelona", 6.0]] | True |
| pt | [["Aluguer de skateboard 1 hora", 6.0], ["Aluguer de skateboard 2 horas", 12.0], ["Aluguer de skateboard 3 horas", 15.0], ["Aluguer de skateboard dia completo", 18.0], ["Aluguer de skateboard 24 horas", 20.0], ["Aluguer de skateboard dia extra", 10.0]] | [["1 hora", 6.0], ["2 horas", 12.0], ["3 horas", 15.0], ["Dia completo", 18.0], ["24 horas", 20.0], ["Dia extra", 10.0], ["Aluguer de skateboard por 1 hora em Barcelona", 6.0]] | True |
| ca | [["Lloguer de skateboard 1 hora", 6.0], ["Lloguer de skateboard 2 hores", 12.0], ["Lloguer de skateboard 3 hores", 15.0], ["Lloguer de skateboard dia complet", 18.0], ["Lloguer de skateboard 24 hores", 20.0], ["Lloguer de skateboard dia extra", 10.0]] | [["1 hora", 6.0], ["2 hores", 12.0], ["3 hores", 15.0], ["Dia complet", 18.0], ["24 hores", 20.0], ["Dia extra", 10.0], ["Lloguer de skateboard 1 hora a Barcelona", 6.0]] | True |
| sv | [["Hyra skateboard 1 timme", 6.0], ["Hyra skateboard 2 timmar", 12.0], ["Hyra skateboard 3 timmar", 15.0], ["Hyra skateboard heldag", 18.0], ["Hyra skateboard 24 timmar", 20.0], ["Hyra skateboard extra dag", 10.0]] | [["1 timme", 6.0], ["2 timmar", 12.0], ["3 timmar", 15.0], ["Heldag", 18.0], ["24 timmar", 20.0], ["Extra dag", 10.0], ["Skateboarduthyrning 1 timme i Barcelona", 6.0]] | True |
| pl | [["Wynajem deskorolek 1 godzina", 6.0], ["Wynajem deskorolek 2 godziny", 12.0], ["Wynajem deskorolek 3 godziny", 15.0], ["Całodniowy wynajem deskorolek", 18.0], ["Wynajem deskorolek 24 godziny", 20.0], ["Dodatkowy dzień wynajmu deskorolek", 10.0]] | [["1 godzina", 6.0], ["2 godziny", 12.0], ["3 godziny", 15.0], ["Cały dzień", 18.0], ["24 godziny", 20.0], ["Dodatkowy dzień", 10.0], ["Godzinny wynajem deskorolek w Barcelonie", 6.0]] | True |

## R. MATRIZ POLÍTICAS

Textos completos extraídos por idioma: equipamiento, documentos, depósito, reservas, tallas y condiciones. Ausencia de una mención no equivale a contradicción. El alcance es coherencia del HTML con CANONICAL, no validación legal ni de disponibilidad.

| Idioma | Línea | Texto |
| --- | --- | --- |
| en | 706 | Rent skateboards and cruiser boards from our local shop in Vila Olímpica del Poblenou, near Barceloneta Beach and Port Olímpic. Stable boards for beginners and casual riders, with a children's helmet, wrist guards, knee pads and elbow pads included. Free luggage storage and local route tips. |
| en | 736 | Stable boards for easy rides |
| en | 737 | Choose from quality skateboards and cruiser boards prepared for relaxed rides, beginner sessions and smooth cruising along the coast. |
| en | 741 | A children's helmet, wrist guards, knee pads and elbow pads are included with every rental. |
| en | 745 | Start riding just steps from Barceloneta Beach and Port Olímpic. Explore the seafront promenade, open spaces and nearby skate-friendly areas without long transfers. |
| en | 754 | These are the current public prices for our skateboard and cruiser board rental service. You can also compare all rates on our Prices page, and contact us on WhatsApp to confirm availability before visiting. |
| en | 766 | Ideal for a longer beachfront ride, Port Olímpic and open areas near Ciutadella Park. |
| en | 809 | Children's helmet included with every skateboard rental |
| en | 810 | Knee, elbow &amp; wrist pads included |
| en | 852 | Open every day: 10:30–13:30 and 16:30–20:00. We offer hourly and daily rentals with flexible return times. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental. Our local team can help you choose a stable board, explain the basics and recommend suitable routes. For local route ideas and practical tips, you can read our skateboard rental guide in Barcelona. |
| en | 919 | No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started. |
| en | 922 | Is protective gear included with the rental? |
| en | 923 | Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental. |
| en | 926 | Where can I ride a skateboard near the shop? |
| en | 927 | Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby. |
| en | 931 | Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want. |
| en | 934 | Do I need a licence to rent a skateboard? |
| en | 935 | No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID. |
| en | 939 | Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride. |
| en | 952 | More Barcelona rentals and local guides |
| en | 953 | Discover related rental services from our Vila Olímpica shop and browse local guides across the main activities we offer in Barcelona. |
| en | 1000 | Children's helmet included · Protective gear included · Help choosing the right board · Storage for jackets, backpacks and luggage. |
| es | 700 | Alquila skateboards y tablas cruiser en nuestra tienda local de Vila Olímpica del Poblenou, cerca de la Barceloneta y Port Olímpic. Tablas estables para principiantes y usuarios ocasionales, casco infantil y protecciones incluidos. Consigna gratuita y consejos de rutas locales. |
| es | 731 | Elige entre skateboards y tablas cruiser de calidad, preparados para paseos tranquilos, primeras sesiones y rutas suaves junto al mar. |
| es | 734 | Todo incluido |
| es | 735 | El casco infantil está incluido con cada alquiler, y las protecciones están incluidas. |
| es | 748 | Estos son los precios públicos actuales de nuestro alquiler de skateboard y tablas cruiser. También puedes comparar todas las tarifas en nuestra página de precios y contactarnos por WhatsApp para confirmar la disponibilidad antes de venir. |
| es | 754 | Perfecto para una vuelta rápida por la playa o para probar un skateboard por primera vez. |
| es | 760 | Ideal para una ruta más larga por la playa, el Port Olímpic y zonas abiertas cerca del Parc de la Ciutadella. |
| es | 780 | Amplía tu alquiler de skateboard un día más con una tarifa reducida. |
| es | 803 | Casco infantil incluido con cada alquiler de skateboard |
| es | 804 | Protecciones incluidas |
| es | 806 | Asistencia de nuestro equipo local en la recogida |
| es | 841 | RSB es una tienda local de alquiler en Carrer de Salvador Espriu, cerca de la Vila Olímpica, la playa de la Barceloneta y el Port Olímpic. Es un punto de salida práctico para rodar por el paseo marítimo o probar zonas cercanas aptas para skate en Barcelona. |
| es | 846 | Abierto todos los días: 10:30–13:30 y 16:30–20:00. Ofrecemos alquileres por horas y por días. El casco infantil y las protecciones están incluidos con cada alquiler de skateboard. Nuestro equipo local puede ayudarte a elegir una tabla estable, explicar lo básico y recomendar rutas adecuadas. Para ideas de rutas y consejos prácticos, puedes leer nuestra guía de alquiler de skateboard en Barcelona. |
| es | 909 | ¿Está incluido el equipo de protección? |
| es | 910 | Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas. |
| es | 922 | No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido. |
| es | 930 | Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard. |
| es | 940 | Descubre servicios de alquiler relacionados desde nuestra tienda en la Vila Olímpica y consulta guías locales de las principales actividades que ofrecemos en Barcelona. |
| es | 955 | Precios de alquiler de skateboard y accesorios incluidos |
| es | 987 | Casco infantil incluido · Protecciones incluidas · Ayuda para elegir la tabla adecuada · Consigna para chaquetas, mochilas y maletas. |
| es | 997 | Consulta disponibilidad para tu alquiler de skateboard en Barcelona |
| fr | 639 | Louez des skateboards et des planches cruiser dans notre boutique locale à Vila Olímpica del Poblenou, face à la plage et à côté du Port Olímpic. Planches stables pour débutants et skateurs occasionnels, avec casque pour enfant, protège-poignets, genouillères et coudières inclus. Consigne gratuite et conseils d’itinéraires locaux. |
| fr | 674 | Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location. |
| fr | 687 | Voici les prix publics actuels de notre service de location de skateboard et cruiser board. Vous pouvez aussi comparer tous les tarifs sur notre page des prix, et nous contacter sur WhatsApp pour confirmer la disponibilité avant de venir. |
| fr | 699 | Idéal pour une balade plus longue en bord de mer, le Port Olímpic et les espaces ouverts près du parc de la Ciutadella. |
| fr | 742 | Casque pour enfant inclus avec chaque location de skateboard |
| fr | 743 | Genouillères, coudières et protège-poignets inclus |
| fr | 744 | Aide pour choisir le bon skateboard ou cruiser board |
| fr | 745 | Aide de notre équipe locale au moment du retrait |
| fr | 785 | Ouvert tous les jours : 10:30–13:30 et 16:30–20:00. Nous proposons des locations à l’heure et à la journée. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard. Notre équipe locale peut vous aider à choisir une planche stable, expliquer les bases et recommander des itinéraires adaptés. Pour des idées d’itinéraires et des conseils pratiques, consultez notre guide de location de skateboard à Barcelone. |
| fr | 845 | Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer. |
| fr | 848 | Les protections sont-elles incluses ? |
| fr | 849 | Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard. |
| fr | 857 | Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité. |
| fr | 860 | Faut-il un permis pour louer un skateboard ? |
| fr | 861 | Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide. |
| fr | 882 | Autres locations et guides locaux à Barcelone |
| fr | 883 | Découvrez les services de location associés depuis notre boutique de la Vila Olímpica et consultez nos guides locaux sur les principales activités que nous proposons à Barcelone. |
| fr | 930 | Casque pour enfant, protège-poignets, genouillères et coudières inclus · Aide pour choisir la bonne planche · Consigne pour vestes, sacs à dos et bagages. |
| fr | 941 | Écrivez-nous sur WhatsApp ou passez à notre boutique de la Vila Olímpica pour organiser votre location de skateboard près de la plage de la Barceloneta. Notre équipe vous aidera à choisir la bonne planche et vous recommandera les meilleurs itinéraires ou zones adaptées au skate à proximité. |
| it | 644 | Noleggia skateboard e cruiser board nel nostro negozio locale a Vila Olímpica del Poblenou, vicino alla Barceloneta e a Port Olímpic. Tavole stabili per principianti e rider occasionali, casco per bambini incluso e protezioni incluse per ginocchia, gomiti e polsi. Deposito bagagli gratuito e consigli sui percorsi locali. |
| it | 679 | Un casco per bambini è incluso in ogni noleggio, e le protezioni per ginocchia, gomiti e polsi sono incluse. |
| it | 692 | Questi sono i prezzi pubblici attuali del nostro servizio di noleggio skateboard e cruiser board. Puoi anche confrontare tutte le tariffe nella nostra pagina prezzi, e contattarci su WhatsApp per confermare la disponibilità prima di venire. |
| it | 704 | Ideale per un giro più lungo sul lungomare, al Port Olímpic e negli spazi aperti vicino al Parc de la Ciutadella. |
| it | 724 | Estendi il noleggio dello skateboard per un altro giorno a tariffa ridotta. |
| it | 747 | Casco per bambini incluso con ogni noleggio skateboard |
| it | 748 | Protezioni per ginocchia, gomiti e polsi incluse |
| it | 752 | Deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato |
| it | 790 | Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00. Offriamo noleggi a ore e giornalieri. Un casco per bambini è incluso in ogni noleggio skateboard e le protezioni sono incluse. Il nostro team locale può aiutarti a scegliere una tavola stabile, spiegarti le basi e consigliarti percorsi adatti. Per idee di percorsi e consigli pratici, puoi leggere la nostra guida al noleggio skateboard a Barcellona. |
| it | 850 | No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare. |
| it | 853 | Le protezioni sono incluse nel noleggio? |
| it | 854 | Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse. |
| it | 866 | Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido. |
| it | 870 | Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri. |
| it | 887 | Altri noleggi e guide locali a Barcellona |
| it | 888 | Scopri servizi di noleggio collegati dal nostro negozio nella Vila Olímpica e consulta guide locali sulle principali attività che offriamo a Barcellona. |
| it | 935 | Casco per bambini incluso · Protezioni incluse · Aiuto nella scelta della tavola giusta · Deposito per giacche, zaini e bagagli. |
| de | 646 | Miete Skateboards und Cruiserboards in unserem lokalen Geschäft in Vila Olímpica del Poblenou, direkt gegenüber dem Strand und neben dem Port Olímpic. Stabile Boards für Anfänger und Freizeitfahrer, Kinderhelm und Knie-, Ellbogen- und Handgelenkschoner inklusive. Kostenlose Gepäckaufbewahrung und lokale Routentipps. |
| de | 681 | Ein Kinderhelm ist bei jeder Miete inklusive, Knie-, Ellenbogen- und Handgelenkschoner sind inklusive. |
| de | 706 | Ideal für eine längere Fahrt am Strand, Port Olímpic und offene Bereiche nahe dem Parc de la Ciutadella. |
| de | 749 | Kinderhelm bei jeder Skateboard-Miete inklusive |
| de | 793 | Geöffnet von 10:30–13:30 und 16:30–20:00 Uhr. Wir bieten stundenweise und tageweise Mieten. Ein Kinderhelm ist bei jeder Skateboard-Miete inklusive, Schoner sind inklusive. Unser lokales Team hilft dir bei der Auswahl eines stabilen Boards, erklärt die Grundlagen und empfiehlt passende Routen. Für lokale Routenideen und praktische Tipps lies unseren Guide zum Skateboard-Verleih in Barcelona. |
| de | 867 | Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive. |
| de | 882 | Brauche ich einen Führerschein, um ein Skateboard zu mieten? |
| de | 885 | Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich. |
| de | 913 | Weitere Verleihe und lokale Guides in Barcelona |
| de | 914 | Entdecke weitere Verleihservices unseres Shops in der Vila Olímpica und lokale Guides zu den wichtigsten Aktivitäten, die wir in Barcelona anbieten. |
| de | 961 | Kinderhelm inklusive · Schoner inklusive · Hilfe bei der Wahl des passenden Boards · Aufbewahrung für Jacken, Rucksäcke und Gepäck. |
| nl | 655 | Huur skateboards en cruiserboards bij onze lokale winkel in Vila Olímpica del Poblenou, tegenover het strand en naast Port Olímpic. Stabiele boards voor beginners en recreatieve rijders, kinderhelm inbegrepen en knie-, elleboog- en polsbeschermers inbegrepen. Gratis bagageopslag en lokale routetips. |
| nl | 690 | Een kinderhelm is inbegrepen bij elke huur, en knie-, elleboog- en polsbescherming is inbegrepen. |
| nl | 703 | Dit zijn de actuele openbare prijzen voor onze skateboard- en cruiser board-verhuur. Je kunt alle tarieven ook vergelijken op onze prijzenpagina en via WhatsApp contact met ons opnemen om de beschikbaarheid te bevestigen voordat je langskomt. |
| nl | 715 | Ideaal voor een langere rit langs het strand, Port Olímpic en open ruimtes bij Parc de la Ciutadella. |
| nl | 758 | Kinderhelm inbegrepen bij elke skateboardhuur |
| nl | 759 | Knie-, elleboog- en polsbeschermers inbegrepen |
| nl | 802 | Elke dag geopend: 10:30–13:30 en 16:30–20:00. We bieden verhuur per uur en per dag. Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze gids voor skateboard huren in Barcelona. |
| nl | 876 | Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen. |
| nl | 891 | Heb ik een rijbewijs nodig om een skateboard te huren? |
| nl | 894 | Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID. |
| nl | 907 | Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken. |
| nl | 913 | Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen. |
| nl | 922 | Meer verhuur en lokale gidsen in Barcelona |
| nl | 923 | Ontdek gerelateerde verhuurdiensten vanuit onze shop in Vila Olímpica en bekijk lokale gidsen voor de belangrijkste activiteiten die we in Barcelona aanbieden. |
| nl | 970 | Kinderhelm inbegrepen · Beschermers inbegrepen · Hulp bij het kiezen van het juiste board · Opslag voor jassen, rugzakken en bagage. |
| nl | 980 | Check beschikbaarheid voor skateboard huren in Barcelona |
| pt | 661 | Aluga skateboards e cruiser boards na nossa loja local em Vila Olímpica del Poblenou, perto da Barceloneta e do Port Olímpic. Pranchas estáveis para principiantes e riders casuais, capacete infantil e proteções para joelhos, cotovelos e pulsos incluídos. Dispomos de um serviço gratuito de guarda de bagagem e damos dicas de rotas locais. |
| pt | 692 | Escolhe entre skateboards e cruiser boards de qualidade, preparados para passeios tranquilos, primeiras sessões e cruising suave junto à costa. |
| pt | 696 | Um capacete infantil está incluído em cada aluguer, e proteções de joelhos, cotovelos e pulsos estão incluídas. |
| pt | 709 | Estes são os preços públicos atuais do nosso serviço de aluguer de skateboard e cruiser board. Também podes comparar todas as tarifas na nossa página de preços, e contactar-nos por WhatsApp para confirmar disponibilidade antes de vir. |
| pt | 715 | Perfeito para uma volta rápida junto à praia ou para experimentar um skateboard pela primeira vez. |
| pt | 721 | Ideal para um passeio mais longo junto à praia, Port Olímpic e espaços abertos perto do Parc de la Ciutadella. |
| pt | 741 | Prolonga o teu aluguer de skateboard por mais um dia com tarifa reduzida. |
| pt | 764 | Capacete infantil incluído em cada aluguer de skateboard |
| pt | 765 | Proteções para joelhos, cotovelos e pulsos incluídas |
| pt | 769 | Serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada |
| pt | 802 | A RSB é uma loja local de aluguer na Carrer de Salvador Espriu, perto da Vila Olímpica, da praia da Barceloneta e do Port Olímpic. É um ponto de partida prático para andar junto ao mar ou explorar zonas próximas adequadas para skate em Barcelona. |
| pt | 807 | Aberto todos os dias: 10:30–13:30 e 16:30–20:00. Oferecemos alugueres à hora e ao dia com devoluções flexíveis. Um capacete infantil está incluído em cada aluguer de skateboard e as proteções estão incluídas. A nossa equipa local pode ajudar-te a escolher uma tábua estável, explicar o básico e recomendar percursos adequados. Para ideias de percursos locais e dicas práticas, lê o nosso guia de aluguer de skateboard em Barcelona. |
| pt | 873 | Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar. |
| pt | 876 | O equipamento de proteção está incluído? |
| pt | 877 | Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas. |
| pt | 889 | Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido. |
| pt | 893 | Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas. |
| pt | 897 | Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento. |
| pt | 901 | Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard. |
| pt | 911 | Descobre serviços de aluguer relacionados na nossa loja da Vila Olímpica e consulta guias locais das principais atividades que oferecemos em Barcelona. |
| pt | 958 | Capacete infantil incluído · Proteções incluídas · Ajuda para escolher a tábua certa · Guarda de casacos, mochilas e bagagem. |
| pt | 968 | Confirma disponibilidade para o teu aluguer de skateboard em Barcelona |
| pt | 969 | Envia-nos mensagem por WhatsApp ou visita a nossa loja na Vila Olímpica para organizar o teu aluguer de skateboard perto da praia da Barceloneta. A nossa equipa ajuda-te a escolher a tábua certa e recomenda os melhores percursos ou zonas adequadas para skate nas proximidades. |
| ca | 644 | Lloga skateboards i cruiser boards a la nostra botiga local de Vila Olímpica del Poblenou, a prop de la Barceloneta i Port Olímpic. Taules estables per a principiants i persones amb experiència, casc infantil inclòs i proteccions incloses per a genolls, colzes i canells. Servei gratuït de guarda d’equipatge i consells de ruta locals. |
| ca | 679 | El casc infantil està inclòs amb cada lloguer, i les proteccions estan incloses. |
| ca | 698 | Perfecte per fer una volta ràpida per la platja o provar un skateboard per primera vegada. |
| ca | 704 | Ideal per a una ruta més llarga pel front marítim, el Port Olímpic i espais oberts prop del Parc de la Ciutadella. |
| ca | 747 | Casc infantil inclòs amb cada lloguer de skateboard |
| ca | 748 | Proteccions per a genolls, colzes i canells sempre incloses |
| ca | 750 | Suport del nostre equip local en la recollida |
| ca | 753 | Servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada |
| ca | 786 | RSB és una botiga local de lloguer al Carrer de Salvador Espriu, a prop de la Vila Olímpica, la platja de la Barceloneta i el Port Olímpic. És un punt de sortida pràctic per rodar pel front marítim o provar zones properes aptes per a skate a Barcelona. |
| ca | 791 | Obert cada dia: 10:30–13:30 i 16:30–20:00. Oferim lloguers per hores i per dies. El casc infantil està inclòs amb cada lloguer de skateboard i les proteccions estan incloses. El nostre equip local pot ajudar-te a triar una taula estable, explicar-te els bàsics i recomanar rutes adequades. Per a idees de rutes locals i consells pràctics, pots llegir la nostra guia de lloguer de skateboard a Barcelona. |
| ca | 860 | L’equip de protecció està inclòs? |
| ca | 861 | Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses. |
| ca | 873 | No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid. |
| ca | 877 | Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes. |
| ca | 881 | Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida. |
| ca | 942 | Casc infantil inclòs · Proteccions incloses · Ajuda per triar la taula adequada · Guarda d’equipatge per a jaquetes, motxilles i maletes. |
| sv | 657 | Hyr skateboards och cruiserbrädor från vår lokala butik i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Stabila brädor för nybörjare och avslappnade åkare, barnhjälm och knä-, armbågs- och handledsskydd ingår. Gratis bagageförvaring och lokala ruttips. |
| sv | 692 | Barnhjälm ingår i varje hyra, och knä-, armbågs- och handledsskydd ingår. |
| sv | 705 | Det här är de aktuella offentliga priserna för vår uthyrning av skateboard och cruiserbräda. Du kan också jämföra alla priser på vår prissida, och kontakta oss på WhatsApp för att bekräfta tillgänglighet innan du kommer. |
| sv | 711 | Perfekt för en snabb tur vid stranden eller för att prova skateboard för första gången. |
| sv | 722 | Bäst om du vill kombinera turer längs kusten med extra tid vid lokala platser för skateboardåkning. |
| sv | 732 | Hämta idag och lämna tillbaka imorgon för att få ut mer av Barcelona på bräda. |
| sv | 760 | Barnhjälm ingår i varje skateboardhyra |
| sv | 763 | Hjälp av vårt lokala team vid upphämtning |
| sv | 804 | Öppet varje dag: 10:30–13:30 och 16:30–20:00. Vi erbjuder uthyrning per timme och per dag. Barnhjälm ingår i varje skateboardhyra och skydd ingår. Vårt lokala team kan hjälpa dig att välja en stabil bräda, förklara grunderna och rekommendera passande rutter. För lokala rutttips och praktiska råd kan du läsa vår guide till skateboarduthyrning i Barcelona. |
| sv | 870 | Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med. |
| sv | 874 | Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår. |
| sv | 885 | Behöver jag körkort för att hyra skateboard? |
| sv | 886 | Nej. Inget körkort krävs för att hyra en skateboard. |
| sv | 895 | Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid. |
| sv | 899 | Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard. |
| sv | 908 | Fler uthyrningar och lokala guider i Barcelona |
| sv | 909 | Upptäck relaterade uthyrningstjänster från vår butik i Vila Olímpica och läs lokala guider om de viktigaste aktiviteterna vi erbjuder i Barcelona. |
| sv | 920 | Hyra rullskridskor i Barcelona |
| sv | 956 | Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår · Hjälp att välja rätt bräda · Förvaring för jackor, ryggsäckar och bagage. |
| pl | 714 | Wynajmij deskorolki i cruisery w naszej lokalnej wypożyczalni w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Stabilne deski dla początkujących i osób jeżdżących rekreacyjnie, kask dziecięcy oraz ochraniacze na kolana, łokcie i nadgarstki w cenie. Darmowe przechowanie bagażu i lokalne wskazówki tras. |
| pl | 749 | Kask dziecięcy jest w cenie każdego wynajmu, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę. |
| pl | 768 | Idealne na krótką przejażdżkę przy plaży albo pierwszą próbę jazdy na deskorolce. |
| pl | 774 | Idealne na dłuższą jazdę przy plaży, Port Olímpic i otwartych przestrzeniach blisko parku Ciutadella. |
| pl | 817 | Kask dziecięcy jest wliczony w każdy wynajem deskorolki. |
| pl | 861 | Otwarte codziennie: 10:30–13:30 i 16:30–20:00. Oferujemy wynajem na godziny i dni. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze są wliczone w cenę. Nasz lokalny zespół pomoże wybrać stabilną deskę, wyjaśni podstawy i poleci odpowiednie trasy. Lokalne pomysły na trasy i praktyczne wskazówki znajdziesz w naszym przewodniku po wynajmie deskorolek w Barcelonie. |
| pl | 929 | Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę. |
| pl | 941 | Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy. |
| pl | 1011 | Kask dziecięcy w cenie · Ochraniacze w cenie · Pomoc w wyborze odpowiedniej deski · Przechowanie kurtek, plecaków i bagażu. |

## S. MATRIZ FAQ VISIBLE ↔ SCHEMA

| Idioma | N.º | Visible completo | Schema completo | Pregunta coincide | Respuesta coincide |
| --- | --- | --- | --- | --- | --- |
| en | 1 | {"line": 917, "question": "Do I need experience to rent a skateboard?", "answer": "No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Do I need experience to rent a skateboard?", "answer": "No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started.", "answer_raw": "No, you do not need previous experience. We rent skateboards to beginners and confident riders, and our staff can help you choose a comfortable board to get started."} | True | True |
| en | 2 | {"line": 921, "question": "Is protective gear included with the rental?", "answer": "Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Is protective gear included with the rental?", "answer": "Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental.", "answer_raw": "Yes. A children's helmet, wrist guards, knee pads and elbow pads are included with every skateboard rental."} | True | True |
| en | 3 | {"line": 925, "question": "Where can I ride a skateboard near the shop?", "answer": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Where can I ride a skateboard near the shop?", "answer": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby.", "answer_raw": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring more skate-friendly spots nearby."} | True | True |
| en | 4 | {"line": 929, "question": "Do you have skateboards for beginners?", "answer": "Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Do you have skateboards for beginners?", "answer": "Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want.", "answer_raw": "Yes. We can help you choose a stable skateboard or cruiser board depending on your experience and the kind of ride you want."} | True | True |
| en | 5 | {"line": 933, "question": "Do I need a licence to rent a skateboard?", "answer": "No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Do I need a licence to rent a skateboard?", "answer": "No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID.", "answer_raw": "No driving licence is needed. Skateboards are a non-motorised activity, so anyone can rent one with a valid ID."} | True | True |
| en | 6 | {"line": 937, "question": "Can I store my bag or luggage at the shop?", "answer": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Can I store my bag or luggage at the shop?", "answer": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride.", "answer_raw": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride."} | True | True |
| en | 7 | {"line": 941, "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Contact us if you want to confirm board availability or the best time to collect your skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Contact us if you want to confirm board availability or the best time to collect your skateboard.", "answer_raw": "You can book via WhatsApp, email or phone. Contact us if you want to confirm board availability or the best time to collect your skateboard."} | True | True |
| es | 1 | {"line": 904, "question": "¿Necesito experiencia para alquilar un skateboard?", "answer": "No, no necesitas experiencia previa. Alquilamos skateboards a principiantes y personas con experiencia, y nuestro equipo puede ayudarte a elegir una tabla cómoda para empezar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "¿Necesito experiencia para alquilar un skateboard?", "answer": "No, no necesitas experiencia previa. Alquilamos skateboards a principiantes y personas con experiencia, y nuestro equipo puede ayudarte a elegir una tabla cómoda para empezar.", "answer_raw": "No, no necesitas experiencia previa. Alquilamos skateboards a principiantes y personas con experiencia, y nuestro equipo puede ayudarte a elegir una tabla cómoda para empezar."} | True | True |
| es | 2 | {"line": 908, "question": "¿Está incluido el equipo de protección?", "answer": "Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "¿Está incluido el equipo de protección?", "answer": "Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas.", "answer_raw": "Sí. El casco infantil está incluido con cada alquiler de skateboard, y las rodilleras, coderas y muñequeras están incluidas."} | True | True |
| es | 3 | {"line": 912, "question": "¿Dónde puedo usar un skateboard cerca de la tienda?", "answer": "Nuestra tienda está cerca del paseo marítimo, el Port Olímpic y zonas abiertas donde muchos visitantes empiezan con una ruta tranquila antes de explorar otros espacios aptos para skate.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "¿Dónde puedo usar un skateboard cerca de la tienda?", "answer": "Nuestra tienda está cerca del paseo marítimo, el Port Olímpic y zonas abiertas donde muchos visitantes empiezan con una ruta tranquila antes de explorar otros espacios aptos para skate.", "answer_raw": "Nuestra tienda está cerca del paseo marítimo, el Port Olímpic y zonas abiertas donde muchos visitantes empiezan con una ruta tranquila antes de explorar otros espacios aptos para skate."} | True | True |
| es | 4 | {"line": 916, "question": "¿Tenéis skateboards para principiantes?", "answer": "Sí. Podemos ayudarte a elegir un skateboard estable o una tabla cruiser según tu experiencia y el tipo de ruta que quieras hacer.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "¿Tenéis skateboards para principiantes?", "answer": "Sí. Podemos ayudarte a elegir un skateboard estable o una tabla cruiser según tu experiencia y el tipo de ruta que quieras hacer.", "answer_raw": "Sí. Podemos ayudarte a elegir un skateboard estable o una tabla cruiser según tu experiencia y el tipo de ruta que quieras hacer."} | True | True |
| es | 5 | {"line": 920, "question": "¿Necesito carnet para alquilar un skateboard?", "answer": "No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "¿Necesito carnet para alquilar un skateboard?", "answer": "No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido.", "answer_raw": "No se necesita carnet de conducir. El skateboard es una actividad no motorizada, así que cualquiera puede alquilar uno con un DNI o pasaporte válido."} | True | True |
| es | 6 | {"line": 924, "question": "¿Puedo dejar mi mochila o equipaje en la tienda?", "answer": "Sí. Ofrecemos consigna gratuita para chaquetas, mochilas y maletas en nuestra tienda supervisada mientras ruedas.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "¿Puedo dejar mi mochila o equipaje en la tienda?", "answer": "Sí. Ofrecemos consigna gratuita para chaquetas, mochilas y maletas en nuestra tienda supervisada mientras ruedas.", "answer_raw": "Sí. Ofrecemos consigna gratuita para chaquetas, mochilas y maletas en nuestra tienda supervisada mientras ruedas."} | True | True |
| es | 7 | {"line": 928, "question": "¿Cómo reservo o contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "¿Cómo reservo o contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard.", "answer_raw": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de tablas o la mejor hora para recoger tu skateboard."} | True | True |
| fr | 1 | {"line": 843, "question": "Faut-il de l’expérience pour louer un skateboard ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Faut-il de l’expérience pour louer un skateboard ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer.", "answer_raw": "Non, aucune expérience préalable n’est nécessaire. Nous louons des skateboards aux débutants comme aux riders plus à l’aise, et notre équipe peut vous aider à choisir une planche confortable pour commencer."} | True | True |
| fr | 2 | {"line": 847, "question": "Les protections sont-elles incluses ?", "answer": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Les protections sont-elles incluses ?", "answer": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard.", "answer_raw": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de skateboard."} | True | True |
| fr | 3 | {"line": 851, "question": "Où puis-je faire du skateboard près de la boutique ?", "answer": "Notre boutique est proche de la promenade maritime, du Port Olímpic et d’espaces ouverts où beaucoup de visiteurs commencent tranquillement avant d’explorer d’autres zones adaptées au skate.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Où puis-je faire du skateboard près de la boutique ?", "answer": "Notre boutique est proche de la promenade maritime, du Port Olímpic et d’espaces ouverts où beaucoup de visiteurs commencent tranquillement avant d’explorer d’autres zones adaptées au skate.", "answer_raw": "Notre boutique est proche de la promenade maritime, du Port Olímpic et d’espaces ouverts où beaucoup de visiteurs commencent tranquillement avant d’explorer d’autres zones adaptées au skate."} | True | True |
| fr | 4 | {"line": 855, "question": "Avez-vous des skateboards pour débutants ?", "answer": "Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Avez-vous des skateboards pour débutants ?", "answer": "Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité.", "answer_raw": "Oui. Nous pouvons vous aider à choisir un skateboard stable ou un cruiser board selon votre expérience et le type de balade souhaité."} | True | True |
| fr | 5 | {"line": 859, "question": "Faut-il un permis pour louer un skateboard ?", "answer": "Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Faut-il un permis pour louer un skateboard ?", "answer": "Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide.", "answer_raw": "Aucun permis n’est nécessaire. Le skateboard est une activité non motorisée, donc toute personne peut en louer un avec une pièce d’identité valide."} | True | True |
| fr | 6 | {"line": 863, "question": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "answer": "Oui. Une consigne gratuite pour vestes, sacs à dos et bagages est disponible dans notre boutique surveillée pendant votre sortie.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "answer": "Oui. Une consigne gratuite pour vestes, sacs à dos et bagages est disponible dans notre boutique surveillée pendant votre sortie.", "answer_raw": "Oui. Une consigne gratuite pour vestes, sacs à dos et bagages est disponible dans notre boutique surveillée pendant votre sortie."} | True | True |
| fr | 7 | {"line": 867, "question": "Puis-je réserver ou poser des questions par WhatsApp ?", "answer": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puis-je réserver ou poser des questions par WhatsApp ?", "answer": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait.", "answer_raw": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait."} | True | True |
| fr | 8 | {"line": 871, "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver par WhatsApp, email ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des planches ou le meilleur moment pour récupérer votre skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver par WhatsApp, email ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des planches ou le meilleur moment pour récupérer votre skateboard.", "answer_raw": "Vous pouvez réserver par WhatsApp, email ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des planches ou le meilleur moment pour récupérer votre skateboard."} | True | True |
| it | 1 | {"line": 848, "question": "Serve esperienza per noleggiare uno skateboard?", "answer": "No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Serve esperienza per noleggiare uno skateboard?", "answer": "No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare.", "answer_raw": "No, non serve esperienza precedente. Noleggiamo skateboard sia a principianti sia a rider più sicuri, e il nostro staff può aiutarti a scegliere una tavola comoda per iniziare."} | True | True |
| it | 2 | {"line": 852, "question": "Le protezioni sono incluse nel noleggio?", "answer": "Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Le protezioni sono incluse nel noleggio?", "answer": "Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse.", "answer_raw": "Sì. Un casco per bambini è incluso in ogni noleggio skateboard, e le protezioni per ginocchia, gomiti e polsi sono incluse."} | True | True |
| it | 3 | {"line": 856, "question": "Dove posso andare in skateboard vicino al negozio?", "answer": "Il nostro negozio è vicino al lungomare, al Port Olímpic e a spazi aperti dove molti visitatori iniziano con un giro tranquillo prima di esplorare altri spot adatti allo skate.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Dove posso andare in skateboard vicino al negozio?", "answer": "Il nostro negozio è vicino al lungomare, al Port Olímpic e a spazi aperti dove molti visitatori iniziano con un giro tranquillo prima di esplorare altri spot adatti allo skate.", "answer_raw": "Il nostro negozio è vicino al lungomare, al Port Olímpic e a spazi aperti dove molti visitatori iniziano con un giro tranquillo prima di esplorare altri spot adatti allo skate."} | True | True |
| it | 4 | {"line": 860, "question": "Avete skateboard per principianti?", "answer": "Sì. Possiamo aiutarti a scegliere uno skateboard stabile o un cruiser board in base alla tua esperienza e al tipo di giro che vuoi fare.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Avete skateboard per principianti?", "answer": "Sì. Possiamo aiutarti a scegliere uno skateboard stabile o un cruiser board in base alla tua esperienza e al tipo di giro che vuoi fare.", "answer_raw": "Sì. Possiamo aiutarti a scegliere uno skateboard stabile o un cruiser board in base alla tua esperienza e al tipo di giro che vuoi fare."} | True | True |
| it | 5 | {"line": 864, "question": "Serve una patente per noleggiare uno skateboard?", "answer": "Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Serve una patente per noleggiare uno skateboard?", "answer": "Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido.", "answer_raw": "Non serve patente. Lo skateboard è un’attività non motorizzata, quindi chiunque può noleggiarne uno con un documento valido."} | True | True |
| it | 6 | {"line": 868, "question": "Posso lasciare borsa o bagagli in negozio?", "answer": "Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Posso lasciare borsa o bagagli in negozio?", "answer": "Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri.", "answer_raw": "Sì. È disponibile un deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato mentre giri."} | True | True |
| it | 7 | {"line": 872, "question": "Posso prenotare o fare domande su WhatsApp?", "answer": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare disponibilità, fare domande o organizzare l’orario di ritiro.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso prenotare o fare domande su WhatsApp?", "answer": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare disponibilità, fare domande o organizzare l’orario di ritiro.", "answer_raw": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare disponibilità, fare domande o organizzare l’orario di ritiro."} | True | True |
| it | 8 | {"line": 876, "question": "Come prenoto o vi contatto?", "answer": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle tavole o il momento migliore per ritirare il tuo skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Come prenoto o vi contatto?", "answer": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle tavole o il momento migliore per ritirare il tuo skateboard.", "answer_raw": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle tavole o il momento migliore per ritirare il tuo skateboard."} | True | True |
| de | 1 | {"line": 857, "question": "Brauche ich Erfahrung, um ein Skateboard zu mieten?", "answer": "Nein, du brauchst keine Vorerfahrung. Wir vermieten Skateboards an Anfänger und erfahrene Skater, und unser Team hilft dir, ein komfortables Board für den Einstieg zu wählen.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Brauche ich Erfahrung, um ein Skateboard zu mieten?", "answer": "Nein, du brauchst keine Vorerfahrung. Wir vermieten Skateboards an Anfänger und erfahrene Skater, und unser Team hilft dir, ein komfortables Board für den Einstieg zu wählen.", "answer_raw": "Nein, du brauchst keine Vorerfahrung. Wir vermieten Skateboards an Anfänger und erfahrene Skater, und unser Team hilft dir, ein komfortables Board für den Einstieg zu wählen."} | True | True |
| de | 2 | {"line": 863, "question": "Ist Schutzausrüstung in der Miete enthalten?", "answer": "Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Ist Schutzausrüstung in der Miete enthalten?", "answer": "Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive.", "answer_raw": "Ja. Ein Kinderhelm ist bei jeder Skateboard-Miete enthalten, und Knie-, Ellenbogen- und Handgelenkschoner sind inklusive."} | True | True |
| de | 3 | {"line": 869, "question": "Wo kann ich in der Nähe des Shops Skateboard fahren?", "answer": "Unser Shop liegt nahe der Strandpromenade, dem Port Olímpic und offenen Flächen, wo viele Besucher entspannt starten, bevor sie weitere geeignete Bereiche zum Skaten in der Nähe erkunden.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Wo kann ich in der Nähe des Shops Skateboard fahren?", "answer": "Unser Shop liegt nahe der Strandpromenade, dem Port Olímpic und offenen Flächen, wo viele Besucher entspannt starten, bevor sie weitere geeignete Bereiche zum Skaten in der Nähe erkunden.", "answer_raw": "Unser Shop liegt nahe der Strandpromenade, dem Port Olímpic und offenen Flächen, wo viele Besucher entspannt starten, bevor sie weitere geeignete Bereiche zum Skaten in der Nähe erkunden."} | True | True |
| de | 4 | {"line": 875, "question": "Habt ihr Skateboards für Anfänger?", "answer": "Ja. Wir helfen dir, je nach Erfahrung und gewünschter Fahrt ein stabiles Skateboard oder Cruiserboard auszuwählen.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Habt ihr Skateboards für Anfänger?", "answer": "Ja. Wir helfen dir, je nach Erfahrung und gewünschter Fahrt ein stabiles Skateboard oder Cruiserboard auszuwählen.", "answer_raw": "Ja. Wir helfen dir, je nach Erfahrung und gewünschter Fahrt ein stabiles Skateboard oder Cruiserboard auszuwählen."} | True | True |
| de | 5 | {"line": 881, "question": "Brauche ich einen Führerschein, um ein Skateboard zu mieten?", "answer": "Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Brauche ich einen Führerschein, um ein Skateboard zu mieten?", "answer": "Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich.", "answer_raw": "Nein. Für die Skateboard-Miete ist kein Führerschein erforderlich."} | True | True |
| de | 6 | {"line": 887, "question": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "answer": "Ja. Kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck ist in unserem betreuten Shop möglich, während du fährst.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "answer": "Ja. Kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck ist in unserem betreuten Shop möglich, während du fährst.", "answer_raw": "Ja. Kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck ist in unserem betreuten Shop möglich, während du fährst."} | True | True |
| de | 7 | {"line": 894, "question": "Kann ich per WhatsApp buchen oder Fragen stellen?", "answer": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um die Verfügbarkeit zu bestätigen, Fragen zu stellen oder deine Abholzeit zu vereinbaren.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kann ich per WhatsApp buchen oder Fragen stellen?", "answer": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um die Verfügbarkeit zu bestätigen, Fragen zu stellen oder deine Abholzeit zu vereinbaren.", "answer_raw": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um die Verfügbarkeit zu bestätigen, Fragen zu stellen oder deine Abholzeit zu vereinbaren."} | True | True |
| de | 8 | {"line": 900, "question": "Wie buche ich oder kontaktiere euch?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Board-Verfügbarkeit oder den besten Abholzeitpunkt bestätigen möchtest.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Wie buche ich oder kontaktiere euch?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Board-Verfügbarkeit oder den besten Abholzeitpunkt bestätigen möchtest.", "answer_raw": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Board-Verfügbarkeit oder den besten Abholzeitpunkt bestätigen möchtest."} | True | True |
| nl | 1 | {"line": 866, "question": "Heb ik ervaring nodig om een skateboard te huren?", "answer": "Nee, je hebt geen ervaring nodig. We verhuren skateboards aan beginners en ervaren skaters, en ons team helpt je een comfortabel board te kiezen om te starten.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Heb ik ervaring nodig om een skateboard te huren?", "answer": "Nee, je hebt geen ervaring nodig. We verhuren skateboards aan beginners en ervaren skaters, en ons team helpt je een comfortabel board te kiezen om te starten.", "answer_raw": "Nee, je hebt geen ervaring nodig. We verhuren skateboards aan beginners en ervaren skaters, en ons team helpt je een comfortabel board te kiezen om te starten."} | True | True |
| nl | 2 | {"line": 872, "question": "Is bescherming inbegrepen bij de huur?", "answer": "Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Is bescherming inbegrepen bij de huur?", "answer": "Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen.", "answer_raw": "Ja. Een kinderhelm is inbegrepen bij elke skateboardhuur, en knie-, elleboog- en polsbescherming is inbegrepen."} | True | True |
| nl | 3 | {"line": 878, "question": "Waar kan ik skateboarden in de buurt van de shop?", "answer": "Onze shop ligt dicht bij de boulevard, Port Olímpic en open ruimtes waar veel bezoekers rustig beginnen voordat ze meer skatevriendelijke plekken in de buurt ontdekken.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Waar kan ik skateboarden in de buurt van de shop?", "answer": "Onze shop ligt dicht bij de boulevard, Port Olímpic en open ruimtes waar veel bezoekers rustig beginnen voordat ze meer skatevriendelijke plekken in de buurt ontdekken.", "answer_raw": "Onze shop ligt dicht bij de boulevard, Port Olímpic en open ruimtes waar veel bezoekers rustig beginnen voordat ze meer skatevriendelijke plekken in de buurt ontdekken."} | True | True |
| nl | 4 | {"line": 884, "question": "Hebben jullie skateboards voor beginners?", "answer": "Ja. We kunnen je helpen een stabiel skateboard of cruiser board te kiezen, afhankelijk van je ervaring en het soort rit dat je wilt.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Hebben jullie skateboards voor beginners?", "answer": "Ja. We kunnen je helpen een stabiel skateboard of cruiser board te kiezen, afhankelijk van je ervaring en het soort rit dat je wilt.", "answer_raw": "Ja. We kunnen je helpen een stabiel skateboard of cruiser board te kiezen, afhankelijk van je ervaring en het soort rit dat je wilt."} | True | True |
| nl | 5 | {"line": 890, "question": "Heb ik een rijbewijs nodig om een skateboard te huren?", "answer": "Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Heb ik een rijbewijs nodig om een skateboard te huren?", "answer": "Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID.", "answer_raw": "Nee, er is geen rijbewijs nodig. Skateboards zijn niet gemotoriseerd, dus iedereen kan er een huren met een geldig ID."} | True | True |
| nl | 6 | {"line": 896, "question": "Kan ik mijn tas of bagage in de shop achterlaten?", "answer": "Ja. Gratis opslag voor jassen, rugzakken en bagage is beschikbaar in onze bewaakte shop terwijl je rijdt.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kan ik mijn tas of bagage in de shop achterlaten?", "answer": "Ja. Gratis opslag voor jassen, rugzakken en bagage is beschikbaar in onze bewaakte shop terwijl je rijdt.", "answer_raw": "Ja. Gratis opslag voor jassen, rugzakken en bagage is beschikbaar in onze bewaakte shop terwijl je rijdt."} | True | True |
| nl | 7 | {"line": 903, "question": "Kan ik reserveren of vragen stellen via WhatsApp?", "answer": "Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan ik reserveren of vragen stellen via WhatsApp?", "answer": "Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken.", "answer_raw": "Ja. Je kunt ons via WhatsApp berichten voor je komt om beschikbaarheid te bevestigen, vragen te stellen of je ophaaltijd af te spreken."} | True | True |
| nl | 8 | {"line": 909, "question": "Hoe reserveer ik of neem ik contact met jullie op?", "answer": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hoe reserveer ik of neem ik contact met jullie op?", "answer": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen.", "answer_raw": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact op als je de beschikbaarheid van boards of het beste ophaalmoment wilt bevestigen."} | True | True |
| pt | 1 | {"line": 871, "question": "Preciso de experiência para alugar um skateboard?", "answer": "Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Preciso de experiência para alugar um skateboard?", "answer": "Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar.", "answer_raw": "Não, não precisas de experiência prévia. Alugamos skateboards a principiantes e riders confiantes, e a nossa equipa pode ajudar-te a escolher uma tábua confortável para começar."} | True | True |
| pt | 2 | {"line": 875, "question": "O equipamento de proteção está incluído?", "answer": "Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "O equipamento de proteção está incluído?", "answer": "Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas.", "answer_raw": "Sim. Um capacete infantil está incluído em cada aluguer de skateboard, e proteções de joelhos, cotovelos e pulsos estão incluídas."} | True | True |
| pt | 3 | {"line": 879, "question": "Onde posso andar de skateboard perto da loja?", "answer": "A nossa loja fica perto do passeio marítimo, do Port Olímpic e de espaços abertos onde muitos visitantes começam com uma volta tranquila antes de explorar outros spots próximos adequados para skate.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Onde posso andar de skateboard perto da loja?", "answer": "A nossa loja fica perto do passeio marítimo, do Port Olímpic e de espaços abertos onde muitos visitantes começam com uma volta tranquila antes de explorar outros spots próximos adequados para skate.", "answer_raw": "A nossa loja fica perto do passeio marítimo, do Port Olímpic e de espaços abertos onde muitos visitantes começam com uma volta tranquila antes de explorar outros spots próximos adequados para skate."} | True | True |
| pt | 4 | {"line": 883, "question": "Têm skateboards para principiantes?", "answer": "Sim. Podemos ajudar-te a escolher um skateboard estável ou um cruiser board conforme a tua experiência e o tipo de passeio que procuras.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Têm skateboards para principiantes?", "answer": "Sim. Podemos ajudar-te a escolher um skateboard estável ou um cruiser board conforme a tua experiência e o tipo de passeio que procuras.", "answer_raw": "Sim. Podemos ajudar-te a escolher um skateboard estável ou um cruiser board conforme a tua experiência e o tipo de passeio que procuras."} | True | True |
| pt | 5 | {"line": 887, "question": "Preciso de carta para alugar um skateboard?", "answer": "Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Preciso de carta para alugar um skateboard?", "answer": "Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido.", "answer_raw": "Não é necessária carta de condução. O skateboard é uma atividade não motorizada, por isso qualquer pessoa pode alugar um com documento válido."} | True | True |
| pt | 6 | {"line": 891, "question": "Posso deixar a minha mochila ou bagagem na loja?", "answer": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Posso deixar a minha mochila ou bagagem na loja?", "answer": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas.", "answer_raw": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e bagagem na nossa loja supervisionada enquanto andas."} | True | True |
| pt | 7 | {"line": 895, "question": "Posso reservar ou fazer perguntas por WhatsApp?", "answer": "Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso reservar ou fazer perguntas por WhatsApp?", "answer": "Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento.", "answer_raw": "Sim. Podes enviar-nos mensagem no WhatsApp antes de vir para confirmar disponibilidade, fazer perguntas ou combinar a hora de levantamento."} | True | True |
| pt | 8 | {"line": 899, "question": "Como faço a reserva ou contacto convosco?", "answer": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Como faço a reserva ou contacto convosco?", "answer": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard.", "answer_raw": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade de tábuas ou a melhor hora para levantar o teu skateboard."} | True | True |
| ca | 1 | {"line": 855, "question": "Necessito experiència per llogar un skateboard?", "answer": "No, no necessites experiència prèvia. Lloguem skateboards a principiants i persones amb experiència, i el nostre equip pot ajudar-te a triar una taula còmoda per començar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Necessito experiència per llogar un skateboard?", "answer": "No, no necessites experiència prèvia. Lloguem skateboards a principiants i persones amb experiència, i el nostre equip pot ajudar-te a triar una taula còmoda per començar.", "answer_raw": "No, no necessites experiència prèvia. Lloguem skateboards a principiants i persones amb experiència, i el nostre equip pot ajudar-te a triar una taula còmoda per començar."} | True | True |
| ca | 2 | {"line": 859, "question": "L’equip de protecció està inclòs?", "answer": "Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "L’equip de protecció està inclòs?", "answer": "Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses.", "answer_raw": "Sí. El casc infantil està inclòs amb cada lloguer de skateboard, i les genolleres, colzeres i canelleres estan incloses."} | True | True |
| ca | 3 | {"line": 863, "question": "On puc anar amb skateboard a prop de la botiga?", "answer": "La nostra botiga és a prop del passeig marítim, el Port Olímpic i zones obertes on molts visitants comencen amb una ruta tranquil·la abans d’explorar altres espais aptes per a skate.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "On puc anar amb skateboard a prop de la botiga?", "answer": "La nostra botiga és a prop del passeig marítim, el Port Olímpic i zones obertes on molts visitants comencen amb una ruta tranquil·la abans d’explorar altres espais aptes per a skate.", "answer_raw": "La nostra botiga és a prop del passeig marítim, el Port Olímpic i zones obertes on molts visitants comencen amb una ruta tranquil·la abans d’explorar altres espais aptes per a skate."} | True | True |
| ca | 4 | {"line": 867, "question": "Teniu skateboards per a principiants?", "answer": "Sí. Podem ajudar-te a triar un skateboard estable o un cruiser board segons la teva experiència i el tipus de ruta que vulguis fer.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Teniu skateboards per a principiants?", "answer": "Sí. Podem ajudar-te a triar un skateboard estable o un cruiser board segons la teva experiència i el tipus de ruta que vulguis fer.", "answer_raw": "Sí. Podem ajudar-te a triar un skateboard estable o un cruiser board segons la teva experiència i el tipus de ruta que vulguis fer."} | True | True |
| ca | 5 | {"line": 871, "question": "Necessito carnet per llogar un skateboard?", "answer": "No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Necessito carnet per llogar un skateboard?", "answer": "No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid.", "answer_raw": "No cal carnet de conduir. El skateboard és una activitat no motoritzada, així que qualsevol persona pot llogar-ne un amb un document d’identitat vàlid."} | True | True |
| ca | 6 | {"line": 875, "question": "Puc deixar la motxilla o l’equipatge a la botiga?", "answer": "Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Puc deixar la motxilla o l’equipatge a la botiga?", "answer": "Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes.", "answer_raw": "Sí. Oferim servei gratuït de guarda d’equipatge per a jaquetes, motxilles i maletes a la nostra botiga supervisada mentre rodes."} | True | True |
| ca | 7 | {"line": 879, "question": "Puc reservar o fer preguntes per WhatsApp?", "answer": "Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puc reservar o fer preguntes per WhatsApp?", "answer": "Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida.", "answer_raw": "Sí. Pots escriure’ns per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o acordar l’hora de recollida."} | True | True |
| ca | 8 | {"line": 883, "question": "Com reservo o contacto amb vosaltres?", "answer": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar disponibilitat de taules o el millor moment per recollir el teu skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Com reservo o contacto amb vosaltres?", "answer": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar disponibilitat de taules o el millor moment per recollir el teu skateboard.", "answer_raw": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar disponibilitat de taules o el millor moment per recollir el teu skateboard."} | True | True |
| sv | 1 | {"line": 868, "question": "Behöver jag erfarenhet för att hyra skateboard?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Behöver jag erfarenhet för att hyra skateboard?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med.", "answer_raw": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut skateboards till nybörjare och vana åkare, och vårt team kan hjälpa dig att välja en bekväm bräda att börja med."} | True | True |
| sv | 2 | {"line": 872, "question": "Ingår skyddsutrustning i hyran?", "answer": "Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Ingår skyddsutrustning i hyran?", "answer": "Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår.", "answer_raw": "Ja. Barnhjälm ingår i varje skateboardhyra, och knä-, armbågs- och handledsskydd ingår."} | True | True |
| sv | 3 | {"line": 876, "question": "Var kan jag åka skateboard nära butiken?", "answer": "Vår butik ligger nära strandpromenaden, Port Olímpic och öppna ytor där många besökare börjar med en lugn tur innan de utforskar fler skatevänliga platser i närheten.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Var kan jag åka skateboard nära butiken?", "answer": "Vår butik ligger nära strandpromenaden, Port Olímpic och öppna ytor där många besökare börjar med en lugn tur innan de utforskar fler skatevänliga platser i närheten.", "answer_raw": "Vår butik ligger nära strandpromenaden, Port Olímpic och öppna ytor där många besökare börjar med en lugn tur innan de utforskar fler skatevänliga platser i närheten."} | True | True |
| sv | 4 | {"line": 880, "question": "Har ni skateboards för nybörjare?", "answer": "Ja. Vi kan hjälpa dig att välja en stabil skateboard eller cruiserbräda beroende på din erfarenhet och vilken typ av tur du vill göra.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Har ni skateboards för nybörjare?", "answer": "Ja. Vi kan hjälpa dig att välja en stabil skateboard eller cruiserbräda beroende på din erfarenhet och vilken typ av tur du vill göra.", "answer_raw": "Ja. Vi kan hjälpa dig att välja en stabil skateboard eller cruiserbräda beroende på din erfarenhet och vilken typ av tur du vill göra."} | True | True |
| sv | 5 | {"line": 884, "question": "Behöver jag körkort för att hyra skateboard?", "answer": "Nej. Inget körkort krävs för att hyra en skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Behöver jag körkort för att hyra skateboard?", "answer": "Nej. Inget körkort krävs för att hyra en skateboard.", "answer_raw": "Nej. Inget körkort krävs för att hyra en skateboard."} | True | True |
| sv | 6 | {"line": 888, "question": "Kan jag lämna väska eller bagage i butiken?", "answer": "Ja. Gratis förvaring för jackor, ryggsäckar och bagage finns i vår övervakade butik medan du åker.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kan jag lämna väska eller bagage i butiken?", "answer": "Ja. Gratis förvaring för jackor, ryggsäckar och bagage finns i vår övervakade butik medan du åker.", "answer_raw": "Ja. Gratis förvaring för jackor, ryggsäckar och bagage finns i vår övervakade butik medan du åker."} | True | True |
| sv | 7 | {"line": 893, "question": "Kan jag boka eller ställa frågor via WhatsApp?", "answer": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan jag boka eller ställa frågor via WhatsApp?", "answer": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid.", "answer_raw": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid."} | True | True |
| sv | 8 | {"line": 897, "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard.", "answer_raw": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta tillgänglighet eller bästa tid att hämta din skateboard."} | True | True |
| pl | 1 | {"line": 923, "question": "Czy potrzebuję doświadczenia, aby wynająć deskorolkę?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy deskorolki początkującym i pewniejszym osobom, a nasz zespół pomoże wybrać wygodną deskę na start.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Czy potrzebuję doświadczenia, aby wynająć deskorolkę?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy deskorolki początkującym i pewniejszym osobom, a nasz zespół pomoże wybrać wygodną deskę na start.", "answer_raw": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy deskorolki początkującym i pewniejszym osobom, a nasz zespół pomoże wybrać wygodną deskę na start."} | True | True |
| pl | 2 | {"line": 927, "question": "Czy sprzęt ochronny jest w cenie wynajmu?", "answer": "Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Czy sprzęt ochronny jest w cenie wynajmu?", "answer": "Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę.", "answer_raw": "Tak. Kask dziecięcy jest wliczony w każdy wynajem deskorolki, a ochraniacze na kolana, łokcie i nadgarstki są wliczone w cenę."} | True | True |
| pl | 3 | {"line": 931, "question": "Gdzie mogę jeździć na deskorolce blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym odkrywaniem pobliskich miejsc przyjaznych do jazdy.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Gdzie mogę jeździć na deskorolce blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym odkrywaniem pobliskich miejsc przyjaznych do jazdy.", "answer_raw": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym odkrywaniem pobliskich miejsc przyjaznych do jazdy."} | True | True |
| pl | 4 | {"line": 935, "question": "Czy macie deskorolki dla początkujących?", "answer": "Tak. Pomożemy wybrać stabilną deskorolkę lub cruisera w zależności od Twojego doświadczenia i rodzaju jazdy, którego szukasz.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Czy macie deskorolki dla początkujących?", "answer": "Tak. Pomożemy wybrać stabilną deskorolkę lub cruisera w zależności od Twojego doświadczenia i rodzaju jazdy, którego szukasz.", "answer_raw": "Tak. Pomożemy wybrać stabilną deskorolkę lub cruisera w zależności od Twojego doświadczenia i rodzaju jazdy, którego szukasz."} | True | True |
| pl | 5 | {"line": 939, "question": "Czy potrzebuję prawa jazdy, aby wynająć deskorolkę?", "answer": "Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Czy potrzebuję prawa jazdy, aby wynająć deskorolkę?", "answer": "Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy.", "answer_raw": "Nie. Do wynajmu deskorolki nie jest wymagane prawo jazdy."} | True | True |
| pl | 6 | {"line": 943, "question": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "answer": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "answer": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni.", "answer_raw": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni."} | True | True |
| pl | 7 | {"line": 948, "question": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "answer": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "answer": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru.", "answer_raw": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru."} | True | True |
| pl | 8 | {"line": 952, "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność deski albo najlepszą godzinę odbioru deskorolki.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność deski albo najlepszą godzinę odbioru deskorolki.", "answer_raw": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność deski albo najlepszą godzinę odbioru deskorolki."} | True | True |

## T. MATRIZ RATING/REVIEWS

Rating canónico 4.6, 226 reseñas, escala 1–5. Los testimonios individuales pueden tener 5 estrellas sin contradecir la media. Se verifica presencia y correspondencia; autenticidad externa no verificada.

| Idioma | Comparación completa |
| --- | --- |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Quick and easy! Light on the paperwork, and open on Sundays. Bikes, scooters, skateboards, rollerblades. Small shop has it all!\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2018-10-11"}, "line": 866, "visible_card": {"line": 866, "text": "★★★★★ “Quick and easy! Light on the paperwork, and open on Sundays. Bikes, scooters, skateboards, rollerblades. Small shop has it all!” TheDoctorIsIn Google review · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excelente servicio, además está al lado del paseo marítimo, si quieres disfrutar Barcelona en ruedas aquí encuentras bicis, patines, patinetas, scooters. Tamnbien tienen patines y bicis para niños.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 860, "visible_card": {"line": 860, "text": "★★★★★ “Excelente servicio, además está al lado del paseo marítimo, si quieres disfrutar Barcelona en ruedas aquí encuentras bicis, patines, patinetas, scooters. Tamnbien tienen patines y bicis para niños.” Claudia Montes · Reseña de Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excellent service, et en plus la boutique est à côté de la promenade maritime. Si vous voulez profiter de Barcelone sur des roues, vous y trouverez des vélos, des patins, des skateboards et des scooters. Ils ont aussi des patins et des vélos pour enfants.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 799, "visible_card": {"line": 799, "text": "★★★★★ “Excellent service, et en plus la boutique est à côté de la promenade maritime. Si vous voulez profiter de Barcelone sur des roues, vous y trouverez des vélos, des patins, des skateboards et des scooters. Ils ont aussi des patins et des vélos pour enfants.” Claudia Montes · Avis Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Claudia Montes"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Servizio eccellente, inoltre il negozio è accanto al lungomare. Se vuoi goderti Barcellona su ruote, qui trovi biciclette, pattini, skateboard e scooter. Hanno anche pattini e biciclette per bambini.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 804, "visible_card": {"line": 804, "text": "★★★★★ “Servizio eccellente, inoltre il negozio è accanto al lungomare. Se vuoi goderti Barcellona su ruote, qui trovi biciclette, pattini, skateboard e scooter. Hanno anche pattini e biciclette per bambini.” Claudia Montes · Recensione Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Schnell und unkompliziert! Wenig Papierkram und sonntags geöffnet. Fahrräder, Scooter, Skateboards, Inlineskates. Der kleine Laden hat alles!“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 806, "visible_card": {"line": 806, "text": "★★★★★ „Schnell und unkompliziert! Wenig Papierkram und sonntags geöffnet. Fahrräder, Scooter, Skateboards, Inlineskates. Der kleine Laden hat alles!“ TheDoctorIsIn Google-Bewertung · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Snel en eenvoudig! Weinig papierwerk en open op zondag. Fietsen, scooters, skateboards, inline skates. De kleine winkel heeft alles!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 815, "visible_card": {"line": 815, "text": "★★★★★ “Snel en eenvoudig! Weinig papierwerk en open op zondag. Fietsen, scooters, skateboards, inline skates. De kleine winkel heeft alles!” TheDoctorIsIn Google-review · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Rápido e fácil! Pouca burocracia e aberto aos domingos. Bicicletas, scooters, skates, patins em linha. A pequena loja tem tudo!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 820, "visible_card": {"line": 820, "text": "★★★★★ “Rápido e fácil! Pouca burocracia e aberto aos domingos. Bicicletas, scooters, skates, patins em linha. A pequena loja tem tudo!” TheDoctorIsIn Avaliação Google · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ràpid i fàcil! Poca paperassa i obert els diumenges. Bicicletes, scooters, monopatins i patins en línia. La petita botiga ho té tot!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 804, "visible_card": {"line": 804, "text": "★★★★★ “Ràpid i fàcil! Poca paperassa i obert els diumenges. Bicicletes, scooters, monopatins i patins en línia. La petita botiga ho té tot!” TheDoctorIsIn Ressenya de Google · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Snabbt och enkelt! Lite pappersarbete och öppet på söndagar. Cyklar, scootrar, skateboards och inlines. Den lilla butiken har allt!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 817, "visible_card": {"line": 817, "text": "★★★★★ “Snabbt och enkelt! Lite pappersarbete och öppet på söndagar. Cyklar, scootrar, skateboards och inlines. Den lilla butiken har allt!” TheDoctorIsIn Google-recension · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/skateboard/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "TheDoctorIsIn"}, "datePublished": "2018-10-11", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Szybko i łatwo! Mało formalności i otwarte w niedziele. Rowery, skutery, deskorolki i rolki. Ten mały sklep ma wszystko!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 872, "visible_card": {"line": 872, "text": "★★★★★ “Szybko i łatwo! Mało formalności i otwarte w niedziele. Rowery, skutery, deskorolki i rolki. Ten mały sklep ma wszystko!” TheDoctorIsIn Opinia Google · 2018-10-11", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |

## U. MATRIZ ESTRUCTURA HTML/ARTICLE

| Idioma | Conteos fuente/token/DOM | Errores token | Pila sin cerrar | IDs duplicados |
| --- | --- | --- | --- | --- |
| en | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| es | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| fr | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| it | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| de | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| nl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pt | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| ca | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| sv | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 15, "text_close": 15, "token_open": 15, "token_close": 15, "parsed": 15}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |

## V. MATRIZ ENLACES INTERNOS/SELECTOR IDIOMAS

| Idioma | Selectores | Referencias ID | Controles / formularios |
| --- | --- | --- | --- |
| en | [{"line": 643, "id": null, "links": [{"line": 644, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 644, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 662, "id": null, "links": [{"line": 663, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 663, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 691, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title", "exists": true}, {"line": 858, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 910, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 948, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 638, "text": "Language", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 658, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 665, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Toggle menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 918, "text": "Do I need experience to rent a skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 922, "text": "Is protective gear included with the rental?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 926, "text": "Where can I ride a skateboard near the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 930, "text": "Do you have skateboards for beginners?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 934, "text": "Do I need a licence to rent a skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 938, "text": "Can I store my bag or luggage at the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 942, "text": "How do I book or contact you?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| es | [{"line": 637, "id": null, "links": [{"line": 638, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 638, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 656, "id": null, "links": [{"line": 657, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 657, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 685, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-es", "exists": true}, {"line": 897, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 935, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 632, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 652, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 659, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir o cerrar menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 905, "text": "¿Necesito experiencia para alquilar un skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 909, "text": "¿Está incluido el equipo de protección?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 913, "text": "¿Dónde puedo usar un skateboard cerca de la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 917, "text": "¿Tenéis skateboards para principiantes?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 921, "text": "¿Necesito carnet para alquilar un skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 925, "text": "¿Puedo dejar mi mochila o equipaje en la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 929, "text": "¿Cómo reservo o contacto con vosotros?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| fr | [{"line": 577, "id": null, "links": [{"line": 578, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 578, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 596, "id": null, "links": [{"line": 597, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 624, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-fr", "exists": true}, {"line": 836, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 878, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 572, "text": "Langue", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 592, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 599, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Ouvrir ou fermer le menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 844, "text": "Faut-il de l’expérience pour louer un skateboard ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 848, "text": "Les protections sont-elles incluses ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 852, "text": "Où puis-je faire du skateboard près de la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 856, "text": "Avez-vous des skateboards pour débutants ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 860, "text": "Faut-il un permis pour louer un skateboard ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 864, "text": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 868, "text": "Puis-je réserver ou poser des questions par WhatsApp ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 872, "text": "Comment réserver ou vous contacter ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| it | [{"line": 579, "id": null, "links": [{"line": 580, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 598, "id": null, "links": [{"line": 599, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 629, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-it", "exists": true}, {"line": 841, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 883, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 574, "text": "Lingua", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 594, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 601, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Apri o chiudi menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 849, "text": "Serve esperienza per noleggiare uno skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 853, "text": "Le protezioni sono incluse nel noleggio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 857, "text": "Dove posso andare in skateboard vicino al negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 861, "text": "Avete skateboard per principianti?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 865, "text": "Serve una patente per noleggiare uno skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 869, "text": "Posso lasciare borsa o bagagli in negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 873, "text": "Posso prenotare o fare domande su WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 877, "text": "Come prenoto o vi contatto?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| de | [{"line": 584, "id": null, "links": [{"line": 585, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 585, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 603, "id": null, "links": [{"line": 604, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 604, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 631, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-de", "exists": true}, {"line": 799, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 850, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 909, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 579, "text": "Sprache", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 599, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 606, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menü öffnen oder schließen", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 859, "text": "Brauche ich Erfahrung, um ein Skateboard zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 865, "text": "Ist Schutzausrüstung in der Miete enthalten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 871, "text": "Wo kann ich in der Nähe des Shops Skateboard fahren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 877, "text": "Habt ihr Skateboards für Anfänger?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 883, "text": "Brauche ich einen Führerschein, um ein Skateboard zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 889, "text": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 896, "text": "Kann ich per WhatsApp buchen oder Fragen stellen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 902, "text": "Wie buche ich oder kontaktiere euch?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| nl | [{"line": 593, "id": null, "links": [{"line": 594, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 594, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 612, "id": null, "links": [{"line": 613, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 613, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 640, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-nl", "exists": true}, {"line": 808, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 859, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 918, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 588, "text": "Taal", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 608, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 615, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menu openen of sluiten", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 868, "text": "Heb ik ervaring nodig om een skateboard te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 874, "text": "Is bescherming inbegrepen bij de huur?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 880, "text": "Waar kan ik skateboarden in de buurt van de shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 886, "text": "Hebben jullie skateboards voor beginners?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 892, "text": "Heb ik een rijbewijs nodig om een skateboard te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 898, "text": "Kan ik mijn tas of bagage in de shop achterlaten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 905, "text": "Kan ik reserveren of vragen stellen via WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 911, "text": "Hoe reserveer ik of neem ik contact met jullie op?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pt | [{"line": 596, "id": null, "links": [{"line": 597, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 597, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 615, "id": null, "links": [{"line": 616, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 616, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 646, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-pt", "exists": true}, {"line": 813, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 864, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 906, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 591, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 611, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 618, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir ou fechar menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 872, "text": "Preciso de experiência para alugar um skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 876, "text": "O equipamento de proteção está incluído?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 880, "text": "Onde posso andar de skateboard perto da loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 884, "text": "Têm skateboards para principiantes?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 888, "text": "Preciso de carta para alugar um skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 892, "text": "Posso deixar a minha mochila ou bagagem na loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 896, "text": "Posso reservar ou fazer perguntas por WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 900, "text": "Como faço a reserva ou contacto convosco?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| ca | [{"line": 579, "id": null, "links": [{"line": 580, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 580, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 598, "id": null, "links": [{"line": 599, "text": "en English", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 599, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 629, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-cat", "exists": true}, {"line": 797, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 848, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 890, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 574, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 594, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 601, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Obrir o tancar menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 856, "text": "Necessito experiència per llogar un skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 860, "text": "L’equip de protecció està inclòs?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 864, "text": "On puc anar amb skateboard a prop de la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 868, "text": "Teniu skateboards per a principiants?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 872, "text": "Necessito carnet per llogar un skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 876, "text": "Puc deixar la motxilla o l’equipatge a la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 880, "text": "Puc reservar o fer preguntes per WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 884, "text": "Com reservo o contacto amb vosaltres?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| sv | [{"line": 594, "id": null, "links": [{"line": 595, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 595, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 613, "id": null, "links": [{"line": 614, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 614, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 642, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title-sv", "exists": true}, {"line": 810, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 861, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 904, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 589, "text": "Språk", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 609, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 616, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Öppna eller stäng meny", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 869, "text": "Behöver jag erfarenhet för att hyra skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 873, "text": "Ingår skyddsutrustning i hyran?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 877, "text": "Var kan jag åka skateboard nära butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 881, "text": "Har ni skateboards för nybörjare?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 885, "text": "Behöver jag körkort för att hyra skateboard?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 889, "text": "Kan jag lämna väska eller bagage i butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 894, "text": "Kan jag boka eller ställa frågor via WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 898, "text": "Hur bokar jag eller kontaktar er?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pl | [{"line": 651, "id": null, "links": [{"line": 652, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 652, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}, {"line": 670, "id": null, "links": [{"line": 671, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/skateboard/", "role": "menuitem"}}, {"line": 671, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/skateboard/", "role": "menuitem"}}], "selected": []}] | [{"line": 699, "attribute": "aria-labelledby", "ref": "skateboard-business-facts-title", "exists": true}, {"line": 865, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 916, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 959, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 646, "text": "Język", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 666, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 673, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Przełącz menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 924, "text": "Czy potrzebuję doświadczenia, aby wynająć deskorolkę?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 928, "text": "Czy sprzęt ochronny jest w cenie wynajmu?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 932, "text": "Gdzie mogę jeździć na deskorolce blisko wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 936, "text": "Czy macie deskorolki dla początkujących?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 940, "text": "Czy potrzebuję prawa jazdy, aby wynająć deskorolkę?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 944, "text": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 949, "text": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 953, "text": "Jak mogę zarezerwować lub skontaktować się z wami?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |

Los 12.046 enlaces internos de los 200 HTML apuntan al corpus incluido y todas las anclas locales se resuelven. No se han solicitado respuestas HTTP. La marca estática de idioma activo es una mejora.

## W. MATRIZ GLOBAL POR IDIOMA

| Idioma | Primera pasada | Segunda pasada independiente | Comprobaciones de página |
| --- | --- | --- | --- |
| en | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "en", "expected": "en", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/skateboard/", "pass": true}] |
| es | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/es/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/es/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "es", "expected": "es", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/skateboard/", "pass": true}] |
| fr | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/fr/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/fr/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "fr", "expected": "fr", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/skateboard/", "pass": true}] |
| it | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/it/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/it/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "it", "expected": "it", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/skateboard/", "pass": true}] |
| de | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/de/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/de/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "de", "expected": "de", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/skateboard/", "pass": true}] |
| nl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/nl/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/nl/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "nl", "expected": "nl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/skateboard/", "pass": true}] |
| pt | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pt/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/pt/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pt-PT", "expected": "pt-PT", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/skateboard/", "pass": true}] |
| ca | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/cat/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/cat/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "ca", "expected": "ca", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/skateboard/", "pass": true}] |
| sv | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/sv/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/sv/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "sv", "expected": "sv", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/skateboard/", "pass": true}] |
| pl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pl/skateboard/", "expected_page": "https://rentalscooterbarcelona.com/pl/skateboard/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pl", "expected": "pl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/skateboard/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/skateboard/", "pass": true}] |

## LISTA FINAL DE CAMBIOS PROPUESTOS

| Punto | Idioma | Prioridad | Elemento | Propuesta |
| --- | --- | --- | --- | --- |
| U03 | ca | 2 | https://rentalscooterbarcelona.com/cat/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | de | 2 | https://rentalscooterbarcelona.com/de/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | en | 2 | https://rentalscooterbarcelona.com/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | es | 2 | https://rentalscooterbarcelona.com/es/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | fr | 2 | https://rentalscooterbarcelona.com/fr/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | it | 2 | https://rentalscooterbarcelona.com/it/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | nl | 2 | https://rentalscooterbarcelona.com/nl/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pl | 2 | https://rentalscooterbarcelona.com/pl/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pt | 2 | https://rentalscooterbarcelona.com/pt/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | sv | 2 | https://rentalscooterbarcelona.com/sv/skateboard/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U05 | nl | 3 | Párrafo de enlace a la guía | Een kinderhelm is inbegrepen bij elke skateboardhuur en beschermers zijn inbegrepen. Ons lokale team kan je helpen een stabiel board te kiezen, de basis uitleggen en geschikte routes aanbevelen. Voor lokale route-ideeën en praktische tips kun je onze &lt;a href="https://rentalscooterbarcelona.com/nl/blog/skateboard/"&gt;gids voor skateboard huren in Barcelona&lt;/a&gt; lezen.&lt;/p&gt; |

## CONTROL FINAL

Integridad SHA-256 comprobada contra cada entrada ZIP. Las evidencias contienen valores y líneas por archivo. No se han modificado HTML ni aplicado correcciones. Imágenes y tamaños quedan pendientes; no se ha certificado renderizado, entrega de formularios, indexación ni disponibilidad remota.
