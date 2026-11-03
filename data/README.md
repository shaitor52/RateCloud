# Dated public data

- [Performance CSV](performance-2026-11-03.csv): all 15 numeric values from the public five-model table, retrieved November 3, 2026. Durations are complete-request seconds; rates are effective tokens/second including waiting. Fast response means the fastest decile. Raw observations, cohort size, and measurement interval were not published alongside the table. This is not a new benchmark or a live feed.
- [Pricing JSON](pricing-2026-11-03.json): dated official per-million-token text API prices and corresponding Rate Cloud 30-day subscription prices. Every provider row includes its source URL. The catalog is a selected comparison, not every vendor plan.
- [Offline calculator](../tools/compare_costs.py): 80% input / 20% output scenarios with dated USD subscription display prices and an optional input-cache-hit share. No network calls or credentials. Cache writes, tools, tax, batch rates, and special long-context tiers are excluded.

Use the [cost comparison](../articles/08-cost-and-service-comparison.md) for assumptions, applicability, and caveats. A cost scenario is not a promise that a subscription can process that volume within its term.
