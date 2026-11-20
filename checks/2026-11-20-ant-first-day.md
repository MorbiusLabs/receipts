# ANT's first day: opened at $111.50, closed at $97.17. What "$2 trillion" counts

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-ant-first-day/) · **Checked:** 2026-11-20 · **Status:** all claims sourced

Anthropic's Class A shares started trading on Nasdaq on Nov 19 under the ticker ANT, after pricing at $83. Below are the first day's prices from Nasdaq's own data and the valuation figures rebuilt from the final prospectus (424B4).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | ANT opened at $111.50, 34% above the $83 IPO price | **REAL** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/ant/historical), Nov 19: open $111.50. (111.50 − 83) / 83 = +34.3%. Yahoo Finance's one-minute data puts the first trade at 11:48 a.m. ET |
| 2 | It closed at $97.17, up 17% on the day | **REAL** | Nasdaq: close $97.17. [StockAnalysis](https://stockanalysis.com/stocks/ant/): "97.17 +14.17 (17.07%)" at 4:00 p.m. That is 12.9% below the open |
| 3 | It traded between $92.72 and $115.10 on about 857 million shares | **REAL** | Nasdaq: high $115.10, low $92.72, volume 857,312,300. Reports during the day gave a high of $114.99; Nasdaq's end-of-day record is higher |
| 4 | Anthropic is worth $2 trillion | **OUR READ** | Only at the opening price, and only on a fully diluted count that adds options and RSUs. At the close that count gives $1.76 trillion. On shares actually outstanding after the deal it was $1.47 trillion at the open and $1.28 trillion at the close |
| 5 | The IPO valued Anthropic at $1.5 trillion | **REAL** | Our sum of the 424B4's pro forma table (Class A, Class N, options, RSUs, Class T and F): 18,137,587,875 shares × $83 = $1.505 trillion. On the 13,219,642,276 shares the 424B4 says will be outstanding, it is $1.10 trillion |
| 6 | It was a $107 billion sale | **REAL** | Two deals added together: the IPO, 980,000,000 × $83 = $81.34B, and a separate $26.0B private placement of non-voting Class N shares to AMD, Broadcom, Google, Micron, Microsoft, Nvidia and TSMC Partners, at the IPO price ([424B4](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074944/anthropicpbc-424b4.htm)). Total $107.34B |
| 7 | ANT opened at $83 | **FALSE** | $83 is the IPO price, paid by investors who got allocations. The first public trade was at $111.50 (Nasdaq) |
| 8 | It slipped further after hours | **REAL (their data)** | StockAnalysis: $92.58 at 7:59 p.m. ET, down 4.72% from the close. After-hours trading is thin |
| 9 | The deal is done | **WATCH** | The 424B4 says the private placement "is contingent upon, and is scheduled to close immediately" after the IPO, which closes on or about Nov 20. The underwriters' option on 147 million more shares runs for 30 days |

## Reproduce

```python
ipo, open_, close, high = 83.00, 111.50, 97.17, 115.10
print((open_ - ipo) / ipo, (close - ipo) / ipo, (close - open_) / open_)   # 0.343 0.171 -0.129

# 424B4, shares outstanding after the offering and the private placement
out = 7_583_103_996 + 5_636_538_278 + 2            # Class A + Class N + Class T and F
# 424B4, pro forma table "Total" row: Class A, Class N, options, RSUs, Class T and F
fd = 7_585_256_149 + 7_766_496_616 + 1_712_133_811 + 1_073_701_297 + 2
for p in (ipo, open_, close):
    print(p, round(out * p / 1e12, 3), round(fd * p / 1e12, 3))
# 83.0 1.097 1.505 / 111.5 1.474 2.022 / 97.17 1.285 1.762

print(980_000_000 * ipo / 1e9 + 26.0)              # 107.34 billion
print(313_253_007 * ipo / 1e9)                     # 26.0 billion, Class N placement shares
```

## What would change this page

The underwriters using their option, or the private placement failing to close. We use Nasdaq's end-of-day record for prices; if Nasdaq corrects it, we will update with the date.

## Corrections

None so far. If you find an error, open an issue with the source.
