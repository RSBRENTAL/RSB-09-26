# 02_PRICES — Mejoras no obligatorias

Extraídas del informe original. No son errores adicionales ni instrucciones para aplicar cambios automáticamente. Respetar los idiomas indicados en cada propuesta.

## I. MEJORAS RECOMENDADAS

### Redacción del depósito: aclarar si existen excepciones

En SCOOTER se usa una formulación condicional en los 10 idiomas; en PRICES también en CA, SV y PL. Las otras 7 versiones de PRICES afirman que el depósito se aplica al scooter. CANONICAL establece un depósito reembolsable, pero no detalla excepciones por categoría. Esto justifica unificar y precisar el mensaje; no demuestra por sí solo que una de las políticas sea falsa. No se propone inventar un importe ni convertir la mención histórica de 250 € de una reseña en una condición vigente.

| Idioma | Línea FAQ visible | Texto literal |
| --- | --- | --- |
| CA | 1530 | Per a la majoria d’articles pots venir directament a la botiga, però els caps de setmana i en temporada alta és recomanable reservar, sobretot per a grups. Cal document d’identitat o passaport per a tots els lloguers. Només en el lloguer de scooter pot aplicar-se un dipòsit retornable; bicicletes, patins en línia, patins de quatre rodes, skateboards i longboards no requereixen dipòsit. |
| SV | 1537 | För de flesta artiklar kan du komma direkt till butiken, men på helger och under högsäsong rekommenderas bokning, särskilt för grupper. ID-kort eller pass krävs för alla hyror. En återbetalningsbar deposition kan endast tillkomma vid scooteruthyrning; inlines, cyklar, rullskridskor, skateboards och longboards kräver ingen deposition. |
| PL | 1543 | W przypadku większości sprzętu możesz przyjść bezpośrednio do wypożyczalni, ale w weekendy i w sezonie zalecana jest rezerwacja, szczególnie dla grup. Do każdego wynajmu wymagany jest dokument tożsamości lub paszport. Kaucja zwrotna może być wymagana wyłącznie przy wynajmie skutera; rolki, rowery, wrotki, deskorolki i longboardy nie wymagają kaucji. |

### Relaciones accesibles de los desplegables

Las 6 preguntas por idioma tienen botones con `aria-expanded`; sus paneles no tienen IDs ni `aria-controls` en el HTML. Los menús de idioma tampoco tienen IDs de panel en estas páginas. No hay referencias rotas: falta la asociación explícita. Puede completarse, comprobando antes cómo actúa el JS externo, que no pertenece a este alcance.

### Identificar el idioma activo en el HTML

Cada selector contiene las 10 URLs correctas, pero no hay `aria-current` ni una clase `active` en sus enlaces estáticos. Es una mejora de información accesible. No se deduce que el JS externo deje el selector sin indicador visual en ejecución.


## J. OPCIONALES

La cobertura Schema adicional de EN, ES y PL (AggregateOffer y algunos ContactPoint/acciones) no convierte a los otros idiomas en incorrectos. Las entidades del mismo @id repartidas en varios bloques pueden complementarse; por ejemplo, las listas `sameAs` parciales son compatibles con la lista más amplia. Solo se señala como incidencia la divergencia de fecha de P1.

Se registran diferencias de dimensiones declaradas de una misma imagen en distintos contextos. Pueden corresponder a tamaños de presentación o recortes. Para decidir si son errores hacen falta los archivos de imagen y el CSS; no se propone una corrección de dimensiones a ciegas. Los title y textos OG/Twitter pueden diferir manteniendo el mismo tema y no necesitan ser idénticos.

