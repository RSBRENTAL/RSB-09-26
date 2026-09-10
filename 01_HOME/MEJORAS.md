# 01_HOME — Mejoras no obligatorias

Extraídas del informe original. No son errores adicionales ni instrucciones para aplicar cambios automáticamente. Respetar los idiomas indicados en cada propuesta.

## I. MEJORAS RECOMENDADAS

### Explicitar «3 días o más» junto a cada anuncio de entrega gratuita

En el bloque de ventajas de ES, FR, IT, PT y CA la frase de entrega gratuita remite a condiciones sin incluir allí la duración. La condición correcta sí aparece en el hero, la tarjeta de scooter y la FAQ del mismo HTML. Es una mejora de claridad para lecturas aisladas; no se cuenta como contradicción de política.

### Identificar el idioma activo en el HTML

Cada selector contiene las 10 URLs correctas, pero no hay `aria-current` ni una clase `active` en sus enlaces estáticos. Es una mejora de información accesible. No se deduce que el JS externo deje el selector sin indicador visual en ejecución.


## J. OPCIONALES

La cobertura Schema adicional de EN, ES y PL (AggregateOffer y algunos ContactPoint/acciones) no convierte a los otros idiomas en incorrectos. Las entidades del mismo @id repartidas en varios bloques pueden complementarse; por ejemplo, las listas `sameAs` parciales son compatibles con la lista más amplia. Solo se señala como incidencia la divergencia de fecha de P1.

Se registran diferencias de dimensiones declaradas de una misma imagen en distintos contextos. Pueden corresponder a tamaños de presentación o recortes. Para decidir si son errores hacen falta los archivos de imagen y el CSS; no se propone una corrección de dimensiones a ciegas. Los title y textos OG/Twitter pueden diferir manteniendo el mismo tema y no necesitan ser idénticos.

