# Nuestra infraestructura: alquilamos capacidad, desplegamos modelos y operamos la inferencia

[English](../../articles/10-infrastructure.md) · [Русский](../../ru/articles/10-infrastructure.md) · Español · [Português](../../pt/articles/10-infrastructure.md)

**Rate Cloud alquila capacidad de cómputo empresarial, despliega los pesos de los modelos y gestiona su ejecución.** Nuestro trabajo abarca la infraestructura y el flujo de inferencia: elegir hardware y entornos de ejecución compatibles, preparar perfiles de modelo, poner réplicas en servicio, enrutar solicitudes y gestionar la recuperación.

Los clientes eligen un modelo y conectan sus herramientas mediante la API. Rate Cloud opera la capa computacional que hace posible ese acceso. El hardware se alquila a empresas propietarias; la propiedad del equipo alquilado y las responsabilidades operativas del entorno que ejecuta los modelos son distintas.

## Qué gestiona Rate Cloud

| Área | Nuestro trabajo |
| --- | --- |
| Capacidad de cómputo | Alquilar capacidad empresarial y combinar una reserva estable con recursos adicionales disponibles |
| Despliegue de modelos | Ubicar pesos de modelo compatibles y preparar el motor de inferencia para la versión seleccionada |
| Perfiles de precisión | Validar perfiles aptos del formato original, de precisión mixta o cuantizados para el mismo modelo |
| Preparación de réplicas | Cargar los pesos, calentar la ejecución, comprobar la disponibilidad y admitir solo réplicas adecuadas |
| Enrutamiento de solicitudes | Ajustar el contexto, las imágenes, las herramientas, el formato de salida, la memoria, la cola y el estado de las réplicas |
| Operación y recuperación | Supervisar la ejecución, retirar réplicas defectuosas y, cuando sea posible, recuperarse dentro del plazo original de la operación |

Por eso la descripción del servicio abarca la ubicación de pesos, los entornos de inferencia, la precisión y el ciclo de vida de las réplicas, además del endpoint de API. Estas responsabilidades operativas son centrales en la arquitectura pública.

## Familias de hardware de la arquitectura publicada

La arquitectura menciona sistemas Huawei Atlas y aceleradores Ascend. Son descripciones públicas de plataformas, no un inventario en directo de cada máquina ni una promesa de que todos los modelos funcionen en todos los dispositivos enumerados.

| Plataforma | Función publicada |
| --- | --- |
| Atlas 800I A2 | Inferencia de modelos grandes; ocho NPU de 64 GB cada una |
| Atlas 800I A3 | Inferencia de modelos grandes; ocho NPU físicas de 128 GB cada una, presentadas como dieciséis dispositivos lógicos |
| Atlas 900 A2 PoD y A3 SuperPoD | Grupos de aceleradores distribuidos para ejecutar modelos grandes |
| Atlas 500 y 500 A2 | Tareas de servicio más pequeñas |
| Atlas 800 con Atlas 300I Duo | Clase de compatibilidad independiente, que se evalúa por separado |

Las descripciones físicas y lógicas del A3 se refieren a la misma memoria y no deben sumarse. La compatibilidad se comprueba para cada combinación de modelo, formato de pesos, motor y hardware. Los cálculos estrechamente acoplados usan una red local compatible; mover solicitudes completas entre sitios es una operación distinta.

## De los pesos del modelo a una API utilizable

Una réplica debe contar con la versión correcta y un entorno de ejecución compatible, memoria suficiente, funciones permitidas, calentamiento completado y una comprobación de disponibilidad satisfactoria. Tener hardware libre no significa que haya un modelo disponible.

El enrutador selecciona un perfil validado adecuado del modelo solicitado por el usuario. Se prioriza la calidad para código difícil, matemáticas, herramientas, esquemas estrictos y solicitudes inciertas. Flash y Pro siguen siendo modelos distintos. Consulta [enrutamiento y cuantización](03-routing-and-quantization.md) para conocer el proceso de selección.

Los grupos estables sostienen la carga base y la recuperación. Los recursos interrumpibles adicionales amplían la capacidad disponible. Un aviso de revocación de recursos detiene nuevas asignaciones a la réplica afectada. Antes de la salida, la recuperación puede reintentar en una réplica compatible dentro del plazo original. Una transmisión interrumpida debe seguir apareciendo como incompleta.

## Por qué esto permite el acceso por suscripción

Gestionar conjuntamente capacidad de cómputo, perfiles de modelo y enrutamiento permite a Rate Cloud controlar cómo se usan los recursos adecuados. Los clientes pagan por el acceso al modelo y la concurrencia durante un periodo de suscripción, sin una cuota acumulada de tokens. El procesamiento sigue limitado por la velocidad del modelo, el contexto, los plazos de operación, los espacios y la disponibilidad; esto no garantiza un volumen mensual fijo ni un servicio ininterrumpido 24/7.

Este artículo describe el modelo operativo público y las responsabilidades que asume Rate Cloud. No afirma que cada solicitud use una sola ruta de ejecución exclusiva ni certifica el inventario actual de equipos. La arquitectura y las condiciones oficiales vigentes siguen siendo la referencia.

## Explora el servicio

[Crea una cuenta y prueba Rate Cloud](https://rate-cloud.com/register). La prueba estándar de tres horas requiere verificar el correo electrónico y vincular Telegram, y usa un espacio simultáneo. Consulta [las ventajas por invitación](11-referral-program.md) para conocer las condiciones distintas de las invitaciones válidas.

¿Ya tienes cuenta? [Abre las instrucciones de conexión](https://rate-cloud.com/user/instructions). ¿Quieres crear un servicio con tu marca? [Explora White Label](https://rate-cloud.com/en/white-label).

Fuentes, consultadas el 3 de noviembre de 2026: [cómo funciona Rate Cloud](https://rate-cloud.com/how-it-works), [condiciones del servicio](https://rate-cloud.com/offer) y [acceso a modelos](https://rate-cloud.com/). [Volver a la documentación](../README.md).
