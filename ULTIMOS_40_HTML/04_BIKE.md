# Auditoría HTML — 04_BIKE

2026-09-09. Diez idiomas. Fuente: ZIP adjunto y CANONICAL.md. HTML original sin modificar.

## A. INVENTARIO DE ARCHIVOS

| Idioma | Archivo original | Bytes | Líneas | SHA-256 |
| --- | --- | --- | --- | --- |
| en | BIKE/bike/index.html | 75068 | 1164 | 1f7904d99b1a26d55ac3cb48dc25841992764a0664e0f232ea98557b414233cc |
| es | BIKE/es/bike/index.html | 78477 | 1137 | 163d5397ce02a29c40a4da46d2e6fb9b9ea7a65764e84d4b9e923798a28103bc |
| fr | BIKE/fr/bike/index.html | 77874 | 1062 | 0f3ccf1e42bae63ca2b7e7b5750b090e3f4a51c211be4fca9b13de14dc69d95c |
| it | BIKE/it/bike/index.html | 77648 | 1072 | 150f22717c9f1aeb8525c455cbec4afde524427d3ac67c2c80929b5714793476 |
| de | BIKE/de/bike/index.html | 77101 | 1108 | c0e923be7e4048adb0ddf4db0a8a465f1601fbf5f707b635ada095454b5792ea |
| nl | BIKE/nl/bike/index.html | 76051 | 1116 | 7dfe74d99fe7ef5121db426e5944a7914c4fc5b73443e9d0d9ac3adda300fe41 |
| pt | BIKE/pt/bike/index.html | 77511 | 1108 | 5d3d2972745dab873084c2b46521d7e23bfaf5193aa4f76a074cdbdb7eebd7df |
| ca | BIKE/cat/bike/index.html | 76605 | 1093 | 7e29239031cec16bb0723feafc823767ffecf202f1bb6d4bdac0e9780e9e11ab |
| sv | BIKE/sv/bike/index.html | 75637 | 1102 | 7dbd628d2cb64e47e33e1c9d85804f670504e9b028ef535b3edfe6e787d26497 |
| pl | BIKE/pl/bike/index.html | 77253 | 1163 | 1d06da992081276779472944d9eb4a41bb9442caf730642da19f0bdfdcc16eaf |

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
| nl | U03 | 22/23 |
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

**Elemento:** https://rentalscooterbarcelona.com/cat/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 136 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 481 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### de

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 137 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 489 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### en

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 170 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 556 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### es

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/es/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 167 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 550 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### fr

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/fr/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 137 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 481 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### it

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/it/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 136 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 481 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### nl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 497 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pl/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 170 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 556 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pt

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pt/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 497 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### sv

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/sv/bike/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 150 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 497 del HTML original:

```html
"dateModified": "2026-08-24"
```

## G. ERRORES BAJOS

Ninguno demostrado.

## H. INCOHERENCIAS QUE REQUIEREN FUENTE CANÓNICA

U03: fecha de modificación real por idioma. Los dos valores están documentados; CANONICAL no permite elegir uno.

Los datos de identidad, dirección, horario, mapas y equipamiento ya están definidos: no requieren nueva confirmación. Las tarifas y tallas documentadas no equivalen a una certificación externa de vigencia.

## I. MEJORAS RECOMENDADAS

