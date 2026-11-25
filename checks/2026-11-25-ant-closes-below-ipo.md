# ANT closed at $81.91 on Nov 24, its first close below the $83 IPO price

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-25-ant-closes-below-ipo/) · **Checked:** 2026-11-25 · **Status:** all prices are Nasdaq's end-of-day record; the cause of the drop is not checked

Anthropic's fourth trading day, Tuesday Nov 24. Days one and two are on our [first-day](https://morbiuslabs.org/p/2026-11-20-ant-first-day/) and [day-two](https://morbiuslabs.org/p/2026-11-21-ant-day-two/) pages.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | ANT closed below its $83 IPO price | **REAL** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/ant/historical), Nov 24: close $81.905, 1.3% below $83. [StockAnalysis](https://stockanalysis.com/stocks/ant/) shows "81.91 -5.73 (-6.54%)" at the close |
| 2 | It was the first close below the IPO price | **REAL** | Nasdaq closes: $97.17 (Nov 19), $88.91 (Nov 20), $87.64 (Nov 23), $81.905 (Nov 24). Only the last is below $83 |
| 3 | It fell 6.5% on the day | **REAL** | Nasdaq: $81.905 against $87.64, down 6.54%. Volume 313.0 million shares |
| 4 | At the low it was almost 9% under the IPO price | **REAL** | Nasdaq: the day's low was $75.61, 8.9% below $83. On Nov 20 the low had stopped at $83.05 |
| 5 | It has lost about a quarter from its first trade | **REAL** | Nasdaq: first trade $111.50 on Nov 19. $81.905 is 26.5% lower, and 15.7% below the first close of $97.17 |
| 6 | IPO buyers are still sitting on gains | **FALSE** | At the Nov 24 close, 980 million IPO shares × ($81.905 − $83) = −$1.07 billion on paper, assuming every share is still held |
| 7 | A specific report caused the drop | **OUR READ** | Outlets point to different reasons. Price data shows when the stock fell, not why, and we did not check the reports they cite |

## Reproduce

```python
closes = {"Nov 19": 97.17, "Nov 20": 88.91, "Nov 23": 87.64, "Nov 24": 81.905}
ipo = 83
print([d for d, c in closes.items() if c < ipo])   # ['Nov 24']
print(round((81.905 / ipo - 1) * 100, 2))           # -1.32
print(round((81.905 / 87.64 - 1) * 100, 2))         # -6.54
print(round((75.61 / ipo - 1) * 100, 2))            # -8.9
print(round((81.905 / 111.50 - 1) * 100, 1))        # -26.5
print(round(980e6 * (81.905 - ipo) / 1e9, 2))       # -1.07 (billion)
```

## What would change this page

A correction to Nasdaq's end-of-day record. Later closes are tracked on the Anthropic story page.

## Corrections

None so far. If you find an error, open an issue with the source.
