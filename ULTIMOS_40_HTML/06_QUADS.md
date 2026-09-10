# Auditoría HTML — 06_QUADS

2026-09-09. Diez idiomas. Fuente: ZIP adjunto y CANONICAL.md. HTML original sin modificar.

## A. INVENTARIO DE ARCHIVOS

| Idioma | Archivo original | Bytes | Líneas | SHA-256 |
| --- | --- | --- | --- | --- |
| en | quads/index.html | 72965 | 1092 | 6ebbb73492ab2876c8e8cf5d271e542ba3e05b085a1b7f0ba09972e81fa6ea97 |
| es | es/quads/index.html | 74735 | 1080 | 7a6bdc7d08c23b0c3eb3bf3f91f1fb765fef4a3fcc47516c224f74ecbbb5f6f9 |
| fr | fr/quads/index.html | 73662 | 1012 | e8d74c123392391a528275f54a963f658b45560f4ba2a44b41a6786c719dcd7e |
| it | it/quads/index.html | 73168 | 1021 | 0431231ef07ec79afd7ea6ccefea3a4b148b3fd284047c8df344692970322a2c |
| de | de/quads/index.html | 73642 | 1043 | 34328ba3a6d728b9c6a68695a05a02eb3e4189f9a4d8842c227592d1171401e4 |
| nl | nl/quads/index.html | 72682 | 1052 | 3ace9b352b7b8a24d2a416686ee0e9c95f89ed394dba70460dac74863bc9f2b0 |
| pt | pt/quads/index.html | 74124 | 1044 | 6d04a97f454a528af2e1d77e37961146727f86cee1972ed0c0cccf8beb99a902 |
| ca | cat/quads/index.html | 73674 | 1028 | da2ab52cbf9ea781e1b3bb0eb3e25a46004df96b8d87af9b0852fe814fbad1ce |
| sv | sv/quads/index.html | 72435 | 1038 | e9d936b8674959f677d78d3709e4ad3194e32d893e205e41070b1c4213a96179 |
| pl | pl/quads/index.html | 73712 | 1092 | d27e826fd8db73f0b14b8013a886167176ca2c4673a520af6789fe677632606e |

## B. MÉTODOS REALMENTE EJECUTADOS

Lectura completa de 10 fuentes, tokenización HTML, parser lxml, análisis de todos los JSON-LD, extracción del head, entidades, precios, FAQ, reseñas, políticas y enlaces. Segunda pasada independiente directamente sobre los ZIP originales: 23 controles por HTML. Comprobación de sintaxis del JavaScript inline, sin ejecutarlo. Cruce de tarifas con PRICES y de enlaces con los 200 HTML. Inspección de párrafos de guía DE/NL. Sin acceso al sitio publicado, validación externa de normativa o ejecución de recursos remotos.

## C. RESULTADO GLOBAL

| Idioma | Errores confirmados | Segunda pasada: controles superados |
| --- | --- | --- |
| en | U03 | 22/23 |
| es | U03 | 22/23 |
| fr | U03 | 22/23 |
| it | U03 | 22/23 |
| de | U03, U05 | 22/23 |
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

**Elemento:** https://rentalscooterbarcelona.com/cat/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 151 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 518 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### de

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/de/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 152 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 526 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### en

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 184 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 591 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### es

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/es/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 180 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 585 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### fr

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/fr/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 151 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 519 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### it

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/it/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 151 del HTML original:

```html
"dateModified": "2026-07-30"
```

Línea 518 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### nl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/nl/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 164 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 535 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pl

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pl/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 184 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 591 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### pt

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/pt/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 164 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 535 del HTML original:

```html
"dateModified": "2026-08-24"
```

#### sv

### U03 · Prioridad 2 · MEDIO

Dos dateModified para la misma WebPage

**Elemento:** https://rentalscooterbarcelona.com/sv/quads/#webpage.dateModified

**Actual:** 2026-07-30 / 2026-08-24

**Corrección propuesta:** Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.

**Motivo:** Dos valores de dateModified para la misma entidad WebPage.

**Impacto:** Ambigüedad temporal del grafo; el JSON sigue siendo válido.

**Estado:** FECHA REAL PENDIENTE. Consolidar la propiedad en los dos bloques; fecha real pendiente.

Línea 164 del HTML original:

```html
"dateModified": "2026-07-30",
```

Línea 535 del HTML original:

```html
"dateModified": "2026-08-24"
```

## G. ERRORES BAJOS

#### de

### U05 · Prioridad 3 · BAJO

Falta el infinitivo en el enlace a la guía, DE/NL

**Elemento:** Párrafo de enlace a la guía

**Actual:** Geöffnet von 10:30–13:30 und 16:30–20:00 Uhr. Wir bieten stunden- und tageweise Vermietung. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren Guide zum Rollschuhe mieten in Barcelona.

**Corrección propuesta:** Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren &lt;a href="https://rentalscooterbarcelona.com/de/blog/roller-skates/"&gt;Guide zum Rollschuhe mieten in Barcelona&lt;/a&gt; lesen.&lt;/p&gt;

**Motivo:** La construcción modal queda sin infinitivo final.

**Impacto:** Frase incompleta en alemán/neerlandés.

**Estado:** CORRECCIÓN DEFINIDA. Una inserción de lesen al final del enlace; conservar URL.

Línea 809 del HTML original:

```html
Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren <a href="https://rentalscooterbarcelona.com/de/blog/roller-skates/">Guide zum Rollschuhe mieten in Barcelona</a>.</p>
```

## H. INCOHERENCIAS QUE REQUIEREN FUENTE CANÓNICA

U03: fecha de modificación real por idioma. Los dos valores están documentados; CANONICAL no permite elegir uno.

Los datos de identidad, dirección, horario, mapas y equipamiento ya están definidos: no requieren nueva confirmación. Las tarifas y tallas documentadas no equivalen a una certificación externa de vigencia.

## I. MEJORAS RECOMENDADAS