# Mejoras opcionales — 04_BIKE

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
<title>Bike Rental Barcelona | City Bikes Near Port Olímpic | RSB</title>
<meta content="Rent bikes in Barcelona near Port Olímpic and Barceloneta. City bikes for adults and kids, helmet and lock included, child seat option and local route tips." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Bike Rental Barcelona | City Bikes Near Port Olímpic | RSB" property="og:title"/>
<meta content="Rent bikes in Barcelona near Port Olímpic and Barceloneta. City bikes for adults and kids, helmet and lock included, child seat option and local route tips." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Bike rental in Barcelona near Vila Olímpica del Poblenou and Barceloneta Beach" property="og:image:alt"/>
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
<meta content="Bike Rental Barcelona | City Bikes Near Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Rent bikes in Barcelona near Port Olímpic and Barceloneta. City bikes for adults and kids, helmet and lock included, child seat option and local route tips." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Bike rental in Barcelona near Vila Olímpica del Poblenou and Barceloneta Beach" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "@id": "https://rentalscooterbarcelona.com/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/bike/",
      "name": "Bike Rental Barcelona | City Bikes Near Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "en",
      "description": "Rent bikes in Barcelona near Port Olímpic and Barceloneta. City bikes for adults and kids, helmet and lock included, child seat option and local route tips.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/bike/#faq"
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
      "@id": "https://rentalscooterbarcelona.com/bike/#breadcrumb",
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
          "name": "Bike rental",
          "item": "https://rentalscooterbarcelona.com/bike/"
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
      "@id": "https://rentalscooterbarcelona.com/bike/#service",
      "name": "Bike rental in Barcelona",
      "serviceType": "Bike rental",
      "description": "Our bike rental service in Barcelona near Port Olímpic and Barceloneta Beach offers comfortable city bikes for adults and kids. A children's helmet and lock are included with every rental, and an optional child seat is available on selected bikes. Free storage and local route recommendations provided.",
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
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Bike rental price range",
          "priceCurrency": "EUR",
          "lowPrice": "4",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/bike/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 hour",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "1 hour bike rental near Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 hours",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "4 hour bike rental near Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Full day",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "Full day bike rental in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 hours",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "24 hour bike rental in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 days",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "2 day bike rental in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Extra day",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/bike/",
          "description": "Extra day bike rental in Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ],
      "url": "https://rentalscooterbarcelona.com/bike/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Do I need experience to rent a bike?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started."
          }
        },
        {
          "@type": "Question",
          "name": "Is a helmet or lock included with the rental?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes."
          }
        },
        {
          "@type": "Question",
          "name": "Where can I ride a bike near the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby."
          }
        },
        {
          "@type": "Question",
          "name": "Do you have bikes for beginners or kids?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need a licence to rent a bike?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID."
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
          "name": "Can I book or ask questions by WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. You can message us on WhatsApp before coming to confirm availability, ask questions or arrange your pick-up time."
          }
        },
        {
          "@type": "Question",
          "name": "How do I book or contact you?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "You can book via WhatsApp, email or phone. Contact us if you want to confirm bike availability or the best time to collect your bike."
          }
        }
      ],
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"My boyfriend and I rented a pair of skates and bike to go up the board walk and it was so fun! The owners were so sweet and helpful and the price was great! Very happy with this place and will come back.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2026-04-04"
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Gvidas Gečas"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Super. Affordable and good location, got a fixed bike that was patient enough to drive all over the city daily, even shoes have matched!😁\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2023-02-05"
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Fabio Mendes"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Went here to rent bikes to stroll the beach path. Oscar was very friendly and to the point. Fast easy process for renting, no long forms or speeches. Good, fair price and you're on your way! Thank you, Oscar.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2020-02-20"
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
<title>Alquiler de bicicletas en Barcelona | Bicis urbanas | RSB</title>
<meta name="description" content="Alquiler de bicicletas en Barcelona, en la Vila Olímpica. Bicis urbanas para adultos y niños, candado incluido y rutas por Port Olímpic y Barceloneta.">
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/es/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta property="og:title" content="Alquiler de bicicletas en Barcelona | Bicis urbanas | RSB">
<meta property="og:description" content="Alquiler de bicicletas en Barcelona, en la Vila Olímpica. Bicis urbanas para adultos y niños, candado incluido y rutas por Port Olímpic y Barceloneta.">
<meta content="https://rentalscooterbarcelona.com/es/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Alquiler de bicicletas en Barcelona cerca de Vila Olímpica del Poblenou y la playa de la Barceloneta" property="og:image:alt"/>
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
<meta name="twitter:title" content="Alquiler de bicicletas en Barcelona | Bicis urbanas | RSB">
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta name="twitter:description" content="Alquiler de bicicletas en Barcelona, en la Vila Olímpica. Bicis urbanas para adultos y niños, candado incluido y rutas por Port Olímpic y Barceloneta.">
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Alquiler de bicicletas en Barcelona cerca de Vila Olímpica del Poblenou y la playa de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta. Con el alquiler de bicicletas se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.",
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
      "@id": "https://rentalscooterbarcelona.com/es/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/es/bike/",
      "name": "Alquiler de bicicletas en Barcelona | Bicis urbanas | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "es",
      "description": "Alquiler de bicicletas en Barcelona, en la Vila Olímpica. Bicis urbanas para adultos y niños, candado incluido y rutas por Port Olímpic y Barceloneta.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/es/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/bike/#faq"
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
      "@id": "https://rentalscooterbarcelona.com/es/bike/#breadcrumb",
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
          "name": "Alquiler de bicicletas",
          "item": "https://rentalscooterbarcelona.com/es/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta. Con el alquiler de bicicletas se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Tarjeta de crédito, tarjeta de débito, PayPal",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#service",
      "url": "https://rentalscooterbarcelona.com/es/bike/",
      "name": "Alquiler de bicicletas en Barcelona",
      "serviceType": "Alquiler de bicicletas",
      "description": "Nuestro servicio de alquiler de bicicletas en Barcelona, cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta, ofrece cómodas bicicletas urbanas para adultos y niños. Con cada alquiler se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.",
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
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Rango de precios del alquiler de bicicletas",
          "priceCurrency": "EUR",
          "lowPrice": "4",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/es/bike/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 hora",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "1 hora de alquiler de bicicleta cerca de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 horas",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "4 horas de alquiler de bicicleta cerca de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Día completo",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "Alquiler de bicicleta de día completo en Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 horas",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "Alquiler de bicicleta de 24 horas en Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 días",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "Alquiler de bicicleta de 2 días en Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Día extra",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/es/bike/",
          "description": "Día extra de alquiler de bicicleta en Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Necesito experiencia para alquilar una bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no necesitas experiencia previa. Alquilamos bicicletas a principiantes y a personas que ya montan con confianza, y nuestro equipo puede ayudarte a elegir una bicicleta cómoda para empezar."
          }
        },
        {
          "@type": "Question",
          "name": "¿Se incluye casco o candado con el alquiler?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional."
          }
        },
        {
          "@type": "Question",
          "name": "¿Dónde puedo montar en bicicleta cerca de la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nuestra tienda está cerca del paseo marítimo, Port Olímpic, Torre MAPFRE y Casino Barcelona, en una zona desde la que muchos visitantes empiezan una ruta tranquila antes de explorar parques y carriles bici cercanos."
          }
        },
        {
          "@type": "Question",
          "name": "¿Tenéis bicicletas para principiantes o para niños?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños."
          }
        },
        {
          "@type": "Question",
          "name": "¿Necesito licencia para alquilar una bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido."
          }
        },
        {
          "@type": "Question",
          "name": "¿Puedo guardar mi bolsa o equipaje en la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Disponemos de consigna gratuita para chaquetas, mochilas y equipaje en nuestra tienda supervisada mientras montas."
          }
        },
        {
          "@type": "Question",
          "name": "¿Puedo reservar o preguntar por WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cómo reservo o cómo contacto con vosotros?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya."
          }
        }
      ],
      "inLanguage": "es"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/es/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/es/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/es/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/es/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/es/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/es/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/es/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Alfonso Arellano"
      },
      "datePublished": "2026-03-13",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Alquilé una bici aquí y la verdad es que quedé muy contento. Los precios están muy bien comparados con otros sitios y las bicicletas están en buen estado. Además, la dueña es súper maja y el trato fue muy amable desde el primer momento, te explica todo con calma y te hace sentir a gusto. Sin duda es un sitio muy recomendable si necesitas alquilar una bici sin complicaciones y a buen precio. Volvería a alquilar aquí sin dudarlo.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "ectnes montano"
      },
      "datePublished": "2025-04-02",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Me gustó mucho el trato, ya que la chica que nos atendió tenía un total conocimiento de Barcelona, nos dio muchos tips de que conocer y que lugares visitar Las bicicletas y patines , están en un buen estado y creo que el mantenimiento constante, hacen que está tienda tenga un material en excelentes condiciones Mil y mil gracias a Natalia por su servicio excelente Nos volveremos a ver muy pronto Super recomendable\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Lourdes Arrastia"
      },
      "datePublished": "2021-07-14",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Me encanto la atención, muy amables. Pero sobre todo rentar una bici a un precio tan económico. ❤️\"",
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
<title>Location de vélos à Barcelone | RSB</title>
<meta content="Louez un vélo urbain à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, antivol, consigne gratuite et conseils d’itinéraires inclus." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/fr/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Location de vélos à Barcelone | Vélos urbains près de Port Olímpic | RSB" property="og:title"/>
<meta content="Louez un vélo urbain à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, antivol, consigne gratuite et conseils d’itinéraires inclus." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/fr/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Location de vélos à Barcelone près de Vila Olímpica del Poblenou et de la plage de la Barceloneta" property="og:image:alt"/>
<meta content="fr_FR" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Location de vélos à Barcelone | Vélos urbains près de Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Louez un vélo urbain à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, antivol, consigne gratuite et conseils d’itinéraires inclus." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Location de vélos à Barcelone près de Vila Olímpica del Poblenou et de la plage de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, avec location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta. Le casque pour enfant et l’antivol sont inclus avec la location de vélos, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.",
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
          "contactType": "service client",
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
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/fr/bike/",
      "name": "Location de vélos à Barcelone | Vélos urbains près de Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "fr",
      "description": "Louez un vélo urbain à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, antivol, consigne gratuite et conseils d’itinéraires inclus.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/fr/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#breadcrumb",
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
          "name": "Location de vélos",
          "item": "https://rentalscooterbarcelona.com/fr/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, avec location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta. Le casque pour enfant et l’antivol sont inclus avec la location de vélos, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Carte de crédit, carte de débit, PayPal",
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
          "contactType": "service client",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#service",
      "name": "Location de vélos à Barcelone",
      "serviceType": "Location de vélos",
      "description": "Notre service de location de vélos à Barcelone, près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta, propose des vélos urbains confortables pour adultes et enfants. Le casque pour enfant et l’antivol sont inclus avec chaque location, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 heure",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "1 heure de location de vélo près de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 heures",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "4 heures de location de vélo près de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Journée complète",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "Location de vélo à la journée à Barcelone",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 heures",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "Location de vélo 24 heures à Barcelone",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 jours",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "Location de vélo 2 jours à Barcelone",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Jour supplémentaire",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/fr/bike/",
          "description": "Jour supplémentaire de location de vélo à Barcelone",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Ai-je besoin d’expérience pour louer un vélo ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer."
          }
        },
        {
          "@type": "Question",
          "name": "Le casque ou l’antivol sont-ils inclus avec la location ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos."
          }
        },
        {
          "@type": "Question",
          "name": "Où puis-je rouler à vélo près de la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Notre boutique se trouve près de la promenade du front de mer, de Port Olímpic, de Torre MAPFRE et de Casino Barcelona, dans un secteur où de nombreux visiteurs commencent une balade tranquille avant d’explorer les parcs et pistes cyclables à proximité."
          }
        },
        {
          "@type": "Question",
          "name": "Avez-vous des vélos pour débutants ou pour enfants ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants."
          }
        },
        {
          "@type": "Question",
          "name": "Ai-je besoin d’un permis pour louer un vélo ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un."
          }
        },
        {
          "@type": "Question",
          "name": "Puis-je laisser mon sac ou mes bagages à la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Nous disposons d’une consigne gratuite pour les vestes, sacs à dos et bagages dans notre boutique surveillée pendant votre sortie."
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
            "text": "Vous pouvez réserver via WhatsApp, e-mail ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des vélos ou le meilleur moment pour venir chercher le vôtre."
          }
        }
      ],
      "inLanguage": "fr"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/fr/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/fr/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/fr/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/fr/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/fr/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Alfonso Arellano"
      },
      "datePublished": "2026-03-13",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"J’ai loué un vélo ici et j’en ai été vraiment très satisfait. Les prix sont très bons par rapport à d’autres endroits et les vélos sont en bon état. De plus, la propriétaire est très sympathique et l’accueil a été chaleureux dès le premier instant ; elle explique tout calmement et vous met à l’aise. C’est sans aucun doute un endroit très recommandable si vous avez besoin de louer un vélo facilement et à bon prix. J’y louerais de nouveau sans hésiter.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "ectnes montano"
      },
      "datePublished": "2025-04-02",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"J’ai beaucoup apprécié l’accueil, car la personne qui nous a aidés connaissait parfaitement Barcelone et nous a donné de nombreux conseils sur les lieux à découvrir et à visiter. Les vélos et les patins sont en bon état et je pense que l’entretien constant permet à cette boutique de proposer un matériel en excellent état. Mille mercis à Natalia pour son excellent service. Nous nous reverrons très bientôt. Je recommande vivement.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Lourdes Arrastia"
      },
      "datePublished": "2021-07-14",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"J’ai adoré l’accueil, ils sont très aimables. Mais surtout, louer un vélo à un prix aussi économique. ❤️\"",
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
<title>Noleggio biciclette a Barcellona | RSB</title>
<meta content="Noleggio biciclette a Barcellona vicino a Port Olímpic e Barceloneta. City bike per adulti e bambini, casco bambino e lucchetto inclusi." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/it/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Noleggio biciclette a Barcellona | Biciclette urbane vicino a Port Olímpic | RSB" property="og:title"/>
<meta content="Noleggia biciclette a Barcellona vicino a Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica offre comode biciclette urbane per adulti e bambini, casco bambino e lucchetto inclusi, seggiolino opzionale, deposito bagagli gratuito e consigli sui percorsi locali." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/it/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Noleggio biciclette a Barcellona vicino a Vila Olímpica del Poblenou e alla spiaggia della Barceloneta" property="og:image:alt"/>
<meta content="it_IT" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Noleggio biciclette a Barcellona | Biciclette urbane vicino a Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Noleggia biciclette a Barcellona vicino a Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica offre comode biciclette urbane per adulti e bambini, casco bambino e lucchetto inclusi, seggiolino opzionale, deposito bagagli gratuito e consigli sui percorsi locali." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Noleggio biciclette a Barcellona vicino a Vila Olímpica del Poblenou e alla spiaggia della Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
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
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta. Con il noleggio biciclette sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.",
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
          "contactType": "servizio clienti",
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
      "@id": "https://rentalscooterbarcelona.com/it/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/it/bike/",
      "name": "Noleggio biciclette a Barcellona | Biciclette urbane vicino a Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "it",
      "description": "Noleggia biciclette a Barcellona vicino a Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica offre comode biciclette urbane per adulti e bambini, casco bambino e lucchetto inclusi, seggiolino opzionale, deposito bagagli gratuito e consigli sui percorsi locali.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/it/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#breadcrumb",
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
          "name": "Noleggio biciclette",
          "item": "https://rentalscooterbarcelona.com/it/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta. Con il noleggio biciclette sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Carta di credito, carta di debito, PayPal",
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
          "contactType": "servizio clienti",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#service",
      "name": "Noleggio biciclette a Barcellona",
      "serviceType": "Noleggio biciclette",
      "description": "Il nostro servizio di noleggio biciclette a Barcellona, vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta, offre comode city bike per adulti e bambini. Con ogni noleggio sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 ora",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "1 ora di noleggio bici vicino a Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 ore",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "4 ore di noleggio bici vicino a Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Giornata intera",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "Noleggio bici per una giornata intera a Barcellona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 ore",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "Noleggio bici 24 ore a Barcellona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 giorni",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "Noleggio bici per 2 giorni a Barcellona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Giorno extra",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/it/bike/",
          "description": "Giorno extra di noleggio bici a Barcellona",
          "availability": "https://schema.org/InStock"
        }
      ],
      "url": "https://rentalscooterbarcelona.com/it/bike/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Ho bisogno di esperienza per noleggiare una bicicletta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, non è necessaria esperienza precedente. Noleggiamo biciclette sia a principianti sia a chi pedala già con sicurezza, e il nostro team può aiutarti a scegliere una bici comoda per iniziare."
          }
        },
        {
          "@type": "Question",
          "name": "Il casco o il lucchetto sono inclusi nel noleggio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale."
          }
        },
        {
          "@type": "Question",
          "name": "Dove posso andare in bici vicino al negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Il nostro negozio si trova vicino al lungomare, a Port Olímpic, Torre MAPFRE e Casino Barcelona, in una zona da cui molti visitatori iniziano un percorso tranquillo prima di esplorare parchi e piste ciclabili vicine."
          }
        },
        {
          "@type": "Question",
          "name": "Avete biciclette per principianti o per bambini?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Possiamo aiutarti a scegliere una bicicletta adatta alla tua altezza e al tuo livello, comprese biciclette adatte ai bambini."
          }
        },
        {
          "@type": "Question",
          "name": "Ho bisogno della patente per noleggiare una bicicletta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso lasciare la mia borsa o i bagagli in negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali."
          }
        },
        {
          "@type": "Question",
          "name": "Posso prenotare o fare domande via WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare la disponibilità, fare domande o organizzare l’orario di ritiro."
          }
        },
        {
          "@type": "Question",
          "name": "Come posso prenotare o contattarvi?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle biciclette o il momento migliore per ritirare la tua."
          }
        }
      ],
      "inLanguage": "it"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/it/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/it/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/it/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/it/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/it/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/it/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/it/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Alfonso Arellano"
      },
      "datePublished": "2026-03-13",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Ho noleggiato una bicicletta qui e ne sono rimasto davvero molto soddisfatto. I prezzi sono molto buoni rispetto ad altri posti e le biciclette sono in buono stato. Inoltre, la proprietaria è molto simpatica e il trattamento è stato gentile fin dal primo momento; ti spiega tutto con calma e ti fa sentire a tuo agio. È senza dubbio un posto molto consigliato se hai bisogno di noleggiare una bicicletta senza complicazioni e a buon prezzo. Noleggerei di nuovo qui senza esitare.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "ectnes montano"
      },
      "datePublished": "2025-04-02",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Mi è piaciuto molto il servizio, perché la ragazza che ci ha assistito conosceva perfettamente Barcellona e ci ha dato molti consigli su cosa vedere e quali luoghi visitare. Le biciclette e i pattini sono in buono stato e credo che la manutenzione costante permetta a questo negozio di avere materiale in condizioni eccellenti. Mille grazie a Natalia per il suo servizio eccellente. Ci rivedremo molto presto. Super consigliato.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Lourdes Arrastia"
      },
      "datePublished": "2021-07-14",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Mi è piaciuta molto l’attenzione, sono stati molto gentili. Ma soprattutto poter noleggiare una bicicletta a un prezzo così conveniente. ❤️\"",
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
<title>Fahrradverleih in Barcelona | Citybikes nahe Port Olímpic | RSB</title>
<meta content="Fahrrad mieten in Barcelona nahe Port Olímpic und Barceloneta. Citybikes für Erwachsene und Kinder, Schloss und Kinderhelm inklusive." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/de/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/><meta content="de_DE" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Fahrradverleih in Barcelona | Citybikes nahe Port Olímpic | RSB" property="og:title"/>
<meta content="Miete Fahrräder in Barcelona nahe Port Olímpic und dem Strand der Barceloneta. Unser lokaler Shop in Vila Olímpica bietet bequeme Citybikes für Erwachsene und Kinder, Kinderhelm und Schloss inklusive, optionalen Kindersitz, kostenlose Gepäckaufbewahrung, lokale Routentipps und flexible Zeiten für Abholung oder Rückgabe." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/de/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Fahrradverleih in Barcelona nahe Vila Olímpica del Poblenou und dem Strand der Barceloneta" property="og:image:alt"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Fahrradverleih in Barcelona | Citybikes nahe Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Miete Fahrräder in Barcelona nahe Port Olímpic und dem Strand der Barceloneta. Unser lokaler Shop in Vila Olímpica bietet bequeme Citybikes für Erwachsene und Kinder, Kinderhelm und Schloss inklusive, optionalen Kindersitz, kostenlose Gepäckaufbewahrung, lokale Routentipps und flexible Zeiten für Abholung oder Rückgabe." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Fahrradverleih in Barcelona nahe Vila Olímpica del Poblenou und dem Strand der Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
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
      "description": "Lokaler Verleihshop in Vila Olímpica del Poblenou, Barcelona, mit Scooter-, Inlineskates-, Fahrrad-, Rollschuh-, Skateboard- und Longboard-Verleih nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta. Beim Fahrradverleih sind Kinderhelm und Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.",
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
      "@id": "https://rentalscooterbarcelona.com/de/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/de/bike/",
      "name": "Fahrradverleih in Barcelona | Citybikes nahe Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "de",
      "description": "Miete Fahrräder in Barcelona nahe Port Olímpic und dem Strand der Barceloneta. Unser lokaler Shop in Vila Olímpica bietet bequeme Citybikes für Erwachsene und Kinder, Kinderhelm und Schloss inklusive, optionalen Kindersitz, kostenlose Gepäckaufbewahrung, lokale Routentipps und flexible Zeiten für Abholung oder Rückgabe.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/de/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/de/bike/#breadcrumb"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#breadcrumb",
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
          "name": "Fahrradverleih",
          "item": "https://rentalscooterbarcelona.com/de/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokaler Verleihshop in Vila Olímpica del Poblenou, Barcelona, mit Scooter-, Inlineskates-, Fahrrad-, Rollschuh-, Skateboard- und Longboard-Verleih nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta. Beim Fahrradverleih sind Kinderhelm und Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Kreditkarte, Debitkarte, PayPal",
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
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#service",
      "name": "Fahrradverleih in Barcelona",
      "serviceType": "Fahrradverleih",
      "description": "Unser Fahrradverleih in Barcelona nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta bietet bequeme Citybikes für Erwachsene und Kinder. Kinderhelm und Schloss sind bei jeder Miete inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 Stunde",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "1 Stunde Fahrradverleih nahe Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 Stunden",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "4 Stunden Fahrradverleih nahe Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Ganzer Tag",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "Ganztägiger Fahrradverleih in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 Stunden",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "24-Stunden-Fahrradverleih in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 Tage",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "2-Tage-Fahrradverleih in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Zusätzlicher Tag",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/de/bike/",
          "description": "Zusätzlicher Tag Fahrradverleih in Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ],
      "url": "https://rentalscooterbarcelona.com/de/bike/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Brauche ich Erfahrung, um ein Fahrrad zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein, Vorerfahrung ist nicht nötig. Wir vermieten Fahrräder an Anfänger und sichere Fahrer, und unser Team hilft dir, ein bequemes Fahrrad für den Einstieg zu wählen."
          }
        },
        {
          "@type": "Question",
          "name": "Sind Helm oder Schloss in der Miete enthalten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar."
          }
        },
        {
          "@type": "Question",
          "name": "Wo kann ich in der Nähe des Shops Fahrrad fahren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Unser Shop liegt nahe der Strandpromenade, Port Olímpic, Torre MAPFRE und Casino Barcelona, in einem Bereich, in dem viele Besucher eine entspannte Route starten, bevor sie Parks und nahegelegene Radwege erkunden."
          }
        },
        {
          "@type": "Question",
          "name": "Gibt es Fahrräder für Anfänger oder Kinder?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder."
          }
        },
        {
          "@type": "Question",
          "name": "Brauche ich einen Führerschein, um ein Fahrrad zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein. Für die Fahrradmiete ist kein Führerschein erforderlich."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. In unserem beaufsichtigten Shop gibt es kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck, während du fährst."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich per WhatsApp buchen oder Fragen stellen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um Verfügbarkeit zu bestätigen, Fragen zu stellen oder die Abholzeit zu vereinbaren."
          }
        },
        {
          "@type": "Question",
          "name": "Wie kann ich buchen oder Kontakt aufnehmen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Fahrradverfügbarkeit oder den besten Zeitpunkt zur Abholung bestätigen möchtest."
          }
        }
      ],
      "inLanguage": "de"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/de/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/de/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/de/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/de/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/de/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/de/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/de/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Mein Freund und ich haben ein Paar Skates und ein Fahrrad gemietet, um die Strandpromenade entlangzufahren, und es hat sehr viel Spaß gemacht! Die Besitzer waren sehr lieb und hilfsbereit, und der Preis war großartig! Wir sind mit diesem Ort sehr zufrieden und werden wiederkommen.“\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Gvidas Gečas"
      },
      "datePublished": "2023-02-05",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Super. Günstig und gut gelegen; ich bekam ein repariertes Fahrrad, das geduldig genug war, um täglich durch die ganze Stadt zu fahren; sogar die Schuhe haben gepasst!😁“\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Fabio Mendes"
      },
      "datePublished": "2020-02-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Wir waren hier, um Fahrräder für eine Fahrt an der Strandpromenade zu mieten. Oscar war sehr freundlich und kam direkt auf den Punkt. Schneller, einfacher Mietvorgang, keine langen Formulare oder Erklärungen. Guter, fairer Preis, und schon kann es losgehen! Vielen Dank, Oscar.“\"",
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
<title>Fietsverhuur in Barcelona | Stadsfietsen bij Port Olímpic | RSB</title>
<meta content="Fiets huren in Barcelona vlak bij Port Olímpic en Barceloneta. Stadsfietsen voor volwassenen en kinderen, slot en kinderhelm inbegrepen." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/nl/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Fietsverhuur in Barcelona | Stadsfietsen bij Port Olímpic | RSB" property="og:title"/>
<meta content="Huur fietsen in Barcelona vlak bij Port Olímpic en het strand van Barceloneta. Onze lokale winkel in Vila Olímpica biedt comfortabele stadsfietsen voor volwassenen en kinderen, kinderhelm en slot inbegrepen, optioneel kinderzitje, gratis bagageopslag, lokale routetips en flexibele tijden voor ophalen of terugbrengen." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/nl/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Fietsverhuur in Barcelona vlak bij Vila Olímpica del Poblenou en het strand van Barceloneta" property="og:image:alt"/>
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
<meta content="Fietsverhuur in Barcelona | Stadsfietsen bij Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Huur fietsen in Barcelona vlak bij Port Olímpic en het strand van Barceloneta. Onze lokale winkel in Vila Olímpica biedt comfortabele stadsfietsen voor volwassenen en kinderen, kinderhelm en slot inbegrepen, optioneel kinderzitje, gratis bagageopslag, lokale routetips en flexibele tijden voor ophalen of terugbrengen." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Fietsverhuur in Barcelona vlak bij Vila Olímpica del Poblenou en het strand van Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met verhuur van scooters, inline skates, fietsen, rolschaatsen, skateboards en longboards vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta. Bij de fietsverhuur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.",
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
          "contactType": "klantenservice",
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
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/nl/bike/",
      "name": "Fietsverhuur in Barcelona | Stadsfietsen bij Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "nl",
      "description": "Huur fietsen in Barcelona vlak bij Port Olímpic en het strand van Barceloneta. Onze lokale winkel in Vila Olímpica biedt comfortabele stadsfietsen voor volwassenen en kinderen, kinderhelm en slot inbegrepen, optioneel kinderzitje, gratis bagageopslag, lokale routetips en flexibele tijden voor ophalen of terugbrengen.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/nl/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Start",
          "item": "https://rentalscooterbarcelona.com/nl/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Fietsverhuur",
          "item": "https://rentalscooterbarcelona.com/nl/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met verhuur van scooters, inline skates, fietsen, rolschaatsen, skateboards en longboards vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta. Bij de fietsverhuur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Creditcard, betaalkaart, PayPal",
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
          "contactType": "klantenservice",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#service",
      "name": "Fietsverhuur in Barcelona",
      "serviceType": "Fietsverhuur",
      "description": "Onze fietsverhuur in Barcelona, vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta, biedt comfortabele stadsfietsen voor volwassenen en kinderen. Bij elke huur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 uur",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "1 uur fietsverhuur vlak bij Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 uur",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "4 uur fietsverhuur vlak bij Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Hele dag",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "Hele dag fietsverhuur in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 uur",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "24 uur fietsverhuur in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 dagen",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "2 dagen fietsverhuur in Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Extra dag",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/nl/bike/",
          "description": "Extra dag fietsverhuur in Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Heb ik ervaring nodig om een fiets te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, eerdere ervaring is niet nodig. We verhuren fietsen aan beginners en aan mensen die al zeker fietsen, en ons team kan je helpen een comfortabele fiets te kiezen om te starten."
          }
        },
        {
          "@type": "Question",
          "name": "Zijn een helm of slot inbegrepen bij de huur?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar."
          }
        },
        {
          "@type": "Question",
          "name": "Waar kan ik fietsen in de buurt van de winkel?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Onze winkel ligt dicht bij de boulevard, Port Olímpic, Torre MAPFRE en Casino Barcelona, in een gebied waar veel bezoekers een rustige route beginnen voordat ze parken en fietspaden in de buurt verkennen."
          }
        },
        {
          "@type": "Question",
          "name": "Hebben jullie fietsen voor beginners of kinderen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. We kunnen je helpen een fiets te kiezen die past bij je lengte en niveau, inclusief fietsen die geschikt zijn voor kinderen."
          }
        },
        {
          "@type": "Question",
          "name": "Heb ik een rijbewijs nodig om een fiets te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren."
          }
        },
        {
          "@type": "Question",
          "name": "Kan ik mijn tas of bagage in de winkel achterlaten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. We bieden gratis opslag voor jassen, rugzakken en bagage in onze bewaakte winkel terwijl je fietst."
          }
        },
        {
          "@type": "Question",
          "name": "Kan ik via WhatsApp reserveren of vragen stellen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen."
          }
        },
        {
          "@type": "Question",
          "name": "Hoe reserveer ik of neem ik contact met jullie op?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen."
          }
        }
      ],
      "inLanguage": "nl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/nl/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/nl/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/nl/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/nl/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/nl/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Mijn vriend en ik huurden een paar skates en een fiets om over de boulevard te gaan en het was zo leuk! De eigenaren waren zo lief en behulpzaam en de prijs was geweldig! We zijn erg blij met deze plek en komen terug.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Gvidas Gečas"
      },
      "datePublished": "2023-02-05",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Super. Betaalbaar en goed gelegen; ik kreeg een gerepareerde fiets die geduldig genoeg was om dagelijks door de hele stad te rijden; zelfs de schoenen pasten!😁\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Fabio Mendes"
      },
      "datePublished": "2020-02-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"We kwamen hier om fietsen te huren voor een rit langs het strandpad. Oscar was erg vriendelijk en direct. Snel en eenvoudig huurproces, zonder lange formulieren of verhalen. Goede, eerlijke prijs en je kunt op weg! Bedankt, Oscar.\"",
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
<title>Aluguer de bicicletas em Barcelona | RSB</title>
<meta content="Aluguer de bicicletas em Barcelona perto de Port Olímpic e Barceloneta. Bicicletas para adultos e crianças, cadeado e capacete incluídos." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pt/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Aluguer de bicicletas em Barcelona | Bicicletas urbanas perto de Port Olímpic | RSB" property="og:title"/>
<meta content="Aluga bicicletas em Barcelona perto de Port Olímpic e da praia da Barceloneta. A nossa loja local em Vila Olímpica oferece bicicletas urbanas confortáveis para adultos e crianças, capacete infantil e cadeado incluídos, cadeira infantil opcional, serviço gratuito de guarda de bagagem e dicas de rotas locais." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pt/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Aluguer de bicicletas em Barcelona perto de Vila Olímpica del Poblenou e da praia da Barceloneta" property="og:image:alt"/>
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
<meta content="Aluguer de bicicletas em Barcelona | Bicicletas urbanas perto de Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Aluga bicicletas em Barcelona perto de Port Olímpic e da praia da Barceloneta. A nossa loja local em Vila Olímpica oferece bicicletas urbanas confortáveis para adultos e crianças, capacete infantil e cadeado incluídos, cadeira infantil opcional, serviço gratuito de guarda de bagagem e dicas de rotas locais." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Aluguer de bicicletas em Barcelona perto de Vila Olímpica del Poblenou e da praia da Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de 4 rodas, skateboard e longboard perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta. No aluguer de bicicletas estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.",
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
          "contactType": "apoio ao cliente",
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
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/pt/bike/",
      "name": "Aluguer de bicicletas em Barcelona | Bicicletas urbanas perto de Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "pt-PT",
      "description": "Aluga bicicletas em Barcelona perto de Port Olímpic e da praia da Barceloneta. A nossa loja local em Vila Olímpica oferece bicicletas urbanas confortáveis para adultos e crianças, capacete infantil e cadeado incluídos, cadeira infantil opcional, serviço gratuito de guarda de bagagem e dicas de rotas locais.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pt/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#breadcrumb",
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
          "name": "Aluguer de bicicletas",
          "item": "https://rentalscooterbarcelona.com/pt/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de 4 rodas, skateboard e longboard perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta. No aluguer de bicicletas estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Cartão de crédito, cartão de débito, PayPal",
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
          "contactType": "apoio ao cliente",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#service",
      "name": "Aluguer de bicicletas em Barcelona",
      "serviceType": "Aluguer de bicicletas",
      "description": "O nosso serviço de aluguer de bicicletas em Barcelona, perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta, oferece bicicletas urbanas confortáveis para adultos e crianças. Em cada aluguer estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 hora",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "1 hora de aluguer de bicicleta perto de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 horas",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "4 horas de aluguer de bicicleta perto de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Dia completo",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "Aluguer de bicicleta de dia completo em Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 horas",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "Aluguer de bicicleta de 24 horas em Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 dias",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "Aluguer de bicicleta de 2 dias em Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Dia extra",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pt/bike/",
          "description": "Dia extra de aluguer de bicicleta em Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Preciso de experiência para alugar uma bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não, não precisas de experiência anterior. Alugamos bicicletas a principiantes e a pessoas que já pedalam com confiança, e a nossa equipa pode ajudar-te a escolher uma bicicleta confortável para começar."
          }
        },
        {
          "@type": "Question",
          "name": "O capacete ou o cadeado estão incluídos no aluguer?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional."
          }
        },
        {
          "@type": "Question",
          "name": "Onde posso andar de bicicleta perto da loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A nossa loja fica perto do passeio marítimo, Port Olímpic, Torre MAPFRE e Casino Barcelona, numa zona de onde muitos visitantes começam um percurso tranquilo antes de explorar parques e ciclovias próximas."
          }
        },
        {
          "@type": "Question",
          "name": "Têm bicicletas para principiantes ou para crianças?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Podemos ajudar-te a escolher uma bicicleta adequada à tua altura e ao teu nível, incluindo bicicletas apropriadas para crianças."
          }
        },
        {
          "@type": "Question",
          "name": "Preciso de carta de condução para alugar uma bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso guardar a minha mala ou bagagem na loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas."
          }
        },
        {
          "@type": "Question",
          "name": "Posso reservar ou fazer perguntas por WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha."
          }
        },
        {
          "@type": "Question",
          "name": "Como reservo ou como vos contacto?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua."
          }
        }
      ],
      "inLanguage": "pt-PT"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/pt/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/pt/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/pt/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/pt/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/pt/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Eu e o meu namorado alugámos um par de patins e uma bicicleta para percorrer o passeio marítimo e foi muito divertido! Os proprietários foram muito queridos e prestáveis e o preço foi ótimo! Ficámos muito satisfeitos com este sítio e vamos voltar.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Gvidas Gečas"
      },
      "datePublished": "2023-02-05",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Excelente. Acessível e bem localizado; deram-me uma bicicleta reparada que foi suficientemente paciente para percorrer toda a cidade diariamente; até os sapatos combinaram!😁\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "João Junior"
      },
      "datePublished": "2021-04-21",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲\"",
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
<title>Lloguer de bicicletes a Barcelona | RSB</title>
<meta content="Lloga bicicletes a Barcelona prop de Port Olímpic i Barceloneta. Casc infantil, candau, guarda d’equipatge i consells de ruta inclosos." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/cat/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Lloguer de bicicletes a Barcelona | Bicicletes urbanes a prop de Port Olímpic | RSB" property="og:title"/>
<meta content="Lloga bicicletes a Barcelona a prop de Port Olímpic i de la platja de la Barceloneta. La nostra botiga local a Vila Olímpica ofereix còmodes bicicletes urbanes per a adults i nens, casc infantil i cadenat inclosos, cadireta infantil opcional, servei gratuït de guarda d’equipatge i consells de rutes locals." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/cat/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Lloguer de bicicletes a Barcelona a prop de Vila Olímpica del Poblenou i de la platja de la Barceloneta" property="og:image:alt"/>
<meta content="ca_ES" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Lloguer de bicicletes a Barcelona | Bicicletes urbanes a prop de Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Lloga bicicletes a Barcelona a prop de Port Olímpic i de la platja de la Barceloneta. La nostra botiga local a Vila Olímpica ofereix còmodes bicicletes urbanes per a adults i nens, casc infantil i cadenat inclosos, cadireta infantil opcional, servei gratuït de guarda d’equipatge i consells de rutes locals." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Lloguer de bicicletes a Barcelona a prop de Vila Olímpica del Poblenou i de la platja de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<!-- Use global site styles -->
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
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
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta. Amb el lloguer de bicicletes s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.",
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
          "contactType": "atenció al client",
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
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/cat/bike/",
      "name": "Lloguer de bicicletes a Barcelona | Bicicletes urbanes a prop de Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "ca",
      "description": "Lloga bicicletes a Barcelona a prop de Port Olímpic i de la platja de la Barceloneta. La nostra botiga local a Vila Olímpica ofereix còmodes bicicletes urbanes per a adults i nens, casc infantil i cadenat inclosos, cadireta infantil opcional, servei gratuït de guarda d’equipatge i consells de rutes locals.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/cat/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#breadcrumb",
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
          "name": "Lloguer de bicicletes",
          "item": "https://rentalscooterbarcelona.com/cat/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta. Amb el lloguer de bicicletes s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Targeta de crèdit, targeta de dèbit, PayPal",
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
          "contactType": "atenció al client",
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
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#service",
      "name": "Lloguer de bicicletes a Barcelona",
      "serviceType": "Lloguer de bicicletes",
      "description": "El nostre servei de lloguer de bicicletes a Barcelona, a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta, ofereix còmodes bicicletes urbanes per a adults i nens. Amb cada lloguer s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 hora",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "1 hora de lloguer de bicicleta a prop de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 hores",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "4 hores de lloguer de bicicleta a prop de Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Dia complet",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "Lloguer de bicicleta de dia complet a Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 hores",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "Lloguer de bicicleta de 24 hores a Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 dies",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "Lloguer de bicicleta de 2 dies a Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Dia extra",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/cat/bike/",
          "description": "Dia extra de lloguer de bicicleta a Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ],
      "url": "https://rentalscooterbarcelona.com/cat/bike/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Necessito experiència per llogar una bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no cal experiència prèvia. Lloguem bicicletes a principiants i a persones que ja pedalen amb confiança, i el nostre equip pot ajudar-te a triar una bicicleta còmoda per començar."
          }
        },
        {
          "@type": "Question",
          "name": "S’inclou casc o cadenat amb el lloguer?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional."
          }
        },
        {
          "@type": "Question",
          "name": "On puc anar amb bicicleta a prop de la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La nostra botiga és a prop del passeig marítim, Port Olímpic, Torre MAPFRE i Casino Barcelona, en una zona des d’on molts visitants comencen una ruta tranquil·la abans d’explorar parcs i carrils bici propers."
          }
        },
        {
          "@type": "Question",
          "name": "Teniu bicicletes per a principiants o per a nens?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens."
          }
        },
        {
          "@type": "Question",
          "name": "Necessito carnet per llogar una bicicleta?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid."
          }
        },
        {
          "@type": "Question",
          "name": "Puc guardar la meva bossa o equipatge a la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales."
          }
        },
        {
          "@type": "Question",
          "name": "Puc reservar o fer preguntes per WhatsApp?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida."
          }
        },
        {
          "@type": "Question",
          "name": "Com reservo o com us contacto?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar la disponibilitat de les bicicletes o el millor moment per recollir la teva."
          }
        }
      ],
      "inLanguage": "ca"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/cat/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/cat/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/cat/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/cat/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/cat/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"El meu xicot i jo vam llogar uns patins i una bicicleta per recórrer el passeig marítim i va ser molt divertit! Els propietaris van ser molt amables i servicials i el preu va ser fantàstic! Estem molt contents amb aquest lloc i hi tornarem.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Marta"
      },
      "datePublished": "2021-04-02",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Ideal per llogar bicis i fer un passeig per la platja. Personal molt amable i molt bon preu.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Roex Info"
      },
      "datePublished": "2018-12-28",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Es molt bona empressa de Lloguer de biciletes, el tracta es molt bó al igual que la qualitat del material que llogues. Recomanable 100% :)\"",
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
<title>Cykeluthyrning i Barcelona | Stadscyklar nära Port Olímpic | RSB</title>
<meta content="Hyra cykel i Barcelona nära Port Olímpic och Barceloneta. Stadscyklar för vuxna och barn, lås och barnhjälm ingår." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/sv/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Cykeluthyrning i Barcelona | Stadscyklar nära Port Olímpic | RSB" property="og:title"/>
<meta content="Hyr cyklar i Barcelona mitt emot stranden och intill Port Olímpic. Vår lokala butik i Vila Olímpica erbjuder bekväma stadscyklar för vuxna och barn, barnhjälm och lås ingår, barnsits som tillval, gratis bagageförvaring och lokala ruttips." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/sv/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Cykeluthyrning i Barcelona nära Vila Olímpica del Poblenou och Barceloneta-stranden" property="og:image:alt"/>
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
<meta content="Cykeluthyrning i Barcelona | Stadscyklar nära Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Hyr cyklar i Barcelona mitt emot stranden och intill Port Olímpic. Vår lokala butik i Vila Olímpica erbjuder bekväma stadscyklar för vuxna och barn, barnhjälm och lås ingår, barnsits som tillval, gratis bagageförvaring och lokala ruttips." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Cykeluthyrning i Barcelona nära Vila Olímpica del Poblenou och Barceloneta-stranden" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med uthyrning av scooter, inlines, cyklar, rullskridskor, skateboard och longboard nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden. Vid cykeluthyrning ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.",
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
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/sv/bike/",
      "name": "Cykeluthyrning i Barcelona | Stadscyklar nära Port Olímpic | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "sv",
      "description": "Hyr cyklar i Barcelona mitt emot stranden och intill Port Olímpic. Vår lokala butik i Vila Olímpica erbjuder bekväma stadscyklar för vuxna och barn, barnhjälm och lås ingår, barnsits som tillval, gratis bagageförvaring och lokala ruttips.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/sv/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/bike/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#breadcrumb",
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
          "name": "Cykeluthyrning",
          "item": "https://rentalscooterbarcelona.com/sv/bike/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med uthyrning av scooter, inlines, cyklar, rullskridskor, skateboard och longboard nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden. Vid cykeluthyrning ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
      "telephone": "+34 640 559 468",
      "email": "info@rentalscooterbarcelona.com",
      "priceRange": "€4–€115",
      "paymentAccepted": "Kreditkort, betalkort, PayPal",
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
        "https://www.facebook.com/rentalscooterbarcelona",
        "https://www.instagram.com/rentalscooterbarcelona/",
        "https://x.com/RSBscooterbarce",
        "https://es.pinterest.com/rsbscooter/",
        "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html",
        "https://www.google.com/maps?cid=912877649802486634",
        "https://maps.apple.com/place?place-id=IA5C7938C1925731A&address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&coordinate=41.3906488%2C2.1984312&name=Rental+Scooter&_provider=9902",
        "https://www.bing.com/maps/search?style=r&q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&ss=id.local_ypid%3A%22YND84466019C726C1%22"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#service",
      "name": "Cykeluthyrning i Barcelona",
      "serviceType": "Cykeluthyrning",
      "description": "Vår cykeluthyrning i Barcelona, nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden, erbjuder bekväma stadscyklar för vuxna och barn. Barnhjälm och lås ingår vid varje hyra, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.",
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
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 timme",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "1 timmes cykeluthyrning nära Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 timmar",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "4 timmars cykeluthyrning nära Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Heldag",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "Heldagsuthyrning av cykel i Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 timmar",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "24 timmars cykeluthyrning i Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 dagar",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "2 dagars cykeluthyrning i Barcelona",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Extra dag",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/sv/bike/",
          "description": "Extra dag cykeluthyrning i Barcelona",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Behöver jag erfarenhet för att hyra en cykel?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med."
          }
        },
        {
          "@type": "Question",
          "name": "Ingår hjälm eller lås i hyran?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval."
          }
        },
        {
          "@type": "Question",
          "name": "Var kan jag cykla nära butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vår butik ligger nära strandpromenaden, Port Olímpic, Torre MAPFRE och Casino Barcelona, i ett område där många besökare börjar en lugn tur innan de utforskar parker och närliggande cykelvägar."
          }
        },
        {
          "@type": "Question",
          "name": "Har ni cyklar för nybörjare eller barn?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Vi kan hjälpa dig att välja en cykel som passar din längd och nivå, inklusive cyklar som passar barn."
          }
        },
        {
          "@type": "Question",
          "name": "Behöver jag körkort för att hyra en cykel?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej. Inget körkort krävs för att hyra en cykel."
          }
        },
        {
          "@type": "Question",
          "name": "Kan jag lämna min väska eller mitt bagage i butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Vi erbjuder gratis förvaring för jackor, ryggsäckar och bagage i vår övervakade butik medan du cyklar."
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
            "text": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel."
          }
        }
      ],
      "inLanguage": "sv"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/sv/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/sv/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/sv/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/sv/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/sv/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Min pojkvän och jag hyrde ett par rullskridskor och en cykel för att ta oss längs strandpromenaden, och det var så roligt! Ägarna var mycket vänliga och hjälpsamma och priset var toppen! Vi är mycket nöjda med stället och kommer tillbaka.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Alfonso Arellano"
      },
      "datePublished": "2026-03-13",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Jag hyrde en cykel här och blev verkligen mycket nöjd. Priserna är mycket bra jämfört med andra ställen och cyklarna är i gott skick. Dessutom är ägaren mycket trevlig och bemötandet var vänligt från första stund; hon förklarar allt lugnt och får dig att känna dig bekväm. Det är utan tvekan ett ställe jag rekommenderar om du behöver hyra en cykel enkelt och till ett bra pris. Jag skulle hyra här igen utan att tveka.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Fabio Mendes"
      },
      "datePublished": "2020-02-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Jag gick hit för att hyra cyklar och cykla längs strandvägen. Oscar var mycket vänlig och saklig. Uthyrningen gick snabbt och enkelt, utan långa formulär eller genomgångar. Ett bra och rättvist pris, sedan är det bara att ge sig av! Tack, Oscar.\"",
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
<title>Wynajem rowerów w Barcelonie | RSB</title>
<meta content="Wynajmij rowery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Rowery miejskie dla dorosłych i dzieci, kask i zapięcie w cenie, opcjonalny fotelik dziecięcy i lokalne trasy." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pl/bike/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/bike/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/bike/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/bike/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/bike/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/bike/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/bike/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/bike/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/bike/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/bike/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/bike/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Wynajem rowerów w Barcelonie | Rowery miejskie przy Port Olímpic | RSB" property="og:title"/>
<meta content="Wynajmij rowery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Rowery miejskie dla dorosłych i dzieci, kask i zapięcie w cenie, opcjonalny fotelik dziecięcy i lokalne trasy." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pl/bike/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Wynajem rowerów w Barcelonie blisko Vila Olímpica del Poblenou i plaży Barceloneta" property="og:image:alt"/>
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
<meta content="Wynajem rowerów w Barcelonie | Rowery miejskie przy Port Olímpic | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Wynajmij rowery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Rowery miejskie dla dorosłych i dzieci, kask i zapięcie w cenie, opcjonalny fotelik dziecięcy i lokalne trasy." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Wynajem rowerów w Barcelonie blisko Vila Olímpica del Poblenou i plaży Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Wynajem" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
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
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#webpage",
      "url": "https://rentalscooterbarcelona.com/pl/bike/",
      "name": "Wynajem rowerów w Barcelonie | Rowery miejskie przy Port Olímpic",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "pl",
      "description": "Wynajmij rowery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Rowery miejskie dla dorosłych i dzieci, kask i zapięcie w cenie, opcjonalny fotelik dziecięcy i lokalne trasy.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pl/bike/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/bike/#faq"
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
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#breadcrumb",
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
          "name": "Wynajem rowerów",
          "item": "https://rentalscooterbarcelona.com/pl/bike/"
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
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#service",
      "name": "Wynajem rowerów w Barcelonie",
      "serviceType": "Wynajem rowerów",
      "description": "Nasza usługa wynajmu rowerów w Barcelonie naprzeciwko plaży i obok Port Olímpic oferuje wygodne rowery miejskie dla dorosłych i dzieci. Kask dziecięcy i zapięcie są w cenie każdego wynajmu, opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach, a także zapewniamy darmowe przechowanie rzeczy i lokalne wskazówki tras.",
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
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Zakres cen wynajmu rowerów",
          "priceCurrency": "EUR",
          "lowPrice": "4",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/pl/bike/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "1 godzina",
          "price": "4",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "1 godzina wynajem rowerów blisko Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "4 godziny",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "4 hour wynajem rowerów blisko Port Olímpic",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Cały dzień",
          "price": "10",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "Całodniowy wynajem rowerów w Barcelonie",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "24 godziny",
          "price": "12",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "24 hour wynajem rowerów w Barcelonie",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "2 dni",
          "price": "20",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "Dwudniowy wynajem rowerów w Barcelonie",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Dodatkowy dzień",
          "price": "8",
          "priceCurrency": "EUR",
          "url": "https://rentalscooterbarcelona.com/pl/bike/",
          "description": "Dodatkowy dzień wynajmu rowerów w Barcelonie",
          "availability": "https://schema.org/InStock"
        }
      ],
      "url": "https://rentalscooterbarcelona.com/pl/bike/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Czy potrzebuję doświadczenia, aby wynająć rower?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy rowery początkującym i pewnym siebie rowerzystom, a nasz zespół pomoże wybrać wygodny rower na start."
          }
        },
        {
          "@type": "Question",
          "name": "Czy kask lub zapięcie są wliczone w wynajem?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach."
          }
        },
        {
          "@type": "Question",
          "name": "Gdzie mogę jeździć rowerem blisko wypożyczalni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym zwiedzaniem parków i pobliskich ścieżek rowerowych."
          }
        },
        {
          "@type": "Question",
          "name": "Czy macie rowery dla początkujących lub dzieci?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Pomożemy dobrać rower do Twojego wzrostu i poziomu doświadczenia, także rowery odpowiednie dla dzieci."
          }
        },
        {
          "@type": "Question",
          "name": "Czy potrzebuję prawa jazdy, aby wynająć rower?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie. Do wynajmu roweru nie jest wymagane prawo jazdy."
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
            "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność roweru albo najlepszą godzinę odbioru."
          }
        }
      ],
      "inLanguage": "pl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#itemlist",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "url": "https://rentalscooterbarcelona.com/pl/scooter/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "url": "https://rentalscooterbarcelona.com/pl/bike/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "url": "https://rentalscooterbarcelona.com/pl/rollerblades/"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "url": "https://rentalscooterbarcelona.com/pl/skateboard/"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "url": "https://rentalscooterbarcelona.com/pl/longboard/"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "url": "https://rentalscooterbarcelona.com/pl/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Bailey Brooke"
      },
      "datePublished": "2026-04-04",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Mój chłopak i ja wynajęliśmy parę rolek i rower, aby przejechać się promenadą, i świetnie się bawiliśmy! Właściciele byli bardzo mili i pomocni, a cena była świetna! Jesteśmy bardzo zadowoleni z tego miejsca i wrócimy.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Alfonso Arellano"
      },
      "datePublished": "2026-03-13",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Wynająłem tutaj rower i byłem naprawdę bardzo zadowolony. Ceny są bardzo dobre w porównaniu z innymi miejscami, a rowery są w dobrym stanie. Właścicielka jest bardzo sympatyczna i od pierwszej chwili traktuje klientów życzliwie; wszystko spokojnie wyjaśnia i sprawia, że czujesz się swobodnie. Zdecydowanie polecam to miejsce, jeśli potrzebujesz bezproblemowo wynająć rower w dobrej cenie. Bez wahania wynająłbym tutaj ponownie.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Fabio Mendes"
      },
      "datePublished": "2020-02-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Przyszedłem tutaj wynająć rowery na przejażdżkę ścieżką przy plaży. Oscar był bardzo miły i konkretny. Wynajem przebiegł szybko i łatwo, bez długich formularzy ani przemówień. Dobra, uczciwa cena i można ruszać! Dziękuję, Oscar.\"",
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
| en | https://rentalscooterbarcelona.com/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| es | https://rentalscooterbarcelona.com/es/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| fr | https://rentalscooterbarcelona.com/fr/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| it | https://rentalscooterbarcelona.com/it/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| de | https://rentalscooterbarcelona.com/de/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| nl | https://rentalscooterbarcelona.com/nl/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| pt | https://rentalscooterbarcelona.com/pt/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| ca | https://rentalscooterbarcelona.com/cat/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| sv | https://rentalscooterbarcelona.com/sv/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |
| pl | https://rentalscooterbarcelona.com/pl/bike/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/bike/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/bike/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/bike/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/bike/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/bike/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/bike/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/bike/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/bike/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/bike/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/bike/", "hreflang": "pl", "rel": "alternate"}] | True |

## M. MATRIZ SCHEMA @id + URL

