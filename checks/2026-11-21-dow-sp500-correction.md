# Dow and S&P 500 closed in correction, Nasdaq gave back 2026. The S&P is still up 0.95% for the year

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-21-dow-sp500-correction/) · **Checked:** 2026-11-21 · **Status:** all claims sourced; Nov 20 S&P 500 and Nasdaq closes from Yahoo Finance's closed-market ticker, matched to FRED's Nov 19 closes

Friday Nov 20 closes against each index's record close and its Dec 31, 2025 close. A correction means a fall of 10% or more from the peak; a bear market, 20%.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The S&P 500 closed in correction territory | **REAL** | [Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-19-dow-sp-500-nasdaq-anthropic-nvidia-141644188.html) ticker: "6,910.39 -265.44 -3.70%". [FRED SP500](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500): record close 7,818.93 on Oct 6, 2026; Nov 19 close 7,175.83, and 7,175.83 minus 265.44 is 6,910.39. Down 11.62% from the record |
| 2 | The Dow closed in correction territory | **REAL** | [FRED DJIA](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DJIA): Nov 20 close 48,147.33, record close 54,349.12 on Aug 5, 2026. Down 11.41%. Yahoo's ticker shows the same close |
| 3 | The Nasdaq erased its 2026 gains | **REAL** | Yahoo ticker: "22,617.73 -1,261.47 -5.28%". [FRED NASDAQCOM](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NASDAQCOM): Dec 31, 2025 close 23,241.99, so the index is down 2.69% for the year. Yahoo: "fully erasing this year's gains" |
| 4 | The Nasdaq sank 5% | **REAL** | Down 5.28% on the day, from FRED's Nov 19 close of 23,879.20 |
| 5 | The S&P 500 and the Dow are still up for 2026 | **OUR READ** | Barely. S&P 500: 6,910.39 against 6,845.50 on Dec 31, 2025, up 0.95%. Dow: 48,147.33 against 48,063.29, up 0.17% |
| 6 | The Nasdaq is not yet in a bear market | **OUR READ** | Down 18.05% from its record close of 27,599.89 on Oct 6, 2026. The usual line is 20% |

The headline is Yahoo's: "Dow and S&P 500 enter correction, Nasdaq sinks 5% to erase 2026 gains as AI trade melts down". Earlier intraday entries in the same blog said the S&P had "fallen 10.7%" from its record; the closing drawdowns are deeper. Claims 5 and 6 are what the headline leaves out, from the same data. Causes (the AI trade, Nvidia, rates) are not part of these verdicts.

## Reproduce

```python
import csv, io, urllib.request
def fred(s):
    t = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}").read().decode()
    return {d: float(v) for d, v in list(csv.reader(io.StringIO(t)))[1:] if v not in ("", ".")}
nov20 = {"SP500": 6910.39, "DJIA": 48147.33, "NASDAQCOM": 22617.73}   # Yahoo ticker; FRED for DJIA
for s, c in nov20.items():
    f = fred(s)
    peak = max(f.values())
    print(s, peak, round((c / peak - 1) * 100, 2), round((c / f["2025-12-31"] - 1) * 100, 2), round((c / f["2026-11-19"] - 1) * 100, 2))
# SP500     7818.93  -11.62  0.95  -3.7
# DJIA      54349.12 -11.41  0.17  -1.93
# NASDAQCOM 27599.89 -18.05 -2.69  -5.28
```

## Corrections

None so far. If you find an error, open an issue with the source.
