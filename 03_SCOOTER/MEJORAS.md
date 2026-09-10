# 03_SCOOTER — Mejoras no obligatorias

Extraídas del informe original. No son errores adicionales ni instrucciones para aplicar cambios automáticamente. Respetar los idiomas indicados en cada propuesta.

## I. MEJORAS RECOMENDADAS

### Redacción del depósito: aclarar si existen excepciones

En SCOOTER se usa una formulación condicional en los 10 idiomas; en PRICES también en CA, SV y PL. Las otras 7 versiones de PRICES afirman que el depósito se aplica al scooter. CANONICAL establece un depósito reembolsable, pero no detalla excepciones por categoría. Esto justifica unificar y precisar el mensaje; no demuestra por sí solo que una de las políticas sea falsa. No se propone inventar un importe ni convertir la mención histórica de 250 € de una reseña en una condición vigente.

| Idioma | Línea FAQ visible | Texto literal |
| --- | --- | --- |
| EN | 1161 | A refundable deposit may apply depending on the scooter category and vehicle. Bring your ID or passport and contact us for details. |
| ES | 1119 | Puede aplicarse un depósito reembolsable según la categoría y el vehículo. Trae tu DNI o pasaporte y contáctanos para más detalles. |
| FR | 1012 | Une caution remboursable peut s’appliquer selon la catégorie du scooter et le véhicule. Apportez votre pièce d’identité ou passeport et contactez-nous pour plus de détails. |
| IT | 1017 | È possibile che venga richiesto un deposito rimborsabile in base alla categoria dello scooter e al veicolo. Porta un documento d’identità o passaporto e contattaci per maggiori dettagli. |
| DE | 1113 | Je nach Scooter-Kategorie und Fahrzeug kann eine rückerstattbare Kaution erforderlich sein. Bring deinen Ausweis oder Reisepass mit und kontaktiere uns für weitere Details. |
| NL | 1122 | Er kan een terugbetaalbare borg gelden afhankelijk van de scootercategorie en het voertuig. Neem je ID of paspoort mee en neem contact met ons op voor meer details. |
| PT | 1084 | Pode aplicar-se uma caução reembolsável conforme a categoria da scooter e o veículo. Traz o teu documento de identificação ou passaporte e contacta-nos para mais detalhes. |
| CA | 1060 | Pot aplicar-se un dipòsit reemborsable segons la categoria del scooter i el vehicle. Porta el DNI o passaport i contacta’ns per a més detalls. |
| SV | 1073 | En återbetalningsbar deposition kan krävas beroende på scooterns kategori och fordonet. Ta med ID eller pass och kontakta oss för mer information. |
| PL | 1127 | Może obowiązywać zwrotna kaucja w zależności od kategorii skutera i pojazdu. Zabierz dowód osobisty lub paszport i skontaktuj się z nami, aby uzyskać więcej informacji. |

### Acotar qué resume AggregateOffer en EN, ES y PL

Declara `lowPrice=35`, `highPrice=115`, `offerCount=5`. Las cinco tarifas individuales son 35, 40, 80, 115 y 30 EUR. La de 30 EUR es una prolongación («día extra») y no equivale a un alquiler inicial. El mínimo aritmético es 30, pero presentar «desde 30» como precio de entrada podría inducir a error. Conviene separar claramente la prolongación del conjunto resumido o documentar el alcance del agregado. No se declara que el alquiler inicial de 35 EUR esté mal ni se recomienda cambiarlo a 30 automáticamente.

### Identificar el idioma activo en el HTML

Cada selector contiene las 10 URLs correctas, pero no hay `aria-current` ni una clase `active` en sus enlaces estáticos. Es una mejora de información accesible. No se deduce que el JS externo deje el selector sin indicador visual en ejecución.


## J. OPCIONALES

La cobertura Schema adicional de EN, ES y PL (AggregateOffer y algunos ContactPoint/acciones) no convierte a los otros idiomas en incorrectos. Las entidades del mismo @id repartidas en varios bloques pueden complementarse; por ejemplo, las listas `sameAs` parciales son compatibles con la lista más amplia. Solo se señala como incidencia la divergencia de fecha de P1.

Las 60 reseñas de SCOOTER tienen fecha visible, pero no `Review.datePublished` en Schema. Añadirla con el dato visible es opcional; la ausencia no contradice la fecha. Solo PT incluye una FAQ adicional sobre devolución fuera de horario: coincide con CANONICAL y no exige copiarla a otros idiomas.

Se registran diferencias de dimensiones declaradas de una misma imagen en distintos contextos. Pueden corresponder a tamaños de presentación o recortes. Para decidir si son errores hacen falta los archivos de imagen y el CSS; no se propone una corrección de dimensiones a ciegas. Los title y textos OG/Twitter pueden diferir manteniendo el mismo tema y no necesitan ser idénticos.

