# Your AI agent buys the wrong thing. Who pays?

**Post:** [x.com/MorbiusLabs/status/2122271535855514084](https://x.com/MorbiusLabs/status/2122271535855514084) · **Checked:** 2026-11-16 · **Status:** all claims sourced

Main source: Cloud Security Alliance AI Safety Initiative, research note "Agents at the Checkout: Loss Allocation in Frontier-Lab Payment Wallets", published 2026-11-15 ([labs.cloudsecurityalliance.org](https://labs.cloudsecurityalliance.org/research/csa-research-note-agent-payment-wallet-liability-concentrati/)).

| # | Claim | Verdict | Primary source |
|---|---|---|---|
| 1 | A per-purchase Face ID approval is strong evidence that you authorized the purchase | **REAL (their analysis)** | CSA note: per-purchase biometric approval "produces strong evidence that the cardholder authorized each transaction" |
| 2 | Wrong item, you approved without noticing: the loss likely moves to you, merchant returns soften it | **REAL (their analysis)** | CSA note, Table 2, confidence: medium |
| 3 | Prompt injection steers the agent to a bad seller and you approve: unresolved | **REAL (their analysis)** | Table 2, confidence: low |
| 4 | Purchase inside limits set in advance, later disputed: unresolved | **REAL (their analysis)** | Table 2, confidence: low |
| 5 | Wrong purchase by an agent registered with Amex: Amex has pledged to absorb it | **REAL (their analysis)** | Table 2, confidence: medium |
| 6 | The AI lab has no direct loss share in any scenario | **REAL (their analysis)** | Table 2 assigns the lab no direct share in any row |
| 7 | OpenAI says you keep your card's dispute protections, for example for defective items | **REAL** | [openai.com/index/introducing-chatgpt-wallet](https://openai.com/index/introducing-chatgpt-wallet) (Nov 13): "Users keep their card's existing rewards and protections for eligible disputes with businesses, for example when an item is defective." |
| 8 | OpenAI does not say who pays when the agent buys the wrong thing and you approved it | **REAL** | Not addressed on the announcement page. The CSA note makes the same observation |
| 9 | The best evidence of what you asked for now sits with the agent platform | **REAL (their analysis, paraphrased)** | CSA note: the most probative evidence of user intent "now sits with the agent platform rather than with the issuer or the merchant" |

"Their analysis" means the claim is the researchers' reading of current rules, not a court ruling.

## Corrections

None so far.
