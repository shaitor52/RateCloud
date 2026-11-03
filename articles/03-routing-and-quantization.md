# How intelligent routing and quantization work

English · [Русский](../ru/articles/03-routing-and-quantization.md)

Rate Cloud's public architecture describes a combination of stable compute capacity, additional available enterprise capacity, approved model precision profiles, and request-aware routing. The objective is to use resources efficiently while preserving the identity and functional requirements of the selected model.

This article explains the published architecture. It is not an independent verification of every production deployment or a promise that every hardware and precision combination is always available.

## Compute capacity and model replicas

The service describes renting spare capacity from enterprise cluster owners alongside a stable reserve. Rate Cloud manages model-weight placement, inference engines, precision profiles, and request distribution.

The architecture names Huawei Atlas systems and Ascend accelerators, including Atlas 800I A2 and A3 for large models and Atlas 900 A2 PoD and A3 SuperPoD for distributed groups. Hardware compatibility is evaluated for each model. Moving a request between sites differs from splitting tightly coupled model computation across arbitrary sites: a replica's tightly coupled computation uses a compatible local network.

A usable replica needs more than available memory. It must have compatible weights, runtime support, required API features, loaded state, warmup, and a successful readiness check.

## What quantization changes

Model parameters and intermediate calculations can use different numerical formats. More compact formats reduce memory requirements and can change execution efficiency, but they can also affect output quality. Lower precision therefore needs evaluation against the relevant source release and task types.

The published design uses quality, balanced, and economical profiles of the same model. A quality profile can use the validated original format, W8A8, or another approved configuration. A balanced profile can combine components at different precisions, such as 4 and 8 bits. An effective average near 6 bits does not imply a universal INT6 implementation. Economical profiles can use validated W4A16, W4A8, or MXFP4 configurations when the model and hardware support them.

The availability of a named format depends on the model release, hardware, runtime, and quality checks. It is not a format offered indiscriminately for every model. Increasing the nominal precision of already quantized weights does not restore information lost during earlier quantization.

## Quality gates before routing

Profiles are evaluated against the exact source model release on public, synthetic, and purpose-built tasks covering code, mathematics, long context, tools, and strict JSON. The published process considers answer quality, memory consumption, speed, and API behavior. User conversations are not used for model training or calibration.

A compact profile is eligible only for tasks it can handle adequately. Difficult code, mathematics, tool workflows, strict schemas, and uncertain requests prioritize quality. A short prompt can still describe a difficult problem. Changing `reasoning_effort` is a separate control and should not be presented as an effect of quantization.

## How the router chooses

The router considers context requirements, image inputs, tools, output format, task complexity, available memory, queue state, replica health, and the remaining resource allocation period. It first determines suitable routes; cost is considered among those suitable options.

The selected model remains fixed. The operation also fixes the applicable weight revision and allowed features. An incompatible server is excluded before assignment. If suitable capacity is unavailable, the system can wait within its internal budget or return an explicit temporary-unavailability error rather than silently substituting another model.

## The request lifecycle

1. Establish the protected connection and validate the API key, subscription, and available slot.
2. Determine the request's requirements and choose an eligible profile of the requested model.
3. Assign a ready, compatible replica and begin execution.
4. Deliver the response, release the slot, and clear temporary content under the data-handling rules.

A logical operation has a `request_id`; individual compute attempts have an `attempt_id`. Before output begins, recovery may retry on a compatible replica within the original overall deadline. Recovery can increase latency.

Once streaming has begun, the prefix of one generation must not be joined to a new generation's continuation. A broken stream is incomplete and must be handled as such by the client.

## Stable and interruptible resources

Stable groups support the baseline workload and recovery. Additional interruptible groups expand capacity. A replica receiving a resource-revocation warning stops taking new operations. Losing a critical accelerator makes its dependent replica unavailable. Independent failure groups reduce the impact of a single fault, but recovery design does not guarantee every model is continuously available.

Source: [Rate Cloud: how it works](https://rate-cloud.com/how-it-works), retrieved November 3, 2026. [Back to overview](../README.md).
