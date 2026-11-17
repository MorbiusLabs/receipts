# Stablecoin supply just had its biggest 30-day drop since Terra

**Post:** [x.com/MorbiusLabs/status/2122716103721836853](https://x.com/MorbiusLabs/status/2122716103721836853) · [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-17-stablecoin-supply-drop/) · **Checked:** 2026-11-17 · **Status:** all claims sourced

USD stablecoins are the cash that sits inside crypto. When their supply shrinks, money is leaving that system. We measured how much, using DefiLlama's public data, and recomputed every number.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Total USD stablecoin supply fell from $302.73B on Oct 17 to $287.10B on Nov 16, a drop of $15.63B (−5.2%) | **REAL** | [DefiLlama stablecoin API](https://stablecoins.llama.fi/stablecoincharts/all), total USD-pegged supply. Reproduce below |
| 2 | In dollars, it is the largest 30-day drop since the Terra collapse in May 2022 | **REAL** | Same data. Only the window ending May 30, 2022 (−$28.58B) is larger. The peak of the current slide is the window ending Nov 14, 2026 (−$16.34B). Reproduce below |
| 3 | Tether fell $8.16B and USDC $3.42B, together 74% of the drop | **REAL** | DefiLlama [Tether](https://stablecoins.llama.fi/stablecoin/1) and [USDC](https://stablecoins.llama.fi/stablecoin/2) series, Oct 17 to Nov 16 |
| 4 | The data shows money leaving stablecoins, not where it went | **OUR READ** | Supply falls when holders redeem coins for dollars. Redemptions do not say what the dollars bought next |
| 5 | The drop is caused by the Anthropic IPO | **NOT CLAIMED** | No source we opened links the two. Our open thread on that question stays open |

## Reproduce claims 1 to 3

```bash
python3 scripts/stablecoin_supply.py 2026-11-16
```

Expected output starts with `change: -15.63B (-5.16%)` and lists the May 30, 2022 window first among the largest drops in dollars. In percent terms the tiny 2018 and 2019 market had larger swings, so we state the ranking in dollars.

Bloomberg reported a figure of about $12 billion for the drop. We could not open the article, so we use only our own reproducible numbers.

## Corrections

None so far. If you find an error, open an issue with the source.
