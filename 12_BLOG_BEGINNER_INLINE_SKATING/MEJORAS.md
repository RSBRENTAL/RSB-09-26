# 12_BLOG_BEGINNER_INLINE_SKATING — Mejoras no obligatorias

Extraídas del informe original. No son errores adicionales ni instrucciones para aplicar cambios automáticamente. Respetar los idiomas indicados en cada propuesta.

## I. MEJORAS RECOMENDADAS

### Relaciones accesibles e idioma activo

Los 240 selectores del ZIP enlazan a los 10 destinos correctos; no señalan la opción actual con aria-current/clase active en el HTML estático. Se recomienda identificarla. En las FAQ de blog, los botones con aria-expanded no están asociados mediante aria-controls a paneles con ID. Añadir la asociación es una mejora; no hay referencias rotas. Comprobar el JS antes de implementarla. No se deduce que el indicador o acordeón falle en ejecución.

### FAQ específicas de cada artículo

Las cinco FAQ de BEGINNER y HOURLY en EN son idénticas entre sí, aunque el cuerpo aborda decisiones distintas. Coinciden con el Schema de cada página, así que no hay desajuste FAQ/Schema. En HOURLY conviene responder sobre devolución, cómputo de tiempo y ampliaciones; en BEGINNER, sobre ajuste, frenado y elección de trayecto. No se extrapola esta identidad literal a los otros nueve idiomas.


## J. OPCIONALES

Las variantes fr/fr-FR, it/it-IT y equivalentes conservan el mismo idioma: no se consideran un error por distinta precisión regional. Tampoco se exige identidad literal entre title, H1, OG, Twitter y headline si el tema sigue siendo coherente. No se exige traducir un slug estable ni sustituir /cat/ por /ca/.

Un BlogPosting con @id propio y mainEntityOfPage correcto no necesita una url redundante para evitar un error inexistente. Puede añadirse por uniformidad. La fecha de publicación puede variar por traducción; solo se señalan fechas de actualización contradictorias de la misma entidad o del artículo visible. WebPage y BlogPosting son entidades diferentes: sus fechas no se igualan automáticamente.

Las extensiones del mismo @id en varios bloques pueden complementar rating, reseñas, sameAs o autor; no se clasifican como duplicación errónea por su mera presencia. La Organization llamada Google es publicador de reseñas, no una segunda empresa RSB. AggregateOffer/ContactPoint/acciones no tienen por qué tener idéntica cobertura entre idiomas. La presencia de rating no garantiza que Google muestre estrellas.

Las dimensiones de imágenes son atributos de presentación. Sin imágenes ni CSS no se puede asegurar que diferencias de width/height sean errores. No se propone modificarlas a ciegas. Una fecha visible con elemento time/datetime sería una mejora semántica, pero primero debe resolverse el dato real de P4.

