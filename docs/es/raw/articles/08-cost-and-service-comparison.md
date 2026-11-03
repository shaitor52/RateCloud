# Rate Cloud frente a las API oficiales: coste fijo para trabajo sostenido

English · [Русский](../../ru/articles/08-cost-and-service-comparison.md) · Español · [Português](../../pt/articles/08-cost-and-service-comparison.md)

**La ventaja de Rate Cloud es un precio de suscripción fijo y sin cuota acumulada de tokens. A medida que aumenta el uso, el precio de la suscripción al modelo se mantiene.** Una API de pago por uso cobra cada token facturable. Esto puede hacer que la programación, el análisis y la automatización sostenidos sean mucho más baratos en Rate Cloud, siempre que la carga de trabajo se ajuste a su velocidad, concurrencia, funciones y disponibilidad.

Rate Cloud no es automáticamente más barato cuando el uso es ligero. Los proveedores oficiales ofrecen descuentos útiles por caché, lotes, horarios de menor demanda y otras condiciones. Esta comparación hace explícitos esos compromisos. Comprobado el 3 de noviembre de 2026; no es una promesa de precios futuros.

## Tarifas oficiales de API y suscripciones de Rate Cloud

Las tarifas de API corresponden a un millón de tokens. Las tarifas de entrada de esta tabla son **sin caché**. Los precios de Rate Cloud están expresados en USD por 30 días para una suscripción a un modelo con cuatro espacios. Reflejan la visualización de moneda del sitio consultada el 3 de noviembre de 2026 y pueden cambiar antes del pago.

| API oficial y condición de facturación | Entrada USD/M | Salida USD/M | Modelo Rate Cloud / USD por 30 días |
| --- | ---: | ---: | --- |
| Z.ai GLM-5.3 | 1,40 | 4,40 | GLM 5.3 / 34,38 |
| Z.ai GLM-5.3-Flash | 0,15 | 0,50 | GLM 5.3 Flash / 30,16 |
| DeepSeek V4.1 Flash, horario valle | 0,15 | 0,60 | DeepSeek V4.1 Flash / 30,16 |
| DeepSeek V4.1 Flash, hora punta | 0,30 | 1,20 | DeepSeek V4.1 Flash / 30,16 |
| DeepSeek V4 Pro, horario valle | 0,66 | 1,98 | DeepSeek V4 Pro / 27,56 |
| DeepSeek V4 Pro, hora punta | 1,32 | 3,96 | DeepSeek V4 Pro / 27,56 |
| QwenCloud Qwen3.8-Max, endpoint de Singapur | 2,00 | 6,00 | Qwen 3.8 Max / 31,49 |
| OpenAI GPT-6.1 Sol, Standard y contexto corto | 2,00 | 10,00 | Alternativa de otro modelo; GPT no se vende aquí |

