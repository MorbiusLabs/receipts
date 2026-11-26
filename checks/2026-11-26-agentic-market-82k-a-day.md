# AI agents paid $82,099 in USDC in a day on Coinbase's Agentic Market, in payments of cents. The "$50 million at launch" has no source

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-26-agentic-market-82k-a-day/) · **Checked:** 2026-11-26 · **Status:** dashboard figures read from agentic.market on Nov 26, 2026 at 16:26 UTC; they change live

Agentic Market is Coinbase's marketplace where AI agents find paid APIs and pay per call in USDC over the x402 protocol. Coverage this week said Coinbase opened it to open-weight AI models and repeated launch figures. We read Coinbase's own pages.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | AI agents buy services on Agentic Market and pay in USDC | **REAL** | [agentic.market/about](https://agentic.market/about): "Agentic Market is where agents discover paid APIs and settle in USDC." and "Your agent pays in USDC the moment the API returns a result." |
| 2 | Agents paid about $82,000 in one day | **REAL** | [agentic.market](https://agentic.market/) dashboard, Nov 26, 16:26 UTC: "1D TOTAL PAYMENT VOLUME $82,099.09" |
| 3 | Single payments are worth cents | **REAL** | Same dashboard, live feed. At 16:26 UTC: 140 payments shown, from $0.005 to $0.024. At 16:47 UTC: 138 of 140 at $0.020 or less, two at $1.00. All on Base. The About page's own example: "$0.01 USDC" |
| 4 | 7.3 million transactions and about 41,000 buyers in 30 days | **REAL** | Same dashboard: "TRANSACTIONS 30D 7,326,100" and "BUYERS/SELLERS 30D 40,948 / 14,450" |
| 5 | Total volume is about $58 million | **REAL** | Same dashboard: "Total Payment Volume $58,326,483.72" |
| 6 | 69,000 agents processed 165 million transactions worth $50 million around the April launch | **REAL (their reporting)** | [Dataconomy](https://dataconomy.com/2026/11/25/coinbase-opens-agentic-market-to-specialized-ai-models/), Nov 25, and Crypto Briefing, Nov 24, print these figures without naming a source. Coinbase's dashboard and About page do not show them |
| 7 | Coinbase opened the market to open-weight AI models | **REAL (their reporting)** | Same two articles. We did not find the invitation on agentic.market or in Coinbase's posts we read |
| 8 | Coinbase owns x402 | **FALSE** | agentic.market footer: "x402 is owned by the Linux Foundation. This webpage and marketplace is operated by Coinbase and is not an official product of the x402 Foundation." |

## Reproduce

Open [agentic.market](https://agentic.market/). The figures in rows 2 to 5 are live and will have moved since our read.

```python
day, total = 82_099.09, 58_326_483.72
tx30, buyers30, sellers30 = 7_326_100, 40_948, 14_450
print(round(tx30 / buyers30))          # 179 transactions per buyer in 30 days
print(round(total / 1e6, 1))           # 58.3 (million)
```

## What would change this page

A Coinbase post or filing with launch-day figures, or a published list of open-weight models on the market.

## Corrections

None so far. If you find an error, open an issue with the source.
