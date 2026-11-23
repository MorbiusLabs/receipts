# Coinbase's official ChatGPT plugin places trades. OpenAI's plugin rules list "investment trades" as prohibited

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-23-coinbase-chatgpt-plugin-openai-rules/) · **Checked:** 2026-11-23 · **Status:** the plugin and the rule text are sourced to Coinbase's and OpenAI's own pages; that the two do not fit is our reading, and neither company has explained it

Coinbase launched an official trading plugin for ChatGPT on Tue Nov 17, Yahoo Finance reported. OpenAI's published plugin guidelines still list "investment trades" among prohibited services. We opened both pages, plus OpenAI's help center, which names Coinbase as an example of a finance plugin with trades. We found no exception in the guidelines and no statement from either company on how they fit.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Coinbase has an official plugin for ChatGPT | **REAL** | [Coinbase Developer Docs](https://docs.cdp.coinbase.com/ai-agents/coinbase-for-agents/coinbase-mcp): "choose the official Coinbase plugin for ChatGPT if you want to review and approve every trade yourself" and "The official plugin is currently available to U.S. Coinbase users" |
| 2 | It trades crypto, US stocks and futures | **REAL (their reporting)** | [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/coinbase-launches-trading-plugin-chatgpt-185257768.html), Nov 17: it lets US users "trade crypto, eligible US stocks, and dated futures from inside a chat". We did not open Coinbase's own announcement |
| 3 | OpenAI's plugin rules prohibit investment trades | **REAL** | [OpenAI Plugin Guidelines](https://developers.openai.com/plugins/plugin-guidelines), under "Prohibited fraudulent, deceptive, or high-risk services": "Execution of money transfers, crypto transfers, or investment trades". The page has no date, and we found no exception for licensed or regulated brokers |
| 4 | OpenAI knows about Coinbase trades in ChatGPT | **REAL** | [OpenAI Help Center](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt): "For trades and actions involving financial transactions initiated during usage of a finance related plugin (e.g. Coinbase) a saved ChatGPT app permission does not replace the provider's explicit confirmation for each transaction." |
| 5 | The listing and the rule do not fit, and neither company has explained why | **OUR READ** | The rule bans the service; the plugin offers it. Yahoo: "Neither company has said how Coinbase's listing fits those rules", though Coinbase's Alec Lovett thanked the OpenAI team for its work on the launch. So this is not a listing OpenAI missed. What we cannot find is the written basis for it |
| 6 | Each plugin trade needs your confirmation | **REAL** | Coinbase docs: "Coinbase confirmation cards cover order placement, edits, cancellations, and USD–USDC conversions". OpenAI: "Allow all actions or Always allow does not grant standing permission for these trades, including through an automated or scheduled task." |
| 7 | Coinbase also offers a ChatGPT route without per-trade approval | **REAL** | Coinbase docs: "For automated trading workflows without approving each trade individually, use a custom Coinbase MCP connection." The confirmation applies to the plugin, not to every way of connecting Coinbase to ChatGPT |
| 8 | OpenAI said it will remove the Coinbase plugin | **NOT CLAIMED** | The guidelines say in general that "Previously approved plugins may be removed for policy violations". Nothing we opened says OpenAI plans to act on Coinbase |

## What would change this page

OpenAI updating the guidelines or saying that licensed brokers are exempt; OpenAI removing the plugin; a statement from Coinbase or OpenAI.

## Corrections

None so far. If you find an error, open an issue with the source.