Fuentes: [precios de Z.ai](https://docs.z.ai/guides/overview/pricing), [precios y franjas horarias de DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/), [precios del modelo QwenCloud y endpoint de Singapur](https://www.qwencloud.com/models/qwen3.8-max), [precios de GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) y [catálogo de Rate Cloud](https://rate-cloud.com/).

El nombre de la API oficial de DeepSeek Flash es `deepseek-flash` para la versión V4.1-Flash-1017; Rate Cloud usa `deepseek-v4.1-flash`. Las horas punta de DeepSeek son 01:00-04:00 y 06:00-10:00 UTC de lunes a viernes, excepto festivos públicos chinos; el resto de horas es valle. Las filas de GLM y DeepSeek comparan las versiones con el mismo nombre. Qwen comparte la etiqueta de familia del producto; las funciones de alojamiento y los perfiles de ejecución pueden diferir. GPT es una alternativa para trabajos similares, no tiene los mismos pesos, capacidades ni calidad de salida.

## Coste de uso repetido

Supongamos que el total de tokens facturados se compone de un 80 % de entrada y un 20 % de salida, sin aciertos de caché, herramientas, lotes, impuestos, descuentos especiales ni recargo por contexto largo. Cuando corresponda, los tokens de razonamiento deben incluirse en la salida facturable. Son **escenarios aritméticos de carga de trabajo**, no uso real de clientes ni una cantidad que Rate Cloud garantice procesar en 30 días.

| API oficial | 10M de tokens totales | 100M | 500M | 1 000 millones |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.3 | $20 | $200 | $1 000 | $2 000 |
| GLM-5.3-Flash | $2,20 | $22 | $110 | $220 |
| DeepSeek Flash, valle / punta | $2,40 / $4,80 | $24 / $48 | $120 / $240 | $240 / $480 |
| DeepSeek Pro, valle / punta | $9,24 / $18,48 | $92,40 / $184,80 | $462 / $924 | $924 / $1 848 |
| Qwen3.8-Max | $28 | $280 | $1 400 | $2 800 |
| GPT-6.1 Sol Standard | $36 | $360 | $1 800 | $3 600 |

**Los precios publicados en USD de las suscripciones de modelos de Rate Cloud a 30 días se mantienen entre $27,56 y $34,38 en estos escenarios de volumen.** Esto describe la estructura de precios, no garantiza que se complete un volumen de mil millones de tokens. Varias suscripciones, espacios adicionales, alojamiento del cliente, servicios de búsqueda web, cómputo de CI y otras herramientas de tu aplicación pueden añadir costes.

## Punto de equilibrio en lugar de una afirmación engañosa de ahorro universal

Con precios en USD, 500 millones de tokens sin caché cuestan $1 000 en la API oficial GLM-5.3 frente a $34,38 por una suscripción GLM de Rate Cloud: unas 29,1 veces el coste de acceso al modelo. Con la API económica DeepSeek Flash en horario valle, el mismo cálculo da $120 frente a $30,16: unas 4,0 veces. Los precios de Rate Cloud reflejan la visualización en USD del sitio consultada el 3 de noviembre de 2026 y pueden cambiar antes del pago.

Con esos precios, el volumen de equilibrio sin caché es de unos 17,19 millones de tokens para GLM-5.3, 137,09 millones para GLM Flash, 125,67 millones para DeepSeek Flash en valle, 29,83 millones para DeepSeek Pro en valle y 11,25 millones para Qwen. Por debajo del umbral correspondiente, la factura por tokens del proveedor oficial puede ser menor. Una proporción alta de aciertos de caché eleva esos umbrales.

Fórmula general, con el volumen expresado en millones:

```text
weighted USD per million = input_fraction * input_price + output_fraction * output_price
break_even_millions = subscription_USD / weighted_USD_per_million
```

Ejemplo de sensibilidad con todos los tokens de entrada acertando en caché para DeepSeek Flash valle: con $0,003 por entrada y $0,60 por salida, 500 millones al 80/20 cuestan $61,20, no $120. Frente a los $30,16 de la suscripción DeepSeek Flash de Rate Cloud, son unas 2,0 veces el coste. La elegibilidad real de caché no está garantizada, y pueden aplicarse cargos por escritura de caché u otros conceptos. Qwen, Z.ai y OpenAI también publican descuentos de caché; OpenAI ofrece tarifas menores para Batch/Flex y cobra más por modos de contexto largo o Fast. Compara la tarifa concreta que usarías.

Reproduce escenarios sin conexión con los [datos de precios fechados](../../data/pricing-2026-11-03.json) y la [calculadora](../../tools/compare_costs.py):

```sh
python3 tools/compare_costs.py --million-tokens 500
python3 tools/compare_costs.py --million-tokens 500 --cached-input-share 1
```

Ejecuta desde la raíz del repositorio. No se hacen solicitudes a API. Los importes de suscripción son el snapshot de visualización en USD indicado arriba, no una cotización para compras futuras.

## Velocidad y compromisos del servicio

Elige Rate Cloud cuando importe más un coste predecible para trabajo sostenido que minimizar la latencia de cada respuesta. Un proveedor directo o un nivel premium de velocidad puede ser más adecuado si tus propias pruebas muestran menor latencia o si necesitas sus funciones alojadas, mucha más concurrencia o condiciones contractuales. Cuatro espacios de Rate Cloud no equivalen a las cuotas de concurrencia de las API oficiales.

Este repositorio **no** contiene una prueba de velocidad controlada con las mismas instrucciones y el mismo esfuerzo en todos estos servicios. Por ello no publicamos tokens por segundo inventados para la competencia ni afirmamos una clasificación universal de velocidad medida. El resumen completo de velocidad publicado por Rate Cloud está en [rendimiento](04-performance.md). Incluye el tiempo de espera y difiere de la velocidad pura de generación de tokens. Esta comparación reconoce explícitamente los compromisos de latencia y capacidad, sin presentarlos como un resultado comparativo establecido.

Las suscripciones oficiales de programación y las aplicaciones de chat gratuitas son productos distintos del acceso a API medido por uso. Esta tabla compara las API indicadas, no todos los planes de cada proveedor. Evalúa la calidad y las funciones además del precio.

[Casos de uso en los que ayuda una factura fija de tokens](09-unlimited-use-cases.md) · [Volver al índice](../README.md)
