# Modelos y cómo elegir

El catálogo publicado de Rate Cloud contiene cinco modelos. Cada uno tiene una suscripción independiente y un identificador exacto para solicitudes HTTP directas. Elige un modelo según el trabajo que necesitas y pruébalo con entradas representativas.

## Catálogo publicado

| Modelo | ID de API directa | Enfoque principal | Entrada de imagen | Precio publicado por 30 días |
| --- | --- | --- | --- | ---: |
| GLM 5.3 | `glm-5.3` | Desarrollo complejo y agentes autónomos | No | $34,38 USD |
| GLM 5.3 Flash | `glm-5.3-flash` | Solicitudes frecuentes, programación diaria, automatización y subagentes | Sí | $30,16 USD |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Agentes de programación y tareas de programación en paralelo | Sí | $30,16 USD |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Razonamiento en varios pasos, arquitectura y revisión de código | No | $27,56 USD |
| Qwen 3.8 Max | `qwen-3.8-max` | Repositorios grandes, documentos, investigación y contexto largo | Sí | $31,49 USD |

Los precios en USD y las capacidades reflejan la visualización de moneda del sitio el 3 de noviembre de 2026. Los precios pueden cambiar antes de pagar; comprueba el panel antes de comprar. Cada suscripción de pago indicada incluye cuatro solicitudes simultáneas y no tiene una cuota acumulada de tokens durante su vigencia. La entrada de imagen significa que el modelo acepta imágenes; no implica generación de imágenes.

## Elegir un modelo para tu flujo de trabajo

GLM 5.3 está orientado al trabajo sostenido en proyectos de software complejos, análisis de repositorios, uso de herramientas y coordinación de subagentes. GLM 5.3 Flash se dirige al trabajo cotidiano repetido y a la automatización que requiere muchas llamadas independientes.

DeepSeek V4.1 Flash está orientado a generar y modificar código, agentes de programación y cargas de trabajo con muchas tareas de programación. DeepSeek V4 Pro destaca el razonamiento y el análisis profundo, incluidas las decisiones de arquitectura y las revisiones en las que la calidad importa más que reducir al mínimo la demora.

Qwen 3.8 Max se presenta para grandes volúmenes de material, incluidos repositorios y documentos. La referencia a contexto largo no es una especificación numérica de la ventana de contexto. Antes de diseñar flujos con entradas grandes, consulta la documentación vigente y los límites reales de las solicitudes.

Son casos de uso del producto, no una clasificación universal ni una garantía de que un modelo gane en todas las tareas. Una evaluación útil incluye la corrección de la tarea, el seguimiento de instrucciones, el comportamiento de las llamadas a herramientas, los requisitos de imágenes, el tiempo de respuesta y la cantidad de correcciones manuales necesarias.

## Identidad del modelo y perfil de ejecución

Un modelo puede tener varios perfiles de precisión aprobados. El sistema de enrutamiento selecciona un perfil adecuado del modelo solicitado por el usuario. Elegir un perfil de ejecución compacto no significa sustituir el modelo solicitado por otra entrada del catálogo. Flash y Pro son modelos distintos.

Usa los ID exactos de la tabla para la API directa. Los nombres de modelo específicos de un cliente pueden incluir un prefijo de proveedor, que no forma parte del identificador HTTP directo. Que un modelo aparezca en la lista de un cliente no demuestra por sí solo que la cuenta o la clave tengan permiso para ejecutarlo.

Fuentes: [catálogo y precios](https://rate-cloud.com/), [ID de modelos para API](https://rate-cloud.com/docs) y [perfiles de modelo](https://rate-cloud.com/how-it-works). [Volver al índice](../README.md).
