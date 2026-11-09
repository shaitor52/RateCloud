# Dated public data

- [Subscription periods JSON](subscriptions-2026-11-03.json): USD display prices for each model for 3, 7 and 30 days. Three- and seven-day base prices were observed in Rate Cloud's public subscription dialog on November 3, 2026, then converted to USD using the dated public display-currency API rate. Thirty-day USD prices were retrieved from that public API. The file records source and conversion details. This is a dated display-price snapshot; confirm current prices before purchase.
- [Current performance CSV](performance-2026-11-09.csv): owner-reported time to first text, output generation speed, and approximate context, dated November 9, 2026. These are separate metrics and are not an independent controlled benchmark.
- [Historical performance CSV](performance-2026-11-03.csv): the earlier public-table snapshot is retained as historical data. Its older fields and values are not current performance guidance.
- [Pricing JSON](pricing-2026-11-03.json): dated official per-million-token text API prices and corresponding Rate Cloud 30-day subscription prices. Every provider row includes its source URL. The catalog is a selected comparison, not every vendor plan.
- [Offline calculator](../tools/compare_costs.py): 80% input / 20% output scenarios with dated USD subscription display prices and an optional input-cache-hit share. No network calls or credentials. Cache writes, tools, tax, batch rates, and special long-context tiers are excluded.

Use the [cost comparison](../articles/08-cost-and-service-comparison.md) for assumptions, applicability, and caveats. A cost scenario is not a promise that a subscription can process that volume within its term.