# Mejoras opcionales — 06_QUADS

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
<title>Roller Skate Rental Barcelona | Quad &amp; Classic Skates | RSB</title>
<meta content="Rent classic quad roller skates in Barcelona near Port Olímpic and Barceloneta. Kids' helmet and protective pads included, plus free luggage storage." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Roller Skate Rental Barcelona | Quad &amp; Classic Skates | RSB" property="og:title"/>
<meta content="Rent classic quad roller skates in Barcelona near Port Olímpic and Barceloneta. Kids' helmet and protective pads included, plus free luggage storage." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Roller skate rental in Barcelona near Vila Olímpica del Poblenou and Barceloneta Beach" property="og:image:alt"/>
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
<meta content="Roller Skate Rental Barcelona | Quad &amp; Classic Skates | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Rent classic quad roller skates in Barcelona near Port Olímpic and Barceloneta. Kids' helmet and protective pads included, plus free luggage storage." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Roller skate rental in Barcelona near Vila Olímpica del Poblenou and Barceloneta Beach" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "@id": "https://rentalscooterbarcelona.com/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/quads/",
      "name": "Roller Skate Rental Barcelona | Quad & Classic Skates | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "en",
      "description": "Rent classic quad roller skates in Barcelona near Port Olímpic and Barceloneta. Kids' helmet and protective pads included, plus free luggage storage.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/quads/#faq"
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
      "@id": "https://rentalscooterbarcelona.com/quads/#breadcrumb",
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
          "name": "Roller skate rental",
          "item": "https://rentalscooterbarcelona.com/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/quads/#service",
      "serviceType": "Roller skates, quad skates and classic skates rental",
      "name": "Roller skate rental in Barcelona",
      "url": "https://rentalscooterbarcelona.com/quads/",
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
      "description": "Rent roller skates and quad skates in Barcelona near Port Olímpic and Barceloneta. Children's helmet, wrist guards, knee pads and elbow pads included, free luggage storage and local tips.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Roller skate rental price range",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Roller skate rental 1 hour",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Roller skate rental 2 hours",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Roller skate rental 3 hours",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Roller skate rental full day",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Roller skate rental 24 hours",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Roller skate rental extra day",
          "url": "https://rentalscooterbarcelona.com/quads/",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Do I need experience to rent roller skates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start."
          }
        },
        {
          "@type": "Question",
          "name": "Is protective gear included with the rental?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost."
          }
        },
        {
          "@type": "Question",
          "name": "Where can I roller skate near the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our rental shop is just steps from the seafront promenade and Port Olímpic. The flat coastal paths and Ciutadella Park offer good routes for relaxed roller skating near our store."
          }
        },
        {
          "@type": "Question",
          "name": "What sizes are available?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit."
          }
        },
        {
          "@type": "Question",
          "name": "Can teenagers rent roller skates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need a licence to rent roller skates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID."
          }
        },
        {
          "@type": "Question",
          "name": "Can I store my shoes or luggage at the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Free storage for shoes, jackets, handbags, backpacks and suitcases is available in our supervised shop during your rental."
          }
        },
        {
          "@type": "Question",
          "name": "How do I book or contact you?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability."
          }
        }
      ],
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Great place to rent skates in Barcelona. We rented both inline skates (rollerblades) and classic 4-wheel roller skates. Everything was in good condition, the staff was helpful and the location near the beach is perfect for skating. Highly recommended if you're looking for inline skate or roller skate rental in Barcelona.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2026-08-10"
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
<title>Alquiler de patines de 4 ruedas en Barcelona | RSB</title>
<meta name="description" content="Alquila patines clásicos de 4 ruedas en Barcelona, cerca de Port Olímpic y Barceloneta. Casco infantil, protecciones y consigna gratuita incluidas.">
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/es/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta property="og:title" content="Alquiler de patines de 4 ruedas en Barcelona | Patines clásicos | RSB">
<meta property="og:description" content="Alquila patines clásicos de 4 ruedas en Barcelona, cerca de Port Olímpic y Barceloneta. Casco infantil, protecciones y consigna gratuita incluidas.">
<meta content="https://rentalscooterbarcelona.com/es/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Alquiler de patines de 4 ruedas en Barcelona cerca de Vila Olímpica del Poblenou y la playa de la Barceloneta" property="og:image:alt"/>
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
<meta name="twitter:title" content="Alquiler de patines de 4 ruedas en Barcelona | Patines clásicos | RSB">
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta name="twitter:description" content="Alquila patines clásicos de 4 ruedas en Barcelona, cerca de Port Olímpic y Barceloneta. Casco infantil, protecciones y consigna gratuita incluidas.">
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Alquiler de patines de 4 ruedas en Barcelona cerca de Vila Olímpica del Poblenou y la playa de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, patines de 4 ruedas, bicicletas, skateboards y longboards cerca del Port Olímpic y la playa de la Barceloneta. Consigna gratuita, recomendaciones de rutas y atención local.",
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
      "@id": "https://rentalscooterbarcelona.com/es/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/es/quads/",
      "name": "Alquiler de patines de 4 ruedas en Barcelona | Patines clásicos | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Alquila patines clásicos de 4 ruedas en Barcelona, cerca de Port Olímpic y Barceloneta. Casco infantil, protecciones y consigna gratuita incluidas.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/es/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "inLanguage": "es",
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
      "@id": "https://rentalscooterbarcelona.com/es/quads/#breadcrumb",
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
          "name": "Alquiler de patines de 4 ruedas",
          "item": "https://rentalscooterbarcelona.com/es/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, patines de 4 ruedas, bicicletas, skateboards y longboards cerca del Port Olímpic y la playa de la Barceloneta. Consigna gratuita, recomendaciones de rutas y atención local.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/es/quads/#service",
      "serviceType": "Alquiler de patines de 4 ruedas y patines clásicos",
      "name": "Alquiler de patines de 4 ruedas en Barcelona",
      "url": "https://rentalscooterbarcelona.com/es/quads/",
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
      "description": "Alquila patines de 4 ruedas y patines clásicos en Barcelona cerca del Port Olímpic y la playa de la Barceloneta. Nuestra tienda en Vila Olímpica del Poblenou ofrece patines tradicionales para niños mayores, adolescentes y adultos, casco infantil, muñequeras, rodilleras y coderas incluidas, consigna gratuita y tallas UE 35–42.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Rango de precios del alquiler de patines de 4 ruedas",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Alquiler de patines de 4 ruedas 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Alquiler de patines de 4 ruedas 2 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Alquiler de patines de 4 ruedas 3 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Alquiler de patines de 4 ruedas día completo",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Alquiler de patines de 4 ruedas 24 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Alquiler de patines de 4 ruedas día extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/es/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/es/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Necesito experiencia para alquilar patines?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar."
          }
        },
        {
          "@type": "Question",
          "name": "¿Está incluido el equipo de protección?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines."
          }
        },
        {
          "@type": "Question",
          "name": "¿Dónde puedo patinar cerca de la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nuestra tienda está a pocos pasos del paseo marítimo y del Port Olímpic. Los caminos llanos de la costa y el Parc de la Ciutadella ofrecen buenas rutas para patinar con calma cerca de la tienda."
          }
        },
        {
          "@type": "Question",
          "name": "¿Qué tallas hay disponibles?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda."
          }
        },
        {
          "@type": "Question",
          "name": "¿Pueden alquilar patines los adolescentes?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42."
          }
        },
        {
          "@type": "Question",
          "name": "¿Necesito carnet para alquilar patines?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido."
          }
        },
        {
          "@type": "Question",
          "name": "¿Puedo dejar mis zapatos o maletas en la tienda?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Tenemos consigna gratuita para zapatos, chaquetas, bolsos, mochilas y maletas en nuestra tienda supervisada durante el alquiler."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cómo reservo o contacto con vosotros?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad."
          }
        }
      ],
      "inLanguage": "es"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/es/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/es/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/es/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Sonia"
      },
      "datePublished": "2026-05-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Alquilamos patines en línea en Barcelona en nuestras vacaciones,, tambien tienen patines de 4 ruedas, esta situada en la Vila Olimpica, al lado del paseo maritimo ycerca de la Barceloneta. Buen precio y una atenci¡on genial, lo recomiendo .100x100\"",
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
<title>Location de Patins à Roulettes Barcelone | Rollers Quad | RSB</title>
<meta content="Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/fr/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Location de Patins à Roulettes Barcelone | Rollers Quad | RSB" property="og:title"/>
<meta content="Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/fr/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Location de patins à roulettes à Barcelone près de Vila Olímpica del Poblenou et de la plage de la Barceloneta" property="og:image:alt"/>
<meta content="fr_FR" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Location de Patins à Roulettes Barcelone | Rollers Quad | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Location de patins à roulettes à Barcelone près de Vila Olímpica del Poblenou et de la plage de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant scooters, rollers en ligne, patins à roulettes, vélos, skateboards et longboards près du Port Olímpic et de la plage de la Barceloneta. Consigne gratuite, conseils d’itinéraires et assistance locale.",
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
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/fr/quads/",
      "name": "Location de Patins à Roulettes Barcelone | Rollers Quad | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/fr/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "inLanguage": "fr"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#breadcrumb",
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
          "name": "Location de patins à roulettes",
          "item": "https://rentalscooterbarcelona.com/fr/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant scooters, rollers en ligne, patins à roulettes, vélos, skateboards et longboards près du Port Olímpic et de la plage de la Barceloneta. Consigne gratuite, conseils d’itinéraires et assistance locale.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#service",
      "serviceType": "Location de patins à roulettes et rollers quad",
      "name": "Location de patins à roulettes à Barcelone",
      "url": "https://rentalscooterbarcelona.com/fr/quads/",
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
      "description": "Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Location de patins à roulettes 1 heure",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Location de patins à roulettes 2 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Location de patins à roulettes 3 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Location de patins à roulettes journée complète",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Location de patins à roulettes 24 heures",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Location de patins à roulettes jour supplémentaire",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/fr/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Faut-il de l’expérience pour louer des patins à roulettes ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer."
          }
        },
        {
          "@type": "Question",
          "name": "Les protections sont-elles incluses dans la location ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins."
          }
        },
        {
          "@type": "Question",
          "name": "Où puis-je patiner près de la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Notre boutique se trouve face à la plage et à côté du Port Olímpic. Les chemins plats du bord de mer et le parc de la Ciutadella offrent de bons itinéraires pour patiner tranquillement près de la boutique."
          }
        },
        {
          "@type": "Question",
          "name": "Quelles pointures sont disponibles ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nous proposons des patins à roulettes en pointures EU 35 à 42. Vous pouvez essayer plusieurs pointures en boutique pour trouver la plus confortable."
          }
        },
        {
          "@type": "Question",
          "name": "Les adolescents peuvent-ils louer des patins ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Nos patins conviennent aux grands enfants, adolescents et adultes dans les pointures EU 35 à 42 disponibles."
          }
        },
        {
          "@type": "Question",
          "name": "Faut-il un permis pour louer des patins ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide."
          }
        },
        {
          "@type": "Question",
          "name": "Puis-je laisser mes chaussures ou mes bagages à la boutique ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Une consigne gratuite pour chaussures, vestes, sacs à main, sacs à dos et valises est disponible dans notre boutique surveillée pendant votre location."
          }
        },
        {
          "@type": "Question",
          "name": "Comment réserver ou vous contacter ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vous pouvez réserver par WhatsApp, e-mail ou téléphone. Retrouvez toutes les coordonnées sur notre site et contactez-nous si vous avez des questions sur les pointures ou les disponibilités."
          }
        }
      ],
      "inLanguage": "fr"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#service-list",
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
            "name": "Location de rollers en ligne à Barcelone",
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
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/fr/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Sonia"
      },
      "datePublished": "2026-05-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Nous avons loué des rollers en ligne à Barcelone pendant nos vacances. Ils ont aussi des patins à quatre roues. La boutique se trouve à la Vila Olímpica, à côté de la promenade maritime et près de la Barceloneta. Bon prix et excellent accueil, je recommande à 100 %.\"",
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
<title>Noleggio pattini a rotelle a Barcellona | Pattini classici | RSB</title>
<meta content="Noleggio pattini a rotelle a Barcellona vicino a Port Olímpic e Barceloneta. Polsiere incluse e misure EU 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/it/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Noleggio pattini a rotelle a Barcellona | Pattini classici | RSB" property="og:title"/>
<meta content="Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/it/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Noleggio pattini a rotelle a Barcellona vicino a Vila Olímpica del Poblenou e alla spiaggia della Barceloneta" property="og:image:alt"/>
<meta content="it_IT" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Noleggio pattini a rotelle a Barcellona | Pattini classici | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Noleggio pattini a rotelle a Barcellona vicino a Vila Olímpica del Poblenou e alla spiaggia della Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con scooter, pattini in linea, pattini a rotelle, biciclette, skateboard e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Deposito gratuito, consigli sui percorsi e assistenza locale.",
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
      "@id": "https://rentalscooterbarcelona.com/it/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/it/quads/",
      "name": "Noleggio pattini a rotelle a Barcellona | Pattini classici | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "it",
      "description": "Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/it/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/it/quads/#breadcrumb",
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
          "name": "Noleggio pattini a rotelle",
          "item": "https://rentalscooterbarcelona.com/it/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con scooter, pattini in linea, pattini a rotelle, biciclette, skateboard e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Deposito gratuito, consigli sui percorsi e assistenza locale.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/it/quads/#service",
      "serviceType": "Noleggio pattini a rotelle e pattini a quattro ruote",
      "name": "Noleggio pattini a rotelle a Barcellona",
      "url": "https://rentalscooterbarcelona.com/it/quads/",
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
      "description": "Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Noleggio pattini a rotelle 1 ora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Noleggio pattini a rotelle 2 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Noleggio pattini a rotelle 3 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Noleggio pattini a rotelle giornata intera",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Noleggio pattini a rotelle 24 ore",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Noleggio pattini a rotelle giorno extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/it/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/it/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Serve esperienza per noleggiare pattini a rotelle?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, non serve esperienza. Offriamo pattini stabili per principianti e pattinatori più sicuri, e il nostro team ti aiuta a scegliere la taglia giusta prima di iniziare."
          }
        },
        {
          "@type": "Question",
          "name": "Le protezioni sono incluse nel noleggio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini."
          }
        },
        {
          "@type": "Question",
          "name": "Dove posso pattinare vicino al negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio."
          }
        },
        {
          "@type": "Question",
          "name": "Quali taglie sono disponibili?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Abbiamo pattini a rotelle nelle taglie EU 35–42. Puoi provare diverse taglie in negozio per trovare la più comoda."
          }
        },
        {
          "@type": "Question",
          "name": "Gli adolescenti possono noleggiare pattini?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. I nostri pattini vanno bene per ragazzi, adolescenti e adulti nelle taglie disponibili EU 35–42."
          }
        },
        {
          "@type": "Question",
          "name": "Serve una patente per noleggiare pattini?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso lasciare scarpe o bagagli in negozio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Durante il noleggio puoi lasciare gratuitamente scarpe, giacche, borse, zaini e valigie nel nostro negozio sorvegliato."
          }
        },
        {
          "@type": "Question",
          "name": "Come posso prenotare o contattarvi?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puoi prenotare via WhatsApp, e-mail o telefono. Trovi tutti i dettagli di contatto sul nostro sito e puoi scriverci se hai domande su taglie o disponibilità."
          }
        }
      ],
      "inLanguage": "it"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/it/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/it/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/it/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Sonia"
      },
      "datePublished": "2026-05-20",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Abbiamo noleggiato pattini in linea a Barcellona durante le nostre vacanze. Hanno anche pattini a quattro ruote. Il negozio si trova nella Vila Olímpica, accanto al lungomare e vicino alla Barceloneta. Buon prezzo e ottimo servizio, lo consiglio al 100%.\"",
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
<title>Rollschuhe mieten in Barcelona | Klassische Rollschuhe | RSB</title>
<meta content="Rollschuhe mieten in Barcelona nahe Port Olímpic und Barceloneta. Klassische Quad-Skates, Handgelenkschoner und Größen EU 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/de/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/><meta content="de_DE" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Rollschuhe mieten in Barcelona | Klassische Rollschuhe | RSB" property="og:title"/>
<meta content="Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/de/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Rollschuhe mieten in Barcelona nahe Vila Olímpica del Poblenou und Barceloneta-Strand" property="og:image:alt"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Rollschuhe mieten in Barcelona | Klassische Rollschuhe | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Rollschuhe mieten in Barcelona nahe Vila Olímpica del Poblenou und Barceloneta-Strand" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inline-Skates, Rollschuhen, Fahrrädern, Skateboards und Longboards nahe Port Olímpic und Barceloneta-Strand. Kostenlose Gepäckaufbewahrung, Routentipps und persönliche Beratung vor Ort.",
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
      "@id": "https://rentalscooterbarcelona.com/de/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/de/quads/",
      "name": "Rollschuhe mieten in Barcelona | Klassische Rollschuhe | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "de",
      "description": "Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/de/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/de/quads/#breadcrumb"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/de/quads/#breadcrumb",
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
          "name": "Rollschuhe mieten",
          "item": "https://rentalscooterbarcelona.com/de/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inline-Skates, Rollschuhen, Fahrrädern, Skateboards und Longboards nahe Port Olímpic und Barceloneta-Strand. Kostenlose Gepäckaufbewahrung, Routentipps und persönliche Beratung vor Ort.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp",
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/de/quads/#service",
      "serviceType": "Rollschuhe und klassische Quad-Skates mieten",
      "name": "Rollschuhe mieten in Barcelona",
      "url": "https://rentalscooterbarcelona.com/de/quads/",
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
      "description": "Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Rollschuhe 1 Stunde mieten",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Rollschuhe 2 Stunden mieten",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Rollschuhe 3 Stunden mieten",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Rollschuhe ganztägig mieten",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Rollschuhe 24 Stunden mieten",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Rollschuhe Zusatztag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/de/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/de/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Brauche ich Erfahrung, um Rollschuhe zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe."
          }
        },
        {
          "@type": "Question",
          "name": "Ist Schutzausrüstung in der Miete enthalten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive."
          }
        },
        {
          "@type": "Question",
          "name": "Wo kann ich in der Nähe des Geschäfts Rollschuh fahren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Unser Geschäft liegt direkt gegenüber dem Strand und neben dem Port Olímpic. Die flachen Wege an der Küste und der Parc de la Ciutadella eignen sich gut für entspanntes Rollschuhfahren."
          }
        },
        {
          "@type": "Question",
          "name": "Welche Größen sind verfügbar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden."
          }
        },
        {
          "@type": "Question",
          "name": "Können Jugendliche Rollschuhe mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42."
          }
        },
        {
          "@type": "Question",
          "name": "Brauche ich einen Führerschein, um Rollschuhe zu mieten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich meine Schuhe oder mein Gepäck im Geschäft lassen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Während der Miete können Schuhe, Jacken, Handtaschen, Rucksäcke und Koffer kostenlos in unserem betreuten Geschäft aufbewahrt werden."
          }
        },
        {
          "@type": "Question",
          "name": "Wie kann ich buchen oder Kontakt aufnehmen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben."
          }
        }
      ],
      "inLanguage": "de"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/de/quads/#service-list",
      "name": "Wichtigste Mietservices in Barcelona",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 6,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Scooter mieten in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/scooter/"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Inline-Skates mieten in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/rollerblades/"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Service",
            "name": "Fahrrad mieten in Barcelona",
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
            "name": "Skateboard mieten in Barcelona",
            "url": "https://rentalscooterbarcelona.com/de/skateboard/"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "Service",
            "name": "Longboard mieten in Barcelona",
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
      "@id": "https://rentalscooterbarcelona.com/de/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/de/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Ein toller Ort, um in Barcelona Skates zu mieten. Wir haben sowohl Inlineskates (Rollerblades) als auch klassische Rollschuhe mit vier Rollen gemietet. Alles war in gutem Zustand, das Personal war hilfsbereit und die Lage nahe dem Strand ist perfekt zum Skaten. Sehr empfehlenswert, wenn man in Barcelona Inlineskates oder Rollschuhe mieten möchte.“\"",
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
<title>Rolschaatsen huren in Barcelona | Klassieke Rolschaatsen | RSB</title>
<meta content="Rolschaatsen huren in Barcelona bij Port Olímpic en Barceloneta. Klassieke quad skates, polsbeschermers en maten EU 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/nl/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Rolschaatsen huren in Barcelona | Klassieke Rolschaatsen | RSB" property="og:title"/>
<meta content="Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/nl/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Rolschaatsen huren in Barcelona dicht bij Vila Olímpica del Poblenou en het strand van Barceloneta" property="og:image:alt"/>
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
<meta content="Rolschaatsen huren in Barcelona | Klassieke Rolschaatsen | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Rolschaatsen huren in Barcelona dicht bij Vila Olímpica del Poblenou en het strand van Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met scooters, inline skates, rolschaatsen, fietsen, skateboards en longboards dicht bij Port Olímpic en het strand van Barceloneta. Gratis bagageopslag, routetips en lokale hulp.",
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
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/nl/quads/",
      "name": "Rolschaatsen huren in Barcelona | Klassieke Rolschaatsen | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/nl/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "inLanguage": "nl",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#breadcrumb",
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
          "name": "Rolschaatsen huren",
          "item": "https://rentalscooterbarcelona.com/nl/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met scooters, inline skates, rolschaatsen, fietsen, skateboards en longboards dicht bij Port Olímpic en het strand van Barceloneta. Gratis bagageopslag, routetips en lokale hulp.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#service",
      "serviceType": "Rolschaatsen en klassieke quad skates huren",
      "name": "Rolschaatsen huren in Barcelona",
      "url": "https://rentalscooterbarcelona.com/nl/quads/",
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
      "description": "Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Rolschaatsen huren 1 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Rolschaatsen huren 2 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Rolschaatsen huren 3 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Rolschaatsen huren hele dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Rolschaatsen huren 24 uur",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Rolschaatsen huren extra dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/nl/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Heb ik ervaring nodig om rolschaatsen te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen."
          }
        },
        {
          "@type": "Question",
          "name": "Is bescherming inbegrepen bij de huur?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen."
          }
        },
        {
          "@type": "Question",
          "name": "Waar kan ik rolschaatsen in de buurt van de winkel?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Onze verhuurwinkel ligt tegenover het strand en naast Port Olímpic. De vlakke kustpaden en Parc de la Ciutadella zijn goede routes om rustig te rolschaatsen."
          }
        },
        {
          "@type": "Question",
          "name": "Welke maten zijn beschikbaar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We hebben rolschaatsen in EU-maten 35 tot 42. Je kunt in de winkel verschillende maten passen om de meest comfortabele te vinden."
          }
        },
        {
          "@type": "Question",
          "name": "Kunnen tieners rolschaatsen huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Onze rolschaatsen passen oudere kinderen, tieners en volwassenen binnen de beschikbare EU-maten 35 tot 42."
          }
        },
        {
          "@type": "Question",
          "name": "Heb ik een rijbewijs nodig om rolschaatsen te huren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende."
          }
        },
        {
          "@type": "Question",
          "name": "Kan ik mijn schoenen of bagage in de winkel achterlaten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Tijdens je huur kun je schoenen, jassen, handtassen, rugzakken en koffers gratis achterlaten in onze bewaakte winkel."
          }
        },
        {
          "@type": "Question",
          "name": "Hoe kan ik boeken of contact opnemen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid."
          }
        }
      ],
      "inLanguage": "nl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/nl/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Een geweldige plek om skates te huren in Barcelona. We huurden zowel inline skates (rollerblades) als klassieke rolschaatsen met vier wielen. Alles was in goede staat, het personeel was behulpzaam en de locatie vlak bij het strand is perfect om te skaten. Een echte aanrader als je inline skates of rolschaatsen wilt huren in Barcelona.\"",
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
<title>Aluguer de patins de 4 rodas em Barcelona | RSB</title>
<meta content="Aluguer de patins de 4 rodas em Barcelona perto de Port Olímpic e Barceloneta. Proteções de pulso incluídas e tamanhos EU 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pt/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Aluguer de patins de 4 rodas em Barcelona | RSB" property="og:title"/>
<meta content="Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pt/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Aluguer de patins de 4 rodas em Barcelona perto de Vila Olímpica del Poblenou e da praia de Barceloneta" property="og:image:alt"/>
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
<meta content="Aluguer de patins de 4 rodas em Barcelona | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Aluguer de patins de 4 rodas em Barcelona perto de Vila Olímpica del Poblenou e da praia de Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com scooters, patins em linha, patins de 4 rodas, bicicletas, skateboards e longboards perto do Port Olímpic e da praia de Barceloneta. Serviço gratuito de guarda de bagagem, recomendações de percursos e atendimento local.",
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
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/pt/quads/",
      "name": "Aluguer de patins de 4 rodas em Barcelona | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pt/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "inLanguage": "pt-PT",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#breadcrumb",
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
          "name": "Aluguer de patins de 4 rodas",
          "item": "https://rentalscooterbarcelona.com/pt/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com scooters, patins em linha, patins de 4 rodas, bicicletas, skateboards e longboards perto do Port Olímpic e da praia de Barceloneta. Serviço gratuito de guarda de bagagem, recomendações de percursos e atendimento local.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#service",
      "serviceType": "Aluguer de patins de 4 rodas e patins clássicos",
      "name": "Aluguer de patins de 4 rodas em Barcelona",
      "url": "https://rentalscooterbarcelona.com/pt/quads/",
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
      "description": "Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Aluguer de patins de 4 rodas 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Aluguer de patins de 4 rodas 2 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Aluguer de patins de 4 rodas 3 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Aluguer de patins de 4 rodas dia completo",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Aluguer de patins de 4 rodas 24 horas",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Aluguer de patins de 4 rodas dia extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/pt/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Preciso de experiência para alugar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não, não precisas de experiência prévia. Temos patins estáveis para principiantes e patinadores mais confiantes, e a nossa equipa ajuda a escolher o tamanho certo antes de começar."
          }
        },
        {
          "@type": "Question",
          "name": "O equipamento de proteção está incluído?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins."
          }
        },
        {
          "@type": "Question",
          "name": "Onde posso patinar perto da loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A nossa loja fica a poucos passos do passeio marítimo e do Port Olímpic. Os caminhos planos junto à costa e o Parc de la Ciutadella são boas rotas para patinar tranquilamente perto da loja."
          }
        },
        {
          "@type": "Question",
          "name": "Que tamanhos estão disponíveis?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Temos patins nos tamanhos EU 35 a 42. Podes experimentar vários tamanhos na loja para encontrar o mais confortável."
          }
        },
        {
          "@type": "Question",
          "name": "Adolescentes podem alugar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Os nossos patins servem para crianças mais velhas, adolescentes e adultos dentro dos tamanhos EU 35 a 42 disponíveis."
          }
        },
        {
          "@type": "Question",
          "name": "Preciso de carta para alugar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido."
          }
        },
        {
          "@type": "Question",
          "name": "Posso deixar os sapatos ou a bagagem na loja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada."
          }
        },
        {
          "@type": "Question",
          "name": "Como posso reservar ou contactar-vos?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade."
          }
        }
      ],
      "inLanguage": "pt-PT"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pt/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Um ótimo sítio para alugar patins em Barcelona. Alugámos tanto patins em linha (rollerblades) como patins clássicos de quatro rodas. Tudo estava em boas condições, o pessoal foi prestável e a localização perto da praia é perfeita para patinar. Muito recomendável se procura alugar patins em linha ou patins clássicos em Barcelona.\"",
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
<title>Lloguer de patins de 4 rodes a Barcelona | Patins clàssics | RSB</title>
<meta content="Lloga patins de 4 rodes a Barcelona prop de Port Olímpic i Barceloneta. Proteccions de canell incloses i talles de la UE 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/cat/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Lloguer de patins de 4 rodes a Barcelona | Patins clàssics | RSB" property="og:title"/>
<meta content="Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/cat/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Lloguer de patins de 4 rodes a Barcelona prop de Vila Olímpica del Poblenou i la platja de la Barceloneta" property="og:image:alt"/>
<meta content="ca_ES" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Lloguer de patins de 4 rodes a Barcelona | Patins clàssics | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Lloguer de patins de 4 rodes a Barcelona prop de Vila Olímpica del Poblenou i la platja de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, patins de 4 rodes, bicicletes, skateboards i longboards prop del Port Olímpic i la platja de la Barceloneta. Servei gratuït de guarda d’equipatge, recomanacions de rutes i atenció local.",
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
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/cat/quads/",
      "name": "Lloguer de patins de 4 rodes a Barcelona | Patins clàssics | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "ca",
      "description": "Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/cat/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#breadcrumb",
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
          "name": "Lloguer de patins de 4 rodes",
          "item": "https://rentalscooterbarcelona.com/cat/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, patins de 4 rodes, bicicletes, skateboards i longboards prop del Port Olímpic i la platja de la Barceloneta. Servei gratuït de guarda d’equipatge, recomanacions de rutes i atenció local.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#service",
      "serviceType": "Lloguer de patins de 4 rodes i patins clàssics",
      "name": "Lloguer de patins de 4 rodes a Barcelona",
      "url": "https://rentalscooterbarcelona.com/cat/quads/",
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
      "description": "Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Lloguer de patins de 4 rodes 1 hora",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Lloguer de patins de 4 rodes 2 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Lloguer de patins de 4 rodes 3 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Lloguer de patins de 4 rodes dia complet",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Lloguer de patins de 4 rodes 24 hores",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Lloguer de patins de 4 rodes dia extra",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/cat/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Cal experiència per llogar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar."
          }
        },
        {
          "@type": "Question",
          "name": "L’equip de protecció està inclòs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins."
          }
        },
        {
          "@type": "Question",
          "name": "On puc patinar a prop de la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La nostra botiga és davant de la platja i al costat del Port Olímpic. Els camins costaners plans i el Parc de la Ciutadella ofereixen bones rutes per patinar tranquil·lament a prop de la botiga."
          }
        },
        {
          "@type": "Question",
          "name": "Quines talles hi ha disponibles?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tenim patins en talles de la UE 35 a 42. Pots provar diverses talles a la botiga per trobar la més còmoda."
          }
        },
        {
          "@type": "Question",
          "name": "Els adolescents poden llogar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Els nostres patins serveixen per a nens grans, adolescents i adults dins del rang de talles de la UE 35 a 42."
          }
        },
        {
          "@type": "Question",
          "name": "Cal carnet per llogar patins?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid."
          }
        },
        {
          "@type": "Question",
          "name": "Puc deixar les sabates o l’equipatge a la botiga?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer."
          }
        },
        {
          "@type": "Question",
          "name": "Com reservo o contacto amb vosaltres?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pots reservar per WhatsApp, correu electrònic o telèfon. Trobaràs totes les dades de contacte al nostre web i ens pots preguntar qualsevol dubte sobre talles o disponibilitat."
          }
        }
      ],
      "inLanguage": "ca"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/cat/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Un lloc fantàstic per llogar patins a Barcelona. Vam llogar tant patins en línia com patins clàssics de quatre rodes. Tot estava en bon estat, el personal va ser servicial i la ubicació prop de la platja és perfecta per patinar. Molt recomanable si busques lloguer de patins en línia o patins clàssics a Barcelona.\"",
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
<title>Hyra Rullskridskor i Barcelona | Klassiska Rullskridskor | RSB</title>
<meta content="Hyra rullskridskor i Barcelona nära Port Olímpic och Barceloneta. Klassiska quad skates, handledsskydd och storlekar EU 35–42." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/sv/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Hyra Rullskridskor i Barcelona | Klassiska Rullskridskor | RSB" property="og:title"/>
<meta content="Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/sv/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Hyra rullskridskor i Barcelona nära Vila Olímpica del Poblenou och Barceloneta-stranden" property="og:image:alt"/>
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
<meta content="Hyra Rullskridskor i Barcelona | Klassiska Rullskridskor | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Hyra rullskridskor i Barcelona nära Vila Olímpica del Poblenou och Barceloneta-stranden" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med scootrar, inlines, rullskridskor, cyklar, skateboards och longboards nära Port Olímpic och Barceloneta-stranden. Gratis bagageförvaring, ruttips och lokal hjälp.",
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
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/sv/quads/",
      "name": "Hyra Rullskridskor i Barcelona | Klassiska Rullskridskor | RSB",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/sv/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/quads/#faq"
        }
      ],
      "dateModified": "2026-07-30",
      "inLanguage": "sv",
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#breadcrumb",
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
          "name": "Hyra rullskridskor",
          "item": "https://rentalscooterbarcelona.com/sv/quads/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med scootrar, inlines, rullskridskor, cyklar, skateboards och longboards nära Port Olímpic och Barceloneta-stranden. Gratis bagageförvaring, ruttips och lokal hjälp.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp",
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
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#service",
      "serviceType": "Hyra rullskridskor och klassiska rullskridskor",
      "name": "Hyra rullskridskor i Barcelona",
      "url": "https://rentalscooterbarcelona.com/sv/quads/",
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
      "description": "Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips.",
      "offers": [
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Hyra rullskridskor 1 timme",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Hyra rullskridskor 2 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Hyra rullskridskor 3 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Hyra rullskridskor heldag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Hyra rullskridskor 24 timmar",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Hyra rullskridskor extra dag",
          "availability": "https://schema.org/InStock",
          "url": "https://rentalscooterbarcelona.com/sv/quads/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Behöver jag erfarenhet för att hyra rullskridskor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar."
          }
        },
        {
          "@type": "Question",
          "name": "Ingår skyddsutrustning i hyran?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor."
          }
        },
        {
          "@type": "Question",
          "name": "Var kan jag åka rullskridskor nära butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken."
          }
        },
        {
          "@type": "Question",
          "name": "Vilka storlekar finns?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste."
          }
        },
        {
          "@type": "Question",
          "name": "Kan tonåringar hyra rullskridskor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42."
          }
        },
        {
          "@type": "Question",
          "name": "Behöver jag körkort för att hyra rullskridskor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nej. Inget körkort krävs för att hyra rullskridskor."
          }
        },
        {
          "@type": "Question",
          "name": "Kan jag lämna skor eller bagage i butiken?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Under hyran kan du lämna skor, jackor, handväskor, ryggsäckar och resväskor gratis i vår bemannade butik."
          }
        },
        {
          "@type": "Question",
          "name": "Hur bokar jag eller kontaktar er?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet."
          }
        }
      ],
      "inLanguage": "sv"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#service-list",
      "name": "Viktigaste uthyrningstjänsterna i Barcelona",
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
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/sv/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Ett fantastiskt ställe att hyra rullskridskor i Barcelona. Vi hyrde både inlines och klassiska fyrhjuliga rullskridskor. Allt var i gott skick, personalen var hjälpsam och läget nära stranden är perfekt för att åka. Rekommenderas varmt om du söker uthyrning av inlines eller rullskridskor i Barcelona.\"",
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
<title>Wynajem wrotek w Barcelonie | Klasyczne wrotki | RSB</title>
<meta content="Wynajmij klasyczne wrotki w Barcelonie, naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy, ochraniacze i bezpłatne przechowanie bagażu w cenie wynajmu." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pl/quads/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/quads/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/quads/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/quads/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/quads/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/quads/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/quads/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/quads/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/quads/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/quads/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/quads/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Wynajem wrotek w Barcelonie | Klasyczne wrotki | RSB" property="og:title"/>
<meta content="Wynajmij klasyczne wrotki w Barcelonie, naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy, ochraniacze i bezpłatne przechowanie bagażu w cenie wynajmu." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pl/quads/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="1200" property="og:image:width"/>
<meta content="800" property="og:image:height"/>
<meta content="Wynajem wrotek w Barcelonie blisko Vila Olímpica del Poblenou i plaży Barceloneta" property="og:image:alt"/>
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
<meta content="Wynajem wrotek w Barcelonie | Klasyczne wrotki | RSB" name="twitter:title"/>
<meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Wynajmij klasyczne wrotki w Barcelonie, naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy, ochraniacze i bezpłatne przechowanie bagażu w cenie wynajmu." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp" name="twitter:image"/>
<meta content="Wynajem wrotek w Barcelonie blisko Vila Olímpica del Poblenou i plaży Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Wynajem" name="apple-mobile-web-app-title"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-480-v1.webp 480w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-800-v1.webp 800w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp 1200w, https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp 1600w" rel="preload"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/styles.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/scooter/styles41.css?v=41" rel="stylesheet"/>
<style id="quads-lcp-cls-fixes">
.hero{position:relative;overflow:hidden;min-height:42rem;background:#0b1022;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg .layer,
.hero-bg img{display:block;width:100%;height:100%;}
.hero-bg img{object-fit:cover;object-position:center 40%;}
.hero-content{position:relative;z-index:2;min-height:42rem;}
.pills{min-height:3.6rem;}
.pills .pill{min-height:1.2rem;}
@media (max-width: 640px){
  .hero{min-height:38rem;}
  .hero-content{min-height:38rem;}
  .pills{min-height:6.3rem;}
}
</style>
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
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#webpage",
      "url": "https://rentalscooterbarcelona.com/pl/quads/",
      "name": "Wynajem wrotek w Barcelonie | Klasyczne wrotki",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "inLanguage": "pl",
      "description": "Wynajmij klasyczne wrotki w Barcelonie, naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy, ochraniacze i bezpłatne przechowanie bagażu w cenie wynajmu.",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/pl/quads/#service"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/quads/#faq"
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
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#breadcrumb",
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
          "name": "Wynajem wrotek",
          "item": "https://rentalscooterbarcelona.com/pl/quads/"
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
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#service",
      "serviceType": "Wynajem wrotek i klasycznych wrotek",
      "name": "Wynajem wrotek w Barcelonie",
      "url": "https://rentalscooterbarcelona.com/pl/quads/",
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
      "description": "Wynajmij klasyczne wrotki w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie w cenie, darmowe przechowanie bagażu i lokalne wskazówki.",
      "offers": [
        {
          "@type": "AggregateOffer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "name": "Zakres cen wynajmu wrotek",
          "priceCurrency": "EUR",
          "lowPrice": "6",
          "highPrice": "20",
          "offerCount": "6",
          "url": "https://rentalscooterbarcelona.com/pl/quads/"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "6",
          "name": "Wynajem wrotek 1 godzina",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "12",
          "name": "Wynajem wrotek 2 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "15",
          "name": "Wynajem wrotek 3 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "18",
          "name": "Całodniowy wynajem wrotek",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "20",
          "name": "Wynajem wrotek 24 godziny",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut",
          "priceCurrency": "EUR",
          "price": "10",
          "name": "Dodatkowy dzień wynajmu wrotek",
          "url": "https://rentalscooterbarcelona.com/pl/quads/",
          "availability": "https://schema.org/InStock"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Czy potrzebuję doświadczenia, aby wynająć wrotki?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem."
          }
        },
        {
          "@type": "Question",
          "name": "Czy sprzęt ochronny jest w cenie wynajmu?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek."
          }
        },
        {
          "@type": "Question",
          "name": "Gdzie mogę jeździć na wrotkach blisko wypożyczalni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nasza wypożyczalnia znajduje się naprzeciwko plaży i obok Port Olímpic. Płaskie nadmorskie ścieżki i park Ciutadella oferują dobre trasy do spokojnej jazdy na wrotkach blisko naszej wypożyczalni."
          }
        },
        {
          "@type": "Question",
          "name": "Jakie rozmiary są dostępne?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie."
          }
        },
        {
          "@type": "Question",
          "name": "Czy nastolatki mogą wynająć wrotki?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42."
          }
        },
        {
          "@type": "Question",
          "name": "Czy potrzebuję prawa jazdy, aby wynająć wrotki?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy."
          }
        },
        {
          "@type": "Question",
          "name": "Czy mogę zostawić buty lub bagaż w wypożyczalni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Podczas wynajmu dostępne jest darmowe przechowanie butów, kurtek, torebek, plecaków i walizek w naszej nadzorowanej wypożyczalni."
          }
        },
        {
          "@type": "Question",
          "name": "Jak mogę zarezerwować lub skontaktować się z wami?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność."
          }
        }
      ],
      "inLanguage": "pl"
    },
    {
      "@type": "ItemList",
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#service-list",
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
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pl/quads/#google-review-1"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/quads/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Pierre L"
      },
      "datePublished": "2026-08-10",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Świetne miejsce na wynajem rolek w Barcelonie. Wynajęliśmy zarówno rolki, jak i klasyczne wrotki na czterech kółkach. Wszystko było w dobrym stanie, personel był pomocny, a lokalizacja blisko plaży jest idealna do jazdy. Gorąco polecam, jeśli szukasz wynajmu rolek lub wrotek w Barcelonie.\"",
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
| en | https://rentalscooterbarcelona.com/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| es | https://rentalscooterbarcelona.com/es/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| fr | https://rentalscooterbarcelona.com/fr/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| it | https://rentalscooterbarcelona.com/it/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| de | https://rentalscooterbarcelona.com/de/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| nl | https://rentalscooterbarcelona.com/nl/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| pt | https://rentalscooterbarcelona.com/pt/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| ca | https://rentalscooterbarcelona.com/cat/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| sv | https://rentalscooterbarcelona.com/sv/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |
| pl | https://rentalscooterbarcelona.com/pl/quads/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/quads/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/quads/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/quads/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/quads/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/quads/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/quads/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/quads/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/quads/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/quads/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/quads/", "hreflang": "pl", "rel": "alternate"}] | True |

## M. MATRIZ SCHEMA @id + URL

