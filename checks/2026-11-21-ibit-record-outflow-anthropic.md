# A record $541 million left BlackRock's bitcoin ETF on ANT's first day. Nothing shows it went into Anthropic

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-21-ibit-record-outflow-anthropic/) · **Checked:** 2026-11-21, updated 2026-11-22 · **Status:** all flow figures from Farside Investors' daily table (US$ millions)

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | IBIT had its biggest one-day outflow ever on Nov 19 | **REAL** | [Farside, bitcoin ETF flows](https://farside.co.uk/bitcoin-etf-flow-all-data/): IBIT (541.1) on Nov 19, 2026, the largest daily outflow in its history. The previous record was (528.3) on Jan 30, 2026. [Cointelegraph](https://cointelegraph.com/markets/blackrock-ibit-record-single-day-outflow) reported the same figure |
| 2 | All US spot bitcoin ETFs lost $582 million that day | **REAL** | Farside total for Nov 19: (582.3). IBIT was 93% of it |
| 3 | The money left bitcoin to buy Anthropic stock | **NOT CLAIMED** | Cointelegraph says the withdrawals "coincided with a broader market selloff" as Anthropic's debut "failed to sustain gains in AI-related stocks". That is timing. No source we read shows money moving from bitcoin funds into ANT |
| 4 | The outflows started with ANT's debut | **FALSE** | Farside: Nov 2 to 18, before ANT traded, US spot bitcoin ETFs had already lost $2,885.5M, with outflows on 11 of those 13 trading days. Nov 2 to 19 in total: $3,467.8M out, 12 of 14 days negative |

See the open question on our [threads page](https://morbiuslabs.org/threads/): does Anthropic's IPO pull cash out of crypto? It is still open.

## Reproduce

```python
total_2_19, nov_19 = -3467.8, -582.3   # Farside daily totals: sum of Nov 2-19, and Nov 19
print(round(total_2_19 - nov_19, 1))      # -2885.5 before ANT's first trading day
print(round(541.1 / 582.3 * 100))         # 93% of Nov 19 outflows were IBIT
```

## Corrections

2026-11-22: flow figures now come from Farside directly (we could not open it on Nov 21 and cited Cointelegraph). Claim 4 added.
