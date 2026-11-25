# CFTC staff say exchanges and clearinghouses can count bitcoin, ether and stablecoins toward their reserves. Staff view only, with haircuts, and never as the cash part

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-25-cftc-crypto-operating-reserves/) · **Checked:** 2026-11-25 · **Status:** all claims sourced to the CFTC press release and Staff Letter 26-31

On Nov 23 two CFTC divisions issued a staff advisory on crypto and the money that derivatives platforms must set aside to keep running for a year. Headlines said the CFTC "clears" bitcoin, ether and stablecoins as venue capital. The advisory is narrower.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Exchanges and clearinghouses can count bitcoin, ether and stablecoins toward their reserves | **REAL** | [CFTC press release 9331-26](https://www.cftc.gov/PressRoom/PressReleases/9331-26), Nov 23, 2026: "certain crypto assets, including bitcoin, ether, and payment stablecoins, may be counted toward the requirement to hold financial resources covering at least 12 months of operating costs, subject to appropriate haircuts." It covers swap execution facilities, designated contract markets and derivatives clearing organizations |
| 2 | The CFTC approved it as a rule | **FALSE** | Same release: "The advisory represents the views of staff only. It does not create new rules or enforceable rights, nor is it a no-action position and does not necessarily reflect the views of the Commission." |
| 3 | The coins count at full value | **FALSE** | [Staff Letter 26-31](https://www.cftc.gov/csl/26-31/download): staff "would not object" to haircuts that "include a 20% minimum haircut for bitcoin and ether, and a 2% haircut for payment stablecoins" |
| 4 | Any crypto token can be used | **FALSE** | Letter 26-31: "A crypto asset that is not readily marketable and that does not constitute a payment stablecoin would generally require a 100% haircut, meaning it cannot be used" |
| 5 | Crypto can cover the cash part of the reserve | **FALSE** | Release: crypto assets "are not eligible towards the separate liquidity requirement". The letter says at least six of the twelve months must be "cash and/or highly liquid securities" for exchanges (DCMs) and clearinghouses (DCOs), and at least three months for swap execution facilities |
| 6 | Clearinghouses can use crypto to cover a member's default | **NOT CLAIMED** | Letter 26-31: "Nothing in this advisory should be interpreted as addressing whether crypto assets, including payment stablecoins, may be used to satisfy a DCO's default resources requirements" |

## Reproduce

```python
btc_counted = 100 * (1 - 0.20)     # 80.0: $100 of bitcoin or ether counts as at most $80
usd_coin_counted = 100 * (1 - 0.02) # 98.0: $100 of a payment stablecoin counts as $98
print(btc_counted, usd_coin_counted)
print(1 - 6 / 12)   # 0.5: the most of a DCM's or DCO's 12-month reserve that crypto can cover
print(1 - 3 / 12)   # 0.75: the same for a swap execution facility
```

## What would change this page

A Commission vote or rule on the same question, or a staff letter on DCO default resources.

## Corrections

None so far. If you find an error, open an issue with the source.
