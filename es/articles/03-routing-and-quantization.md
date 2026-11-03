# Cómo funcionan el enrutamiento inteligente y la cuantización

La arquitectura pública de Rate Cloud describe una combinación de capacidad informática estable, capacidad empresarial adicional disponible, perfiles de precisión aprobados para modelos y enrutamiento que tiene en cuenta cada solicitud. El objetivo es usar los recursos de manera eficiente y conservar la identidad y los requisitos funcionales del modelo seleccionado.

Este artículo explica la arquitectura publicada. No es una verificación independiente de cada despliegue de producción ni una promesa de que toda combinación de hardware y precisión esté siempre disponible.

## Capacidad informática y réplicas del modelo

El servicio describe el alquiler de capacidad libre de propietarios de clústeres empresariales, junto con una reserva estable. Rate Cloud gestiona la ubicación de los pesos del modelo, los motores de inferencia, los perfiles de precisión y la distribución de solicitudes.

La arquitectura menciona sistemas Huawei Atlas y aceleradores Ascend, incluidos Atlas 800I A2 y A3 para modelos grandes, y Atlas 900 A2 PoD y A3 SuperPoD para grupos distribuidos. La compatibilidad de hardware se evalúa para cada modelo. Trasladar una solicitud entre sitios no es lo mismo que dividir cálculos estrechamente acoplados de un modelo entre sitios arbitrarios: los cálculos de una réplica que están estrechamente acoplados utilizan una red local compatible.

Una réplica utilizable necesita más que memoria disponible. Debe contar con pesos compatibles, soporte del entorno de ejecución y de las funciones de API requeridas, estado cargado, calentamiento y una comprobación de disponibilidad satisfactoria.

## Qué cambia la cuantización

Los parámetros del modelo y los cálculos intermedios pueden usar distintos formatos numéricos. Los formatos más compactos reducen los requisitos de memoria y pueden cambiar la eficiencia de ejecución, pero también pueden afectar la calidad de la salida. Por ello, la precisión reducida debe evaluarse respecto a la versión de origen pertinente y los tipos de tarea.

El diseño publicado usa perfiles de calidad, equilibrado y económico de un mismo modelo. Un perfil de calidad puede usar el formato original validado, W8A8 u otra configuración aprobada. Un perfil equilibrado puede combinar componentes con distintas precisiones, como 4 y 8 bits. Un promedio efectivo cercano a 6 bits no implica una implementación INT6 universal. Los perfiles económicos pueden utilizar configuraciones W4A16, W4A8 o MXFP4 validadas cuando el modelo y el hardware las admiten.

La disponibilidad de un formato concreto depende de la versión del modelo, el hardware, el entorno de ejecución y las comprobaciones de calidad. No se ofrece indiscriminadamente para todos los modelos. Aumentar la precisión nominal de unos pesos ya cuantizados no recupera la información perdida en una cuantización anterior.

## Controles de calidad antes del enrutamiento

Los perfiles se evalúan frente a la versión exacta del modelo de origen mediante tareas públicas, sintéticas y preparadas específicamente sobre código, matemáticas, contexto largo, herramientas y JSON estricto. El proceso publicado considera la calidad de las respuestas, el consumo de memoria, la velocidad y el comportamiento de la API. Las conversaciones de usuarios no se usan para entrenar ni calibrar los modelos.

Un perfil compacto solo es apto para tareas que puede resolver adecuadamente. Para código difícil, matemáticas, flujos con herramientas, esquemas estrictos y solicitudes inciertas se prioriza la calidad. Una instrucción corta también puede describir un problema difícil. Cambiar `reasoning_effort` es un control independiente y no debe presentarse como efecto de la cuantización.

## Cómo elige el enrutador

El enrutador tiene en cuenta los requisitos de contexto, imágenes, herramientas y formato de salida, la complejidad de la tarea, la memoria disponible, el estado de la cola y de la réplica, y el periodo restante de asignación de recursos. Primero determina las rutas adecuadas; después considera el coste entre esas opciones.

El modelo seleccionado permanece fijo. La operación también fija la revisión de pesos aplicable y las funciones permitidas. Los servidores incompatibles se excluyen antes de la asignación. Si no hay capacidad adecuada, el sistema puede esperar dentro de su presupuesto interno o devolver un error explícito de indisponibilidad temporal, en lugar de sustituir silenciosamente el modelo por otro.

## Ciclo de vida de una solicitud

1. Establecer la conexión protegida y validar la clave de API, la suscripción y un espacio disponible.
2. Determinar los requisitos de la solicitud y elegir un perfil apto del modelo solicitado.
3. Asignar una réplica lista y compatible e iniciar la ejecución.
4. Entregar la respuesta, liberar el espacio y borrar el contenido temporal según las reglas de tratamiento de datos.

Una operación lógica tiene un `request_id`; cada intento de cálculo tiene un `attempt_id`. Antes de que empiece la salida, la recuperación puede repetir el trabajo en una réplica compatible dentro del plazo total original. Esto puede aumentar la latencia.

Una vez iniciada la transmisión, no se debe unir el prefijo de una generación a la continuación de otra nueva. Una transmisión interrumpida está incompleta y el cliente debe tratarla como tal.

## Recursos estables e interrumpibles

Los grupos estables sostienen la carga base y la recuperación. Los grupos interrumpibles adicionales amplían la capacidad. Una réplica que recibe un aviso de revocación de recursos deja de aceptar operaciones nuevas. La pérdida de un acelerador crítico deja indisponible la réplica que depende de él. Los grupos de fallo independientes reducen el impacto de un único incidente, pero el diseño de recuperación no garantiza la disponibilidad continua de cada modelo.

Fuente: [Rate Cloud: cómo funciona](https://rate-cloud.com/how-it-works), consultado el 3 de noviembre de 2026. [Volver al índice](../README.md).
