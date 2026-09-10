# Auditoría HTML — 09_LOCATION_CONTACT

2026-09-09. Diez idiomas. Fuente: ZIP adjunto y CANONICAL.md. HTML original sin modificar.

## A. INVENTARIO DE ARCHIVOS

| Idioma | Archivo original | Bytes | Líneas | SHA-256 |
| --- | --- | --- | --- | --- |
| en | LOCATION_CONTACT-main/09_LOCATION_CONTACT/location-contact/index.html | 67639 | 998 | ee5633cb2b2df9a903d854784168e30eb0f2e90409551dbac5a8ed6232c97617 |
| es | LOCATION_CONTACT-main/09_LOCATION_CONTACT/es/location-contact/index.html | 66091 | 996 | 0c8c217885c7efc1f06f7efb545e25ca26bf3079b203b084e460b04f00260ef5 |
| fr | LOCATION_CONTACT-main/09_LOCATION_CONTACT/fr/location-contact/index.html | 65317 | 938 | 6332bdd3ff0d69dbc5b7dd62dc3a645ae382f92f4ec760d405bcc39c90bf1dd8 |
| it | LOCATION_CONTACT-main/09_LOCATION_CONTACT/it/location-contact/index.html | 64984 | 949 | e6027a1e84461c33a99d4fd51acc4c0b8139986cb131d114ca3935487ec07e3a |
| de | LOCATION_CONTACT-main/09_LOCATION_CONTACT/de/location-contact/index.html | 65386 | 956 | da6e7f7c863006a0f21f3ac15850d4cf0a084667cd8f4c9892a6586b341fe648 |
| nl | LOCATION_CONTACT-main/09_LOCATION_CONTACT/nl/location-contact/index.html | 64853 | 969 | f1a05ad8c3d87950190f74442087204f7ab4b3a7f99663ca48913d0a4df117be |
| pt | LOCATION_CONTACT-main/09_LOCATION_CONTACT/pt/location-contact/index.html | 65776 | 979 | a01692e260e92c82950fd10089e64ddb0a1ddf6c8e07a226f80b82f83fc1fbc6 |
| ca | LOCATION_CONTACT-main/09_LOCATION_CONTACT/cat/location-contact/index.html | 65262 | 959 | 65a836f6bf2ea30d93fdf5f0e651680c2f0832953f5cf70f92befafcafbcb754 |
| sv | LOCATION_CONTACT-main/09_LOCATION_CONTACT/sv/location-contact/index.html | 65307 | 969 | 6708ca15d2271477946721c107ddb1195c8fc7c449c2cf36df81cf2b4046a1ab |
| pl | LOCATION_CONTACT-main/09_LOCATION_CONTACT/pl/location-contact/index.html | 67035 | 1009 | 2c3fcd69427b60328f33c430f0db693a34f1f01cee17a93ba4ca1da2e88932b1 |

## B. MÉTODOS REALMENTE EJECUTADOS

Lectura completa de 10 fuentes, tokenización HTML, parser lxml, análisis de todos los JSON-LD, extracción del head, entidades, precios, FAQ, reseñas, políticas y enlaces. Segunda pasada independiente directamente sobre los ZIP originales: 23 controles por HTML. Comprobación de sintaxis del JavaScript inline, sin ejecutarlo. Cruce de tarifas con PRICES y de enlaces con los 200 HTML. Inspección de párrafos de guía DE/NL. Sin acceso al sitio publicado, validación externa de normativa o ejecución de recursos remotos.

## C. RESULTADO GLOBAL

| Idioma | Errores confirmados | Segunda pasada: controles superados |
| --- | --- | --- |
| en | Ninguno demostrado | 23/23 |
| es | Ninguno demostrado | 23/23 |
| fr | Ninguno demostrado | 23/23 |
| it | Ninguno demostrado | 23/23 |
| de | Ninguno demostrado | 23/23 |
| nl | Ninguno demostrado | 23/23 |
| pt | Ninguno demostrado | 23/23 |
| ca | Ninguno demostrado | 23/23 |
| sv | Ninguno demostrado | 23/23 |
| pl | Ninguno demostrado | 23/23 |

## D. ERRORES CRÍTICOS

Ninguno demostrado en el alcance estático.

## E. ERRORES ALTOS

Ninguno demostrado en el alcance estático.

## F. ERRORES MEDIOS

Ninguno demostrado.

## G. ERRORES BAJOS

Ninguno demostrado.

## H. INCOHERENCIAS QUE REQUIEREN FUENTE CANÓNICA

No aparece conflicto de fecha de modificación en esta página.

Los datos de identidad, dirección, horario, mapas y equipamiento ya están definidos: no requieren nueva confirmación. Las tarifas y tallas documentadas no equivalen a una certificación externa de vigencia.

## I. MEJORAS RECOMENDADAS

# Mejoras opcionales — 09_LOCATION_CONTACT

Explicitar el idioma activo con aria-current en los selectores estáticos. Es una mejora de orientación; los enlaces ya apuntan al idioma correcto.

Probar posteriormente el formulario en navegador y móvil, incluyendo WhatsApp instalado/no instalado y bloqueo de ventanas. El script valida campos, construye una URL wa.me y contiene un fallback; la entrega real no se ha probado. Valorar explicar junto al botón que el envío final se completa en WhatsApp.

Revisión visual, imágenes, recortes, resolución y tamaños: aplazada expresamente.

## J. OPCIONALES

Unificar plantillas de datos para evitar divergencias futuras entre idiomas y bloques JSON-LD. No fusionar IDs distintos de servicios ni localizar las entidades globales.

## K. MATRIZ COMPLETA DEL HEAD

### en

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>RSB Rental Scooter Barcelona Location in Vila Olímpica</title>
<meta content="Find RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach. Address, WhatsApp, opening hours, map and directions." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="RSB Rental Scooter Barcelona Location in Vila Olímpica" property="og:title"/>
<meta content="Find RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach. Address, WhatsApp, opening hours, map and directions." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="RSB Rental Scooter Barcelona shop in Vila Olímpica del Poblenou near Port Olímpic and Barceloneta Beach" property="og:image:alt"/>
<meta content="en_GB" property="og:locale"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="RSB Rental Scooter Barcelona Location in Vila Olímpica" name="twitter:title"/>
<meta content="Find RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach. Address, WhatsApp, opening hours, map and directions." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="RSB Rental Scooter Barcelona shop in Vila Olímpica del Poblenou near Port Olímpic and Barceloneta Beach" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Rental" name="apple-mobile-web-app-title"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/location-contact/",
      "name": "RSB Rental Scooter Barcelona Location in Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Find RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach. Address, WhatsApp, opening hours, map and directions.",
      "inLanguage": "en",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/location-contact/#faq"
        }
      ],
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
      "@id": "https://rentalscooterbarcelona.com/location-contact/#breadcrumb",
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
          "name": "Location & Contact",
          "item": "https://rentalscooterbarcelona.com/location-contact/"
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Where is RSB Rental Scooter Barcelona located?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona is at Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach."
          }
        },
        {
          "@type": "Question",
          "name": "How can I contact RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page."
          }
        },
        {
          "@type": "Question",
          "name": "What are the opening hours?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Open every day: 10:30–13:30 and 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Is the shop near the beach?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. The shop is in Vila Olímpica, a short walk from Port Olímpic and Barceloneta Beach."
          }
        }
      ],
      "inLanguage": "en"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Yassine Souri"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Best Rollers 🛼 rental spot , You can go alongside Barceloneta. Amazing time and experience. The owner is also a wonderful guy. I recommend a lot\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2026-07-30"
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "James Liddell"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Really helpfull women. Cheap price and great location\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2019-02-15"
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Crystal S"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"What a friendly and patient one person operated business. Several people were approached for rental and I was the only non-Spanish and non-Catalan speaking person. We were not in a hurry, so I motioned to take others. But no, he was patient, explained how to operate equipment and walked us to an area to try it out before we went off on our own. I thought the price was reasonable too. Would definitely visit again and suggest that others visit. Oh the only thing it did not come with a lock, which was fine for us. But no way I would leave unattended on beach.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      },
      "datePublished": "2019-09-28"
    }
  ]
}
</script>

```

### es

```html

<meta charset="utf-8"/>
    <link rel="manifest" href="/site.webmanifest"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Ubicación y contacto | RSB Rental Scooter Barcelona</title>
<meta name="description" content="Ubicación y contacto de RSB Rental Scooter Barcelona en la Vila Olímpica, cerca de Port Olímpic y Barceloneta. Dirección, WhatsApp, horarios y mapa.">
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/es/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta property="og:title" content="Ubicación y contacto | RSB Rental Scooter Barcelona">
<meta property="og:description" content="Ubicación y contacto de RSB Rental Scooter Barcelona en la Vila Olímpica, cerca de Port Olímpic y Barceloneta. Dirección, WhatsApp, horarios y mapa.">
<meta content="https://rentalscooterbarcelona.com/es/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Tienda de RSB Rental Scooter Barcelona en Vila Olímpica del Poblenou cerca del Port Olímpic y la Barceloneta" property="og:image:alt"/>
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
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta name="twitter:title" content="Ubicación y contacto | RSB Rental Scooter Barcelona">
<meta name="twitter:description" content="Ubicación y contacto de RSB Rental Scooter Barcelona en la Vila Olímpica, cerca de Port Olímpic y Barceloneta. Dirección, WhatsApp, horarios y mapa.">
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Tienda de RSB Rental Scooter Barcelona en Vila Olímpica del Poblenou cerca del Port Olímpic y la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de la Barceloneta y el Port Olímpic.",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/es/location-contact/",
      "name": "Ubicación y contacto | RSB Rental Scooter Barcelona",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Ubicación y contacto de RSB Rental Scooter Barcelona en la Vila Olímpica, cerca de Port Olímpic y Barceloneta. Dirección, WhatsApp, horarios y mapa.",
      "inLanguage": "es",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/es/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/location-contact/#faq"
        }
      ],
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      },
      "potentialAction": {
        "@type": "CommunicateAction",
        "name": "Reserva por WhatsApp",
        "target": "https://wa.me/34640559468"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#breadcrumb",
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
          "name": "Ubicación y contacto",
          "item": "https://rentalscooterbarcelona.com/es/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de la Barceloneta y el Port Olímpic.",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Dónde está RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona está en Carrer de Salvador Espriu, 63, 08005 Barcelona, en Vila Olímpica del Poblenou, cerca del Port Olímpic y la Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cómo puedo contactar con RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puedes llamar o enviar WhatsApp al +34 640 559 468, escribir a info@rentalscooterbarcelona.com o usar el formulario de esta página."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cuál es el horario?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Abierto todos los días: 10:30–13:30 y 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "¿La tienda está cerca de la playa?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. La tienda está en Vila Olímpica, frente a la playa y junto a Port Olímpic."
          }
        }
      ],
      "inLanguage": "es"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Marc Bonet Fernández"
      },
      "datePublished": "2025-07-01",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Pequeña sorpresa junto a la playa de Barcelona. Mi experiencia fué genial. Precios razonables y a un tiro de piedra del paseo marítimo. Lo mejor de todo, la atención de la propietaria.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Rita Conti"
      },
      "datePublished": "2022-08-30",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Experiencia increíble, buena ubicación y personal súper amable. 100% recomendable. Mil gracias Natalia por tu disponibilidad, tu ayuda y tus consejos!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Armando Vidales"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Lo recomiendo ampliamente! Muy buena experiencia, muy amables y muy buen coste. La ubicación ideal.\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Adresse de RSB Rental Scooter Barcelona à Vila Olímpica</title>
<meta content="Trouvez RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta. Adresse, WhatsApp, horaires, plan et itinéraire." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/fr/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Adresse de RSB Rental Scooter Barcelona à Vila Olímpica" property="og:title"/>
<meta content="Trouvez RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta. Adresse, WhatsApp, horaires, plan et itinéraire." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/fr/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Boutique RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou près du Port Olímpic et de la Barceloneta" property="og:image:alt"/>
<meta content="fr_FR" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Adresse de RSB Rental Scooter Barcelona à Vila Olímpica" name="twitter:title"/>
<meta content="Trouvez RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta. Adresse, WhatsApp, horaires, plan et itinéraire." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Boutique RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou près du Port Olímpic et de la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant la location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de la Barceloneta et du Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/fr/location-contact/",
      "name": "Adresse de RSB Rental Scooter Barcelona à Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Trouvez RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta. Adresse, WhatsApp, horaires, plan et itinéraire.",
      "inLanguage": "fr",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#faq"
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#breadcrumb",
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
          "name": "Adresse et contact",
          "item": "https://rentalscooterbarcelona.com/fr/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant la location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de la Barceloneta et du Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Où se trouve RSB Rental Scooter Barcelona ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona se trouve au Carrer de Salvador Espriu, 63, 08005 Barcelone, à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Comment contacter RSB Rental Scooter Barcelona ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page."
          }
        },
        {
          "@type": "Question",
          "name": "Quels sont les horaires ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ouvert tous les jours : 10:30–13:30 et 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "La boutique est-elle près de la plage ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. La boutique se trouve à Vila Olímpica, face à la plage et à côté du Port Olímpic."
          }
        }
      ],
      "inLanguage": "fr"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Marc Bonet Fernández"
      },
      "datePublished": "2025-07-01",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Une petite surprise près de la plage de Barcelone. Mon expérience a été géniale. Des prix raisonnables et à deux pas de la promenade maritime. Le meilleur de tout, l’accueil de la propriétaire.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Rita Conti"
      },
      "datePublished": "2022-08-30",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Expérience incroyable, bon emplacement et personnel très aimable. Recommandé à 100 %. Mille mercis à Natalia pour ta disponibilité, ton aide et tes conseils !\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Armando Vidales"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Je le recommande vivement ! Très bonne expérience, personnel très aimable et très bon prix. L’emplacement est idéal.\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Dove si trova RSB Rental Scooter Barcelona a Vila Olímpica</title>
<meta content="Trova RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta. Indirizzo, WhatsApp, orari, mappa e indicazioni." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/it/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Dove si trova RSB Rental Scooter Barcelona a Vila Olímpica" property="og:title"/>
<meta content="Trova RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta. Indirizzo, WhatsApp, orari, mappa e indicazioni." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/it/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Negozio RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou vicino al Port Olímpic e alla Barceloneta" property="og:image:alt"/>
<meta content="it_IT" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Dove si trova RSB Rental Scooter Barcelona a Vila Olímpica" name="twitter:title"/>
<meta content="Trova RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta. Indirizzo, WhatsApp, orari, mappa e indicazioni." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Negozio RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou vicino al Port Olímpic e alla Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino alla Barceloneta e al Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/it/location-contact/",
      "name": "Dove si trova RSB Rental Scooter Barcelona a Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Trova RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta. Indirizzo, WhatsApp, orari, mappa e indicazioni.",
      "inLanguage": "it",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/it/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/location-contact/#faq"
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#breadcrumb",
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
          "name": "Dove siamo e contatti",
          "item": "https://rentalscooterbarcelona.com/it/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino alla Barceloneta e al Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Dove si trova RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona si trova in Carrer de Salvador Espriu, 63, 08005 Barcellona, a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Come posso contattare RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina."
          }
        },
        {
          "@type": "Question",
          "name": "Quali sono gli orari?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Il negozio è vicino alla spiaggia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sì. Il negozio è a Vila Olímpica, di fronte alla spiaggia e accanto al Port Olímpic."
          }
        }
      ],
      "inLanguage": "it"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Marc Bonet Fernández"
      },
      "datePublished": "2025-07-01",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Una piccola sorpresa vicino alla spiaggia di Barcellona. La mia esperienza è stata fantastica. Prezzi ragionevoli e a due passi dal lungomare. La cosa migliore è stata l’attenzione della proprietaria.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Rita Conti"
      },
      "datePublished": "2022-08-30",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Esperienza incredibile, buona posizione e personale super gentile. Consigliato al 100%. Grazie mille Natalia per la tua disponibilità, il tuo aiuto e i tuoi consigli!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Armando Vidales"
      },
      "datePublished": "2021-04-12",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Lo consiglio vivamente! Ottima esperienza, persone molto gentili e ottimo prezzo. La posizione è ideale.\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Standort von RSB Rental Scooter Barcelona in Vila Olímpica</title>
