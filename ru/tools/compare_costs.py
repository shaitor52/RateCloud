"""Reproduce dated text-token scenarios offline; does not call any API."""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def decimal_number(value):
    try:
        return Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError("Use a valid decimal number.") from error


def positive(value):
    number = decimal_number(value)
    if not number.is_finite() or number <= 0:
        raise argparse.ArgumentTypeError("Use a finite number greater than zero.")
    return number


def fraction(value):
    number = decimal_number(value)
    if not number.is_finite() or not 0 <= number <= 1:
        raise argparse.ArgumentTypeError("Use a number between 0 and 1.")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rub-per-usd", type=positive, required=True,
                        help="Your explicit exchange-rate assumption; not fetched live.")
    parser.add_argument("--million-tokens", type=positive, default=Decimal("500"))
    parser.add_argument("--cached-input-share", type=fraction, default=Decimal("0"),
                        help="Fraction of input tokens billed as cache hits; cache writes excluded.")
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1] / "data/pricing-2026-11-03.json"
    data = json.loads(path.read_text(), parse_float=Decimal)
    print(f"Snapshot {data['checked_date']}; 80% input / 20% output; "
          f"{args.million_tokens}M tokens; assumed RUB/USD {args.rub_per_usd}; "
          f"input cache-hit share {args.cached_input_share}.")
    print("Illustrative cost only. No throughput or quality equivalence is assumed.")
    for row in data["providers"]:
        effective_input = (Decimal(str(row["input_usd"])) * (1 - args.cached_input_share)
                           + Decimal(str(row["cached_input_usd"])) * args.cached_input_share)
        unit = Decimal("0.8") * effective_input + Decimal("0.2") * Decimal(str(row["output_usd"]))
        usd = args.million_tokens * unit
        print(f"{row['label']}: ${usd:.2f} = RUB {usd * args.rub_per_usd:.2f}")
        subscription = row["ratecloud_30_day_rub"]
        if subscription is not None:
            threshold = Decimal(subscription) / (args.rub_per_usd * unit)
            print(f"  Rate Cloud RUB {subscription}/30 days; break-even {threshold:.2f}M tokens.")
    print("Excludes taxes, tools, cache writes, batch and special/long-context rates.")


if __name__ == "__main__":
    main()
