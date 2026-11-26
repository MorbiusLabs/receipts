# ANT traded back above $83 on Nov 25, then closed at $82.79, below the IPO price for a second day

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-26-ant-above-83-intraday-only/) · **Checked:** 2026-11-26 · **Status:** all prices are Nasdaq's end-of-day record; the reasons for the rebound are not checked

Anthropic's fifth trading day, Wednesday Nov 25. At 3:05 p.m. ET, 24/7 Wall St. ran the headline "ANT Stock Reclaims $83 IPO Price". The stock closed under it. Day four is on our [first-close-below page](https://morbiuslabs.org/p/2026-11-25-ant-closes-below-ipo/).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | ANT reclaimed its $83 IPO price on Nov 25 | **FALSE** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/ant/historical), Nov 25: close $82.79, 0.25% below $83. The [24/7 Wall St. headline](https://247wallst.com/investing/2026/11/25/anthropics-sharp-reversal-up-4-ant-stock-reclaims-83-ipo-price-after-early-8-drop-coreweave-slides-2-iren-holds-steady/) was written in afternoon trading, at "$84.50" |
| 2 | It traded above $83 during the day | **REAL** | Nasdaq: the day's high was $85.92, 3.5% above $83 |
| 3 | It closed below $83 for a second straight day | **REAL** | Nasdaq closes: $81.905 (Nov 24), $82.79 (Nov 25) |
| 4 | It set a new low | **REAL** | Nasdaq: the day's low was $73.85, 11.0% below $83 and under the Nov 24 low of $75.61 |
| 5 | It finished the day up | **REAL** | Nasdaq: $82.79 against $81.905, up $0.885 or 1.08%. Volume 293.7 million shares |
| 6 | IPO buyers are back in profit | **FALSE** | At the Nov 25 close, 980 million IPO shares × ($82.79 − $83) = −$206 million on paper, assuming every share is still held |
| 7 | Analyst calls and ARK's buying drove the rebound | **OUR READ** | 24/7 Wall St. credits them. Price data shows the stock moved, not why, and we did not check those reports |

## Reproduce

```python
ipo, prev, close = 83, 81.905, 82.79
high, low = 85.92, 73.85
print(round((close / ipo - 1) * 100, 2))        # -0.25
print(round((high / ipo - 1) * 100, 2))         # 3.52
print(round((low / ipo - 1) * 100, 2))          # -11.02
print(round((close / prev - 1) * 100, 2))       # 1.08
print(round(980e6 * (close - ipo) / 1e6))       # -206 (million)
```

## What would change this page

A correction to Nasdaq's Nov 25 record.

## Corrections

None so far. If you find an error, open an issue with the source.