<meta content="Finde RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta. Adresse, WhatsApp, Öffnungszeiten, Karte und Anfahrt." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/de/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/><meta content="de_DE" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Standort von RSB Rental Scooter Barcelona in Vila Olímpica" property="og:title"/>
<meta content="Finde RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta. Adresse, WhatsApp, Öffnungszeiten, Karte und Anfahrt." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/de/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Geschäft von RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou nahe Port Olímpic und Barceloneta" property="og:image:alt"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Standort von RSB Rental Scooter Barcelona in Vila Olímpica" name="twitter:title"/>
<meta content="Finde RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta. Adresse, WhatsApp, Öffnungszeiten, Karte und Anfahrt." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Geschäft von RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou nahe Port Olímpic und Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Lokale Mietstation in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inlineskates, Fahrrädern, Rollschuhen, Skateboards und Longboards, direkt gegenüber dem Strand und neben dem Port Olímpic.",
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
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/de/location-contact/",
      "name": "Standort von RSB Rental Scooter Barcelona in Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Finde RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta. Adresse, WhatsApp, Öffnungszeiten, Karte und Anfahrt.",
      "inLanguage": "de",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/de/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/location-contact/#faq"
        }
      ],
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#breadcrumb",
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
          "name": "Standort & Kontakt",
          "item": "https://rentalscooterbarcelona.com/de/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokale Mietstation in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inlineskates, Fahrrädern, Rollschuhen, Skateboards und Longboards, direkt gegenüber dem Strand und neben dem Port Olímpic.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
        "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
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
          "contactType": "Kundenservice",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Wo befindet sich RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona befindet sich in der Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Wie kann ich RSB Rental Scooter Barcelona kontaktieren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kannst anrufen oder eine WhatsApp-Nachricht an +34 640 559 468 senden, eine E-Mail an info@rentalscooterbarcelona.com schreiben oder das Kontaktformular auf dieser Seite nutzen."
          }
        },
        {
          "@type": "Question",
          "name": "Wie sind die Öffnungszeiten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Täglich geöffnet: 10:30–13:30 und 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Liegt die Station nahe am Strand?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Die Station liegt in Vila Olímpica, nur wenige Gehminuten von Port Olímpic und Barceloneta entfernt."
          }
        }
      ],
      "inLanguage": "de"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "maria yo"
      },
      "datePublished": "2021-08-09",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Super nette Leute! Perfekte Standort um von dort direkt zum Strand Skaten, Radfahrern oder sonst...dann die Küste entlang weiter zu entdecken... […] Ich kann es nur empfehlen. Danke euch!“\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "James Liddell"
      },
      "datePublished": "2019-02-15",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Sehr hilfsbereite Frau. Günstiger Preis und tolle Lage.“\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Luz"
      },
      "datePublished": "2026-03-08",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"„Wir sind mit meinem Sohn zum Port Olímpic gekommen, um zu skaten, und die Ausrüstung war großartig. Auch der Service war sehr freundlich, vielen Dank!!“\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Locatie van RSB Rental Scooter Barcelona in Vila Olímpica</title>
<meta content="Vind RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Adres, WhatsApp, openingstijden, kaart en route." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/nl/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Locatie van RSB Rental Scooter Barcelona in Vila Olímpica" property="og:title"/>
<meta content="Vind RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Adres, WhatsApp, openingstijden, kaart en route." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/nl/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Winkel van RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou vlak bij Port Olímpic en Barceloneta" property="og:image:alt"/>
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
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Locatie van RSB Rental Scooter Barcelona in Vila Olímpica" name="twitter:title"/>
<meta content="Vind RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Adres, WhatsApp, openingstijden, kaart en route." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Winkel van RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou vlak bij Port Olímpic en Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, voor scooters huren, inline skates huren, fietsen huren, rolschaatsen, skateboard en longboard vlak bij Barceloneta en Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/nl/location-contact/",
      "name": "Locatie van RSB Rental Scooter Barcelona in Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Vind RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Adres, WhatsApp, openingstijden, kaart en route.",
      "inLanguage": "nl",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#faq"
        }
      ],
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#breadcrumb",
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
          "name": "Locatie & contact",
          "item": "https://rentalscooterbarcelona.com/nl/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, voor scooters huren, inline skates huren, fietsen huren, rolschaatsen, skateboard en longboard vlak bij Barceloneta en Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Waar is RSB Rental Scooter Barcelona gevestigd?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona is gevestigd aan Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Hoe kan ik contact opnemen met RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken."
          }
        },
        {
          "@type": "Question",
          "name": "Wat zijn de openingstijden?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Elke dag geopend: 10:30–13:30 en 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Is de winkel dicht bij het strand?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. De winkel ligt in Vila Olímpica, tegenover het strand en naast Port Olímpic."
          }
        }
      ],
      "inLanguage": "nl"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Yassine Souri"
      },
      "datePublished": "2026-07-30",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"De beste verhuurplek voor rollers 🛼. Je kunt langs Barceloneta gaan. Geweldige tijd en ervaring. De eigenaar is ook een geweldige man. Ik raad het ten zeerste aan.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-2",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "sofie van santen"
      },
      "datePublished": "2024-07-29",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Hele aardige eigenaresse!\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Luz"
      },
      "datePublished": "2026-03-08",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"We kwamen met mijn zoon naar Port Olímpic om te skaten en de uitrusting was geweldig. De service was ook erg vriendelijk, heel erg bedankt!!\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Localização da RSB Rental Scooter Barcelona em Vila Olímpica</title>
<meta content="Encontre a RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta. Morada, WhatsApp, horários, mapa e direções." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pt/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Localização da RSB Rental Scooter Barcelona em Vila Olímpica" property="og:title"/>
<meta content="Encontre a RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta. Morada, WhatsApp, horários, mapa e direções." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pt/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Loja da RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou perto do Port Olímpic e da Barceloneta" property="og:image:alt"/>
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
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Localização da RSB Rental Scooter Barcelona em Vila Olímpica" name="twitter:title"/>
<meta content="Encontre a RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta. Morada, WhatsApp, horários, mapa e direções." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Loja da RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou perto do Port Olímpic e da Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de quatro rodas, skateboard e longboard perto da Barceloneta e do Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/pt/location-contact/",
      "name": "Localização da RSB Rental Scooter Barcelona em Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Encontre a RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta. Morada, WhatsApp, horários, mapa e direções.",
      "inLanguage": "pt-PT",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#faq"
        }
      ],
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#breadcrumb",
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
          "name": "Localização e contacto",
          "item": "https://rentalscooterbarcelona.com/pt/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de quatro rodas, skateboard e longboard perto da Barceloneta e do Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Onde fica a RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A RSB Rental Scooter Barcelona fica em Carrer de Salvador Espriu, 63, 08005 Barcelona, em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Como posso contactar a RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pode ligar ou enviar WhatsApp para +34 640 559 468, escrever para info@rentalscooterbarcelona.com ou usar o formulário desta página."
          }
        },
        {
          "@type": "Question",
          "name": "Quais são os horários?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Aberto todos os dias: 10:30–13:30 e 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "A loja fica perto da praia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. A loja fica em Vila Olímpica, a poucos minutos a pé do Port Olímpic e da Barceloneta."
          }
        }
      ],
      "inLanguage": "pt-PT"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Yassine Souri"
      },
      "datePublished": "2026-07-30",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"O melhor local para alugar rollers 🛼. Pode ir ao longo da Barceloneta. Um tempo e uma experiência incríveis. O proprietário também é uma pessoa maravilhosa. Recomendo muito.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-2",
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
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Luz"
      },
      "datePublished": "2026-03-08",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Viemos ao Port Olímpic patinar com o meu filho e o equipamento foi ótimo. O atendimento também foi muito agradável, muito obrigado!!\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Ubicació de RSB Rental Scooter Barcelona a Vila Olímpica</title>
<meta content="Troba RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta. Adreça, WhatsApp, horaris, mapa i com arribar-hi." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/cat/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Ubicació de RSB Rental Scooter Barcelona a Vila Olímpica" property="og:title"/>
<meta content="Troba RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta. Adreça, WhatsApp, horaris, mapa i com arribar-hi." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/cat/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Botiga de RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou a prop del Port Olímpic i la Barceloneta" property="og:image:alt"/>
<meta content="ca_ES" property="og:locale"/><meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="pl_PL" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Ubicació de RSB Rental Scooter Barcelona a Vila Olímpica" name="twitter:title"/>
<meta content="Troba RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta. Adreça, WhatsApp, horaris, mapa i com arribar-hi." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Botiga de RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou a prop del Port Olímpic i la Barceloneta" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<noscript></noscript>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/><link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/><link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de la Barceloneta i el Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/cat/location-contact/",
      "name": "Ubicació de RSB Rental Scooter Barcelona a Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Troba RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta. Adreça, WhatsApp, horaris, mapa i com arribar-hi.",
      "inLanguage": "ca",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#faq"
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#breadcrumb",
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
          "name": "Ubicació i contacte",
          "item": "https://rentalscooterbarcelona.com/cat/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de la Barceloneta i el Port Olímpic.",
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
          "contactType": "customer service",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "On és RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona és al Carrer de Salvador Espriu, 63, 08005 Barcelona, a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta."
          }
        },
        {
          "@type": "Question",
          "name": "Com puc contactar amb RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pots trucar o enviar WhatsApp al +34 640 559 468, escriure a info@rentalscooterbarcelona.com o fer servir el formulari d’aquesta pàgina."
          }
        },
        {
          "@type": "Question",
          "name": "Quin és l’horari?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Obert cada dia: 10:30–13:30 i 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "La botiga és a prop de la platja?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí. La botiga és a la Vila Olímpica, davant de la platja i al costat del Port Olímpic."
          }
        }
      ],
      "inLanguage": "ca"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "James Liddell"
      },
      "datePublished": "2019-02-15",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Dona molt servicial. Preu barat i ubicació fantàstica.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-2",
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
      "reviewBody": "\"Vam llogar patins en línia a Barcelona durant les vacances. També tenen patins de quatre rodes. La botiga és a la Vila Olímpica, al costat del passeig marítim i prop de la Barceloneta. Bon preu i una atenció genial, ho recomano al 100%.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Michel new technology"
      },
      "datePublished": "2020-09-24",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"L’assistent de la botiga era molt agradable i divertit. Tornarem l’any que ve i ho recomanarem a tots els nostres amics i familiars. Moltes gràcies per l’ajuda, per les recomanacions i per l’amabilitat! Bons preus i bona atenció.\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Plats för RSB Rental Scooter Barcelona i Vila Olímpica</title>
