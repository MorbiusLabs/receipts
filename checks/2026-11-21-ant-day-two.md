# ANT day two: down 8.5%, five cents from the IPO price at the low, still 7% above it at the close

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-21-ant-day-two/) · **Checked:** 2026-11-21 · **Status:** all claims sourced; prices are Nasdaq's end-of-day record

Anthropic's second trading day, Friday Nov 20. The day-one numbers are on [our first-day page](https://morbiuslabs.org/p/2026-11-20-ant-first-day/).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | ANT fell about 9% on its second day | **REAL** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/ant/historical), Nov 20: close $88.91 against $97.17, down 8.50%. [StockAnalysis](https://stockanalysis.com/stocks/ant/) shows the same close, "-8.26 (-8.50%)". Volume 400.5 million shares |
| 2 | It fell 9% at the open | **FALSE** | Nasdaq: open $89.86, down 7.52% from Thursday's close. The 8.5% drop is the close, not the open |
| 3 | ANT fell below its $83 IPO price | **FALSE** | Nasdaq: the day's low was $83.05, five cents above the IPO price. It closed at $88.91, 7.1% above it |
| 4 | Anthropic's IPO buyers made $14 billion | **FALSE** | True only at Thursday's close: 980 million IPO shares × ($97.17 − $83) = $13.89B. At Friday's close: × ($88.91 − $83) = $5.79B. Paper gains, assuming every share is still held |
| 5 | The stock is down about 20% from its first trade | **REAL** | $88.91 against the $111.50 first trade on Nov 19: down 20.3% |
| 6 | Anthropic is still worth more than a trillion dollars | **OUR READ** | At $88.91: $1.18 trillion on the 13,219,642,276 shares outstanding after the deal, $1.61 trillion fully diluted (both share counts from the 424B4, see the first-day page) |

## Reproduce

```python
close, prev, ipo, first, open_ = 88.91, 97.17, 83.00, 111.50, 89.86
print(round((close - prev) / prev * 100, 2), round((open_ - prev) / prev * 100, 2))   # -8.5 -7.52
print(round((close - ipo) / ipo * 100, 2), round((close - first) / first * 100, 2))   # 7.12 -20.26
print(round(980e6 * (97.17 - ipo) / 1e9, 2), round(980e6 * (close - ipo) / 1e9, 2))   # 13.89 5.79
print(round(13_219_642_276 * close / 1e12, 3), round(18_137_587_875 * close / 1e12, 3))  # 1.175 1.613
```

## Corrections

None so far. If you find an error, open an issue with the source.
