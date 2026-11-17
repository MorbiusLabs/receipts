#!/usr/bin/env python3
"""Recompute the November 2026 numbers from our "Is the Anthropic IPO draining crypto?" post.

    python3 november_moves.py

- US spot Bitcoin ETF flows: daily totals from farside.co.uk/bitcoin-etf-flow-all-data
  (copied below, because Farside blocks automated requests; compare them by eye).
- Bitcoin: public CoinGecko market_chart endpoint, daily points.
- Nvidia and the Nasdaq Composite: public Yahoo Finance chart endpoint, daily closes.
No dependencies, no API key.
"""
import json
import urllib.request
from datetime import date, datetime, timezone

# Farside "Total" column, US$ millions. Nov 16 uses Farside's final figure (+7.9), corrected on Nov 17.
FARSIDE = {
    "2026-11-02": -398.6, "2026-11-03": -115.6, "2026-11-04": 74.6, "2026-11-05": -430.2,
    "2026-11-06": -411.9, "2026-11-09": -201.0, "2026-11-10": -95.0, "2026-11-11": -299.8,
    "2026-11-12": -284.1, "2026-11-13": -185.4, "2026-11-16": 7.9,
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (receipts-script)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())


def day(ts):
    return datetime.fromtimestamp(ts, timezone.utc).date()


def yahoo(symbol):
    p1 = int(datetime(2026, 10, 28, tzinfo=timezone.utc).timestamp())
    p2 = int(datetime(2026, 11, 18, tzinfo=timezone.utc).timestamp())
    r = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={p1}&period2={p2}&interval=1d")["chart"]["result"][0]
    return {day(t): c for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c}


def pct(a, b):
    return (b / a - 1) * 100


def main():
    total = sum(FARSIDE.values())
    best, run, start = (0, None, None), 0, None
    for d in sorted(FARSIDE):
        if FARSIDE[d] < 0:
            run, start = run + 1, start or d
            if run > best[0]:
                best = (run, start, d)
        else:
            run, start = 0, None
    print(f"ETF flows Nov 2-16: {total:,.1f} $M, longest outflow streak: {best[0]} sessions ({best[1]} to {best[2]})")

    btc = get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=60&interval=daily")["prices"]
    nov1 = next(p for t, p in btc if day(t / 1000) == date(2026, 11, 1))
    print(f"Bitcoin  Nov 1 -> latest: {pct(nov1, btc[-1][1]):.1f}%   (${nov1:,.0f} -> ${btc[-1][1]:,.0f})")

    oct30, nov4, nov5, nov16 = date(2026, 10, 30), date(2026, 11, 4), date(2026, 11, 5), date(2026, 11, 16)
    nv = yahoo("NVDA")
    print(f"Nvidia   Oct 30 -> Nov 16: {pct(nv[oct30], nv[nov16]):.1f}%   (${nv[oct30]:.2f} -> ${nv[nov16]:.2f})")
    nq = yahoo("%5EIXIC")
    print(f"Nasdaq   Oct 30 -> Nov 16: {pct(nq[oct30], nq[nov16]):.1f}%   Nov 5 alone: {pct(nq[nov4], nq[nov5]):.1f}%")


if __name__ == "__main__":
    main()
