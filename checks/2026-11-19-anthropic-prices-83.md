# Anthropic prices at $83, above its range, and sells 155 million more shares

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-19-anthropic-prices-83/) · **Checked:** 2026-11-19 · **Status:** all claims sourced

Anthropic priced its IPO on the evening of Nov 18. ANT starts trading on Nasdaq on Nov 19. Here is what the company's own release and its SEC filings say, and the numbers we recomputed from them.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Anthropic priced its IPO at $83.00 per share | **REAL** | [Anthropic release](https://www.anthropic.com/news/anthropic-prices-initial-public-offering), Nov 18: "priced its initial public offering of its Class A common stock at $83.00 per share" |
| 2 | That is above the $70 to $78 range in its filings | **REAL** | The range was in [S-1/A No. 3](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074338/anthropicpbc-sx1ax3.htm). $83 is 6.4% above the top of the range and 12.2% above the midpoint ($74) |
| 3 | The deal grew from 825 million to 980 million shares | **REAL** | Release: 980,000,000 shares, 956,351,354 sold by Anthropic and 23,648,646 by selling stockholders. The extra shares were registered in an [S-1MEF](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074904/anthropic-sx1mef.htm) filed Nov 18: 178,250,000 more, including 23,250,000 for the underwriters' option. Anthropic's own share count rose from 801.35 million to 956.35 million; the selling stockholders' count did not change |
| 4 | The offering raised $81.34 billion | **REAL** | 980,000,000 × $83 = $81,340,000,000, before underwriting fees. Anthropic's part: 956,351,354 × $83 = $79.38 billion. Selling stockholders: $1.96 billion, which Anthropic does not receive |
| 5 | It is the largest IPO on record | **REAL** | Base deal against base deal: $81.34 billion against SpaceX's $75 billion in June ([our Nov 17 check](https://morbiuslabs.org/p/2026-11-17-anthropic-ipo-draining-crypto/), claim 3). With SpaceX's overallotment (about $86 billion) the comparison holds only if Anthropic's underwriters also use their option |
| 6 | Underwriters can buy 147 million more shares within 30 days | **REAL** | Release: "a 30-day option to purchase up to an additional 147,000,000 shares". 147 / 980 = 15%. If fully used, the deal reaches 1.127 billion shares and $93.54 billion |
| 7 | The $26 billion private placement is priced at $83 too | **REAL** | The S-1/A sets the Class N placement "at a price per share equal to the initial public offering price". At $83 that is about 313 million non-voting shares. It is separate from the $81.34 billion |
| 8 | ANT trades on Nasdaq from Nov 19; the deal closes Nov 20 | **REAL** | Release, "subject to the satisfaction of customary closing conditions" |
| 9 | Crypto money funded the order book | **NOT CLAIMED** | Nothing we have read shows who bought. See [our Nov 17 check](https://morbiuslabs.org/p/2026-11-17-anthropic-ipo-draining-crypto/) on the "IPO is draining crypto" claim |

## Reproduce

```python
shares, own, sellers, price, option = 980_000_000, 956_351_354, 23_648_646, 83, 147_000_000
assert own + sellers == shares
print(shares * price / 1e9)             # 81.34
print(own * price / 1e9)                # 79.377
print(price / 78 - 1, price / 74 - 1)   # 0.064, 0.122
print((shares + option) * price / 1e9)  # 93.541
print(26e9 / price / 1e6)               # 313.25 million Class N shares
```

## Not on this page

Reported valuations ($1.5 trillion fully diluted, about $1.08 trillion market value) depend on share counts we have not added up ourselves. The final prospectus (424B4) was not on EDGAR when we checked; we will compare it with the release when it is.

## Corrections

None so far. If you find an error, open an issue with the source.
