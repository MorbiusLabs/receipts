# "Tokenized Anthropic" on BNB Chain is not Anthropic stock

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-19-tokenized-anthropic-bnb/) · **Checked:** 2026-11-19 · **Status:** all claims sourced; Binance's terms are quoted through CoinDesk

Binance founder Changpeng Zhao said tokens linked to Anthropic would trade on BNB Chain from the company's first day on Nasdaq. The tokens are real. What they give you is price exposure, not a share.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Buying ANTx or another "tokenized Anthropic" makes you an Anthropic shareholder | **FALSE** | [Kraken](https://www.kraken.com/ipo/anthropic), the xStocks venue: "xStocks are not equity and confer no voting or shareholder rights". [CoinDesk](https://www.coindesk.com/markets/2026/11/19/cz-says-tokenized-anthropic-is-coming-to-bnb-chain-on-ipo-day), Nov 18: Binance says the token "confers no direct ownership in Anthropic" and has no voting, dividend or shareholder rights |
| 2 | Tokens tracking Anthropic go live on BNB Chain on IPO day, via bStocks, Ondo and xStocks | **REAL (their reporting)** | CoinDesk, Nov 18, reporting CZ's post and BNB Chain's promotion. We could not open the post on X itself |
| 3 | Every token is backed 1:1 by real Anthropic shares | **FALSE** | CoinDesk: Binance says reserves "may not always consist of Anthropic shares", with cash or other assets possible, and it "neither verifies those reserves independently nor guarantees 1:1 backing" |
| 4 | Anthropic is behind these tokens | **NOT CLAIMED** | No source we opened says Anthropic is involved. Kraken names the issuer: Backed Assets (JE) Limited, a Jersey company. Anthropic's IPO release does not mention tokens |
| 5 | Binance Wallet's pre-IPO campaign filled a 500 million USDC cap | **REAL (their reporting)** | CoinDesk: it opened at 06:00 UTC Nov 18 and closed early. Committing "does not guarantee an allocation"; unallocated USDC is refunded |
| 6 | Token buyers got the IPO price | **OUR READ** | Binance listed an indicative band of 70 to 78 USDC plus a 5% xStocks fee (CoinDesk). Kraken says "Plus a 5% spread". At the $83 IPO price, 5% on top is 87.15 USDC per token. Fills are decided by underwriters and may be zero |
| 7 | Anyone can buy them on Kraken | **FALSE** | Kraken, for its xStocks version: "Not available in the U.S. or to U.S. persons, or in the United Kingdom, Canada or Australia" |
| 8 | Ondo's ANTon is backed by the underlying securities | **REAL (their claim)** | CoinDesk quoting Ondo: backed by "the underlying securities and cash in transit". Holders get no shareholder or information rights. We did not open Ondo's own page |

## Reproduce

```python
ipo = 83.00
print(round(ipo * 1.05, 2))        # 87.15 USDC with a 5% fee or spread
print(round(78 * 1.05, 2))          # 81.90 at the old top of the band
```

## Corrections

None so far. If you find an error, open an issue with the source.