| Idioma | Bloque | Ruta | Entidad completa |
| --- | --- | --- | --- |
| en | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| en | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "en", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/bike/#webpage", "url": "https://rentalscooterbarcelona.com/bike/", "name": "Bike Rental Barcelona \| City Bikes Near Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "en", "description": "Rent bikes in Barcelona near Port Olímpic and Barceloneta. City bikes for adults and kids, helmet and lock included, child seat option and local route tips.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp booking", "target": "https://wa.me/34640559468"}} |
| en | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/"}, {"@type": "ListItem", "position": 2, "name": "Bike rental", "item": "https://rentalscooterbarcelona.com/bike/"}]} |
| en | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/bike/#service", "name": "Bike rental in Barcelona", "serviceType": "Bike rental", "description": "Our bike rental service in Barcelona near Port Olímpic and Barceloneta Beach offers comfortable city bikes for adults and kids. A children's helmet and lock are included with every rental, and an optional child seat is available on selected bikes. Free storage and local route recommendations provided.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Bike rental price range", "priceCurrency": "EUR", "lowPrice": "4", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/bike/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hour", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "1 hour bike rental near Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 hours", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "4 hour bike rental near Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Full day", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "Full day bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 hours", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "24 hour bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 days", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "2 day bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra day", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "Extra day bike rental in Barcelona", "availability": "https://schema.org/InStock"}], "url": "https://rentalscooterbarcelona.com/bike/"} |
| en | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Do I need experience to rent a bike?", "acceptedAnswer": {"@type": "Answer", "text": "No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started."}}, {"@type": "Question", "name": "Is a helmet or lock included with the rental?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes."}}, {"@type": "Question", "name": "Where can I ride a bike near the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby."}}, {"@type": "Question", "name": "Do you have bikes for beginners or kids?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids."}}, {"@type": "Question", "name": "Do I need a licence to rent a bike?", "acceptedAnswer": {"@type": "Answer", "text": "No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID."}}, {"@type": "Question", "name": "Can I store my bag or luggage at the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride."}}, {"@type": "Question", "name": "Can I book or ask questions by WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. You can message us on WhatsApp before coming to confirm availability, ask questions or arrange your pick-up time."}}, {"@type": "Question", "name": "How do I book or contact you?", "acceptedAnswer": {"@type": "Answer", "text": "You can book via WhatsApp, email or phone. Contact us if you want to confirm bike availability or the best time to collect your bike."}}], "inLanguage": "en"} |
| en | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/quads/"}]} |
| en | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/bike/#webpage", "dateModified": "2026-08-24"} |
| en | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/bike/#google-review-3"}]} |
| en | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"My boyfriend and I rented a pair of skates and bike to go up the board walk and it was so fun! The owners were so sweet and helpful and the price was great! Very happy with this place and will come back.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-04-04"} |
| en | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Super. Affordable and good location, got a fixed bike that was patient enough to drive all over the city daily, even shoes have matched!😁\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2023-02-05"} |
| en | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Went here to rent bikes to stroll the beach path. Oscar was very friendly and to the point. Fast easy process for renting, no long forms or speeches. Good, fair price and you're on your way! Thank you, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2020-02-20"} |
| es | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta. Con el alquiler de bicicletas se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| es | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "es", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/bike/#webpage", "url": "https://rentalscooterbarcelona.com/es/bike/", "name": "Alquiler de bicicletas en Barcelona \| Bicis urbanas \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "es", "description": "Alquiler de bicicletas en Barcelona, en la Vila Olímpica. Bicis urbanas para adultos y niños, candado incluido y rutas por Port Olímpic y Barceloneta.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/es/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/es/bike/#faq"}], "dateModified": "2026-07-30", "potentialAction": {"@type": "CommunicateAction", "name": "Reserva por WhatsApp", "target": "https://wa.me/34640559468"}, "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/es/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://rentalscooterbarcelona.com/es/"}, {"@type": "ListItem", "position": 2, "name": "Alquiler de bicicletas", "item": "https://rentalscooterbarcelona.com/es/bike/"}]} |
| es | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta. Con el alquiler de bicicletas se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Tarjeta de crédito, tarjeta de débito, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| es | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/es/bike/#service", "url": "https://rentalscooterbarcelona.com/es/bike/", "name": "Alquiler de bicicletas en Barcelona", "serviceType": "Alquiler de bicicletas", "description": "Nuestro servicio de alquiler de bicicletas en Barcelona, cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta, ofrece cómodas bicicletas urbanas para adultos y niños. Con cada alquiler se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. Consigna gratuita para el equipaje y recomendaciones de rutas locales incluidas.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Rango de precios del alquiler de bicicletas", "priceCurrency": "EUR", "lowPrice": "4", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/es/bike/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "1 hora de alquiler de bicicleta cerca de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 horas", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "4 horas de alquiler de bicicleta cerca de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Día completo", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de día completo en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 horas", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de 24 horas en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 días", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de 2 días en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Día extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Día extra de alquiler de bicicleta en Barcelona", "availability": "https://schema.org/InStock"}]} |
| es | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/es/bike/#faq", "mainEntity": [{"@type": "Question", "name": "¿Necesito experiencia para alquilar una bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "No, no necesitas experiencia previa. Alquilamos bicicletas a principiantes y a personas que ya montan con confianza, y nuestro equipo puede ayudarte a elegir una bicicleta cómoda para empezar."}}, {"@type": "Question", "name": "¿Se incluye casco o candado con el alquiler?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional."}}, {"@type": "Question", "name": "¿Dónde puedo montar en bicicleta cerca de la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Nuestra tienda está cerca del paseo marítimo, Port Olímpic, Torre MAPFRE y Casino Barcelona, en una zona desde la que muchos visitantes empiezan una ruta tranquila antes de explorar parques y carriles bici cercanos."}}, {"@type": "Question", "name": "¿Tenéis bicicletas para principiantes o para niños?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños."}}, {"@type": "Question", "name": "¿Necesito licencia para alquilar una bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido."}}, {"@type": "Question", "name": "¿Puedo guardar mi bolsa o equipaje en la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Disponemos de consigna gratuita para chaquetas, mochilas y equipaje en nuestra tienda supervisada mientras montas."}}, {"@type": "Question", "name": "¿Puedo reservar o preguntar por WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida."}}, {"@type": "Question", "name": "¿Cómo reservo o cómo contacto con vosotros?", "acceptedAnswer": {"@type": "Answer", "text": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya."}}], "inLanguage": "es"} |
| es | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/es/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/es/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/es/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/es/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/es/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/es/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/es/quads/"}]} |
| es | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/bike/#webpage", "dateModified": "2026-08-24"} |
| es | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-3"}]} |
| es | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Alquilé una bici aquí y la verdad es que quedé muy contento. Los precios están muy bien comparados con otros sitios y las bicicletas están en buen estado. Además, la dueña es súper maja y el trato fue muy amable desde el primer momento, te explica todo con calma y te hace sentir a gusto. Sin duda es un sitio muy recomendable si necesitas alquilar una bici sin complicaciones y a buen precio. Volvería a alquilar aquí sin dudarlo.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| es | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Me gustó mucho el trato, ya que la chica que nos atendió tenía un total conocimiento de Barcelona, nos dio muchos tips de que conocer y que lugares visitar Las bicicletas y patines , están en un buen estado y creo que el mantenimiento constante, hacen que está tienda tenga un material en excelentes condiciones Mil y mil gracias a Natalia por su servicio excelente Nos volveremos a ver muy pronto Super recomendable\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| es | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Me encanto la atención, muy amables. Pero sobre todo rentar una bici a un precio tan económico. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, avec location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta. Le casque pour enfant et l’antivol sont inclus avec la location de vélos, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "service client", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| fr | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "fr"} |
| fr | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/bike/#webpage", "url": "https://rentalscooterbarcelona.com/fr/bike/", "name": "Location de vélos à Barcelone \| Vélos urbains près de Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "fr", "description": "Louez un vélo urbain à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, antivol, consigne gratuite et conseils d’itinéraires inclus.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/fr/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/fr/bike/#faq"}], "dateModified": "2026-07-30"} |
| fr | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/fr/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://rentalscooterbarcelona.com/fr/"}, {"@type": "ListItem", "position": 2, "name": "Location de vélos", "item": "https://rentalscooterbarcelona.com/fr/bike/"}]} |
| fr | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, avec location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta. Le casque pour enfant et l’antivol sont inclus avec la location de vélos, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Carte de crédit, carte de débit, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "service client", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| fr | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/fr/bike/#service", "name": "Location de vélos à Barcelone", "serviceType": "Location de vélos", "description": "Notre service de location de vélos à Barcelone, près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta, propose des vélos urbains confortables pour adultes et enfants. Le casque pour enfant et l’antivol sont inclus avec chaque location, et un siège enfant en option est disponible sur certains vélos. Consigne gratuite pour les bagages et recommandations d’itinéraires locaux incluses.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 heure", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "1 heure de location de vélo près de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 heures", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "4 heures de location de vélo près de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Journée complète", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo à la journée à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 heures", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo 24 heures à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 jours", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo 2 jours à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Jour supplémentaire", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Jour supplémentaire de location de vélo à Barcelone", "availability": "https://schema.org/InStock"}]} |
| fr | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/fr/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Ai-je besoin d’expérience pour louer un vélo ?", "acceptedAnswer": {"@type": "Answer", "text": "Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer."}}, {"@type": "Question", "name": "Le casque ou l’antivol sont-ils inclus avec la location ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos."}}, {"@type": "Question", "name": "Où puis-je rouler à vélo près de la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Notre boutique se trouve près de la promenade du front de mer, de Port Olímpic, de Torre MAPFRE et de Casino Barcelona, dans un secteur où de nombreux visiteurs commencent une balade tranquille avant d’explorer les parcs et pistes cyclables à proximité."}}, {"@type": "Question", "name": "Avez-vous des vélos pour débutants ou pour enfants ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants."}}, {"@type": "Question", "name": "Ai-je besoin d’un permis pour louer un vélo ?", "acceptedAnswer": {"@type": "Answer", "text": "Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un."}}, {"@type": "Question", "name": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Nous disposons d’une consigne gratuite pour les vestes, sacs à dos et bagages dans notre boutique surveillée pendant votre sortie."}}, {"@type": "Question", "name": "Puis-je réserver ou poser des questions par WhatsApp ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait."}}, {"@type": "Question", "name": "Comment réserver ou vous contacter ?", "acceptedAnswer": {"@type": "Answer", "text": "Vous pouvez réserver via WhatsApp, e-mail ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des vélos ou le meilleur moment pour venir chercher le vôtre."}}], "inLanguage": "fr"} |
| fr | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/fr/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/fr/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/fr/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/fr/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/fr/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/fr/quads/"}]} |
| fr | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/bike/#webpage", "dateModified": "2026-08-24"} |
| fr | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-3"}]} |
| fr | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai loué un vélo ici et j’en ai été vraiment très satisfait. Les prix sont très bons par rapport à d’autres endroits et les vélos sont en bon état. De plus, la propriétaire est très sympathique et l’accueil a été chaleureux dès le premier instant ; elle explique tout calmement et vous met à l’aise. C’est sans aucun doute un endroit très recommandable si vous avez besoin de louer un vélo facilement et à bon prix. J’y louerais de nouveau sans hésiter.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai beaucoup apprécié l’accueil, car la personne qui nous a aidés connaissait parfaitement Barcelone et nous a donné de nombreux conseils sur les lieux à découvrir et à visiter. Les vélos et les patins sont en bon état et je pense que l’entretien constant permet à cette boutique de proposer un matériel en excellent état. Mille mercis à Natalia pour son excellent service. Nous nous reverrons très bientôt. Je recommande vivement.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai adoré l’accueil, ils sont très aimables. Mais surtout, louer un vélo à un prix aussi économique. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta. Con il noleggio biciclette sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "servizio clienti", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| it | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "it"} |
| it | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/bike/#webpage", "url": "https://rentalscooterbarcelona.com/it/bike/", "name": "Noleggio biciclette a Barcellona \| Biciclette urbane vicino a Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "it", "description": "Noleggia biciclette a Barcellona vicino a Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica offre comode biciclette urbane per adulti e bambini, casco bambino e lucchetto inclusi, seggiolino opzionale, deposito bagagli gratuito e consigli sui percorsi locali.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/it/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/it/bike/#faq"}], "dateModified": "2026-07-30"} |
| it | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/it/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inizio", "item": "https://rentalscooterbarcelona.com/it/"}, {"@type": "ListItem", "position": 2, "name": "Noleggio biciclette", "item": "https://rentalscooterbarcelona.com/it/bike/"}]} |
| it | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta. Con il noleggio biciclette sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Carta di credito, carta di debito, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "servizio clienti", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| it | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/it/bike/#service", "name": "Noleggio biciclette a Barcellona", "serviceType": "Noleggio biciclette", "description": "Il nostro servizio di noleggio biciclette a Barcellona, vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta, offre comode city bike per adulti e bambini. Con ogni noleggio sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Deposito bagagli gratuito e consigli su percorsi locali inclusi.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 ora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "1 ora di noleggio bici vicino a Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 ore", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "4 ore di noleggio bici vicino a Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Giornata intera", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici per una giornata intera a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 ore", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici 24 ore a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 giorni", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici per 2 giorni a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Giorno extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Giorno extra di noleggio bici a Barcellona", "availability": "https://schema.org/InStock"}], "url": "https://rentalscooterbarcelona.com/it/bike/"} |
| it | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/it/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Ho bisogno di esperienza per noleggiare una bicicletta?", "acceptedAnswer": {"@type": "Answer", "text": "No, non è necessaria esperienza precedente. Noleggiamo biciclette sia a principianti sia a chi pedala già con sicurezza, e il nostro team può aiutarti a scegliere una bici comoda per iniziare."}}, {"@type": "Question", "name": "Il casco o il lucchetto sono inclusi nel noleggio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale."}}, {"@type": "Question", "name": "Dove posso andare in bici vicino al negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Il nostro negozio si trova vicino al lungomare, a Port Olímpic, Torre MAPFRE e Casino Barcelona, in una zona da cui molti visitatori iniziano un percorso tranquillo prima di esplorare parchi e piste ciclabili vicine."}}, {"@type": "Question", "name": "Avete biciclette per principianti o per bambini?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Possiamo aiutarti a scegliere una bicicletta adatta alla tua altezza e al tuo livello, comprese biciclette adatte ai bambini."}}, {"@type": "Question", "name": "Ho bisogno della patente per noleggiare una bicicletta?", "acceptedAnswer": {"@type": "Answer", "text": "No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido."}}, {"@type": "Question", "name": "Posso lasciare la mia borsa o i bagagli in negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali."}}, {"@type": "Question", "name": "Posso prenotare o fare domande via WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare la disponibilità, fare domande o organizzare l’orario di ritiro."}}, {"@type": "Question", "name": "Come posso prenotare o contattarvi?", "acceptedAnswer": {"@type": "Answer", "text": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle biciclette o il momento migliore per ritirare la tua."}}], "inLanguage": "it"} |
| it | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/it/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/it/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/it/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/it/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/it/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/it/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/it/quads/"}]} |
| it | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/bike/#webpage", "dateModified": "2026-08-24"} |
| it | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-3"}]} |
| it | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ho noleggiato una bicicletta qui e ne sono rimasto davvero molto soddisfatto. I prezzi sono molto buoni rispetto ad altri posti e le biciclette sono in buono stato. Inoltre, la proprietaria è molto simpatica e il trattamento è stato gentile fin dal primo momento; ti spiega tutto con calma e ti fa sentire a tuo agio. È senza dubbio un posto molto consigliato se hai bisogno di noleggiare una bicicletta senza complicazioni e a buon prezzo. Noleggerei di nuovo qui senza esitare.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mi è piaciuto molto il servizio, perché la ragazza che ci ha assistito conosceva perfettamente Barcellona e ci ha dato molti consigli su cosa vedere e quali luoghi visitare. Le biciclette e i pattini sono in buono stato e credo che la manutenzione costante permetta a questo negozio di avere materiale in condizioni eccellenti. Mille grazie a Natalia per il suo servizio eccellente. Ci rivedremo molto presto. Super consigliato.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mi è piaciuta molto l’attenzione, sono stati molto gentili. Ma soprattutto poter noleggiare una bicicletta a un prezzo così conveniente. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokaler Verleihshop in Vila Olímpica del Poblenou, Barcelona, mit Scooter-, Inlineskates-, Fahrrad-, Rollschuh-, Skateboard- und Longboard-Verleih nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta. Beim Fahrradverleih sind Kinderhelm und Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| de | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "de", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| de | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/bike/#webpage", "url": "https://rentalscooterbarcelona.com/de/bike/", "name": "Fahrradverleih in Barcelona \| Citybikes nahe Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "de", "description": "Miete Fahrräder in Barcelona nahe Port Olímpic und dem Strand der Barceloneta. Unser lokaler Shop in Vila Olímpica bietet bequeme Citybikes für Erwachsene und Kinder, Kinderhelm und Schloss inklusive, optionalen Kindersitz, kostenlose Gepäckaufbewahrung, lokale Routentipps und flexible Zeiten für Abholung oder Rückgabe.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/de/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/de/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/de/bike/#breadcrumb"}} |
| de | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/de/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://rentalscooterbarcelona.com/de/"}, {"@type": "ListItem", "position": 2, "name": "Fahrradverleih", "item": "https://rentalscooterbarcelona.com/de/bike/"}]} |
| de | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokaler Verleihshop in Vila Olímpica del Poblenou, Barcelona, mit Scooter-, Inlineskates-, Fahrrad-, Rollschuh-, Skateboard- und Longboard-Verleih nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta. Beim Fahrradverleih sind Kinderhelm und Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1200-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kreditkarte, Debitkarte, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| de | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/de/bike/#service", "name": "Fahrradverleih in Barcelona", "serviceType": "Fahrradverleih", "description": "Unser Fahrradverleih in Barcelona nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand der Barceloneta bietet bequeme Citybikes für Erwachsene und Kinder. Kinderhelm und Schloss sind bei jeder Miete inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Kostenlose Gepäckaufbewahrung und lokale Routentipps inklusive.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 Stunde", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "1 Stunde Fahrradverleih nahe Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 Stunden", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "4 Stunden Fahrradverleih nahe Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Ganzer Tag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "Ganztägiger Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 Stunden", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "24-Stunden-Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 Tage", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "2-Tage-Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Zusätzlicher Tag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "Zusätzlicher Tag Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}], "url": "https://rentalscooterbarcelona.com/de/bike/"} |
| de | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/de/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Brauche ich Erfahrung, um ein Fahrrad zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein, Vorerfahrung ist nicht nötig. Wir vermieten Fahrräder an Anfänger und sichere Fahrer, und unser Team hilft dir, ein bequemes Fahrrad für den Einstieg zu wählen."}}, {"@type": "Question", "name": "Sind Helm oder Schloss in der Miete enthalten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar."}}, {"@type": "Question", "name": "Wo kann ich in der Nähe des Shops Fahrrad fahren?", "acceptedAnswer": {"@type": "Answer", "text": "Unser Shop liegt nahe der Strandpromenade, Port Olímpic, Torre MAPFRE und Casino Barcelona, in einem Bereich, in dem viele Besucher eine entspannte Route starten, bevor sie Parks und nahegelegene Radwege erkunden."}}, {"@type": "Question", "name": "Gibt es Fahrräder für Anfänger oder Kinder?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder."}}, {"@type": "Question", "name": "Brauche ich einen Führerschein, um ein Fahrrad zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein. Für die Fahrradmiete ist kein Führerschein erforderlich."}}, {"@type": "Question", "name": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. In unserem beaufsichtigten Shop gibt es kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck, während du fährst."}}, {"@type": "Question", "name": "Kann ich per WhatsApp buchen oder Fragen stellen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um Verfügbarkeit zu bestätigen, Fragen zu stellen oder die Abholzeit zu vereinbaren."}}, {"@type": "Question", "name": "Wie kann ich buchen oder Kontakt aufnehmen?", "acceptedAnswer": {"@type": "Answer", "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Fahrradverfügbarkeit oder den besten Zeitpunkt zur Abholung bestätigen möchtest."}}], "inLanguage": "de"} |
| de | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/de/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/de/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/de/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/de/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/de/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/de/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/de/quads/"}]} |
| de | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/bike/#webpage", "dateModified": "2026-08-24"} |
| de | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-3"}]} |
| de | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Mein Freund und ich haben ein Paar Skates und ein Fahrrad gemietet, um die Strandpromenade entlangzufahren, und es hat sehr viel Spaß gemacht! Die Besitzer waren sehr lieb und hilfsbereit, und der Preis war großartig! Wir sind mit diesem Ort sehr zufrieden und werden wiederkommen.“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Super. Günstig und gut gelegen; ich bekam ein repariertes Fahrrad, das geduldig genug war, um täglich durch die ganze Stadt zu fahren; sogar die Schuhe haben gepasst!😁“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Wir waren hier, um Fahrräder für eine Fahrt an der Strandpromenade zu mieten. Oscar war sehr freundlich und kam direkt auf den Punkt. Schneller, einfacher Mietvorgang, keine langen Formulare oder Erklärungen. Guter, fairer Preis, und schon kann es losgehen! Vielen Dank, Oscar.“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met verhuur van scooters, inline skates, fietsen, rolschaatsen, skateboards en longboards vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta. Bij de fietsverhuur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "klantenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| nl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "nl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/bike/#webpage", "url": "https://rentalscooterbarcelona.com/nl/bike/", "name": "Fietsverhuur in Barcelona \| Stadsfietsen bij Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "nl", "description": "Huur fietsen in Barcelona vlak bij Port Olímpic en het strand van Barceloneta. Onze lokale winkel in Vila Olímpica biedt comfortabele stadsfietsen voor volwassenen en kinderen, kinderhelm en slot inbegrepen, optioneel kinderzitje, gratis bagageopslag, lokale routetips en flexibele tijden voor ophalen of terugbrengen.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/nl/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/nl/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/nl/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Start", "item": "https://rentalscooterbarcelona.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Fietsverhuur", "item": "https://rentalscooterbarcelona.com/nl/bike/"}]} |
| nl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met verhuur van scooters, inline skates, fietsen, rolschaatsen, skateboards en longboards vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta. Bij de fietsverhuur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Creditcard, betaalkaart, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "klantenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| nl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/nl/bike/#service", "name": "Fietsverhuur in Barcelona", "serviceType": "Fietsverhuur", "description": "Onze fietsverhuur in Barcelona, vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta, biedt comfortabele stadsfietsen voor volwassenen en kinderen. Bij elke huur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Gratis bagageopslag en lokale routetips inbegrepen.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 uur", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "1 uur fietsverhuur vlak bij Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 uur", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "4 uur fietsverhuur vlak bij Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Hele dag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "Hele dag fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 uur", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "24 uur fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dagen", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "2 dagen fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra dag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "Extra dag fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}]} |
| nl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/nl/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Heb ik ervaring nodig om een fiets te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, eerdere ervaring is niet nodig. We verhuren fietsen aan beginners en aan mensen die al zeker fietsen, en ons team kan je helpen een comfortabele fiets te kiezen om te starten."}}, {"@type": "Question", "name": "Zijn een helm of slot inbegrepen bij de huur?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar."}}, {"@type": "Question", "name": "Waar kan ik fietsen in de buurt van de winkel?", "acceptedAnswer": {"@type": "Answer", "text": "Onze winkel ligt dicht bij de boulevard, Port Olímpic, Torre MAPFRE en Casino Barcelona, in een gebied waar veel bezoekers een rustige route beginnen voordat ze parken en fietspaden in de buurt verkennen."}}, {"@type": "Question", "name": "Hebben jullie fietsen voor beginners of kinderen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. We kunnen je helpen een fiets te kiezen die past bij je lengte en niveau, inclusief fietsen die geschikt zijn voor kinderen."}}, {"@type": "Question", "name": "Heb ik een rijbewijs nodig om een fiets te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren."}}, {"@type": "Question", "name": "Kan ik mijn tas of bagage in de winkel achterlaten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. We bieden gratis opslag voor jassen, rugzakken en bagage in onze bewaakte winkel terwijl je fietst."}}, {"@type": "Question", "name": "Kan ik via WhatsApp reserveren of vragen stellen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen."}}, {"@type": "Question", "name": "Hoe reserveer ik of neem ik contact met jullie op?", "acceptedAnswer": {"@type": "Answer", "text": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen."}}], "inLanguage": "nl"} |
| nl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/nl/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/nl/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/nl/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/nl/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/nl/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/nl/quads/"}]} |
| nl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/bike/#webpage", "dateModified": "2026-08-24"} |
| nl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-3"}]} |
| nl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mijn vriend en ik huurden een paar skates en een fiets om over de boulevard te gaan en het was zo leuk! De eigenaren waren zo lief en behulpzaam en de prijs was geweldig! We zijn erg blij met deze plek en komen terug.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Super. Betaalbaar en goed gelegen; ik kreeg een gerepareerde fiets die geduldig genoeg was om dagelijks door de hele stad te rijden; zelfs de schoenen pasten!😁\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"We kwamen hier om fietsen te huren voor een rit langs het strandpad. Oscar was erg vriendelijk en direct. Snel en eenvoudig huurproces, zonder lange formulieren of verhalen. Goede, eerlijke prijs en je kunt op weg! Bedankt, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de 4 rodas, skateboard e longboard perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta. No aluguer de bicicletas estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "apoio ao cliente", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pt | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pt-PT", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/bike/#webpage", "url": "https://rentalscooterbarcelona.com/pt/bike/", "name": "Aluguer de bicicletas em Barcelona \| Bicicletas urbanas perto de Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "pt-PT", "description": "Aluga bicicletas em Barcelona perto de Port Olímpic e da praia da Barceloneta. A nossa loja local em Vila Olímpica oferece bicicletas urbanas confortáveis para adultos e crianças, capacete infantil e cadeado incluídos, cadeira infantil opcional, serviço gratuito de guarda de bagagem e dicas de rotas locais.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pt/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/pt/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pt/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": "https://rentalscooterbarcelona.com/pt/"}, {"@type": "ListItem", "position": 2, "name": "Aluguer de bicicletas", "item": "https://rentalscooterbarcelona.com/pt/bike/"}]} |
| pt | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de 4 rodas, skateboard e longboard perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta. No aluguer de bicicletas estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Cartão de crédito, cartão de débito, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "apoio ao cliente", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| pt | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pt/bike/#service", "name": "Aluguer de bicicletas em Barcelona", "serviceType": "Aluguer de bicicletas", "description": "O nosso serviço de aluguer de bicicletas em Barcelona, perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta, oferece bicicletas urbanas confortáveis para adultos e crianças. Em cada aluguer estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. Está disponível um serviço gratuito de guarda de bagagem, além de recomendações de rotas locais.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "1 hora de aluguer de bicicleta perto de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 horas", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "4 horas de aluguer de bicicleta perto de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia completo", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de dia completo em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 horas", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de 24 horas em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dias", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de 2 dias em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Dia extra de aluguer de bicicleta em Barcelona", "availability": "https://schema.org/InStock"}]} |
| pt | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pt/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Preciso de experiência para alugar uma bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "Não, não precisas de experiência anterior. Alugamos bicicletas a principiantes e a pessoas que já pedalam com confiança, e a nossa equipa pode ajudar-te a escolher uma bicicleta confortável para começar."}}, {"@type": "Question", "name": "O capacete ou o cadeado estão incluídos no aluguer?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional."}}, {"@type": "Question", "name": "Onde posso andar de bicicleta perto da loja?", "acceptedAnswer": {"@type": "Answer", "text": "A nossa loja fica perto do passeio marítimo, Port Olímpic, Torre MAPFRE e Casino Barcelona, numa zona de onde muitos visitantes começam um percurso tranquilo antes de explorar parques e ciclovias próximas."}}, {"@type": "Question", "name": "Têm bicicletas para principiantes ou para crianças?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Podemos ajudar-te a escolher uma bicicleta adequada à tua altura e ao teu nível, incluindo bicicletas apropriadas para crianças."}}, {"@type": "Question", "name": "Preciso de carta de condução para alugar uma bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido."}}, {"@type": "Question", "name": "Posso guardar a minha mala ou bagagem na loja?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas."}}, {"@type": "Question", "name": "Posso reservar ou fazer perguntas por WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha."}}, {"@type": "Question", "name": "Como reservo ou como vos contacto?", "acceptedAnswer": {"@type": "Answer", "text": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua."}}], "inLanguage": "pt-PT"} |
| pt | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pt/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/pt/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/pt/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/pt/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/pt/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/pt/quads/"}]} |
| pt | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/bike/#webpage", "dateModified": "2026-08-24"} |
| pt | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-3"}]} |
| pt | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Eu e o meu namorado alugámos um par de patins e uma bicicleta para percorrer o passeio marítimo e foi muito divertido! Os proprietários foram muito queridos e prestáveis e o preço foi ótimo! Ficámos muito satisfeitos com este sítio e vamos voltar.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excelente. Acessível e bem localizado; deram-me uma bicicleta reparada que foi suficientemente paciente para percorrer toda a cidade diariamente; até os sapatos combinaram!😁\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "João Junior"}, "datePublished": "2021-04-21", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta. Amb el lloguer de bicicletes s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "atenció al client", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| ca | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "ca"} |
| ca | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/bike/#webpage", "url": "https://rentalscooterbarcelona.com/cat/bike/", "name": "Lloguer de bicicletes a Barcelona \| Bicicletes urbanes a prop de Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "ca", "description": "Lloga bicicletes a Barcelona a prop de Port Olímpic i de la platja de la Barceloneta. La nostra botiga local a Vila Olímpica ofereix còmodes bicicletes urbanes per a adults i nens, casc infantil i cadenat inclosos, cadireta infantil opcional, servei gratuït de guarda d’equipatge i consells de rutes locals.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/cat/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/cat/bike/#faq"}], "dateModified": "2026-07-30"} |
| ca | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/cat/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inici", "item": "https://rentalscooterbarcelona.com/cat/"}, {"@type": "ListItem", "position": 2, "name": "Lloguer de bicicletes", "item": "https://rentalscooterbarcelona.com/cat/bike/"}]} |
| ca | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta. Amb el lloguer de bicicletes s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Targeta de crèdit, targeta de dèbit, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "atenció al client", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| ca | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/cat/bike/#service", "name": "Lloguer de bicicletes a Barcelona", "serviceType": "Lloguer de bicicletes", "description": "El nostre servei de lloguer de bicicletes a Barcelona, a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i de la platja de la Barceloneta, ofereix còmodes bicicletes urbanes per a adults i nens. Amb cada lloguer s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. Guarda d’equipatge gratuïta i recomanacions de rutes locals incloses.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "1 hora de lloguer de bicicleta a prop de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 hores", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "4 hores de lloguer de bicicleta a prop de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia complet", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de dia complet a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 hores", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de 24 hores a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dies", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de 2 dies a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Dia extra de lloguer de bicicleta a Barcelona", "availability": "https://schema.org/InStock"}], "url": "https://rentalscooterbarcelona.com/cat/bike/"} |
| ca | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/cat/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Necessito experiència per llogar una bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "No, no cal experiència prèvia. Lloguem bicicletes a principiants i a persones que ja pedalen amb confiança, i el nostre equip pot ajudar-te a triar una bicicleta còmoda per començar."}}, {"@type": "Question", "name": "S’inclou casc o cadenat amb el lloguer?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional."}}, {"@type": "Question", "name": "On puc anar amb bicicleta a prop de la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "La nostra botiga és a prop del passeig marítim, Port Olímpic, Torre MAPFRE i Casino Barcelona, en una zona des d’on molts visitants comencen una ruta tranquil·la abans d’explorar parcs i carrils bici propers."}}, {"@type": "Question", "name": "Teniu bicicletes per a principiants o per a nens?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens."}}, {"@type": "Question", "name": "Necessito carnet per llogar una bicicleta?", "acceptedAnswer": {"@type": "Answer", "text": "No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid."}}, {"@type": "Question", "name": "Puc guardar la meva bossa o equipatge a la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales."}}, {"@type": "Question", "name": "Puc reservar o fer preguntes per WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida."}}, {"@type": "Question", "name": "Com reservo o com us contacto?", "acceptedAnswer": {"@type": "Answer", "text": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar la disponibilitat de les bicicletes o el millor moment per recollir la teva."}}], "inLanguage": "ca"} |
| ca | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/cat/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/cat/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/cat/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/cat/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/cat/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/cat/quads/"}]} |
| ca | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/bike/#webpage", "dateModified": "2026-08-24"} |
| ca | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-3"}]} |
| ca | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"El meu xicot i jo vam llogar uns patins i una bicicleta per recórrer el passeig marítim i va ser molt divertit! Els propietaris van ser molt amables i servicials i el preu va ser fantàstic! Estem molt contents amb aquest lloc i hi tornarem.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marta"}, "datePublished": "2021-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ideal per llogar bicis i fer un passeig per la platja. Personal molt amable i molt bon preu.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Roex Info"}, "datePublished": "2018-12-28", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Es molt bona empressa de Lloguer de biciletes, el tracta es molt bó al igual que la qualitat del material que llogues. Recomanable 100% :)\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med uthyrning av scooter, inlines, cyklar, rullskridskor, skateboard och longboard nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden. Vid cykeluthyrning ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| sv | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "sv", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/bike/#webpage", "url": "https://rentalscooterbarcelona.com/sv/bike/", "name": "Cykeluthyrning i Barcelona \| Stadscyklar nära Port Olímpic \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "sv", "description": "Hyr cyklar i Barcelona mitt emot stranden och intill Port Olímpic. Vår lokala butik i Vila Olímpica erbjuder bekväma stadscyklar för vuxna och barn, barnhjälm och lås ingår, barnsits som tillval, gratis bagageförvaring och lokala ruttips.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/sv/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/sv/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/sv/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Hem", "item": "https://rentalscooterbarcelona.com/sv/"}, {"@type": "ListItem", "position": 2, "name": "Cykeluthyrning", "item": "https://rentalscooterbarcelona.com/sv/bike/"}]} |
| sv | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med uthyrning av scooter, inlines, cyklar, rullskridskor, skateboard och longboard nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden. Vid cykeluthyrning ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.", "image": ["https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kreditkort, betalkort, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"]} |
| sv | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/sv/bike/#service", "name": "Cykeluthyrning i Barcelona", "serviceType": "Cykeluthyrning", "description": "Vår cykeluthyrning i Barcelona, nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden, erbjuder bekväma stadscyklar för vuxna och barn. Barnhjälm och lås ingår vid varje hyra, och på vissa cyklar finns barnsits som tillval. Gratis bagageförvaring och lokala ruttips ingår.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 timme", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "1 timmes cykeluthyrning nära Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 timmar", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "4 timmars cykeluthyrning nära Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Heldag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "Heldagsuthyrning av cykel i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 timmar", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "24 timmars cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dagar", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "2 dagars cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra dag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "Extra dag cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}]} |
| sv | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/sv/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Behöver jag erfarenhet för att hyra en cykel?", "acceptedAnswer": {"@type": "Answer", "text": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med."}}, {"@type": "Question", "name": "Ingår hjälm eller lås i hyran?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval."}}, {"@type": "Question", "name": "Var kan jag cykla nära butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Vår butik ligger nära strandpromenaden, Port Olímpic, Torre MAPFRE och Casino Barcelona, i ett område där många besökare börjar en lugn tur innan de utforskar parker och närliggande cykelvägar."}}, {"@type": "Question", "name": "Har ni cyklar för nybörjare eller barn?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Vi kan hjälpa dig att välja en cykel som passar din längd och nivå, inklusive cyklar som passar barn."}}, {"@type": "Question", "name": "Behöver jag körkort för att hyra en cykel?", "acceptedAnswer": {"@type": "Answer", "text": "Nej. Inget körkort krävs för att hyra en cykel."}}, {"@type": "Question", "name": "Kan jag lämna min väska eller mitt bagage i butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Vi erbjuder gratis förvaring för jackor, ryggsäckar och bagage i vår övervakade butik medan du cyklar."}}, {"@type": "Question", "name": "Kan jag boka eller ställa frågor via WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid."}}, {"@type": "Question", "name": "Hur bokar jag eller kontaktar er?", "acceptedAnswer": {"@type": "Answer", "text": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel."}}], "inLanguage": "sv"} |
| sv | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/sv/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/sv/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/sv/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/sv/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/sv/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/sv/quads/"}]} |
| sv | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/bike/#webpage", "dateModified": "2026-08-24"} |
| sv | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-3"}]} |
| sv | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Min pojkvän och jag hyrde ett par rullskridskor och en cykel för att ta oss längs strandpromenaden, och det var så roligt! Ägarna var mycket vänliga och hjälpsamma och priset var toppen! Vi är mycket nöjda med stället och kommer tillbaka.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Jag hyrde en cykel här och blev verkligen mycket nöjd. Priserna är mycket bra jämfört med andra ställen och cyklarna är i gott skick. Dessutom är ägaren mycket trevlig och bemötandet var vänligt från första stund; hon förklarar allt lugnt och får dig att känna dig bekväm. Det är utan tvekan ett ställe jag rekommenderar om du behöver hyra en cykel enkelt och till ett bra pris. Jag skulle hyra här igen utan att tveka.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Jag gick hit för att hyra cyklar och cykla längs strandvägen. Oscar var mycket vänlig och saklig. Uthyrningen gick snabbt och enkelt, utan långa formulär eller genomgångar. Ett bra och rättvist pris, sedan är det bara att ge sig av! Tack, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/bike/#webpage", "url": "https://rentalscooterbarcelona.com/pl/bike/", "name": "Wynajem rowerów w Barcelonie \| Rowery miejskie przy Port Olímpic", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "pl", "description": "Wynajmij rowery w Barcelonie naprzeciwko plaży i obok Port Olímpic. Rowery miejskie dla dorosłych i dzieci, kask i zapięcie w cenie, opcjonalny fotelik dziecięcy i lokalne trasy.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-bike-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pl/bike/#service"}, {"@id": "https://rentalscooterbarcelona.com/pl/bike/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp rezerwacja", "target": "https://wa.me/34640559468"}} |
| pl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pl/bike/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://rentalscooterbarcelona.com/pl/"}, {"@type": "ListItem", "position": 2, "name": "Wynajem rowerów", "item": "https://rentalscooterbarcelona.com/pl/bike/"}]} |
| pl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Karta kredytowa, karta debetowa, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pl/bike/#service", "name": "Wynajem rowerów w Barcelonie", "serviceType": "Wynajem rowerów", "description": "Nasza usługa wynajmu rowerów w Barcelonie naprzeciwko plaży i obok Port Olímpic oferuje wygodne rowery miejskie dla dorosłych i dzieci. Kask dziecięcy i zapięcie są w cenie każdego wynajmu, opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach, a także zapewniamy darmowe przechowanie rzeczy i lokalne wskazówki tras.", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Zakres cen wynajmu rowerów", "priceCurrency": "EUR", "lowPrice": "4", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/pl/bike/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 godzina", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "1 godzina wynajem rowerów blisko Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 godziny", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "4 hour wynajem rowerów blisko Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Cały dzień", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Całodniowy wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 godziny", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "24 hour wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dni", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Dwudniowy wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dodatkowy dzień", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Dodatkowy dzień wynajmu rowerów w Barcelonie", "availability": "https://schema.org/InStock"}], "url": "https://rentalscooterbarcelona.com/pl/bike/"} |
| pl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pl/bike/#faq", "mainEntity": [{"@type": "Question", "name": "Czy potrzebuję doświadczenia, aby wynająć rower?", "acceptedAnswer": {"@type": "Answer", "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy rowery początkującym i pewnym siebie rowerzystom, a nasz zespół pomoże wybrać wygodny rower na start."}}, {"@type": "Question", "name": "Czy kask lub zapięcie są wliczone w wynajem?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach."}}, {"@type": "Question", "name": "Gdzie mogę jeździć rowerem blisko wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym zwiedzaniem parków i pobliskich ścieżek rowerowych."}}, {"@type": "Question", "name": "Czy macie rowery dla początkujących lub dzieci?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Pomożemy dobrać rower do Twojego wzrostu i poziomu doświadczenia, także rowery odpowiednie dla dzieci."}}, {"@type": "Question", "name": "Czy potrzebuję prawa jazdy, aby wynająć rower?", "acceptedAnswer": {"@type": "Answer", "text": "Nie. Do wynajmu roweru nie jest wymagane prawo jazdy."}}, {"@type": "Question", "name": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni."}}, {"@type": "Question", "name": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru."}}, {"@type": "Question", "name": "Jak mogę zarezerwować lub skontaktować się z wami?", "acceptedAnswer": {"@type": "Answer", "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność roweru albo najlepszą godzinę odbioru."}}], "inLanguage": "pl"} |
| pl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pl/bike/#itemlist", "itemListElement": [{"@type": "ListItem", "position": 1, "url": "https://rentalscooterbarcelona.com/pl/scooter/"}, {"@type": "ListItem", "position": 2, "url": "https://rentalscooterbarcelona.com/pl/bike/"}, {"@type": "ListItem", "position": 3, "url": "https://rentalscooterbarcelona.com/pl/rollerblades/"}, {"@type": "ListItem", "position": 4, "url": "https://rentalscooterbarcelona.com/pl/skateboard/"}, {"@type": "ListItem", "position": 5, "url": "https://rentalscooterbarcelona.com/pl/longboard/"}, {"@type": "ListItem", "position": 6, "url": "https://rentalscooterbarcelona.com/pl/quads/"}]} |
| pl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/bike/#webpage", "dateModified": "2026-08-24"} |
| pl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-3"}]} |
| pl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mój chłopak i ja wynajęliśmy parę rolek i rower, aby przejechać się promenadą, i świetnie się bawiliśmy! Właściciele byli bardzo mili i pomocni, a cena była świetna! Jesteśmy bardzo zadowoleni z tego miejsca i wrócimy.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Wynająłem tutaj rower i byłem naprawdę bardzo zadowolony. Ceny są bardzo dobre w porównaniu z innymi miejscami, a rowery są w dobrym stanie. Właścicielka jest bardzo sympatyczna i od pierwszej chwili traktuje klientów życzliwie; wszystko spokojnie wyjaśnia i sprawia, że czujesz się swobodnie. Zdecydowanie polecam to miejsce, jeśli potrzebujesz bezproblemowo wynająć rower w dobrej cenie. Bez wahania wynająłbym tutaj ponownie.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Przyszedłem tutaj wynająć rowery na przejażdżkę ścieżką przy plaży. Oscar był bardzo miły i konkretny. Wynajem przebiegł szybko i łatwo, bez długich formularzy ani przemówień. Dobra, uczciwa cena i można ruszać! Dziękuję, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}} |

