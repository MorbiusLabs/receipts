# receipts

![receipts: every claim we post, with its verdict and primary source](assets/social-preview.png)

Every claim we post, with its source.

[@MorbiusLabs](https://x.com/MorbiusLabs) covers the stories where AI and money meet: banks, crypto, stablecoins, payments. This repo is the paper trail. Each check, on X or on [morbiuslabs.org](https://morbiuslabs.org), gets a page that lists every factual claim, a verdict and the primary source behind it. Where a number comes from public data, there is a script that recomputes it.

If you think we got something wrong, open an issue with a source. Corrections are logged on the page they affect.

## Fact-checks

| Date | Post | Claims | Page |
|---|---|---|---|
| 2026-11-17 | Anthropic's last filing before pricing: range unchanged, Nasdaq approved | 7 (6 real, 1 watch) | [checks/2026-11-17-anthropic-final-filing.md](checks/2026-11-17-anthropic-final-filing.md) |
| 2026-11-17 | Fed's Waller: tokenization and AI "could be catalysts for one another" | 5 (4 real, 1 not claimed) | [checks/2026-11-17-waller-tokenization-ai.md](checks/2026-11-17-waller-tokenization-ai.md) |
| 2026-11-17 | An AI agent account with spending limits launched today | 6 (2 real, 4 their reporting) | [checks/2026-11-17-lightspark-agent-accounts.md](checks/2026-11-17-lightspark-agent-accounts.md) |
| 2026-11-17 | Did AI hijack Bitcoin miners? What Luxor actually said | 6 (4 their reporting, 1 watch, 1 not claimed) | [checks/2026-11-17-luxor-ai-mining-hack.md](checks/2026-11-17-luxor-ai-mining-hack.md) |
| 2026-11-17 | Stablecoin supply just had its biggest 30-day drop since Terra | 5 (3 real, 1 our read, 1 not claimed) | [checks/2026-11-17-stablecoin-supply-drop.md](checks/2026-11-17-stablecoin-supply-drop.md) |
| 2026-11-17 | Did AI hack Binance? What Binance's own report says | 7 (6 their reporting, 1 false) | [checks/2026-11-17-binance-hack-ai.md](checks/2026-11-17-binance-hack-ai.md) |
| 2026-11-17 | Nvidia reports today, its first quarter without Jensen Huang | 6 (5 real, 1 not claimed) | [checks/2026-11-17-nvidia-first-report-without-huang.md](checks/2026-11-17-nvidia-first-report-without-huang.md) |
| 2026-11-17 | Zelle sent $1.25M in ZelleUSD on Solana. When does it launch? | 6 (1 real, 4 their reporting, 1 watch) | [checks/2026-11-17-zelleusd-solana.md](checks/2026-11-17-zelleusd-solana.md) |
| 2026-11-17 | Is the Anthropic IPO draining crypto? | 14 (8 real, 2 corrected, 2 their reporting or analysis, 1 our read, 1 watch) | [checks/2026-11-17-anthropic-ipo-draining-crypto.md](checks/2026-11-17-anthropic-ipo-draining-crypto.md) |
| 2026-11-16 | Banks froze today, "internet off" tomorrow | 11 (7 real, 3 false, 1 not claimed) | [checks/2026-11-16-banks-down-internet-off.md](checks/2026-11-16-banks-down-internet-off.md) |
| 2026-11-16 | Your AI agent buys the wrong thing. Who pays? | 9 | [checks/2026-11-16-who-pays-agent-checkout.md](checks/2026-11-16-who-pays-agent-checkout.md) |
| 2026-11-14 | Agent payments split into two rails | 6 | [checks/2026-11-14-two-rails.md](checks/2026-11-14-two-rails.md) |

## Verdicts

| Verdict | Meaning |
|---|---|
| **REAL** | Confirmed by a primary source: the document, filing, speech, statement or chain data itself |
| **REAL (their analysis)** | A source's reading or forecast, reported as theirs, not as settled fact |
| **FALSE** | No primary source supports it, or a primary source contradicts it |
| **WATCH** | A real risk named by a credible source, not yet an event |
| **EXAMPLE** | An illustrative number in our post, not a measurement |
| **OUR READ** | Our interpretation of the sourced data on the same page, labeled as opinion |
| **NOT CLAIMED** | A link readers might assume, which we did not make |

## Scripts

| Script | What it checks |
|---|---|
| [scripts/stablecoin_supply.py](scripts/stablecoin_supply.py) | Total USD stablecoin supply: the 30-day change to any date, the Tether and USDC parts, and the largest drops on record, from DefiLlama |
| [scripts/november_moves.py](scripts/november_moves.py) | November 2026 Bitcoin ETF flows and the Bitcoin, Nvidia and Nasdaq moves, from Farside, CoinGecko and Yahoo Finance |
| [scripts/btc_blocks_window.py](scripts/btc_blocks_window.py) | Bitcoin blocks and transactions mined inside any time window, from the public mempool.space API |

Python 3, standard library only, no API keys.

```bash
python3 scripts/btc_blocks_window.py 2026-11-16T17:00:00Z 2026-11-16T20:00:00Z
```

## Rules we follow

1. Primary sources first. A news article counts only for what it directly observed, and we say so.
2. Quotes are exact. Paraphrases are marked.
3. Numbers we compute ourselves ship with the script.
4. We never link two events without a source that links them.

## License

Code: MIT. Text: CC BY 4.0. Quote it, link back.
