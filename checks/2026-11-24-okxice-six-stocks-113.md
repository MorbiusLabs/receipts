# OKXICE opened 24/7 tokenized stock trading with six stocks. The 113 assets come "on a rolling basis"

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-24-okxice-six-stocks-113/) · **Checked:** 2026-11-24 · **Status:** launch and fine print sourced to OKX; the six-stock count and the 67 objections are Crypto in America's reporting

OKXICE, the OKX and ICE joint venture, opened its Tokenized Securities Venue to eligible US customers at noon ET on Nov 23. Headlines said it launched "with 113 assets". OKX's own page says the 113 are confirmed and arrive over time.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | OKXICE opened round-the-clock trading in tokenized US stocks on Nov 23 | **REAL** | [OKX, "24/7 Securities Trading Arrives on OKXICE"](https://www.okx.com/en-us/learn/okxice-tsv-launch-going-live), Nov 23: "Starting at noon ET today, eligible U.S. customers can trade available assets around the clock" |
| 2 | All 113 assets trade from day one | **FALSE** | Same page: "The venue has confirmed 113 assets, including stocks, ETFs and ETPs, which will become available on a rolling basis beginning today" |
| 3 | Six stocks were tradable at the start | **REAL (their reporting)** | [Crypto in America](https://www.cryptoinamerica.com/p/tokenized-stock-trading-begins-on), Nov 23: "six stocks initially available to trade: Coinbase (COIN), Securitize (SECZ), Strategy (MSTR), BitGo (BTGO), Robinhood (HOOD) and Circle (CRCL)". OKX's page gives no live count |
| 4 | The list grew before launch | **REAL** | OKX on [Nov 11](https://www.okx.com/en-us/learn/okxice-tsv-launch): "More than 70 assets are expected to be listed", including "59 Direxion ETFs". On Nov 23: 113 confirmed |
| 5 | Big companies objected to having their shares tokenized | **REAL (their reporting)** | Crypto in America: "56 of the 62 issuers on OKXICE's original proposed stock list objected", "including Apple, Nvidia, Amazon and JPMorgan", and "In total, 67 companies have filed objections, according to OKXICE's latest public notice, dated November 20". We did not open that notice |
| 6 | The venue is approved by the SEC | **FALSE** | OKX's page: "OKXICE TSV is offered by OKXICE LLC under a temporary SEC exemption ... It is not a registered exchange or broker-dealer and is not approved by the SEC" |
| 7 | The New York Stock Exchange runs it | **FALSE** | OKX's page: "the NYSE does not operate or oversee this venue". ICE, the NYSE's parent, is OKX's partner in the joint venture |

## Reproduce

```python
confirmed, at_start = 113, 6
print(confirmed - at_start)   # 107: confirmed assets not tradable at the start, if six is right
print(56 / 62 * 100)          # 90.3: share of the original stock list that objected
```

## What would change this page

An OKX or OKXICE list of live assets, or the Nov 20 public notice showing a different objection count.

## Corrections

None so far. If you find an error, open an issue with the source.
