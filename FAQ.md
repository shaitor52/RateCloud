# Rate Cloud: frequently asked questions

[English](FAQ.md) · [Русский](ru/FAQ.md) · [Overview](README.md)

Product information reflects the official website on November 3, 2026. Check the live dashboard and terms before purchasing.

## What is Rate Cloud?

Rate Cloud provides subscription API access to GLM, DeepSeek, and Qwen for development, AI agents, automation, and applications. A subscription selects a model and an access period rather than billing each million tokens. See [the service overview](articles/01-about-rate-cloud.md).

## Is there a token limit?

There is no cumulative input or output token quota during an active subscription. A single operation still has finite context capacity, a deadline, and technical constraints. Actual processing volume depends on speed, input and output lengths, available slots, and service availability.

## Does four slots mean only four requests?

No. A paid subscription allows four requests to run at the same time. Completed requests free their slots for new work. Several API keys on the same account use the relevant model's shared slot pool.

## Is there a requests-per-minute limit?

Yes. The account may start 20 new LLM requests in any rolling 60-second window. This limit is shared across all models, API keys, subscriptions, Full model packages, and both service origins. Additional subscriptions and Full model packages add concurrent slots, not requests-per-minute capacity. A 429 rate-limit response means the account reached its rolling request allowance; a 429 slot-limit response means all applicable concurrent slots are occupied. These limits are separate.

## Can I add more parallel capacity?

The public offer allows combining subscriptions. Two subscriptions to the same model provide eight slots for that model. Different model subscriptions provide their own model-specific pools.

## Full model

Full model includes all five current models: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro, and Qwen 3.8 Max. One package costs $45.45 for 30 days, $22.72 for 7 days, or $13.63 for 3 days. A 10% code lowers those amounts to $40.90, $20.45, and $12.27, using the public display-currency snapshot dated November 3, 2026. Confirm the live order total before paying. Each package adds one concurrent slot to each of the five models. Package quantities stack equally across every model and cannot be reassigned: two packages provide two simultaneous requests per model. An additional purchase adds slots for its paid term. Renewal of the selected package quantity extends the term without changing slot counts. Individual model subscriptions add independent capacity. First-purchase promo, referral-discount, and bonus-credit rules apply. Manual renewals are new orders and may use promo codes or bonuses when the account meets the usual eligibility rules. Automatic renewal through Whop is charged at the full agreed price without repeating the introductory discount.

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

The public table reports separate owner-reported figures for time to first text and output generation speed, dated November 9, 2026, plus approximate context. See [performance and methodology](articles/04-performance.md). These are not guarantees or controlled comparisons on identical prompts.

## Are prompts used to train models?

The service states that user data is not used to train models and that no permanent prompt-and-response text history is created. Temporary processing, isolated computational cache, operational metadata, and account records are separate categories. See [privacy and reliability](articles/06-privacy-and-reliability.md) and the current privacy policy linked from the website.

## Is every model guaranteed to be available 24/7?

No. The site expressly does not guarantee continuous availability of every model. The published compensation rule covers a specific complete system outage condition, not every slow request or individual model error. Consult the applicable terms.

## Can I test before paying?

The published introductory trial provides the first three hours with one concurrent slot after registration and email and Telegram verification. Confirm your trial status in the dashboard.

## Can I sell subscriptions under my own brand?

Rate Cloud offers White Label services with branding, a site and dashboard, payments, and technical infrastructure. See [the White Label article](articles/07-white-label.md) and [current official offer](https://rate-cloud.com/white-label).

Sources: [homepage](https://rate-cloud.com/), [how it works](https://rate-cloud.com/how-it-works), and [API guide](https://rate-cloud.com/docs).

## Does Rate Cloud operate the models itself?

The published operating model covers leasing enterprise compute, placing model weights, and operating inference engines, replicas, precision profiles, and routing. See [our infrastructure](articles/10-infrastructure.md) for the hardware families and operational responsibilities. This describes the public architecture, not an exclusive-path guarantee for every request.

## What does the referral program offer?

A valid invitation for a new account provides five trial hours instead of three and 10% off the first subscription purchase, subject to verification and eligibility rules. The referrer can receive 10%, 3%, and 1% from qualifying payments along the three-step recommendation chain. Read [referral details](articles/11-referral-program.md) for attribution, payment exclusions, pending periods, and withdrawal rules.

[Register for the standard trial](https://rate-cloud.com/register) after checking the current terms. Email and Telegram verification are required and the standard trial uses one concurrent slot. If invited, use the actual personal invitation before registration. [White Label](articles/07-white-label.md) has separate partner terms.
