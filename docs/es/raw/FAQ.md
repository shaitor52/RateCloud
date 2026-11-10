# Rate Cloud: preguntas frecuentes

[English](../FAQ.md) · [Русский](../ru/FAQ.md) · Español · [Inicio](README.md)

La información del producto refleja el sitio oficial del 3 de noviembre de 2026. Antes de comprar, consulta el panel y las condiciones vigentes.

## ¿Qué es Rate Cloud?

Rate Cloud ofrece acceso por suscripción a las API de GLM, DeepSeek y Qwen para desarrollo, agentes de IA, automatización y aplicaciones. La suscripción selecciona un modelo y un periodo de acceso, en lugar de cobrar por cada millón de tokens. Consulta [la descripción del servicio](articles/01-about-rate-cloud.md).

## ¿Hay un límite de tokens?

Durante una suscripción activa no hay una cuota acumulada de tokens de entrada o salida. Cada operación sigue teniendo una capacidad finita de contexto, un plazo y limitaciones técnicas. El volumen real de procesamiento depende de la velocidad, las longitudes de entrada y salida, los espacios disponibles y la disponibilidad del servicio.

## ¿Cuatro espacios significan solo cuatro solicitudes?

No. Una suscripción de pago permite ejecutar cuatro solicitudes al mismo tiempo. Cuando una termina, libera su espacio para otro trabajo. Varias claves de API de la misma cuenta usan el conjunto compartido del modelo correspondiente.

## ¿Cuál es el límite de solicitudes por minuto?

La cuenta puede iniciar 20 solicitudes nuevas a LLM en cualquier ventana móvil de 60 segundos. El límite se comparte entre todos los modelos, claves API, suscripciones, paquetes Full model y ambos orígenes del servicio. Las suscripciones y paquetes Full model adicionales aumentan los espacios simultáneos, pero no el límite de solicitudes por minuto. Una respuesta 429 por límite de frecuencia significa que la cuenta alcanzó su cupo en la ventana móvil; una respuesta 429 por límite de espacios significa que todos los espacios simultáneos aplicables están ocupados. Son límites distintos.

## ¿Puedo añadir más capacidad paralela?

La oferta pública permite combinar suscripciones. Dos suscripciones al mismo modelo ofrecen ocho espacios para ese modelo. Las suscripciones a modelos distintos tienen conjuntos propios.

## ¿Qué modelos puedo usar?

El catálogo publicado incluye GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro y Qwen 3.8 Max. Consulta [el catálogo fechado](articles/02-models.md) para ver los ID exactos de API, precios, usos previstos y compatibilidad con imágenes.

## ¿Un modelo Flash es igual que uno Pro?

No. Son entradas distintas del catálogo. Los perfiles de precisión son variantes de ejecución del modelo seleccionado; no autorizan a sustituir silenciosamente el modelo por otro. Consulta [enrutamiento y cuantización](articles/03-routing-and-quantization.md).

## ¿Cómo elige el enrutamiento inteligente un perfil de precisión?

El diseño publicado comprueba los requisitos de la tarea y las réplicas aptas, prioriza la calidad para trabajos difíciles o inciertos y considera el coste solo entre las rutas adecuadas. La elegibilidad depende del contexto, las imágenes, las herramientas, el formato de salida, la memoria disponible, las colas y el estado de la réplica. La compatibilidad de cada perfil depende del modelo y el hardware concretos.

## ¿La cuantización garantiza respuestas idénticas?

No. La precisión numérica puede afectar la calidad de salida. La arquitectura pública describe una validación frente a la versión de origen y controles de calidad específicos por tarea. Un perfil económico solo es apto cuando su calidad resulta adecuada. La cuantización es independiente de los ajustes de esfuerzo de razonamiento.

## ¿Qué aplicaciones se pueden conectar?

La guía oficial cubre OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes y otros clientes compatibles. Nuestras [guías prácticas](guides/README.md) cubren algunas configuraciones. Las funciones disponibles dependen del cliente y del modelo; conectarlo no convierte el modelo seleccionado en un modelo propio del proveedor del cliente.

## ¿Qué URL base debe usar mi aplicación?

