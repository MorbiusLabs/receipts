#!/usr/bin/env python3
"""Total USD stablecoin supply: the 30-day change to a date, and how it ranks since 2018.

Uses the public DefiLlama stablecoins API. No dependencies, no API key.

    python3 stablecoin_supply.py 2026-11-16

prints the 30-day change in total USD-pegged supply, the Tether and USDC parts,
and the largest 30-day drops on record (one per episode), in dollars and percent.
"""
import json
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone

API = "https://stablecoins.llama.fi"


def get(path):
    req = urllib.request.Request(API + path, headers={"User-Agent": "receipts-script"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def day(ts):
    return datetime.fromtimestamp(int(ts), timezone.utc).date()


def main():
    end = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.now(timezone.utc).date()
    start = end - timedelta(days=30)
    total = {day(x["date"]): x["totalCirculatingUSD"].get("peggedUSD", 0) for x in get("/stablecoincharts/all")}
    a, b = total[start], total[end]
    print(f"Total USD stablecoins  {start}: ${a/1e9:,.2f}B  {end}: ${b/1e9:,.2f}B  change: {(b-a)/1e9:+,.2f}B ({(b/a-1)*100:+.2f}%)")

    parts = 0
    for sid, name in ((1, "Tether"), (2, "USDC")):
        pts = {day(x["date"]): x["circulating"]["peggedUSD"] for x in get(f"/stablecoin/{sid}")["tokens"]}
        ch = pts[end] - pts[start]
        parts += ch
        print(f"{name:7s} {pts[start]/1e9:,.2f}B -> {pts[end]/1e9:,.2f}B  change: {ch/1e9:+,.2f}B")
    print(f"Tether + USDC = {parts/(b-a)*100:.0f}% of the total change")

    # every 30-day window in the history, worst first, one per episode (windows ending > 20 days apart)
    wins = []
    for d, v in total.items():
        p = total.get(d - timedelta(days=30))
        if p:
            wins.append((v - p, (v / p - 1) * 100, d))
    for label, key in (("dollars", 0), ("percent", 1)):
        print(f"\nLargest 30-day drops by {label}:")
        seen = []
        for w in sorted(wins, key=lambda x: x[key]):
            if all(abs((w[2] - s).days) > 20 for s in seen):
                seen.append(w[2])
                print(f"  window ending {w[2]}: {w[0]/1e9:+,.2f}B ({w[1]:+.2f}%)")
            if len(seen) == 5:
                break


if __name__ == "__main__":
    main()