| Idioma | Bloque | Ruta | Entidad completa |
| --- | --- | --- | --- |
| en | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| en | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "en", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/quads/#webpage", "url": "https://rentalscooterbarcelona.com/quads/", "name": "Roller Skate Rental Barcelona \| Quad &amp; Classic Skates \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "en", "description": "Rent classic quad roller skates in Barcelona near Port Olímpic and Barceloneta. Kids' helmet and protective pads included, plus free luggage storage.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/quads/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp booking", "target": "https://wa.me/34640559468"}} |
| en | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/"}, {"@type": "ListItem", "position": 2, "name": "Roller skate rental", "item": "https://rentalscooterbarcelona.com/quads/"}]} |
| en | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/quads/#service", "serviceType": "Roller skates, quad skates and classic skates rental", "name": "Roller skate rental in Barcelona", "url": "https://rentalscooterbarcelona.com/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Rent roller skates and quad skates in Barcelona near Port Olímpic and Barceloneta. Children's helmet, wrist guards, knee pads and elbow pads included, free luggage storage and local tips.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Roller skate rental price range", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Roller skate rental 1 hour", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Roller skate rental 2 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Roller skate rental 3 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Roller skate rental full day", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Roller skate rental 24 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Roller skate rental extra day", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}]} |
| en | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Do I need experience to rent roller skates?", "acceptedAnswer": {"@type": "Answer", "text": "No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start."}}, {"@type": "Question", "name": "Is protective gear included with the rental?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost."}}, {"@type": "Question", "name": "Where can I roller skate near the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Our rental shop is just steps from the seafront promenade and Port Olímpic. The flat coastal paths and Ciutadella Park offer good routes for relaxed roller skating near our store."}}, {"@type": "Question", "name": "What sizes are available?", "acceptedAnswer": {"@type": "Answer", "text": "We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit."}}, {"@type": "Question", "name": "Can teenagers rent roller skates?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range."}}, {"@type": "Question", "name": "Do I need a licence to rent roller skates?", "acceptedAnswer": {"@type": "Answer", "text": "No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID."}}, {"@type": "Question", "name": "Can I store my shoes or luggage at the shop?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Free storage for shoes, jackets, handbags, backpacks and suitcases is available in our supervised shop during your rental."}}, {"@type": "Question", "name": "How do I book or contact you?", "acceptedAnswer": {"@type": "Answer", "text": "You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability."}}], "inLanguage": "en"} |
| en | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/quads/#service-list", "name": "Main rental services in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter rental in Barcelona", "url": "https://rentalscooterbarcelona.com/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inline skates rental in Barcelona", "url": "https://rentalscooterbarcelona.com/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Bike rental in Barcelona", "url": "https://rentalscooterbarcelona.com/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Roller skate rental in Barcelona", "url": "https://rentalscooterbarcelona.com/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard rental in Barcelona", "url": "https://rentalscooterbarcelona.com/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard rental in Barcelona", "url": "https://rentalscooterbarcelona.com/longboard/"}}]} |
| en | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/quads/#webpage", "dateModified": "2026-08-24"} |
| en | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/quads/#google-review-1"}]} |
| en | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Great place to rent skates in Barcelona. We rented both inline skates (rollerblades) and classic 4-wheel roller skates. Everything was in good condition, the staff was helpful and the location near the beach is perfect for skating. Highly recommended if you're looking for inline skate or roller skate rental in Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-08-10"} |
| es | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, patines de 4 ruedas, bicicletas, skateboards y longboards cerca del Port Olímpic y la playa de la Barceloneta. Consigna gratuita, recomendaciones de rutas y atención local.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| es | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "es", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/quads/#webpage", "url": "https://rentalscooterbarcelona.com/es/quads/", "name": "Alquiler de patines de 4 ruedas en Barcelona \| Patines clásicos \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Alquila patines clásicos de 4 ruedas en Barcelona, cerca de Port Olímpic y Barceloneta. Casco infantil, protecciones y consigna gratuita incluidas.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/es/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/es/quads/#faq"}], "dateModified": "2026-07-30", "inLanguage": "es", "potentialAction": {"@type": "CommunicateAction", "name": "Reserva por WhatsApp", "target": "https://wa.me/34640559468"}, "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/es/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://rentalscooterbarcelona.com/es/"}, {"@type": "ListItem", "position": 2, "name": "Alquiler de patines de 4 ruedas", "item": "https://rentalscooterbarcelona.com/es/quads/"}]} |
| es | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, patines de 4 ruedas, bicicletas, skateboards y longboards cerca del Port Olímpic y la playa de la Barceloneta. Consigna gratuita, recomendaciones de rutas y atención local.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| es | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/es/quads/#service", "serviceType": "Alquiler de patines de 4 ruedas y patines clásicos", "name": "Alquiler de patines de 4 ruedas en Barcelona", "url": "https://rentalscooterbarcelona.com/es/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Alquila patines de 4 ruedas y patines clásicos en Barcelona cerca del Port Olímpic y la playa de la Barceloneta. Nuestra tienda en Vila Olímpica del Poblenou ofrece patines tradicionales para niños mayores, adolescentes y adultos, casco infantil, muñequeras, rodilleras y coderas incluidas, consigna gratuita y tallas UE 35–42.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Rango de precios del alquiler de patines de 4 ruedas", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Alquiler de patines de 4 ruedas 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Alquiler de patines de 4 ruedas 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Alquiler de patines de 4 ruedas 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Alquiler de patines de 4 ruedas día completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Alquiler de patines de 4 ruedas 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Alquiler de patines de 4 ruedas día extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}]} |
| es | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/es/quads/#faq", "mainEntity": [{"@type": "Question", "name": "¿Necesito experiencia para alquilar patines?", "acceptedAnswer": {"@type": "Answer", "text": "No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar."}}, {"@type": "Question", "name": "¿Está incluido el equipo de protección?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines."}}, {"@type": "Question", "name": "¿Dónde puedo patinar cerca de la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Nuestra tienda está a pocos pasos del paseo marítimo y del Port Olímpic. Los caminos llanos de la costa y el Parc de la Ciutadella ofrecen buenas rutas para patinar con calma cerca de la tienda."}}, {"@type": "Question", "name": "¿Qué tallas hay disponibles?", "acceptedAnswer": {"@type": "Answer", "text": "Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda."}}, {"@type": "Question", "name": "¿Pueden alquilar patines los adolescentes?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42."}}, {"@type": "Question", "name": "¿Necesito carnet para alquilar patines?", "acceptedAnswer": {"@type": "Answer", "text": "No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido."}}, {"@type": "Question", "name": "¿Puedo dejar mis zapatos o maletas en la tienda?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Tenemos consigna gratuita para zapatos, chaquetas, bolsos, mochilas y maletas en nuestra tienda supervisada durante el alquiler."}}, {"@type": "Question", "name": "¿Cómo reservo o contacto con vosotros?", "acceptedAnswer": {"@type": "Answer", "text": "Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad."}}], "inLanguage": "es"} |
| es | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/es/quads/#service-list", "name": "Servicios de alquiler principales en Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Alquiler de scooters en Barcelona", "url": "https://rentalscooterbarcelona.com/es/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Alquiler de patines en línea en Barcelona", "url": "https://rentalscooterbarcelona.com/es/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Alquiler de bicicletas en Barcelona", "url": "https://rentalscooterbarcelona.com/es/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Alquiler de patines de 4 ruedas en Barcelona", "url": "https://rentalscooterbarcelona.com/es/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Alquiler de skateboard en Barcelona", "url": "https://rentalscooterbarcelona.com/es/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Alquiler de longboard en Barcelona", "url": "https://rentalscooterbarcelona.com/es/longboard/"}}]} |
| es | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/quads/#webpage", "dateModified": "2026-08-24"} |
| es | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/es/quads/#google-review-1"}]} |
| es | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Alquilamos patines en línea en Barcelona en nuestras vacaciones,, tambien tienen patines de 4 ruedas, esta situada en la Vila Olimpica, al lado del paseo maritimo ycerca de la Barceloneta. Buen precio y una atenci¡on genial, lo recomiendo .100x100\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant scooters, rollers en ligne, patins à roulettes, vélos, skateboards et longboards près du Port Olímpic et de la plage de la Barceloneta. Consigne gratuite, conseils d’itinéraires et assistance locale.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| fr | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "fr"} |
| fr | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/quads/#webpage", "url": "https://rentalscooterbarcelona.com/fr/quads/", "name": "Location de Patins à Roulettes Barcelone \| Rollers Quad \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/fr/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/fr/quads/#faq"}], "dateModified": "2026-07-30", "inLanguage": "fr"} |
| fr | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/fr/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://rentalscooterbarcelona.com/fr/"}, {"@type": "ListItem", "position": 2, "name": "Location de patins à roulettes", "item": "https://rentalscooterbarcelona.com/fr/quads/"}]} |
| fr | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant scooters, rollers en ligne, patins à roulettes, vélos, skateboards et longboards près du Port Olímpic et de la plage de la Barceloneta. Consigne gratuite, conseils d’itinéraires et assistance locale.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| fr | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/fr/quads/#service", "serviceType": "Location de patins à roulettes et rollers quad", "name": "Location de patins à roulettes à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Louez des patins à roulettes à Barcelone, face à la plage et à côté du Port Olímpic. Casque pour enfant, protège-poignets, genouillères et coudières inclus.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Location de patins à roulettes 1 heure", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Location de patins à roulettes 2 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Location de patins à roulettes 3 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Location de patins à roulettes journée complète", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Location de patins à roulettes 24 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Location de patins à roulettes jour supplémentaire", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}]} |
| fr | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/fr/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Faut-il de l’expérience pour louer des patins à roulettes ?", "acceptedAnswer": {"@type": "Answer", "text": "Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer."}}, {"@type": "Question", "name": "Les protections sont-elles incluses dans la location ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins."}}, {"@type": "Question", "name": "Où puis-je patiner près de la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Notre boutique se trouve face à la plage et à côté du Port Olímpic. Les chemins plats du bord de mer et le parc de la Ciutadella offrent de bons itinéraires pour patiner tranquillement près de la boutique."}}, {"@type": "Question", "name": "Quelles pointures sont disponibles ?", "acceptedAnswer": {"@type": "Answer", "text": "Nous proposons des patins à roulettes en pointures EU 35 à 42. Vous pouvez essayer plusieurs pointures en boutique pour trouver la plus confortable."}}, {"@type": "Question", "name": "Les adolescents peuvent-ils louer des patins ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Nos patins conviennent aux grands enfants, adolescents et adultes dans les pointures EU 35 à 42 disponibles."}}, {"@type": "Question", "name": "Faut-il un permis pour louer des patins ?", "acceptedAnswer": {"@type": "Answer", "text": "Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide."}}, {"@type": "Question", "name": "Puis-je laisser mes chaussures ou mes bagages à la boutique ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Une consigne gratuite pour chaussures, vestes, sacs à main, sacs à dos et valises est disponible dans notre boutique surveillée pendant votre location."}}, {"@type": "Question", "name": "Comment réserver ou vous contacter ?", "acceptedAnswer": {"@type": "Answer", "text": "Vous pouvez réserver par WhatsApp, e-mail ou téléphone. Retrouvez toutes les coordonnées sur notre site et contactez-nous si vous avez des questions sur les pointures ou les disponibilités."}}], "inLanguage": "fr"} |
| fr | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/fr/quads/#service-list", "name": "Principaux services de location à Barcelone", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Location de scooters à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Location de rollers en ligne à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Location de vélos à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Location de patins à roulettes à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Location de skateboard à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Location de longboard à Barcelone", "url": "https://rentalscooterbarcelona.com/fr/longboard/"}}]} |
| fr | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/quads/#webpage", "dateModified": "2026-08-24"} |
| fr | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/fr/quads/#google-review-1"}]} |
| fr | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Nous avons loué des rollers en ligne à Barcelone pendant nos vacances. Ils ont aussi des patins à quatre roues. La boutique se trouve à la Vila Olímpica, à côté de la promenade maritime et près de la Barceloneta. Bon prix et excellent accueil, je recommande à 100 %.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con scooter, pattini in linea, pattini a rotelle, biciclette, skateboard e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Deposito gratuito, consigli sui percorsi e assistenza locale.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| it | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "it"} |
| it | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/quads/#webpage", "url": "https://rentalscooterbarcelona.com/it/quads/", "name": "Noleggio pattini a rotelle a Barcellona \| Pattini classici \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "it", "description": "Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/it/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/it/quads/#faq"}], "dateModified": "2026-07-30"} |
| it | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/it/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inizio", "item": "https://rentalscooterbarcelona.com/it/"}, {"@type": "ListItem", "position": 2, "name": "Noleggio pattini a rotelle", "item": "https://rentalscooterbarcelona.com/it/quads/"}]} |
| it | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con scooter, pattini in linea, pattini a rotelle, biciclette, skateboard e longboard vicino al Port Olímpic e alla spiaggia della Barceloneta. Deposito gratuito, consigli sui percorsi e assistenza locale.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| it | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/it/quads/#service", "serviceType": "Noleggio pattini a rotelle e pattini a quattro ruote", "name": "Noleggio pattini a rotelle a Barcellona", "url": "https://rentalscooterbarcelona.com/it/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Noleggia pattini a rotelle e pattini a quattro ruote a Barcellona vicino al Port Olímpic e alla spiaggia della Barceloneta. Il nostro negozio locale a Vila Olímpica del Poblenou offre pattini classici per bambini più grandi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi, deposito gratuito e misure EU 35–42.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Noleggio pattini a rotelle 1 ora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Noleggio pattini a rotelle 2 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Noleggio pattini a rotelle 3 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Noleggio pattini a rotelle giornata intera", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Noleggio pattini a rotelle 24 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Noleggio pattini a rotelle giorno extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}]} |
| it | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/it/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Serve esperienza per noleggiare pattini a rotelle?", "acceptedAnswer": {"@type": "Answer", "text": "No, non serve esperienza. Offriamo pattini stabili per principianti e pattinatori più sicuri, e il nostro team ti aiuta a scegliere la taglia giusta prima di iniziare."}}, {"@type": "Question", "name": "Le protezioni sono incluse nel noleggio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini."}}, {"@type": "Question", "name": "Dove posso pattinare vicino al negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio."}}, {"@type": "Question", "name": "Quali taglie sono disponibili?", "acceptedAnswer": {"@type": "Answer", "text": "Abbiamo pattini a rotelle nelle taglie EU 35–42. Puoi provare diverse taglie in negozio per trovare la più comoda."}}, {"@type": "Question", "name": "Gli adolescenti possono noleggiare pattini?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. I nostri pattini vanno bene per ragazzi, adolescenti e adulti nelle taglie disponibili EU 35–42."}}, {"@type": "Question", "name": "Serve una patente per noleggiare pattini?", "acceptedAnswer": {"@type": "Answer", "text": "Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido."}}, {"@type": "Question", "name": "Posso lasciare scarpe o bagagli in negozio?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Durante il noleggio puoi lasciare gratuitamente scarpe, giacche, borse, zaini e valigie nel nostro negozio sorvegliato."}}, {"@type": "Question", "name": "Come posso prenotare o contattarvi?", "acceptedAnswer": {"@type": "Answer", "text": "Puoi prenotare via WhatsApp, e-mail o telefono. Trovi tutti i dettagli di contatto sul nostro sito e puoi scriverci se hai domande su taglie o disponibilità."}}], "inLanguage": "it"} |
| it | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/it/quads/#service-list", "name": "Principali servizi di noleggio a Barcellona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Noleggio scooter a Barcellona", "url": "https://rentalscooterbarcelona.com/it/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Noleggio pattini in linea a Barcellona", "url": "https://rentalscooterbarcelona.com/it/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Noleggio biciclette a Barcellona", "url": "https://rentalscooterbarcelona.com/it/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Noleggio pattini a rotelle a Barcellona", "url": "https://rentalscooterbarcelona.com/it/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Noleggio skateboard a Barcellona", "url": "https://rentalscooterbarcelona.com/it/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Noleggio longboard a Barcellona", "url": "https://rentalscooterbarcelona.com/it/longboard/"}}]} |
| it | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/quads/#webpage", "dateModified": "2026-08-24"} |
| it | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/it/quads/#google-review-1"}]} |
| it | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Abbiamo noleggiato pattini in linea a Barcellona durante le nostre vacanze. Hanno anche pattini a quattro ruote. Il negozio si trova nella Vila Olímpica, accanto al lungomare e vicino alla Barceloneta. Buon prezzo e ottimo servizio, lo consiglio al 100%.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inline-Skates, Rollschuhen, Fahrrädern, Skateboards und Longboards nahe Port Olímpic und Barceloneta-Strand. Kostenlose Gepäckaufbewahrung, Routentipps und persönliche Beratung vor Ort.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| de | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "de", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| de | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/quads/#webpage", "url": "https://rentalscooterbarcelona.com/de/quads/", "name": "Rollschuhe mieten in Barcelona \| Klassische Rollschuhe \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "de", "description": "Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/de/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/de/quads/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/de/quads/#breadcrumb"}} |
| de | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/de/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://rentalscooterbarcelona.com/de/"}, {"@type": "ListItem", "position": 2, "name": "Rollschuhe mieten", "item": "https://rentalscooterbarcelona.com/de/quads/"}]} |
| de | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokaler Verleih in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inline-Skates, Rollschuhen, Fahrrädern, Skateboards und Longboards nahe Port Olímpic und Barceloneta-Strand. Kostenlose Gepäckaufbewahrung, Routentipps und persönliche Beratung vor Ort.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1200-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kartenzahlung akzeptiert. PayPal für Online-Zahlungen verfügbar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "Kundenservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| de | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/de/quads/#service", "serviceType": "Rollschuhe und klassische Quad-Skates mieten", "name": "Rollschuhe mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "description": "Miete Rollschuhe und klassische Quad-Skates in Barcelona nahe Port Olímpic und Barceloneta-Strand. Unser lokaler Verleih in Vila Olímpica del Poblenou bietet klassische Rollschuhe für größere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive, kostenlose Gepäckaufbewahrung und Größen EU 35–42.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Rollschuhe 1 Stunde mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Rollschuhe 2 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Rollschuhe 3 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Rollschuhe ganztägig mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Rollschuhe 24 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Rollschuhe Zusatztag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}]} |
| de | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/de/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Brauche ich Erfahrung, um Rollschuhe zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe."}}, {"@type": "Question", "name": "Ist Schutzausrüstung in der Miete enthalten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive."}}, {"@type": "Question", "name": "Wo kann ich in der Nähe des Geschäfts Rollschuh fahren?", "acceptedAnswer": {"@type": "Answer", "text": "Unser Geschäft liegt direkt gegenüber dem Strand und neben dem Port Olímpic. Die flachen Wege an der Küste und der Parc de la Ciutadella eignen sich gut für entspanntes Rollschuhfahren."}}, {"@type": "Question", "name": "Welche Größen sind verfügbar?", "acceptedAnswer": {"@type": "Answer", "text": "Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden."}}, {"@type": "Question", "name": "Können Jugendliche Rollschuhe mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42."}}, {"@type": "Question", "name": "Brauche ich einen Führerschein, um Rollschuhe zu mieten?", "acceptedAnswer": {"@type": "Answer", "text": "Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich."}}, {"@type": "Question", "name": "Kann ich meine Schuhe oder mein Gepäck im Geschäft lassen?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Während der Miete können Schuhe, Jacken, Handtaschen, Rucksäcke und Koffer kostenlos in unserem betreuten Geschäft aufbewahrt werden."}}, {"@type": "Question", "name": "Wie kann ich buchen oder Kontakt aufnehmen?", "acceptedAnswer": {"@type": "Answer", "text": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben."}}], "inLanguage": "de"} |
| de | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/de/quads/#service-list", "name": "Wichtigste Mietservices in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inline-Skates mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Fahrrad mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Rollschuhe mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard mieten in Barcelona", "url": "https://rentalscooterbarcelona.com/de/longboard/"}}]} |
| de | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/quads/#webpage", "dateModified": "2026-08-24"} |
| de | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/de/quads/#google-review-1"}]} |
| de | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Ein toller Ort, um in Barcelona Skates zu mieten. Wir haben sowohl Inlineskates (Rollerblades) als auch klassische Rollschuhe mit vier Rollen gemietet. Alles war in gutem Zustand, das Personal war hilfsbereit und die Lage nahe dem Strand ist perfekt zum Skaten. Sehr empfehlenswert, wenn man in Barcelona Inlineskates oder Rollschuhe mieten möchte.“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met scooters, inline skates, rolschaatsen, fietsen, skateboards en longboards dicht bij Port Olímpic en het strand van Barceloneta. Gratis bagageopslag, routetips en lokale hulp.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| nl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "nl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/quads/#webpage", "url": "https://rentalscooterbarcelona.com/nl/quads/", "name": "Rolschaatsen huren in Barcelona \| Klassieke Rolschaatsen \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/nl/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/nl/quads/#faq"}], "dateModified": "2026-07-30", "inLanguage": "nl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/nl/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Rolschaatsen huren", "item": "https://rentalscooterbarcelona.com/nl/quads/"}]} |
| nl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, met scooters, inline skates, rolschaatsen, fietsen, skateboards en longboards dicht bij Port Olímpic en het strand van Barceloneta. Gratis bagageopslag, routetips en lokale hulp.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| nl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/nl/quads/#service", "serviceType": "Rolschaatsen en klassieke quad skates huren", "name": "Rolschaatsen huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Huur rolschaatsen en klassieke quad skates in Barcelona, dicht bij Port Olímpic en het strand van Barceloneta. Onze lokale verhuurwinkel in Vila Olímpica del Poblenou biedt klassieke vierwielige rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen, gratis bagageopslag en maten EU 35–42.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Rolschaatsen huren 1 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Rolschaatsen huren 2 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Rolschaatsen huren 3 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Rolschaatsen huren hele dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Rolschaatsen huren 24 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Rolschaatsen huren extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}]} |
| nl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/nl/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Heb ik ervaring nodig om rolschaatsen te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen."}}, {"@type": "Question", "name": "Is bescherming inbegrepen bij de huur?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen."}}, {"@type": "Question", "name": "Waar kan ik rolschaatsen in de buurt van de winkel?", "acceptedAnswer": {"@type": "Answer", "text": "Onze verhuurwinkel ligt tegenover het strand en naast Port Olímpic. De vlakke kustpaden en Parc de la Ciutadella zijn goede routes om rustig te rolschaatsen."}}, {"@type": "Question", "name": "Welke maten zijn beschikbaar?", "acceptedAnswer": {"@type": "Answer", "text": "We hebben rolschaatsen in EU-maten 35 tot 42. Je kunt in de winkel verschillende maten passen om de meest comfortabele te vinden."}}, {"@type": "Question", "name": "Kunnen tieners rolschaatsen huren?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Onze rolschaatsen passen oudere kinderen, tieners en volwassenen binnen de beschikbare EU-maten 35 tot 42."}}, {"@type": "Question", "name": "Heb ik een rijbewijs nodig om rolschaatsen te huren?", "acceptedAnswer": {"@type": "Answer", "text": "Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende."}}, {"@type": "Question", "name": "Kan ik mijn schoenen of bagage in de winkel achterlaten?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Tijdens je huur kun je schoenen, jassen, handtassen, rugzakken en koffers gratis achterlaten in onze bewaakte winkel."}}, {"@type": "Question", "name": "Hoe kan ik boeken of contact opnemen?", "acceptedAnswer": {"@type": "Answer", "text": "Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid."}}], "inLanguage": "nl"} |
| nl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/nl/quads/#service-list", "name": "Belangrijkste verhuurdiensten in Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Scooter huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Inline skates huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Fiets huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Rolschaatsen huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Skateboard huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Longboard huren in Barcelona", "url": "https://rentalscooterbarcelona.com/nl/longboard/"}}]} |
| nl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/quads/#webpage", "dateModified": "2026-08-24"} |
| nl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/nl/quads/#google-review-1"}]} |
| nl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Een geweldige plek om skates te huren in Barcelona. We huurden zowel inline skates (rollerblades) als klassieke rolschaatsen met vier wielen. Alles was in goede staat, het personeel was behulpzaam en de locatie vlak bij het strand is perfect om te skaten. Een echte aanrader als je inline skates of rolschaatsen wilt huren in Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com scooters, patins em linha, patins de 4 rodas, bicicletas, skateboards e longboards perto do Port Olímpic e da praia de Barceloneta. Serviço gratuito de guarda de bagagem, recomendações de percursos e atendimento local.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pt | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pt-PT", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/quads/#webpage", "url": "https://rentalscooterbarcelona.com/pt/quads/", "name": "Aluguer de patins de 4 rodas em Barcelona \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pt/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/pt/quads/#faq"}], "dateModified": "2026-07-30", "inLanguage": "pt-PT", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pt/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": "https://rentalscooterbarcelona.com/pt/"}, {"@type": "ListItem", "position": 2, "name": "Aluguer de patins de 4 rodas", "item": "https://rentalscooterbarcelona.com/pt/quads/"}]} |
| pt | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com scooters, patins em linha, patins de 4 rodas, bicicletas, skateboards e longboards perto do Port Olímpic e da praia de Barceloneta. Serviço gratuito de guarda de bagagem, recomendações de percursos e atendimento local.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| pt | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pt/quads/#service", "serviceType": "Aluguer de patins de 4 rodas e patins clássicos", "name": "Aluguer de patins de 4 rodas em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Aluga patins de 4 rodas e patins clássicos em Barcelona, perto do Port Olímpic e da praia de Barceloneta. A nossa loja local em Vila Olímpica del Poblenou oferece patins tradicionais para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos, serviço gratuito de guarda de bagagem, tamanhos EU 35–42 e horários flexíveis.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Aluguer de patins de 4 rodas 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Aluguer de patins de 4 rodas 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Aluguer de patins de 4 rodas 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Aluguer de patins de 4 rodas dia completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Aluguer de patins de 4 rodas 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Aluguer de patins de 4 rodas dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}]} |
| pt | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pt/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Preciso de experiência para alugar patins?", "acceptedAnswer": {"@type": "Answer", "text": "Não, não precisas de experiência prévia. Temos patins estáveis para principiantes e patinadores mais confiantes, e a nossa equipa ajuda a escolher o tamanho certo antes de começar."}}, {"@type": "Question", "name": "O equipamento de proteção está incluído?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins."}}, {"@type": "Question", "name": "Onde posso patinar perto da loja?", "acceptedAnswer": {"@type": "Answer", "text": "A nossa loja fica a poucos passos do passeio marítimo e do Port Olímpic. Os caminhos planos junto à costa e o Parc de la Ciutadella são boas rotas para patinar tranquilamente perto da loja."}}, {"@type": "Question", "name": "Que tamanhos estão disponíveis?", "acceptedAnswer": {"@type": "Answer", "text": "Temos patins nos tamanhos EU 35 a 42. Podes experimentar vários tamanhos na loja para encontrar o mais confortável."}}, {"@type": "Question", "name": "Adolescentes podem alugar patins?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Os nossos patins servem para crianças mais velhas, adolescentes e adultos dentro dos tamanhos EU 35 a 42 disponíveis."}}, {"@type": "Question", "name": "Preciso de carta para alugar patins?", "acceptedAnswer": {"@type": "Answer", "text": "Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido."}}, {"@type": "Question", "name": "Posso deixar os sapatos ou a bagagem na loja?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada."}}, {"@type": "Question", "name": "Como posso reservar ou contactar-vos?", "acceptedAnswer": {"@type": "Answer", "text": "Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade."}}], "inLanguage": "pt-PT"} |
| pt | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pt/quads/#service-list", "name": "Principais serviços de aluguer em Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Aluguer de scooters em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Aluguer de patins em linha em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Aluguer de bicicletas em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Aluguer de patins de 4 rodas em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Aluguer de skateboard em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Aluguer de longboard em Barcelona", "url": "https://rentalscooterbarcelona.com/pt/longboard/"}}]} |
| pt | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/quads/#webpage", "dateModified": "2026-08-24"} |
| pt | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pt/quads/#google-review-1"}]} |
| pt | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Um ótimo sítio para alugar patins em Barcelona. Alugámos tanto patins em linha (rollerblades) como patins clássicos de quatro rodas. Tudo estava em boas condições, o pessoal foi prestável e a localização perto da praia é perfeita para patinar. Muito recomendável se procura alugar patins em linha ou patins clássicos em Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, patins de 4 rodes, bicicletes, skateboards i longboards prop del Port Olímpic i la platja de la Barceloneta. Servei gratuït de guarda d’equipatge, recomanacions de rutes i atenció local.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| ca | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "ca"} |
| ca | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/quads/#webpage", "url": "https://rentalscooterbarcelona.com/cat/quads/", "name": "Lloguer de patins de 4 rodes a Barcelona \| Patins clàssics \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "ca", "description": "Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/cat/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/cat/quads/#faq"}], "dateModified": "2026-07-30"} |
| ca | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/cat/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inici", "item": "https://rentalscooterbarcelona.com/cat/"}, {"@type": "ListItem", "position": 2, "name": "Lloguer de patins de 4 rodes", "item": "https://rentalscooterbarcelona.com/cat/quads/"}]} |
| ca | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, patins de 4 rodes, bicicletes, skateboards i longboards prop del Port Olímpic i la platja de la Barceloneta. Servei gratuït de guarda d’equipatge, recomanacions de rutes i atenció local.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| ca | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/cat/quads/#service", "serviceType": "Lloguer de patins de 4 rodes i patins clàssics", "name": "Lloguer de patins de 4 rodes a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "description": "Lloga patins de 4 rodes i patins clàssics a Barcelona, prop del Port Olímpic i la platja de la Barceloneta. La nostra botiga a Vila Olímpica del Poblenou ofereix patins tradicionals per a infants més grans, adolescents i adults, casc infantil, canelleres, genolleres i colzeres inclosos, servei gratuït de guarda d’equipatge i talles de la UE 35–42.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Lloguer de patins de 4 rodes 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Lloguer de patins de 4 rodes 2 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Lloguer de patins de 4 rodes 3 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Lloguer de patins de 4 rodes dia complet", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Lloguer de patins de 4 rodes 24 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Lloguer de patins de 4 rodes dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}]} |
| ca | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/cat/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Cal experiència per llogar patins?", "acceptedAnswer": {"@type": "Answer", "text": "No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar."}}, {"@type": "Question", "name": "L’equip de protecció està inclòs?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins."}}, {"@type": "Question", "name": "On puc patinar a prop de la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "La nostra botiga és davant de la platja i al costat del Port Olímpic. Els camins costaners plans i el Parc de la Ciutadella ofereixen bones rutes per patinar tranquil·lament a prop de la botiga."}}, {"@type": "Question", "name": "Quines talles hi ha disponibles?", "acceptedAnswer": {"@type": "Answer", "text": "Tenim patins en talles de la UE 35 a 42. Pots provar diverses talles a la botiga per trobar la més còmoda."}}, {"@type": "Question", "name": "Els adolescents poden llogar patins?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Els nostres patins serveixen per a nens grans, adolescents i adults dins del rang de talles de la UE 35 a 42."}}, {"@type": "Question", "name": "Cal carnet per llogar patins?", "acceptedAnswer": {"@type": "Answer", "text": "No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid."}}, {"@type": "Question", "name": "Puc deixar les sabates o l’equipatge a la botiga?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer."}}, {"@type": "Question", "name": "Com reservo o contacto amb vosaltres?", "acceptedAnswer": {"@type": "Answer", "text": "Pots reservar per WhatsApp, correu electrònic o telèfon. Trobaràs totes les dades de contacte al nostre web i ens pots preguntar qualsevol dubte sobre talles o disponibilitat."}}], "inLanguage": "ca"} |
| ca | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/cat/quads/#service-list", "name": "Serveis principals de lloguer a Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Lloguer de scooters a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Lloguer de patins en línia a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Lloguer de bicicletes a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Lloguer de patins de 4 rodes a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Lloguer de skateboard a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Lloguer de longboard a Barcelona", "url": "https://rentalscooterbarcelona.com/cat/longboard/"}}]} |
| ca | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/quads/#webpage", "dateModified": "2026-08-24"} |
| ca | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/cat/quads/#google-review-1"}]} |
| ca | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Un lloc fantàstic per llogar patins a Barcelona. Vam llogar tant patins en línia com patins clàssics de quatre rodes. Tot estava en bon estat, el personal va ser servicial i la ubicació prop de la platja és perfecta per patinar. Molt recomanable si busques lloguer de patins en línia o patins clàssics a Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med scootrar, inlines, rullskridskor, cyklar, skateboards och longboards nära Port Olímpic och Barceloneta-stranden. Gratis bagageförvaring, ruttips och lokal hjälp.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| sv | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "sv", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/quads/#webpage", "url": "https://rentalscooterbarcelona.com/sv/quads/", "name": "Hyra Rullskridskor i Barcelona \| Klassiska Rullskridskor \| RSB", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/sv/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/sv/quads/#faq"}], "dateModified": "2026-07-30", "inLanguage": "sv", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/sv/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Hem", "item": "https://rentalscooterbarcelona.com/sv/"}, {"@type": "ListItem", "position": 2, "name": "Hyra rullskridskor", "item": "https://rentalscooterbarcelona.com/sv/quads/"}]} |
| sv | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med scootrar, inlines, rullskridskor, cyklar, skateboards och longboards nära Port Olímpic och Barceloneta-stranden. Gratis bagageförvaring, ruttips och lokal hjälp.", "image": ["https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp", "https://rentalscooterbarcelona.com/images/rsb-bike-rental-shop-olympic-village-barcelona.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-logo-horizontal-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kortbetalning accepteras. PayPal finns för onlinebetalningar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "kundservice", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| sv | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/sv/quads/#service", "serviceType": "Hyra rullskridskor och klassiska rullskridskor", "name": "Hyra rullskridskor i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "description": "Hyr rullskridskor och klassiska rullskridskor i Barcelona nära Port Olímpic och Barceloneta-stranden. Vår lokala uthyrningsbutik i Vila Olímpica del Poblenou erbjuder klassiska fyrhjuliga rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår, gratis bagageförvaring, storlekar EU 35–42 och lokala ruttips.", "offers": [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Hyra rullskridskor 1 timme", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Hyra rullskridskor 2 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Hyra rullskridskor 3 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Hyra rullskridskor heldag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Hyra rullskridskor 24 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Hyra rullskridskor extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}]} |
| sv | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/sv/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Behöver jag erfarenhet för att hyra rullskridskor?", "acceptedAnswer": {"@type": "Answer", "text": "Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar."}}, {"@type": "Question", "name": "Ingår skyddsutrustning i hyran?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor."}}, {"@type": "Question", "name": "Var kan jag åka rullskridskor nära butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken."}}, {"@type": "Question", "name": "Vilka storlekar finns?", "acceptedAnswer": {"@type": "Answer", "text": "Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste."}}, {"@type": "Question", "name": "Kan tonåringar hyra rullskridskor?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42."}}, {"@type": "Question", "name": "Behöver jag körkort för att hyra rullskridskor?", "acceptedAnswer": {"@type": "Answer", "text": "Nej. Inget körkort krävs för att hyra rullskridskor."}}, {"@type": "Question", "name": "Kan jag lämna skor eller bagage i butiken?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Under hyran kan du lämna skor, jackor, handväskor, ryggsäckar och resväskor gratis i vår bemannade butik."}}, {"@type": "Question", "name": "Hur bokar jag eller kontaktar er?", "acceptedAnswer": {"@type": "Answer", "text": "Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet."}}], "inLanguage": "sv"} |
| sv | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/sv/quads/#service-list", "name": "Viktigaste uthyrningstjänsterna i Barcelona", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Hyra scooter i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Hyra inlines i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Hyra cykel i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Hyra rullskridskor i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Hyra skateboard i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Hyra longboard i Barcelona", "url": "https://rentalscooterbarcelona.com/sv/longboard/"}}]} |
| sv | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/quads/#webpage", "dateModified": "2026-08-24"} |
| sv | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/sv/quads/#google-review-1"}]} |
| sv | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ett fantastiskt ställe att hyra rullskridskor i Barcelona. Vi hyrde både inlines och klassiska fyrhjuliga rullskridskor. Allt var i gott skick, personalen var hjälpsam och läget nära stranden är perfekt för att åka. Rekommenderas varmt om du söker uthyrning av inlines eller rullskridskor i Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[2] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/quads/#webpage", "url": "https://rentalscooterbarcelona.com/pl/quads/", "name": "Wynajem wrotek w Barcelonie \| Klasyczne wrotki", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "inLanguage": "pl", "description": "Wynajmij klasyczne wrotki w Barcelonie, naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy, ochraniacze i bezpłatne przechowanie bagażu w cenie wynajmu.", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-roller-skates-rental-barcelona-hero-group-beach-1600-v1.webp"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/pl/quads/#service"}, {"@id": "https://rentalscooterbarcelona.com/pl/quads/#faq"}], "dateModified": "2026-07-30", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp rezerwacja", "target": "https://wa.me/34640559468"}} |
| pl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pl/quads/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://rentalscooterbarcelona.com/pl/"}, {"@type": "ListItem", "position": 2, "name": "Wynajem wrotek", "item": "https://rentalscooterbarcelona.com/pl/quads/"}]} |
| pl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Karta kredytowa, karta debetowa, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[5] | {"@type": "Service", "@id": "https://rentalscooterbarcelona.com/pl/quads/#service", "serviceType": "Wynajem wrotek i klasycznych wrotek", "name": "Wynajem wrotek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/quads/", "provider": {"@id": "https://rentalscooterbarcelona.com/#business"}, "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "description": "Wynajmij klasyczne wrotki w Barcelonie naprzeciwko plaży i obok Port Olímpic. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie w cenie, darmowe przechowanie bagażu i lokalne wskazówki.", "offers": [{"@type": "AggregateOffer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "name": "Zakres cen wynajmu wrotek", "priceCurrency": "EUR", "lowPrice": "6", "highPrice": "20", "offerCount": "6", "url": "https://rentalscooterbarcelona.com/pl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Wynajem wrotek 1 godzina", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Wynajem wrotek 2 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Wynajem wrotek 3 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Całodniowy wynajem wrotek", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Wynajem wrotek 24 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Dodatkowy dzień wynajmu wrotek", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}]} |
| pl | 1 | $.@graph[6] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pl/quads/#faq", "mainEntity": [{"@type": "Question", "name": "Czy potrzebuję doświadczenia, aby wynająć wrotki?", "acceptedAnswer": {"@type": "Answer", "text": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem."}}, {"@type": "Question", "name": "Czy sprzęt ochronny jest w cenie wynajmu?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek."}}, {"@type": "Question", "name": "Gdzie mogę jeździć na wrotkach blisko wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Nasza wypożyczalnia znajduje się naprzeciwko plaży i obok Port Olímpic. Płaskie nadmorskie ścieżki i park Ciutadella oferują dobre trasy do spokojnej jazdy na wrotkach blisko naszej wypożyczalni."}}, {"@type": "Question", "name": "Jakie rozmiary są dostępne?", "acceptedAnswer": {"@type": "Answer", "text": "Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie."}}, {"@type": "Question", "name": "Czy nastolatki mogą wynająć wrotki?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42."}}, {"@type": "Question", "name": "Czy potrzebuję prawa jazdy, aby wynająć wrotki?", "acceptedAnswer": {"@type": "Answer", "text": "Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy."}}, {"@type": "Question", "name": "Czy mogę zostawić buty lub bagaż w wypożyczalni?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Podczas wynajmu dostępne jest darmowe przechowanie butów, kurtek, torebek, plecaków i walizek w naszej nadzorowanej wypożyczalni."}}, {"@type": "Question", "name": "Jak mogę zarezerwować lub skontaktować się z wami?", "acceptedAnswer": {"@type": "Answer", "text": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność."}}], "inLanguage": "pl"} |
| pl | 1 | $.@graph[7] | {"@type": "ItemList", "@id": "https://rentalscooterbarcelona.com/pl/quads/#service-list", "name": "Główne usługi wynajmu w Barcelonie", "itemListOrder": "https://schema.org/ItemListOrderAscending", "numberOfItems": 6, "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Service", "name": "Wynajem skuterów w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/scooter/"}}, {"@type": "ListItem", "position": 2, "item": {"@type": "Service", "name": "Wynajem rolek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/rollerblades/"}}, {"@type": "ListItem", "position": 3, "item": {"@type": "Service", "name": "Wynajem rowerów w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/bike/"}}, {"@type": "ListItem", "position": 4, "item": {"@type": "Service", "name": "Wynajem wrotek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/quads/"}}, {"@type": "ListItem", "position": 5, "item": {"@type": "Service", "name": "Wynajem deskorolek w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/skateboard/"}}, {"@type": "ListItem", "position": 6, "item": {"@type": "Service", "name": "Wynajem longboardu w Barcelonie", "url": "https://rentalscooterbarcelona.com/pl/longboard/"}}]} |
| pl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/quads/#webpage", "dateModified": "2026-08-24"} |
| pl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pl/quads/#google-review-1"}]} |
| pl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Świetne miejsce na wynajem rolek w Barcelonie. Wynajęliśmy zarówno rolki, jak i klasyczne wrotki na czterech kółkach. Wszystko było w dobrym stanie, personel był pomocny, a lokalizacja blisko plaży jest idealna do jazdy. Gorąco polecam, jeśli szukasz wynajmu rolek lub wrotek w Barcelonie.\"", "publisher": {"@type": "Organization", "name": "Google"}} |

