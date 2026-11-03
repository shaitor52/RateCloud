# Our infrastructure: we lease compute, deploy models, and operate inference

English · [Русский](../ru/articles/10-infrastructure.md)

**Rate Cloud leases enterprise computing capacity, deploys model weights, and manages model execution.** Our role covers the infrastructure and inference workflow: choosing compatible hardware and runtimes, preparing model profiles, bringing replicas into service, routing requests, and handling recovery.

Customers choose a model and connect their tools through the API. Rate Cloud operates the computational layer behind that access. Hardware is rented from enterprise owners; rented equipment and the model-running environment have different ownership and operational responsibilities.

## What Rate Cloud manages

| Area | Our work |
| --- | --- |
| Computing capacity | Lease enterprise capacity and combine a stable reserve with additional available resources |
| Model deployment | Place compatible model weights and prepare the inference engine for the selected release |
| Precision profiles | Validate eligible original, mixed-precision, or quantized profiles of the same model |
| Replica readiness | Load weights, warm up execution, check readiness, and admit only suitable replicas |
| Request routing | Match context, images, tools, output format, memory, queue state, and replica health |
| Operation and recovery | Monitor execution, retire unhealthy replicas, and recover within the original operation deadline where possible |

This is why the service description covers weight placement, inference runtimes, precision, and replica lifecycle as well as an API endpoint. Those operational responsibilities are central to the public architecture.

## The hardware families in the published architecture

The architecture names Huawei Atlas systems and Ascend accelerators. These are published platform descriptions, not a live inventory of every machine or a promise that every model runs on every listed device.

| Platform | Published role |
| --- | --- |
| Atlas 800I A2 | Large-model inference; eight NPUs with 64 GB each |
| Atlas 800I A3 | Large-model inference; eight physical NPUs with 128 GB each, presented as sixteen logical devices |
| Atlas 900 A2 PoD and A3 SuperPoD | Distributed accelerator groups for large-model execution |
| Atlas 500 and 500 A2 | Smaller service tasks |
| Atlas 800 with Atlas 300I Duo | A separate compatibility class, evaluated independently |

The physical and logical descriptions of A3 refer to the same memory and must not be added together. Compatibility is checked for each model, weight format, engine, and hardware combination. Tightly coupled computation uses a compatible local network; moving whole requests between sites is a separate operation.

## From model weights to a usable API

A model replica must have the right release and compatible runtime, sufficient memory, permitted features, completed warmup, and a successful readiness check. Free hardware by itself is not an available model.

The router selects a suitable validated profile of the model requested by the user. Quality takes priority for difficult code, mathematics, tools, strict schemas, and uncertain requests. Flash and Pro remain distinct models. See [routing and quantization](03-routing-and-quantization.md) for the selection process.

Stable groups support the baseline and recovery. Additional interruptible resources expand available capacity. A resource-revocation warning stops new assignments to the affected replica. Recovery before output may retry on a compatible replica within the original deadline. An interrupted stream must remain visibly incomplete.

## Why this supports subscription access

Operating compute capacity, model profiles, and routing together gives Rate Cloud control over how suitable resources are used. Customers pay for model access and concurrency during a subscription period without a cumulative token quota. Processing remains bounded by model speed, context, operation deadlines, slots, and availability; this does not guarantee a fixed monthly volume or uninterrupted 24/7 service.

This article describes the public operating model and the responsibilities Rate Cloud takes on. It does not assert that every request uses a single exclusive execution path or certify a current fleet inventory. The current official architecture and terms remain the reference.

## Explore the service

[Create an account and try Rate Cloud](https://rate-cloud.com/register). The standard three-hour trial requires email and Telegram verification and uses one concurrent slot. See [referral benefits](11-referral-program.md) for the separate conditions of eligible invitations.

Already have an account? [Open the connection instructions](https://rate-cloud.com/user/instructions). Want to build your own branded service? [Explore White Label](https://rate-cloud.com/en/white-label).

Sources, checked November 3, 2026: [how Rate Cloud works](https://rate-cloud.com/how-it-works), [service terms](https://rate-cloud.com/offer), and [model access](https://rate-cloud.com/). [Back to documentation](../README.md).
