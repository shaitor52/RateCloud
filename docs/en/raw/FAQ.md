# Rate Cloud: frequently asked questions

[English](FAQ.md) · [Русский](ru/FAQ.md) · [Overview](README.md)

Product information reflects the official website on November 3, 2026. Check the live dashboard and terms before purchasing.

## What is Rate Cloud?

Rate Cloud provides subscription API access to GLM, DeepSeek, and Qwen for development, AI agents, automation, and applications. A subscription selects a model and an access period rather than billing each million tokens. See [the service overview](articles/01-about-rate-cloud.md).

## Is there a token limit?

There is no cumulative input or output token quota during an active subscription. A single operation still has finite context capacity, a deadline, and technical constraints. Actual processing volume depends on speed, input and output lengths, available slots, and service availability.

## Does four slots mean only four requests?

No. A paid subscription allows four requests to run at the same time. Completed requests free their slots for new work. Several API keys on the same account use the relevant model's shared slot pool.

## Can I add more parallel capacity?

The public offer allows combining subscriptions. Two subscriptions to the same model provide eight slots for that model. Different model subscriptions provide their own model-specific pools.

## Which models can I use?

The published catalog lists GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro, and Qwen 3.8 Max. See [the dated catalog](articles/02-models.md) for exact API IDs, prices, positioning, and image-input support.

## Is a Flash model the same as a Pro model?

No. They are distinct catalog entries. Precision profiles are execution variants of the selected model; they are not permission to substitute another model silently. See [routing and quantization](articles/03-routing-and-quantization.md).

## How does intelligent routing choose a precision profile?

The published design checks task requirements and eligible replicas, prioritizes quality for difficult or uncertain work, and considers cost only among suitable routes. Context, images, tools, output format, available memory, queues, and replica health influence eligibility. Profile support depends on the specific model and hardware.

## Does quantization guarantee identical answers?

No. Numerical precision can affect output quality. The public architecture describes validation against the source release and task-specific quality gates. An economical profile is eligible only where its quality is suitable. Quantization is separate from reasoning-effort settings.

## Which applications can connect?

The official guide covers OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes, and other compatible clients. Our [practical guides](guides/README.md) cover selected setups. Client and model support determine available features; connecting a client does not change the selected model into a first-party model from the client's vendor.

## What base URL should my application use?

The general OpenAI-compatible base URL is `https://llm.rate-cloud.com/v1`. Dedicated compatibility URLs exist for particular clients. Use the [official documentation](https://rate-cloud.com/docs) and the matching guide rather than mixing endpoint families.

## Why can a listed model reject my request?

Catalog visibility does not establish execution access. Check an active trial or subscription, key model permissions, expiry, IP restrictions, and client compatibility settings. Also check occupied slots and the returned error. Share the time and request identifier with support without sending the key or private content.

## How fast is Rate Cloud?

The website publishes a historical performance table. It measures complete-request latency and effective token rates including waiting. Your task can differ. See [performance and methodology](articles/04-performance.md); the figures are not a guaranteed SLA or controlled identical-prompt benchmark.

## Are prompts used to train models?

The service states that user data is not used to train models and that no permanent prompt-and-response text history is created. Temporary processing, isolated computational cache, operational metadata, and account records are separate categories. See [privacy and reliability](articles/06-privacy-and-reliability.md) and the current privacy policy linked from the website.

## Is every model guaranteed to be available 24/7?

No. The site expressly does not guarantee continuous availability of every model. The published compensation rule covers a specific complete system outage condition, not every slow request or individual model error. Consult the applicable terms.

## Can I test before paying?

The published introductory trial provides the first three hours with one concurrent slot after registration and email and Telegram verification. Confirm your trial status in the dashboard.

## Can I sell subscriptions under my own brand?

Rate Cloud offers White Label services with branding, a site and dashboard, payments, and technical infrastructure. See [the White Label article](articles/07-white-label.md) and [current official offer](https://rate-cloud.com/white-label).

Sources: [homepage](https://rate-cloud.com/), [how it works](https://rate-cloud.com/how-it-works), and [API guide](https://rate-cloud.com/docs).