## N. MATRIZ ARTICLE/BLOGPOSTING

No hay entidades Article/BlogPosting en estas páginas de servicio/contacto; no se exige un esquema editorial. Los elementos HTML article se cuentan por separado en U.

## O. MATRIZ GEO/COORDENADAS

| Idioma | Coordenadas extraídas | IDs de mapas | Sin coordenadas antiguas |
| --- | --- | --- | --- |
| en | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 94, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 338, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| es | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 91, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 330, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| fr | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 84, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 274, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| it | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 83, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 273, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| de | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 81, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 281, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| nl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 94, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 290, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pt | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 94, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 290, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| ca | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 83, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 273, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| sv | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 94, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 290, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 94, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 338, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |

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
| en | [{"line": 779, "text": "1 hour €6 Perfect for a quick seafront roll or trying quad skates for the first time.", "price": 6.0}, {"line": 784, "text": "Most popular 2 hours €12 Ideal for Barceloneta, Port Olímpic and Ciutadella Park at your own pace.", "price": 12.0}, {"line": 790, "text": "3 hours €15 Best for longer beachfront routes and easy cruising through the park.", "price": 15.0}, {"line": 795, "text": "Full day €18 Enjoy a full day on classic roller skates with flexible same-day return.", "price": 18.0}, {"line": 800, "text": "24 hours €20 Pick up today and return tomorrow to stretch your skating time into the next day.", "price": 20.0}, {"line": 805, "text": "Extra day €10 Extend your rental for one more day at a lower rate.", "price": 10.0}] | [{"line": 991, "text": "1 hour€6", "price": 6.0}, {"line": 991, "text": "2 hours€12", "price": 12.0}, {"line": 991, "text": "3 hours€15", "price": 15.0}, {"line": 991, "text": "Full day€18", "price": 18.0}, {"line": 991, "text": "24 hours€20", "price": 20.0}, {"line": 991, "text": "Extra day€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Roller skate rental 1 hour", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Roller skate rental 2 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Roller skate rental 3 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Roller skate rental full day", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Roller skate rental 24 hours", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Roller skate rental extra day", "url": "https://rentalscooterbarcelona.com/quads/", "availability": "https://schema.org/InStock"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| es | [{"line": 773, "text": "1 hora €6 Perfecto para una vuelta rápida por el paseo marítimo o para probar patines de 4 ruedas por primera vez.", "price": 6.0}, {"line": 778, "text": "Más popular 2 horas €12 Ideal para recorrer la Barceloneta, el Port Olímpic y el Parc de la Ciutadella a tu ritmo.", "price": 12.0}, {"line": 784, "text": "3 horas €15 La mejor opción para rutas más largas junto a la playa y paseos tranquilos por el parque.", "price": 15.0}, {"line": 789, "text": "Día completo €18 Disfruta de un día completo con patines clásicos y devuélvelos el mismo día.", "price": 18.0}, {"line": 794, "text": "24 horas €20 Recógelos hoy y devuélvelos mañana para alargar tu tiempo de patinaje hasta el día siguiente.", "price": 20.0}, {"line": 799, "text": "Día extra €10 Amplía tu alquiler un día más con una tarifa reducida.", "price": 10.0}] | [{"line": 964, "text": "1 hora€6", "price": 6.0}, {"line": 964, "text": "2 horas€12", "price": 12.0}, {"line": 964, "text": "3 horas€15", "price": 15.0}, {"line": 964, "text": "Día completo€18", "price": 18.0}, {"line": 964, "text": "24 horas€20", "price": 20.0}, {"line": 964, "text": "Día extra€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Alquiler de patines de 4 ruedas 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Alquiler de patines de 4 ruedas 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Alquiler de patines de 4 ruedas 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Alquiler de patines de 4 ruedas día completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Alquiler de patines de 4 ruedas 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Alquiler de patines de 4 ruedas día extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/es/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| fr | [{"line": 705, "text": "1 heure €6 Parfait pour une petite balade en bord de mer ou pour essayer les rollers quad pour la première fois.", "price": 6.0}, {"line": 710, "text": "Le plus populaire 2 heures €12 Idéal pour la Barceloneta, le Port Olímpic et le parc de la Ciutadella à votre rythme.", "price": 12.0}, {"line": 716, "text": "3 heures €15 Idéal pour des parcours plus longs en bord de mer et une balade tranquille dans le parc.", "price": 15.0}, {"line": 721, "text": "Journée complète €18 Profitez d’une journée complète en patins à roulettes classiques.", "price": 18.0}, {"line": 726, "text": "24 heures €20 Retirez-les aujourd’hui et retournez-les demain pour prolonger votre temps de patinage jusqu’au lendemain.", "price": 20.0}, {"line": 731, "text": "Jour supplémentaire €10 Prolongez votre location d’un jour supplémentaire à tarif réduit.", "price": 10.0}] | [{"line": 896, "text": "1 heure€6", "price": 6.0}, {"line": 896, "text": "2 heures€12", "price": 12.0}, {"line": 896, "text": "3 heures€15", "price": 15.0}, {"line": 896, "text": "Journée complète€18", "price": 18.0}, {"line": 896, "text": "24 heures€20", "price": 20.0}, {"line": 896, "text": "Jour supplémentaire€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Location de patins à roulettes 1 heure", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Location de patins à roulettes 2 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Location de patins à roulettes 3 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Location de patins à roulettes journée complète", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Location de patins à roulettes 24 heures", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Location de patins à roulettes jour supplémentaire", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/fr/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| it | [{"line": 710, "text": "1 ora €6 Perfetto per un giro veloce sul lungomare o per provare i pattini a quattro ruote per la prima volta.", "price": 6.0}, {"line": 715, "text": "Più richiesto 2 ore €12 Ideale per la Barceloneta, il Port Olímpic e il Parc de la Ciutadella al tuo ritmo.", "price": 12.0}, {"line": 721, "text": "3 ore €15 Ideale per percorsi più lunghi sul mare e giri tranquilli nel parco.", "price": 15.0}, {"line": 726, "text": "Giornata intera €18 Goditi una giornata intera con pattini classici a rotelle e riconsegna in giornata.", "price": 18.0}, {"line": 731, "text": "24 ore €20 Ritira oggi e riconsegna domani per allungare il tempo di pattinaggio fino al giorno successivo.", "price": 20.0}, {"line": 736, "text": "Giorno extra €10 Estendi il noleggio di un altro giorno a una tariffa ridotta.", "price": 10.0}] | [{"line": 901, "text": "1 ora€6", "price": 6.0}, {"line": 901, "text": "2 ore€12", "price": 12.0}, {"line": 901, "text": "3 ore€15", "price": 15.0}, {"line": 901, "text": "Giornata intera€18", "price": 18.0}, {"line": 901, "text": "24 ore€20", "price": 20.0}, {"line": 901, "text": "Giorno extra€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Noleggio pattini a rotelle 1 ora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Noleggio pattini a rotelle 2 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Noleggio pattini a rotelle 3 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Noleggio pattini a rotelle giornata intera", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Noleggio pattini a rotelle 24 ore", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Noleggio pattini a rotelle giorno extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/it/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| de | [{"line": 712, "text": "1 Stunde €6 Perfekt für eine kurze Fahrt an der Strandpromenade oder um Quad-Skates zum ersten Mal auszuprobieren.", "price": 6.0}, {"line": 717, "text": "Am beliebtesten 2 Stunden €12 Ideal für Barceloneta, Port Olímpic und den Parc de la Ciutadella in deinem eigenen Tempo.", "price": 12.0}, {"line": 723, "text": "3 Stunden €15 Am besten für längere Routen am Strand und entspanntes Fahren durch den Park.", "price": 15.0}, {"line": 728, "text": "Ganzer Tag €18 Genieße einen ganzen Tag mit klassischen Rollschuhen und flexibler Rückgabe am selben Tag.", "price": 18.0}, {"line": 733, "text": "24 Stunden €20 Heute abholen und morgen zurückgeben, um die Fahrzeit bis zum nächsten Tag zu verlängern.", "price": 20.0}, {"line": 738, "text": "Zusatztag €10 Verlängere deine Miete um einen weiteren Tag zu einem günstigeren Tarif.", "price": 10.0}] | [{"line": 942, "text": "1 Stunde€6", "price": 6.0}, {"line": 942, "text": "2 Stunden€12", "price": 12.0}, {"line": 942, "text": "3 Stunden€15", "price": 15.0}, {"line": 942, "text": "Ganzer Tag€18", "price": 18.0}, {"line": 942, "text": "24 Stunden€20", "price": 20.0}, {"line": 942, "text": "Zusatztag€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Rollschuhe 1 Stunde mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Rollschuhe 2 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Rollschuhe 3 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Rollschuhe ganztägig mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Rollschuhe 24 Stunden mieten", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Rollschuhe Zusatztag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/de/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| nl | [{"line": 721, "text": "1 uur €6 Perfect voor een korte rit langs zee of om quad skates voor het eerst te proberen.", "price": 6.0}, {"line": 726, "text": "Populairst 2 uur €12 Ideaal voor Barceloneta, Port Olímpic en Parc de la Ciutadella in je eigen tempo.", "price": 12.0}, {"line": 732, "text": "3 uur €15 Het beste voor langere routes langs het strand en rustig rijden door het park.", "price": 15.0}, {"line": 737, "text": "Volledige dag €18 Geniet een volledige dag van klassieke rolschaatsen met flexibele terugbrengmogelijkheid op dezelfde dag.", "price": 18.0}, {"line": 742, "text": "24 uur €20 Haal vandaag op en breng morgen terug om je rolschaatstijd tot de volgende dag te verlengen.", "price": 20.0}, {"line": 747, "text": "Extra dag €10 Verleng je huur met nog een dag tegen een lager tarief.", "price": 10.0}] | [{"line": 951, "text": "1 uur€6", "price": 6.0}, {"line": 951, "text": "2 uur€12", "price": 12.0}, {"line": 951, "text": "3 uur€15", "price": 15.0}, {"line": 951, "text": "Volledige dag€18", "price": 18.0}, {"line": 951, "text": "24 uur€20", "price": 20.0}, {"line": 951, "text": "Extra dag€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Rolschaatsen huren 1 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Rolschaatsen huren 2 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Rolschaatsen huren 3 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Rolschaatsen huren hele dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Rolschaatsen huren 24 uur", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Rolschaatsen huren extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/nl/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| pt | [{"line": 727, "text": "1 hora €6 Perfeito para uma volta rápida junto ao mar ou para experimentar patins de 4 rodas pela primeira vez.", "price": 6.0}, {"line": 732, "text": "Mais popular 2 horas €12 Ideal para a Barceloneta, o Port Olímpic e o Parc de la Ciutadella ao teu ritmo.", "price": 12.0}, {"line": 738, "text": "3 horas €15 A melhor opção para percursos mais longos junto à praia e passeios tranquilos pelo parque.", "price": 15.0}, {"line": 743, "text": "Dia completo €18 Desfruta de um dia completo com patins clássicos e devolução flexível no mesmo dia.", "price": 18.0}, {"line": 748, "text": "24 horas €20 Recolha hoje e devolve amanhã para prolongar o tempo de patinagem até ao dia seguinte.", "price": 20.0}, {"line": 753, "text": "Dia extra €10 Prolonga o aluguer por mais um dia com uma tarifa reduzida.", "price": 10.0}] | [{"line": 939, "text": "1 hora€6", "price": 6.0}, {"line": 939, "text": "2 horas€12", "price": 12.0}, {"line": 939, "text": "3 horas€15", "price": 15.0}, {"line": 939, "text": "Dia completo€18", "price": 18.0}, {"line": 939, "text": "24 horas€20", "price": 20.0}, {"line": 939, "text": "Dia extra€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Aluguer de patins de 4 rodas 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Aluguer de patins de 4 rodas 2 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Aluguer de patins de 4 rodas 3 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Aluguer de patins de 4 rodas dia completo", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Aluguer de patins de 4 rodas 24 horas", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Aluguer de patins de 4 rodas dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/pt/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| ca | [{"line": 710, "text": "1 hora €6 Perfecte per fer una volta ràpida pel passeig marítim o provar patins de 4 rodes per primera vegada.", "price": 6.0}, {"line": 715, "text": "Més popular 2 hores €12 Ideal per recórrer la Barceloneta, el Port Olímpic i el Parc de la Ciutadella al teu ritme.", "price": 12.0}, {"line": 721, "text": "3 hores €15 La millor opció per a rutes més llargues vora la platja i passejos tranquils pel parc.", "price": 15.0}, {"line": 726, "text": "Dia complet €18 Gaudeix d’un dia complet amb patins clàssics.", "price": 18.0}, {"line": 731, "text": "24 hores €20 Recull-los avui i torna’ls demà per allargar el temps de patinatge fins l’endemà.", "price": 20.0}, {"line": 736, "text": "Dia extra €10 Allarga el lloguer un dia més amb una tarifa reduïda.", "price": 10.0}] | [{"line": 923, "text": "1 hora€6", "price": 6.0}, {"line": 923, "text": "2 hores€12", "price": 12.0}, {"line": 923, "text": "3 hores€15", "price": 15.0}, {"line": 923, "text": "Dia complet€18", "price": 18.0}, {"line": 923, "text": "24 hores€20", "price": 20.0}, {"line": 923, "text": "Dia extra€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Lloguer de patins de 4 rodes 1 hora", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Lloguer de patins de 4 rodes 2 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Lloguer de patins de 4 rodes 3 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Lloguer de patins de 4 rodes dia complet", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Lloguer de patins de 4 rodes 24 hores", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Lloguer de patins de 4 rodes dia extra", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/cat/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| sv | [{"line": 723, "text": "1 timme €6 Perfekt för en kort tur längs havet eller för att prova quad skates för första gången.", "price": 6.0}, {"line": 728, "text": "Mest populärt 2 timmar €12 Perfekt för Barceloneta, Port Olímpic och Parc de la Ciutadella i din egen takt.", "price": 12.0}, {"line": 734, "text": "3 timmar €15 Bäst för längre strandrutter och lugn åkning genom parken.", "price": 15.0}, {"line": 739, "text": "Heldag €18 Njut av en hel dag med klassiska rullskridskor och flexibel återlämning samma dag.", "price": 18.0}, {"line": 744, "text": "24 timmar €20 Hämta idag och lämna tillbaka imorgon för att förlänga åktiden till nästa dag.", "price": 20.0}, {"line": 749, "text": "Extra dag €10 Förläng hyran med en extra dag till ett lägre pris.", "price": 10.0}] | [{"line": 937, "text": "1 timme€6", "price": 6.0}, {"line": 937, "text": "2 timmar€12", "price": 12.0}, {"line": 937, "text": "3 timmar€15", "price": 15.0}, {"line": 937, "text": "Heldag€18", "price": 18.0}, {"line": 937, "text": "24 timmar€20", "price": 20.0}, {"line": 937, "text": "Extra dag€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Hyra rullskridskor 1 timme", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Hyra rullskridskor 2 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Hyra rullskridskor 3 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Hyra rullskridskor heldag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Hyra rullskridskor 24 timmar", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Hyra rullskridskor extra dag", "availability": "https://schema.org/InStock", "url": "https://rentalscooterbarcelona.com/sv/quads/"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |
| pl | [{"line": 779, "text": "1 godzina €6 Idealne na krótką przejażdżkę nad morzem albo pierwszą próbę jazdy na wrotkach.", "price": 6.0}, {"line": 784, "text": "Najpopularniejsze 2 godziny €12 Idealne do odkrywania Barceloneta, Port Olímpic i parku Ciutadella we własnym tempie.", "price": 12.0}, {"line": 790, "text": "3 godziny €15 Najlepsze na dłuższe trasy przy plaży i spokojną jazdę przez park.", "price": 15.0}, {"line": 795, "text": "Cały dzień €18 Ciesz się całym dniem jazdy na klasycznych wrotkach z elastycznym zwrotem tego samego dnia.", "price": 18.0}, {"line": 800, "text": "24 godziny €20 Odbierz dziś i zwróć jutro, aby przedłużyć czas jazdy do następnego dnia.", "price": 20.0}, {"line": 805, "text": "Dodatkowy dzień €10 Przedłuż wynajem o jeszcze jeden dzień w niższej cenie.", "price": 10.0}] | [{"line": 991, "text": "1 godzina€6", "price": 6.0}, {"line": 991, "text": "2 godziny€12", "price": 12.0}, {"line": 991, "text": "3 godziny€15", "price": 15.0}, {"line": 991, "text": "Cały dzień€18", "price": 18.0}, {"line": 991, "text": "24 godziny€20", "price": 20.0}, {"line": 991, "text": "Dodatkowy dzień€10", "price": 10.0}] | [{"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "6", "name": "Wynajem wrotek 1 godzina", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "12", "name": "Wynajem wrotek 2 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "15", "name": "Wynajem wrotek 3 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "18", "name": "Całodniowy wynajem wrotek", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "20", "name": "Wynajem wrotek 24 godziny", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}, {"@type": "Offer", "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "priceCurrency": "EUR", "price": "10", "name": "Dodatkowy dzień wynajmu wrotek", "url": "https://rentalscooterbarcelona.com/pl/quads/", "availability": "https://schema.org/InStock"}] | [] | [{"test": "all_card_prices_match_same_group_EN_or_inline_service_context", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}, {"test": "offer_prices_match_cards", "pass": true}, {"test": "compact_matches_cards", "actual": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "expected": [6.0, 12.0, 15.0, 18.0, 20.0, 10.0], "pass": true}] |

| Idioma | Ofertas servicio | Ofertas PRICES | Coinciden tarifas base |
| --- | --- | --- | --- |
| en | [["Roller skate rental 1 hour", 6.0], ["Roller skate rental 2 hours", 12.0], ["Roller skate rental 3 hours", 15.0], ["Roller skate rental full day", 18.0], ["Roller skate rental 24 hours", 20.0], ["Roller skate rental extra day", 10.0]] | [["1 hour", 6.0], ["2 hours", 12.0], ["3 hours", 15.0], ["Full day", 18.0], ["24 hours", 20.0], ["Extra day", 10.0], ["1-hour roller skate rental in Barcelona", 6.0]] | True |
| es | [["Alquiler de patines de 4 ruedas 1 hora", 6.0], ["Alquiler de patines de 4 ruedas 2 horas", 12.0], ["Alquiler de patines de 4 ruedas 3 horas", 15.0], ["Alquiler de patines de 4 ruedas día completo", 18.0], ["Alquiler de patines de 4 ruedas 24 horas", 20.0], ["Alquiler de patines de 4 ruedas día extra", 10.0]] | [["1 hora", 6.0], ["2 horas", 12.0], ["3 horas", 15.0], ["Día completo", 18.0], ["24 horas", 20.0], ["Día extra", 10.0], ["Alquiler de patines de 4 ruedas 1 hora en Barcelona", 6.0]] | True |
| fr | [["Location de patins à roulettes 1 heure", 6.0], ["Location de patins à roulettes 2 heures", 12.0], ["Location de patins à roulettes 3 heures", 15.0], ["Location de patins à roulettes journée complète", 18.0], ["Location de patins à roulettes 24 heures", 20.0], ["Location de patins à roulettes jour supplémentaire", 10.0]] | [["1 heure", 6.0], ["2 heures", 12.0], ["3 heures", 15.0], ["Journée complète", 18.0], ["24 heures", 20.0], ["Jour supplémentaire", 10.0], ["Location de patins à roulettes 1 heure à Barcelone", 6.0]] | True |
| it | [["Noleggio pattini a rotelle 1 ora", 6.0], ["Noleggio pattini a rotelle 2 ore", 12.0], ["Noleggio pattini a rotelle 3 ore", 15.0], ["Noleggio pattini a rotelle giornata intera", 18.0], ["Noleggio pattini a rotelle 24 ore", 20.0], ["Noleggio pattini a rotelle giorno extra", 10.0]] | [["1 ora", 6.0], ["2 ore", 12.0], ["3 ore", 15.0], ["Giornata intera", 18.0], ["24 ore", 20.0], ["Giorno extra", 10.0], ["Noleggio pattini a rotelle 1 ora a Barcellona", 6.0]] | True |
| de | [["Rollschuhe 1 Stunde mieten", 6.0], ["Rollschuhe 2 Stunden mieten", 12.0], ["Rollschuhe 3 Stunden mieten", 15.0], ["Rollschuhe ganztägig mieten", 18.0], ["Rollschuhe 24 Stunden mieten", 20.0], ["Rollschuhe Zusatztag", 10.0]] | [["1 Stunde", 6.0], ["2 Stunden", 12.0], ["3 Stunden", 15.0], ["Ganzer Tag", 18.0], ["24 Stunden", 20.0], ["Zusätzlicher Tag", 10.0], ["Rollschuhe mieten – 1 Stunde in Barcelona", 6.0]] | True |
| nl | [["Rolschaatsen huren 1 uur", 6.0], ["Rolschaatsen huren 2 uur", 12.0], ["Rolschaatsen huren 3 uur", 15.0], ["Rolschaatsen huren hele dag", 18.0], ["Rolschaatsen huren 24 uur", 20.0], ["Rolschaatsen huren extra dag", 10.0]] | [["1 uur", 6.0], ["2 uur", 12.0], ["3 uur", 15.0], ["Hele dag", 18.0], ["24 uur", 20.0], ["Extra dag", 10.0], ["Rolschaatsen huren voor 1 uur in Barcelona", 6.0]] | True |
| pt | [["Aluguer de patins de 4 rodas 1 hora", 6.0], ["Aluguer de patins de 4 rodas 2 horas", 12.0], ["Aluguer de patins de 4 rodas 3 horas", 15.0], ["Aluguer de patins de 4 rodas dia completo", 18.0], ["Aluguer de patins de 4 rodas 24 horas", 20.0], ["Aluguer de patins de 4 rodas dia extra", 10.0]] | [["1 hora", 6.0], ["2 horas", 12.0], ["3 horas", 15.0], ["Dia completo", 18.0], ["24 horas", 20.0], ["Dia extra", 10.0], ["Aluguer de patins de 4 rodas por 1 hora em Barcelona", 6.0]] | True |
| ca | [["Lloguer de patins de 4 rodes 1 hora", 6.0], ["Lloguer de patins de 4 rodes 2 hores", 12.0], ["Lloguer de patins de 4 rodes 3 hores", 15.0], ["Lloguer de patins de 4 rodes dia complet", 18.0], ["Lloguer de patins de 4 rodes 24 hores", 20.0], ["Lloguer de patins de 4 rodes dia extra", 10.0]] | [["1 hora", 6.0], ["2 hores", 12.0], ["3 hores", 15.0], ["Dia complet", 18.0], ["24 hores", 20.0], ["Dia extra", 10.0], ["Lloguer de patins de 4 rodes 1 hora a Barcelona", 6.0]] | True |
| sv | [["Hyra rullskridskor 1 timme", 6.0], ["Hyra rullskridskor 2 timmar", 12.0], ["Hyra rullskridskor 3 timmar", 15.0], ["Hyra rullskridskor heldag", 18.0], ["Hyra rullskridskor 24 timmar", 20.0], ["Hyra rullskridskor extra dag", 10.0]] | [["1 timme", 6.0], ["2 timmar", 12.0], ["3 timmar", 15.0], ["Heldag", 18.0], ["24 timmar", 20.0], ["Extra dag", 10.0], ["Rullskridskouthyrning 1 timme i Barcelona", 6.0]] | True |
| pl | [["Wynajem wrotek 1 godzina", 6.0], ["Wynajem wrotek 2 godziny", 12.0], ["Wynajem wrotek 3 godziny", 15.0], ["Całodniowy wynajem wrotek", 18.0], ["Wynajem wrotek 24 godziny", 20.0], ["Dodatkowy dzień wynajmu wrotek", 10.0]] | [["1 godzina", 6.0], ["2 godziny", 12.0], ["3 godziny", 15.0], ["Cały dzień", 18.0], ["24 godziny", 20.0], ["Dodatkowy dzień", 10.0], ["Godzinny wynajem wrotek w Barcelonie", 6.0]] | True |

## R. MATRIZ POLÍTICAS

Textos completos extraídos por idioma: equipamiento, documentos, depósito, reservas, tallas y condiciones. Ausencia de una mención no equivale a contradicción. El alcance es coherencia del HTML con CANONICAL, no validación legal ni de disponibilidad.

| Idioma | Línea | Texto |
| --- | --- | --- |
| en | 728 | Rent roller skates and quad skates from our local shop in Vila Olímpica del Poblenou, near Barceloneta Beach and Port Olímpic. Stable classic four-wheel skates for older children, teenagers and adults, with a children's helmet, wrist guards, knee pads and elbow pads included. Free luggage storage, local route tips and sizes EU 35–42. |
| en | 759 | Choose from well-maintained roller skates and quad skates for older children, teenagers and adults, ready for relaxed rides by the beach and around Vila Olímpica. |
| en | 762 | Protective gear included |
| en | 763 | Children's helmet, wrist guards, knee pads and elbow pads are included with every rental at no extra cost. |
| en | 767 | Start skating just steps from Barceloneta Beach and Port Olímpic. Explore the seafront promenade and Ciutadella Park without traffic or long transfers. |
| en | 776 | These are the current public prices for our roller skates and quad skates rental service. You can also compare all rates on our Prices page, and contact us on WhatsApp to confirm availability or reserve your size before visiting. |
| en | 788 | Ideal for Barceloneta, Port Olímpic and Ciutadella Park at your own pace. |
| en | 830 | Children's helmet included |
| en | 831 | Wrist guards, knee pads and elbow pads included |
| en | 832 | Sizes from EU 35 to 42 |
| en | 833 | Size help and fit check at pick-up |
| en | 873 | Open every day: 10:30–13:30 and 16:30–20:00. We offer hourly and daily rentals with flexible return times. Children's helmet, wrist guards, knee pads and elbow pads are included with every rental. Sizes range from EU 35 to 42, and our local team provides basic instructions and route guidance. For local route ideas and practical tips, you can read our roller skate rental guide in Barcelona. |
| en | 939 | No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start. |
| en | 942 | Is protective gear included with the rental? |
| en | 943 | Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost. |
| en | 950 | What sizes are available? |
| en | 951 | We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit. |
| en | 955 | Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range. |
| en | 958 | Do I need a licence to rent roller skates? |
| en | 959 | No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID. |
| en | 967 | You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability. |
| en | 976 | More Barcelona rentals and local guides |
| en | 977 | Discover related rental services from our Vila Olímpica shop and browse local guides across the main activities we offer in Barcelona. |
| en | 991 | Children's helmet included · Wrist guards, knee pads and elbow pads included · Size help at the shop · Storage for shoes, jackets, bags and luggage. |
| en | 1000 | Message us on WhatsApp or visit our shop in Vila Olímpica to organise your roller skate rental near Barceloneta Beach. Our team will help you choose the right size and recommend the best routes. |
| es | 722 | Alquila patines de 4 ruedas y patines clásicos en nuestra tienda local de Vila Olímpica del Poblenou, cerca de la playa de la Barceloneta y el Port Olímpic. Patines tradicionales estables para niños mayores, adolescentes y adultos, con casco infantil, muñequeras, rodilleras y coderas incluidas. Consigna gratuita, consejos de rutas locales y tallas UE 35–42. |
| es | 753 | Elige patines de 4 ruedas y patines clásicos bien mantenidos para niños mayores, adolescentes y adultos, listos para patinar con calma junto a la playa y por la Vila Olímpica. |
| es | 756 | Protecciones incluidas |
| es | 757 | El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines. |
| es | 770 | Estos son los precios públicos actuales de nuestro servicio de alquiler de patines de 4 ruedas y patines clásicos. También puedes comparar todas las tarifas en nuestra página de precios, y contactarnos por WhatsApp para confirmar disponibilidad o reservar tu talla antes de venir. |
| es | 776 | Perfecto para una vuelta rápida por el paseo marítimo o para probar patines de 4 ruedas por primera vez. |
| es | 782 | Ideal para recorrer la Barceloneta, el Port Olímpic y el Parc de la Ciutadella a tu ritmo. |
| es | 802 | Amplía tu alquiler un día más con una tarifa reducida. |
| es | 806 | Protecciones y extras para patines |
| es | 824 | Casco infantil incluido en cada alquiler |
| es | 825 | Muñequeras, rodilleras y coderas incluidas |
| es | 826 | Tallas UE 35 a 42 |
| es | 827 | Ayuda con la talla y prueba en la recogida |
| es | 862 | RSB es una tienda local de alquiler en Carrer de Salvador Espriu, en la Vila Olímpica, cerca de la playa de la Barceloneta y el Port Olímpic. Es un punto de salida cómodo para patinar con calma por el paseo marítimo o por el centro de Barcelona. |
| es | 867 | Abierto todos los días: 10:30–13:30 y 16:30–20:00. Ofrecemos alquileres por horas y por días. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines. Las tallas van de la UE 35 a la 42, y nuestro equipo local da instrucciones básicas y recomendaciones de ruta. Para ideas de rutas y consejos prácticos, puedes leer nuestra guía de alquiler de patines de 4 ruedas en Barcelona. |
| es | 912 | No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar. |
| es | 915 | ¿Está incluido el equipo de protección? |
| es | 916 | Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines. |
| es | 923 | ¿Qué tallas hay disponibles? |
| es | 924 | Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda. |
| es | 928 | Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42. |
| es | 932 | No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido. |
| es | 940 | Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad. |
| es | 950 | Descubre otros servicios de alquiler de nuestra tienda en la Vila Olímpica y consulta guías locales de las principales actividades que ofrecemos en Barcelona. |
| es | 964 | Precios de patines de 4 ruedas y extras incluidos |
| es | 964 | Lista de precios resumida de nuestra tienda local en la Vila Olímpica, cerca del Port Olímpic y la Barceloneta. |
| es | 964 | Casco infantil incluido · Muñequeras, rodilleras y coderas incluidas · Ayuda con la talla en la tienda · Guarda de zapatos, chaquetas, bolsas y maletas. |
| es | 972 | Consulta disponibilidad para alquilar patines de 4 ruedas en Barcelona |
| es | 973 | Escríbenos por WhatsApp o visita nuestra tienda en la Vila Olímpica para organizar tu alquiler de patines cerca de la playa de la Barceloneta. Nuestro equipo te ayudará a elegir la talla correcta y recomendará las mejores rutas. |
| fr | 654 | Louez des patins à roulettes et rollers quad dans notre boutique locale à Vila Olímpica del Poblenou, face à la plage et à côté du Port Olímpic. Patins classiques à quatre roues, stables pour grands enfants, adolescents et adultes, avec casque pour enfant, protège-poignets, genouillères et coudières inclus. Consigne gratuite, conseils d’itinéraires et tailles EU 35–42. |
| fr | 688 | Protège-poignets, genouillères et coudières inclus |
| fr | 689 | Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins. |
| fr | 702 | Voici les prix publics actuels pour notre service de location de patins à roulettes et rollers quad. Vous pouvez aussi comparer tous les tarifs sur notre page des prix, et nous contacter sur WhatsApp pour confirmer la disponibilité ou réserver votre pointure avant de venir. |
| fr | 714 | Idéal pour la Barceloneta, le Port Olímpic et le parc de la Ciutadella à votre rythme. |
| fr | 719 | Idéal pour des parcours plus longs en bord de mer et une balade tranquille dans le parc. |
| fr | 738 | Protections et extras pour patins |
| fr | 756 | Casque pour enfant inclus avec chaque location |
| fr | 757 | Protège-poignets, genouillères et coudières inclus |
| fr | 759 | Aide pour la pointure et essayage au retrait |
| fr | 799 | Ouvert tous les jours : 10:30–13:30 et 16:30–20:00. Nous proposons des locations à l’heure et à la journée. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins. Les pointures vont du 35 au 42, et notre équipe locale fournit des instructions de base et des conseils d’itinéraires. Pour des idées d’itinéraires locaux et des conseils pratiques, vous pouvez lire notre guide de location de patins à roulettes à Barcelone. |
| fr | 817 | Notre boutique se trouve à la Vila Olímpica, près de la plage de la Barceloneta et du Port Olímpic. Elle est idéalement située pour récupérer vos patins à roulettes et rejoindre les chemins plats du bord de mer ou explorer le centre de Barcelone. |
| fr | 844 | Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer. |
| fr | 847 | Les protections sont-elles incluses dans la location ? |
| fr | 848 | Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins. |
| fr | 863 | Faut-il un permis pour louer des patins ? |
| fr | 864 | Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide. |
| fr | 881 | Plus de locations et guides locaux à Barcelone |
| fr | 882 | Découvrez les autres services de location de notre boutique de la Vila Olímpica et consultez nos guides locaux sur les principales activités que nous proposons à Barcelone. |
| fr | 896 | Casque pour enfant inclus · Protège-poignets, genouillères et coudières inclus · Aide pour la pointure en boutique · Consigne pour chaussures, vestes, sacs et bagages. |
| fr | 905 | Écrivez-nous sur WhatsApp ou passez à notre boutique de la Vila Olímpica pour organiser votre location de patins à roulettes près de la plage de la Barceloneta. Notre équipe vous aidera à choisir la bonne pointure et les meilleurs itinéraires. |
| it | 659 | Noleggia pattini a rotelle e pattini a quattro ruote nel nostro negozio locale a Vila Olímpica del Poblenou, vicino alla spiaggia della Barceloneta e al Port Olímpic. Pattini classici stabili per ragazzi, adolescenti e adulti, casco per bambini, polsiere, ginocchiere e gomitiere inclusi. Deposito gratuito, consigli sui percorsi e taglie EU 35–42. |
| it | 693 | Protezioni incluse |
| it | 694 | Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini. |
| it | 707 | Questi sono i prezzi pubblici attuali per il nostro servizio di noleggio pattini a rotelle e pattini a quattro ruote. Puoi anche confrontare tutte le tariffe nella nostra pagina prezzi, e contattarci su WhatsApp per confermare la disponibilità o prenotare la tua taglia prima di venire. |
| it | 719 | Ideale per la Barceloneta, il Port Olímpic e il Parc de la Ciutadella al tuo ritmo. |
| it | 724 | Ideale per percorsi più lunghi sul mare e giri tranquilli nel parco. |
| it | 739 | Estendi il noleggio di un altro giorno a una tariffa ridotta. |
| it | 743 | Protezioni ed extra per pattini |
| it | 761 | Casco per bambini incluso con ogni noleggio |
| it | 762 | Polsiere, ginocchiere e gomitiere incluse |
| it | 766 | Deposito gratuito per scarpe, giacche e bagagli nel nostro negozio sorvegliato |
| it | 804 | Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00. Offriamo noleggi a ore e a giornata. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini. Le taglie vanno dal 35 al 42 EU e il nostro team locale fornisce istruzioni di base e consigli sui percorsi. Per idee di percorsi locali e consigli pratici, puoi leggere la nostra guida al noleggio di pattini a rotelle a Barcellona. |
| it | 852 | Le protezioni sono incluse nel noleggio? |
| it | 853 | Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini. |
| it | 857 | Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio. |
| it | 869 | Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido. |
| it | 886 | Altri noleggi a Barcellona e guide locali |
| it | 887 | Scopri gli altri servizi di noleggio del nostro negozio alla Vila Olímpica e consulta le guide locali sulle principali attività che offriamo a Barcellona. |
| it | 901 | Casco per bambini incluso · Polsiere, ginocchiere e gomitiere incluse · Aiuto con la taglia in negozio · Deposito per scarpe, giacche, borse e bagagli. |
| de | 661 | Miete Rollschuhe und Quad-Skates in unserem lokalen Geschäft in Vila Olímpica del Poblenou, direkt gegenüber dem Strand und neben dem Port Olímpic. Stabile klassische Rollschuhe für ältere Kinder, Jugendliche und Erwachsene, Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive. Kostenlose Aufbewahrung, Routentipps und Größen EU 35–42. |
| de | 692 | Wähle gut gepflegte Rollschuhe und Quad-Skates für ältere Kinder, Jugendliche und Erwachsene, ideal für entspannte Fahrten am Strand und rund um die Vila Olímpica. |
| de | 696 | Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. |
| de | 709 | Dies sind die aktuellen öffentlichen Preise für unsere Rollschuhe- und Quad-Skates-Vermietung. Du kannst alle Tarife auch auf unserer Preisseite vergleichen und uns per WhatsApp kontaktieren, um die Verfügbarkeit zu bestätigen oder deine Größe vor dem Besuch zu reservieren. |
| de | 721 | Ideal für Barceloneta, Port Olímpic und den Parc de la Ciutadella in deinem eigenen Tempo. |
| de | 763 | Kinderhelm bei jeder Miete inklusive |
| de | 765 | Größen EU 35 bis 42 |
| de | 766 | Größenhilfe und Passformcheck bei der Abholung |
| de | 807 | Geöffnet von 10:30–13:30 und 16:30–20:00 Uhr. Wir bieten stunden- und tageweise Vermietung. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren Guide zum Rollschuhe mieten in Barcelona. |
| de | 846 | Unser Geschäft befindet sich in der Vila Olímpica, direkt gegenüber dem Strand und neben dem Port Olímpic. Es liegt ideal, um deine Rollschuhe abzuholen und die flachen Küstenwege oder das Zentrum von Barcelona zu erreichen. |
| de | 875 | Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe. |
| de | 881 | Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. |
| de | 890 | Welche Größen sind verfügbar? |
| de | 893 | Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden. |
| de | 899 | Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42. |
| de | 902 | Brauche ich einen Führerschein, um Rollschuhe zu mieten? |
| de | 905 | Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich. |
| de | 918 | Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben. |
| de | 927 | Weitere Verleihangebote und lokale Guides in Barcelona |
| de | 928 | Entdecke weitere Mietservices unseres Geschäfts in der Vila Olímpica und lies lokale Guides zu den wichtigsten Aktivitäten, die wir in Barcelona anbieten. |
| de | 942 | Kinderhelm inklusive · Handgelenkschoner, Knieschoner und Ellbogenschoner inklusive · Größenhilfe im Geschäft · Aufbewahrung für Schuhe, Jacken, Taschen und Gepäck. |
| de | 951 | Schreib uns per WhatsApp oder besuche unser Geschäft in der Vila Olímpica, um deine Rollschuhmiete nahe Barceloneta-Strand zu organisieren. Unser Team hilft bei der passenden Größe und empfiehlt die besten Routen. |
| nl | 670 | Huur rolschaatsen en quad skates bij onze lokale winkel in Vila Olímpica del Poblenou, tegenover het strand en naast Port Olímpic. Stabiele klassieke rolschaatsen voor oudere kinderen, tieners en volwassenen, een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen. Gratis bagageopslag, lokale routetips en maten EU 35–42. |
| nl | 705 | Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn bij elke huur inbegrepen. |
| nl | 718 | Dit zijn de actuele openbare prijzen voor onze verhuur van rolschaatsen en quad skates. Je kunt alle tarieven ook vergelijken op onze prijzenpagina en via WhatsApp contact met ons opnemen om de beschikbaarheid te bevestigen of je maat te reserveren voordat je langskomt. |
| nl | 730 | Ideaal voor Barceloneta, Port Olímpic en Parc de la Ciutadella in je eigen tempo. |
| nl | 740 | Geniet een volledige dag van klassieke rolschaatsen met flexibele terugbrengmogelijkheid op dezelfde dag. |
| nl | 772 | Kinderhelm inbegrepen bij elke huur |
| nl | 773 | Polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen |
| nl | 775 | Hulp met maat en pasvorm bij ophalen |
| nl | 816 | Elke dag geopend: 10:30–13:30 en 16:30–20:00. We verhuren per uur en per dag. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn inbegrepen bij elke huur. De maten lopen van EU 35 tot 42, en ons lokale team geeft basisinstructies en routetips. Voor lokale route-ideeën en praktische tips kun je onze gids voor rolschaatsen huren in Barcelona lezen. |
| nl | 855 | Onze winkel ligt in Vila Olímpica, dicht bij Barceloneta en Port Olímpic. Het is een ideale plek om je rolschaatsen op te halen en de vlakke kustpaden of het centrum van Barcelona te bereiken. |
| nl | 884 | Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen. |
| nl | 890 | Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen. |
| nl | 911 | Heb ik een rijbewijs nodig om rolschaatsen te huren? |
| nl | 914 | Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende. |
| nl | 927 | Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid. |
| nl | 936 | Meer verhuur in Barcelona en lokale gidsen |
| nl | 937 | Ontdek gerelateerde verhuurdiensten van onze winkel in Vila Olímpica en bekijk lokale gidsen over de belangrijkste activiteiten die we in Barcelona aanbieden. |
| nl | 951 | Kinderhelm inbegrepen · Polsbeschermers, kniebeschermers en elleboogbeschermers inbegrepen · Maatadvies in de winkel · Opslag voor schoenen, jassen, tassen en bagage. |
| nl | 959 | Check beschikbaarheid voor rolschaatsen huren in Barcelona |
| nl | 960 | Stuur ons een WhatsApp of kom langs in onze winkel in Vila Olímpica om je rolschaatsenhuur bij Barceloneta te regelen. Ons team helpt je met de juiste maat en de beste routes. |
| pt | 676 | Aluga patins de 4 rodas e patins clássicos na nossa loja local em Vila Olímpica del Poblenou, perto da praia da Barceloneta e do Port Olímpic. Patins tradicionais estáveis para crianças mais velhas, adolescentes e adultos, capacete infantil, proteções de pulso, joelheiras e cotoveleiras incluídos. Dispomos de um serviço gratuito de guarda de bagagem, damos dicas de percursos locais e temos tamanhos EU 35–42. |
| pt | 710 | Proteções incluídas |
| pt | 711 | Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins. |
| pt | 724 | Estes são os preços públicos atuais do nosso serviço de aluguer de patins de 4 rodas e patins clássicos. Também podes comparar todas as tarifas na nossa página de preços, e contactar-nos por WhatsApp para confirmar disponibilidade ou reservar o teu tamanho antes da visita. |
| pt | 730 | Perfeito para uma volta rápida junto ao mar ou para experimentar patins de 4 rodas pela primeira vez. |
| pt | 736 | Ideal para a Barceloneta, o Port Olímpic e o Parc de la Ciutadella ao teu ritmo. |
| pt | 756 | Prolonga o aluguer por mais um dia com uma tarifa reduzida. |
| pt | 760 | Proteções e extras para patins |
| pt | 778 | Capacete infantil incluído em cada aluguer |
| pt | 779 | Proteções de pulso, joelheiras e cotoveleiras incluídas |
| pt | 783 | Serviço gratuito de guarda de bagagem para sapatos, casacos e bagagem na nossa loja supervisionada |
| pt | 816 | A RSB é uma loja local de aluguer na Carrer de Salvador Espriu, na Vila Olímpica, perto da praia da Barceloneta e do Port Olímpic. É um ponto de partida prático para patinar tranquilamente junto ao mar ou pelo centro de Barcelona. |
| pt | 821 | Aberto todos os dias: 10:30–13:30 e 16:30–20:00. Temos alugueres à hora e ao dia com horários de devolução flexíveis. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins. Os tamanhos vão do EU 35 ao 42, e a nossa equipa local dá instruções básicas e conselhos de rota. Para ideias de rotas locais e dicas práticas, podes ler o nosso guia de aluguer de patins de 4 rodas em Barcelona. |
| pt | 890 | O equipamento de proteção está incluído? |
| pt | 891 | Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins. |
| pt | 907 | Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido. |
| pt | 911 | Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada. |
| pt | 915 | Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade. |
| pt | 925 | Descobre outros serviços de aluguer da nossa loja na Vila Olímpica e consulta guias locais sobre as principais atividades que oferecemos em Barcelona. |
| pt | 939 | Capacete infantil incluído · Proteções de pulso, joelheiras e cotoveleiras incluídas · Ajuda com o tamanho na loja · Guarda de sapatos, casacos, malas e bagagem. |
| pt | 947 | Verificar disponibilidade para alugar patins de 4 rodas em Barcelona |
| ca | 659 | Lloga patins de 4 rodes i patins clàssics a la nostra botiga local de Vila Olímpica del Poblenou, a prop de la platja de la Barceloneta i el Port Olímpic. Patins tradicionals estables per a nens grans, adolescents i adults, amb casc infantil, canelleres, genolleres i colzeres inclosos. Servei gratuït de guarda d’equipatge, consells de rutes locals i talles de la UE 35–42. |
| ca | 693 | Proteccions incloses |
| ca | 694 | Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins. |
| ca | 707 | Aquests són els preus públics actuals del nostre servei de lloguer de patins de 4 rodes i patins clàssics. També pots comparar totes les tarifes a la nostra pàgina de preus, i contactar-nos per WhatsApp per confirmar disponibilitat o reservar la teva talla abans de venir. |
| ca | 713 | Perfecte per fer una volta ràpida pel passeig marítim o provar patins de 4 rodes per primera vegada. |
| ca | 719 | Ideal per recórrer la Barceloneta, el Port Olímpic i el Parc de la Ciutadella al teu ritme. |
| ca | 743 | Proteccions i extres per a patins |
| ca | 761 | Casc infantil inclòs amb cada lloguer |
| ca | 764 | Ajuda amb la talla i prova en la recollida |
| ca | 767 | Servei gratuït de guarda d’equipatge per a sabates, jaquetes i equipatge a la nostra botiga supervisada |
| ca | 800 | RSB és una botiga local de lloguer al Carrer de Salvador Espriu, a la Vila Olímpica, prop de la platja de la Barceloneta i el Port Olímpic. És un punt de sortida còmode per patinar tranquil·lament pel passeig marítim o pel centre de Barcelona. |
| ca | 805 | Obert cada dia: 10:30–13:30 i 16:30–20:00. Oferim lloguers per hores i per dies. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins. Les talles van de la talla 35 a la 42 de la UE, i el nostre equip local dona instruccions bàsiques i recomanacions de ruta. Per a idees de rutes i consells pràctics, pots llegir la nostra guia de lloguer de patins de 4 rodes a Barcelona. |
| ca | 871 | No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar. |
| ca | 874 | L’equip de protecció està inclòs? |
| ca | 875 | Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins. |
| ca | 891 | No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid. |
| ca | 895 | Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer. |
| ca | 923 | Llista de preus resumida de la nostra botiga local a la Vila Olímpica, prop del Port Olímpic i la Barceloneta. |
| ca | 923 | Casc infantil, canelleres, genolleres i colzeres inclosos · Ajuda amb la talla a la botiga · Guarda de sabates, jaquetes, bosses i equipatge. |
| ca | 932 | Escriu-nos per WhatsApp o visita la nostra botiga a la Vila Olímpica per organitzar el teu lloguer de patins prop de la platja de la Barceloneta. El nostre equip t’ajudarà a triar la talla correcta i et recomanarà les millors rutes. |
| sv | 671 | Hyra rullskridskor i Barcelona |
| sv | 672 | Hyr rullskridskor och quad skates i vår lokala butik i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Stabila klassiska rullskridskor för äldre barn, tonåringar och vuxna, barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår. Gratis förvaring, lokala ruttips och storlekar EU 35–42. |
| sv | 702 | Klassiska rullskridskor |
| sv | 703 | Välj välskötta rullskridskor och quad skates för äldre barn, tonåringar och vuxna, redo för avslappnad åkning vid stranden och runt Vila Olímpica. |
| sv | 707 | Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor utan extra kostnad. |
| sv | 710 | Enkla rutter vid havet |
| sv | 718 | Priser för rullskridskor |
| sv | 719 | Priser för att hyra rullskridskor i Barcelona |
| sv | 720 | Detta är våra aktuella priser för uthyrning av rullskridskor och quad skates. Du kan också jämföra alla priser på vår prissida, och kontakta oss via WhatsApp för att kontrollera tillgänglighet eller reservera din storlek innan du kommer. |
| sv | 742 | Njut av en hel dag med klassiska rullskridskor och flexibel återlämning samma dag. |
| sv | 747 | Hämta idag och lämna tillbaka imorgon för att förlänga åktiden till nästa dag. |
| sv | 756 | Skydd som ingår för rullskridskor |
| sv | 771 | Vad ingår när du hyr rullskridskor |
| sv | 772 | Vår uthyrning av rullskridskor är enkel och praktisk för besökare nära Barceloneta, Vila Olímpica och centrala Barcelona. |
| sv | 774 | Barnhjälm ingår i varje hyra |
| sv | 776 | Storlekar EU 35 till 42 |
| sv | 777 | Storlekshjälp och passformskontroll vid hämtning |
| sv | 812 | Varför välja vår lokala uthyrning av rullskridskor |
| sv | 813 | RSB är en lokal uthyrningsbutik på Carrer de Salvador Espriu i Vila Olímpica, mitt emot stranden och intill Port Olímpic. Det är en praktisk startpunkt för avslappnad rullskridskoåkning längs havet eller i centrala Barcelona. |
| sv | 818 | Öppet varje dag: 10:30–13:30 och 16:30–20:00. Vi erbjuder uthyrning per timme och per dag. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor. Storlekarna går från EU 35 till 42, och vårt lokala team ger grundläggande instruktioner och ruttips. För lokala ruttips och praktiska råd kan du läsa vår guide för att hyra rullskridskor i Barcelona. |
| sv | 856 | Hitta vår uthyrning av rullskridskor i Vila Olímpica, Barcelona |
| sv | 857 | Vår butik ligger i Vila Olímpica, mitt emot stranden och intill Port Olímpic. Den ligger perfekt för att hämta dina rullskridskor och nå de plana kustvägarna eller utforska centrala Barcelona. |
| sv | 879 | Vanliga frågor om att hyra rullskridskor i Barcelona |
| sv | 883 | Behöver jag erfarenhet för att hyra rullskridskor? |
| sv | 884 | Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar. |
| sv | 888 | Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor. |
| sv | 891 | Var kan jag åka rullskridskor nära butiken? |
| sv | 892 | Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken. |
| sv | 895 | Vilka storlekar finns? |
| sv | 896 | Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste. |
| sv | 899 | Kan tonåringar hyra rullskridskor? |
| sv | 900 | Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42. |
| sv | 903 | Behöver jag körkort för att hyra rullskridskor? |
| sv | 904 | Nej. Inget körkort krävs för att hyra rullskridskor. |
| sv | 913 | Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet. |
| sv | 922 | Fler uthyrningar i Barcelona och lokala guider |
| sv | 923 | Upptäck fler uthyrningstjänster från vår butik i Vila Olímpica och läs lokala guider om de viktigaste aktiviteterna vi erbjuder i Barcelona. |
| sv | 934 | Hyra rullskridskor i Barcelona |
| sv | 937 | Priser för rullskridskor och inkluderade tillbehör |
| sv | 937 | Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår · Hjälp med storlek i butiken · Förvaring av skor, jackor, väskor och bagage. |
| sv | 945 | Kontrollera tillgänglighet för att hyra rullskridskor i Barcelona |
| sv | 946 | Skriv till oss på WhatsApp eller besök vår butik i Vila Olímpica för att ordna uthyrning av rullskridskor nära Barceloneta. Vårt team hjälper dig välja rätt storlek och rekommenderar de bästa rutterna. |
| pl | 728 | Wynajmij klasyczne wrotki w naszej lokalnej wypożyczalni w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Stabilne klasyczne wrotki dla starszych dzieci, nastolatków i dorosłych, kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie w cenie. Darmowe przechowanie bagażu, lokalne wskazówki tras i rozmiary EU 35–42. |
| pl | 763 | Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek. |
| pl | 776 | To są aktualne publiczne ceny naszej usługi wynajmu wrotek. Możesz też porównać wszystkie stawki na naszej stronie cennika i skontaktować się z nami przez WhatsApp, aby potwierdzić dostępność lub zarezerwować rozmiar przed wizytą. |
| pl | 782 | Idealne na krótką przejażdżkę nad morzem albo pierwszą próbę jazdy na wrotkach. |
| pl | 788 | Idealne do odkrywania Barceloneta, Port Olímpic i parku Ciutadella we własnym tempie. |
| pl | 830 | Kask dziecięcy wliczony w każdy wynajem wrotek |
| pl | 832 | Rozmiary od EU 35 do 42 |
| pl | 833 | Pomoc w doborze rozmiaru i sprawdzenie dopasowania przy odbiorze |
| pl | 874 | Otwarte codziennie: 10:30–13:30 i 16:30–20:00. Oferujemy wynajem na godziny i dni. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek. Rozmiary obejmują EU 35–42, a nasz lokalny zespół udziela podstawowych instrukcji i wskazówek tras. Lokalne pomysły na trasy i praktyczne wskazówki znajdziesz w naszym przewodniku po wynajmie wrotek w Barcelonie. |
| pl | 911 | Nasza wypożyczalnia znajduje się w Vila Olímpica, naprzeciwko plaży i obok Port Olímpic. To idealne miejsce, aby odebrać wrotki i ruszyć na płaskie nadmorskie ścieżki lub odkrywać centrum Barcelony. |
| pl | 938 | Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem. |
| pl | 942 | Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek. |
| pl | 949 | Jakie rozmiary są dostępne? |
| pl | 950 | Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie. |
| pl | 954 | Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42. |
| pl | 958 | Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy. |
| pl | 967 | Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność. |
| pl | 991 | Kask dziecięcy i ochraniacze na nadgarstki, kolana i łokcie w cenie · Pomoc w doborze rozmiaru w wypożyczalni · Przechowanie butów, kurtek, toreb i bagażu. |
| pl | 1000 | Napisz do nas na WhatsApp albo odwiedź naszą wypożyczalnię w Vila Olímpica, aby zorganizować wynajem wrotek blisko plaży Barceloneta. Nasz zespół pomoże dobrać właściwy rozmiar i poleci najlepsze trasy. |

## S. MATRIZ FAQ VISIBLE ↔ SCHEMA

| Idioma | N.º | Visible completo | Schema completo | Pregunta coincide | Respuesta coincide |
| --- | --- | --- | --- | --- | --- |
| en | 1 | {"line": 937, "question": "Do I need experience to rent roller skates?", "answer": "No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Do I need experience to rent roller skates?", "answer": "No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start.", "answer_raw": "No, you do not need previous experience. We provide stable roller skates for beginners and more confident skaters, and our team can help you choose the right fit before you start."} | True | True |
| en | 2 | {"line": 941, "question": "Is protective gear included with the rental?", "answer": "Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Is protective gear included with the rental?", "answer": "Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost.", "answer_raw": "Yes. Children's helmet, wrist guards, knee pads and elbow pads are included with every roller skate rental at no extra cost."} | True | True |
| en | 3 | {"line": 945, "question": "Where can I roller skate near the shop?", "answer": "Our rental shop is just steps from the seafront promenade and Port Olímpic. The flat coastal paths and Ciutadella Park offer good routes for relaxed roller skating near our store.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Where can I roller skate near the shop?", "answer": "Our rental shop is just steps from the seafront promenade and Port Olímpic. The flat coastal paths and Ciutadella Park offer good routes for relaxed roller skating near our store.", "answer_raw": "Our rental shop is just steps from the seafront promenade and Port Olímpic. The flat coastal paths and Ciutadella Park offer good routes for relaxed roller skating near our store."} | True | True |
| en | 4 | {"line": 949, "question": "What sizes are available?", "answer": "We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "What sizes are available?", "answer": "We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit.", "answer_raw": "We offer roller skates in EU sizes 35 to 42. You can try different sizes at the shop to find the most comfortable fit."} | True | True |
| en | 5 | {"line": 953, "question": "Can teenagers rent roller skates?", "answer": "Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Can teenagers rent roller skates?", "answer": "Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range.", "answer_raw": "Yes. Our roller skates fit older children, teenagers and adults within the available EU 35 to 42 size range."} | True | True |
| en | 6 | {"line": 957, "question": "Do I need a licence to rent roller skates?", "answer": "No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Do I need a licence to rent roller skates?", "answer": "No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID.", "answer_raw": "No driving licence is needed. Roller skates are a non‑motorised activity so anyone can rent them with a valid ID."} | True | True |
| en | 7 | {"line": 961, "question": "Can I store my shoes or luggage at the shop?", "answer": "Yes. Free storage for shoes, jackets, handbags, backpacks and suitcases is available in our supervised shop during your rental.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Can I store my shoes or luggage at the shop?", "answer": "Yes. Free storage for shoes, jackets, handbags, backpacks and suitcases is available in our supervised shop during your rental.", "answer_raw": "Yes. Free storage for shoes, jackets, handbags, backpacks and suitcases is available in our supervised shop during your rental."} | True | True |
| en | 8 | {"line": 965, "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "How do I book or contact you?", "answer": "You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability.", "answer_raw": "You can book via WhatsApp, email or phone. Find all contact details on our website and feel free to ask if you have any questions about sizes or availability."} | True | True |
| es | 1 | {"line": 910, "question": "¿Necesito experiencia para alquilar patines?", "answer": "No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "¿Necesito experiencia para alquilar patines?", "answer": "No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar.", "answer_raw": "No, no necesitas experiencia previa. Ofrecemos patines estables para principiantes y patinadores con más seguridad, y nuestro equipo te ayuda a elegir la talla adecuada antes de empezar."} | True | True |
| es | 2 | {"line": 914, "question": "¿Está incluido el equipo de protección?", "answer": "Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "¿Está incluido el equipo de protección?", "answer": "Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines.", "answer_raw": "Sí. El casco infantil, las muñequeras, las rodilleras y las coderas están incluidos con cada alquiler de patines."} | True | True |
| es | 3 | {"line": 918, "question": "¿Dónde puedo patinar cerca de la tienda?", "answer": "Nuestra tienda está a pocos pasos del paseo marítimo y del Port Olímpic. Los caminos llanos de la costa y el Parc de la Ciutadella ofrecen buenas rutas para patinar con calma cerca de la tienda.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "¿Dónde puedo patinar cerca de la tienda?", "answer": "Nuestra tienda está a pocos pasos del paseo marítimo y del Port Olímpic. Los caminos llanos de la costa y el Parc de la Ciutadella ofrecen buenas rutas para patinar con calma cerca de la tienda.", "answer_raw": "Nuestra tienda está a pocos pasos del paseo marítimo y del Port Olímpic. Los caminos llanos de la costa y el Parc de la Ciutadella ofrecen buenas rutas para patinar con calma cerca de la tienda."} | True | True |
| es | 4 | {"line": 922, "question": "¿Qué tallas hay disponibles?", "answer": "Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "¿Qué tallas hay disponibles?", "answer": "Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda.", "answer_raw": "Tenemos patines en tallas UE 35 a 42. Puedes probar varias tallas en la tienda para encontrar la más cómoda."} | True | True |
| es | 5 | {"line": 926, "question": "¿Pueden alquilar patines los adolescentes?", "answer": "Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "¿Pueden alquilar patines los adolescentes?", "answer": "Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42.", "answer_raw": "Sí. Nuestros patines sirven para niños mayores, adolescentes y adultos dentro del rango de tallas UE 35 a 42."} | True | True |
| es | 6 | {"line": 930, "question": "¿Necesito carnet para alquilar patines?", "answer": "No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "¿Necesito carnet para alquilar patines?", "answer": "No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido.", "answer_raw": "No se necesita carnet de conducir. Los patines son una actividad no motorizada, así que cualquier persona puede alquilarlos con DNI o pasaporte válido."} | True | True |
| es | 7 | {"line": 934, "question": "¿Puedo dejar mis zapatos o maletas en la tienda?", "answer": "Sí. Tenemos consigna gratuita para zapatos, chaquetas, bolsos, mochilas y maletas en nuestra tienda supervisada durante el alquiler.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "¿Puedo dejar mis zapatos o maletas en la tienda?", "answer": "Sí. Tenemos consigna gratuita para zapatos, chaquetas, bolsos, mochilas y maletas en nuestra tienda supervisada durante el alquiler.", "answer_raw": "Sí. Tenemos consigna gratuita para zapatos, chaquetas, bolsos, mochilas y maletas en nuestra tienda supervisada durante el alquiler."} | True | True |
| es | 8 | {"line": 938, "question": "¿Cómo reservo o contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "¿Cómo reservo o contacto con vosotros?", "answer": "Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad.", "answer_raw": "Puedes reservar por WhatsApp, email o teléfono. Encontrarás todos los datos de contacto en nuestra web y puedes preguntarnos cualquier duda sobre tallas o disponibilidad."} | True | True |
| fr | 1 | {"line": 842, "question": "Faut-il de l’expérience pour louer des patins à roulettes ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Faut-il de l’expérience pour louer des patins à roulettes ?", "answer": "Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer.", "answer_raw": "Non, aucune expérience préalable n’est nécessaire. Nous proposons des patins stables pour débutants et patineurs plus à l’aise, et notre équipe vous aide à choisir la bonne pointure avant de commencer."} | True | True |
| fr | 2 | {"line": 846, "question": "Les protections sont-elles incluses dans la location ?", "answer": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Les protections sont-elles incluses dans la location ?", "answer": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins.", "answer_raw": "Oui. Un casque pour enfant, des protège-poignets, des genouillères et des coudières sont inclus avec chaque location de patins."} | True | True |
| fr | 3 | {"line": 850, "question": "Où puis-je patiner près de la boutique ?", "answer": "Notre boutique se trouve face à la plage et à côté du Port Olímpic. Les chemins plats du bord de mer et le parc de la Ciutadella offrent de bons itinéraires pour patiner tranquillement près de la boutique.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Où puis-je patiner près de la boutique ?", "answer": "Notre boutique se trouve face à la plage et à côté du Port Olímpic. Les chemins plats du bord de mer et le parc de la Ciutadella offrent de bons itinéraires pour patiner tranquillement près de la boutique.", "answer_raw": "Notre boutique se trouve face à la plage et à côté du Port Olímpic. Les chemins plats du bord de mer et le parc de la Ciutadella offrent de bons itinéraires pour patiner tranquillement près de la boutique."} | True | True |
| fr | 4 | {"line": 854, "question": "Quelles pointures sont disponibles ?", "answer": "Nous proposons des patins à roulettes en pointures EU 35 à 42. Vous pouvez essayer plusieurs pointures en boutique pour trouver la plus confortable.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Quelles pointures sont disponibles ?", "answer": "Nous proposons des patins à roulettes en pointures EU 35 à 42. Vous pouvez essayer plusieurs pointures en boutique pour trouver la plus confortable.", "answer_raw": "Nous proposons des patins à roulettes en pointures EU 35 à 42. Vous pouvez essayer plusieurs pointures en boutique pour trouver la plus confortable."} | True | True |
| fr | 5 | {"line": 858, "question": "Les adolescents peuvent-ils louer des patins ?", "answer": "Oui. Nos patins conviennent aux grands enfants, adolescents et adultes dans les pointures EU 35 à 42 disponibles.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Les adolescents peuvent-ils louer des patins ?", "answer": "Oui. Nos patins conviennent aux grands enfants, adolescents et adultes dans les pointures EU 35 à 42 disponibles.", "answer_raw": "Oui. Nos patins conviennent aux grands enfants, adolescents et adultes dans les pointures EU 35 à 42 disponibles."} | True | True |
| fr | 6 | {"line": 862, "question": "Faut-il un permis pour louer des patins ?", "answer": "Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Faut-il un permis pour louer des patins ?", "answer": "Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide.", "answer_raw": "Aucun permis de conduire n’est nécessaire. Les patins à roulettes sont une activité non motorisée, il suffit d’une pièce d’identité valide."} | True | True |
| fr | 7 | {"line": 866, "question": "Puis-je laisser mes chaussures ou mes bagages à la boutique ?", "answer": "Oui. Une consigne gratuite pour chaussures, vestes, sacs à main, sacs à dos et valises est disponible dans notre boutique surveillée pendant votre location.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puis-je laisser mes chaussures ou mes bagages à la boutique ?", "answer": "Oui. Une consigne gratuite pour chaussures, vestes, sacs à main, sacs à dos et valises est disponible dans notre boutique surveillée pendant votre location.", "answer_raw": "Oui. Une consigne gratuite pour chaussures, vestes, sacs à main, sacs à dos et valises est disponible dans notre boutique surveillée pendant votre location."} | True | True |
| fr | 8 | {"line": 870, "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver par WhatsApp, e-mail ou téléphone. Retrouvez toutes les coordonnées sur notre site et contactez-nous si vous avez des questions sur les pointures ou les disponibilités.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Comment réserver ou vous contacter ?", "answer": "Vous pouvez réserver par WhatsApp, e-mail ou téléphone. Retrouvez toutes les coordonnées sur notre site et contactez-nous si vous avez des questions sur les pointures ou les disponibilités.", "answer_raw": "Vous pouvez réserver par WhatsApp, e-mail ou téléphone. Retrouvez toutes les coordonnées sur notre site et contactez-nous si vous avez des questions sur les pointures ou les disponibilités."} | True | True |
| it | 1 | {"line": 847, "question": "Serve esperienza per noleggiare pattini a rotelle?", "answer": "No, non serve esperienza. Offriamo pattini stabili per principianti e pattinatori più sicuri, e il nostro team ti aiuta a scegliere la taglia giusta prima di iniziare.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Serve esperienza per noleggiare pattini a rotelle?", "answer": "No, non serve esperienza. Offriamo pattini stabili per principianti e pattinatori più sicuri, e il nostro team ti aiuta a scegliere la taglia giusta prima di iniziare.", "answer_raw": "No, non serve esperienza. Offriamo pattini stabili per principianti e pattinatori più sicuri, e il nostro team ti aiuta a scegliere la taglia giusta prima di iniziare."} | True | True |
| it | 2 | {"line": 851, "question": "Le protezioni sono incluse nel noleggio?", "answer": "Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Le protezioni sono incluse nel noleggio?", "answer": "Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini.", "answer_raw": "Sì. Casco per bambini, polsiere, ginocchiere e gomitiere sono inclusi con ogni noleggio di pattini."} | True | True |
| it | 3 | {"line": 855, "question": "Dove posso pattinare vicino al negozio?", "answer": "Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Dove posso pattinare vicino al negozio?", "answer": "Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio.", "answer_raw": "Il nostro negozio si trova di fronte alla spiaggia e accanto al Port Olímpic. I percorsi pianeggianti lungo la costa e il Parc de la Ciutadella sono ideali per pattinare con calma vicino al negozio."} | True | True |
| it | 4 | {"line": 859, "question": "Quali taglie sono disponibili?", "answer": "Abbiamo pattini a rotelle nelle taglie EU 35–42. Puoi provare diverse taglie in negozio per trovare la più comoda.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Quali taglie sono disponibili?", "answer": "Abbiamo pattini a rotelle nelle taglie EU 35–42. Puoi provare diverse taglie in negozio per trovare la più comoda.", "answer_raw": "Abbiamo pattini a rotelle nelle taglie EU 35–42. Puoi provare diverse taglie in negozio per trovare la più comoda."} | True | True |
| it | 5 | {"line": 863, "question": "Gli adolescenti possono noleggiare pattini?", "answer": "Sì. I nostri pattini vanno bene per ragazzi, adolescenti e adulti nelle taglie disponibili EU 35–42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Gli adolescenti possono noleggiare pattini?", "answer": "Sì. I nostri pattini vanno bene per ragazzi, adolescenti e adulti nelle taglie disponibili EU 35–42.", "answer_raw": "Sì. I nostri pattini vanno bene per ragazzi, adolescenti e adulti nelle taglie disponibili EU 35–42."} | True | True |
| it | 6 | {"line": 867, "question": "Serve una patente per noleggiare pattini?", "answer": "Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Serve una patente per noleggiare pattini?", "answer": "Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido.", "answer_raw": "Non serve la patente. I pattini a rotelle sono un’attività non motorizzata: basta un documento valido."} | True | True |
| it | 7 | {"line": 871, "question": "Posso lasciare scarpe o bagagli in negozio?", "answer": "Sì. Durante il noleggio puoi lasciare gratuitamente scarpe, giacche, borse, zaini e valigie nel nostro negozio sorvegliato.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso lasciare scarpe o bagagli in negozio?", "answer": "Sì. Durante il noleggio puoi lasciare gratuitamente scarpe, giacche, borse, zaini e valigie nel nostro negozio sorvegliato.", "answer_raw": "Sì. Durante il noleggio puoi lasciare gratuitamente scarpe, giacche, borse, zaini e valigie nel nostro negozio sorvegliato."} | True | True |
| it | 8 | {"line": 875, "question": "Come posso prenotare o contattarvi?", "answer": "Puoi prenotare via WhatsApp, e-mail o telefono. Trovi tutti i dettagli di contatto sul nostro sito e puoi scriverci se hai domande su taglie o disponibilità.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Come posso prenotare o contattarvi?", "answer": "Puoi prenotare via WhatsApp, e-mail o telefono. Trovi tutti i dettagli di contatto sul nostro sito e puoi scriverci se hai domande su taglie o disponibilità.", "answer_raw": "Puoi prenotare via WhatsApp, e-mail o telefono. Trovi tutti i dettagli di contatto sul nostro sito e puoi scriverci se hai domande su taglie o disponibilità."} | True | True |
| de | 1 | {"line": 871, "question": "Brauche ich Erfahrung, um Rollschuhe zu mieten?", "answer": "Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Brauche ich Erfahrung, um Rollschuhe zu mieten?", "answer": "Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe.", "answer_raw": "Nein, Vorerfahrung ist nicht nötig. Wir bieten stabile Rollschuhe für Anfänger und geübtere Fahrer, und unser Team hilft bei der passenden Größe."} | True | True |
| de | 2 | {"line": 877, "question": "Ist Schutzausrüstung in der Miete enthalten?", "answer": "Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Ist Schutzausrüstung in der Miete enthalten?", "answer": "Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive.", "answer_raw": "Ja. Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive."} | True | True |
| de | 3 | {"line": 883, "question": "Wo kann ich in der Nähe des Geschäfts Rollschuh fahren?", "answer": "Unser Geschäft liegt direkt gegenüber dem Strand und neben dem Port Olímpic. Die flachen Wege an der Küste und der Parc de la Ciutadella eignen sich gut für entspanntes Rollschuhfahren.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Wo kann ich in der Nähe des Geschäfts Rollschuh fahren?", "answer": "Unser Geschäft liegt direkt gegenüber dem Strand und neben dem Port Olímpic. Die flachen Wege an der Küste und der Parc de la Ciutadella eignen sich gut für entspanntes Rollschuhfahren.", "answer_raw": "Unser Geschäft liegt direkt gegenüber dem Strand und neben dem Port Olímpic. Die flachen Wege an der Küste und der Parc de la Ciutadella eignen sich gut für entspanntes Rollschuhfahren."} | True | True |
| de | 4 | {"line": 889, "question": "Welche Größen sind verfügbar?", "answer": "Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Welche Größen sind verfügbar?", "answer": "Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden.", "answer_raw": "Wir bieten Rollschuhe in den EU-Größen 35 bis 42 an. Du kannst im Geschäft verschiedene Größen ausprobieren, um die bequemste zu finden."} | True | True |
| de | 5 | {"line": 895, "question": "Können Jugendliche Rollschuhe mieten?", "answer": "Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Können Jugendliche Rollschuhe mieten?", "answer": "Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42.", "answer_raw": "Ja. Unsere Rollschuhe passen älteren Kindern, Jugendlichen und Erwachsenen im verfügbaren Größenbereich EU 35 bis 42."} | True | True |
| de | 6 | {"line": 901, "question": "Brauche ich einen Führerschein, um Rollschuhe zu mieten?", "answer": "Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Brauche ich einen Führerschein, um Rollschuhe zu mieten?", "answer": "Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich.", "answer_raw": "Nein. Für die Rollschuhmiete ist kein Führerschein erforderlich."} | True | True |
| de | 7 | {"line": 908, "question": "Kann ich meine Schuhe oder mein Gepäck im Geschäft lassen?", "answer": "Ja. Während der Miete können Schuhe, Jacken, Handtaschen, Rucksäcke und Koffer kostenlos in unserem betreuten Geschäft aufbewahrt werden.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kann ich meine Schuhe oder mein Gepäck im Geschäft lassen?", "answer": "Ja. Während der Miete können Schuhe, Jacken, Handtaschen, Rucksäcke und Koffer kostenlos in unserem betreuten Geschäft aufbewahrt werden.", "answer_raw": "Ja. Während der Miete können Schuhe, Jacken, Handtaschen, Rucksäcke und Koffer kostenlos in unserem betreuten Geschäft aufbewahrt werden."} | True | True |
| de | 8 | {"line": 914, "question": "Wie kann ich buchen oder Kontakt aufnehmen?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Wie kann ich buchen oder Kontakt aufnehmen?", "answer": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben.", "answer_raw": "Du kannst per WhatsApp, E-Mail oder Telefon buchen. Alle Kontaktdaten findest du auf unserer Website; bei Fragen zu Größen oder Verfügbarkeit kannst du uns jederzeit schreiben."} | True | True |
| nl | 1 | {"line": 880, "question": "Heb ik ervaring nodig om rolschaatsen te huren?", "answer": "Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Heb ik ervaring nodig om rolschaatsen te huren?", "answer": "Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen.", "answer_raw": "Nee, je hebt geen ervaring nodig. We hebben stabiele rolschaatsen voor beginners en ervaren rijders, en ons team helpt je de juiste maat te kiezen."} | True | True |
| nl | 2 | {"line": 886, "question": "Is bescherming inbegrepen bij de huur?", "answer": "Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Is bescherming inbegrepen bij de huur?", "answer": "Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen.", "answer_raw": "Ja. Een kinderhelm, polsbeschermers, kniebeschermers en elleboogbeschermers zijn altijd inbegrepen."} | True | True |
| nl | 3 | {"line": 892, "question": "Waar kan ik rolschaatsen in de buurt van de winkel?", "answer": "Onze verhuurwinkel ligt tegenover het strand en naast Port Olímpic. De vlakke kustpaden en Parc de la Ciutadella zijn goede routes om rustig te rolschaatsen.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Waar kan ik rolschaatsen in de buurt van de winkel?", "answer": "Onze verhuurwinkel ligt tegenover het strand en naast Port Olímpic. De vlakke kustpaden en Parc de la Ciutadella zijn goede routes om rustig te rolschaatsen.", "answer_raw": "Onze verhuurwinkel ligt tegenover het strand en naast Port Olímpic. De vlakke kustpaden en Parc de la Ciutadella zijn goede routes om rustig te rolschaatsen."} | True | True |
| nl | 4 | {"line": 898, "question": "Welke maten zijn beschikbaar?", "answer": "We hebben rolschaatsen in EU-maten 35 tot 42. Je kunt in de winkel verschillende maten passen om de meest comfortabele te vinden.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Welke maten zijn beschikbaar?", "answer": "We hebben rolschaatsen in EU-maten 35 tot 42. Je kunt in de winkel verschillende maten passen om de meest comfortabele te vinden.", "answer_raw": "We hebben rolschaatsen in EU-maten 35 tot 42. Je kunt in de winkel verschillende maten passen om de meest comfortabele te vinden."} | True | True |
| nl | 5 | {"line": 904, "question": "Kunnen tieners rolschaatsen huren?", "answer": "Ja. Onze rolschaatsen passen oudere kinderen, tieners en volwassenen binnen de beschikbare EU-maten 35 tot 42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Kunnen tieners rolschaatsen huren?", "answer": "Ja. Onze rolschaatsen passen oudere kinderen, tieners en volwassenen binnen de beschikbare EU-maten 35 tot 42.", "answer_raw": "Ja. Onze rolschaatsen passen oudere kinderen, tieners en volwassenen binnen de beschikbare EU-maten 35 tot 42."} | True | True |
| nl | 6 | {"line": 910, "question": "Heb ik een rijbewijs nodig om rolschaatsen te huren?", "answer": "Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Heb ik een rijbewijs nodig om rolschaatsen te huren?", "answer": "Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende.", "answer_raw": "Nee, je hebt geen rijbewijs nodig. Rolschaatsen is niet gemotoriseerd; een geldig identiteitsbewijs is voldoende."} | True | True |
| nl | 7 | {"line": 917, "question": "Kan ik mijn schoenen of bagage in de winkel achterlaten?", "answer": "Ja. Tijdens je huur kun je schoenen, jassen, handtassen, rugzakken en koffers gratis achterlaten in onze bewaakte winkel.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan ik mijn schoenen of bagage in de winkel achterlaten?", "answer": "Ja. Tijdens je huur kun je schoenen, jassen, handtassen, rugzakken en koffers gratis achterlaten in onze bewaakte winkel.", "answer_raw": "Ja. Tijdens je huur kun je schoenen, jassen, handtassen, rugzakken en koffers gratis achterlaten in onze bewaakte winkel."} | True | True |
| nl | 8 | {"line": 923, "question": "Hoe kan ik boeken of contact opnemen?", "answer": "Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hoe kan ik boeken of contact opnemen?", "answer": "Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid.", "answer_raw": "Je kunt boeken via WhatsApp, e-mail of telefoon. Alle contactgegevens staan op onze website. Stel gerust vragen over maten of beschikbaarheid."} | True | True |
| pt | 1 | {"line": 885, "question": "Preciso de experiência para alugar patins?", "answer": "Não, não precisas de experiência prévia. Temos patins estáveis para principiantes e patinadores mais confiantes, e a nossa equipa ajuda a escolher o tamanho certo antes de começar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Preciso de experiência para alugar patins?", "answer": "Não, não precisas de experiência prévia. Temos patins estáveis para principiantes e patinadores mais confiantes, e a nossa equipa ajuda a escolher o tamanho certo antes de começar.", "answer_raw": "Não, não precisas de experiência prévia. Temos patins estáveis para principiantes e patinadores mais confiantes, e a nossa equipa ajuda a escolher o tamanho certo antes de começar."} | True | True |
| pt | 2 | {"line": 889, "question": "O equipamento de proteção está incluído?", "answer": "Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "O equipamento de proteção está incluído?", "answer": "Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins.", "answer_raw": "Sim. Capacete infantil, proteções de pulso, joelheiras e cotoveleiras estão incluídos em cada aluguer de patins."} | True | True |
| pt | 3 | {"line": 893, "question": "Onde posso patinar perto da loja?", "answer": "A nossa loja fica a poucos passos do passeio marítimo e do Port Olímpic. Os caminhos planos junto à costa e o Parc de la Ciutadella são boas rotas para patinar tranquilamente perto da loja.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Onde posso patinar perto da loja?", "answer": "A nossa loja fica a poucos passos do passeio marítimo e do Port Olímpic. Os caminhos planos junto à costa e o Parc de la Ciutadella são boas rotas para patinar tranquilamente perto da loja.", "answer_raw": "A nossa loja fica a poucos passos do passeio marítimo e do Port Olímpic. Os caminhos planos junto à costa e o Parc de la Ciutadella são boas rotas para patinar tranquilamente perto da loja."} | True | True |
| pt | 4 | {"line": 897, "question": "Que tamanhos estão disponíveis?", "answer": "Temos patins nos tamanhos EU 35 a 42. Podes experimentar vários tamanhos na loja para encontrar o mais confortável.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Que tamanhos estão disponíveis?", "answer": "Temos patins nos tamanhos EU 35 a 42. Podes experimentar vários tamanhos na loja para encontrar o mais confortável.", "answer_raw": "Temos patins nos tamanhos EU 35 a 42. Podes experimentar vários tamanhos na loja para encontrar o mais confortável."} | True | True |
| pt | 5 | {"line": 901, "question": "Adolescentes podem alugar patins?", "answer": "Sim. Os nossos patins servem para crianças mais velhas, adolescentes e adultos dentro dos tamanhos EU 35 a 42 disponíveis.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Adolescentes podem alugar patins?", "answer": "Sim. Os nossos patins servem para crianças mais velhas, adolescentes e adultos dentro dos tamanhos EU 35 a 42 disponíveis.", "answer_raw": "Sim. Os nossos patins servem para crianças mais velhas, adolescentes e adultos dentro dos tamanhos EU 35 a 42 disponíveis."} | True | True |
| pt | 6 | {"line": 905, "question": "Preciso de carta para alugar patins?", "answer": "Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Preciso de carta para alugar patins?", "answer": "Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido.", "answer_raw": "Não é necessária carta de condução. Os patins são uma atividade não motorizada; basta um documento de identificação válido."} | True | True |
| pt | 7 | {"line": 909, "question": "Posso deixar os sapatos ou a bagagem na loja?", "answer": "Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Posso deixar os sapatos ou a bagagem na loja?", "answer": "Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada.", "answer_raw": "Sim. Durante o aluguer, podes usar o nosso serviço gratuito de guarda de bagagem para sapatos, casacos, malas de mão, mochilas e malas na loja supervisionada."} | True | True |
| pt | 8 | {"line": 913, "question": "Como posso reservar ou contactar-vos?", "answer": "Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Como posso reservar ou contactar-vos?", "answer": "Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade.", "answer_raw": "Podes reservar por WhatsApp, e-mail ou telefone. Podes encontrar todos os dados de contacto no nosso site e perguntar à vontade se tiveres dúvidas sobre tamanhos ou disponibilidade."} | True | True |
| ca | 1 | {"line": 869, "question": "Cal experiència per llogar patins?", "answer": "No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Cal experiència per llogar patins?", "answer": "No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar.", "answer_raw": "No, no cal experiència prèvia. Oferim patins estables per a principiants i patinadors amb més confiança, i el nostre equip t’ajuda a triar la talla adequada abans de començar."} | True | True |
| ca | 2 | {"line": 873, "question": "L’equip de protecció està inclòs?", "answer": "Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "L’equip de protecció està inclòs?", "answer": "Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins.", "answer_raw": "Sí. Casc infantil, canelleres, genolleres i colzeres estan inclosos amb cada lloguer de patins."} | True | True |
| ca | 3 | {"line": 877, "question": "On puc patinar a prop de la botiga?", "answer": "La nostra botiga és davant de la platja i al costat del Port Olímpic. Els camins costaners plans i el Parc de la Ciutadella ofereixen bones rutes per patinar tranquil·lament a prop de la botiga.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "On puc patinar a prop de la botiga?", "answer": "La nostra botiga és davant de la platja i al costat del Port Olímpic. Els camins costaners plans i el Parc de la Ciutadella ofereixen bones rutes per patinar tranquil·lament a prop de la botiga.", "answer_raw": "La nostra botiga és davant de la platja i al costat del Port Olímpic. Els camins costaners plans i el Parc de la Ciutadella ofereixen bones rutes per patinar tranquil·lament a prop de la botiga."} | True | True |
| ca | 4 | {"line": 881, "question": "Quines talles hi ha disponibles?", "answer": "Tenim patins en talles de la UE 35 a 42. Pots provar diverses talles a la botiga per trobar la més còmoda.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Quines talles hi ha disponibles?", "answer": "Tenim patins en talles de la UE 35 a 42. Pots provar diverses talles a la botiga per trobar la més còmoda.", "answer_raw": "Tenim patins en talles de la UE 35 a 42. Pots provar diverses talles a la botiga per trobar la més còmoda."} | True | True |
| ca | 5 | {"line": 885, "question": "Els adolescents poden llogar patins?", "answer": "Sí. Els nostres patins serveixen per a nens grans, adolescents i adults dins del rang de talles de la UE 35 a 42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Els adolescents poden llogar patins?", "answer": "Sí. Els nostres patins serveixen per a nens grans, adolescents i adults dins del rang de talles de la UE 35 a 42.", "answer_raw": "Sí. Els nostres patins serveixen per a nens grans, adolescents i adults dins del rang de talles de la UE 35 a 42."} | True | True |
| ca | 6 | {"line": 889, "question": "Cal carnet per llogar patins?", "answer": "No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Cal carnet per llogar patins?", "answer": "No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid.", "answer_raw": "No cal carnet de conduir. Els patins són una activitat no motoritzada, així que qualsevol persona els pot llogar amb un document d’identitat o passaport vàlid."} | True | True |
| ca | 7 | {"line": 893, "question": "Puc deixar les sabates o l’equipatge a la botiga?", "answer": "Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Puc deixar les sabates o l’equipatge a la botiga?", "answer": "Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer.", "answer_raw": "Sí. Disposem de servei gratuït de guarda d’equipatge per a sabates, jaquetes, bosses de mà, motxilles i maletes a la nostra botiga supervisada durant el lloguer."} | True | True |
| ca | 8 | {"line": 897, "question": "Com reservo o contacto amb vosaltres?", "answer": "Pots reservar per WhatsApp, correu electrònic o telèfon. Trobaràs totes les dades de contacte al nostre web i ens pots preguntar qualsevol dubte sobre talles o disponibilitat.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Com reservo o contacto amb vosaltres?", "answer": "Pots reservar per WhatsApp, correu electrònic o telèfon. Trobaràs totes les dades de contacte al nostre web i ens pots preguntar qualsevol dubte sobre talles o disponibilitat.", "answer_raw": "Pots reservar per WhatsApp, correu electrònic o telèfon. Trobaràs totes les dades de contacte al nostre web i ens pots preguntar qualsevol dubte sobre talles o disponibilitat."} | True | True |
| sv | 1 | {"line": 882, "question": "Behöver jag erfarenhet för att hyra rullskridskor?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Behöver jag erfarenhet för att hyra rullskridskor?", "answer": "Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar.", "answer_raw": "Nej, du behöver ingen tidigare erfarenhet. Vi har stabila rullskridskor för nybörjare och vana åkare, och vårt team hjälper dig välja rätt storlek innan du börjar."} | True | True |
| sv | 2 | {"line": 886, "question": "Ingår skyddsutrustning i hyran?", "answer": "Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Ingår skyddsutrustning i hyran?", "answer": "Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor.", "answer_raw": "Ja. Barnhjälm, handledsskydd, knäskydd och armbågsskydd ingår i varje hyra av rullskridskor."} | True | True |
| sv | 3 | {"line": 890, "question": "Var kan jag åka rullskridskor nära butiken?", "answer": "Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Var kan jag åka rullskridskor nära butiken?", "answer": "Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken.", "answer_raw": "Vår butik ligger mitt emot stranden och intill Port Olímpic. De plana kustvägarna och Parc de la Ciutadella är bra rutter för lugn rullskridskoåkning nära butiken."} | True | True |
| sv | 4 | {"line": 894, "question": "Vilka storlekar finns?", "answer": "Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Vilka storlekar finns?", "answer": "Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste.", "answer_raw": "Vi har rullskridskor i EU-storlekar 35 till 42. Du kan prova olika storlekar i butiken för att hitta den bekvämaste."} | True | True |
| sv | 5 | {"line": 898, "question": "Kan tonåringar hyra rullskridskor?", "answer": "Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Kan tonåringar hyra rullskridskor?", "answer": "Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42.", "answer_raw": "Ja. Våra rullskridskor passar äldre barn, tonåringar och vuxna inom storlekarna EU 35 till 42."} | True | True |
| sv | 6 | {"line": 902, "question": "Behöver jag körkort för att hyra rullskridskor?", "answer": "Nej. Inget körkort krävs för att hyra rullskridskor.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Behöver jag körkort för att hyra rullskridskor?", "answer": "Nej. Inget körkort krävs för att hyra rullskridskor.", "answer_raw": "Nej. Inget körkort krävs för att hyra rullskridskor."} | True | True |
| sv | 7 | {"line": 907, "question": "Kan jag lämna skor eller bagage i butiken?", "answer": "Ja. Under hyran kan du lämna skor, jackor, handväskor, ryggsäckar och resväskor gratis i vår bemannade butik.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Kan jag lämna skor eller bagage i butiken?", "answer": "Ja. Under hyran kan du lämna skor, jackor, handväskor, ryggsäckar och resväskor gratis i vår bemannade butik.", "answer_raw": "Ja. Under hyran kan du lämna skor, jackor, handväskor, ryggsäckar och resväskor gratis i vår bemannade butik."} | True | True |
| sv | 8 | {"line": 911, "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Hur bokar jag eller kontaktar er?", "answer": "Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet.", "answer_raw": "Du kan boka via WhatsApp, e-post eller telefon. Du hittar alla kontaktuppgifter på vår webbplats och kan gärna fråga om storlekar eller tillgänglighet."} | True | True |
| pl | 1 | {"line": 936, "question": "Czy potrzebuję doświadczenia, aby wynająć wrotki?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem.", "links": []} | {"path": "$.@graph[6].mainEntity[0]", "question": "Czy potrzebuję doświadczenia, aby wynająć wrotki?", "answer": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem.", "answer_raw": "Nie, wcześniejsze doświadczenie nie jest potrzebne. Oferujemy stabilne wrotki dla początkujących i pewniejszych osób, a nasz zespół pomoże dobrać właściwy rozmiar przed startem."} | True | True |
| pl | 2 | {"line": 940, "question": "Czy sprzęt ochronny jest w cenie wynajmu?", "answer": "Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek.", "links": []} | {"path": "$.@graph[6].mainEntity[1]", "question": "Czy sprzęt ochronny jest w cenie wynajmu?", "answer": "Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek.", "answer_raw": "Tak. Kask dziecięcy oraz ochraniacze na nadgarstki, kolana i łokcie są wliczone w każdy wynajem wrotek."} | True | True |
| pl | 3 | {"line": 944, "question": "Gdzie mogę jeździć na wrotkach blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się naprzeciwko plaży i obok Port Olímpic. Płaskie nadmorskie ścieżki i park Ciutadella oferują dobre trasy do spokojnej jazdy na wrotkach blisko naszej wypożyczalni.", "links": []} | {"path": "$.@graph[6].mainEntity[2]", "question": "Gdzie mogę jeździć na wrotkach blisko wypożyczalni?", "answer": "Nasza wypożyczalnia znajduje się naprzeciwko plaży i obok Port Olímpic. Płaskie nadmorskie ścieżki i park Ciutadella oferują dobre trasy do spokojnej jazdy na wrotkach blisko naszej wypożyczalni.", "answer_raw": "Nasza wypożyczalnia znajduje się naprzeciwko plaży i obok Port Olímpic. Płaskie nadmorskie ścieżki i park Ciutadella oferują dobre trasy do spokojnej jazdy na wrotkach blisko naszej wypożyczalni."} | True | True |
| pl | 4 | {"line": 948, "question": "Jakie rozmiary są dostępne?", "answer": "Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie.", "links": []} | {"path": "$.@graph[6].mainEntity[3]", "question": "Jakie rozmiary są dostępne?", "answer": "Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie.", "answer_raw": "Oferujemy wrotki w rozmiarach EU 35–42. W wypożyczalni możesz przymierzyć różne rozmiary, aby znaleźć najwygodniejsze dopasowanie."} | True | True |
| pl | 5 | {"line": 952, "question": "Czy nastolatki mogą wynająć wrotki?", "answer": "Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42.", "links": []} | {"path": "$.@graph[6].mainEntity[4]", "question": "Czy nastolatki mogą wynająć wrotki?", "answer": "Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42.", "answer_raw": "Tak. Nasze wrotki pasują starszym dzieciom, nastolatkom i dorosłym w dostępnym zakresie rozmiarów EU 35–42."} | True | True |
| pl | 6 | {"line": 956, "question": "Czy potrzebuję prawa jazdy, aby wynająć wrotki?", "answer": "Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy.", "links": []} | {"path": "$.@graph[6].mainEntity[5]", "question": "Czy potrzebuję prawa jazdy, aby wynająć wrotki?", "answer": "Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy.", "answer_raw": "Nie. Do wynajmu wrotek nie jest wymagane prawo jazdy."} | True | True |
| pl | 7 | {"line": 961, "question": "Czy mogę zostawić buty lub bagaż w wypożyczalni?", "answer": "Tak. Podczas wynajmu dostępne jest darmowe przechowanie butów, kurtek, torebek, plecaków i walizek w naszej nadzorowanej wypożyczalni.", "links": []} | {"path": "$.@graph[6].mainEntity[6]", "question": "Czy mogę zostawić buty lub bagaż w wypożyczalni?", "answer": "Tak. Podczas wynajmu dostępne jest darmowe przechowanie butów, kurtek, torebek, plecaków i walizek w naszej nadzorowanej wypożyczalni.", "answer_raw": "Tak. Podczas wynajmu dostępne jest darmowe przechowanie butów, kurtek, torebek, plecaków i walizek w naszej nadzorowanej wypożyczalni."} | True | True |
| pl | 8 | {"line": 965, "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność.", "links": []} | {"path": "$.@graph[6].mainEntity[7]", "question": "Jak mogę zarezerwować lub skontaktować się z wami?", "answer": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność.", "answer_raw": "Możesz zarezerwować przez WhatsApp, e-mail lub telefon. Wszystkie dane kontaktowe znajdziesz na naszej stronie. Możesz też zapytać o rozmiary lub dostępność."} | True | True |

## T. MATRIZ RATING/REVIEWS

Rating canónico 4.6, 226 reseñas, escala 1–5. Los testimonios individuales pueden tener 5 estrellas sin contradecir la media. Se verifica presencia y correspondencia; autenticidad externa no verificada.

| Idioma | Comparación completa |
| --- | --- |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Great place to rent skates in Barcelona. We rented both inline skates (rollerblades) and classic 4-wheel roller skates. Everything was in good condition, the staff was helpful and the location near the beach is perfect for skating. Highly recommended if you're looking for inline skate or roller skate rental in Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-08-10"}, "line": 886, "visible_card": {"line": 886, "text": "★★★★★ “Great place to rent skates in Barcelona. We rented both inline skates (rollerblades) and classic 4-wheel roller skates. Everything was in good condition, the staff was helpful and the location near the beach is perfect for skating. Highly recommended if you're looking for inline skate or roller skate rental in Barcelona.” Pierre L Google review · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Alquilamos patines en línea en Barcelona en nuestras vacaciones,, tambien tienen patines de 4 ruedas, esta situada en la Vila Olimpica, al lado del paseo maritimo ycerca de la Barceloneta. Buen precio y una atenci¡on genial, lo recomiendo .100x100\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 989, "visible_card": {"line": 989, "text": "★★★★★ “Alquilamos patines en línea en Barcelona en nuestras vacaciones,, tambien tienen patines de 4 ruedas, esta situada en la Vila Olimpica, al lado del paseo maritimo ycerca de la Barceloneta. Buen precio y una atenci¡on genial, lo recomiendo .100x100” Sonia · Reseña de Google · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Nous avons loué des rollers en ligne à Barcelone pendant nos vacances. Ils ont aussi des patins à quatre roues. La boutique se trouve à la Vila Olímpica, à côté de la promenade maritime et près de la Barceloneta. Bon prix et excellent accueil, je recommande à 100 %.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 921, "visible_card": {"line": 921, "text": "★★★★★ “Nous avons loué des rollers en ligne à Barcelone pendant nos vacances. Ils ont aussi des patins à quatre roues. La boutique se trouve à la Vila Olímpica, à côté de la promenade maritime et près de la Barceloneta. Bon prix et excellent accueil, je recommande à 100 %.” Sonia · Avis Google · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Abbiamo noleggiato pattini in linea a Barcellona durante le nostre vacanze. Hanno anche pattini a quattro ruote. Il negozio si trova nella Vila Olímpica, accanto al lungomare e vicino alla Barceloneta. Buon prezzo e ottimo servizio, lo consiglio al 100%.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 926, "visible_card": {"line": 926, "text": "★★★★★ “Abbiamo noleggiato pattini in linea a Barcellona durante le nostre vacanze. Hanno anche pattini a quattro ruote. Il negozio si trova nella Vila Olímpica, accanto al lungomare e vicino alla Barceloneta. Buon prezzo e ottimo servizio, lo consiglio al 100%.” Sonia · Recensione Google · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Ein toller Ort, um in Barcelona Skates zu mieten. Wir haben sowohl Inlineskates (Rollerblades) als auch klassische Rollschuhe mit vier Rollen gemietet. Alles war in gutem Zustand, das Personal war hilfsbereit und die Lage nahe dem Strand ist perfekt zum Skaten. Sehr empfehlenswert, wenn man in Barcelona Inlineskates oder Rollschuhe mieten möchte.“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 827, "visible_card": {"line": 827, "text": "★★★★★ „Ein toller Ort, um in Barcelona Skates zu mieten. Wir haben sowohl Inlineskates (Rollerblades) als auch klassische Rollschuhe mit vier Rollen gemietet. Alles war in gutem Zustand, das Personal war hilfsbereit und die Lage nahe dem Strand ist perfekt zum Skaten. Sehr empfehlenswert, wenn man in Barcelona Inlineskates oder Rollschuhe mieten möchte.“ Pierre L Google-Bewertung · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Een geweldige plek om skates te huren in Barcelona. We huurden zowel inline skates (rollerblades) als klassieke rolschaatsen met vier wielen. Alles was in goede staat, het personeel was behulpzaam en de locatie vlak bij het strand is perfect om te skaten. Een echte aanrader als je inline skates of rolschaatsen wilt huren in Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 836, "visible_card": {"line": 836, "text": "★★★★★ “Een geweldige plek om skates te huren in Barcelona. We huurden zowel inline skates (rollerblades) als klassieke rolschaatsen met vier wielen. Alles was in goede staat, het personeel was behulpzaam en de locatie vlak bij het strand is perfect om te skaten. Een echte aanrader als je inline skates of rolschaatsen wilt huren in Barcelona.” Pierre L Google-review · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Um ótimo sítio para alugar patins em Barcelona. Alugámos tanto patins em linha (rollerblades) como patins clássicos de quatro rodas. Tudo estava em boas condições, o pessoal foi prestável e a localização perto da praia é perfeita para patinar. Muito recomendável se procura alugar patins em linha ou patins clássicos em Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 841, "visible_card": {"line": 841, "text": "★★★★★ “Um ótimo sítio para alugar patins em Barcelona. Alugámos tanto patins em linha (rollerblades) como patins clássicos de quatro rodas. Tudo estava em boas condições, o pessoal foi prestável e a localização perto da praia é perfeita para patinar. Muito recomendável se procura alugar patins em linha ou patins clássicos em Barcelona.” Pierre L Avaliação Google · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Un lloc fantàstic per llogar patins a Barcelona. Vam llogar tant patins en línia com patins clàssics de quatre rodes. Tot estava en bon estat, el personal va ser servicial i la ubicació prop de la platja és perfecta per patinar. Molt recomanable si busques lloguer de patins en línia o patins clàssics a Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 825, "visible_card": {"line": 825, "text": "★★★★★ “Un lloc fantàstic per llogar patins a Barcelona. Vam llogar tant patins en línia com patins clàssics de quatre rodes. Tot estava en bon estat, el personal va ser servicial i la ubicació prop de la platja és perfecta per patinar. Molt recomanable si busques lloguer de patins en línia o patins clàssics a Barcelona.” Pierre L Ressenya de Google · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Ett fantastiskt ställe att hyra rullskridskor i Barcelona. Vi hyrde både inlines och klassiska fyrhjuliga rullskridskor. Allt var i gott skick, personalen var hjälpsam och läget nära stranden är perfekt för att åka. Rekommenderas varmt om du söker uthyrning av inlines eller rullskridskor i Barcelona.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 838, "visible_card": {"line": 838, "text": "★★★★★ “Ett fantastiskt ställe att hyra rullskridskor i Barcelona. Vi hyrde både inlines och klassiska fyrhjuliga rullskridskor. Allt var i gott skick, personalen var hjälpsam och läget nära stranden är perfekt för att åka. Rekommenderas varmt om du söker uthyrning av inlines eller rullskridskor i Barcelona.” Pierre L Google-recension · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/quads/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Pierre L"}, "datePublished": "2026-08-10", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Świetne miejsce na wynajem rolek w Barcelonie. Wynajęliśmy zarówno rolki, jak i klasyczne wrotki na czterech kółkach. Wszystko było w dobrym stanie, personel był pomocny, a lokalizacja blisko plaży jest idealna do jazdy. Gorąco polecam, jeśli szukasz wynajmu rolek lub wrotek w Barcelonie.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 892, "visible_card": {"line": 892, "text": "★★★★★ “Świetne miejsce na wynajem rolek w Barcelonie. Wynajęliśmy zarówno rolki, jak i klasyczne wrotki na czterech kółkach. Wszystko było w dobrym stanie, personel był pomocny, a lokalizacja blisko plaży jest idealna do jazdy. Gorąco polecam, jeśli szukasz wynajmu rolek lub wrotek w Barcelonie.” Pierre L Opinia Google · 2026-08-10", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |

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
| en | [{"line": 665, "id": null, "links": [{"line": 666, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 666, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 666, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 666, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 666, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 666, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 666, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 666, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 666, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 666, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 684, "id": null, "links": [{"line": 685, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 685, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 685, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 685, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 685, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 685, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 685, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 685, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 685, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 685, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 713, "attribute": "aria-labelledby", "ref": "quads-business-facts-title", "exists": true}, {"line": 879, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 930, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 972, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 660, "text": "Language", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 680, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 687, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Toggle menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 938, "text": "Do I need experience to rent roller skates?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 942, "text": "Is protective gear included with the rental?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 946, "text": "Where can I roller skate near the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 950, "text": "What sizes are available?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 954, "text": "Can teenagers rent roller skates?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 958, "text": "Do I need a licence to rent roller skates?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 962, "text": "Can I store my shoes or luggage at the shop?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 966, "text": "How do I book or contact you?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| es | [{"line": 659, "id": null, "links": [{"line": 660, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 660, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 660, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 660, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 660, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 660, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 660, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 660, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 660, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 660, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 678, "id": null, "links": [{"line": 679, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 679, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 679, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 679, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 679, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 679, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 679, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 679, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 679, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 679, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 707, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-es", "exists": true}, {"line": 903, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 945, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 654, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 674, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 681, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir o cerrar menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 911, "text": "¿Necesito experiencia para alquilar patines?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 915, "text": "¿Está incluido el equipo de protección?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 919, "text": "¿Dónde puedo patinar cerca de la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 923, "text": "¿Qué tallas hay disponibles?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 927, "text": "¿Pueden alquilar patines los adolescentes?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 931, "text": "¿Necesito carnet para alquilar patines?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 935, "text": "¿Puedo dejar mis zapatos o maletas en la tienda?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 939, "text": "¿Cómo reservo o contacto con vosotros?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| fr | [{"line": 592, "id": null, "links": [{"line": 593, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 593, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 593, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 593, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 593, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 593, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 593, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 593, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 593, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 593, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 611, "id": null, "links": [{"line": 612, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 612, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 612, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 612, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 612, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 612, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 612, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 612, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 612, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 612, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 639, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-fr", "exists": true}, {"line": 835, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 877, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 587, "text": "Langue", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 607, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 614, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Ouvrir ou fermer le menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 843, "text": "Faut-il de l’expérience pour louer des patins à roulettes ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 847, "text": "Les protections sont-elles incluses dans la location ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 851, "text": "Où puis-je patiner près de la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 855, "text": "Quelles pointures sont disponibles ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 859, "text": "Les adolescents peuvent-ils louer des patins ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 863, "text": "Faut-il un permis pour louer des patins ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 867, "text": "Puis-je laisser mes chaussures ou mes bagages à la boutique ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 871, "text": "Comment réserver ou vous contacter ?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| it | [{"line": 594, "id": null, "links": [{"line": 595, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 595, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 595, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 595, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 595, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 595, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 595, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 595, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 595, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 595, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 613, "id": null, "links": [{"line": 614, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 614, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 614, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 614, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 614, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 614, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 614, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 614, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 614, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 614, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 644, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-it", "exists": true}, {"line": 840, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 882, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 589, "text": "Lingua", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 609, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 616, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Apri o chiudi il menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 848, "text": "Serve esperienza per noleggiare pattini a rotelle?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 852, "text": "Le protezioni sono incluse nel noleggio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 856, "text": "Dove posso pattinare vicino al negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 860, "text": "Quali taglie sono disponibili?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 864, "text": "Gli adolescenti possono noleggiare pattini?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 868, "text": "Serve una patente per noleggiare pattini?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 872, "text": "Posso lasciare scarpe o bagagli in negozio?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 876, "text": "Come posso prenotare o contattarvi?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| de | [{"line": 599, "id": null, "links": [{"line": 600, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 600, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 600, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 600, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 600, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 600, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 600, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 600, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 600, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 600, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 618, "id": null, "links": [{"line": 619, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 619, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 619, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 619, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 619, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 619, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 619, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 619, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 619, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 619, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 646, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-de", "exists": true}, {"line": 820, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 864, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 923, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 594, "text": "Sprache", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 614, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 621, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menü öffnen", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 873, "text": "Brauche ich Erfahrung, um Rollschuhe zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 879, "text": "Ist Schutzausrüstung in der Miete enthalten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 885, "text": "Wo kann ich in der Nähe des Geschäfts Rollschuh fahren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 891, "text": "Welche Größen sind verfügbar?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 897, "text": "Können Jugendliche Rollschuhe mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 903, "text": "Brauche ich einen Führerschein, um Rollschuhe zu mieten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 910, "text": "Kann ich meine Schuhe oder mein Gepäck im Geschäft lassen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 916, "text": "Wie kann ich buchen oder Kontakt aufnehmen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| nl | [{"line": 608, "id": null, "links": [{"line": 609, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 609, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 609, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 609, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 609, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 609, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 609, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 609, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 609, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 609, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 627, "id": null, "links": [{"line": 628, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 628, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 628, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 628, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 628, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 628, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 628, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 628, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 628, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 628, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 655, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-nl", "exists": true}, {"line": 829, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 873, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 932, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 603, "text": "Taal", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 623, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 630, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menu openen of sluiten", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 882, "text": "Heb ik ervaring nodig om rolschaatsen te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 888, "text": "Is bescherming inbegrepen bij de huur?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 894, "text": "Waar kan ik rolschaatsen in de buurt van de winkel?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 900, "text": "Welke maten zijn beschikbaar?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 906, "text": "Kunnen tieners rolschaatsen huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 912, "text": "Heb ik een rijbewijs nodig om rolschaatsen te huren?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 919, "text": "Kan ik mijn schoenen of bagage in de winkel achterlaten?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 925, "text": "Hoe kan ik boeken of contact opnemen?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pt | [{"line": 611, "id": null, "links": [{"line": 612, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 612, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 612, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 612, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 612, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 612, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 612, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 612, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 612, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 612, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 630, "id": null, "links": [{"line": 631, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 631, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 631, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 631, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 631, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 631, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 631, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 631, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 631, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 631, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 661, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-pt", "exists": true}, {"line": 834, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 878, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 920, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 606, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 626, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 633, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir ou fechar menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 886, "text": "Preciso de experiência para alugar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 890, "text": "O equipamento de proteção está incluído?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 894, "text": "Onde posso patinar perto da loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 898, "text": "Que tamanhos estão disponíveis?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 902, "text": "Adolescentes podem alugar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 906, "text": "Preciso de carta para alugar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 910, "text": "Posso deixar os sapatos ou a bagagem na loja?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 914, "text": "Como posso reservar ou contactar-vos?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| ca | [{"line": 594, "id": null, "links": [{"line": 595, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 595, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 595, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 595, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 595, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 595, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 595, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 595, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 595, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 595, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 613, "id": null, "links": [{"line": 614, "text": "en English", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 614, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 614, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 614, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 614, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 614, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 614, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 614, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 614, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 614, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 644, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-cat", "exists": true}, {"line": 818, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 862, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 904, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 589, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 609, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 616, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Obrir o tancar el menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 870, "text": "Cal experiència per llogar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 874, "text": "L’equip de protecció està inclòs?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 878, "text": "On puc patinar a prop de la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 882, "text": "Quines talles hi ha disponibles?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 886, "text": "Els adolescents poden llogar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 890, "text": "Cal carnet per llogar patins?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 894, "text": "Puc deixar les sabates o l’equipatge a la botiga?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 898, "text": "Com reservo o contacto amb vosaltres?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| sv | [{"line": 609, "id": null, "links": [{"line": 610, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 610, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 610, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 610, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 610, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 610, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 610, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 610, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 610, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 610, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 628, "id": null, "links": [{"line": 629, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 629, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 629, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 629, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 629, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 629, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 629, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 629, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 629, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 629, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 657, "attribute": "aria-labelledby", "ref": "quads-business-facts-title-sv", "exists": true}, {"line": 831, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 875, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 918, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 604, "text": "Språk", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 624, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 631, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Öppna eller stäng menyn", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 883, "text": "Behöver jag erfarenhet för att hyra rullskridskor?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 887, "text": "Ingår skyddsutrustning i hyran?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 891, "text": "Var kan jag åka rullskridskor nära butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 895, "text": "Vilka storlekar finns?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 899, "text": "Kan tonåringar hyra rullskridskor?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 903, "text": "Behöver jag körkort för att hyra rullskridskor?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 908, "text": "Kan jag lämna skor eller bagage i butiken?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 912, "text": "Hur bokar jag eller kontaktar er?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |
| pl | [{"line": 665, "id": null, "links": [{"line": 666, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 666, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 666, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 666, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 666, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 666, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 666, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 666, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 666, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 666, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}, {"line": 684, "id": null, "links": [{"line": 685, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/quads/", "role": "menuitem"}}, {"line": 685, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/quads/", "role": "menuitem"}}, {"line": 685, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/quads/", "role": "menuitem"}}, {"line": 685, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/quads/", "role": "menuitem"}}, {"line": 685, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/quads/", "role": "menuitem"}}, {"line": 685, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/quads/", "role": "menuitem"}}, {"line": 685, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/quads/", "role": "menuitem"}}, {"line": 685, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/quads/", "role": "menuitem"}}, {"line": 685, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/quads/", "role": "menuitem"}}, {"line": 685, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/quads/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/quads/", "role": "menuitem"}}], "selected": []}] | [{"line": 713, "attribute": "aria-labelledby", "ref": "quads-business-facts-title", "exists": true}, {"line": 885, "attribute": "aria-labelledby", "ref": "reviews-title", "exists": true}, {"line": 929, "attribute": "aria-labelledby", "ref": "faq-title", "exists": true}, {"line": 972, "attribute": "aria-labelledby", "ref": "more-rsb-title", "exists": true}] | [{"tag": "button", "line": 660, "text": "Język", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 680, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 687, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Przełącz menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "button", "line": 937, "text": "Czy potrzebuję doświadczenia, aby wynająć wrotki?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 941, "text": "Czy sprzęt ochronny jest w cenie wynajmu?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 945, "text": "Gdzie mogę jeździć na wrotkach blisko wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 949, "text": "Jakie rozmiary są dostępne?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 953, "text": "Czy nastolatki mogą wynająć wrotki?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 957, "text": "Czy potrzebuję prawa jazdy, aby wynająć wrotki?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 962, "text": "Czy mogę zostawić buty lub bagaż w wypożyczalni?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 966, "text": "Jak mogę zarezerwować lub skontaktować się z wami?", "attrs": {"aria-expanded": "false", "class": "faq-q", "type": "button"}, "parent_interactive": []}] |

Los 12.046 enlaces internos de los 200 HTML apuntan al corpus incluido y todas las anclas locales se resuelven. No se han solicitado respuestas HTTP. La marca estática de idioma activo es una mejora.

## W. MATRIZ GLOBAL POR IDIOMA

| Idioma | Primera pasada | Segunda pasada independiente | Comprobaciones de página |
| --- | --- | --- | --- |
| en | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/quads/", "expected_page": "https://rentalscooterbarcelona.com/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "en", "expected": "en", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/quads/", "pass": true}] |
| es | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/es/quads/", "expected_page": "https://rentalscooterbarcelona.com/es/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "es", "expected": "es", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/quads/", "pass": true}] |
| fr | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/fr/quads/", "expected_page": "https://rentalscooterbarcelona.com/fr/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "fr", "expected": "fr", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/quads/", "pass": true}] |
| it | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/it/quads/", "expected_page": "https://rentalscooterbarcelona.com/it/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "it", "expected": "it", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/quads/", "pass": true}] |
| de | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/de/quads/", "expected_page": "https://rentalscooterbarcelona.com/de/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "de", "expected": "de", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/quads/", "pass": true}] |
| nl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/nl/quads/", "expected_page": "https://rentalscooterbarcelona.com/nl/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "nl", "expected": "nl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/quads/", "pass": true}] |
| pt | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pt/quads/", "expected_page": "https://rentalscooterbarcelona.com/pt/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pt-PT", "expected": "pt-PT", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/quads/", "pass": true}] |
| ca | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/cat/quads/", "expected_page": "https://rentalscooterbarcelona.com/cat/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "ca", "expected": "ca", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/quads/", "pass": true}] |
| sv | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/sv/quads/", "expected_page": "https://rentalscooterbarcelona.com/sv/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "sv", "expected": "sv", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/quads/", "pass": true}] |
| pl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": false, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pl/quads/", "expected_page": "https://rentalscooterbarcelona.com/pl/quads/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pl", "expected": "pl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/quads/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/quads/", "pass": true}] |

## LISTA FINAL DE CAMBIOS PROPUESTOS

| Punto | Idioma | Prioridad | Elemento | Propuesta |
| --- | --- | --- | --- | --- |
| U03 | ca | 2 | https://rentalscooterbarcelona.com/cat/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | de | 2 | https://rentalscooterbarcelona.com/de/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | en | 2 | https://rentalscooterbarcelona.com/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | es | 2 | https://rentalscooterbarcelona.com/es/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | fr | 2 | https://rentalscooterbarcelona.com/fr/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | it | 2 | https://rentalscooterbarcelona.com/it/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | nl | 2 | https://rentalscooterbarcelona.com/nl/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pl | 2 | https://rentalscooterbarcelona.com/pl/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | pt | 2 | https://rentalscooterbarcelona.com/pt/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U03 | sv | 2 | https://rentalscooterbarcelona.com/sv/quads/#webpage.dateModified | Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente. |
| U05 | de | 3 | Párrafo de enlace a la guía | Kinderhelm, Handgelenkschoner, Knieschoner und Ellbogenschoner sind bei jeder Rollschuhmiete inklusive. Die Größen reichen von EU 35 bis 42, und unser lokales Team gibt grundlegende Hinweise sowie Routentipps. Für lokale Routenideen und praktische Tipps kannst du unseren &lt;a href="https://rentalscooterbarcelona.com/de/blog/roller-skates/"&gt;Guide zum Rollschuhe mieten in Barcelona&lt;/a&gt; lesen.&lt;/p&gt; |

## CONTROL FINAL

Integridad SHA-256 comprobada contra cada entrada ZIP. Las evidencias contienen valores y líneas por archivo. No se han modificado HTML ni aplicado correcciones. Imágenes y tamaños quedan pendientes; no se ha certificado renderizado, entrega de formularios, indexación ni disponibilidad remota.