## N. MATRIZ ARTICLE/BLOGPOSTING

No hay entidades Article/BlogPosting en estas páginas de servicio/contacto; no se exige un esquema editorial. Los elementos HTML article se cuentan por separado en U.

## O. MATRIZ GEO/COORDENADAS

| Idioma | Coordenadas extraídas | IDs de mapas | Sin coordenadas antiguas |
| --- | --- | --- | --- |
| en | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 80, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 324, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| es | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 77, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 321, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| fr | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 70, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 263, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| it | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 69, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 262, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| de | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 67, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 270, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| nl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 80, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 279, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pt | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 80, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 279, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| ca | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 69, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 262, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| sv | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 80, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 279, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 80, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 324, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |

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
| en | [{"line": 797, "text": "1 hour €4 Perfect for a short ride along the beach or trying a bike for the first time.", "price": 4.0}, {"line": 802, "text": "Most popular 4 hours €8 Ideal for a half‑day ride exploring the seafront, Port Olímpic and Ciutadella Park.", "price": 8.0}, {"line": 808, "text": "Full day €10 Enjoy a full day cycling around Barcelona's beaches and parks.", "price": 10.0}, {"line": 813, "text": "24 hours €12 Pick up today and return tomorrow to make the most of your time on two wheels.", "price": 12.0}, {"line": 818, "text": "2 days €20 Get more time to explore with a bike over two days.", "price": 20.0}, {"line": 823, "text": "Extra day €8 Extend your bike rental for another day at a reduced rate.", "price": 8.0}] | [{"line": 1032, "text": "1 hour €4", "price": 4.0}, {"line": 1036, "text": "4 hours €8", "price": 8.0}, {"line": 1040, "text": "Full day €10", "price": 10.0}, {"line": 1044, "text": "24 hours €12", "price": 12.0}, {"line": 1048, "text": "2 days €20", "price": 20.0}, {"line": 1052, "text": "Extra day €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hour", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "1 hour bike rental near Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 hours", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "4 hour bike rental near Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Full day", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "Full day bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 hours", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "24 hour bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 days", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "2 day bike rental in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra day", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/bike/", "description": "Extra day bike rental in Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 828, "text": "Included extras Bike gear &amp; extras Luggage storageFREE Child seat (selected bikes)€3 Helmet (children)FREE Bike lockFREE Quick local route tipsFREE Reserve by WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| es | [{"line": 791, "text": "1 hora €4 Perfecto para un paseo corto junto a la playa o para probar una bicicleta por primera vez.", "price": 4.0}, {"line": 796, "text": "Más popular 4 horas €8 Ideal para un recorrido de medio día explorando el paseo marítimo, Port Olímpic y el Parc de la Ciutadella.", "price": 8.0}, {"line": 802, "text": "Día completo €10 Disfruta de un día completo pedaleando por las playas y parques de Barcelona.", "price": 10.0}, {"line": 807, "text": "24 horas €12 Recógela hoy y devuélvela mañana para aprovechar al máximo tu tiempo sobre dos ruedas.", "price": 12.0}, {"line": 812, "text": "2 días €20 Gana más tiempo para explorar con una bicicleta durante dos días.", "price": 20.0}, {"line": 817, "text": "Día extra €8 Amplía tu alquiler de bicicleta un día más a una tarifa reducida.", "price": 8.0}] | [{"line": 1005, "text": "1 hora €4", "price": 4.0}, {"line": 1009, "text": "4 horas €8", "price": 8.0}, {"line": 1013, "text": "Día completo €10", "price": 10.0}, {"line": 1017, "text": "24 horas €12", "price": 12.0}, {"line": 1021, "text": "2 días €20", "price": 20.0}, {"line": 1025, "text": "Día extra €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "1 hora de alquiler de bicicleta cerca de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 horas", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "4 horas de alquiler de bicicleta cerca de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Día completo", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de día completo en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 horas", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de 24 horas en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 días", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Alquiler de bicicleta de 2 días en Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Día extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/es/bike/", "description": "Día extra de alquiler de bicicleta en Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 822, "text": "Extras incluidos Accesorios y extras de bicicleta Consigna para el equipajeGRATIS Silla infantil (bicicletas seleccionadas)€3 Casco infantilGRATIS Candado de bicicletaGRATIS Consejos rápidos de rutas localesGRATIS Reservar por WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| fr | [{"line": 720, "text": "1 heure €4 Parfait pour une courte balade le long de la plage ou pour essayer un vélo pour la première fois.", "price": 4.0}, {"line": 725, "text": "Le plus populaire 4 heures €8 Idéal pour une demi-journée à explorer la promenade du front de mer, Port Olímpic et le parc de la Ciutadella.", "price": 8.0}, {"line": 731, "text": "Journée complète €10 Profitez d’une journée complète à pédaler le long des plages et dans les parcs de Barcelone.", "price": 10.0}, {"line": 736, "text": "24 heures €12 Prenez-le aujourd’hui et rendez-le demain pour profiter au maximum de votre temps sur deux roues.", "price": 12.0}, {"line": 741, "text": "2 jours €20 Profitez de plus de temps pour explorer Barcelone à vélo pendant deux jours.", "price": 20.0}, {"line": 746, "text": "Jour supplémentaire €8 Prolongez votre location de vélo d’une journée supplémentaire à tarif réduit.", "price": 8.0}] | [{"line": 932, "text": "1 heure €4", "price": 4.0}, {"line": 936, "text": "4 heures €8", "price": 8.0}, {"line": 940, "text": "Journée complète €10", "price": 10.0}, {"line": 944, "text": "24 heures €12", "price": 12.0}, {"line": 948, "text": "2 jours €20", "price": 20.0}, {"line": 952, "text": "Jour supplémentaire €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 heure", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "1 heure de location de vélo près de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 heures", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "4 heures de location de vélo près de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Journée complète", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo à la journée à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 heures", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo 24 heures à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 jours", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Location de vélo 2 jours à Barcelone", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Jour supplémentaire", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/fr/bike/", "description": "Jour supplémentaire de location de vélo à Barcelone", "availability": "https://schema.org/InStock"}] | [{"line": 751, "text": "Extras inclus Équipement et extras des vélos Consigne pour bagagesGRATUIT Siège enfant (certains vélos)€3 Casque pour enfantGRATUIT Antivol de véloGRATUIT Conseils rapides d’itinéraires locauxGRATUIT Réserver sur WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| it | [{"line": 726, "text": "1 ora €4 Perfetto per un breve giro vicino alla spiaggia o per provare una bicicletta per la prima volta.", "price": 4.0}, {"line": 731, "text": "Più richiesto 4 ore €8 Ideale per un percorso di mezza giornata lungo il lungomare, Port Olímpic e il Parc de la Ciutadella.", "price": 8.0}, {"line": 737, "text": "Giornata intera €10 Goditi una giornata intera pedalando tra le spiagge e i parchi di Barcellona.", "price": 10.0}, {"line": 742, "text": "24 ore €12 Ritira oggi e restituisci domani per sfruttare al massimo il tuo tempo su due ruote.", "price": 12.0}, {"line": 747, "text": "2 giorni €20 Hai più tempo per esplorare Barcellona in bicicletta per due giorni.", "price": 20.0}, {"line": 752, "text": "Giorno extra €8 Prolunga il tuo noleggio bici di un giorno in più a una tariffa ridotta.", "price": 8.0}] | [{"line": 938, "text": "1 ora €4", "price": 4.0}, {"line": 942, "text": "4 ore €8", "price": 8.0}, {"line": 946, "text": "Giornata intera €10", "price": 10.0}, {"line": 950, "text": "24 ore €12", "price": 12.0}, {"line": 954, "text": "2 giorni €20", "price": 20.0}, {"line": 958, "text": "Giorno extra €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 ora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "1 ora di noleggio bici vicino a Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 ore", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "4 ore di noleggio bici vicino a Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Giornata intera", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici per una giornata intera a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 ore", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici 24 ore a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 giorni", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Noleggio bici per 2 giorni a Barcellona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Giorno extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/it/bike/", "description": "Giorno extra di noleggio bici a Barcellona", "availability": "https://schema.org/InStock"}] | [{"line": 757, "text": "Extra inclusi Attrezzatura ed extra delle biciclette Deposito bagagliGRATUITO Seggiolino bambino (alcune biciclette)€3 Casco bambinoGRATUITO Lucchetto biciGRATUITO Consigli rapidi su percorsi localiGRATUITO Prenota su WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| de | [{"line": 728, "text": "1 Stunde €4 Perfekt für eine kurze Fahrt am Strand oder um ein Fahrrad zum ersten Mal auszuprobieren.", "price": 4.0}, {"line": 733, "text": "Am beliebtesten 4 Stunden €8 Ideal für eine halbtägige Tour entlang der Strandpromenade, Port Olímpic und des Parc de la Ciutadella.", "price": 8.0}, {"line": 739, "text": "Ganzer Tag €10 Genieße einen ganzen Tag auf dem Rad entlang der Strände und Parks von Barcelona.", "price": 10.0}, {"line": 744, "text": "24 Stunden €12 Heute abholen und morgen zurückgeben, um deine Zeit auf zwei Rädern optimal zu nutzen.", "price": 12.0}, {"line": 749, "text": "2 Tage €20 Mehr Zeit, Barcelona zwei Tage lang mit dem Fahrrad zu erkunden.", "price": 20.0}, {"line": 754, "text": "Zusätzlicher Tag €8 Verlängere deine Fahrradmiete um einen weiteren Tag zu einem günstigeren Preis.", "price": 8.0}] | [{"line": 978, "text": "1 Stunde €4", "price": 4.0}, {"line": 982, "text": "4 Stunden €8", "price": 8.0}, {"line": 986, "text": "Ganzer Tag €10", "price": 10.0}, {"line": 990, "text": "24 Stunden €12", "price": 12.0}, {"line": 994, "text": "2 Tage €20", "price": 20.0}, {"line": 998, "text": "Zusatztag €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 Stunde", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "1 Stunde Fahrradverleih nahe Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 Stunden", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "4 Stunden Fahrradverleih nahe Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Ganzer Tag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "Ganztägiger Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 Stunden", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "24-Stunden-Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 Tage", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "2-Tage-Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Zusätzlicher Tag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/de/bike/", "description": "Zusätzlicher Tag Fahrradverleih in Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 759, "text": "Inklusive Extras Fahrrad-Zubehör und Extras GepäckaufbewahrungKOSTENLOS Kindersitz (ausgewählte Fahrräder)€3 KinderhelmKOSTENLOS FahrradschlossKOSTENLOS Schnelle lokale RoutentippsKOSTENLOS Per WhatsApp reservieren", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| nl | [{"line": 736, "text": "1 uur €4 Perfect voor een korte rit langs het strand of om voor het eerst een fiets uit te proberen.", "price": 4.0}, {"line": 741, "text": "Meest gekozen 4 uur €8 Ideaal voor een rit van een halve dag langs de boulevard, Port Olímpic en Parc de la Ciutadella.", "price": 8.0}, {"line": 747, "text": "Hele dag €10 Geniet een hele dag van fietsen langs de stranden en parken van Barcelona.", "price": 10.0}, {"line": 752, "text": "24 uur €12 Haal vandaag op en breng morgen terug om het meeste uit je tijd op twee wielen te halen.", "price": 12.0}, {"line": 757, "text": "2 dagen €20 Meer tijd om Barcelona twee dagen lang per fiets te verkennen.", "price": 20.0}, {"line": 762, "text": "Extra dag €8 Verleng je fietsverhuur met een extra dag tegen een lager tarief.", "price": 8.0}] | [{"line": 986, "text": "1 uur €4", "price": 4.0}, {"line": 990, "text": "4 uur €8", "price": 8.0}, {"line": 994, "text": "Hele dag €10", "price": 10.0}, {"line": 998, "text": "24 uur €12", "price": 12.0}, {"line": 1002, "text": "2 dagen €20", "price": 20.0}, {"line": 1006, "text": "Extra dag €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 uur", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "1 uur fietsverhuur vlak bij Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 uur", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "4 uur fietsverhuur vlak bij Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Hele dag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "Hele dag fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 uur", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "24 uur fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dagen", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "2 dagen fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra dag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/nl/bike/", "description": "Extra dag fietsverhuur in Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 767, "text": "Inbegrepen extra’s Fietsuitrusting en extra’s BagageopslagGRATIS Kinderzitje (geselecteerde fietsen)€3 KinderhelmGRATIS FietsslotGRATIS Snelle lokale routetipsGRATIS Reserveren via WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| pt | [{"line": 742, "text": "1 hora €4 Perfeito para um passeio curto junto à praia ou para experimentar uma bicicleta pela primeira vez.", "price": 4.0}, {"line": 747, "text": "Mais popular 4 horas €8 Ideal para um percurso de meio dia explorando o passeio marítimo, Port Olímpic e o Parc de la Ciutadella.", "price": 8.0}, {"line": 753, "text": "Dia completo €10 Desfruta de um dia completo a pedalar pelas praias e parques de Barcelona.", "price": 10.0}, {"line": 758, "text": "24 horas €12 Leva hoje e devolve amanhã para aproveitares ao máximo o teu tempo sobre duas rodas.", "price": 12.0}, {"line": 763, "text": "2 dias €20 Ganha mais tempo para explorar Barcelona de bicicleta durante dois dias.", "price": 20.0}, {"line": 768, "text": "Dia extra €8 Prolonga o teu aluguer de bicicleta por mais um dia a um preço reduzido.", "price": 8.0}] | [{"line": 974, "text": "1 hora €4", "price": 4.0}, {"line": 978, "text": "4 horas €8", "price": 8.0}, {"line": 982, "text": "Dia completo €10", "price": 10.0}, {"line": 986, "text": "24 horas €12", "price": 12.0}, {"line": 990, "text": "2 dias €20", "price": 20.0}, {"line": 994, "text": "Dia extra €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "1 hora de aluguer de bicicleta perto de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 horas", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "4 horas de aluguer de bicicleta perto de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia completo", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de dia completo em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 horas", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de 24 horas em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dias", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Aluguer de bicicleta de 2 dias em Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pt/bike/", "description": "Dia extra de aluguer de bicicleta em Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 773, "text": "Extras incluídos Equipamento e extras das bicicletas Guarda de bagagemGRÁTIS Cadeira infantil (bicicletas selecionadas)€3 Capacete infantilGRÁTIS Cadeado de bicicletaGRÁTIS Dicas rápidas de rotas locaisGRÁTIS Reservar por WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| ca | [{"line": 726, "text": "1 hora €4 Perfecte per a una passejada curta al costat de la platja o per provar una bicicleta per primera vegada.", "price": 4.0}, {"line": 731, "text": "Més popular 4 hores €8 Ideal per a un recorregut de mig dia explorant el passeig marítim, Port Olímpic i el Parc de la Ciutadella.", "price": 8.0}, {"line": 737, "text": "Dia complet €10 Gaudeix d’un dia complet pedalant per les platges i parcs de Barcelona.", "price": 10.0}, {"line": 742, "text": "24 hores €12 Recull-la avui i torna-la demà per aprofitar al màxim el teu temps sobre dues rodes.", "price": 12.0}, {"line": 747, "text": "2 dies €20 Guanya més temps per explorar Barcelona amb bicicleta durant dos dies.", "price": 20.0}, {"line": 752, "text": "Dia extra €8 Amplia el teu lloguer de bicicleta un dia més a un preu reduït.", "price": 8.0}] | [{"line": 959, "text": "1 hora €4", "price": 4.0}, {"line": 963, "text": "4 hores €8", "price": 8.0}, {"line": 967, "text": "Dia complet €10", "price": 10.0}, {"line": 971, "text": "24 hores €12", "price": 12.0}, {"line": 975, "text": "2 dies €20", "price": 20.0}, {"line": 979, "text": "Dia extra €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 hora", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "1 hora de lloguer de bicicleta a prop de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 hores", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "4 hores de lloguer de bicicleta a prop de Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia complet", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de dia complet a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 hores", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de 24 hores a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dies", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Lloguer de bicicleta de 2 dies a Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dia extra", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/cat/bike/", "description": "Dia extra de lloguer de bicicleta a Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 757, "text": "Extres inclosos Equipament i extres de bicicletes Guarda d’equipatgeGRATUÏT Cadireta infantil (bicicletes seleccionades)€3 Casc infantilGRATUÏT Cadenat de bicicletaGRATUÏT Consells ràpids de rutes localsGRATUÏT Reservar per WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| sv | [{"line": 738, "text": "1 timme €4 Perfekt för en kort tur längs stranden eller för att prova en cykel för första gången.", "price": 4.0}, {"line": 743, "text": "Mest populär 4 timmar €8 Perfekt för en halvdagstur längs strandpromenaden, Port Olímpic och Parc de la Ciutadella.", "price": 8.0}, {"line": 749, "text": "Heldag €10 Njut av en heldag på cykel längs Barcelonas stränder och parker.", "price": 10.0}, {"line": 754, "text": "24 timmar €12 Hämta idag och lämna tillbaka imorgon för att få ut så mycket som möjligt av din tid på två hjul.", "price": 12.0}, {"line": 759, "text": "2 dagar €20 Få mer tid att utforska Barcelona med cykel i två dagar.", "price": 20.0}, {"line": 764, "text": "Extra dag €8 Förläng din cykelhyra med en extra dag till ett lägre pris.", "price": 8.0}] | [{"line": 972, "text": "1 timme €4", "price": 4.0}, {"line": 976, "text": "4 timmar €8", "price": 8.0}, {"line": 980, "text": "Heldag €10", "price": 10.0}, {"line": 984, "text": "24 timmar €12", "price": 12.0}, {"line": 988, "text": "2 dagar €20", "price": 20.0}, {"line": 992, "text": "Extra dag €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 timme", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "1 timmes cykeluthyrning nära Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 timmar", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "4 timmars cykeluthyrning nära Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Heldag", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "Heldagsuthyrning av cykel i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 timmar", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "24 timmars cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dagar", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "2 dagars cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Extra dag", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/sv/bike/", "description": "Extra dag cykeluthyrning i Barcelona", "availability": "https://schema.org/InStock"}] | [{"line": 769, "text": "Extra som ingår Cykelutrustning och extra BagageförvaringGRATIS Barnsits (utvalda cyklar)€3 BarnhjälmGRATIS CykellåsGRATIS Snabba lokala ruttipsGRATIS Boka via WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |
| pl | [{"line": 797, "text": "1 godzina €4 Idealne na krótką przejażdżkę wzdłuż plaży lub pierwszą próbę jazdy rowerem.", "price": 4.0}, {"line": 802, "text": "Najpopularniejsze 4 godziny €8 Idealne na półdniową przejażdżkę nad morzem, przy Port Olímpic i w parku Ciutadella.", "price": 8.0}, {"line": 808, "text": "Cały dzień €10 Ciesz się całym dniem jazdy rowerem po plażach i parkach Barcelony.", "price": 10.0}, {"line": 813, "text": "24 godziny €12 Odbierz rower dziś i zwróć jutro, aby lepiej wykorzystać czas na dwóch kółkach.", "price": 12.0}, {"line": 818, "text": "2 dni €20 Zyskaj więcej czasu na zwiedzanie przez dwa dni na rowerze.", "price": 20.0}, {"line": 823, "text": "Dodatkowy dzień €8 Przedłuż wynajem roweru o kolejny dzień w niższej cenie.", "price": 8.0}] | [{"line": 1031, "text": "1 godzina €4", "price": 4.0}, {"line": 1035, "text": "4 godziny €8", "price": 8.0}, {"line": 1039, "text": "Cały dzień €10", "price": 10.0}, {"line": 1043, "text": "24 godziny €12", "price": 12.0}, {"line": 1047, "text": "2 dni €20", "price": 20.0}, {"line": 1051, "text": "Dodatkowy dzień €8", "price": 8.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "1 godzina", "price": "4", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "1 godzina wynajem rowerów blisko Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "4 godziny", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "4 hour wynajem rowerów blisko Port Olímpic", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Cały dzień", "price": "10", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Całodniowy wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "24 godziny", "price": "12", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "24 hour wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "2 dni", "price": "20", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Dwudniowy wynajem rowerów w Barcelonie", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Dodatkowy dzień", "price": "8", "priceCurrency": "EUR", "url": "https://rentalscooterbarcelona.com/pl/bike/", "description": "Dodatkowy dzień wynajmu rowerów w Barcelonie", "availability": "https://schema.org/InStock"}] | [{"line": 828, "text": "Dodatki w cenie Sprzęt i dodatki do rowerów Przechowanie bagażuDARMOWO Fotelik dziecięcy (wybrane rowery)€3 Kask (dzieci)DARMOWO Zapięcie roweroweDARMOWO Szybkie lokalne wskazówki trasDARMOWO Zarezerwuj przez WhatsApp", "price": 3.0}] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "expected": [4.0, 8.0, 10.0, 12.0, 20.0, 8.0], "pass": true}] |

| Idioma | Ofertas servicio | Ofertas PRICES | Coinciden tarifas base |
| --- | --- | --- | --- |
| en | [["1 hour", 4.0], ["4 hours", 8.0], ["Full day", 10.0], ["24 hours", 12.0], ["2 days", 20.0], ["Extra day", 8.0]] | [["1 hour", 4.0], ["4 hours", 8.0], ["Full day", 10.0], ["24 hours", 12.0], ["2 days", 20.0], ["Extra day", 8.0], ["Child seat (selected bikes)", 3.0], ["1-hour bike rental in Barcelona", 4.0]] | True |
| es | [["1 hora", 4.0], ["4 horas", 8.0], ["Día completo", 10.0], ["24 horas", 12.0], ["2 días", 20.0], ["Día extra", 8.0]] | [["1 hora", 4.0], ["4 horas", 8.0], ["Día completo", 10.0], ["24 horas", 12.0], ["2 días", 20.0], ["Día extra", 8.0], ["Silla infantil (bicicletas seleccionadas)", 3.0], ["Alquiler de bicicletas 1 hora en Barcelona", 4.0]] | True |
| fr | [["1 heure", 4.0], ["4 heures", 8.0], ["Journée complète", 10.0], ["24 heures", 12.0], ["2 jours", 20.0], ["Jour supplémentaire", 8.0]] | [["1 heure", 4.0], ["4 heures", 8.0], ["Journée complète", 10.0], ["24 heures", 12.0], ["2 jours", 20.0], ["Jour supplémentaire", 8.0], ["Siège enfant (certains vélos)", 3.0], ["Location de vélo 1 heure à Barcelone", 4.0]] | True |
| it | [["1 ora", 4.0], ["4 ore", 8.0], ["Giornata intera", 10.0], ["24 ore", 12.0], ["2 giorni", 20.0], ["Giorno extra", 8.0]] | [["1 ora", 4.0], ["4 ore", 8.0], ["Giornata intera", 10.0], ["24 ore", 12.0], ["2 giorni", 20.0], ["Giorno extra", 8.0], ["Seggiolino bambino (alcune biciclette)", 3.0], ["Noleggio bicicletta 1 ora a Barcellona", 4.0]] | True |
| de | [["1 Stunde", 4.0], ["4 Stunden", 8.0], ["Ganzer Tag", 10.0], ["24 Stunden", 12.0], ["2 Tage", 20.0], ["Zusätzlicher Tag", 8.0]] | [["1 Stunde", 4.0], ["4 Stunden", 8.0], ["Ganzer Tag", 10.0], ["24 Stunden", 12.0], ["2 Tage", 20.0], ["Zusätzlicher Tag", 8.0], ["Kindersitz (ausgewählte Fahrräder)", 3.0], ["Fahrrad mieten – 1 Stunde in Barcelona", 4.0]] | True |
| nl | [["1 uur", 4.0], ["4 uur", 8.0], ["Hele dag", 10.0], ["24 uur", 12.0], ["2 dagen", 20.0], ["Extra dag", 8.0]] | [["1 uur", 4.0], ["4 uur", 8.0], ["Hele dag", 10.0], ["24 uur", 12.0], ["2 dagen", 20.0], ["Extra dag", 8.0], ["Kinderzitje (geselecteerde fietsen)", 3.0], ["Fiets huren voor 1 uur in Barcelona", 4.0]] | True |
| pt | [["1 hora", 4.0], ["4 horas", 8.0], ["Dia completo", 10.0], ["24 horas", 12.0], ["2 dias", 20.0], ["Dia extra", 8.0]] | [["1 hora", 4.0], ["4 horas", 8.0], ["Dia completo", 10.0], ["24 horas", 12.0], ["2 dias", 20.0], ["Dia extra", 8.0], ["Cadeira para criança (bicicletas selecionadas)", 3.0], ["Aluguer de bicicleta por 1 hora em Barcelona", 4.0]] | True |
| ca | [["1 hora", 4.0], ["4 hores", 8.0], ["Dia complet", 10.0], ["24 hores", 12.0], ["2 dies", 20.0], ["Dia extra", 8.0]] | [["1 hora", 4.0], ["4 hores", 8.0], ["Dia complet", 10.0], ["24 hores", 12.0], ["2 dies", 20.0], ["Dia extra", 8.0], ["Cadireta infantil (bicicletes seleccionades)", 3.0], ["Lloguer de bicicleta 1 hora a Barcelona", 4.0]] | True |
| sv | [["1 timme", 4.0], ["4 timmar", 8.0], ["Heldag", 10.0], ["24 timmar", 12.0], ["2 dagar", 20.0], ["Extra dag", 8.0]] | [["1 timme", 4.0], ["4 timmar", 8.0], ["Heldag", 10.0], ["24 timmar", 12.0], ["2 dagar", 20.0], ["Extra dag", 8.0], ["Barnstol (utvalda cyklar)", 3.0], ["Cykeluthyrning 1 timme i Barcelona", 4.0]] | True |
| pl | [["1 godzina", 4.0], ["4 godziny", 8.0], ["Cały dzień", 10.0], ["24 godziny", 12.0], ["2 dni", 20.0], ["Dodatkowy dzień", 8.0]] | [["1 godzina", 4.0], ["4 godziny", 8.0], ["Cały dzień", 10.0], ["24 godziny", 12.0], ["2 dni", 20.0], ["Dodatkowy dzień", 8.0], ["Fotelik dziecięcy (wybrane rowery)", 3.0], ["Godzinny wynajem rowerów w Barcelonie", 4.0]] | True |

El asiento infantil de BIKE (3 EUR) es un extra y no una séptima duración. CONTACT no contiene tarifas: no aplicable.

## R. MATRIZ POLÍTICAS

Textos completos extraídos por idioma: equipamiento, documentos, depósito, reservas, tallas y condiciones. Ausencia de una mención no equivale a contradicción. El alcance es coherencia del HTML con CANONICAL, no validación legal ni de disponibilidad.

| Idioma | Línea | Texto |
| --- | --- | --- |
| en | 745 | Rent bikes from our local shop in Vila Olímpica del Poblenou, near Barceloneta Beach and Port Olímpic. Comfortable city bikes for adults and kids, children's helmet and lock included, optional child seat available on selected bikes. Free luggage storage and local route tips. |
| en | 776 | Comfortable bikes for city rides |
| en | 777 | Choose from comfortable city bikes prepared for relaxed rides along the seafront and through the city. We have options for adults and kids so everyone can enjoy the ride. |
| en | 781 | A children's helmet and a lock are included with every rental, and an optional child seat is available on selected bikes. |
| en | 785 | Start riding just steps from Barceloneta Beach and Port Olímpic. Explore the seafront promenade, bike‑friendly parks and nearby cycle lanes without long transfers. |
| en | 794 | These are the current public prices for our bike rental service. You can also compare all rates on our Prices page, and contact us on WhatsApp to confirm availability before visiting. |
| en | 800 | Perfect for a short ride along the beach or trying a bike for the first time. |
| en | 806 | Ideal for a half‑day ride exploring the seafront, Port Olímpic and Ciutadella Park. |
| en | 850 | Children's helmet and lock included with every bike rental |
| en | 888 | RSB is a local rental shop in Carrer de Salvador Espriu, close to Vila Olímpica del Poblenou, Barceloneta Beach and Port Olímpic. It is a practical starting point for riding the seafront, reaching Ciutadella Park and using nearby cycle lanes around central Barcelona. |
| en | 893 | Open every day: 10:30–13:30 and 16:30–20:00. We offer hourly, full‑day and multi‑day bike rentals with flexible return times. A children's helmet and a bike lock are included with every rental, and an optional child seat is available on selected bikes. Our local team can help you choose the right size, explain the basics and recommend suitable beach, park and city routes. For local route ideas and practical tips, you can read our bike rental guide in Barcelona. |
| en | 976 | No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started. |
| en | 979 | Is a helmet or lock included with the rental? |
| en | 980 | Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes. |
| en | 983 | Where can I ride a bike near the shop? |
| en | 984 | Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby. |
| en | 987 | Do you have bikes for beginners or kids? |
| en | 988 | Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids. |
| en | 991 | Do I need a licence to rent a bike? |
| en | 992 | No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID. |
| en | 996 | Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride. |
| en | 1013 | More Barcelona rentals and local guides |
| en | 1014 | Discover related rental services from our shop in Vila Olímpica del Poblenou and browse local guides across the main activities we offer in Barcelona. |
| en | 1061 | Children's helmet and lock included · Optional child seat (€3) · Help choosing the right bike · Storage for jackets, backpacks and luggage. |
| es | 739 | Alquila bicicletas en nuestra tienda local de Vila Olímpica del Poblenou, cerca de Torre MAPFRE, Port Olímpic, Casino Barcelona y la playa de la Barceloneta. Cómodas bicicletas urbanas para adultos y niños, casco infantil y candado incluidos, y silla infantil opcional en algunas bicicletas. Consigna gratuita para el equipaje y consejos de rutas locales. |
| es | 771 | Elige entre cómodas bicicletas urbanas preparadas para paseos tranquilos por el paseo marítimo y por la ciudad. Tenemos opciones para adultos y niños para que todos disfruten del recorrido. |
| es | 774 | Todo incluido |
| es | 775 | Con cada alquiler se incluyen casco infantil y candado, y en algunas bicicletas hay silla infantil opcional. |
| es | 788 | Estos son los precios públicos actuales de nuestro servicio de alquiler de bicicletas. También puedes comparar todas las tarifas en nuestra página de precios, y contactarnos por WhatsApp para confirmar disponibilidad antes de venir. |
| es | 800 | Ideal para un recorrido de medio día explorando el paseo marítimo, Port Olímpic y el Parc de la Ciutadella. |
| es | 820 | Amplía tu alquiler de bicicleta un día más a una tarifa reducida. |
| es | 844 | Casco infantil y candado incluidos con cada alquiler de bicicleta |
| es | 846 | Ayuda para elegir la bicicleta adecuada según tu altura y necesidades |
| es | 847 | Ayuda de nuestro equipo local en la recogida |
| es | 882 | RSB es una tienda local de alquiler en Carrer de Salvador Espriu, cerca de Vila Olímpica, la playa de la Barceloneta, Torre MAPFRE, Casino Barcelona y Port Olímpic. Es un punto de partida práctico para recorrer el paseo marítimo, llegar al Parc de la Ciutadella y usar los carriles bici cercanos del centro de Barcelona. |
| es | 887 | Abierto todos los días: 10:30–13:30 y 16:30–20:00. Ofrecemos alquileres de bicicletas por horas, día completo y varios días. Se incluye un casco infantil y un candado con cada alquiler, y hay sillita infantil opcional en bicicletas seleccionadas. Nuestro equipo local puede ayudarte a elegir la talla adecuada, explicarte lo básico y recomendarte rutas por la playa, parques y ciudad. Para ideas de rutas y consejos prácticos, puedes leer nuestra guía de alquiler de bicicletas en Barcelona. |
| es | 952 | ¿Se incluye casco o candado con el alquiler? |
| es | 953 | Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional. |
| es | 961 | Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños. |
| es | 964 | ¿Necesito licencia para alquilar una bicicleta? |
| es | 965 | No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido. |
| es | 968 | ¿Puedo guardar mi bolsa o equipaje en la tienda? |
| es | 973 | Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida. |
| es | 977 | Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya. |
| es | 987 | Descubre servicios de alquiler relacionados desde nuestra tienda de Vila Olímpica del Poblenou y consulta guías locales sobre las principales actividades que ofrecemos en Barcelona. |
| es | 1002 | Precios del alquiler de bicicletas y accesorios incluidos |
| es | 1034 | Casco infantil y candado incluidos · Silla infantil opcional (€3) · Ayuda para elegir la bicicleta adecuada · Consigna para chaquetas, mochilas y equipaje. |
| es | 1044 | Consulta disponibilidad para tu alquiler de bicicletas en Barcelona |
| fr | 668 | Louez des vélos dans notre boutique locale à Vila Olímpica del Poblenou, près de Torre MAPFRE, Port Olímpic, Casino Barcelona et de la plage de la Barceloneta. Vélos urbains confortables pour adultes et enfants, casque pour enfant et antivol inclus, siège enfant en option sur certains vélos. Consigne gratuite pour les bagages et conseils d’itinéraires locaux. |
| fr | 704 | Chaque location inclut un casque pour enfant et un antivol, et un siège enfant en option est disponible sur certains vélos. |
| fr | 717 | Voici les tarifs publics actuels de notre service de location de vélos. Vous pouvez aussi comparer tous les prix sur notre page de tarifs, et nous contacter sur WhatsApp pour confirmer la disponibilité avant de venir. |
| fr | 729 | Idéal pour une demi-journée à explorer la promenade du front de mer, Port Olímpic et le parc de la Ciutadella. |
| fr | 773 | Casque pour enfant et antivol inclus avec chaque location de vélo |
| fr | 775 | Aide pour choisir le vélo adapté à votre taille et à vos besoins |
| fr | 816 | Ouvert tous les jours : 10:30–13:30 et 16:30–20:00. Nous proposons des locations de vélos à l’heure, à la journée complète et sur plusieurs jours.Chaque location inclut un casque pour enfant et un antivol, et un siège enfant en option est disponible sur certains vélos. Notre équipe locale peut vous aider à choisir la bonne taille, expliquer l’essentiel et recommander des itinéraires adaptés entre plage, parcs et ville. Pour des idées d’itinéraires et des conseils pratiques, vous pouvez lire notre guide de location de vélos à Barcelone. |
| fr | 847 | Notre boutique se trouve à Vila Olímpica, près de la plage de la Barceloneta, de Torre MAPFRE, de Casino Barcelona et de Port Olímpic. Elle est idéalement située pour récupérer un vélo et partir directement vers la promenade du front de mer, le parc de la Ciutadella ou les pistes cyclables voisines de Barcelone. |
| fr | 849 | Notre boutique se trouve à Vila Olímpica, près de la plage de la Barceloneta, de Torre MAPFRE, de Casino Barcelona et de Port Olímpic. Elle est idéalement située pour récupérer un vélo et partir directement vers la promenade du front de mer, le parc de la Ciutadella ou les pistes cyclables voisines de Barcelone. |
| fr | 876 | Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer. |
| fr | 879 | Le casque ou l’antivol sont-ils inclus avec la location ? |
| fr | 880 | Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos. |
| fr | 888 | Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants. |
| fr | 891 | Ai-je besoin d’un permis pour louer un vélo ? |
| fr | 892 | Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un. |
| fr | 912 | Découvrez des services de location liés depuis notre boutique de Vila Olímpica del Poblenou et consultez des guides locaux sur les principales activités que nous proposons à Barcelone. |
| fr | 913 | Plus de locations à Barcelone et guides locaux |
| fr | 914 | Découvrez des services de location liés depuis notre boutique de Vila Olímpica del Poblenou et consultez nos guides locaux sur les principales activités que nous proposons à Barcelone. |
| fr | 961 | Casque, antivol et consigne bagages · Casque pour enfant et antivol inclus · Siège enfant en option (€3) · Aide pour choisir le vélo adapté · Consigne pour vestes, sacs à dos et bagages. |
| fr | 972 | Écrivez-nous sur WhatsApp ou passez dans notre boutique de Vila Olímpica pour organiser votre location de vélos près de la plage de la Barceloneta. Notre équipe vous aidera à choisir le vélo adapté et vous recommandera des itinéraires faciles le long de la côte, dans les parcs et en ville. |
| it | 674 | Noleggia biciclette nel nostro negozio locale a Vila Olímpica del Poblenou, vicino a Torre MAPFRE, Port Olímpic, Casino Barcelona e alla spiaggia della Barceloneta. Comode biciclette urbane per adulti e bambini, casco bambino e lucchetto inclusi, seggiolino opzionale su alcune biciclette. Deposito bagagli gratuito e consigli sui percorsi locali. |
| it | 675 | Il noleggio bici riguarda biciclette city standard; non noleggiamo e-bike né biciclette elettriche. Area di servizio: Barcellona. Valutazione 4,6/5 basata su 226 recensioni Google. |
| it | 710 | Con ogni noleggio sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. |
| it | 723 | Questi sono i prezzi pubblici attuali del nostro servizio di noleggio biciclette. Puoi anche confrontare tutte le tariffe nella nostra pagina dei prezzi e contattarci su WhatsApp per confermare la disponibilità prima di venire. |
| it | 735 | Ideale per un percorso di mezza giornata lungo il lungomare, Port Olímpic e il Parc de la Ciutadella. |
| it | 755 | Prolunga il tuo noleggio bici di un giorno in più a una tariffa ridotta. |
| it | 779 | Casco bambino e lucchetto inclusi con ogni noleggio bici |
| it | 784 | Deposito gratuito per giacche, zaini e bagagli nel nostro negozio sorvegliato |
| it | 822 | Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00. Offriamo noleggi di biciclette a ore, per giornata intera e per più giorni.Con ogni noleggio sono inclusi casco bambino e lucchetto, e su alcune biciclette è disponibile un seggiolino opzionale. Il nostro team locale può aiutarti a scegliere la misura giusta, spiegarti le basi e consigliarti percorsi adatti tra spiaggia, parchi e città. Per idee di percorsi e consigli pratici, puoi leggere la nostra guida al noleggio biciclette a Barcellona. |
| it | 853 | Il nostro negozio si trova a Vila Olímpica, vicino alla spiaggia della Barceloneta, Torre MAPFRE, Casino Barcelona e Port Olímpic. È in una posizione ideale per ritirare una bicicletta e partire direttamente verso il lungomare, il Parc de la Ciutadella o le piste ciclabili vicine di Barcellona. |
| it | 855 | Il nostro negozio si trova a Vila Olímpica, vicino alla spiaggia della Barceloneta, Torre MAPFRE, Casino Barcelona e Port Olímpic. È in una posizione ideale per ritirare una bicicletta e partire direttamente verso il lungomare, il Parc de la Ciutadella o le piste ciclabili vicine di Barcellona. |
| it | 885 | Il casco o il lucchetto sono inclusi nel noleggio? |
| it | 886 | Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale. |
| it | 898 | No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido. |
| it | 902 | Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali. |
| it | 918 | Scopri servizi di noleggio correlati dal nostro negozio di Vila Olímpica del Poblenou e consulta guide locali sulle principali attività che offriamo a Barcellona. |
| it | 919 | Altri noleggi a Barcellona e guide locali |
| it | 920 | Scopri i servizi di noleggio correlati dal nostro negozio di Vila Olímpica del Poblenou e consulta le guide locali sulle principali attività che offriamo a Barcellona. |
| it | 967 | Casco, lucchetto e deposito bagagli · Casco bambino e lucchetto inclusi · Seggiolino opzionale (€3) · Aiuto per scegliere la bicicletta giusta · Deposito per giacche, zaini e bagagli. |
| de | 676 | Miete Fahrräder in unserem lokalen Shop in Vila Olímpica del Poblenou, nahe Torre MAPFRE, Port Olímpic, Casino Barcelona und dem Strand Barceloneta. Bequeme Citybikes für Erwachsene und Kinder, Kinderhelm und Schloss inklusive, optionaler Kindersitz bei ausgewählten Fahrrädern. Kostenlose Gepäckaufbewahrung und lokale Routentipps. |
| de | 712 | Bei jeder Miete sind ein Kinderhelm und ein Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. |
| de | 737 | Ideal für eine halbtägige Tour entlang der Strandpromenade, Port Olímpic und des Parc de la Ciutadella. |
| de | 781 | Kinderhelm und Schloss bei jeder Fahrradmiete inklusive |
| de | 783 | Hilfe bei der Wahl des passenden Fahrrads für deine Größe und Bedürfnisse |
| de | 825 | Geöffnet von 10:30–13:30 und 16:30–20:00 Uhr. Wir bieten Fahrradmieten stundenweise, für einen ganzen Tag und für mehrere Tage an.Bei jeder Miete sind ein Kinderhelm und ein Schloss inbegriffen, und bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. Unser lokales Team hilft dir, die richtige Größe zu wählen, das Wichtigste zu erklären und geeignete Routen durch Strand, Parks und Stadt zu empfehlen. Für Routenideen und praktische Tipps kannst du unseren Fahrradverleih-Guide für Barcelona lesen. |
| de | 876 | Unser Shop befindet sich in Vila Olímpica, nahe dem Strand der Barceloneta, Torre MAPFRE, Casino Barcelona und Port Olímpic. Er liegt ideal, um ein Fahrrad abzuholen und direkt zur Strandpromenade, zum Parc de la Ciutadella oder zu den nahegelegenen Radwegen in Barcelona aufzubrechen. |
| de | 878 | Unser Shop befindet sich in Vila Olímpica, nahe dem Strand der Barceloneta, Torre MAPFRE, Casino Barcelona und Port Olímpic. Er liegt ideal, um ein Fahrrad abzuholen und direkt zur Strandpromenade, zum Parc de la Ciutadella oder zu den nahegelegenen Radwegen in Barcelona aufzubrechen. |
| de | 910 | Sind Helm oder Schloss in der Miete enthalten? |
| de | 913 | Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar. |
| de | 925 | Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder. |
| de | 928 | Brauche ich einen Führerschein, um ein Fahrrad zu mieten? |
| de | 931 | Nein. Für die Fahrradmiete ist kein Führerschein erforderlich. |
| de | 958 | Entdecke verwandte Verleihservices aus unserem Shop in Vila Olímpica del Poblenou und stöbere in lokalen Guides zu den wichtigsten Aktivitäten, die wir in Barcelona anbieten. |
| de | 959 | Mehr Verleih in Barcelona und lokale Guides |
| de | 960 | Entdecke verwandte Mietservices aus unserem Geschäft in Vila Olímpica del Poblenou und lies lokale Guides zu den wichtigsten Aktivitäten, die wir in Barcelona anbieten. |
| de | 1007 | Helm, Schloss und Gepäckaufbewahrung · Kinderhelm und Schloss inklusive · Optionaler Kindersitz (€3) · Hilfe bei der Wahl des passenden Fahrrads · Aufbewahrung für Jacken, Rucksäcke und Gepäck. |
| nl | 684 | Huur fietsen in onze lokale winkel in Vila Olímpica del Poblenou, vlak bij Torre MAPFRE, Port Olímpic, Casino Barcelona en het strand van Barceloneta. Comfortabele stadsfietsen voor volwassenen en kinderen, kinderhelm en slot inbegrepen, optioneel kinderzitje op geselecteerde fietsen. Gratis bagageopslag en lokale routetips. |
| nl | 720 | Bij elke huur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. |
| nl | 733 | Dit zijn de actuele openbare prijzen van onze fietsverhuur. Je kunt ook alle tarieven vergelijken op onze prijzenpagina en via WhatsApp contact met ons opnemen om de beschikbaarheid te bevestigen voordat je langskomt. |
| nl | 745 | Ideaal voor een rit van een halve dag langs de boulevard, Port Olímpic en Parc de la Ciutadella. |
| nl | 789 | Kinderhelm en slot inbegrepen bij elke fietsverhuur |
| nl | 833 | Elke dag geopend: 10:30–13:30 en 16:30–20:00. We bieden fietsverhuur per uur, voor een hele dag en voor meerdere dagen.Bij elke huur zijn een kinderhelm en een slot inbegrepen, en op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. Ons lokale team kan je helpen de juiste maat te kiezen, de basis uit te leggen en geschikte routes langs strand, parken en stad aan te bevelen. Voor route-ideeën en praktische tips kun je onze gids voor fietsverhuur in Barcelona lezen. |
| nl | 884 | Onze winkel ligt in Vila Olímpica, vlak bij het strand van Barceloneta, Torre MAPFRE, Casino Barcelona en Port Olímpic. Het is een ideale plek om een fiets op te halen en direct naar de boulevard, Parc de la Ciutadella of de nabijgelegen fietspaden van Barcelona te vertrekken. |
| nl | 886 | Onze winkel ligt in Vila Olímpica, vlak bij het strand van Barceloneta, Torre MAPFRE, Casino Barcelona en Port Olímpic. Het is een ideale plek om een fiets op te halen en direct naar de boulevard, Parc de la Ciutadella of de nabijgelegen fietspaden van Barcelona te vertrekken. |
| nl | 918 | Zijn een helm of slot inbegrepen bij de huur? |
| nl | 921 | Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar. |
| nl | 936 | Heb ik een rijbewijs nodig om een fiets te huren? |
| nl | 939 | Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren. |
| nl | 952 | Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen. |
| nl | 958 | Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen. |
| nl | 966 | Ontdek verwante verhuurdiensten vanuit onze winkel in Vila Olímpica del Poblenou en bekijk lokale gidsen over de belangrijkste activiteiten die we in Barcelona aanbieden. |
| nl | 967 | Meer verhuur in Barcelona en lokale gidsen |
| nl | 968 | Ontdek gerelateerde verhuurdiensten vanuit onze winkel in Vila Olímpica del Poblenou en bekijk lokale gidsen over onze belangrijkste activiteiten in Barcelona. |
| nl | 1015 | Helm, slot en bagageopslag · Kinderhelm en slot inbegrepen · Optioneel kinderzitje (€3) · Hulp bij het kiezen van de juiste fiets · Opslag voor jassen, rugzakken en bagage. |
| nl | 1025 | Controleer beschikbaarheid voor jouw fietsverhuur in Barcelona |
| pt | 690 | Aluga bicicletas na nossa loja local em Vila Olímpica del Poblenou, perto da Torre MAPFRE, Port Olímpic, Casino Barcelona e da praia da Barceloneta. Bicicletas urbanas confortáveis para adultos e crianças, capacete infantil e cadeado incluídos, cadeira infantil opcional em bicicletas selecionadas, serviço gratuito de guarda de bagagem e dicas de rotas locais. |
| pt | 721 | Bicicletas confortáveis para a cidade |
| pt | 722 | Escolhe entre bicicletas urbanas confortáveis preparadas para passeios tranquilos pelo passeio marítimo e pela cidade. Temos opções para adultos e crianças para que todos desfrutem do percurso. |
| pt | 726 | Em cada aluguer estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. |
| pt | 739 | Estes são os preços públicos atuais do nosso serviço de aluguer de bicicletas. Também podes comparar todas as tarifas na nossa página de preços e contactar-nos por WhatsApp para confirmar a disponibilidade antes de vires. |
| pt | 751 | Ideal para um percurso de meio dia explorando o passeio marítimo, Port Olímpic e o Parc de la Ciutadella. |
| pt | 771 | Prolonga o teu aluguer de bicicleta por mais um dia a um preço reduzido. |
| pt | 795 | Capacete infantil e cadeado incluídos em cada aluguer de bicicleta |
| pt | 797 | Ajuda para escolher a bicicleta certa de acordo com a tua altura e necessidades |
| pt | 800 | Serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada |
| pt | 833 | A RSB é uma loja local de aluguer na Carrer de Salvador Espriu, perto de Vila Olímpica, da praia da Barceloneta, Torre MAPFRE, Casino Barcelona e Port Olímpic. É um ponto de partida prático para percorrer o passeio marítimo, chegar ao Parc de la Ciutadella e usar as ciclovias próximas do centro de Barcelona. |
| pt | 838 | Aberto todos os dias: 10:30–13:30 e 16:30–20:00. Oferecemos alugueres de bicicletas por hora, dia completo e vários dias, com horários de devolução flexíveis.Em cada aluguer estão incluídos capacete infantil e cadeado, e em algumas bicicletas há cadeira infantil opcional. A nossa equipa local pode ajudar-te a escolher o tamanho certo, explicar o básico e recomendar rotas adequadas pela praia, parques e cidade. Para ideias de rotas e conselhos práticos, podes ler o nosso guia de aluguer de bicicletas em Barcelona. |
| pt | 921 | O capacete ou o cadeado estão incluídos no aluguer? |
| pt | 922 | Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional. |
| pt | 934 | Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido. |
| pt | 937 | Posso guardar a minha mala ou bagagem na loja? |
| pt | 938 | Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas. |
| pt | 942 | Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha. |
| pt | 946 | Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua. |
| pt | 954 | Descobre serviços de aluguer relacionados a partir da nossa loja em Vila Olímpica del Poblenou e consulta guias locais sobre as principais atividades que oferecemos em Barcelona. |
| pt | 956 | Descobre serviços de aluguer relacionados na nossa loja em Vila Olímpica del Poblenou e consulta guias locais sobre as principais atividades que oferecemos em Barcelona. |
| pt | 1003 | Capacete, cadeado e guarda de bagagem · Capacete infantil e cadeado incluídos · Cadeira infantil opcional (€3) · Ajuda para escolher a bicicleta certa · Guarda de bagagem gratuita. |
| pt | 1013 | Consulta a disponibilidade para o teu aluguer de bicicletas em Barcelona |
| pt | 1014 | Escreve-nos no WhatsApp ou visita a nossa loja em Vila Olímpica para organizar o teu aluguer de bicicletas perto da praia da Barceloneta. A nossa equipa vai ajudar-te a escolher a bicicleta certa e recomendar rotas fáceis ao longo da costa, por parques e pela cidade. |
| ca | 674 | Lloga bicicletes a la nostra botiga local de Vila Olímpica del Poblenou, a prop de Torre MAPFRE, Port Olímpic, Casino Barcelona i la platja de la Barceloneta. Còmodes bicicletes urbanes per a adults i nens, casc infantil i cadenat inclosos, cadireta infantil opcional en bicicletes seleccionades. Guarda d’equipatge gratuïta, consells de rutes locals. |
| ca | 710 | Amb cada lloguer s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. |
| ca | 735 | Ideal per a un recorregut de mig dia explorant el passeig marítim, Port Olímpic i el Parc de la Ciutadella. |
| ca | 779 | Casc infantil i cadenat inclosos amb cada lloguer de bicicleta |
| ca | 781 | Ajuda per triar la bicicleta adequada segons la teva talla i necessitats |
| ca | 782 | Suport del nostre equip local en la recollida |
| ca | 785 | Guarda d’equipatge gratuïta per a jaquetes, motxilles i equipatge a la nostra botiga supervisada |
| ca | 818 | RSB és una botiga local de lloguer al carrer de Salvador Espriu, a prop de Vila Olímpica, de la platja de la Barceloneta, Torre MAPFRE, Casino Barcelona i Port Olímpic. És un punt de partida pràctic per recórrer el passeig marítim, arribar al Parc de la Ciutadella i fer servir els carrils bici propers del centre de Barcelona. |
| ca | 823 | Obert cada dia: 10:30–13:30 i 16:30–20:00. Oferim lloguers de bicicletes per hores, dia complet i diversos dies.Amb cada lloguer s’inclouen casc infantil i cadenat, i en algunes bicicletes hi ha cadireta infantil opcional. El nostre equip local pot ajudar-te a triar la talla adequada, explicar-te el més bàsic i recomanar-te rutes adequades per la platja, els parcs i la ciutat. Per a idees de rutes i consells pràctics, pots llegir la nostra guia de lloguer de bicicletes a Barcelona. |
| ca | 906 | S’inclou casc o cadenat amb el lloguer? |
| ca | 907 | Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional. |
| ca | 915 | Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens. |
| ca | 919 | No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid. |
| ca | 922 | Puc guardar la meva bossa o equipatge a la botiga? |
| ca | 923 | Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales. |
| ca | 927 | Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida. |
| ca | 988 | Casc, cadenat i guarda d’equipatge · Casc infantil i cadenat inclosos · Cadireta infantil opcional (€3) · Ajuda per triar la bicicleta adequada · Guarda d’equipatge per a jaquetes, motxilles i equipatge. |
| sv | 686 | Hyr cyklar i vår lokala butik i Vila Olímpica del Poblenou, nära Torre MAPFRE, Port Olímpic, Casino Barcelona och Barceloneta-stranden. Bekväma stadscyklar för vuxna och barn, barnhjälm och lås ingår, barnsits som tillval på utvalda cyklar. Gratis bagageförvaring och lokala ruttips. |
| sv | 722 | Vid varje hyra ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. |
| sv | 725 | Läge vid havet |
| sv | 735 | Det här är de aktuella offentliga priserna för vår cykeluthyrning. Du kan också jämföra alla priser på vår prissida och kontakta oss via WhatsApp för att bekräfta tillgänglighet innan du kommer. |
| sv | 757 | Hämta idag och lämna tillbaka imorgon för att få ut så mycket som möjligt av din tid på två hjul. |
| sv | 762 | Få mer tid att utforska Barcelona med cykel i två dagar. |
| sv | 791 | Barnhjälm och lås ingår vid varje cykelhyra |
| sv | 794 | Stöd från vårt lokala team vid upphämtning |
| sv | 835 | Öppet varje dag: 10:30–13:30 och 16:30–20:00. Vi erbjuder cykeluthyrning per timme, heldag och flera dagar.Vid varje hyra ingår barnhjälm och lås, och på vissa cyklar finns barnsits som tillval. Vårt lokala team kan hjälpa dig att välja rätt storlek, förklara grunderna och rekommendera lämpliga rutter längs strand, parker och stad. För ruttidéer och praktiska tips kan du läsa vår guide till cykeluthyrning i Barcelona. |
| sv | 915 | Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med. |
| sv | 918 | Ingår hjälm eller lås i hyran? |
| sv | 919 | Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval. |
| sv | 930 | Behöver jag körkort för att hyra en cykel? |
| sv | 931 | Nej. Inget körkort krävs för att hyra en cykel. |
| sv | 940 | Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid. |
| sv | 944 | Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel. |
| sv | 952 | Upptäck relaterade uthyrningstjänster från vår butik i Vila Olímpica del Poblenou och läs lokala guider om de viktigaste aktiviteterna vi erbjuder i Barcelona. |
| sv | 953 | Fler uthyrningar i Barcelona och lokala guider |
| sv | 954 | Upptäck relaterade uthyrningstjänster från vår butik i Vila Olímpica del Poblenou och läs lokala guider om våra viktigaste aktiviteter i Barcelona. |
| sv | 965 | Rullskridskouthyrning i Barcelona |
| sv | 1001 | Hjälm, lås och bagageförvaring · Barnhjälm och lås ingår · Barnsits som tillval (€3) · Hjälp att välja rätt cykel · Förvaring för jackor, ryggsäckar och bagage. |
| pl | 745 | Wynajmij rowery w naszej lokalnej wypożyczalni w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Wygodne rowery miejskie dla dorosłych i dzieci, kask dziecięcy i zapięcie w cenie oraz opcjonalny fotelik dziecięcy w wybranych rowerach. Darmowe przechowanie bagażu i lokalne wskazówki tras. |
| pl | 781 | Kask dziecięcy i zapięcie są w cenie każdego wynajmu, a opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach. |
| pl | 800 | Idealne na krótką przejażdżkę wzdłuż plaży lub pierwszą próbę jazdy rowerem. |
| pl | 806 | Idealne na półdniową przejażdżkę nad morzem, przy Port Olímpic i w parku Ciutadella. |
| pl | 850 | Kask dziecięcy i zapięcie w cenie każdego wynajmu roweru |
| pl | 894 | Otwarte codziennie: 10:30–13:30 i 16:30–20:00. Oferujemy wynajem rowerów na godziny, cały dzień i kilka dni. Kask dziecięcy i zapięcie rowerowe są w cenie każdego wynajmu, a opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach. Nasz lokalny zespół pomoże dobrać odpowiedni rozmiar, wyjaśni podstawy i poleci łatwe trasy nad plażą, w parkach i po mieście. Lokalne pomysły na trasy i praktyczne wskazówki znajdziesz w naszym przewodniku po wynajmie rowerów w Barcelonie. |
| pl | 977 | Czy kask lub zapięcie są wliczone w wynajem? |
| pl | 978 | Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach. |
| pl | 990 | Nie. Do wynajmu roweru nie jest wymagane prawo jazdy. |
| pl | 1060 | Kask dziecięcy i zapięcie w cenie · Opcjonalny fotelik dziecięcy (€3) · Pomoc w wyborze odpowiedniego roweru · Przechowanie kurtek, plecaków i bagażu. |

## S. MATRIZ FAQ VISIBLE ↔ SCHEMA

| Idioma | N.º | Visible completo | Schema completo | Pregunta coincide | Respuesta coincide |
| --- | --- | --- | --- | --- | --- |
| en | 1 | {"line": 974, "question": "Do I need experience to rent a bike?", "answer": "No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Do I need experience to rent a bike?", "answer": "No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started.", "answer_raw": "No, you do not need previous experience. We rent bikes to beginners and confident riders, and our staff can help you choose a comfortable bike to get started."} | True | True |
| en | 2 | {"line": 978, "question": "Is a helmet or lock included with the rental?", "answer": "Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Is a helmet or lock included with the rental?", "answer": "Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes.", "answer_raw": "Yes. A children's helmet and a lock are included with every bike rental. An optional child seat is available on selected bikes."} | True | True |
| en | 3 | {"line": 982, "question": "Where can I ride a bike near the shop?", "answer": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Where can I ride a bike near the shop?", "answer": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby.", "answer_raw": "Our shop is close to the seafront promenade, Port Olímpic and open areas where many visitors start with a relaxed ride before exploring bike-friendly parks and cycle lanes nearby."} | True | True |
| en | 4 | {"line": 986, "question": "Do you have bikes for beginners or kids?", "answer": "Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Do you have bikes for beginners or kids?", "answer": "Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids.", "answer_raw": "Yes. We can help you choose a bike that suits your size and experience level, including bikes suitable for kids."} | True | True |
| en | 5 | {"line": 990, "question": "Do I need a licence to rent a bike?", "answer": "No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Do I need a licence to rent a bike?", "answer": "No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID.", "answer_raw": "No driving licence is needed. Bikes are non-motorised, so anyone can rent one with a valid ID."} | True | True |
| en | 6 | {"line": 994, "question": "Can I store my bag or luggage at the shop?", "answer": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Can I store my bag or luggage at the shop?", "answer": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride.", "answer_raw": "Yes. Free storage for jackets, backpacks and luggage is available in our supervised shop while you ride."} | True | True |
| en | 7 | {"line": 998, "question": "Can I book or ask questions by WhatsApp?", "answer": "Yes. You can message us on WhatsApp before coming to confirm availability, ask questions or arrange your pick-up time.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Can I book or ask questions by WhatsApp?", "answer": "Yes. You can message us on WhatsApp before coming to confirm availability, ask questions or arrange your pick-up time.", "answer_raw": "Yes. You can message us on WhatsApp before coming to confirm availability, ask questions or arrange your pick-up time."} | True | True |
| en | 8 | {"line": 1002, "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Contact us if you want to confirm bike availability or the best time to collect your bike.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Contact us if you want to confirm bike availability or the best time to collect your bike.", "answer_raw": "You can book via WhatsApp, email or phone. Contact us if you want to confirm bike availability or the best time to collect your bike."} | True | True |
| es | 1 | {"line": 947, "question": "¿Necesito experiencia para alquilar una bicicleta?", "answer": "No, no necesitas experiencia previa. Alquilamos bicicletas a principiantes y a personas que ya montan con confianza, y nuestro equipo puede ayudarte a elegir una bicicleta cómoda para empezar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "¿Necesito experiencia para alquilar una bicicleta?", "answer": "No, no necesitas experiencia previa. Alquilamos bicicletas a principiantes y a personas que ya montan con confianza, y nuestro equipo puede ayudarte a elegir una bicicleta cómoda para empezar.", "answer_raw": "No, no necesitas experiencia previa. Alquilamos bicicletas a principiantes y a personas que ya montan con confianza, y nuestro equipo puede ayudarte a elegir una bicicleta cómoda para empezar."} | True | True |
| es | 2 | {"line": 951, "question": "¿Se incluye casco o candado con el alquiler?", "answer": "Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "¿Se incluye casco o candado con el alquiler?", "answer": "Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional.", "answer_raw": "Sí. Con cada alquiler de bicicleta se incluyen casco infantil y candado. En algunas bicicletas hay silla infantil opcional."} | True | True |
| es | 3 | {"line": 955, "question": "¿Dónde puedo montar en bicicleta cerca de la tienda?", "answer": "Nuestra tienda está cerca del paseo marítimo, Port Olímpic, Torre MAPFRE y Casino Barcelona, en una zona desde la que muchos visitantes empiezan una ruta tranquila antes de explorar parques y carriles bici cercanos.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "¿Dónde puedo montar en bicicleta cerca de la tienda?", "answer": "Nuestra tienda está cerca del paseo marítimo, Port Olímpic, Torre MAPFRE y Casino Barcelona, en una zona desde la que muchos visitantes empiezan una ruta tranquila antes de explorar parques y carriles bici cercanos.", "answer_raw": "Nuestra tienda está cerca del paseo marítimo, Port Olímpic, Torre MAPFRE y Casino Barcelona, en una zona desde la que muchos visitantes empiezan una ruta tranquila antes de explorar parques y carriles bici cercanos."} | True | True |
| es | 4 | {"line": 959, "question": "¿Tenéis bicicletas para principiantes o para niños?", "answer": "Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "¿Tenéis bicicletas para principiantes o para niños?", "answer": "Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños.", "answer_raw": "Sí. Podemos ayudarte a elegir una bicicleta que se adapte a tu talla y nivel, incluidas bicicletas adecuadas para niños."} | True | True |
| es | 5 | {"line": 963, "question": "¿Necesito licencia para alquilar una bicicleta?", "answer": "No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "¿Necesito licencia para alquilar una bicicleta?", "answer": "No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido.", "answer_raw": "No hace falta licencia de conducir. Las bicicletas no son motorizadas, así que cualquiera puede alquilar una con un documento de identidad válido."} | True | True |
| es | 6 | {"line": 967, "question": "¿Puedo guardar mi bolsa o equipaje en la tienda?", "answer": "Sí. Disponemos de consigna gratuita para chaquetas, mochilas y equipaje en nuestra tienda supervisada mientras montas.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "¿Puedo guardar mi bolsa o equipaje en la tienda?", "answer": "Sí. Disponemos de consigna gratuita para chaquetas, mochilas y equipaje en nuestra tienda supervisada mientras montas.", "answer_raw": "Sí. Disponemos de consigna gratuita para chaquetas, mochilas y equipaje en nuestra tienda supervisada mientras montas."} | True | True |
| es | 7 | {"line": 971, "question": "¿Puedo reservar o preguntar por WhatsApp?", "answer": "Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "¿Puedo reservar o preguntar por WhatsApp?", "answer": "Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida.", "answer_raw": "Sí. Puedes escribirnos por WhatsApp antes de venir para confirmar disponibilidad, hacer preguntas o organizar la hora de recogida."} | True | True |
| es | 8 | {"line": 975, "question": "¿Cómo reservo o cómo contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "¿Cómo reservo o cómo contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya.", "answer_raw": "Puedes reservar por WhatsApp, email o teléfono. Contáctanos si quieres confirmar disponibilidad de bicicletas o el mejor momento para recoger la tuya."} | True | True |
| fr | 1 | {"line": 874, "question": "Ai-je besoin d’expérience pour louer un vélo ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Ai-je besoin d’expérience pour louer un vélo ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer.", "answer_raw": "Non, aucune expérience préalable n’est nécessaire. Nous louons des vélos aux débutants comme aux cyclistes confirmés, et notre équipe peut vous aider à choisir un vélo confortable pour commencer."} | True | True |
| fr | 2 | {"line": 878, "question": "Le casque ou l’antivol sont-ils inclus avec la location ?", "answer": "Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Le casque ou l’antivol sont-ils inclus avec la location ?", "answer": "Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos.", "answer_raw": "Oui. Chaque location de vélo inclut un casque pour enfant et un antivol. Un siège enfant en option est disponible sur certains vélos."} | True | True |
| fr | 3 | {"line": 882, "question": "Où puis-je rouler à vélo près de la boutique ?", "answer": "Notre boutique se trouve près de la promenade du front de mer, de Port Olímpic, de Torre MAPFRE et de Casino Barcelona, dans un secteur où de nombreux visiteurs commencent une balade tranquille avant d’explorer les parcs et pistes cyclables à proximité.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Où puis-je rouler à vélo près de la boutique ?", "answer": "Notre boutique se trouve près de la promenade du front de mer, de Port Olímpic, de Torre MAPFRE et de Casino Barcelona, dans un secteur où de nombreux visiteurs commencent une balade tranquille avant d’explorer les parcs et pistes cyclables à proximité.", "answer_raw": "Notre boutique se trouve près de la promenade du front de mer, de Port Olímpic, de Torre MAPFRE et de Casino Barcelona, dans un secteur où de nombreux visiteurs commencent une balade tranquille avant d’explorer les parcs et pistes cyclables à proximité."} | True | True |
| fr | 4 | {"line": 886, "question": "Avez-vous des vélos pour débutants ou pour enfants ?", "answer": "Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Avez-vous des vélos pour débutants ou pour enfants ?", "answer": "Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants.", "answer_raw": "Oui. Nous pouvons vous aider à choisir un vélo adapté à votre taille et à votre niveau, y compris des vélos adaptés aux enfants."} | True | True |
| fr | 5 | {"line": 890, "question": "Ai-je besoin d’un permis pour louer un vélo ?", "answer": "Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Ai-je besoin d’un permis pour louer un vélo ?", "answer": "Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un.", "answer_raw": "Aucun permis de conduire n’est nécessaire. Les vélos ne sont pas motorisés, donc toute personne munie d’une pièce d’identité valide peut en louer un."} | True | True |
| fr | 6 | {"line": 894, "question": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "answer": "Oui. Nous disposons d’une consigne gratuite pour les vestes, sacs à dos et bagages dans notre boutique surveillée pendant votre sortie.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "answer": "Oui. Nous disposons d’une consigne gratuite pour les vestes, sacs à dos et bagages dans notre boutique surveillée pendant votre sortie.", "answer_raw": "Oui. Nous disposons d’une consigne gratuite pour les vestes, sacs à dos et bagages dans notre boutique surveillée pendant votre sortie."} | True | True |
| fr | 7 | {"line": 898, "question": "Puis-je réserver ou poser des questions par WhatsApp ?", "answer": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puis-je réserver ou poser des questions par WhatsApp ?", "answer": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait.", "answer_raw": "Oui. Vous pouvez nous écrire sur WhatsApp avant de venir pour confirmer la disponibilité, poser des questions ou organiser l’heure de retrait."} | True | True |
| fr | 8 | {"line": 902, "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver via WhatsApp, e-mail ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des vélos ou le meilleur moment pour venir chercher le vôtre.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver via WhatsApp, e-mail ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des vélos ou le meilleur moment pour venir chercher le vôtre.", "answer_raw": "Vous pouvez réserver via WhatsApp, e-mail ou téléphone. Contactez-nous si vous souhaitez confirmer la disponibilité des vélos ou le meilleur moment pour venir chercher le vôtre."} | True | True |
| it | 1 | {"line": 880, "question": "Ho bisogno di esperienza per noleggiare una bicicletta?", "answer": "No, non è necessaria esperienza precedente. Noleggiamo biciclette sia a principianti sia a chi pedala già con sicurezza, e il nostro team può aiutarti a scegliere una bici comoda per iniziare.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Ho bisogno di esperienza per noleggiare una bicicletta?", "answer": "No, non è necessaria esperienza precedente. Noleggiamo biciclette sia a principianti sia a chi pedala già con sicurezza, e il nostro team può aiutarti a scegliere una bici comoda per iniziare.", "answer_raw": "No, non è necessaria esperienza precedente. Noleggiamo biciclette sia a principianti sia a chi pedala già con sicurezza, e il nostro team può aiutarti a scegliere una bici comoda per iniziare."} | True | True |
| it | 2 | {"line": 884, "question": "Il casco o il lucchetto sono inclusi nel noleggio?", "answer": "Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Il casco o il lucchetto sono inclusi nel noleggio?", "answer": "Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale.", "answer_raw": "Sì. Ogni noleggio bici include casco bambino e lucchetto. Su alcune biciclette è disponibile un seggiolino opzionale."} | True | True |
| it | 3 | {"line": 888, "question": "Dove posso andare in bici vicino al negozio?", "answer": "Il nostro negozio si trova vicino al lungomare, a Port Olímpic, Torre MAPFRE e Casino Barcelona, in una zona da cui molti visitatori iniziano un percorso tranquillo prima di esplorare parchi e piste ciclabili vicine.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Dove posso andare in bici vicino al negozio?", "answer": "Il nostro negozio si trova vicino al lungomare, a Port Olímpic, Torre MAPFRE e Casino Barcelona, in una zona da cui molti visitatori iniziano un percorso tranquillo prima di esplorare parchi e piste ciclabili vicine.", "answer_raw": "Il nostro negozio si trova vicino al lungomare, a Port Olímpic, Torre MAPFRE e Casino Barcelona, in una zona da cui molti visitatori iniziano un percorso tranquillo prima di esplorare parchi e piste ciclabili vicine."} | True | True |
| it | 4 | {"line": 892, "question": "Avete biciclette per principianti o per bambini?", "answer": "Sì. Possiamo aiutarti a scegliere una bicicletta adatta alla tua altezza e al tuo livello, comprese biciclette adatte ai bambini.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Avete biciclette per principianti o per bambini?", "answer": "Sì. Possiamo aiutarti a scegliere una bicicletta adatta alla tua altezza e al tuo livello, comprese biciclette adatte ai bambini.", "answer_raw": "Sì. Possiamo aiutarti a scegliere una bicicletta adatta alla tua altezza e al tuo livello, comprese biciclette adatte ai bambini."} | True | True |
| it | 5 | {"line": 896, "question": "Ho bisogno della patente per noleggiare una bicicletta?", "answer": "No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Ho bisogno della patente per noleggiare una bicicletta?", "answer": "No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido.", "answer_raw": "No, non serve la patente di guida. Le biciclette non sono motorizzate, quindi chiunque può noleggiarne una con un documento d’identità valido."} | True | True |
| it | 6 | {"line": 900, "question": "Posso lasciare la mia borsa o i bagagli in negozio?", "answer": "Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Posso lasciare la mia borsa o i bagagli in negozio?", "answer": "Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali.", "answer_raw": "Sì. Mettiamo a disposizione deposito bagagli gratuito per giacche, zaini e valigie nel nostro negozio sorvegliato mentre pedali."} | True | True |
| it | 7 | {"line": 904, "question": "Posso prenotare o fare domande via WhatsApp?", "answer": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare la disponibilità, fare domande o organizzare l’orario di ritiro.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso prenotare o fare domande via WhatsApp?", "answer": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare la disponibilità, fare domande o organizzare l’orario di ritiro.", "answer_raw": "Sì. Puoi scriverci su WhatsApp prima di venire per confermare la disponibilità, fare domande o organizzare l’orario di ritiro."} | True | True |
| it | 8 | {"line": 908, "question": "Come posso prenotare o contattarvi?", "answer": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle biciclette o il momento migliore per ritirare la tua.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Come posso prenotare o contattarvi?", "answer": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle biciclette o il momento migliore per ritirare la tua.", "answer_raw": "Puoi prenotare via WhatsApp, email o telefono. Contattaci se vuoi confermare la disponibilità delle biciclette o il momento migliore per ritirare la tua."} | True | True |
| de | 1 | {"line": 903, "question": "Brauche ich Erfahrung, um ein Fahrrad zu mieten?", "answer": "Nein, Vorerfahrung ist nicht nötig. Wir vermieten Fahrräder an Anfänger und sichere Fahrer, und unser Team hilft dir, ein bequemes Fahrrad für den Einstieg zu wählen.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Brauche ich Erfahrung, um ein Fahrrad zu mieten?", "answer": "Nein, Vorerfahrung ist nicht nötig. Wir vermieten Fahrräder an Anfänger und sichere Fahrer, und unser Team hilft dir, ein bequemes Fahrrad für den Einstieg zu wählen.", "answer_raw": "Nein, Vorerfahrung ist nicht nötig. Wir vermieten Fahrräder an Anfänger und sichere Fahrer, und unser Team hilft dir, ein bequemes Fahrrad für den Einstieg zu wählen."} | True | True |
| de | 2 | {"line": 909, "question": "Sind Helm oder Schloss in der Miete enthalten?", "answer": "Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Sind Helm oder Schloss in der Miete enthalten?", "answer": "Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar.", "answer_raw": "Ja. Bei jeder Fahrradmiete sind ein Kinderhelm und ein Schloss inbegriffen. Bei ausgewählten Fahrrädern ist ein optionaler Kindersitz verfügbar."} | True | True |
| de | 3 | {"line": 915, "question": "Wo kann ich in der Nähe des Shops Fahrrad fahren?", "answer": "Unser Shop liegt nahe der Strandpromenade, Port Olímpic, Torre MAPFRE und Casino Barcelona, in einem Bereich, in dem viele Besucher eine entspannte Route starten, bevor sie Parks und nahegelegene Radwege erkunden.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Wo kann ich in der Nähe des Shops Fahrrad fahren?", "answer": "Unser Shop liegt nahe der Strandpromenade, Port Olímpic, Torre MAPFRE und Casino Barcelona, in einem Bereich, in dem viele Besucher eine entspannte Route starten, bevor sie Parks und nahegelegene Radwege erkunden.", "answer_raw": "Unser Shop liegt nahe der Strandpromenade, Port Olímpic, Torre MAPFRE und Casino Barcelona, in einem Bereich, in dem viele Besucher eine entspannte Route starten, bevor sie Parks und nahegelegene Radwege erkunden."} | True | True |
| de | 4 | {"line": 921, "question": "Gibt es Fahrräder für Anfänger oder Kinder?", "answer": "Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Gibt es Fahrräder für Anfänger oder Kinder?", "answer": "Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder.", "answer_raw": "Ja. Wir helfen dir dabei, ein Fahrrad passend zu deiner Größe und deinem Niveau zu wählen, einschließlich Fahrrädern für Kinder."} | True | True |
| de | 5 | {"line": 927, "question": "Brauche ich einen Führerschein, um ein Fahrrad zu mieten?", "answer": "Nein. Für die Fahrradmiete ist kein Führerschein erforderlich.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Brauche ich einen Führerschein, um ein Fahrrad zu mieten?", "answer": "Nein. Für die Fahrradmiete ist kein Führerschein erforderlich.", "answer_raw": "Nein. Für die Fahrradmiete ist kein Führerschein erforderlich."} | True | True |
| de | 6 | {"line": 933, "question": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "answer": "Ja. In unserem beaufsichtigten Shop gibt es kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck, während du fährst.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "answer": "Ja. In unserem beaufsichtigten Shop gibt es kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck, während du fährst.", "answer_raw": "Ja. In unserem beaufsichtigten Shop gibt es kostenlose Aufbewahrung für Jacken, Rucksäcke und Gepäck, während du fährst."} | True | True |
| de | 7 | {"line": 940, "question": "Kann ich per WhatsApp buchen oder Fragen stellen?", "answer": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um Verfügbarkeit zu bestätigen, Fragen zu stellen oder die Abholzeit zu vereinbaren.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kann ich per WhatsApp buchen oder Fragen stellen?", "answer": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um Verfügbarkeit zu bestätigen, Fragen zu stellen oder die Abholzeit zu vereinbaren.", "answer_raw": "Ja. Du kannst uns vor deinem Besuch per WhatsApp schreiben, um Verfügbarkeit zu bestätigen, Fragen zu stellen oder die Abholzeit zu vereinbaren."} | True | True |
| de | 8 | {"line": 946, "question": "Wie kann ich buchen oder Kontakt aufnehmen?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Fahrradverfügbarkeit oder den besten Zeitpunkt zur Abholung bestätigen möchtest.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Wie kann ich buchen oder Kontakt aufnehmen?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Fahrradverfügbarkeit oder den besten Zeitpunkt zur Abholung bestätigen möchtest.", "answer_raw": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Kontaktiere uns, wenn du die Fahrradverfügbarkeit oder den besten Zeitpunkt zur Abholung bestätigen möchtest."} | True | True |
| nl | 1 | {"line": 911, "question": "Heb ik ervaring nodig om een fiets te huren?", "answer": "Nee, eerdere ervaring is niet nodig. We verhuren fietsen aan beginners en aan mensen die al zeker fietsen, en ons team kan je helpen een comfortabele fiets te kiezen om te starten.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Heb ik ervaring nodig om een fiets te huren?", "answer": "Nee, eerdere ervaring is niet nodig. We verhuren fietsen aan beginners en aan mensen die al zeker fietsen, en ons team kan je helpen een comfortabele fiets te kiezen om te starten.", "answer_raw": "Nee, eerdere ervaring is niet nodig. We verhuren fietsen aan beginners en aan mensen die al zeker fietsen, en ons team kan je helpen een comfortabele fiets te kiezen om te starten."} | True | True |
| nl | 2 | {"line": 917, "question": "Zijn een helm of slot inbegrepen bij de huur?", "answer": "Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Zijn een helm of slot inbegrepen bij de huur?", "answer": "Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar.", "answer_raw": "Ja. Bij elke fietsverhuur zijn een kinderhelm en een slot inbegrepen. Op geselecteerde fietsen is een optioneel kinderzitje beschikbaar."} | True | True |
| nl | 3 | {"line": 923, "question": "Waar kan ik fietsen in de buurt van de winkel?", "answer": "Onze winkel ligt dicht bij de boulevard, Port Olímpic, Torre MAPFRE en Casino Barcelona, in een gebied waar veel bezoekers een rustige route beginnen voordat ze parken en fietspaden in de buurt verkennen.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Waar kan ik fietsen in de buurt van de winkel?", "answer": "Onze winkel ligt dicht bij de boulevard, Port Olímpic, Torre MAPFRE en Casino Barcelona, in een gebied waar veel bezoekers een rustige route beginnen voordat ze parken en fietspaden in de buurt verkennen.", "answer_raw": "Onze winkel ligt dicht bij de boulevard, Port Olímpic, Torre MAPFRE en Casino Barcelona, in een gebied waar veel bezoekers een rustige route beginnen voordat ze parken en fietspaden in de buurt verkennen."} | True | True |
| nl | 4 | {"line": 929, "question": "Hebben jullie fietsen voor beginners of kinderen?", "answer": "Ja. We kunnen je helpen een fiets te kiezen die past bij je lengte en niveau, inclusief fietsen die geschikt zijn voor kinderen.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Hebben jullie fietsen voor beginners of kinderen?", "answer": "Ja. We kunnen je helpen een fiets te kiezen die past bij je lengte en niveau, inclusief fietsen die geschikt zijn voor kinderen.", "answer_raw": "Ja. We kunnen je helpen een fiets te kiezen die past bij je lengte en niveau, inclusief fietsen die geschikt zijn voor kinderen."} | True | True |
| nl | 5 | {"line": 935, "question": "Heb ik een rijbewijs nodig om een fiets te huren?", "answer": "Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Heb ik een rijbewijs nodig om een fiets te huren?", "answer": "Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren.", "answer_raw": "Nee, een rijbewijs is niet nodig. Fietsen zijn niet gemotoriseerd, dus iedereen met een geldig identiteitsbewijs kan er een huren."} | True | True |
| nl | 6 | {"line": 941, "question": "Kan ik mijn tas of bagage in de winkel achterlaten?", "answer": "Ja. We bieden gratis opslag voor jassen, rugzakken en bagage in onze bewaakte winkel terwijl je fietst.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kan ik mijn tas of bagage in de winkel achterlaten?", "answer": "Ja. We bieden gratis opslag voor jassen, rugzakken en bagage in onze bewaakte winkel terwijl je fietst.", "answer_raw": "Ja. We bieden gratis opslag voor jassen, rugzakken en bagage in onze bewaakte winkel terwijl je fietst."} | True | True |
| nl | 7 | {"line": 948, "question": "Kan ik via WhatsApp reserveren of vragen stellen?", "answer": "Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan ik via WhatsApp reserveren of vragen stellen?", "answer": "Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen.", "answer_raw": "Ja. Je kunt ons via WhatsApp schrijven voordat je komt om beschikbaarheid te bevestigen, vragen te stellen of het ophaaltijdstip te regelen."} | True | True |
| nl | 8 | {"line": 954, "question": "Hoe reserveer ik of neem ik contact met jullie op?", "answer": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hoe reserveer ik of neem ik contact met jullie op?", "answer": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen.", "answer_raw": "Je kunt reserveren via WhatsApp, e-mail of telefoon. Neem contact met ons op als je de beschikbaarheid van fietsen of het beste moment om de fiets op te halen wilt bevestigen."} | True | True |
| pt | 1 | {"line": 916, "question": "Preciso de experiência para alugar uma bicicleta?", "answer": "Não, não precisas de experiência anterior. Alugamos bicicletas a principiantes e a pessoas que já pedalam com confiança, e a nossa equipa pode ajudar-te a escolher uma bicicleta confortável para começar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Preciso de experiência para alugar uma bicicleta?", "answer": "Não, não precisas de experiência anterior. Alugamos bicicletas a principiantes e a pessoas que já pedalam com confiança, e a nossa equipa pode ajudar-te a escolher uma bicicleta confortável para começar.", "answer_raw": "Não, não precisas de experiência anterior. Alugamos bicicletas a principiantes e a pessoas que já pedalam com confiança, e a nossa equipa pode ajudar-te a escolher uma bicicleta confortável para começar."} | True | True |
| pt | 2 | {"line": 920, "question": "O capacete ou o cadeado estão incluídos no aluguer?", "answer": "Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "O capacete ou o cadeado estão incluídos no aluguer?", "answer": "Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional.", "answer_raw": "Sim. Em cada aluguer de bicicleta estão incluídos capacete infantil e cadeado. Em algumas bicicletas há cadeira infantil opcional."} | True | True |
| pt | 3 | {"line": 924, "question": "Onde posso andar de bicicleta perto da loja?", "answer": "A nossa loja fica perto do passeio marítimo, Port Olímpic, Torre MAPFRE e Casino Barcelona, numa zona de onde muitos visitantes começam um percurso tranquilo antes de explorar parques e ciclovias próximas.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Onde posso andar de bicicleta perto da loja?", "answer": "A nossa loja fica perto do passeio marítimo, Port Olímpic, Torre MAPFRE e Casino Barcelona, numa zona de onde muitos visitantes começam um percurso tranquilo antes de explorar parques e ciclovias próximas.", "answer_raw": "A nossa loja fica perto do passeio marítimo, Port Olímpic, Torre MAPFRE e Casino Barcelona, numa zona de onde muitos visitantes começam um percurso tranquilo antes de explorar parques e ciclovias próximas."} | True | True |
| pt | 4 | {"line": 928, "question": "Têm bicicletas para principiantes ou para crianças?", "answer": "Sim. Podemos ajudar-te a escolher uma bicicleta adequada à tua altura e ao teu nível, incluindo bicicletas apropriadas para crianças.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Têm bicicletas para principiantes ou para crianças?", "answer": "Sim. Podemos ajudar-te a escolher uma bicicleta adequada à tua altura e ao teu nível, incluindo bicicletas apropriadas para crianças.", "answer_raw": "Sim. Podemos ajudar-te a escolher uma bicicleta adequada à tua altura e ao teu nível, incluindo bicicletas apropriadas para crianças."} | True | True |
| pt | 5 | {"line": 932, "question": "Preciso de carta de condução para alugar uma bicicleta?", "answer": "Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Preciso de carta de condução para alugar uma bicicleta?", "answer": "Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido.", "answer_raw": "Não, não é necessária carta de condução. As bicicletas não são motorizadas, por isso qualquer pessoa pode alugar uma com um documento de identificação válido."} | True | True |
| pt | 6 | {"line": 936, "question": "Posso guardar a minha mala ou bagagem na loja?", "answer": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Posso guardar a minha mala ou bagagem na loja?", "answer": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas.", "answer_raw": "Sim. Dispomos de um serviço gratuito de guarda de bagagem para casacos, mochilas e malas na nossa loja supervisionada enquanto pedalas."} | True | True |
| pt | 7 | {"line": 940, "question": "Posso reservar ou fazer perguntas por WhatsApp?", "answer": "Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso reservar ou fazer perguntas por WhatsApp?", "answer": "Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha.", "answer_raw": "Sim. Podes escrever-nos no WhatsApp antes de vires para confirmar disponibilidade, fazer perguntas ou combinar a hora de recolha."} | True | True |
| pt | 8 | {"line": 944, "question": "Como reservo ou como vos contacto?", "answer": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Como reservo ou como vos contacto?", "answer": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua.", "answer_raw": "Podes reservar por WhatsApp, email ou telefone. Contacta-nos se quiseres confirmar a disponibilidade das bicicletas ou o melhor momento para levantar a tua."} | True | True |
| ca | 1 | {"line": 901, "question": "Necessito experiència per llogar una bicicleta?", "answer": "No, no cal experiència prèvia. Lloguem bicicletes a principiants i a persones que ja pedalen amb confiança, i el nostre equip pot ajudar-te a triar una bicicleta còmoda per començar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Necessito experiència per llogar una bicicleta?", "answer": "No, no cal experiència prèvia. Lloguem bicicletes a principiants i a persones que ja pedalen amb confiança, i el nostre equip pot ajudar-te a triar una bicicleta còmoda per començar.", "answer_raw": "No, no cal experiència prèvia. Lloguem bicicletes a principiants i a persones que ja pedalen amb confiança, i el nostre equip pot ajudar-te a triar una bicicleta còmoda per començar."} | True | True |
| ca | 2 | {"line": 905, "question": "S’inclou casc o cadenat amb el lloguer?", "answer": "Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "S’inclou casc o cadenat amb el lloguer?", "answer": "Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional.", "answer_raw": "Sí. Amb cada lloguer de bicicleta s’inclouen casc infantil i cadenat. En algunes bicicletes hi ha cadireta infantil opcional."} | True | True |
| ca | 3 | {"line": 909, "question": "On puc anar amb bicicleta a prop de la botiga?", "answer": "La nostra botiga és a prop del passeig marítim, Port Olímpic, Torre MAPFRE i Casino Barcelona, en una zona des d’on molts visitants comencen una ruta tranquil·la abans d’explorar parcs i carrils bici propers.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "On puc anar amb bicicleta a prop de la botiga?", "answer": "La nostra botiga és a prop del passeig marítim, Port Olímpic, Torre MAPFRE i Casino Barcelona, en una zona des d’on molts visitants comencen una ruta tranquil·la abans d’explorar parcs i carrils bici propers.", "answer_raw": "La nostra botiga és a prop del passeig marítim, Port Olímpic, Torre MAPFRE i Casino Barcelona, en una zona des d’on molts visitants comencen una ruta tranquil·la abans d’explorar parcs i carrils bici propers."} | True | True |
| ca | 4 | {"line": 913, "question": "Teniu bicicletes per a principiants o per a nens?", "answer": "Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Teniu bicicletes per a principiants o per a nens?", "answer": "Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens.", "answer_raw": "Sí. Podem ajudar-te a triar una bicicleta que s’adapti a la teva talla i nivell, incloses bicicletes adequades per a nens."} | True | True |
| ca | 5 | {"line": 917, "question": "Necessito carnet per llogar una bicicleta?", "answer": "No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Necessito carnet per llogar una bicicleta?", "answer": "No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid.", "answer_raw": "No, no cal carnet de conduir. Les bicicletes no són motoritzades, així que qualsevol persona en pot llogar una amb un document d’identitat vàlid."} | True | True |
| ca | 6 | {"line": 921, "question": "Puc guardar la meva bossa o equipatge a la botiga?", "answer": "Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Puc guardar la meva bossa o equipatge a la botiga?", "answer": "Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales.", "answer_raw": "Sí. Disposem de servei gratuït de guarda d’equipatge per a jaquetes, motxilles i equipatge a la nostra botiga supervisada mentre pedales."} | True | True |
| ca | 7 | {"line": 925, "question": "Puc reservar o fer preguntes per WhatsApp?", "answer": "Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puc reservar o fer preguntes per WhatsApp?", "answer": "Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida.", "answer_raw": "Sí. Ens pots escriure per WhatsApp abans de venir per confirmar disponibilitat, fer preguntes o organitzar l’hora de recollida."} | True | True |
| ca | 8 | {"line": 929, "question": "Com reservo o com us contacto?", "answer": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar la disponibilitat de les bicicletes o el millor moment per recollir la teva.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Com reservo o com us contacto?", "answer": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar la disponibilitat de les bicicletes o el millor moment per recollir la teva.", "answer_raw": "Pots reservar per WhatsApp, email o telèfon. Contacta’ns si vols confirmar la disponibilitat de les bicicletes o el millor moment per recollir la teva."} | True | True |
| sv | 1 | {"line": 913, "question": "Behöver jag erfarenhet för att hyra en cykel?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Behöver jag erfarenhet för att hyra en cykel?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med.", "answer_raw": "Nej, du behöver ingen tidigare erfarenhet. Vi hyr ut cyklar till nybörjare och till personer som redan cyklar tryggt, och vårt team kan hjälpa dig att välja en bekväm cykel att börja med."} | True | True |
| sv | 2 | {"line": 917, "question": "Ingår hjälm eller lås i hyran?", "answer": "Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Ingår hjälm eller lås i hyran?", "answer": "Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval.", "answer_raw": "Ja. Vid varje cykelhyra ingår barnhjälm och lås. På vissa cyklar finns barnsits som tillval."} | True | True |
| sv | 3 | {"line": 921, "question": "Var kan jag cykla nära butiken?", "answer": "Vår butik ligger nära strandpromenaden, Port Olímpic, Torre MAPFRE och Casino Barcelona, i ett område där många besökare börjar en lugn tur innan de utforskar parker och närliggande cykelvägar.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Var kan jag cykla nära butiken?", "answer": "Vår butik ligger nära strandpromenaden, Port Olímpic, Torre MAPFRE och Casino Barcelona, i ett område där många besökare börjar en lugn tur innan de utforskar parker och närliggande cykelvägar.", "answer_raw": "Vår butik ligger nära strandpromenaden, Port Olímpic, Torre MAPFRE och Casino Barcelona, i ett område där många besökare börjar en lugn tur innan de utforskar parker och närliggande cykelvägar."} | True | True |
| sv | 4 | {"line": 925, "question": "Har ni cyklar för nybörjare eller barn?", "answer": "Ja. Vi kan hjälpa dig att välja en cykel som passar din längd och nivå, inklusive cyklar som passar barn.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Har ni cyklar för nybörjare eller barn?", "answer": "Ja. Vi kan hjälpa dig att välja en cykel som passar din längd och nivå, inklusive cyklar som passar barn.", "answer_raw": "Ja. Vi kan hjälpa dig att välja en cykel som passar din längd och nivå, inklusive cyklar som passar barn."} | True | True |
| sv | 5 | {"line": 929, "question": "Behöver jag körkort för att hyra en cykel?", "answer": "Nej. Inget körkort krävs för att hyra en cykel.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Behöver jag körkort för att hyra en cykel?", "answer": "Nej. Inget körkort krävs för att hyra en cykel.", "answer_raw": "Nej. Inget körkort krävs för att hyra en cykel."} | True | True |
| sv | 6 | {"line": 933, "question": "Kan jag lämna min väska eller mitt bagage i butiken?", "answer": "Ja. Vi erbjuder gratis förvaring för jackor, ryggsäckar och bagage i vår övervakade butik medan du cyklar.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Kan jag lämna min väska eller mitt bagage i butiken?", "answer": "Ja. Vi erbjuder gratis förvaring för jackor, ryggsäckar och bagage i vår övervakade butik medan du cyklar.", "answer_raw": "Ja. Vi erbjuder gratis förvaring för jackor, ryggsäckar och bagage i vår övervakade butik medan du cyklar."} | True | True |
| sv | 7 | {"line": 938, "question": "Kan jag boka eller ställa frågor via WhatsApp?", "answer": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan jag boka eller ställa frågor via WhatsApp?", "answer": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid.", "answer_raw": "Ja. Du kan skriva till oss på WhatsApp innan du kommer för att bekräfta tillgänglighet, ställa frågor eller ordna upphämtningstid."} | True | True |
| sv | 8 | {"line": 942, "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel.", "answer_raw": "Du kan boka via WhatsApp, e-post eller telefon. Kontakta oss om du vill bekräfta cykeltillgänglighet eller bästa tid för att hämta din cykel."} | True | True |
| pl | 1 | {"line": 972, "question": "Czy potrzebuję doświadczenia, aby wynająć rower?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy rowery początkującym i pewnym siebie rowerzystom, a nasz zespół pomoże wybrać wygodny rower na start.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Czy potrzebuję doświadczenia, aby wynająć rower?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy rowery początkującym i pewnym siebie rowerzystom, a nasz zespół pomoże wybrać wygodny rower na start.", "answer_raw": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Wynajmujemy rowery początkującym i pewnym siebie rowerzystom, a nasz zespół pomoże wybrać wygodny rower na start."} | True | True |
| pl | 2 | {"line": 976, "question": "Czy kask lub zapięcie są wliczone w wynajem?", "answer": "Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Czy kask lub zapięcie są wliczone w wynajem?", "answer": "Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach.", "answer_raw": "Tak. Kask dziecięcy i zapięcie są w cenie każdego wynajmu roweru. Opcjonalny fotelik dziecięcy jest dostępny w wybranych rowerach."} | True | True |
| pl | 3 | {"line": 980, "question": "Gdzie mogę jeździć rowerem blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym zwiedzaniem parków i pobliskich ścieżek rowerowych.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Gdzie mogę jeździć rowerem blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym zwiedzaniem parków i pobliskich ścieżek rowerowych.", "answer_raw": "Nasza wypożyczalnia znajduje się blisko nadmorskiej promenady, Port Olímpic i otwartych przestrzeni, gdzie wielu odwiedzających zaczyna spokojną jazdę przed dalszym zwiedzaniem parków i pobliskich ścieżek rowerowych."} | True | True |
| pl | 4 | {"line": 984, "question": "Czy macie rowery dla początkujących lub dzieci?", "answer": "Tak. Pomożemy dobrać rower do Twojego wzrostu i poziomu doświadczenia, także rowery odpowiednie dla dzieci.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Czy macie rowery dla początkujących lub dzieci?", "answer": "Tak. Pomożemy dobrać rower do Twojego wzrostu i poziomu doświadczenia, także rowery odpowiednie dla dzieci.", "answer_raw": "Tak. Pomożemy dobrać rower do Twojego wzrostu i poziomu doświadczenia, także rowery odpowiednie dla dzieci."} | True | True |
| pl | 5 | {"line": 988, "question": "Czy potrzebuję prawa jazdy, aby wynająć rower?", "answer": "Nie. Do wynajmu roweru nie jest wymagane prawo jazdy.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Czy potrzebuję prawa jazdy, aby wynająć rower?", "answer": "Nie. Do wynajmu roweru nie jest wymagane prawo jazdy.", "answer_raw": "Nie. Do wynajmu roweru nie jest wymagane prawo jazdy."} | True | True |
| pl | 6 | {"line": 992, "question": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "answer": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "answer": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni.", "answer_raw": "Tak. Podczas jazdy dostępne jest darmowe przechowanie kurtek, plecaków i bagażu w naszej nadzorowanej wypożyczalni."} | True | True |
| pl | 7 | {"line": 997, "question": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "answer": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "answer": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru.", "answer_raw": "Tak. Możesz napisać do nas na WhatsApp przed przyjazdem, aby potwierdzić dostępność, zadać pytania lub ustalić godzinę odbioru."} | True | True |
| pl | 8 | {"line": 1001, "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność roweru albo najlepszą godzinę odbioru.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność roweru albo najlepszą godzinę odbioru.", "answer_raw": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Skontaktuj się z nami, jeśli chcesz potwierdzić dostępność roweru albo najlepszą godzinę odbioru."} | True | True |

## T. MATRIZ RATING/REVIEWS

Rating canónico 4.6, 226 reseñas, escala 1–5. Los testimonios individuales pueden tener 5 estrellas sin contradecir la media. Se verifica presencia y correspondencia; autenticidad externa no verificada.

| Idioma | Comparación completa |
| --- | --- |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"My boyfriend and I rented a pair of skates and bike to go up the board walk and it was so fun! The owners were so sweet and helpful and the price was great! Very happy with this place and will come back.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-04-04"}, "line": 907, "visible_card": {"line": 907, "text": "★★★★★ “My boyfriend and I rented a pair of skates and bike to go up the board walk and it was so fun! The owners were so sweet and helpful and the price was great! Very happy with this place and will come back.” Bailey Brooke Google review · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Super. Affordable and good location, got a fixed bike that was patient enough to drive all over the city daily, even shoes have matched!😁\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2023-02-05"}, "line": 915, "visible_card": {"line": 915, "text": "★★★★★ “Super. Affordable and good location, got a fixed bike that was patient enough to drive all over the city daily, even shoes have matched!😁” Gvidas Gečas Google review · 2023-02-05", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Went here to rent bikes to stroll the beach path. Oscar was very friendly and to the point. Fast easy process for renting, no long forms or speeches. Good, fair price and you're on your way! Thank you, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2020-02-20"}, "line": 923, "visible_card": {"line": 923, "text": "★★★★★ “Went here to rent bikes to stroll the beach path. Oscar was very friendly and to the point. Fast easy process for renting, no long forms or speeches. Good, fair price and you're on your way! Thank you, Oscar.” Fabio Mendes Google review · 2020-02-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Alquilé una bici aquí y la verdad es que quedé muy contento. Los precios están muy bien comparados con otros sitios y las bicicletas están en buen estado. Además, la dueña es súper maja y el trato fue muy amable desde el primer momento, te explica todo con calma y te hace sentir a gusto. Sin duda es un sitio muy recomendable si necesitas alquilar una bici sin complicaciones y a buen precio. Volvería a alquilar aquí sin dudarlo.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 901, "visible_card": {"line": 901, "text": "★★★★★ “Alquilé una bici aquí y la verdad es que quedé muy contento. Los precios están muy bien comparados con otros sitios y las bicicletas están en buen estado. Además, la dueña es súper maja y el trato fue muy amable desde el primer momento, te explica todo con calma y te hace sentir a gusto. Sin duda es un sitio muy recomendable si necesitas alquilar una bici sin complicaciones y a buen precio. Volvería a alquilar aquí sin dudarlo.” Alfonso Arellano · Reseña de Google · 2026-03-13", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Me gustó mucho el trato, ya que la chica que nos atendió tenía un total conocimiento de Barcelona, nos dio muchos tips de que conocer y que lugares visitar Las bicicletas y patines , están en un buen estado y creo que el mantenimiento constante, hacen que está tienda tenga un material en excelentes condiciones Mil y mil gracias a Natalia por su servicio excelente Nos volveremos a ver muy pronto Super recomendable\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 902, "visible_card": {"line": 902, "text": "★★★★★ “Me gustó mucho el trato, ya que la chica que nos atendió tenía un total conocimiento de Barcelona, nos dio muchos tips de que conocer y que lugares visitar Las bicicletas y patines , están en un buen estado y creo que el mantenimiento constante, hacen que está tienda tenga un material en excelentes condiciones Mil y mil gracias a Natalia por su servicio excelente Nos volveremos a ver muy pronto Super recomendable” ectnes montano · Reseña de Google · 2025-04-02", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Me encanto la atención, muy amables. Pero sobre todo rentar una bici a un precio tan económico. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 903, "visible_card": {"line": 903, "text": "★★★★★ “Me encanto la atención, muy amables. Pero sobre todo rentar una bici a un precio tan económico. ❤️” Lourdes Arrastia · Reseña de Google · 2021-07-14", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai loué un vélo ici et j’en ai été vraiment très satisfait. Les prix sont très bons par rapport à d’autres endroits et les vélos sont en bon état. De plus, la propriétaire est très sympathique et l’accueil a été chaleureux dès le premier instant ; elle explique tout calmement et vous met à l’aise. C’est sans aucun doute un endroit très recommandable si vous avez besoin de louer un vélo facilement et à bon prix. J’y louerais de nouveau sans hésiter.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 828, "visible_card": {"line": 828, "text": "★★★★★ “J’ai loué un vélo ici et j’en ai été vraiment très satisfait. Les prix sont très bons par rapport à d’autres endroits et les vélos sont en bon état. De plus, la propriétaire est très sympathique et l’accueil a été chaleureux dès le premier instant ; elle explique tout calmement et vous met à l’aise. C’est sans aucun doute un endroit très recommandable si vous avez besoin de louer un vélo facilement et à bon prix. J’y louerais de nouveau sans hésiter.” Alfonso Arellano · Avis Google · 2026-03-13", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai beaucoup apprécié l’accueil, car la personne qui nous a aidés connaissait parfaitement Barcelone et nous a donné de nombreux conseils sur les lieux à découvrir et à visiter. Les vélos et les patins sont en bon état et je pense que l’entretien constant permet à cette boutique de proposer un matériel en excellent état. Mille mercis à Natalia pour son excellent service. Nous nous reverrons très bientôt. Je recommande vivement.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 829, "visible_card": {"line": 829, "text": "★★★★★ “J’ai beaucoup apprécié l’accueil, car la personne qui nous a aidés connaissait parfaitement Barcelone et nous a donné de nombreux conseils sur les lieux à découvrir et à visiter. Les vélos et les patins sont en bon état et je pense que l’entretien constant permet à cette boutique de proposer un matériel en excellent état. Mille mercis à Natalia pour son excellent service. Nous nous reverrons très bientôt. Je recommande vivement.” ectnes montano · Avis Google · 2025-04-02", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"J’ai adoré l’accueil, ils sont très aimables. Mais surtout, louer un vélo à un prix aussi économique. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 830, "visible_card": {"line": 830, "text": "★★★★★ “J’ai adoré l’accueil, ils sont très aimables. Mais surtout, louer un vélo à un prix aussi économique. ❤️” Lourdes Arrastia · Avis Google · 2021-07-14", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ho noleggiato una bicicletta qui e ne sono rimasto davvero molto soddisfatto. I prezzi sono molto buoni rispetto ad altri posti e le biciclette sono in buono stato. Inoltre, la proprietaria è molto simpatica e il trattamento è stato gentile fin dal primo momento; ti spiega tutto con calma e ti fa sentire a tuo agio. È senza dubbio un posto molto consigliato se hai bisogno di noleggiare una bicicletta senza complicazioni e a buon prezzo. Noleggerei di nuovo qui senza esitare.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 834, "visible_card": {"line": 834, "text": "★★★★★ “Ho noleggiato una bicicletta qui e ne sono rimasto davvero molto soddisfatto. I prezzi sono molto buoni rispetto ad altri posti e le biciclette sono in buono stato. Inoltre, la proprietaria è molto simpatica e il trattamento è stato gentile fin dal primo momento; ti spiega tutto con calma e ti fa sentire a tuo agio. È senza dubbio un posto molto consigliato se hai bisogno di noleggiare una bicicletta senza complicazioni e a buon prezzo. Noleggerei di nuovo qui senza esitare.” Alfonso Arellano · Recensione Google · 2026-03-13", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "ectnes montano"}, "datePublished": "2025-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mi è piaciuto molto il servizio, perché la ragazza che ci ha assistito conosceva perfettamente Barcellona e ci ha dato molti consigli su cosa vedere e quali luoghi visitare. Le biciclette e i pattini sono in buono stato e credo che la manutenzione costante permetta a questo negozio di avere materiale in condizioni eccellenti. Mille grazie a Natalia per il suo servizio eccellente. Ci rivedremo molto presto. Super consigliato.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 835, "visible_card": {"line": 835, "text": "★★★★★ “Mi è piaciuto molto il servizio, perché la ragazza che ci ha assistito conosceva perfettamente Barcellona e ci ha dato molti consigli su cosa vedere e quali luoghi visitare. Le biciclette e i pattini sono in buono stato e credo che la manutenzione costante permetta a questo negozio di avere materiale in condizioni eccellenti. Mille grazie a Natalia per il suo servizio eccellente. Ci rivedremo molto presto. Super consigliato.” ectnes montano · Recensione Google · 2025-04-02", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Lourdes Arrastia"}, "datePublished": "2021-07-14", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mi è piaciuta molto l’attenzione, sono stati molto gentili. Ma soprattutto poter noleggiare una bicicletta a un prezzo così conveniente. ❤️\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 836, "visible_card": {"line": 836, "text": "★★★★★ “Mi è piaciuta molto l’attenzione, sono stati molto gentili. Ma soprattutto poter noleggiare una bicicletta a un prezzo così conveniente. ❤️” Lourdes Arrastia · Recensione Google · 2021-07-14", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Mein Freund und ich haben ein Paar Skates und ein Fahrrad gemietet, um die Strandpromenade entlangzufahren, und es hat sehr viel Spaß gemacht! Die Besitzer waren sehr lieb und hilfsbereit, und der Preis war großartig! Wir sind mit diesem Ort sehr zufrieden und werden wiederkommen.“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 836, "visible_card": {"line": 836, "text": "★★★★★ „Mein Freund und ich haben ein Paar Skates und ein Fahrrad gemietet, um die Strandpromenade entlangzufahren, und es hat sehr viel Spaß gemacht! Die Besitzer waren sehr lieb und hilfsbereit, und der Preis war großartig! Wir sind mit diesem Ort sehr zufrieden und werden wiederkommen.“ Bailey Brooke Google-Bewertung · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Super. Günstig und gut gelegen; ich bekam ein repariertes Fahrrad, das geduldig genug war, um täglich durch die ganze Stadt zu fahren; sogar die Schuhe haben gepasst!😁“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 844, "visible_card": {"line": 844, "text": "★★★★★ „Super. Günstig und gut gelegen; ich bekam ein repariertes Fahrrad, das geduldig genug war, um täglich durch die ganze Stadt zu fahren; sogar die Schuhe haben gepasst!😁“ Gvidas Gečas Google-Bewertung · 2023-02-05", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Wir waren hier, um Fahrräder für eine Fahrt an der Strandpromenade zu mieten. Oscar war sehr freundlich und kam direkt auf den Punkt. Schneller, einfacher Mietvorgang, keine langen Formulare oder Erklärungen. Guter, fairer Preis, und schon kann es losgehen! Vielen Dank, Oscar.“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 852, "visible_card": {"line": 852, "text": "★★★★★ „Wir waren hier, um Fahrräder für eine Fahrt an der Strandpromenade zu mieten. Oscar war sehr freundlich und kam direkt auf den Punkt. Schneller, einfacher Mietvorgang, keine langen Formulare oder Erklärungen. Guter, fairer Preis, und schon kann es losgehen! Vielen Dank, Oscar.“ Fabio Mendes Google-Bewertung · 2020-02-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mijn vriend en ik huurden een paar skates en een fiets om over de boulevard te gaan en het was zo leuk! De eigenaren waren zo lief en behulpzaam en de prijs was geweldig! We zijn erg blij met deze plek en komen terug.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 844, "visible_card": {"line": 844, "text": "★★★★★ “Mijn vriend en ik huurden een paar skates en een fiets om over de boulevard te gaan en het was zo leuk! De eigenaren waren zo lief en behulpzaam en de prijs was geweldig! We zijn erg blij met deze plek en komen terug.” Bailey Brooke Google-review · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Super. Betaalbaar en goed gelegen; ik kreeg een gerepareerde fiets die geduldig genoeg was om dagelijks door de hele stad te rijden; zelfs de schoenen pasten!😁\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 852, "visible_card": {"line": 852, "text": "★★★★★ “Super. Betaalbaar en goed gelegen; ik kreeg een gerepareerde fiets die geduldig genoeg was om dagelijks door de hele stad te rijden; zelfs de schoenen pasten!😁” Gvidas Gečas Google-review · 2023-02-05", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"We kwamen hier om fietsen te huren voor een rit langs het strandpad. Oscar was erg vriendelijk en direct. Snel en eenvoudig huurproces, zonder lange formulieren of verhalen. Goede, eerlijke prijs en je kunt op weg! Bedankt, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 860, "visible_card": {"line": 860, "text": "★★★★★ “We kwamen hier om fietsen te huren voor een rit langs het strandpad. Oscar was erg vriendelijk en direct. Snel en eenvoudig huurproces, zonder lange formulieren of verhalen. Goede, eerlijke prijs en je kunt op weg! Bedankt, Oscar.” Fabio Mendes Google-review · 2020-02-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Eu e o meu namorado alugámos um par de patins e uma bicicleta para percorrer o passeio marítimo e foi muito divertido! Os proprietários foram muito queridos e prestáveis e o preço foi ótimo! Ficámos muito satisfeitos com este sítio e vamos voltar.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 849, "visible_card": {"line": 849, "text": "★★★★★ “Eu e o meu namorado alugámos um par de patins e uma bicicleta para percorrer o passeio marítimo e foi muito divertido! Os proprietários foram muito queridos e prestáveis e o preço foi ótimo! Ficámos muito satisfeitos com este sítio e vamos voltar.” Bailey Brooke Avaliação Google · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Gvidas Gečas"}, "datePublished": "2023-02-05", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Excelente. Acessível e bem localizado; deram-me uma bicicleta reparada que foi suficientemente paciente para percorrer toda a cidade diariamente; até os sapatos combinaram!😁\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 857, "visible_card": {"line": 857, "text": "★★★★★ “Excelente. Acessível e bem localizado; deram-me uma bicicleta reparada que foi suficientemente paciente para percorrer toda a cidade diariamente; até os sapatos combinaram!😁” Gvidas Gečas Avaliação Google · 2023-02-05", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "João Junior"}, "datePublished": "2021-04-21", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 865, "visible_card": {"line": 865, "text": "★★★★★ “[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲” João Junior Avaliação Google · 2021-04-21", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"El meu xicot i jo vam llogar uns patins i una bicicleta per recórrer el passeig marítim i va ser molt divertit! Els propietaris van ser molt amables i servicials i el preu va ser fantàstic! Estem molt contents amb aquest lloc i hi tornarem.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 834, "visible_card": {"line": 834, "text": "★★★★★ “El meu xicot i jo vam llogar uns patins i una bicicleta per recórrer el passeig marítim i va ser molt divertit! Els propietaris van ser molt amables i servicials i el preu va ser fantàstic! Estem molt contents amb aquest lloc i hi tornarem.” Bailey Brooke Ressenya de Google · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marta"}, "datePublished": "2021-04-02", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ideal per llogar bicis i fer un passeig per la platja. Personal molt amable i molt bon preu.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 842, "visible_card": {"line": 842, "text": "★★★★★ “Ideal per llogar bicis i fer un passeig per la platja. Personal molt amable i molt bon preu.” Marta Ressenya de Google · 2021-04-02", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Roex Info"}, "datePublished": "2018-12-28", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Es molt bona empressa de Lloguer de biciletes, el tracta es molt bó al igual que la qualitat del material que llogues. Recomanable 100% :)\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 850, "visible_card": {"line": 850, "text": "★★★★★ “Es molt bona empressa de Lloguer de biciletes, el tracta es molt bó al igual que la qualitat del material que llogues. Recomanable 100% :)” Roex Info Ressenya de Google · 2018-12-28", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Min pojkvän och jag hyrde ett par rullskridskor och en cykel för att ta oss längs strandpromenaden, och det var så roligt! Ägarna var mycket vänliga och hjälpsamma och priset var toppen! Vi är mycket nöjda med stället och kommer tillbaka.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 846, "visible_card": {"line": 846, "text": "★★★★★ “Min pojkvän och jag hyrde ett par rullskridskor och en cykel för att ta oss längs strandpromenaden, och det var så roligt! Ägarna var mycket vänliga och hjälpsamma och priset var toppen! Vi är mycket nöjda med stället och kommer tillbaka.” Bailey Brooke Google-recension · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Jag hyrde en cykel här och blev verkligen mycket nöjd. Priserna är mycket bra jämfört med andra ställen och cyklarna är i gott skick. Dessutom är ägaren mycket trevlig och bemötandet var vänligt från första stund; hon förklarar allt lugnt och får dig att känna dig bekväm. Det är utan tvekan ett ställe jag rekommenderar om du behöver hyra en cykel enkelt och till ett bra pris. Jag skulle hyra här igen utan att tveka.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 854, "visible_card": {"line": 854, "text": "★★★★★ “Jag hyrde en cykel här och blev verkligen mycket nöjd. Priserna är mycket bra jämfört med andra ställen och cyklarna är i gott skick. Dessutom är ägaren mycket trevlig och bemötandet var vänligt från första stund; hon förklarar allt lugnt och får dig att känna dig bekväm. Det är utan tvekan ett ställe jag rekommenderar om du behöver hyra en cykel enkelt och till ett bra pris. Jag skulle hyra här igen utan att tveka.” Alfonso Arellano Google-recension · 2026-03-13", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Jag gick hit för att hyra cyklar och cykla längs strandvägen. Oscar var mycket vänlig och saklig. Uthyrningen gick snabbt och enkelt, utan långa formulär eller genomgångar. Ett bra och rättvist pris, sedan är det bara att ge sig av! Tack, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 862, "visible_card": {"line": 862, "text": "★★★★★ “Jag gick hit för att hyra cyklar och cykla längs strandvägen. Oscar var mycket vänlig och saklig. Uthyrningen gick snabbt och enkelt, utan långa formulär eller genomgångar. Ett bra och rättvist pris, sedan är det bara att ge sig av! Tack, Oscar.” Fabio Mendes Google-recension · 2020-02-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Bailey Brooke"}, "datePublished": "2026-04-04", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mój chłopak i ja wynajęliśmy parę rolek i rower, aby przejechać się promenadą, i świetnie się bawiliśmy! Właściciele byli bardzo mili i pomocni, a cena była świetna! Jesteśmy bardzo zadowoleni z tego miejsca i wrócimy.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 905, "visible_card": {"line": 905, "text": "★★★★★ “Mój chłopak i ja wynajęliśmy parę rolek i rower, aby przejechać się promenadą, i świetnie się bawiliśmy! Właściciele byli bardzo mili i pomocni, a cena była świetna! Jesteśmy bardzo zadowoleni z tego miejsca i wrócimy.” Bailey Brooke Opinia Google · 2026-04-04", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Alfonso Arellano"}, "datePublished": "2026-03-13", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Wynająłem tutaj rower i byłem naprawdę bardzo zadowolony. Ceny są bardzo dobre w porównaniu z innymi miejscami, a rowery są w dobrym stanie. Właścicielka jest bardzo sympatyczna i od pierwszej chwili traktuje klientów życzliwie; wszystko spokojnie wyjaśnia i sprawia, że czujesz się swobodnie. Zdecydowanie polecam to miejsce, jeśli potrzebujesz bezproblemowo wynająć rower w dobrej cenie. Bez wahania wynająłbym tutaj ponownie.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 913, "visible_card": {"line": 913, "text": "★★★★★ “Wynająłem tutaj rower i byłem naprawdę bardzo zadowolony. Ceny są bardzo dobre w porównaniu z innymi miejscami, a rowery są w dobrym stanie. Właścicielka jest bardzo sympatyczna i od pierwszej chwili traktuje klientów życzliwie; wszystko spokojnie wyjaśnia i sprawia, że czujesz się swobodnie. Zdecydowanie polecam to miejsce, jeśli potrzebujesz bezproblemowo wynająć rower w dobrej cenie. Bez wahania wynająłbym tutaj ponownie.” Alfonso Arellano Opinia Google · 2026-03-13", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/bike/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Fabio Mendes"}, "datePublished": "2020-02-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Przyszedłem tutaj wynająć rowery na przejażdżkę ścieżką przy plaży. Oscar był bardzo miły i konkretny. Wynajem przebiegł szybko i łatwo, bez długich formularzy ani przemówień. Dobra, uczciwa cena i można ruszać! Dziękuję, Oscar.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 921, "visible_card": {"line": 921, "text": "★★★★★ “Przyszedłem tutaj wynająć rowery na przejażdżkę ścieżką przy plaży. Oscar był bardzo miły i konkretny. Wynajem przebiegł szybko i łatwo, bez długich formularzy ani przemówień. Dobra, uczciwa cena i można ruszać! Dziękuję, Oscar.” Fabio Mendes Opinia Google · 2020-02-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |

## U. MATRIZ ESTRUCTURA HTML/ARTICLE

| Idioma | Conteos fuente/token/DOM | Errores token | Pila sin cerrar | IDs duplicados |
| --- | --- | --- | --- | --- |
| en | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| es | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| fr | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| it | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| de | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| nl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pt | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| ca | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| sv | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 2, "text_close": 2, "token_open": 2, "token_close": 2, "parsed": 2}, "section": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "article": {"text_open": 17, "text_close": 17, "token_open": 17, "token_close": 17, "parsed": 17}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |

## V. MATRIZ ENLACES INTERNOS/SELECTOR IDIOMAS

| Idioma | Selectores | Referencias ID | Controles / formularios |
| --- | --- | --- | --- |
| en | [{"line": 682, "id": null, "links": [{"line": 683, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 683, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 683, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 683, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 683, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 683, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 683, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 683, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 683, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 683, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 701, "id": null, "links": [{"line": 702, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 702, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 702, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 702, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 702, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 702, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 702, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 702, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 702, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 702, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 730, "attribute": "aria-labelledby", "ref": "bike-business-facts-title", "exists": true}, {"line": 899, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 967, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 1009, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 677, "text": "Language", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 697, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 704, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Toggle menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 975, "text": "Do I need experience to rent a bike?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 979, "text": "Is a helmet or lock included with the rental?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 983, "text": "Where can I ride a bike near the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 987, "text": "Do you have bikes for beginners or kids?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 991, "text": "Do I need a licence to rent a bike?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 995, "text": "Can I store my bag or luggage at the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 999, "text": "Can I book or ask questions by WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 1003, "text": "How do I book or contact you?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| es | [{"line": 676, "id": null, "links": [{"line": 677, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 677, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 677, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 677, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 677, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 677, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 677, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 677, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 677, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 677, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 695, "id": null, "links": [{"line": 696, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 696, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 696, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 696, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 696, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 696, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 696, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 696, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 696, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 696, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 724, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-es", "exists": true}, {"line": 940, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 982, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 671, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 691, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 698, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 948, "text": "¿Necesito experiencia para alquilar una bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 952, "text": "¿Se incluye casco o candado con el alquiler?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 956, "text": "¿Dónde puedo montar en bicicleta cerca de la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 960, "text": "¿Tenéis bicicletas para principiantes o para niños?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 964, "text": "¿Necesito licencia para alquilar una bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 968, "text": "¿Puedo guardar mi bolsa o equipaje en la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 972, "text": "¿Puedo reservar o preguntar por WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 976, "text": "¿Cómo reservo o cómo contacto con vosotros?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| fr | [{"line": 606, "id": null, "links": [{"line": 607, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 607, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 607, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 607, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 607, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 607, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 607, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 607, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 607, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 607, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 625, "id": null, "links": [{"line": 626, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 626, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 626, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 626, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 626, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 626, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 626, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 626, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 626, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 626, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 653, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-fr", "exists": true}, {"line": 867, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 909, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 601, "text": "Langue", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 621, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 628, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Ouvrir le menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 875, "text": "Ai-je besoin d’expérience pour louer un vélo ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 879, "text": "Le casque ou l’antivol sont-ils inclus avec la location ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 883, "text": "Où puis-je rouler à vélo près de la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 887, "text": "Avez-vous des vélos pour débutants ou pour enfants ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 891, "text": "Ai-je besoin d’un permis pour louer un vélo ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 895, "text": "Puis-je laisser mon sac ou mes bagages à la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 899, "text": "Puis-je réserver ou poser des questions par WhatsApp ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 903, "text": "Comment réserver ou vous contacter ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| it | [{"line": 609, "id": null, "links": [{"line": 610, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 610, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 610, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 610, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 610, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 610, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 610, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 610, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 610, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 610, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 628, "id": null, "links": [{"line": 629, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 629, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 629, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 629, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 629, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 629, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 629, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 629, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 629, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 629, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 659, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-it", "exists": true}, {"line": 873, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 915, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 604, "text": "Lingua", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiare lingua", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 624, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiare lingua", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 631, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Apri il menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 881, "text": "Ho bisogno di esperienza per noleggiare una bicicletta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 885, "text": "Il casco o il lucchetto sono inclusi nel noleggio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 889, "text": "Dove posso andare in bici vicino al negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 893, "text": "Avete biciclette per principianti o per bambini?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 897, "text": "Ho bisogno della patente per noleggiare una bicicletta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 901, "text": "Posso lasciare la mia borsa o i bagagli in negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 905, "text": "Posso prenotare o fare domande via WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 909, "text": "Come posso prenotare o contattarvi?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| de | [{"line": 614, "id": null, "links": [{"line": 615, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 615, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 615, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 615, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 615, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 615, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 615, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 615, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 615, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 615, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 633, "id": null, "links": [{"line": 634, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 634, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 634, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 634, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 634, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 634, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 634, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 634, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 634, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 634, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 661, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-de", "exists": true}, {"line": 829, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 896, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 955, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 609, "text": "Sprache", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 629, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 636, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menü öffnen", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 905, "text": "Brauche ich Erfahrung, um ein Fahrrad zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 911, "text": "Sind Helm oder Schloss in der Miete enthalten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 917, "text": "Wo kann ich in der Nähe des Shops Fahrrad fahren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 923, "text": "Gibt es Fahrräder für Anfänger oder Kinder?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 929, "text": "Brauche ich einen Führerschein, um ein Fahrrad zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 935, "text": "Kann ich meine Tasche oder mein Gepäck im Shop lassen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 942, "text": "Kann ich per WhatsApp buchen oder Fragen stellen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 948, "text": "Wie kann ich buchen oder Kontakt aufnehmen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| nl | [{"line": 622, "id": null, "links": [{"line": 623, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 623, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 623, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 623, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 623, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 623, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 623, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 623, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 623, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 623, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 641, "id": null, "links": [{"line": 642, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 642, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 642, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 642, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 642, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 642, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 642, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 642, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 642, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 642, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 669, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-nl", "exists": true}, {"line": 837, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 904, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 963, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 617, "text": "Taal", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 637, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 644, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menu openen", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 913, "text": "Heb ik ervaring nodig om een fiets te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 919, "text": "Zijn een helm of slot inbegrepen bij de huur?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 925, "text": "Waar kan ik fietsen in de buurt van de winkel?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 931, "text": "Hebben jullie fietsen voor beginners of kinderen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 937, "text": "Heb ik een rijbewijs nodig om een fiets te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 943, "text": "Kan ik mijn tas of bagage in de winkel achterlaten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 950, "text": "Kan ik via WhatsApp reserveren of vragen stellen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 956, "text": "Hoe reserveer ik of neem ik contact met jullie op?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pt | [{"line": 625, "id": null, "links": [{"line": 626, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 626, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 626, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 626, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 626, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 626, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 626, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 626, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 626, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 626, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 644, "id": null, "links": [{"line": 645, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 645, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 645, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 645, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 645, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 645, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 645, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 645, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 645, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 645, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 675, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-pt", "exists": true}, {"line": 842, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 909, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 951, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 620, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 640, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 647, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 917, "text": "Preciso de experiência para alugar uma bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 921, "text": "O capacete ou o cadeado estão incluídos no aluguer?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 925, "text": "Onde posso andar de bicicleta perto da loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 929, "text": "Têm bicicletas para principiantes ou para crianças?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 933, "text": "Preciso de carta de condução para alugar uma bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 937, "text": "Posso guardar a minha mala ou bagagem na loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 941, "text": "Posso reservar ou fazer perguntas por WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 945, "text": "Como reservo ou como vos contacto?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| ca | [{"line": 609, "id": null, "links": [{"line": 610, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 610, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 610, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 610, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 610, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 610, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 610, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 610, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 610, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 610, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 628, "id": null, "links": [{"line": 629, "text": "en English", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 629, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 629, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 629, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 629, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 629, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 629, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 629, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 629, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 629, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 659, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-cat", "exists": true}, {"line": 827, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 894, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 936, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 604, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 624, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 631, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Obrir menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 902, "text": "Necessito experiència per llogar una bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 906, "text": "S’inclou casc o cadenat amb el lloguer?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 910, "text": "On puc anar amb bicicleta a prop de la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 914, "text": "Teniu bicicletes per a principiants o per a nens?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 918, "text": "Necessito carnet per llogar una bicicleta?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 922, "text": "Puc guardar la meva bossa o equipatge a la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 926, "text": "Puc reservar o fer preguntes per WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 930, "text": "Com reservo o com us contacto?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| sv | [{"line": 623, "id": null, "links": [{"line": 624, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 624, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 624, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 624, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 624, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 624, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 624, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 624, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 624, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 624, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 642, "id": null, "links": [{"line": 643, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 643, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 643, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 643, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 643, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 643, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 643, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 643, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 643, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 643, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 671, "attribute": "aria-labelledby", "ref": "bike-business-facts-title-sv", "exists": true}, {"line": 839, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 906, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 949, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 618, "text": "Språk", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 638, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 645, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Öppna meny", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 914, "text": "Behöver jag erfarenhet för att hyra en cykel?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 918, "text": "Ingår hjälm eller lås i hyran?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 922, "text": "Var kan jag cykla nära butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 926, "text": "Har ni cyklar för nybörjare eller barn?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 930, "text": "Behöver jag körkort för att hyra en cykel?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 934, "text": "Kan jag lämna min väska eller mitt bagage i butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 939, "text": "Kan jag boka eller ställa frågor via WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 943, "text": "Hur bokar jag eller kontaktar er?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pl | [{"line": 682, "id": null, "links": [{"line": 683, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 683, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 683, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 683, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 683, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 683, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 683, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 683, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 683, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 683, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}, {"line": 701, "id": null, "links": [{"line": 702, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/bike/", "role": "menuitem"}}, {"line": 702, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/bike/", "role": "menuitem"}}, {"line": 702, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/bike/", "role": "menuitem"}}, {"line": 702, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/bike/", "role": "menuitem"}}, {"line": 702, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/bike/", "role": "menuitem"}}, {"line": 702, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/bike/", "role": "menuitem"}}, {"line": 702, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/bike/", "role": "menuitem"}}, {"line": 702, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/bike/", "role": "menuitem"}}, {"line": 702, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/bike/", "role": "menuitem"}}, {"line": 702, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/bike/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/bike/", "role": "menuitem"}}], "selected": []}] | [{"line": 730, "attribute": "aria-labelledby", "ref": "bike-business-facts-title", "exists": true}, {"line": 898, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 965, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 1008, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 677, "text": "Język", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 697, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 704, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Przełącz menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 973, "text": "Czy potrzebuję doświadczenia, aby wynająć rower?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 977, "text": "Czy kask lub zapięcie są wliczone w wynajem?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 981, "text": "Gdzie mogę jeździć rowerem blisko wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 985, "text": "Czy macie rowery dla początkujących lub dzieci?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 989, "text": "Czy potrzebuję prawa jazdy, aby wynająć rower?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 993, "text": "Czy mogę zostawić torbę lub bagaż w wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 998, "text": "Czy mogę zarezerwować lub zadać pytania przez WhatsApp?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 1002, "text": "Jak mogę zarezerwować lub skontaktować się z wami?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |

Los 12.046 enlaces internos de los 200 HTML apuntan al corpus incluido y todas las anclas locales se resuelven. No se han solicitado respuestas HTTP. La marca estática de idioma activo es una mejora.

## W. MATRIZ GLOBAL POR IDIOMA

| Idioma | Primera pasada | Segunda pasada independiente | Comprobaciones de página |
| --- | --- | --- | --- |
| en | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/bike/", "expected_page": "https://rentalscooterbarcelona.com/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "en", "expected": "en", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/bike/", "pass": true}] |
| es | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/es/bike/", "expected_page": "https://rentalscooterbarcelona.com/es/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "es", "expected": "es", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/bike/", "pass": true}] |
| fr | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/fr/bike/", "expected_page": "https://rentalscooterbarcelona.com/fr/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "fr", "expected": "fr", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/bike/", "pass": true}] |
| it | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/it/bike/", "expected_page": "https://rentalscooterbarcelona.com/it/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "it", "expected": "it", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/bike/", "pass": true}] |
| de | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/de/bike/", "expected_page": "https://rentalscooterbarcelona.com/de/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "de", "expected": "de", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/bike/", "pass": true}] |
| nl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/nl/bike/", "expected_page": "https://rentalscooterbarcelona.com/nl/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "nl", "expected": "nl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/bike/", "pass": true}] |
| pt | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pt/bike/", "expected_page": "https://rentalscooterbarcelona.com/pt/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pt-PT", "expected": "pt-PT", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/bike/", "pass": true}] |
| ca | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/cat/bike/", "expected_page": "https://rentalscooterbarcelona.com/cat/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "ca", "expected": "ca", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/bike/", "pass": true}] |
| sv | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/sv/bike/", "expected_page": "https://rentalscooterbarcelona.com/sv/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "sv", "expected": "sv", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/bike/", "pass": true}] |
| pl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pl/bike/", "expected_page": "https://rentalscooterbarcelona.com/pl/bike/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pl", "expected": "pl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/bike/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/bike/", "pass": true}] |

## LISTA FINAL DE CAMBIOS PROPUESTOS

| Punto | Idioma | Prioridad | Elemento | Propuesta |
| --- | --- | --- | --- | --- |
| U03 | ca | 2 | https://rentalscooterbarcelona.com/cat/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | de | 2 | https://rentalscooterbarcelona.com/de/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | en | 2 | https://rentalscooterbarcelona.com/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | es | 2 | https://rentalscooterbarcelona.com/es/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | fr | 2 | https://rentalscooterbarcelona.com/fr/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | it | 2 | https://rentalscooterbarcelona.com/it/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | nl | 2 | https://rentalscooterbarcelona.com/nl/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pl | 2 | https://rentalscooterbarcelona.com/pl/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pt | 2 | https://rentalscooterbarcelona.com/pt/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | sv | 2 | https://rentalscooterbarcelona.com/sv/bike/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |

## CONTROL FINAL

Integridad SHA-256 comprobada contra cada entrada ZIP. Las evidencias contienen valores y líneas por archivo. No se han modificado HTML ni aplicado correcciones. Imágenes y tamaños quedan pendientes; no se ha certificado renderizado, entrega de formularios, indexación ni disponibilidad remota.
