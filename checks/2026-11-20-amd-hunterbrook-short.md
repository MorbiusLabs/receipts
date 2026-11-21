# AMD fell 7.7% after a short seller's China report. The report does not say AMD broke the law

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-amd-hunterbrook-short/) · **Checked:** 2026-11-20 · **Status:** price data from Nasdaq; the allegations are Hunterbrook's, and its fund is short AMD

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | AMD fell about 8% on Nov 19 | **REAL** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/amd/historical): close $489.19 against $530.14 on Nov 18, down 7.72%. Volume 71.7 million shares, 2.1 times the day before |
| 2 | A blacklisted Chinese server maker keeps using newer AMD firmware | **REAL (their reporting)** | [Hunterbrook, Nov 19](https://hntrbrk.com/investigations/amd-china): IEIT, on the US Entity List since March 2025, "has incorporated at least six newer versions of AMD's firmware into its own products, most recently in an updated version posted October 19" |
| 3 | AMD broke US export controls | **NOT CLAIMED** | Hunterbrook "does not know how IEIT obtained AMD's code, or whether AMD or anyone else held a license to supply it." On other payments it says they "do not establish that AMD violated U.S. export controls" |
| 4 | The report comes from a neutral source | **FALSE** | Hunterbrook discloses that Hunterbrook Capital "is short $AMD and long a basket of comparable securities", so it profits if the stock falls |
| 5 | AMD disputes the report | **REAL** | AMD statement, quoted by Hunterbrook: the reporting "misrepresents AMD's business practices and relationships" |
| 6 | China is a large share of AMD's sales | **REAL (their figures)** | Hunterbrook: "AMD billed $7.75 billion, or 22.4% of revenue, to China (and Hong Kong) in fiscal 2025." We did not open the 10-K |
| 7 | AMD kept falling the next day | **REAL** | Nasdaq: Nov 20 close $424.39, down another 13.25%, in a broad chip sell-off. Two-day drop from $530.14: 19.95%. No source ties the second day to the report |

## Reproduce

```python
print(round((489.19 - 530.14) / 530.14 * 100, 2))   # -7.72
print(round(71_660_690 / 34_028_590, 2))            # 2.11x the previous day's volume
```

## Corrections

None so far. If you find an error, open an issue with the source.
