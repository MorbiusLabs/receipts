# The S&P 500 lost 8.61% last week, its worst since April 2025. The Dow's 8.02% drop was its worst since March 2020

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-23-sp500-dow-worst-week/) · **Checked:** 2026-11-23 · **Status:** all claims sourced; the Nov 20 S&P 500 close comes from Yahoo Finance's ticker, because FRED has not posted it yet

Friday Nov 13 close against Friday Nov 20 close, ranked against every week in FRED's daily series, which starts in November 2016 for both indexes. This follows [our check of the Nov 20 correction](https://morbiuslabs.org/p/2026-11-21-dow-sp500-correction/).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The S&P 500 lost over 8% last week | **REAL** | [Yahoo Finance](https://finance.yahoo.com/markets/article/a-battered-stock-market-looks-for-the-bottom-what-to-watch-this-week-100000117.html), Nov 22: "the S&P 500 ([^GSPC]) losing over 8%". [FRED SP500](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500): Nov 13 close 7,561.67. Nov 20 close 6,910.39 from the ticker on the same Yahoo page, which is FRED's Nov 19 close of 7,175.83 minus 265.44. Down 8.61%, or 651.28 points |
| 2 | It was the S&P 500's worst week since April 2025 | **REAL** | Weeks that were worse in FRED's series: Feb 28, 2020 (−11.49%), Mar 13, 2020 (−8.79%), Mar 20, 2020 (−14.98%) and Apr 4, 2025 (−9.08%). The only other week at −7% or worse, Dec 21, 2018 (−7.05%), was milder |
| 3 | The Dow lost 8.02%, its worst week since March 2020 | **REAL** | [FRED DJIA](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DJIA): Nov 13 close 52,347.55, Nov 20 close 48,147.33. Down 4,200.22 points. Worse weeks: Feb 28, 2020 (−12.36%), Mar 13, 2020 (−10.36%), Mar 20, 2020 (−17.30%). April 4, 2025 was −7.86% |
| 4 | This is the worst week since 2020 for both indexes | **OUR READ** | True for the Dow, not for the S&P 500: its April 2025 week was deeper. The ranking only reaches back to November 2016, which is enough for both "since" claims |

Causes (the AI trade, Nvidia, rates) are not part of these verdicts. The Nasdaq is not ranked: FRED has no Nov 20 Nasdaq close yet.

## Reproduce

```python
import csv, io, urllib.request, datetime as dt
def fred(s):
    t = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}").read().decode()
    return {dt.date.fromisoformat(d): float(v) for d, v in list(csv.reader(io.StringIO(t)))[1:] if v not in ("", ".")}
for s, extra in [("SP500", {dt.date(2026, 11, 20): 6910.39}), ("DJIA", {})]:   # S&P Nov 20 from the Yahoo ticker
    f = fred(s); f.update({k: v for k, v in extra.items() if k not in f})
    wk = {}
    for d in sorted(f): wk[d.isocalendar()[:2]] = f[d]            # last close of each week
    c = list(wk.values())
    for (k, v), prev in zip(list(wk.items())[1:], c):
        r = (v / prev - 1) * 100
        if r <= -7: print(s, k, round(r, 2))
# SP500: 2018 w51 -7.05, 2020 w9 -11.49, 2020 w11 -8.79, 2020 w12 -14.98, 2025 w14 -9.08, 2026 w47 -8.61
# DJIA:  2020 w9 -12.36, 2020 w11 -10.36, 2020 w12 -17.3, 2025 w14 -7.86, 2026 w47 -8.02
```

## What would change this page

FRED's official Nov 20 S&P 500 close differing from 6,910.39.

## Corrections

None so far. If you find an error, open an issue with the source.
