# SEC: an "AI-driven" algorithm promising 6% a month raised $560 million. The SEC calls it a Ponzi scheme

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-sec-ai-driven-ponzi/) · **Checked:** 2026-11-20 · **Status:** all claims sourced to the SEC release; these are allegations, not court findings

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The SEC charged an Indianapolis firm over a $560 million offering | **REAL** | [SEC release 2026-116](https://www.sec.gov/newsroom/press-releases/2026-116-sec-charges-indianapolis-based-backward-hat-capital-its-co-founders-560-million-dollar-offering), Nov 20: Backward Hat Capital and its co-founders "fraudulently raised approximately $560 million from more than 2,000 investors", the SEC alleges |
| 2 | Investors were told an "AI-driven" algorithm and crypto were behind the returns | **REAL (SEC's allegation)** | Investors were promised their funds "would be converted to crypto assets and then used to engage in FX arbitrage using a proprietary, “AI-driven” algorithm which they claimed always returned at least 6% per month" |
| 3 | 6% a month is a normal return | **FALSE** | Compounded, 6% a month is about 101% a year. No legitimate trading strategy promises that "always" |
| 4 | Earlier investors were paid with newer investors' money | **REAL (SEC's allegation)** | "more than $250 million in Ponzi-like payments to previous investors", about 45% of the money raised. The SEC also alleges "more than $220 million" went to the defendants themselves |
| 5 | Regulators have stepped in | **REAL** | The SEC "obtained a temporary restraining order, asset freeze" and other relief. Federal prosecutors in Manhattan and the CFTC filed parallel charges |
| 6 | A court has found them guilty | **FALSE** | These are charges. No court has ruled on the merits |

## Reproduce

```python
print(round((1.06 ** 12 - 1) * 100, 1))   # 101.2% a year at 6% a month, compounded
print(round(250 / 560 * 100, 1))          # 44.6% of money raised went to Ponzi-like payments
```

## Corrections

None so far. If you find an error, open an issue with the source.
