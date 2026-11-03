# Velocidad y rendimiento de Rate Cloud

La pregunta práctica sobre rendimiento es cuánto tarda en llegar un resultado útil para tu tarea. Una tasa alta de tokens durante la generación no describe toda la experiencia: también influyen la espera, el procesamiento de la entrada, la longitud de la salida y la recuperación.

## Resumen de rendimiento publicado

Los siguientes valores aparecían en la página principal de Rate Cloud el 3 de noviembre de 2026. La fecha es la de consulta, no un periodo de medición establecido de forma independiente.

| Modelo | Respuesta completa habitual, segundos | Tokens/s efectivos habituales, incluida la espera | Tokens/s efectivos de respuestas rápidas, incluida la espera |
| --- | ---: | ---: | ---: |
| GLM 5.3 | 21,48 | 14,05 | 58,47 |
| GLM 5.3 Flash | 23,32 | 14,58 | 61,92 |
| DeepSeek V4 Pro | 15,67 | 25,83 | 127,84 |
| DeepSeek V4.1 Flash | 14,99 | 19,22 | 78,38 |
| Qwen 3.8 Max | 21,37 | 13,13 | 80,68 |

Son observaciones del servicio publicadas, no tiempos de respuesta garantizados, pruebas fijas de hardware ni una comparación controlada con solicitudes idénticas. La página principal no indica junto a esta tabla el tamaño de la muestra ni el intervalo completo de medición, por lo que las cifras no prueban disponibilidad sostenida ni un SLA.

## Qué significan las columnas

El tiempo de respuesta completa va desde el envío de la solicitud hasta la recepción del resultado terminado. Incluye la espera, el procesamiento de la entrada y la generación de la respuesta.

El sitio define “habitual” como el punto medio de los resultados: la mitad termina más rápido y la otra mitad más lento. Las cifras efectivas de tokens por segundo incluyen toda la solicitud y su tiempo de espera. No deben llamarse velocidad pura de decodificación ni tiempo hasta el primer token.

La columna de respuestas rápidas describe las diez solicitudes más rápidas de cada cien. Muestra la parte más veloz de la distribución observada, pero no promete esa tasa para una nueva solicitud. No calcules una longitud media de salida multiplicando valores de latencia y rendimiento resumidos por separado.

## Por qué tu tarea puede tardar más

Un documento largo requiere más procesamiento de entrada que una pregunta breve. Una respuesta detallada tarda más en generarse que una corta. Los agentes que usan herramientas pueden necesitar varias llamadas para completar una tarea. La carga actual, la elegibilidad del perfil, la preparación de la réplica y la recuperación también pueden afectar al tiempo transcurrido.

Un modelo promocionado para tareas frecuentes o rápidas puede tener una duración mediana observada superior a la de otro si difiere la mezcla de solicitudes observadas. La tabla por sí sola no separa la velocidad del modelo de la complejidad de las instrucciones, la longitud de las respuestas o el comportamiento del usuario.

## Concurrencia y rendimiento total

Cuatro espacios de pago permiten que avancen varias operaciones independientes al mismo tiempo. No hacen que una solicitud individual sea cuatro veces más rápida. El paralelismo ayuda cuando el trabajo puede dividirse en tareas independientes; una cadena secuencial de razonamiento o herramientas sigue esperando a que se completen sus dependencias.

Para una evaluación práctica, mide tu propio tiempo hasta obtener un resultado útil, la corrección de la salida, las solicitudes incompletas, los errores y la proporción de tareas que requieren reintentos. Anota el modelo, el tamaño de entrada y salida, la concurrencia y el periodo de observación para que los resultados sean interpretables.

Fuente: [tabla de rendimiento y explicaciones publicadas por Rate Cloud](https://rate-cloud.com/). Consulta también [la documentación de conexión](https://rate-cloud.com/docs). [Volver al índice](../README.md).

## Resultados públicos disponibles y datos descargables

La tabla anterior contiene los 15 resultados numéricos publicados en la tabla de rendimiento de cinco modelos de la página principal cuando se consultó. Una [copia CSV](../../data/performance-2026-11-03.csv) conserva los ID de modelo, las unidades, la fecha de consulta y la URL de origen para reutilizarlos. No se realizó ninguna prueba nueva para crearla.

| Elemento de evidencia | ¿Disponible en esta copia? |
| --- | --- |
| Duración típica de respuesta completa, los cinco modelos | Sí, tabla y CSV |
| Tasa efectiva típica de tokens, incluida la espera, los cinco modelos | Sí, tabla y CSV |
| Tasa efectiva del decil más rápido, los cinco modelos | Sí, tabla y CSV |
| Tiempos de cada solicitud, tamaño de muestra e intervalo observado originales | No se indican junto a la tabla pública |
| Tiempo hasta el primer token, velocidad pura de decodificación y percentiles de latencia | No se indican en la tabla pública |
| Comparación controlada con los mismos trabajos frente a proveedores oficiales | No disponible en este repositorio |

La página principal enlaza la metodología en `/docs#statistics`; cuando se consultó, la documentación actual de conexión no mostraba una sección detallada de estadísticas coincidente. Conservamos esa laguna de evidencia en vez de inventar resultados adicionales. Para comparar precios y condiciones, consulta [la comparación de API oficiales](08-cost-and-service-comparison.md).
