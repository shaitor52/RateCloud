# Privacy, data handling, and availability

English · [Русский](../ru/articles/06-privacy-and-reliability.md)

Rate Cloud's public architecture distinguishes request content, temporary computation state, operational metadata, and account or payment records. These categories serve different purposes and have different retention rules. This article summarizes the published policy and design rather than an independent security audit.

## Request content and temporary buffers

The service states that it does not create a permanent history of prompt and response texts and does not train models on user data. Request content is processed in temporary memory. The documented cleanup targets for accessible, managed application buffers are up to five seconds after successful delivery and up to thirty seconds after a final error, cancellation, or disconnected connection.

These application-buffer targets should not be generalized into a claim that every physical copy on every accelerator is provably erased within those exact times. The public architecture acknowledges a separate trust boundary for rented hardware.

## Isolated computational cache

A computational KV cache has a separate lifetime: up to five minutes without reuse and a maximum absolute age of fifteen minutes. Expired entries become ineligible for new cache hits. An operation already using an entry may finish within its deadline; memory is cleared after the last reference is released.

The documented cache is not persisted to disk or included in snapshots. Compatibility includes the account, model, weight revision, quantization, tokenizer, conversation template, and system instructions. The index is HMAC-protected, and a user cannot select another account's cache area. A project policy can specify a profile without cross-request caching.

Client-side history is separate. An editor, agent, bot, or application may keep its own conversations and files according to its own settings.

## Operational metadata

The public architecture describes metadata including identifiers, model and profile, timestamps, durations, usage, slot state, and error codes, with detailed records removed after thirty days. Those records exclude prompts, responses, tool arguments, files, and authorization tokens. Account, payment, and voluntarily submitted support information have separate purposes and retention rules.

“No permanent prompt history” does not mean “no account or operational records.” Consult the current privacy policy linked from the website for the applicable legal details.

## Transport and infrastructure boundaries

The architecture describes TLS for external transport, identity checks and mTLS between services, access on a service-need basis, and separation of keys, accounts, projects, and cache scopes. API secrets and request bodies are excluded from logs and backups under the documented rules.

Protected transport and hardware-protected computation are different guarantees. The site does not promise confidential-computing protection on every accelerator. A node that loses trusted management is excluded, its authority is revoked, and its return requires verification and cleanup.

## Availability and interrupted work

Continuous 24/7 availability of every model is not guaranteed. Recovery may retry an operation on a compatible replica before output begins, within the original deadline. It can add latency. Once a stream has begun, interruption must remain visible as an incomplete operation rather than a falsely completed response.

The published compensation rule applies to a complete continuous system outage lasting more than four hours with HTTP 503 responses. It provides extensions of twelve hours for a three-day subscription, one day for a seven-day subscription, and three days for a thirty-day subscription. Individual model failures, slow responses, concurrency limits, and other error codes are not covered by that specific rule. The applicable terms and mandatory user rights remain controlling.

When reporting an incident, provide the time and operation identifiers. Do not send API secrets or confidential request content.

Source: [Rate Cloud: data handling, security, and availability](https://rate-cloud.com/how-it-works). Refer to the current terms and privacy policy linked from [the official website](https://rate-cloud.com/). Snapshot: November 3, 2026. [Back to overview](../README.md).
