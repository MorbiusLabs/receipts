# Crypto-stealing code ran on HSBC, Ledger and 176 other sites through one testing tool

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-19-optimizely-crypto-clipper/) · **Checked:** 2026-11-19 · **Status:** all claims sourced

On Nov 16, visitors to some of the world's biggest websites were served code that swapped crypto addresses and skimmed cards. The sites themselves were not hacked. A script they all load from the testing platform Optimizely was.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Malicious code reached visitors of 178 organisations through Optimizely Web | **REAL (their analysis)** | [Report URI](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/), Scott Helme, Nov 16: "188 snippets belonging to 178 organisations were infected", out of 1,611 snippets they fetched. The real number "is likely higher" |
| 2 | HSBC, Ledger, Zoom, the BBC, CNN and IKEA were among them | **REAL (their analysis)** | Same post, full list. HSBC sites in 11 markets are listed, including the US and Hong Kong |
| 3 | HSBC's and Ledger's own systems were breached | **NOT CLAIMED** | Report URI: the code was written into Optimizely projects and served from Optimizely's CDN; "A website can be compromised through a third-party dependency without its own code or infrastructure ever being breached" |
| 4 | The code swapped crypto addresses in pages and in the clipboard | **REAL (their analysis)** | Same post: BTC, ETH and EVM chains, TRON, Solana, TON and others, checksum-validated. It also skimmed cards typed into a site's own forms (not hosted iframes like Stripe or Adyen), stole cookies and screenshots, and loaded iOS exploit kits |
| 5 | The attacker's wallets received about $7,040 | **REAL (their analysis)** | Same post, as of 19:25 UTC Nov 16: $5,380 + $762 + $719 + $100 + $82 = $7,043. Card and cookie theft does not show on-chain, so the total loss is unknown |
| 6 | Almost all infected scripts were cleaned the same day | **REAL (their analysis)** | Same post: 1 of 188 still infected at 21:52 UTC |
| 7 | Optimizely says it fixed the flaw | **REAL (their reporting)** | [iTWire](https://www.itwire.com/business-it-news/security/optimizely-says-it-has-fixed-flaw-used-to-inject-malicious-scripts), Nov 18: Optimizely said it "has fully remediated the Experimentation platform vulnerability". A spokesperson told Gizmodo the flaw was in the account signup flow |
| 8 | AI was behind the attack | **NOT CLAIMED** | No researcher or company has said so. CoinDesk: investigators "have not linked the attack to AI" |

## What to do

If you copied a wallet address from any of these sites on Nov 16, check the address you sent to. If you typed a card number into a site's own checkout form that day, watch the statement.

## Corrections

None so far. If you find an error, open an issue with the source.
