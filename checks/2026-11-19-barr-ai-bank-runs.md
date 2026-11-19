# A Fed governor says AI agents could make bank runs "unfold in minutes"

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-19-barr-ai-bank-runs/) · **Checked:** 2026-11-19 · **Status:** all claims sourced

Michael Barr spoke on Nov 16 in Milan about AI and financial stability. Three days earlier the Fed's Financial Stability Report put AI at the top of its risk survey. We read both.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Barr warned AI agents could speed up bank runs to minutes | **REAL** | [Barr speech](https://www.federalreserve.gov/newsevents/speech/barr20261116a.htm), Nov 16: "AI agents may accelerate deposit outflows during stress periods" and could move funds "potentially accelerating runs that unfold in minutes, overwhelming traditional liquidity management and regulatory intervention timelines" |
| 2 | This is now the Fed's official view | **NOT CLAIMED** | Footnote 1: "The views expressed here are my own and are not necessarily those of my colleagues on the Federal Reserve Board or the Federal Open Market Committee" |
| 3 | AI was the top-cited risk in the Fed's stability report | **REAL** | [Financial Stability Report](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf), Nov 13, Box 5.1: "AI was the top-cited risk". It is a New York Fed survey of 23 contacts, and the box "should not be interpreted as representing the views" of the Board |
| 4 | 87% of contacts named AI | **REAL** | Same report, overview chart: AI at 87% of contacts in fall 2026, up from 50% in spring. 20 of 23 is 87.0% |
| 5 | AI-related off-balance-sheet obligations exceed $3 trillion | **REAL** | Speech: "now exceeds $3 trillion". FSR: not-yet-commenced leases over $1 trillion plus take-or-pay contracts and guarantees over $2 trillion, both undiscounted maximums |
| 6 | Public debt tied to advanced computing is over $1.1 trillion | **REAL** | FSR: "estimated at more than $1.1 trillion as of October 2026" |
| 7 | Barr warned traders using similar AI models could herd | **REAL** | Speech: traders relying on "a small set of similar AI models trained on similar data" face "the risk of herding behavior" |
| 8 | Barr expects big direct losses from AI debt | **NOT CLAIMED** | Speech: "I'm less concerned about direct losses". His worry is a sharp reversal leading to "rapid deleveraging" and fire sales |

## Reproduce

```python
print(round(20 / 23 * 100, 1))   # 87.0, the AI share of 23 contacts
print(1 + 2)                     # >$1T leases + >$2T other = >$3T
```

## Corrections

None so far. If you find an error, open an issue with the source.
