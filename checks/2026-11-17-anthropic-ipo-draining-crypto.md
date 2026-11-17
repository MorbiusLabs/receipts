# Is the Anthropic IPO draining crypto?

**Post:** [x.com/MorbiusLabs/status/2122607724345049413](https://x.com/MorbiusLabs/status/2122607724345049413) · **Checked:** 2026-11-17 · **Status:** all claims sourced

On Nov 16, CZ listed "money shifting to the Anthropic IPO" as one possible reason crypto prices are down. He added that "no one knows for sure" and that "correlation does not prove causation." We checked the money flows behind that idea.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | CZ floated the Anthropic IPO as one reason crypto is down, and 2.4 million people read it | **REAL** | [CZ's post](https://x.com/cz_binance/status/2122000010992824627), Nov 16. It lists the IPO first among "potential reasons". X showed 2,444,122 views when we checked on Nov 17 |
| 2 | Anthropic prices on Wednesday, Nov 18: 825 million shares at $70 to $78, raising up to $64.4 billion | **REAL** | Terms of the amended S-1 (filed Nov 10) as reported by [Fortune](https://fortune.com/2026/11/10/anthropic-ipo-price-range-ai-stock-sell-off/) and Reuters. Ticker ANT on Nasdaq |
| 3 | Only SpaceX raised more, $75 billion in June | **REAL** | SpaceX priced 555.6M shares at $135 on June 11, 2026, a $75B base deal, the largest IPO on record ([Bloomberg](https://news.bloomberglaw.com/capital-markets/elon-musks-spacex-set-to-make-history-with-record-breaking-ipo), Reuters, NPR). We compare base deal with base deal. With the overallotment SpaceX reached about $86B |
| 4 | The order book is reportedly about 6 times covered | **REAL (their reporting)** | Bloomberg, as cited by [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262304476-anthropic-ipo-ant-price-above-78-orders-six-times-november-14-2026-tradingkey), Nov 14. Not confirmed by the company |
| 5 | US spot Bitcoin ETFs lost $2.4 billion in November | **REAL** | [Farside Investors](https://farside.co.uk/bitcoin-etf-flow-all-data/), daily totals Nov 2 to Nov 16 sum to −$2,415.6M. Reproduce below |
| 6 | Outflows every session since Nov 5 | **REAL** | Same table: Nov 5, 6, 9, 10, 11, 12, 13 and 16 are all negative. Nov 4 was +$74.6M. Nov 16 was partly reported when we checked |
| 7 | Bitcoin is down 16% this month | **REAL** | CoinGecko daily prices: $77,521 on Nov 1, $64,616 on the morning of Nov 17 (−16.6%). Reproduce below |
| 8 | Nvidia is one of Anthropic's strategic investors | **REAL** | Fortune: seven strategic partners, including Google and Nvidia, agreed to buy $26B of non-voting stock at the IPO price. This placement is separate from the $64.4B offering |
| 9 | Nvidia is down 24% this month, worse than Bitcoin | **REAL** | Close $204.64 on Oct 30, $156.14 on Nov 16 (−23.7%). Reuters: "down nearly 24% for November". Reproduce below |
| 10 | On Nov 5 the Nasdaq had its worst day since April 2025 | **REAL** | Nasdaq Composite closed 25,736.51 on Nov 4 and 24,315.00 on Nov 5 (−5.5%). "Worst session since April 2025" per CNBC and Reuters, as cited by [IBTimes](https://www.ibtimes.co.uk/nvidia-qualcomm-shares-nasdaq-ai-selloff-1830635) |
| 11 | Bets on another Fed hike are growing | **REAL (their analysis)** | Market commentary after the Nov 6 jobs report and hot inflation data; CZ lists it in the same post. We give no probability number |
| 12 | It looks less like a rotation and more like everyone selling risk at once | **OUR READ** | Our interpretation of claims 5 to 10. If money were moving from crypto into AI, AI stocks would be rising; Nvidia fell harder than Bitcoin |
| 13 | A $64B order book can pull some cash out of crypto at the margin, but there is no proof yet | **WATCH** | Plausible mechanism, no flow data that shows it. We will update this page if any appears |
| 14 | Nvidia reports tonight, Anthropic prices Wednesday, ANT starts trading Thursday | **REAL** | Reuters: Nvidia fiscal Q3 results on Tue, Nov 17 after the close; pricing Wed, Nov 18; trading Thu, Nov 19 |

## Reproduce claims 5, 7 and 9

```bash
python3 scripts/november_moves.py
```

The script sums the Farside daily totals (copied into the script, because Farside blocks automated requests) and pulls prices from the public CoinGecko and Yahoo Finance chart endpoints. Expected output:

```
ETF flows Nov 2-16: -2,415.6 $M, outflow streak since Nov 5: 8 sessions
Bitcoin  Nov 1 -> latest: -16.6%   ($77,521 -> $64,616)   # at posting time
Nvidia   Oct 30 -> Nov 16: -23.7%
Nasdaq   Oct 30 -> Nov 16: -3.6%   Nov 5 alone: -5.5%
```

Bitcoin's line moves with the live price. Run it later and you get a different number for "latest".

## Replies that used these numbers

[@virtualbacon](https://x.com/MorbiusLabs/status/2122609061791175141) · [@Barchart](https://x.com/MorbiusLabs/status/2122609140186886410) · [@Brainmaster](https://x.com/MorbiusLabs/status/2122609230913917127) · [@Defi_Rocketeer](https://x.com/MorbiusLabs/status/2122609316481962302)

## Disclosure

The research and drafting for this post were done with Claude, a model made by Anthropic. We report only the IPO's public terms and market data, and make no call on the company or the stock.

## Corrections

None so far. If you find an error, open an issue with the source.
