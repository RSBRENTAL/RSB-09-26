# 05_ROLLERBLADES — Mejoras no obligatorias

Extraídas del informe original. No son errores adicionales ni instrucciones para aplicar cambios automáticamente. Respetar los idiomas indicados en cada propuesta.

## I. MEJORAS RECOMENDADAS

### Identificar el idioma activo en el HTML

Cada selector contiene las 10 URLs correctas, pero no hay `aria-current` ni una clase `active` en sus enlaces estáticos. Es una mejora de información accesible. No se deduce que el JS externo deje el selector sin indicador visual en ejecución.

### Terminología sueca del encabezado de guías

En SV, línea 916: `Tips innan du hyr skridskor i Barcelona`. Usar `inlines` también en este encabezado haría explícito el mismo servicio que en el H1. Se separa de P4: aquí se recomienda precisión terminológica, no se atribuye a la tienda un servicio de hielo a partir de una palabra aislada.


## J. OPCIONALES

La cobertura Schema adicional de EN, ES y PL (AggregateOffer y algunos ContactPoint/acciones) no convierte a los otros idiomas en incorrectos. Las entidades del mismo @id repartidas en varios bloques pueden complementarse; por ejemplo, las listas `sameAs` parciales son compatibles con la lista más amplia. Solo se señala como incidencia la divergencia de fecha de P1.

Se registran diferencias de dimensiones declaradas de una misma imagen en distintos contextos. Pueden corresponder a tamaños de presentación o recortes. Para decidir si son errores hacen falta los archivos de imagen y el CSS; no se propone una corrección de dimensiones a ciegas. Los title y textos OG/Twitter pueden diferir manteniendo el mismo tema y no necesitan ser idénticos.