La URL base general compatible con OpenAI es `https://llm.rate-cloud.com/v1`. Algunos clientes tienen URL de compatibilidad dedicadas. Usa la [documentación oficial](https://rate-cloud.com/docs) y la guía correspondiente, sin mezclar familias de endpoints.

## ¿Por qué se rechaza una solicitud aunque el modelo aparezca en la lista?

La presencia en el catálogo no confirma el acceso de ejecución. Comprueba que haya una prueba o suscripción activa, los permisos de modelo de la clave, su caducidad, las restricciones de IP y los ajustes de compatibilidad del cliente. Revisa también los espacios ocupados y el error recibido. Comparte con soporte la hora y el identificador de solicitud, sin enviar la clave ni contenido privado.

## ¿Qué velocidad tiene Rate Cloud?

La tabla actual muestra por separado el tiempo hasta el primer texto y la velocidad de generación, comunicados por el propietario el 9 de noviembre de 2026, además del contexto aproximado. Consulta [rendimiento y metodología](articles/04-performance.md). No son garantías ni comparaciones controladas con solicitudes idénticas.

## ¿Se usan los prompts para entrenar modelos?

El servicio declara que los datos de usuarios no se usan para entrenar modelos y que no se crea un historial permanente del texto de prompts y respuestas. El procesamiento temporal, la caché de cálculo aislada, los metadatos operativos y los datos de cuenta son categorías separadas. Consulta [privacidad y disponibilidad](articles/06-privacy-and-reliability.md) y la política de privacidad vigente enlazada desde el sitio.

## ¿Se garantiza que todos los modelos estén disponibles 24/7?

No. El sitio indica expresamente que no se garantiza la disponibilidad continua de cada modelo. La regla de compensación publicada cubre una condición específica de interrupción total del sistema, no toda respuesta lenta ni todo error de un modelo concreto. Consulta las condiciones aplicables.

## ¿Puedo probarlo antes de pagar?

La prueba estándar publicada ofrece las primeras tres horas con un espacio simultáneo después del registro, la verificación del correo electrónico y la vinculación de Telegram. [Regístrate aquí](https://rate-cloud.com/register) y confirma el estado de la prueba en el panel. Una invitación personal válida puede ofrecer a una cuenta nueva cinco horas de prueba y un 10 % de descuento en la primera suscripción, según las [condiciones de referidos](articles/11-referral-program.md).

## ¿Qué infraestructura opera Rate Cloud?

Rate Cloud alquila capacidad de cómputo empresarial, despliega los pesos de modelos, prepara perfiles de precisión, comprueba réplicas y enruta las solicitudes. La lista publicada de hardware es una descripción de plataformas, no un inventario en directo ni una garantía de que cada modelo se ejecute en cada dispositivo. Consulta [la arquitectura de infraestructura](articles/10-infrastructure.md).

## ¿Puedo vender suscripciones con mi propia marca?

Rate Cloud ofrece servicios White Label con marca propia, sitio y panel, pagos e infraestructura técnica. Consulta [el artículo White Label](articles/07-white-label.md) y [la oferta oficial actual](https://rate-cloud.com/white-label). White Label es distinto del programa de referidos y sus ventajas no se acumulan automáticamente.

## ¿Cómo funciona el programa de referidos?

Una invitación personal válida da a una cuenta nueva cinco horas de prueba y un 10 % de descuento en la primera compra de una suscripción. Las bonificaciones publicadas para quien recomienda son 10 %, 3 % y 1 % en tres niveles, sobre pagos elegibles. No hay pago por el registro solamente; se aplican un periodo pendiente de 14 días, atribución del primer enlace válido y un mínimo de retiro equivalente a USD 30. Consulta [las condiciones completas](articles/11-referral-program.md). Usa el enlace personal real antes de registrarte; el enlace general de registro no asigna un referido.

Fuentes: [página principal](https://rate-cloud.com/), [cómo funciona](https://rate-cloud.com/how-it-works) y [guía de API](https://rate-cloud.com/docs).

## Full model

Full model reúne los cinco modelos actuales: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro y Qwen 3.8 Max. Un paquete cuesta $45.45 por 30 días, $22.72 por 7 días o $13.63 por 3 días. Un código promocional del 10% reduce los importes a $40.90, $20.45 y $12.27, según la conversión pública del 3 de noviembre de 2026. Confirma el total del pedido antes de pagar. Cada paquete añade un espacio simultáneo a cada modelo. Las cantidades se acumulan por igual en todos los modelos y no se pueden reasignar: dos paquetes permiten dos solicitudes simultáneas por modelo. Una compra adicional añade espacios durante su periodo pagado. Renovar la cantidad elegida amplía el periodo sin cambiar los espacios. Las suscripciones individuales añaden capacidad independiente. La primera compra sigue las reglas normales de códigos promocionales, recomendación y bonos. La renovación manual es un nuevo pedido y puede usar códigos promocionales o bonos si la cuenta cumple las reglas habituales de elegibilidad. La renovación automática a través de Whop se cobra al precio total acordado, sin repetir el descuento inicial.