<meta content="Hitta RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Adress, WhatsApp, öppettider, karta och vägbeskrivning." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/sv/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Plats för RSB Rental Scooter Barcelona i Vila Olímpica" property="og:title"/>
<meta content="Hitta RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Adress, WhatsApp, öppettider, karta och vägbeskrivning." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/sv/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Butiken RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou mitt emot stranden och intill Port Olímpic" property="og:image:alt"/>
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
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Plats för RSB Rental Scooter Barcelona i Vila Olímpica" name="twitter:title"/>
<meta content="Hitta RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Adress, WhatsApp, öppettider, karta och vägbeskrivning." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Butiken RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou mitt emot stranden och intill Port Olímpic" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med hyra av scooter, inlines, cykel, rullskridskor, skateboard och longboard mitt emot stranden och intill Port Olímpic.",
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
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/sv/location-contact/",
      "name": "Plats för RSB Rental Scooter Barcelona i Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Hitta RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Adress, WhatsApp, öppettider, karta och vägbeskrivning.",
      "inLanguage": "sv",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#faq"
        }
      ],
      "publisher": {
        "@id": "https://rentalscooterbarcelona.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#breadcrumb",
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
          "name": "Plats & kontakt",
          "item": "https://rentalscooterbarcelona.com/sv/location-contact/"
        }
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://rentalscooterbarcelona.com/#business",
      "name": "RSB Rental Scooter Barcelona",
      "alternateName": "RSB",
      "url": "https://rentalscooterbarcelona.com/",
      "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med hyra av scooter, inlines, cykel, rullskridskor, skateboard och longboard mitt emot stranden och intill Port Olímpic.",
      "image": [
        "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp",
        "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"
      ],
      "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp",
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
          "contactType": "kundservice",
          "email": "info@rentalscooterbarcelona.com",
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Var ligger RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona ligger på Carrer de Salvador Espriu, 63, 08005 Barcelona, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic."
          }
        },
        {
          "@type": "Question",
          "name": "Hur kan jag kontakta RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan."
          }
        },
        {
          "@type": "Question",
          "name": "Vilka är öppettiderna?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Öppet varje dag: 10:30–13:30 och 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Ligger butiken nära stranden?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Butiken ligger i Vila Olímpica, en kort promenad från Port Olímpic och Barceloneta."
          }
        }
      ],
      "inLanguage": "sv"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "James Liddell"
      },
      "datePublished": "2019-02-15",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Mycket hjälpsam kvinna. Lågt pris och fantastiskt läge.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-2",
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
      "reviewBody": "\"Vi hyrde inlines i Barcelona under semestern. De har även fyrhjuliga rullskridskor. Butiken ligger i Vila Olímpica, intill strandpromenaden och nära Barceloneta. Bra pris och fantastisk service, jag rekommenderar den till 100 procent.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Michel new technology"
      },
      "datePublished": "2020-09-24",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Butiksbiträdet var mycket trevligt och roligt. Vi kommer tillbaka nästa år och kommer att rekommendera stället till alla våra vänner och släktingar. Tack så mycket för hjälpen, rekommendationerna och det vänliga bemötandet! Bra priser och bra service.\"",
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
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Lokalizacja RSB Rental Scooter Barcelona w Vila Olímpica</title>
<meta content="Znajdź RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Adres, WhatsApp, godziny otwarcia, mapa i dojazd." name="description"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="RSB Rental Scooter Barcelona" name="author"/>
<meta content="#0b1022" name="theme-color"/>
<link href="https://rentalscooterbarcelona.com/pl/location-contact/" rel="canonical"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="x-default" rel="alternate"/><link href="https://rentalscooterbarcelona.com/location-contact/" hreflang="en" rel="alternate"/><link href="https://rentalscooterbarcelona.com/es/location-contact/" hreflang="es" rel="alternate"/><link href="https://rentalscooterbarcelona.com/fr/location-contact/" hreflang="fr" rel="alternate"/><link href="https://rentalscooterbarcelona.com/it/location-contact/" hreflang="it" rel="alternate"/><link href="https://rentalscooterbarcelona.com/de/location-contact/" hreflang="de" rel="alternate"/><link href="https://rentalscooterbarcelona.com/nl/location-contact/" hreflang="nl" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pt/location-contact/" hreflang="pt" rel="alternate"/><link href="https://rentalscooterbarcelona.com/cat/location-contact/" hreflang="ca" rel="alternate"/><link href="https://rentalscooterbarcelona.com/sv/location-contact/" hreflang="sv" rel="alternate"/><link href="https://rentalscooterbarcelona.com/pl/location-contact/" hreflang="pl" rel="alternate"/>
<meta content="ES-CT" name="geo.region"/>
<meta content="Barcelona" name="geo.placename"/>
<meta content="41.3906488;2.1984312" name="geo.position"/>
<meta content="41.3906488, 2.1984312" name="ICBM"/>
<meta content="website" property="og:type"/>
<meta content="RSB Rental Scooter Barcelona" property="og:site_name"/>
<meta content="Lokalizacja RSB Rental Scooter Barcelona w Vila Olímpica" property="og:title"/>
<meta content="Znajdź RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Adres, WhatsApp, godziny otwarcia, mapa i dojazd." property="og:description"/>
<meta content="https://rentalscooterbarcelona.com/pl/location-contact/" property="og:url"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" property="og:image:secure_url"/>
<meta content="image/webp" property="og:image:type"/>
<meta content="585" property="og:image:width"/>
<meta content="594" property="og:image:height"/>
<meta content="Wypożyczalnia RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou naprzeciwko plaży i obok Port Olímpic" property="og:image:alt"/>
<meta content="pl_PL" property="og:locale"/>
<meta content="en_GB" property="og:locale:alternate"/><meta content="es_ES" property="og:locale:alternate"/><meta content="fr_FR" property="og:locale:alternate"/><meta content="it_IT" property="og:locale:alternate"/><meta content="de_DE" property="og:locale:alternate"/><meta content="nl_NL" property="og:locale:alternate"/><meta content="pt_PT" property="og:locale:alternate"/><meta content="ca_ES" property="og:locale:alternate"/><meta content="sv_SE" property="og:locale:alternate"/>
<meta content="summary_large_image" name="twitter:card"/><meta content="@RSBscooterbarce" name="twitter:site"/>
<meta content="Lokalizacja RSB Rental Scooter Barcelona w Vila Olímpica" name="twitter:title"/>
<meta content="Znajdź RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Adres, WhatsApp, godziny otwarcia, mapa i dojazd." name="twitter:description"/>
<meta content="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" name="twitter:image"/>
<meta content="Wypożyczalnia RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou naprzeciwko plaży i obok Port Olímpic" name="twitter:image:alt"/>
<link href="https://rentalscooterbarcelona.com/favicon.ico" rel="icon" sizes="any"/>
<link href="https://rentalscooterbarcelona.com/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/favicon-512x512.png" rel="icon" sizes="512x512" type="image/png"/>
<link href="https://rentalscooterbarcelona.com/apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="RSB Rental Scooter Barcelona" name="application-name"/>
<meta content="RSB Wynajem" name="apple-mobile-web-app-title"/>
<link crossorigin="" href="https://www.googletagmanager.com" rel="preconnect"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<link as="image" fetchpriority="high" href="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp" imagesizes="100vw" imagesrcset="https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp 1200w" rel="preload"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&amp;family=Space+Grotesk:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://rentalscooterbarcelona.com/stylesHome.css?v=20260813" rel="stylesheet"/>
<script data-rsb-dynamic-hours="" type="application/ld+json">
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
      "@type": [
        "ContactPage",
        "WebPage"
      ],
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage",
      "url": "https://rentalscooterbarcelona.com/pl/location-contact/",
      "name": "RSB Rental Scooter Barcelona Lokalizacja w Vila Olímpica",
      "isPartOf": {
        "@id": "https://rentalscooterbarcelona.com/#website"
      },
      "about": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "description": "Znajdź RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Adres, WhatsApp, godziny otwarcia, mapa i dojazd.",
      "inLanguage": "pl",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"
      },
      "breadcrumb": {
        "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#breadcrumb"
      },
      "mainEntity": [
        {
          "@id": "https://rentalscooterbarcelona.com/#business"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#faq"
        }
      ],
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
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#breadcrumb",
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
          "name": "Lokalizacja i kontakt",
          "item": "https://rentalscooterbarcelona.com/pl/location-contact/"
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
      "@type": "FAQPage",
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Gdzie znajduje się RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "RSB Rental Scooter Barcelona znajduje się przy Carrer de Salvador Espriu, 63, 08005 Barcelona, w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic."
          }
        },
        {
          "@type": "Question",
          "name": "Jak mogę skontaktować się z RSB Rental Scooter Barcelona?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Możesz zadzwonić lub wysłać WhatsApp na +34 640 559 468, napisać na info@rentalscooterbarcelona.com albo użyć formularza kontaktowego na tej stronie."
          }
        },
        {
          "@type": "Question",
          "name": "Jakie są godziny otwarcia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Otwarte codziennie: 10:30–13:30 i 16:30–20:00."
          }
        },
        {
          "@type": "Question",
          "name": "Czy wypożyczalnia jest blisko plaży?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tak. Wypożyczalnia znajduje się w Vila Olímpica, kilka minut spacerem od Port Olímpic i plaży Barceloneta."
          }
        }
      ],
      "inLanguage": "pl"
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
<meta content="3_Dfcq2jy9ccTlZt6JQm9ltOZ7UvN2QvG1PhZajyPy8" name="google-site-verification"/>
<style id="index7-home-hero-motion">
.home-page .card-elevated{background:#cfe4ff !important;border-color:rgba(59,130,246,0.30) !important;}
.hero-bg img.zoom{animation:homeHeroZoomIndex7 12s linear forwards !important;transform-origin:center 42% !important;}
@keyframes homeHeroZoomIndex7{from{transform:scale(1);}to{transform:scale(1.07);}}
@media (max-width:640px){
  .hero-bg img{object-position:center 24% !important;}
  .hero-bg img.zoom{animation:homeHeroZoomMobileIndex7 12s linear forwards !important;transform-origin:center 28% !important;}
  @keyframes homeHeroZoomMobileIndex7{from{transform:scale(1);}to{transform:scale(1.02);}}
}
</style>
<style id="index11-home-seo-links">
.hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.hero-service-link:hover{background:rgba(255,255,255,.18)}
@media (max-width:640px){.hero-service-links{gap:.45rem}.hero-service-link{font-size:.74rem;padding:.42rem .62rem;white-space:nowrap}}

.highlight-bar h2{margin:0;font-size:1.02rem;font-weight:800;line-height:1.15}
.highlight-bar p{margin:.2rem 0 0}</style>
<style id="home7-hero-pill-tuning">
.hero .pills{gap:.55rem;justify-content:center}
.hero .pills .pill{box-shadow:0 8px 18px rgba(15,23,42,.12) !important;display:inline-flex;align-items:center;justify-content:center}
.hero-service-links{justify-content:center}
.hero-service-link,
.hero-service-link.more-rentals-link{font-size:.78rem;padding:.42rem .64rem;text-align:center}
@media (max-width:640px){
  .hero-service-links{justify-content:center}
  .hero-service-link,
  .hero-service-link.more-rentals-link{font-size:.72rem;padding:.4rem .58rem}
}
.scooter-media-badge{position:absolute;bottom:14px;left:14px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.48rem .72rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.74rem;line-height:1;letter-spacing:.01em;box-shadow:0 10px 24px rgba(15,23,42,.18);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .media{position:relative}
.home-page .home-service-card .media-price-from{position:absolute;left:12px;top:12px;z-index:3;display:inline-flex;align-items:center;justify-content:center;padding:.42rem .68rem;border-radius:999px;background:rgba(11,16,34,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:800;font-size:.72rem;line-height:1;letter-spacing:.01em;box-shadow:0 8px 20px rgba(15,23,42,.16);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);text-align:center}
.home-page .home-service-card .price-row{display:flex;align-items:baseline;gap:.5rem;width:100%}
.home-page .home-service-card .price-prefix{display:block;flex:0 0 auto;font-weight:800;font-size:.82rem;line-height:1;color:var(--foreground)}
.home-page .home-service-card .price-right{display:flex;align-items:baseline;gap:.3rem;margin-left:auto;justify-content:flex-end;text-align:right;flex:0 0 auto}
.home-page .home-service-card .price-row .price,
.home-page .home-service-card .price-row .price-unit{display:block}
@media (max-width:640px){
  .scooter-media-badge{bottom:12px;left:12px;font-size:.66rem;padding:.42rem .6rem;max-width:calc(100% - 24px)}
  .home-page .home-service-card .media-price-from{top:10px;left:10px;font-size:.64rem;padding:.38rem .56rem}
}
</style>
<style id="home-card-cta-contrast">
.home-page .card-elevated .btn.btn-outline-dark{
  background:rgba(37,99,235,.14) !important;
  border:1px solid rgba(37,99,235,.28) !important;
  color:#0f172a !important;
  box-shadow:0 6px 16px rgba(37,99,235,.12) !important;
  font-weight:700 !important;
}
.home-page .card-elevated .btn.btn-outline-dark:hover,
.home-page .card-elevated .btn.btn-outline-dark:focus-visible{
  background:rgba(37,99,235,.20) !important;
  border-color:rgba(37,99,235,.38) !important;
  box-shadow:0 8px 20px rgba(37,99,235,.16) !important;
}

.home-cta-row{display:flex;justify-content:center;align-items:center;gap:.75rem;flex-wrap:nowrap;margin-top:1.5rem}
.home-cta-row .home-cta-btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.62rem 1rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;white-space:nowrap;flex:1 1 0;min-width:0;max-width:220px}
.home-cta-row .home-cta-btn.prices-btn{background:#2563eb;color:#fff;box-shadow:0 10px 24px rgba(37,99,235,.18)}
.home-cta-row .home-cta-btn.whatsapp-btn{background:#0f766e;color:#fff;box-shadow:0 10px 24px rgba(15,118,110,.16)}
.home-cta-row .home-cta-btn svg{flex:0 0 auto}
.home-page .home-service-card{border:1px solid rgba(59,130,246,.36) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.18) inset !important;overflow:hidden;margin-bottom:1rem}
.home-page .home-service-card + .home-service-card{margin-top:.15rem}
.home-page .highlight-bar{padding:.82rem 1rem .8rem;background:linear-gradient(180deg,#3b82f6 0%,#3179e8 100%)}
.home-page .highlight-bar h2{color:#fff !important;font-size:1.28rem !important;font-weight:900 !important;line-height:1.06 !important;letter-spacing:-.01em}
.home-page .highlight-bar p{color:rgba(255,255,255,.9) !important;font-size:.74rem !important;font-weight:700 !important;line-height:1.18 !important;margin:.18rem 0 0 !important;text-transform:uppercase;letter-spacing:.04em}
.home-page .card-title{font-size:1.44rem !important;line-height:1.12 !important;font-weight:800 !important;letter-spacing:-.01em;color:#0f172a !important}
.home-page .card-desc{font-size:1rem !important;line-height:1.62 !important;color:#475569 !important}
.home-page .home-map-card{padding:.7rem !important;overflow:hidden;border:1px solid rgba(59,130,246,.34) !important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset !important;margin-top:.6rem !important}
.home-page .home-map-card .map-top-cta{display:flex;justify-content:center;margin-bottom:.7rem}
.home-page .home-map-card .map-cta-btn{width:100%;max-width:320px}
.home-page .home-map-card .map-wrap{margin-top:0}
@media (max-width:640px){
  .home-cta-row{gap:.55rem}
  .home-cta-row .home-cta-btn{font-size:.84rem;padding:.58rem .72rem;max-width:none}
  .home-page .card-title{font-size:1.48rem !important}
  .home-page .highlight-bar h2{font-size:1.16rem !important}
  .home-page .highlight-bar p{font-size:.68rem !important}
}
</style>
<style id="location-contact-page-styles">
.location-contact-page .hero{min-height:82vh}
.location-contact-page .hero-bg img.zoom{animation:locationHeroZoom 12s linear forwards !important;transform-origin:center 46% !important}
@keyframes locationHeroZoom{from{transform:scale(1)}to{transform:scale(1.06)}}
.location-contact-page .upper{font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.location-contact-page .hero-service-links{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem;max-width:48rem}
.location-contact-page .hero-service-link{display:inline-flex;align-items:center;justify-content:center;padding:.45rem .75rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.12);color:#fff;text-decoration:none;font-weight:700;font-size:.84rem;line-height:1.1;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.location-contact-page .hero-service-link:hover{background:rgba(255,255,255,.18)}
.location-contact-page .home-map-card{overflow:hidden;border:1px solid rgba(59,130,246,.34)!important;box-shadow:0 10px 24px rgba(15,23,42,.06),0 0 0 1px rgba(255,255,255,.16) inset!important}
.location-contact-page .map-wrap{position:relative;border-radius:18px;overflow:hidden;min-height:370px}
.location-contact-page .map-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.location-contact-page .map-click-target{position:absolute;inset:0;z-index:2}
.location-contact-page .map-label{padding:.8rem .25rem 0 .25rem}
@media (max-width:640px){
  .location-contact-page .hero-service-link{font-size:.74rem;padding:.42rem .62rem}
  .location-contact-page .map-wrap{min-height:320px}
}
</style><script data-rsb-review-entities="" type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage",
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
          "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-1"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-2"
        },
        {
          "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-3"
        }
      ]
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-1",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "James Liddell"
      },
      "datePublished": "2019-02-15",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Bardzo pomocna kobieta. Niska cena i świetna lokalizacja.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-2",
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
      "reviewBody": "\"Podczas wakacji wynajęliśmy rolki w Barcelonie. Mają również wrotki na czterech kółkach. Sklep znajduje się w Vila Olímpica, obok nadmorskiej promenady i blisko Barcelonety. Dobra cena i świetna obsługa, polecam w 100 procentach.\"",
      "publisher": {
        "@type": "Organization",
        "name": "Google"
      }
    },
    {
      "@type": "Review",
      "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-3",
      "itemReviewed": {
        "@id": "https://rentalscooterbarcelona.com/#business"
      },
      "author": {
        "@type": "Person",
        "name": "Michel new technology"
      },
      "datePublished": "2020-09-24",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 5,
        "bestRating": 5,
        "worstRating": 1
      },
      "reviewBody": "\"Pracownik sklepu był bardzo miły i zabawny. Wrócimy w przyszłym roku i polecimy to miejsce wszystkim naszym znajomym i rodzinie. Bardzo dziękujemy za pomoc, rekomendacje i życzliwość! Dobre ceny i dobra obsługa.\"",
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
| en | https://rentalscooterbarcelona.com/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| es | https://rentalscooterbarcelona.com/es/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| fr | https://rentalscooterbarcelona.com/fr/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| it | https://rentalscooterbarcelona.com/it/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| de | https://rentalscooterbarcelona.com/de/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| nl | https://rentalscooterbarcelona.com/nl/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| pt | https://rentalscooterbarcelona.com/pt/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| ca | https://rentalscooterbarcelona.com/cat/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| sv | https://rentalscooterbarcelona.com/sv/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |
| pl | https://rentalscooterbarcelona.com/pl/location-contact/ | [{"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "x-default", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/location-contact/", "hreflang": "en", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/es/location-contact/", "hreflang": "es", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "hreflang": "fr", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/it/location-contact/", "hreflang": "it", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/de/location-contact/", "hreflang": "de", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "hreflang": "nl", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "hreflang": "pt", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "hreflang": "ca", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "hreflang": "sv", "rel": "alternate"}, {"line": 13, "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "hreflang": "pl", "rel": "alternate"}] | True |

## M. MATRIZ SCHEMA @id + URL

| Idioma | Bloque | Ruta | Entidad completa |
| --- | --- | --- | --- |
| en | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| en | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "en", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/location-contact/", "name": "RSB Rental Scooter Barcelona Location in Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Find RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach. Address, WhatsApp, opening hours, map and directions.", "inLanguage": "en", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp booking", "target": "https://wa.me/34640559468"}} |
| en | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/"}, {"@type": "ListItem", "position": 2, "name": "Location &amp; Contact", "item": "https://rentalscooterbarcelona.com/location-contact/"}]} |
| en | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Local rental shop in Vila Olímpica del Poblenou, Barcelona, offering scooter, inline skate, bike, roller skates, skateboard and longboard rentals near Barceloneta and Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| en | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Where is RSB Rental Scooter Barcelona located?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona is at Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach."}}, {"@type": "Question", "name": "How can I contact RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page."}}, {"@type": "Question", "name": "What are the opening hours?", "acceptedAnswer": {"@type": "Answer", "text": "Open every day: 10:30–13:30 and 16:30–20:00."}}, {"@type": "Question", "name": "Is the shop near the beach?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The shop is in Vila Olímpica, a short walk from Port Olímpic and Barceloneta Beach."}}], "inLanguage": "en"} |
| en | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/location-contact/#webpage", "dateModified": "2026-08-24"} |
| en | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-3"}]} |
| en | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Best Rollers 🛼 rental spot , You can go alongside Barceloneta. Amazing time and experience. The owner is also a wonderful guy. I recommend a lot\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-07-30"} |
| en | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Really helpfull women. Cheap price and great location\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2019-02-15"} |
| en | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Crystal S"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"What a friendly and patient one person operated business. Several people were approached for rental and I was the only non-Spanish and non-Catalan speaking person. We were not in a hurry, so I motioned to take others. But no, he was patient, explained how to operate equipment and walked us to an area to try it out before we went off on our own. I thought the price was reasonable too. Would definitely visit again and suggest that others visit. Oh the only thing it did not come with a lock, which was fine for us. But no way I would leave unattended on beach.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2019-09-28"} |
| es | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de la Barceloneta y el Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| es | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "es", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| es | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/es/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/es/location-contact/", "name": "Ubicación y contacto \| RSB Rental Scooter Barcelona", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Ubicación y contacto de RSB Rental Scooter Barcelona en la Vila Olímpica, cerca de Port Olímpic y Barceloneta. Dirección, WhatsApp, horarios y mapa.", "inLanguage": "es", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/es/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/es/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "Reserva por WhatsApp", "target": "https://wa.me/34640559468"}} |
| es | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://rentalscooterbarcelona.com/es/"}, {"@type": "ListItem", "position": 2, "name": "Ubicación y contacto", "item": "https://rentalscooterbarcelona.com/es/location-contact/"}]} |
| es | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Tienda local de alquiler en Vila Olímpica del Poblenou, Barcelona, con alquiler de scooters, patines en línea, bicicletas, patines de 4 ruedas, skateboard y longboard cerca de la Barceloneta y el Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "customer service", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "booking", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| es | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "¿Dónde está RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona está en Carrer de Salvador Espriu, 63, 08005 Barcelona, en Vila Olímpica del Poblenou, cerca del Port Olímpic y la Barceloneta."}}, {"@type": "Question", "name": "¿Cómo puedo contactar con RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Puedes llamar o enviar WhatsApp al +34 640 559 468, escribir a info@rentalscooterbarcelona.com o usar el formulario de esta página."}}, {"@type": "Question", "name": "¿Cuál es el horario?", "acceptedAnswer": {"@type": "Answer", "text": "Abierto todos los días: 10:30–13:30 y 16:30–20:00."}}, {"@type": "Question", "name": "¿La tienda está cerca de la playa?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. La tienda está en Vila Olímpica, frente a la playa y junto a Port Olímpic."}}], "inLanguage": "es"} |
| es | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#webpage", "dateModified": "2026-08-24"} |
| es | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-3"}]} |
| es | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Pequeña sorpresa junto a la playa de Barcelona. Mi experiencia fué genial. Precios razonables y a un tiro de piedra del paseo marítimo. Lo mejor de todo, la atención de la propietaria.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| es | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Experiencia increíble, buena ubicación y personal súper amable. 100% recomendable. Mil gracias Natalia por tu disponibilidad, tu ayuda y tus consejos!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| es | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Lo recomiendo ampliamente! Muy buena experiencia, muy amables y muy buen coste. La ubicación ideal.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant la location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de la Barceloneta et du Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| fr | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "fr"} |
| fr | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/fr/location-contact/", "name": "Adresse de RSB Rental Scooter Barcelona à Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Trouvez RSB Rental Scooter Barcelona à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta. Adresse, WhatsApp, horaires, plan et itinéraire.", "inLanguage": "fr", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/fr/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/fr/location-contact/#faq"}]} |
| fr | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://rentalscooterbarcelona.com/fr/"}, {"@type": "ListItem", "position": 2, "name": "Adresse et contact", "item": "https://rentalscooterbarcelona.com/fr/location-contact/"}]} |
| fr | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Boutique locale de location à Vila Olímpica del Poblenou, Barcelone, proposant la location de scooters, rollers en ligne, vélos, rollers classiques, skateboard et longboard près de la Barceloneta et du Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| fr | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Où se trouve RSB Rental Scooter Barcelona ?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona se trouve au Carrer de Salvador Espriu, 63, 08005 Barcelone, à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta."}}, {"@type": "Question", "name": "Comment contacter RSB Rental Scooter Barcelona ?", "acceptedAnswer": {"@type": "Answer", "text": "Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page."}}, {"@type": "Question", "name": "Quels sont les horaires ?", "acceptedAnswer": {"@type": "Answer", "text": "Ouvert tous les jours : 10:30–13:30 et 16:30–20:00."}}, {"@type": "Question", "name": "La boutique est-elle près de la plage ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. La boutique se trouve à Vila Olímpica, face à la plage et à côté du Port Olímpic."}}], "inLanguage": "fr"} |
| fr | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage", "dateModified": "2026-08-24"} |
| fr | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-3"}]} |
| fr | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Une petite surprise près de la plage de Barcelone. Mon expérience a été géniale. Des prix raisonnables et à deux pas de la promenade maritime. Le meilleur de tout, l’accueil de la propriétaire.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Expérience incroyable, bon emplacement et personnel très aimable. Recommandé à 100 %. Mille mercis à Natalia pour ta disponibilité, ton aide et tes conseils !\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| fr | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Je le recommande vivement ! Très bonne expérience, personnel très aimable et très bon prix. L’emplacement est idéal.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino alla Barceloneta e al Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| it | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "it"} |
| it | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/it/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/it/location-contact/", "name": "Dove si trova RSB Rental Scooter Barcelona a Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Trova RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta. Indirizzo, WhatsApp, orari, mappa e indicazioni.", "inLanguage": "it", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/it/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/it/location-contact/#faq"}]} |
| it | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inizio", "item": "https://rentalscooterbarcelona.com/it/"}, {"@type": "ListItem", "position": 2, "name": "Dove siamo e contatti", "item": "https://rentalscooterbarcelona.com/it/location-contact/"}]} |
| it | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Negozio locale di noleggio a Vila Olímpica del Poblenou, Barcellona, con noleggio di scooter, pattini in linea, biciclette, pattini a rotelle, skateboard e longboard vicino alla Barceloneta e al Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| it | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Dove si trova RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona si trova in Carrer de Salvador Espriu, 63, 08005 Barcellona, a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta."}}, {"@type": "Question", "name": "Come posso contattare RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina."}}, {"@type": "Question", "name": "Quali sono gli orari?", "acceptedAnswer": {"@type": "Answer", "text": "Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00."}}, {"@type": "Question", "name": "Il negozio è vicino alla spiaggia?", "acceptedAnswer": {"@type": "Answer", "text": "Sì. Il negozio è a Vila Olímpica, di fronte alla spiaggia e accanto al Port Olímpic."}}], "inLanguage": "it"} |
| it | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#webpage", "dateModified": "2026-08-24"} |
| it | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-3"}]} |
| it | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Una piccola sorpresa vicino alla spiaggia di Barcellona. La mia esperienza è stata fantastica. Prezzi ragionevoli e a due passi dal lungomare. La cosa migliore è stata l’attenzione della proprietaria.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Esperienza incredibile, buona posizione e personale super gentile. Consigliato al 100%. Grazie mille Natalia per la tua disponibilità, il tuo aiuto e i tuoi consigli!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| it | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Lo consiglio vivamente! Ottima esperienza, persone molto gentili e ottimo prezzo. La posizione è ideale.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokale Mietstation in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inlineskates, Fahrrädern, Rollschuhen, Skateboards und Longboards, direkt gegenüber dem Strand und neben dem Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "Kundenservice", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| de | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "de", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| de | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/de/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/de/location-contact/", "name": "Standort von RSB Rental Scooter Barcelona in Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Finde RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta. Adresse, WhatsApp, Öffnungszeiten, Karte und Anfahrt.", "inLanguage": "de", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/de/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/de/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| de | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://rentalscooterbarcelona.com/de/"}, {"@type": "ListItem", "position": 2, "name": "Standort &amp; Kontakt", "item": "https://rentalscooterbarcelona.com/de/location-contact/"}]} |
| de | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokale Mietstation in Vila Olímpica del Poblenou, Barcelona, mit Scootern, Inlineskates, Fahrrädern, Rollschuhen, Skateboards und Longboards, direkt gegenüber dem Strand und neben dem Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kartenzahlung akzeptiert. PayPal für Online-Zahlungen verfügbar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Strand von Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "Kundenservice", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| de | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Wo befindet sich RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona befindet sich in der Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta."}}, {"@type": "Question", "name": "Wie kann ich RSB Rental Scooter Barcelona kontaktieren?", "acceptedAnswer": {"@type": "Answer", "text": "Du kannst anrufen oder eine WhatsApp-Nachricht an +34 640 559 468 senden, eine E-Mail an info@rentalscooterbarcelona.com schreiben oder das Kontaktformular auf dieser Seite nutzen."}}, {"@type": "Question", "name": "Wie sind die Öffnungszeiten?", "acceptedAnswer": {"@type": "Answer", "text": "Täglich geöffnet: 10:30–13:30 und 16:30–20:00."}}, {"@type": "Question", "name": "Liegt die Station nahe am Strand?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Die Station liegt in Vila Olímpica, nur wenige Gehminuten von Port Olímpic und Barceloneta entfernt."}}], "inLanguage": "de"} |
| de | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#webpage", "dateModified": "2026-08-24"} |
| de | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-3"}]} |
| de | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "maria yo"}, "datePublished": "2021-08-09", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Super nette Leute! Perfekte Standort um von dort direkt zum Strand Skaten, Radfahrern oder sonst...dann die Küste entlang weiter zu entdecken... […] Ich kann es nur empfehlen. Danke euch!“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Sehr hilfsbereite Frau. Günstiger Preis und tolle Lage.“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| de | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Wir sind mit meinem Sohn zum Port Olímpic gekommen, um zu skaten, und die Ausrüstung war großartig. Auch der Service war sehr freundlich, vielen Dank!!“\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, voor scooters huren, inline skates huren, fietsen huren, rolschaatsen, skateboard en longboard vlak bij Barceloneta en Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| nl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "nl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/nl/location-contact/", "name": "Locatie van RSB Rental Scooter Barcelona in Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Vind RSB Rental Scooter Barcelona in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Adres, WhatsApp, openingstijden, kaart en route.", "inLanguage": "nl", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/nl/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/nl/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| nl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rentalscooterbarcelona.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Locatie &amp; contact", "item": "https://rentalscooterbarcelona.com/nl/location-contact/"}]} |
| nl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokale verhuurwinkel in Vila Olímpica del Poblenou, Barcelona, voor scooters huren, inline skates huren, fietsen huren, rolschaatsen, skateboard en longboard vlak bij Barceloneta en Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| nl | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Waar is RSB Rental Scooter Barcelona gevestigd?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona is gevestigd aan Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta."}}, {"@type": "Question", "name": "Hoe kan ik contact opnemen met RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken."}}, {"@type": "Question", "name": "Wat zijn de openingstijden?", "acceptedAnswer": {"@type": "Answer", "text": "Elke dag geopend: 10:30–13:30 en 16:30–20:00."}}, {"@type": "Question", "name": "Is de winkel dicht bij het strand?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. De winkel ligt in Vila Olímpica, tegenover het strand en naast Port Olímpic."}}], "inLanguage": "nl"} |
| nl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage", "dateModified": "2026-08-24"} |
| nl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-3"}]} |
| nl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "datePublished": "2026-07-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"De beste verhuurplek voor rollers 🛼. Je kunt langs Barceloneta gaan. Geweldige tijd en ervaring. De eigenaar is ook een geweldige man. Ik raad het ten zeerste aan.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "sofie van santen"}, "datePublished": "2024-07-29", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Hele aardige eigenaresse!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| nl | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"We kwamen met mijn zoon naar Port Olímpic om te skaten en de uitrusting was geweldig. De service was ook erg vriendelijk, heel erg bedankt!!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de quatro rodas, skateboard e longboard perto da Barceloneta e do Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pt | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pt-PT", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/pt/location-contact/", "name": "Localização da RSB Rental Scooter Barcelona em Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Encontre a RSB Rental Scooter Barcelona em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta. Morada, WhatsApp, horários, mapa e direções.", "inLanguage": "pt-PT", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/pt/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/pt/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pt | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": "https://rentalscooterbarcelona.com/pt/"}, {"@type": "ListItem", "position": 2, "name": "Localização e contacto", "item": "https://rentalscooterbarcelona.com/pt/location-contact/"}]} |
| pt | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Loja local de aluguer em Vila Olímpica del Poblenou, Barcelona, com aluguer de scooters, patins em linha, bicicletas, patins de quatro rodas, skateboard e longboard perto da Barceloneta e do Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| pt | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Onde fica a RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "A RSB Rental Scooter Barcelona fica em Carrer de Salvador Espriu, 63, 08005 Barcelona, em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta."}}, {"@type": "Question", "name": "Como posso contactar a RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Pode ligar ou enviar WhatsApp para +34 640 559 468, escrever para info@rentalscooterbarcelona.com ou usar o formulário desta página."}}, {"@type": "Question", "name": "Quais são os horários?", "acceptedAnswer": {"@type": "Answer", "text": "Aberto todos os dias: 10:30–13:30 e 16:30–20:00."}}, {"@type": "Question", "name": "A loja fica perto da praia?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. A loja fica em Vila Olímpica, a poucos minutos a pé do Port Olímpic e da Barceloneta."}}], "inLanguage": "pt-PT"} |
| pt | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage", "dateModified": "2026-08-24"} |
| pt | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-3"}]} |
| pt | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "datePublished": "2026-07-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"O melhor local para alugar rollers 🛼. Pode ir ao longo da Barceloneta. Um tempo e uma experiência incríveis. O proprietário também é uma pessoa maravilhosa. Recomendo muito.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "João Junior"}, "datePublished": "2021-04-21", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pt | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Viemos ao Port Olímpic patinar com o meu filho e o equipamento foi ótimo. O atendimento também foi muito agradável, muito obrigado!!\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de la Barceloneta i el Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| ca | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "ca"} |
| ca | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/cat/location-contact/", "name": "Ubicació de RSB Rental Scooter Barcelona a Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Troba RSB Rental Scooter Barcelona a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta. Adreça, WhatsApp, horaris, mapa i com arribar-hi.", "inLanguage": "ca", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/cat/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/cat/location-contact/#faq"}]} |
| ca | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inici", "item": "https://rentalscooterbarcelona.com/cat/"}, {"@type": "ListItem", "position": 2, "name": "Ubicació i contacte", "item": "https://rentalscooterbarcelona.com/cat/location-contact/"}]} |
| ca | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Botiga local de lloguer a Vila Olímpica del Poblenou, Barcelona, amb lloguer de scooters, patins en línia, bicicletes, patins de quatre rodes, skateboard i longboard a prop de la Barceloneta i el Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Credit Card, Debit Card, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta Beach"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "customer service", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| ca | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "On és RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona és al Carrer de Salvador Espriu, 63, 08005 Barcelona, a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta."}}, {"@type": "Question", "name": "Com puc contactar amb RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Pots trucar o enviar WhatsApp al +34 640 559 468, escriure a info@rentalscooterbarcelona.com o fer servir el formulari d’aquesta pàgina."}}, {"@type": "Question", "name": "Quin és l’horari?", "acceptedAnswer": {"@type": "Answer", "text": "Obert cada dia: 10:30–13:30 i 16:30–20:00."}}, {"@type": "Question", "name": "La botiga és a prop de la platja?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. La botiga és a la Vila Olímpica, davant de la platja i al costat del Port Olímpic."}}], "inLanguage": "ca"} |
| ca | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage", "dateModified": "2026-08-24"} |
| ca | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-3"}]} |
| ca | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Dona molt servicial. Preu barat i ubicació fantàstica.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Vam llogar patins en línia a Barcelona durant les vacances. També tenen patins de quatre rodes. La botiga és a la Vila Olímpica, al costat del passeig marítim i prop de la Barceloneta. Bon preu i una atenció genial, ho recomano al 100%.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| ca | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"L’assistent de la botiga era molt agradable i divertit. Tornarem l’any que ve i ho recomanarem a tots els nostres amics i familiars. Moltes gràcies per l’ajuda, per les recomanacions i per l’amabilitat! Bons preus i bona atenció.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med hyra av scooter, inlines, cykel, rullskridskor, skateboard och longboard mitt emot stranden och intill Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "kundservice", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| sv | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "sv", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/sv/location-contact/", "name": "Plats för RSB Rental Scooter Barcelona i Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Hitta RSB Rental Scooter Barcelona i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. Adress, WhatsApp, öppettider, karta och vägbeskrivning.", "inLanguage": "sv", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/sv/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/sv/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| sv | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Hem", "item": "https://rentalscooterbarcelona.com/sv/"}, {"@type": "ListItem", "position": 2, "name": "Plats &amp; kontakt", "item": "https://rentalscooterbarcelona.com/sv/location-contact/"}]} |
| sv | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokal uthyrningsbutik i Vila Olímpica del Poblenou, Barcelona, med hyra av scooter, inlines, cykel, rullskridskor, skateboard och longboard mitt emot stranden och intill Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Kortbetalning accepteras. PayPal finns för onlinebetalningar.", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "Barceloneta-stranden"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "contactType": "kundservice", "email": "info@rentalscooterbarcelona.com", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22", "https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html"]} |
| sv | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Var ligger RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona ligger på Carrer de Salvador Espriu, 63, 08005 Barcelona, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic."}}, {"@type": "Question", "name": "Hur kan jag kontakta RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan."}}, {"@type": "Question", "name": "Vilka är öppettiderna?", "acceptedAnswer": {"@type": "Answer", "text": "Öppet varje dag: 10:30–13:30 och 16:30–20:00."}}, {"@type": "Question", "name": "Ligger butiken nära stranden?", "acceptedAnswer": {"@type": "Answer", "text": "Ja. Butiken ligger i Vila Olímpica, en kort promenad från Port Olímpic och Barceloneta."}}], "inLanguage": "sv"} |
| sv | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage", "dateModified": "2026-08-24"} |
| sv | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-3"}]} |
| sv | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mycket hjälpsam kvinna. Lågt pris och fantastiskt läge.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Vi hyrde inlines i Barcelona under semestern. De har även fyrhjuliga rullskridskor. Butiken ligger i Vila Olímpica, intill strandpromenaden och nära Barceloneta. Bra pris och fantastisk service, jag rekommenderar den till 100 procent.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| sv | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Butiksbiträdet var mycket trevligt och roligt. Vi kommer tillbaka nästa år och kommer att rekommendera stället till alla våra vänner och släktingar. Tack så mycket för hjälpen, rekommendationerna och det vänliga bemötandet! Bra priser och bra service.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 1 | $.@graph[0] | {"@type": "Organization", "@id": "https://rentalscooterbarcelona.com/#organization", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "image": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}]} |
| pl | 1 | $.@graph[1] | {"@type": "WebSite", "@id": "https://rentalscooterbarcelona.com/#website", "url": "https://rentalscooterbarcelona.com/", "name": "RSB Rental Scooter Barcelona", "inLanguage": "pl", "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[2] | {"@type": ["ContactPage", "WebPage"], "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage", "url": "https://rentalscooterbarcelona.com/pl/location-contact/", "name": "RSB Rental Scooter Barcelona Lokalizacja w Vila Olímpica", "isPartOf": {"@id": "https://rentalscooterbarcelona.com/#website"}, "about": {"@id": "https://rentalscooterbarcelona.com/#business"}, "description": "Znajdź RSB Rental Scooter Barcelona w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic. Adres, WhatsApp, godziny otwarcia, mapa i dojazd.", "inLanguage": "pl", "primaryImageOfPage": {"@type": "ImageObject", "url": "https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp"}, "breadcrumb": {"@id": "https://rentalscooterbarcelona.com/pl/location-contact/#breadcrumb"}, "mainEntity": [{"@id": "https://rentalscooterbarcelona.com/#business"}, {"@id": "https://rentalscooterbarcelona.com/pl/location-contact/#faq"}], "publisher": {"@id": "https://rentalscooterbarcelona.com/#organization"}, "potentialAction": {"@type": "CommunicateAction", "name": "WhatsApp rezerwacja", "target": "https://wa.me/34640559468"}} |
| pl | 1 | $.@graph[3] | {"@type": "BreadcrumbList", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": "https://rentalscooterbarcelona.com/pl/"}, {"@type": "ListItem", "position": 2, "name": "Lokalizacja i kontakt", "item": "https://rentalscooterbarcelona.com/pl/location-contact/"}]} |
| pl | 1 | $.@graph[4] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "name": "RSB Rental Scooter Barcelona", "alternateName": "RSB", "url": "https://rentalscooterbarcelona.com/", "description": "Lokalna wypożyczalnia w Vila Olímpica del Poblenou w Barcelonie, oferująca wynajem skuterów, rolek, rowerów, wrotek, deskorolek i longboardów naprzeciwko plaży i obok Port Olímpic.", "image": ["https://rentalscooterbarcelona.com/images/rsb-rental-scooter-barcelona-shop-vila-olimpica.webp", "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-shop-interior-inline-skates-bike-vila-olimpica-1200.webp"], "logo": "https://rentalscooterbarcelona.com/images/rsb-barcelona-rental-logo-2-140-v1.webp", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "priceRange": "€4–€115", "paymentAccepted": "Karta kredytowa, karta debetowa, PayPal", "currenciesAccepted": "EUR", "address": {"@type": "PostalAddress", "streetAddress": "Carrer de Salvador Espriu, 63", "addressLocality": "Barcelona", "addressRegion": "Catalonia", "postalCode": "08005", "addressCountry": "ES"}, "geo": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}, "hasMap": "https://www.google.com/maps?cid=912877649802486634", "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "Place", "name": "Vila Olímpica del Poblenou"}, {"@type": "Place", "name": "Port Olímpic"}, {"@type": "Place", "name": "plaża Barceloneta"}], "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:30", "closes": "13:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "16:30", "closes": "20:00"}], "contactPoint": [{"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "obsługa klienta", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}, {"@type": "ContactPoint", "telephone": "+34 640 559 468", "email": "info@rentalscooterbarcelona.com", "contactType": "rezerwacja", "areaServed": "ES", "availableLanguage": ["en", "es", "ca", "fr", "it", "de", "nl", "pt", "sv", "pl"]}], "sameAs": ["https://www.facebook.com/rentalscooterbarcelona", "https://www.instagram.com/rentalscooterbarcelona/", "https://x.com/RSBscooterbarce", "https://es.pinterest.com/rsbscooter/", "https://www.tripadvisor.es/Attraction_Review-g187497-d7708978-Reviews-Rental_Scooter_Barcelona-Barcelona_Catalonia.html", "https://www.google.com/maps?cid=912877649802486634", "https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu%2C+63%2C+08005+Barcelona%2C+Espa%C3%B1a&amp;coordinate=41.3906488%2C2.1984312&amp;name=Rental+Scooter&amp;_provider=9902", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "brand": {"@id": "https://rentalscooterbarcelona.com/#organization"}} |
| pl | 1 | $.@graph[5] | {"@type": "FAQPage", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#faq", "mainEntity": [{"@type": "Question", "name": "Gdzie znajduje się RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "RSB Rental Scooter Barcelona znajduje się przy Carrer de Salvador Espriu, 63, 08005 Barcelona, w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic."}}, {"@type": "Question", "name": "Jak mogę skontaktować się z RSB Rental Scooter Barcelona?", "acceptedAnswer": {"@type": "Answer", "text": "Możesz zadzwonić lub wysłać WhatsApp na +34 640 559 468, napisać na info@rentalscooterbarcelona.com albo użyć formularza kontaktowego na tej stronie."}}, {"@type": "Question", "name": "Jakie są godziny otwarcia?", "acceptedAnswer": {"@type": "Answer", "text": "Otwarte codziennie: 10:30–13:30 i 16:30–20:00."}}, {"@type": "Question", "name": "Czy wypożyczalnia jest blisko plaży?", "acceptedAnswer": {"@type": "Answer", "text": "Tak. Wypożyczalnia znajduje się w Vila Olímpica, kilka minut spacerem od Port Olímpic i plaży Barceloneta."}}], "inLanguage": "pl"} |
| pl | 2 | $.@graph[0] | {"@type": "WebPage", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage", "dateModified": "2026-08-24"} |
| pl | 2 | $.@graph[1] | {"@type": "LocalBusiness", "@id": "https://rentalscooterbarcelona.com/#business", "sameAs": ["https://www.google.com/maps?cid=912877649802486634", "https://www.bing.com/maps/search?style=r&amp;q=RSB+Rental+Scooter+Barcelona%2C+Calle+de+Salvador+Espriu+63%2C+08005+Barcelona%2C+Catalu%C3%B1a%2C+Espa%C3%B1a&amp;ss=id.local_ypid%3A%22YND84466019C726C1%22"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": 226, "bestRating": 5, "worstRating": 1}, "review": [{"@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-1"}, {"@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-2"}, {"@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-3"}]} |
| pl | 2 | $.@graph[2] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Bardzo pomocna kobieta. Niska cena i świetna lokalizacja.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 2 | $.@graph[3] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Podczas wakacji wynajęliśmy rolki w Barcelonie. Mają również wrotki na czterech kółkach. Sklep znajduje się w Vila Olímpica, obok nadmorskiej promenady i blisko Barcelonety. Dobra cena i świetna obsługa, polecam w 100 procentach.\"", "publisher": {"@type": "Organization", "name": "Google"}} |
| pl | 2 | $.@graph[4] | {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Pracownik sklepu był bardzo miły i zabawny. Wrócimy w przyszłym roku i polecimy to miejsce wszystkim naszym znajomym i rodzinie. Bardzo dziękujemy za pomoc, rekomendacje i życzliwość! Dobre ceny i dobra obsługa.\"", "publisher": {"@type": "Organization", "name": "Google"}} |

## N. MATRIZ ARTICLE/BLOGPOSTING

No hay entidades Article/BlogPosting en estas páginas de servicio/contacto; no se exige un esquema editorial. Los elementos HTML article se cuentan por separado en U.

## O. MATRIZ GEO/COORDENADAS

| Idioma | Coordenadas extraídas | IDs de mapas | Sin coordenadas antiguas |
| --- | --- | --- | --- |
| en | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 70, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 319, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| es | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 73, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 317, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| fr | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 66, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 261, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| it | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 65, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 260, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| de | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 63, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 264, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| nl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 76, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 277, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pt | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 76, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 277, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| ca | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 65, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 260, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| sv | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 76, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 277, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |
| pl | [{"line": 16, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488;2.1984312\" name=\"geo.position\"/&gt;"}, {"line": 17, "pair": ["41.3906488", "2.1984312"], "context": "&lt;meta content=\"41.3906488, 2.1984312\" name=\"ICBM\"/&gt;"}, {"line": 70, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"line": 319, "pair": ["41.3906488", "2.1984312"], "context": "        \"https://maps.apple.com/place?place-id=IA5C7938C1925731A&amp;address=Carrer+de+Salvador+Espriu,+63,+08005+Barcelona,+España&amp;coordinate=41.3906488,2.1984312&amp;name=Rental+Scooter&amp;_provider=9902\","}, {"path": "$.@graph[4].geo", "pair": ["41.3906488", "2.1984312"], "context": {"@type": "GeoCoordinates", "latitude": 41.3906488, "longitude": 2.1984312}}] | {"Google CID": ["912877649802486634"], "Apple Place ID": ["IA5C7938C1925731A"], "Bing YPID": []} | True |

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
| en | [] | [] | [] | [] | [] |
| es | [] | [] | [] | [] | [] |
| fr | [] | [] | [] | [] | [] |
| it | [] | [] | [] | [] | [] |
| de | [] | [] | [] | [] | [] |
| nl | [] | [] | [] | [] | [] |
| pt | [] | [] | [] | [] | [] |
| ca | [] | [] | [] | [] | [] |
| sv | [] | [] | [] | [] | [] |
| pl | [] | [] | [] | [] | [] |

| Idioma | Ofertas servicio | Ofertas PRICES | Coinciden tarifas base |
| --- | --- | --- | --- |

El asiento infantil de BIKE (3 EUR) es un extra y no una séptima duración. CONTACT no contiene tarifas: no aplicable.

## R. MATRIZ POLÍTICAS

Textos completos extraídos por idioma: equipamiento, documentos, depósito, reservas, tallas y condiciones. Ausencia de una mención no equivale a contradicción. El alcance es coherencia del HTML con CANONICAL, no validación legal ni de disponibilidad.

| Idioma | Línea | Texto |
| --- | --- | --- |
| en | 682 | Visit RSB Rental Scooter Barcelona at Carrer de Salvador Espriu, 63, in Vila Olímpica del Poblenou, very close to Port Olímpic and Barceloneta Beach. Use this page to check the address, opening hours, phone, WhatsApp, email, map and the fastest way to contact the shop before your visit. |
| en | 771 | For scooters, bring the required driving licence. For inline skates, bikes, skateboards and longboards, a valid ID is normally enough. You can also review the main service pages before coming: |
| en | 826 | Use this page if you need the exact shop location, opening hours, map directions or the fastest way to contact RSB Rental Scooter Barcelona before you come. It is also useful if you want to confirm details before renting scooters, inline skates, bikes or boards. |
| en | 872 | You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page. |
| es | 682 | Visita RSB Rental Scooter Barcelona en Carrer de Salvador Espriu, 63, en Vila Olímpica del Poblenou, muy cerca del Port Olímpic y la Barceloneta. Usa esta página para consultar la dirección, horarios, teléfono, WhatsApp, email, mapa y la forma más rápida de contactar con la tienda antes de venir. |
| es | 704 | Planifica tu visita antes de venir a la tienda. Aquí puedes consultar la dirección exacta, horarios, teléfono, WhatsApp, email y mapa, y elegir la forma más rápida de contactar con RSB sobre alquiler de scooters, patines en línea o bicicletas. |
| es | 719 | Contacto rápido |
| es | 761 | La tienda está bien situada para visitantes alojados cerca de Vila Olímpica, Barceloneta, Port Olímpic, el Parc de la Ciutadella y la zona de playa. Esto hace que la recogida sea rápida si quieres un scooter, patines en línea, una bicicleta u otra opción de alquiler. |
| es | 765 | Punto útil de recogida para alquiler de scooters, bicicletas, patines en línea y tablas. |
| es | 771 | Para scooters, trae el permiso de conducir necesario. Para patines en línea, bicicletas, skateboards y longboards, normalmente basta con un documento de identidad válido. También puedes revisar las páginas principales antes de venir: |
| es | 783 | Envía un mensaje rápido antes de venir |
| es | 784 | Envía un mensaje rápido antes de venir si quieres preguntar por horarios, disponibilidad, cómo llegar o la mejor opción para tu alquiler. |
| es | 826 | Usa esta página si necesitas la ubicación exacta de la tienda, horarios, mapa, indicaciones o la forma más rápida de contactar con RSB Rental Scooter Barcelona antes de venir. También es útil para confirmar detalles antes de alquilar scooters, patines en línea, bicicletas o tablas. |
| fr | 624 | Rendez-vous chez RSB Rental Scooter Barcelona au Carrer de Salvador Espriu, 63, à Vila Olímpica del Poblenou, tout près du Port Olímpic et de la Barceloneta. Utilisez cette page pour consulter l’adresse, les horaires, le téléphone, WhatsApp, l’email, le plan et le moyen le plus rapide de contacter la boutique avant votre visite. |
| fr | 646 | Préparez votre visite avant de venir à la boutique. Vous pouvez consulter ici l’adresse exacte, les horaires, le téléphone, WhatsApp, l’email et le plan, puis choisir le moyen le plus rapide de contacter RSB pour la location de scooters, de rollers en ligne ou de vélos. |
| fr | 661 | Contact rapide |
| fr | 703 | La boutique est bien située pour les visiteurs logeant près de Vila Olímpica, Barceloneta, Port Olímpic, du parc de la Ciutadella et de la zone de plage. Le retrait est rapide, que vous souhaitiez un scooter, des rollers en ligne, un vélo ou une autre option de location. |
| fr | 713 | Pour les scooters, apportez le permis de conduire requis. Pour les rollers en ligne, vélos, skateboards et longboards, une pièce d’identité valide suffit généralement. Vous pouvez aussi consulter les pages principales avant de venir : |
| fr | 725 | Envoyez un message rapide avant votre visite |
| fr | 726 | Envoyez un message rapide avant de venir si vous souhaitez demander les horaires, les disponibilités, l’itinéraire ou la meilleure option de location. |
| fr | 769 | Utilisez cette page si vous avez besoin de l’adresse exacte de la boutique, des horaires, du plan, des directions ou du moyen le plus rapide de contacter RSB Rental Scooter Barcelona avant de venir. Elle est aussi utile pour confirmer des détails avant de louer des scooters, rollers en ligne, vélos ou planches. |
| fr | 770 | De nombreux visiteurs nous contactent ici avant de venir à la boutique, surtout lorsqu’ils veulent un itinéraire depuis la plage, le Port Olímpic ou le centre de Barcelone, ou lorsqu’ils ont besoin d’aide pour choisir la bonne location. |
| fr | 813 | Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page. |
| it | 629 | Visita RSB Rental Scooter Barcelona in Carrer de Salvador Espriu, 63, a Vila Olímpica del Poblenou, molto vicino al Port Olímpic e alla Barceloneta. Usa questa pagina per controllare indirizzo, orari, telefono, WhatsApp, email, mappa e il modo più rapido per contattare il negozio prima della visita. |
| it | 651 | Organizza la visita prima di venire in negozio. Qui puoi controllare l’indirizzo esatto, gli orari, telefono, WhatsApp, email e mappa, poi scegliere il modo più rapido per contattare RSB per noleggio scooter, pattini in linea o biciclette. |
| it | 666 | Contatto rapido |
| it | 708 | Il negozio è ben posizionato per chi soggiorna vicino a Vila Olímpica, Barceloneta, Port Olímpic, Parc de la Ciutadella e alla zona della spiaggia. Il ritiro è rapido sia per scooter, pattini in linea, bici o altre opzioni di noleggio. |
| it | 718 | Per gli scooter, porta la patente richiesta. Per pattini in linea, biciclette, skateboard e longboard, di solito basta un documento valido. Puoi anche consultare le pagine principali prima di venire: |
| it | 730 | Invia un messaggio rapido prima della visita |
| it | 731 | Invia un messaggio rapido prima di venire se vuoi chiedere orari, disponibilità, indicazioni o l’opzione migliore per il tuo noleggio. |
| it | 774 | Usa questa pagina se ti serve la posizione esatta del negozio, gli orari, la mappa, le indicazioni o il modo più rapido per contattare RSB Rental Scooter Barcelona prima di venire. È utile anche per confermare dettagli prima di noleggiare scooter, pattini in linea, bici o tavole. |
| it | 821 | Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina. |
| de | 716 | Für Scooter bring bitte den erforderlichen Führerschein mit. Für Inlineskates, Fahrräder, Skateboards und Longboards reicht normalerweise ein gültiger Ausweis. Du kannst dir vorab auch die wichtigsten Serviceseiten ansehen: |
| nl | 640 | Bezoek RSB Rental Scooter Barcelona aan Carrer de Salvador Espriu, 63, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta. Gebruik deze pagina voor het adres, de openingstijden, telefoon, WhatsApp, e-mail, de kaart en de snelste manier om vóór je bezoek contact met de winkel op te nemen. |
| nl | 728 | Wat je moet voorbereiden |
| nl | 729 | Voor scooters neem je het vereiste rijbewijs mee. Voor inline skates, fietsen, skateboards en longboards is meestal een geldig ID genoeg. Je kunt ook de belangrijkste servicepagina’s bekijken voordat je komt: |
| nl | 742 | Stuur voor je bezoek een snel bericht als je vragen hebt over openingstijden, beschikbaarheid, route of de beste huuroptie. |
| nl | 785 | Gebruik deze pagina als je de exacte locatie, openingstijden, kaart, route of snelste manier nodig hebt om vóór je bezoek contact met RSB Rental Scooter Barcelona op te nemen. Het is ook handig om details te bevestigen voordat je scooters, inline skates, fietsen of boards huurt. |
| nl | 843 | Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken. |
| pt | 646 | Visita a RSB Rental Scooter Barcelona em Carrer de Salvador Espriu, 63, em Vila Olímpica del Poblenou, muito perto do Port Olímpic e da Barceloneta. Usa esta página para consultar a morada, horários, telefone, WhatsApp, email, mapa e a forma mais rápida de contactar a loja antes da visita. |
| pt | 668 | Planeia a visita antes de vir à loja. Aqui pode consultar a morada exata, horários, telefone, WhatsApp, email e mapa, e escolher a forma mais rápida de contactar a RSB sobre aluguer de scooters, patins em linha ou bicicletas. |
| pt | 683 | Contacto rápido |
| pt | 689 | Pedidos por escrito |
| pt | 691 | Útil para pedidos especiais, grupos, aulas ou alugueres mais longos. |
| pt | 724 | Fácil acesso a partir da frente marítima e do centro da cidade |
| pt | 725 | A loja está bem situada para visitantes alojados perto de Vila Olímpica, Barceloneta, Port Olímpic, Parc de la Ciutadella e zona de praia. A recolha é rápida se quiseres uma scooter, patins em linha, uma bicicleta ou outra opção de aluguer. |
| pt | 735 | Para scooters, traz a carta de condução necessária. Para patins em linha, bicicletas, skateboards e longboards, normalmente basta um documento de identificação válido. Também pode consultar as principais páginas antes de vir: |
| pt | 747 | Envia uma mensagem rápida antes da visita |
| pt | 748 | Envia uma mensagem rápida antes de vir se quiseres perguntar sobre horários, disponibilidade, direções ou a melhor opção para o teu aluguer. |
| pt | 791 | Usa esta página se precisares da localização exata da loja, horários, mapa, direções ou a forma mais rápida de contactar a RSB Rental Scooter Barcelona antes de vir. Também é útil para confirmar detalhes antes de alugar scooters, patins em linha, bicicletas ou pranchas. |
| ca | 629 | Visita RSB Rental Scooter Barcelona al Carrer de Salvador Espriu, 63, a Vila Olímpica del Poblenou, molt a prop del Port Olímpic i la Barceloneta. Fes servir aquesta pàgina per consultar l’adreça, horaris, telèfon, WhatsApp, email, mapa i la forma més ràpida de contactar amb la botiga abans de venir. |
| ca | 651 | Planifica la visita abans de venir a la botiga. Aquí pots consultar l’adreça exacta, horaris, telèfon, WhatsApp, email i mapa, i escollir la manera més ràpida de contactar amb RSB sobre lloguer de scooters, patins en línia o bicicletes. |
| ca | 666 | Contacte ràpid |
| ca | 708 | La botiga està ben situada per a visitants allotjats a prop de Vila Olímpica, Barceloneta, Port Olímpic, Parc de la Ciutadella i la zona de platja. La recollida és ràpida si vols un scooter, patins en línia, una bicicleta o una altra opció de lloguer. |
| ca | 712 | Punt de recollida útil per a lloguer de scooters, bicicletes o classes de patinatge en línia. |
| ca | 718 | Per a scooters, porta el permís de conduir necessari. Per a patins en línia, bicicletes, skateboards i longboards, normalment n’hi ha prou amb un document d’identitat vàlid. També pots consultar les pàgines principals abans de venir: |
| ca | 730 | Envia un missatge ràpid abans de venir |
| ca | 731 | Envia un missatge ràpid abans de venir si vols preguntar per horaris, disponibilitat, com arribar-hi o la millor opció per al teu lloguer. |
| ca | 774 | Fes servir aquesta pàgina si necessites la ubicació exacta de la botiga, horaris, mapa, indicacions o la forma més ràpida de contactar amb RSB Rental Scooter Barcelona abans de venir. També és útil per confirmar detalls abans de llogar scooters, patins en línia, bicicletes o taules. |
| sv | 642 | Besök RSB Rental Scooter Barcelona på Carrer de Salvador Espriu, 63, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic. På den här sidan hittar du adress, öppettider, telefon, WhatsApp, e-post, karta och snabbaste sättet att kontakta butiken före ditt besök. |
| sv | 663 | Butikens adress, kontakt och öppettider |
| sv | 664 | Planera ditt besök innan du kommer till butiken. Här kan du kontrollera exakt adress, öppettider, telefon, WhatsApp, e-post och karta och välja snabbaste sättet att kontakta RSB om hyra scooter, inlines eller cykel. |
| sv | 693 | Hyra samma dag möjligt beroende på tillgänglighet och tid. |
| sv | 731 | För scootrar, ta med det körkort som krävs. För inlines, cyklar, skateboards och longboards räcker normalt giltig ID-handling. Du kan också läsa de viktigaste servicesidorna innan du kommer: |
| sv | 744 | Skicka ett snabbt meddelande före ditt besök om du vill fråga om öppettider, tillgänglighet, vägbeskrivning eller bästa hyralternativ. |
| sv | 787 | Använd den här sidan om du behöver exakt butiksplats, öppettider, karta, vägbeskrivning eller snabbaste sättet att kontakta RSB Rental Scooter Barcelona innan du kommer. Den är också användbar om du vill bekräfta detaljer innan du hyr scootrar, inlines, cyklar eller boards. |
| sv | 843 | Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan. |
| sv | 846 | Vilka är öppettiderna? |
| pl | 771 | W przypadku skuterów zabierz wymagane prawo jazdy. W przypadku rolek, rowerów, deskorolek i longboardów zwykle wystarczy ważny dokument tożsamości. Przed przyjazdem możesz też sprawdzić główne strony usług: |

## S. MATRIZ FAQ VISIBLE ↔ SCHEMA

| Idioma | N.º | Visible completo | Schema completo | Pregunta coincide | Respuesta coincide |
| --- | --- | --- | --- | --- | --- |
| en | 1 | {"line": 866, "question": "Where is RSB Rental Scooter Barcelona located?", "answer": "RSB Rental Scooter Barcelona is at Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Where is RSB Rental Scooter Barcelona located?", "answer": "RSB Rental Scooter Barcelona is at Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach.", "answer_raw": "RSB Rental Scooter Barcelona is at Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, near Port Olímpic and Barceloneta Beach."} | True | True |
| en | 2 | {"line": 870, "question": "How can I contact RSB Rental Scooter Barcelona?", "answer": "You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "How can I contact RSB Rental Scooter Barcelona?", "answer": "You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page.", "answer_raw": "You can call or send WhatsApp to +34 640 559 468, email info@rentalscooterbarcelona.com, or use the contact form on this page."} | True | True |
| en | 3 | {"line": 874, "question": "What are the opening hours?", "answer": "Open every day: 10:30–13:30 and 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "What are the opening hours?", "answer": "Open every day: 10:30–13:30 and 16:30–20:00.", "answer_raw": "Open every day: 10:30–13:30 and 16:30–20:00."} | True | True |
| en | 4 | {"line": 878, "question": "Is the shop near the beach?", "answer": "Yes. The shop is in Vila Olímpica, a short walk from Port Olímpic and Barceloneta Beach.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Is the shop near the beach?", "answer": "Yes. The shop is in Vila Olímpica, a short walk from Port Olímpic and Barceloneta Beach.", "answer_raw": "Yes. The shop is in Vila Olímpica, a short walk from Port Olímpic and Barceloneta Beach."} | True | True |
| es | 1 | {"line": 865, "question": "¿Dónde está RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona está en Carrer de Salvador Espriu, 63, 08005 Barcelona, en Vila Olímpica del Poblenou, cerca del Port Olímpic y la Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "¿Dónde está RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona está en Carrer de Salvador Espriu, 63, 08005 Barcelona, en Vila Olímpica del Poblenou, cerca del Port Olímpic y la Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona está en Carrer de Salvador Espriu, 63, 08005 Barcelona, en Vila Olímpica del Poblenou, cerca del Port Olímpic y la Barceloneta."} | True | True |
| es | 2 | {"line": 869, "question": "¿Cómo puedo contactar con RSB Rental Scooter Barcelona?", "answer": "Puedes llamar o enviar WhatsApp al +34 640 559 468, escribir a info@rentalscooterbarcelona.com o usar el formulario de esta página.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "¿Cómo puedo contactar con RSB Rental Scooter Barcelona?", "answer": "Puedes llamar o enviar WhatsApp al +34 640 559 468, escribir a info@rentalscooterbarcelona.com o usar el formulario de esta página.", "answer_raw": "Puedes llamar o enviar WhatsApp al +34 640 559 468, escribir a info@rentalscooterbarcelona.com o usar el formulario de esta página."} | True | True |
| es | 3 | {"line": 873, "question": "¿Cuál es el horario?", "answer": "Abierto todos los días: 10:30–13:30 y 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "¿Cuál es el horario?", "answer": "Abierto todos los días: 10:30–13:30 y 16:30–20:00.", "answer_raw": "Abierto todos los días: 10:30–13:30 y 16:30–20:00."} | True | True |
| es | 4 | {"line": 877, "question": "¿La tienda está cerca de la playa?", "answer": "Sí. La tienda está en Vila Olímpica, frente a la playa y junto a Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "¿La tienda está cerca de la playa?", "answer": "Sí. La tienda está en Vila Olímpica, frente a la playa y junto a Port Olímpic.", "answer_raw": "Sí. La tienda está en Vila Olímpica, frente a la playa y junto a Port Olímpic."} | True | True |
| fr | 1 | {"line": 807, "question": "Où se trouve RSB Rental Scooter Barcelona ?", "answer": "RSB Rental Scooter Barcelona se trouve au Carrer de Salvador Espriu, 63, 08005 Barcelone, à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Où se trouve RSB Rental Scooter Barcelona ?", "answer": "RSB Rental Scooter Barcelona se trouve au Carrer de Salvador Espriu, 63, 08005 Barcelone, à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona se trouve au Carrer de Salvador Espriu, 63, 08005 Barcelone, à Vila Olímpica del Poblenou, près du Port Olímpic et de la Barceloneta."} | True | True |
| fr | 2 | {"line": 811, "question": "Comment contacter RSB Rental Scooter Barcelona ?", "answer": "Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Comment contacter RSB Rental Scooter Barcelona ?", "answer": "Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page.", "answer_raw": "Vous pouvez appeler ou envoyer un WhatsApp au +34 640 559 468, écrire à info@rentalscooterbarcelona.com ou utiliser le formulaire de contact de cette page."} | True | True |
| fr | 3 | {"line": 815, "question": "Quels sont les horaires ?", "answer": "Ouvert tous les jours : 10:30–13:30 et 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Quels sont les horaires ?", "answer": "Ouvert tous les jours : 10:30–13:30 et 16:30–20:00.", "answer_raw": "Ouvert tous les jours : 10:30–13:30 et 16:30–20:00."} | True | True |
| fr | 4 | {"line": 819, "question": "La boutique est-elle près de la plage ?", "answer": "Oui. La boutique se trouve à Vila Olímpica, face à la plage et à côté du Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "La boutique est-elle près de la plage ?", "answer": "Oui. La boutique se trouve à Vila Olímpica, face à la plage et à côté du Port Olímpic.", "answer_raw": "Oui. La boutique se trouve à Vila Olímpica, face à la plage et à côté du Port Olímpic."} | True | True |
| it | 1 | {"line": 815, "question": "Dove si trova RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona si trova in Carrer de Salvador Espriu, 63, 08005 Barcellona, a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Dove si trova RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona si trova in Carrer de Salvador Espriu, 63, 08005 Barcellona, a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona si trova in Carrer de Salvador Espriu, 63, 08005 Barcellona, a Vila Olímpica del Poblenou, vicino al Port Olímpic e alla Barceloneta."} | True | True |
| it | 2 | {"line": 819, "question": "Come posso contattare RSB Rental Scooter Barcelona?", "answer": "Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Come posso contattare RSB Rental Scooter Barcelona?", "answer": "Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina.", "answer_raw": "Puoi chiamare o inviare WhatsApp al +34 640 559 468, scrivere a info@rentalscooterbarcelona.com o usare il modulo di contatto in questa pagina."} | True | True |
| it | 3 | {"line": 823, "question": "Quali sono gli orari?", "answer": "Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Quali sono gli orari?", "answer": "Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00.", "answer_raw": "Aperto tutti i giorni: 10:30–13:30 e 16:30–20:00."} | True | True |
| it | 4 | {"line": 827, "question": "Il negozio è vicino alla spiaggia?", "answer": "Sì. Il negozio è a Vila Olímpica, di fronte alla spiaggia e accanto al Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Il negozio è vicino alla spiaggia?", "answer": "Sì. Il negozio è a Vila Olímpica, di fronte alla spiaggia e accanto al Port Olímpic.", "answer_raw": "Sì. Il negozio è a Vila Olímpica, di fronte alla spiaggia e accanto al Port Olímpic."} | True | True |
| de | 1 | {"line": 824, "question": "Wo befindet sich RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona befindet sich in der Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Wo befindet sich RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona befindet sich in der Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona befindet sich in der Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, nahe Port Olímpic und Barceloneta."} | True | True |
| de | 2 | {"line": 828, "question": "Wie kann ich RSB Rental Scooter Barcelona kontaktieren?", "answer": "Du kannst anrufen oder eine WhatsApp-Nachricht an +34 640 559 468 senden, eine E-Mail an info@rentalscooterbarcelona.com schreiben oder das Kontaktformular auf dieser Seite nutzen.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Wie kann ich RSB Rental Scooter Barcelona kontaktieren?", "answer": "Du kannst anrufen oder eine WhatsApp-Nachricht an +34 640 559 468 senden, eine E-Mail an info@rentalscooterbarcelona.com schreiben oder das Kontaktformular auf dieser Seite nutzen.", "answer_raw": "Du kannst anrufen oder eine WhatsApp-Nachricht an +34 640 559 468 senden, eine E-Mail an info@rentalscooterbarcelona.com schreiben oder das Kontaktformular auf dieser Seite nutzen."} | True | True |
| de | 3 | {"line": 832, "question": "Wie sind die Öffnungszeiten?", "answer": "Täglich geöffnet: 10:30–13:30 und 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Wie sind die Öffnungszeiten?", "answer": "Täglich geöffnet: 10:30–13:30 und 16:30–20:00.", "answer_raw": "Täglich geöffnet: 10:30–13:30 und 16:30–20:00."} | True | True |
| de | 4 | {"line": 836, "question": "Liegt die Station nahe am Strand?", "answer": "Ja. Die Station liegt in Vila Olímpica, nur wenige Gehminuten von Port Olímpic und Barceloneta entfernt.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Liegt die Station nahe am Strand?", "answer": "Ja. Die Station liegt in Vila Olímpica, nur wenige Gehminuten von Port Olímpic und Barceloneta entfernt.", "answer_raw": "Ja. Die Station liegt in Vila Olímpica, nur wenige Gehminuten von Port Olímpic und Barceloneta entfernt."} | True | True |
| nl | 1 | {"line": 837, "question": "Waar is RSB Rental Scooter Barcelona gevestigd?", "answer": "RSB Rental Scooter Barcelona is gevestigd aan Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Waar is RSB Rental Scooter Barcelona gevestigd?", "answer": "RSB Rental Scooter Barcelona is gevestigd aan Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona is gevestigd aan Carrer de Salvador Espriu, 63, 08005 Barcelona, in Vila Olímpica del Poblenou, vlak bij Port Olímpic en Barceloneta."} | True | True |
| nl | 2 | {"line": 841, "question": "Hoe kan ik contact opnemen met RSB Rental Scooter Barcelona?", "answer": "Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Hoe kan ik contact opnemen met RSB Rental Scooter Barcelona?", "answer": "Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken.", "answer_raw": "Je kunt bellen of WhatsApp sturen naar +34 640 559 468, mailen naar info@rentalscooterbarcelona.com of het contactformulier op deze pagina gebruiken."} | True | True |
| nl | 3 | {"line": 845, "question": "Wat zijn de openingstijden?", "answer": "Elke dag geopend: 10:30–13:30 en 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Wat zijn de openingstijden?", "answer": "Elke dag geopend: 10:30–13:30 en 16:30–20:00.", "answer_raw": "Elke dag geopend: 10:30–13:30 en 16:30–20:00."} | True | True |
| nl | 4 | {"line": 849, "question": "Is de winkel dicht bij het strand?", "answer": "Ja. De winkel ligt in Vila Olímpica, tegenover het strand en naast Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Is de winkel dicht bij het strand?", "answer": "Ja. De winkel ligt in Vila Olímpica, tegenover het strand en naast Port Olímpic.", "answer_raw": "Ja. De winkel ligt in Vila Olímpica, tegenover het strand en naast Port Olímpic."} | True | True |
| pt | 1 | {"line": 846, "question": "Onde fica a RSB Rental Scooter Barcelona?", "answer": "A RSB Rental Scooter Barcelona fica em Carrer de Salvador Espriu, 63, 08005 Barcelona, em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Onde fica a RSB Rental Scooter Barcelona?", "answer": "A RSB Rental Scooter Barcelona fica em Carrer de Salvador Espriu, 63, 08005 Barcelona, em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta.", "answer_raw": "A RSB Rental Scooter Barcelona fica em Carrer de Salvador Espriu, 63, 08005 Barcelona, em Vila Olímpica del Poblenou, perto do Port Olímpic e da Barceloneta."} | True | True |
| pt | 2 | {"line": 850, "question": "Como posso contactar a RSB Rental Scooter Barcelona?", "answer": "Pode ligar ou enviar WhatsApp para +34 640 559 468, escrever para info@rentalscooterbarcelona.com ou usar o formulário desta página.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Como posso contactar a RSB Rental Scooter Barcelona?", "answer": "Pode ligar ou enviar WhatsApp para +34 640 559 468, escrever para info@rentalscooterbarcelona.com ou usar o formulário desta página.", "answer_raw": "Pode ligar ou enviar WhatsApp para +34 640 559 468, escrever para info@rentalscooterbarcelona.com ou usar o formulário desta página."} | True | True |
| pt | 3 | {"line": 854, "question": "Quais são os horários?", "answer": "Aberto todos os dias: 10:30–13:30 e 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Quais são os horários?", "answer": "Aberto todos os dias: 10:30–13:30 e 16:30–20:00.", "answer_raw": "Aberto todos os dias: 10:30–13:30 e 16:30–20:00."} | True | True |
| pt | 4 | {"line": 858, "question": "A loja fica perto da praia?", "answer": "Sim. A loja fica em Vila Olímpica, a poucos minutos a pé do Port Olímpic e da Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "A loja fica perto da praia?", "answer": "Sim. A loja fica em Vila Olímpica, a poucos minutos a pé do Port Olímpic e da Barceloneta.", "answer_raw": "Sim. A loja fica em Vila Olímpica, a poucos minutos a pé do Port Olímpic e da Barceloneta."} | True | True |
| ca | 1 | {"line": 827, "question": "On és RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona és al Carrer de Salvador Espriu, 63, 08005 Barcelona, a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "On és RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona és al Carrer de Salvador Espriu, 63, 08005 Barcelona, a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta.", "answer_raw": "RSB Rental Scooter Barcelona és al Carrer de Salvador Espriu, 63, 08005 Barcelona, a Vila Olímpica del Poblenou, a prop del Port Olímpic i la Barceloneta."} | True | True |
| ca | 2 | {"line": 831, "question": "Com puc contactar amb RSB Rental Scooter Barcelona?", "answer": "Pots trucar o enviar WhatsApp al +34 640 559 468, escriure a info@rentalscooterbarcelona.com o fer servir el formulari d’aquesta pàgina.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Com puc contactar amb RSB Rental Scooter Barcelona?", "answer": "Pots trucar o enviar WhatsApp al +34 640 559 468, escriure a info@rentalscooterbarcelona.com o fer servir el formulari d’aquesta pàgina.", "answer_raw": "Pots trucar o enviar WhatsApp al +34 640 559 468, escriure a info@rentalscooterbarcelona.com o fer servir el formulari d’aquesta pàgina."} | True | True |
| ca | 3 | {"line": 835, "question": "Quin és l’horari?", "answer": "Obert cada dia: 10:30–13:30 i 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Quin és l’horari?", "answer": "Obert cada dia: 10:30–13:30 i 16:30–20:00.", "answer_raw": "Obert cada dia: 10:30–13:30 i 16:30–20:00."} | True | True |
| ca | 4 | {"line": 839, "question": "La botiga és a prop de la platja?", "answer": "Sí. La botiga és a la Vila Olímpica, davant de la platja i al costat del Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "La botiga és a prop de la platja?", "answer": "Sí. La botiga és a la Vila Olímpica, davant de la platja i al costat del Port Olímpic.", "answer_raw": "Sí. La botiga és a la Vila Olímpica, davant de la platja i al costat del Port Olímpic."} | True | True |
| sv | 1 | {"line": 837, "question": "Var ligger RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona ligger på Carrer de Salvador Espriu, 63, 08005 Barcelona, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Var ligger RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona ligger på Carrer de Salvador Espriu, 63, 08005 Barcelona, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic.", "answer_raw": "RSB Rental Scooter Barcelona ligger på Carrer de Salvador Espriu, 63, 08005 Barcelona, i Vila Olímpica del Poblenou, mitt emot stranden och intill Port Olímpic."} | True | True |
| sv | 2 | {"line": 841, "question": "Hur kan jag kontakta RSB Rental Scooter Barcelona?", "answer": "Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Hur kan jag kontakta RSB Rental Scooter Barcelona?", "answer": "Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan.", "answer_raw": "Du kan ringa eller skicka WhatsApp till +34 640 559 468, mejla info@rentalscooterbarcelona.com eller använda kontaktformuläret på den här sidan."} | True | True |
| sv | 3 | {"line": 845, "question": "Vilka är öppettiderna?", "answer": "Öppet varje dag: 10:30–13:30 och 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Vilka är öppettiderna?", "answer": "Öppet varje dag: 10:30–13:30 och 16:30–20:00.", "answer_raw": "Öppet varje dag: 10:30–13:30 och 16:30–20:00."} | True | True |
| sv | 4 | {"line": 849, "question": "Ligger butiken nära stranden?", "answer": "Ja. Butiken ligger i Vila Olímpica, en kort promenad från Port Olímpic och Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Ligger butiken nära stranden?", "answer": "Ja. Butiken ligger i Vila Olímpica, en kort promenad från Port Olímpic och Barceloneta.", "answer_raw": "Ja. Butiken ligger i Vila Olímpica, en kort promenad från Port Olímpic och Barceloneta."} | True | True |
| pl | 1 | {"line": 877, "question": "Gdzie znajduje się RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona znajduje się przy Carrer de Salvador Espriu, 63, 08005 Barcelona, w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic.", "links": []} | {"path": "$.@graph[5].mainEntity[0]", "question": "Gdzie znajduje się RSB Rental Scooter Barcelona?", "answer": "RSB Rental Scooter Barcelona znajduje się przy Carrer de Salvador Espriu, 63, 08005 Barcelona, w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic.", "answer_raw": "RSB Rental Scooter Barcelona znajduje się przy Carrer de Salvador Espriu, 63, 08005 Barcelona, w Vila Olímpica del Poblenou, naprzeciwko plaży i obok Port Olímpic."} | True | True |
| pl | 2 | {"line": 881, "question": "Jak mogę skontaktować się z RSB Rental Scooter Barcelona?", "answer": "Możesz zadzwonić lub wysłać WhatsApp na +34 640 559 468, napisać na info@rentalscooterbarcelona.com albo użyć formularza kontaktowego na tej stronie.", "links": []} | {"path": "$.@graph[5].mainEntity[1]", "question": "Jak mogę skontaktować się z RSB Rental Scooter Barcelona?", "answer": "Możesz zadzwonić lub wysłać WhatsApp na +34 640 559 468, napisać na info@rentalscooterbarcelona.com albo użyć formularza kontaktowego na tej stronie.", "answer_raw": "Możesz zadzwonić lub wysłać WhatsApp na +34 640 559 468, napisać na info@rentalscooterbarcelona.com albo użyć formularza kontaktowego na tej stronie."} | True | True |
| pl | 3 | {"line": 885, "question": "Jakie są godziny otwarcia?", "answer": "Otwarte codziennie: 10:30–13:30 i 16:30–20:00.", "links": []} | {"path": "$.@graph[5].mainEntity[2]", "question": "Jakie są godziny otwarcia?", "answer": "Otwarte codziennie: 10:30–13:30 i 16:30–20:00.", "answer_raw": "Otwarte codziennie: 10:30–13:30 i 16:30–20:00."} | True | True |
| pl | 4 | {"line": 889, "question": "Czy wypożyczalnia jest blisko plaży?", "answer": "Tak. Wypożyczalnia znajduje się w Vila Olímpica, kilka minut spacerem od Port Olímpic i plaży Barceloneta.", "links": []} | {"path": "$.@graph[5].mainEntity[3]", "question": "Czy wypożyczalnia jest blisko plaży?", "answer": "Tak. Wypożyczalnia znajduje się w Vila Olímpica, kilka minut spacerem od Port Olímpic i plaży Barceloneta.", "answer_raw": "Tak. Wypożyczalnia znajduje się w Vila Olímpica, kilka minut spacerem od Port Olímpic i plaży Barceloneta."} | True | True |

CONTACT usa article/h3/p dentro de #faq; se ha verificado con ese extractor, no con la clase faq-item de las páginas de servicio.

## T. MATRIZ RATING/REVIEWS

Rating canónico 4.6, 226 reseñas, escala 1–5. Los testimonios individuales pueden tener 5 estrellas sin contradecir la media. Se verifica presencia y correspondencia; autenticidad externa no verificada.

| Idioma | Comparación completa |
| --- | --- |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Best Rollers 🛼 rental spot , You can go alongside Barceloneta. Amazing time and experience. The owner is also a wonderful guy. I recommend a lot\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2026-07-30"}, "line": null, "visible_card": null, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Really helpfull women. Cheap price and great location\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2019-02-15"}, "line": null, "visible_card": null, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| en | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Crystal S"}, "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"What a friendly and patient one person operated business. Several people were approached for rental and I was the only non-Spanish and non-Catalan speaking person. We were not in a hurry, so I motioned to take others. But no, he was patient, explained how to operate equipment and walked us to an area to try it out before we went off on our own. I thought the price was reasonable too. Would definitely visit again and suggest that others visit. Oh the only thing it did not come with a lock, which was fine for us. But no way I would leave unattended on beach.\"", "publisher": {"@type": "Organization", "name": "Google"}, "datePublished": "2019-09-28"}, "line": null, "visible_card": null, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Pequeña sorpresa junto a la playa de Barcelona. Mi experiencia fué genial. Precios razonables y a un tiro de piedra del paseo marítimo. Lo mejor de todo, la atención de la propietaria.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 849, "visible_card": {"line": 849, "text": "★★★★★ “Pequeña sorpresa junto a la playa de Barcelona. Mi experiencia fué genial. Precios razonables y a un tiro de piedra del paseo marítimo. Lo mejor de todo, la atención de la propietaria.” Marc Bonet Fernández · Reseña de Google · 2025-07-01", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Experiencia increíble, buena ubicación y personal súper amable. 100% recomendable. Mil gracias Natalia por tu disponibilidad, tu ayuda y tus consejos!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 850, "visible_card": {"line": 850, "text": "★★★★★ “Experiencia increíble, buena ubicación y personal súper amable. 100% recomendable. Mil gracias Natalia por tu disponibilidad, tu ayuda y tus consejos!” Rita Conti · Reseña de Google · 2022-08-30", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| es | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/es/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Lo recomiendo ampliamente! Muy buena experiencia, muy amables y muy buen coste. La ubicación ideal.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 851, "visible_card": {"line": 851, "text": "★★★★★ “Lo recomiendo ampliamente! Muy buena experiencia, muy amables y muy buen coste. La ubicación ideal.” Armando Vidales · Reseña de Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Une petite surprise près de la plage de Barcelone. Mon expérience a été géniale. Des prix raisonnables et à deux pas de la promenade maritime. Le meilleur de tout, l’accueil de la propriétaire.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 791, "visible_card": {"line": 791, "text": "★★★★★ “Une petite surprise près de la plage de Barcelone. Mon expérience a été géniale. Des prix raisonnables et à deux pas de la promenade maritime. Le meilleur de tout, l’accueil de la propriétaire.” Marc Bonet Fernández · Avis Google · 2025-07-01", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Expérience incroyable, bon emplacement et personnel très aimable. Recommandé à 100 %. Mille mercis à Natalia pour ta disponibilité, ton aide et tes conseils !\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 792, "visible_card": {"line": 792, "text": "★★★★★ “Expérience incroyable, bon emplacement et personnel très aimable. Recommandé à 100 %. Mille mercis à Natalia pour ta disponibilité, ton aide et tes conseils !” Rita Conti · Avis Google · 2022-08-30", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| fr | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/fr/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Je le recommande vivement ! Très bonne expérience, personnel très aimable et très bon prix. L’emplacement est idéal.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 793, "visible_card": {"line": 793, "text": "★★★★★ “Je le recommande vivement ! Très bonne expérience, personnel très aimable et très bon prix. L’emplacement est idéal.” Armando Vidales · Avis Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Marc Bonet Fernández"}, "datePublished": "2025-07-01", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Una piccola sorpresa vicino alla spiaggia di Barcellona. La mia esperienza è stata fantastica. Prezzi ragionevoli e a due passi dal lungomare. La cosa migliore è stata l’attenzione della proprietaria.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 799, "visible_card": {"line": 799, "text": "★★★★★ “Una piccola sorpresa vicino alla spiaggia di Barcellona. La mia esperienza è stata fantastica. Prezzi ragionevoli e a due passi dal lungomare. La cosa migliore è stata l’attenzione della proprietaria.” Marc Bonet Fernández · Recensione Google · 2025-07-01", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Rita Conti"}, "datePublished": "2022-08-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Esperienza incredibile, buona posizione e personale super gentile. Consigliato al 100%. Grazie mille Natalia per la tua disponibilità, il tuo aiuto e i tuoi consigli!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 800, "visible_card": {"line": 800, "text": "★★★★★ “Esperienza incredibile, buona posizione e personale super gentile. Consigliato al 100%. Grazie mille Natalia per la tua disponibilità, il tuo aiuto e i tuoi consigli!” Rita Conti · Recensione Google · 2022-08-30", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| it | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/it/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Armando Vidales"}, "datePublished": "2021-04-12", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Lo consiglio vivamente! Ottima esperienza, persone molto gentili e ottimo prezzo. La posizione è ideale.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 801, "visible_card": {"line": 801, "text": "★★★★★ “Lo consiglio vivamente! Ottima esperienza, persone molto gentili e ottimo prezzo. La posizione è ideale.” Armando Vidales · Recensione Google · 2021-04-12", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "maria yo"}, "datePublished": "2021-08-09", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Super nette Leute! Perfekte Standort um von dort direkt zum Strand Skaten, Radfahrern oder sonst...dann die Küste entlang weiter zu entdecken... […] Ich kann es nur empfehlen. Danke euch!“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 793, "visible_card": {"line": 793, "text": "★★★★★ „Super nette Leute! Perfekte Standort um von dort direkt zum Strand Skaten, Radfahrern oder sonst...dann die Küste entlang weiter zu entdecken... […] Ich kann es nur empfehlen. Danke euch!“ maria yo Google-Bewertung · 2021-08-09", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Sehr hilfsbereite Frau. Günstiger Preis und tolle Lage.“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 799, "visible_card": {"line": 799, "text": "★★★★★ „Sehr hilfsbereite Frau. Günstiger Preis und tolle Lage.“ James Liddell Google-Bewertung · 2019-02-15", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| de | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/de/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"„Wir sind mit meinem Sohn zum Port Olímpic gekommen, um zu skaten, und die Ausrüstung war großartig. Auch der Service war sehr freundlich, vielen Dank!!“\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 805, "visible_card": {"line": 805, "text": "★★★★★ „Wir sind mit meinem Sohn zum Port Olímpic gekommen, um zu skaten, und die Ausrüstung war großartig. Auch der Service war sehr freundlich, vielen Dank!!“ Luz Google-Bewertung · 2026-03-08", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "datePublished": "2026-07-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"De beste verhuurplek voor rollers 🛼. Je kunt langs Barceloneta gaan. Geweldige tijd en ervaring. De eigenaar is ook een geweldige man. Ik raad het ten zeerste aan.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 806, "visible_card": {"line": 806, "text": "★★★★★ “De beste verhuurplek voor rollers 🛼. Je kunt langs Barceloneta gaan. Geweldige tijd en ervaring. De eigenaar is ook een geweldige man. Ik raad het ten zeerste aan.” Yassine Souri Google-review · 2026-07-30", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "sofie van santen"}, "datePublished": "2024-07-29", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Hele aardige eigenaresse!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 812, "visible_card": {"line": 812, "text": "★★★★★ “Hele aardige eigenaresse!” sofie van santen Google-review · 2024-07-29", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| nl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/nl/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"We kwamen met mijn zoon naar Port Olímpic om te skaten en de uitrusting was geweldig. De service was ook erg vriendelijk, heel erg bedankt!!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 818, "visible_card": {"line": 818, "text": "★★★★★ “We kwamen met mijn zoon naar Port Olímpic om te skaten en de uitrusting was geweldig. De service was ook erg vriendelijk, heel erg bedankt!!” Luz Google-review · 2026-03-08", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Yassine Souri"}, "datePublished": "2026-07-30", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"O melhor local para alugar rollers 🛼. Pode ir ao longo da Barceloneta. Um tempo e uma experiência incríveis. O proprietário também é uma pessoa maravilhosa. Recomendo muito.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 815, "visible_card": {"line": 815, "text": "★★★★★ “O melhor local para alugar rollers 🛼. Pode ir ao longo da Barceloneta. Um tempo e uma experiência incríveis. O proprietário também é uma pessoa maravilhosa. Recomendo muito.” Yassine Souri Avaliação Google · 2026-07-30", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "João Junior"}, "datePublished": "2021-04-21", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 821, "visible_card": {"line": 821, "text": "★★★★★ “[…] eu e um grupo de amigos pudemos desfrutar de um tour por Barcelona sem depender do transporte público, alugamos excelentes bicicletas e por um bom preço!!! Agradeço a responsável da loja pelas orientações e um mini roteiro de lugares que nos proporcionou, suas indicações nos foram muito úteis durante nossa jornada.🚲🚲” João Junior Avaliação Google · 2021-04-21", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pt | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pt/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Luz"}, "datePublished": "2026-03-08", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Viemos ao Port Olímpic patinar com o meu filho e o equipamento foi ótimo. O atendimento também foi muito agradável, muito obrigado!!\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 827, "visible_card": {"line": 827, "text": "★★★★★ “Viemos ao Port Olímpic patinar com o meu filho e o equipamento foi ótimo. O atendimento também foi muito agradável, muito obrigado!!” Luz Avaliação Google · 2026-03-08", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Dona molt servicial. Preu barat i ubicació fantàstica.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 798, "visible_card": {"line": 798, "text": "★★★★★ “Dona molt servicial. Preu barat i ubicació fantàstica.” James Liddell Ressenya de Google · 2019-02-15", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Vam llogar patins en línia a Barcelona durant les vacances. També tenen patins de quatre rodes. La botiga és a la Vila Olímpica, al costat del passeig marítim i prop de la Barceloneta. Bon preu i una atenció genial, ho recomano al 100%.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 804, "visible_card": {"line": 804, "text": "★★★★★ “Vam llogar patins en línia a Barcelona durant les vacances. També tenen patins de quatre rodes. La botiga és a la Vila Olímpica, al costat del passeig marítim i prop de la Barceloneta. Bon preu i una atenció genial, ho recomano al 100%.” Sonia Ressenya de Google · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| ca | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/cat/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"L’assistent de la botiga era molt agradable i divertit. Tornarem l’any que ve i ho recomanarem a tots els nostres amics i familiars. Moltes gràcies per l’ajuda, per les recomanacions i per l’amabilitat! Bons preus i bona atenció.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 810, "visible_card": {"line": 810, "text": "★★★★★ “L’assistent de la botiga era molt agradable i divertit. Tornarem l’any que ve i ho recomanarem a tots els nostres amics i familiars. Moltes gràcies per l’ajuda, per les recomanacions i per l’amabilitat! Bons preus i bona atenció.” Michel new technology Ressenya de Google · 2020-09-24", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Mycket hjälpsam kvinna. Lågt pris och fantastiskt läge.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 808, "visible_card": {"line": 808, "text": "★★★★★ “Mycket hjälpsam kvinna. Lågt pris och fantastiskt läge.” James Liddell Google-recension · 2019-02-15", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Vi hyrde inlines i Barcelona under semestern. De har även fyrhjuliga rullskridskor. Butiken ligger i Vila Olímpica, intill strandpromenaden och nära Barceloneta. Bra pris och fantastisk service, jag rekommenderar den till 100 procent.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 814, "visible_card": {"line": 814, "text": "★★★★★ “Vi hyrde inlines i Barcelona under semestern. De har även fyrhjuliga rullskridskor. Butiken ligger i Vila Olímpica, intill strandpromenaden och nära Barceloneta. Bra pris och fantastisk service, jag rekommenderar den till 100 procent.” Sonia Google-recension · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| sv | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/sv/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Butiksbiträdet var mycket trevligt och roligt. Vi kommer tillbaka nästa år och kommer att rekommendera stället till alla våra vänner och släktingar. Tack så mycket för hjälpen, rekommendationerna och det vänliga bemötandet! Bra priser och bra service.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 820, "visible_card": {"line": 820, "text": "★★★★★ “Butiksbiträdet var mycket trevligt och roligt. Vi kommer tillbaka nästa år och kommer att rekommendera stället till alla våra vänner och släktingar. Tack så mycket för hjälpen, rekommendationerna och det vänliga bemötandet! Bra priser och bra service.” Michel new technology Google-recension · 2020-09-24", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-1", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "James Liddell"}, "datePublished": "2019-02-15", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Bardzo pomocna kobieta. Niska cena i świetna lokalizacja.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 848, "visible_card": {"line": 848, "text": "★★★★★ “Bardzo pomocna kobieta. Niska cena i świetna lokalizacja.” James Liddell Opinia Google · 2019-02-15", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-2", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Sonia"}, "datePublished": "2026-05-20", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Podczas wakacji wynajęliśmy rolki w Barcelonie. Mają również wrotki na czterech kółkach. Sklep znajduje się w Vila Olímpica, obok nadmorskiej promenady i blisko Barcelonety. Dobra cena i świetna obsługa, polecam w 100 procentach.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 854, "visible_card": {"line": 854, "text": "★★★★★ “Podczas wakacji wynajęliśmy rolki w Barcelonie. Mają również wrotki na czterech kółkach. Sklep znajduje się w Vila Olímpica, obok nadmorskiej promenady i blisko Barcelonety. Dobra cena i świetna obsługa, polecam w 100 procentach.” Sonia Opinia Google · 2026-05-20", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |
| pl | {"schema": {"@type": "Review", "@id": "https://rentalscooterbarcelona.com/pl/location-contact/#google-review-3", "itemReviewed": {"@id": "https://rentalscooterbarcelona.com/#business"}, "author": {"@type": "Person", "name": "Michel new technology"}, "datePublished": "2020-09-24", "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1}, "reviewBody": "\"Pracownik sklepu był bardzo miły i zabawny. Wrócimy w przyszłym roku i polecimy to miejsce wszystkim naszym znajomym i rodzinie. Bardzo dziękujemy za pomoc, rekomendacje i życzliwość! Dobre ceny i dobra obsługa.\"", "publisher": {"@type": "Organization", "name": "Google"}}, "line": 860, "visible_card": {"line": 860, "text": "★★★★★ “Pracownik sklepu był bardzo miły i zabawny. Wrócimy w przyszłym roku i polecimy to miejsce wszystkim naszym znajomym i rodzinie. Bardzo dziękujemy za pomoc, rekomendacje i życzliwość! Dobre ceny i dobra obsługa.” Michel new technology Opinia Google · 2020-09-24", "links": []}, "author_visible": true, "body_exact_substring": true, "date_visible": true} |

## U. MATRIZ ESTRUCTURA HTML/ARTICLE

| Idioma | Conteos fuente/token/DOM | Errores token | Pila sin cerrar | IDs duplicados |
| --- | --- | --- | --- | --- |
| en | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 8, "text_close": 8, "token_open": 8, "token_close": 8, "parsed": 8}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| es | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| fr | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| it | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| de | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| nl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pt | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| ca | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| sv | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |
| pl | {"html": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "head": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "body": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "header": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "main": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "nav": {"text_open": 3, "text_close": 3, "token_open": 3, "token_close": 3, "parsed": 3}, "section": {"text_open": 6, "text_close": 6, "token_open": 6, "token_close": 6, "parsed": 6}, "article": {"text_open": 11, "text_close": 11, "token_open": 11, "token_close": 11, "parsed": 11}, "footer": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "form": {"text_open": 1, "text_close": 1, "token_open": 1, "token_close": 1, "parsed": 1}, "table": {"text_open": 0, "text_close": 0, "token_open": 0, "token_close": 0, "parsed": 0}} | [] | [] | {} |

## V. MATRIZ ENLACES INTERNOS/SELECTOR IDIOMAS

| Idioma | Selectores | Referencias ID | Controles / formularios |
| --- | --- | --- | --- |
| en | [{"line": 607, "id": null, "links": [{"line": 607, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 625, "id": null, "links": [{"line": 625, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 664, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 789, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 793, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 798, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 802, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 812, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 602, "text": "Language", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 621, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Change language", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 627, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Toggle menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 790, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 794, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 799, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 803, "text": "General question Scooter rental Inline skates rental Bike rental Skateboards &amp; longboards", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 813, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 816, "text": "Send by WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| es | [{"line": 607, "id": null, "links": [{"line": 607, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 625, "id": null, "links": [{"line": 625, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 664, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 789, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 793, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 798, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 802, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 812, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 602, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 621, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambiar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 627, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir o cerrar menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 790, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 794, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 799, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 803, "text": "Consulta general Alquiler de scooters Alquiler de patines en línea Alquiler de bicicletas Skateboards y longboards", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 813, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 816, "text": "Enviar por WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| fr | [{"line": 550, "id": null, "links": [{"line": 550, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 550, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 568, "id": null, "links": [{"line": 568, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 568, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 606, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 731, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 735, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 740, "attribute": "for", "ref": "contactE-mail", "exists": true}, {"line": 744, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 755, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 545, "text": "Langue", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 564, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Changer de langue", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 570, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Ouvrir ou fermer le menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 732, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 736, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 741, "text": "", "attrs": {"id": "contactE-mail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 745, "text": "Question générale Location de scooters Location de rollers en ligne Location de vélos Skateboards et longboards", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 756, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 759, "text": "Envoyer par WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| it | [{"line": 552, "id": null, "links": [{"line": 552, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 570, "id": null, "links": [{"line": 570, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 611, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 736, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 740, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 745, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 749, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 760, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 547, "text": "Lingua", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 566, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Cambia lingua", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 572, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Apri o chiudi menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 737, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 741, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 746, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 750, "text": "Domanda generale Noleggio scooter Noleggio pattini in linea Noleggio biciclette Skateboard e longboard Lezioni", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 761, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 764, "text": "Invia su WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| de | [{"line": 553, "id": null, "links": [{"line": 553, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 553, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 571, "id": null, "links": [{"line": 571, "text": "en Englisch", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "es Spanisch", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "fr Französisch", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "it Italienisch", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "de Deutsch", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "nl Niederländisch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "pt Portugiesisch", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "ca Katalanisch", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 571, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 609, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 734, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 738, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 743, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 747, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 758, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 548, "text": "Sprache", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 567, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Sprache ändern", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 573, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menü öffnen oder schließen", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 735, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 739, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 744, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 748, "text": "Allgemeine Frage Scooter mieten Inlineskates mieten Fahrräder mieten Skateboards &amp; Longboards", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 759, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 762, "text": "Per WhatsApp senden", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| nl | [{"line": 566, "id": null, "links": [{"line": 566, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 566, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 584, "id": null, "links": [{"line": 584, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 584, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 622, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 747, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 751, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 756, "attribute": "for", "ref": "contactE-mail", "exists": true}, {"line": 760, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 771, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 561, "text": "Taal", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 580, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Taal wijzigen", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 586, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Menu openen of sluiten", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 748, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 752, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 757, "text": "", "attrs": {"id": "contactE-mail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 761, "text": "Algemene vraag Scooter huren Inline skates huren Fiets huren Skateboards &amp; longboards Lessen", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 772, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 775, "text": "Versturen via WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| pt | [{"line": 569, "id": null, "links": [{"line": 569, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 569, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 587, "id": null, "links": [{"line": 587, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 587, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 628, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 753, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 757, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 762, "attribute": "for", "ref": "contactE-mail", "exists": true}, {"line": 766, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 777, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 564, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 583, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Alterar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 589, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Abrir ou fechar menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 754, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 758, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 763, "text": "", "attrs": {"id": "contactE-mail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 767, "text": "Pergunta geral Aluguer de scooters Aluguer de patins em linha Aluguer de bicicletas Skateboards e longboards Aulas", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 778, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 781, "text": "Enviar por WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| ca | [{"line": 552, "id": null, "links": [{"line": 552, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 552, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 570, "id": null, "links": [{"line": 570, "text": "en English", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "es Spanish", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "fr French", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "it Italian", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "de German", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "nl Dutch", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "pt Portuguese", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "ca Catalan", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 570, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 611, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 736, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 740, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 745, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 749, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 760, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 547, "text": "Idioma", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 566, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Canviar idioma", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 572, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Obrir o tancar menú", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 737, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 741, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 746, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 750, "text": "Consulta general Lloguer de scooters Lloguer de patins en línia Lloguer de bicicletes Skateboards i longboards Classes", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 761, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 764, "text": "Enviar per WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| sv | [{"line": 567, "id": null, "links": [{"line": 567, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 567, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 585, "id": null, "links": [{"line": 585, "text": "en Engelska", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "es Spanska", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "fr Franska", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "it Italienska", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "de Tyska", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "nl Nederländska", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "pt Portugisiska", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "ca Katalanska", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "sv Svenska", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 585, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 624, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 749, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 753, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 758, "attribute": "for", "ref": "contactE-post", "exists": true}, {"line": 762, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 773, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 562, "text": "Språk", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 581, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Byt språk", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 587, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Öppna eller stäng menyn", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 750, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 754, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 759, "text": "", "attrs": {"id": "contactE-post", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 763, "text": "Allmän fråga Hyra scooter Hyra inlines Hyra cykel Skateboards och longboards Lektioner", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 774, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 777, "text": "Skicka via WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |
| pl | [{"line": 607, "id": null, "links": [{"line": 607, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 607, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}, {"line": 625, "id": null, "links": [{"line": 625, "text": "en Angielski", "href": "https://rentalscooterbarcelona.com/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "es Hiszpański", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/es/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "fr Francuski", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/fr/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "it Włoski", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/it/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "de Niemiecki", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/de/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "nl Niderlandzki", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/nl/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pt Portugalski", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pt/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "ca Kataloński", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/cat/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "sv Szwedzki", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/sv/location-contact/", "role": "menuitem"}}, {"line": 625, "text": "pl Polski", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "attrs": {"class": "dropdown-item", "href": "https://rentalscooterbarcelona.com/pl/location-contact/", "role": "menuitem"}}], "selected": []}] | [{"line": 664, "attribute": "aria-labelledby", "ref": "location-contact-title", "exists": true}, {"line": 789, "attribute": "for", "ref": "contactName", "exists": true}, {"line": 793, "attribute": "for", "ref": "contactPhone", "exists": true}, {"line": 798, "attribute": "for", "ref": "contactEmail", "exists": true}, {"line": 802, "attribute": "for", "ref": "contactTopic", "exists": true}, {"line": 813, "attribute": "for", "ref": "contactMessage", "exists": true}] | [{"tag": "button", "line": 602, "text": "Język", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTrigger", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 621, "text": "", "attrs": {"aria-expanded": "false", "aria-haspopup": "menu", "aria-label": "Zmień język", "class": "dropdown-trigger", "id": "langTriggerMobile", "type": "button"}, "parent_interactive": []}, {"tag": "button", "line": 627, "text": "", "attrs": {"aria-expanded": "false", "aria-label": "Przełącz menu", "class": "icon-btn", "id": "mobileMenuBtn"}, "parent_interactive": []}, {"tag": "input", "line": 790, "text": "", "attrs": {"id": "contactName", "name": "name", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 794, "text": "", "attrs": {"id": "contactPhone", "name": "phone", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "text"}, "parent_interactive": []}, {"tag": "input", "line": 799, "text": "", "attrs": {"id": "contactEmail", "name": "email", "required": "", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit", "type": "email"}, "parent_interactive": []}, {"tag": "select", "line": 803, "text": "Pytanie ogólne Wynajem skuterów Wynajem rolek Wynajem rowerów Deskorolki i longboardy Wynajem wrotek", "attrs": {"id": "contactTopic", "name": "topic", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit"}, "parent_interactive": []}, {"tag": "textarea", "line": 814, "text": "", "attrs": {"id": "contactMessage", "name": "message", "required": "", "rows": "6", "style": "width:100%;padding:.85rem 1rem;border:1px solid var(--border);border-radius:14px;font:inherit;resize:vertical"}, "parent_interactive": []}, {"tag": "button", "line": 817, "text": "Wyślij przez WhatsApp", "attrs": {"class": "btn btn-gradient", "type": "submit"}, "parent_interactive": []}] |

Los 12.046 enlaces internos de los 200 HTML apuntan al corpus incluido y todas las anclas locales se resuelven. No se han solicitado respuestas HTTP. La marca estática de idioma activo es una mejora.

## W. MATRIZ GLOBAL POR IDIOMA

| Idioma | Primera pasada | Segunda pasada independiente | Comprobaciones de página |
| --- | --- | --- | --- |
| en | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "en", "expected": "en", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/location-contact/", "pass": true}] |
| es | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/es/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/es/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "es", "expected": "es", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/es/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/es/location-contact/", "pass": true}] |
| fr | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/fr/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/fr/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "fr", "expected": "fr", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/fr/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/fr/location-contact/", "pass": true}] |
| it | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/it/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/it/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "it", "expected": "it", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/it/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/it/location-contact/", "pass": true}] |
| de | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/de/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/de/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "de", "expected": "de", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/de/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/de/location-contact/", "pass": true}] |
| nl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/nl/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/nl/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "nl", "expected": "nl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/nl/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/nl/location-contact/", "pass": true}] |
| pt | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pt/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/pt/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pt-PT", "expected": "pt-PT", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pt/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pt/location-contact/", "pass": true}] |
| ca | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/cat/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/cat/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "ca", "expected": "ca", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/cat/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/cat/location-contact/", "pass": true}] |
| sv | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/sv/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/sv/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "sv", "expected": "sv", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/sv/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/sv/location-contact/", "pass": true}] |
| pl | {"one_title": true, "one_description": true, "one_canonical": true, "canonical_own_path": true, "no_duplicate_head_singletons": true, "no_noindex_nofollow": true, "one_h1": true, "nonempty_headings": true, "og_locale": true, "og_alternates": true, "og_url": true, "no_meta_refresh_base": true, "json_all_valid": true, "all_references_resolved": true, "html_stack_balanced": true, "textual_structure_balanced": true, "ids_unique": true, "id_references_exist": true, "internal_fragments_exist": true, "img_alt_present": true, "links_named": true, "no_nested_interactives": true, "no_positive_tabindex": true, "no_javascript_hrefs": true, "blank_rel": true, "faq_visible_schema": true, "buttons_named": true, "selectors_match_hreflang": true, "selectors_current_page": false, "links_language": true, "reviews_visible_schema": true, "schema_hours_canonical": true, "global_identity_canonical": true, "coordinates_canonical": true, "no_old_coordinates": true} | {"original_bytes_match": true, "canonical_own": true, "hreflang_full_reciprocal": true, "og_url_own": true, "no_robot_block": true, "no_duplicate_metadata": true, "all_json_reparsed": true, "global_urls_root": true, "nap_address_exact": true, "name_phone_email": true, "ratings_canonical": true, "hours_canonical": true, "page_id_url_own": true, "one_date_per_entity": true, "no_old_coordinates": true, "map_identifiers": true, "unique_dom_ids": true, "aria_references_resolve": true, "faq_content_matches": true, "article_open_close_dom": true, "fragments_in_scope_resolve": true, "tel_mail_wa_canonical": true, "visible_article_date_matches": true} | [{"path": "$.@graph[2]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "url", "actual": "https://rentalscooterbarcelona.com/pl/location-contact/", "expected_page": "https://rentalscooterbarcelona.com/pl/location-contact/", "pass": true}, {"path": "$.@graph[2]", "property": "inLanguage", "actual": "pl", "expected": "pl", "pass": true, "literal_equal": true, "interpretation": "Idioma principal coincidente; región opcional, no es error por granularidad."}, {"path": "$.@graph[0]", "property": "@id", "actual": "https://rentalscooterbarcelona.com/pl/location-contact/#webpage", "expected_page": "https://rentalscooterbarcelona.com/pl/location-contact/", "pass": true}] |

## LISTA FINAL DE CAMBIOS PROPUESTOS

| Punto | Idioma | Prioridad | Elemento | Propuesta |
| --- | --- | --- | --- | --- |

## CONTROL FINAL

Integridad SHA-256 comprobada contra cada entrada ZIP. Las evidencias contienen valores y líneas por archivo. No se han modificado HTML ni aplicado correcciones. Imágenes y tamaños quedan pendientes; no se ha certificado renderizado, entrega de formularios, indexación ni disponibilidad remota.
