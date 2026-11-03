# Qué ofrece Rate Cloud

Rate Cloud se basa en un modelo de compra sencillo: pagas por acceder a un modelo de IA seleccionado durante un periodo definido y luego utilizas su API sin una cuota acumulada de tokens. Esto resulta especialmente útil cuando una aplicación realiza muchas llamadas al modelo y es difícil prever una factura basada en tokens.

Un agente autónomo de programación puede leer un repositorio, planificar un cambio, editar archivos, ejecutar herramientas, revisar errores y repetir el proceso muchas veces. Cada ciclo puede implicar otra solicitud y más tokens de entrada y salida. El precio de la suscripción de Rate Cloud no aumenta según la cantidad de tokens consumidos durante su vigencia.

## Tokens ilimitados y capacidad de procesamiento finita

Tokens ilimitados significa que Rate Cloud no impone una cuota diaria, semanal o mensual sobre el total de tokens de entrada y salida usados durante el periodo de pago. No significa que una solicitud pueda contener un contexto ilimitado ni ejecutarse para siempre. La capacidad de contexto, los plazos de las operaciones, la ejecución simultánea, los límites de protección, la capacidad del hardware y la disponibilidad del servicio siguen siendo finitos.

El volumen mensual real de procesamiento depende del modelo, la longitud de la entrada y la salida, la velocidad de respuesta y el paralelismo disponible. Los ejemplos con cientos de millones o miles de millones de tokens ilustran el principio de precios; no prometen ese volumen mensual de procesamiento.

## Cuatro espacios simultáneos por suscripción de pago

Cada suscripción de pago ofrece cuatro solicitudes simultáneas para su modelo. Un espacio representa una solicitud que se está procesando. Cuando termina, el espacio vuelve a estar disponible. No es un límite de cuatro solicitudes al día o al mes.

Un desarrollador podría usar los cuatro espacios para un agente principal y tres subagentes, cuatro sesiones de trabajo distintas o tareas de automatización independientes. Las claves de API de una misma cuenta comparten el conjunto de espacios del modelo correspondiente. Crear más claves no aumenta la capacidad.

Se pueden combinar suscripciones. Dos suscripciones al mismo modelo ofrecen ocho espacios para ese modelo. Las suscripciones a modelos distintos tienen conjuntos separados: por ejemplo, cuatro espacios de GLM y cuatro de DeepSeek. El flujo de trabajo debe enviar las solicitudes al modelo correspondiente para usar cada conjunto.

## Periodos de acceso y primeros pasos

El sitio ofrece suscripciones de 3, 7 y 30 días. Los nuevos usuarios pueden probar los modelos durante las primeras tres horas tras registrarse y completar las verificaciones requeridas de correo electrónico y Telegram, con un espacio simultáneo. La prueba y las suscripciones de pago tienen condiciones distintas.

Empieza con una tarea representativa: un repositorio en el que realmente trabajas, un documento habitual o un patrón real de automatización. Antes de elegir un modelo y un periodo de suscripción, evalúa la respuesta, el comportamiento de las herramientas y el tiempo total hasta obtener un resultado útil.

## Dónde encaja el servicio

Rate Cloud puede servir como capa de modelos para agentes de programación, asistentes internos, bots, procesos de extracción de datos, flujos de documentos y productos propios. El cliente compatible aporta su propia interfaz, herramientas, instrucciones del proyecto e historial. Las funciones disponibles que dependen del modelo están determinadas por el modelo elegido y la integración de API.

El servicio ofrece acceso a API. Conectar una aplicación conocida no convierte el modelo GLM, DeepSeek o Qwen seleccionado en un modelo propio de primera parte de esa aplicación.

Fuentes: [página principal de Rate Cloud](https://rate-cloud.com/) y [cómo funciona](https://rate-cloud.com/how-it-works). Consulta de fuentes: 3 de noviembre de 2026. [Volver al índice](../README.md).
