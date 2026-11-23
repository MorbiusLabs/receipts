# DOJ: North Korea used "super intelligence" deepfakes in fake video calls. The $6 billion Binance theft is a separate case

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-23-doj-facestealer-super-intelligence/) · **Checked:** 2026-11-23 · **Status:** all claims sourced to the Justice Department release of Nov 12, 2026

On Nov 12 the Justice Department announced two actions against North Korean crypto theft: the takedown of infrastructure behind a fake video call scheme the FBI calls "FaceStealer", and the seizure of part of the crypto stolen from Binance on Oct 29. The release calls FaceStealer a "North Korean Super Intelligence-Enabled Social Engineering Campaign". That line is easy to read as "AI hacked Binance". The release says something narrower.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | North Korean hackers use "super intelligence" to make deepfake videos for fake video meetings | **REAL (their claim)** | [DOJ](https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-north-koreas-massive-theft-cryptocurrency): "The North Korean hackers also use super intelligence (SI) to develop deepfake videos of well-known and influential individuals often in the cryptocurrency and web3 industries". The meetings also replay recorded webcam video of earlier victims, then a fake "fix" for a sound problem installs malware |
| 2 | FaceStealer has stolen more than $400 million | **REAL (their figures)** | DOJ: the scheme "has resulted in the theft of more than $400 million in the last 18 months" |
| 3 | North Korea's military stole more than $6 billion from Binance on Oct 29 | **REAL (their claim)** | DOJ: "members of the North Korean military, referred to by the FBI as “TraderTraitor” stole more than $6 billion worth of virtual assets from the Binance cryptocurrency exchange." This is the government's attribution |
| 4 | The deepfake campaign was used to hack Binance | **NOT CLAIMED** | DOJ opens the Binance section with "Separately from the FaceStealer campaign". Nothing in the release ties the deepfakes or "SI" to the Binance theft |
| 5 | More than $2.7 billion of the Binance theft is frozen, and more than $1.2 billion seized or restrained | **REAL** | DOJ: "the freeze of more than $2.7 billion, with the Department having already obtained court-authorization to seize or restrain in excess of $1.2 billion of that amount." That is at least 45% of the theft frozen and 20% seized or restrained. The Criminal Division says it halted "about half" |
| 6 | "Super intelligence" here means a superintelligent AI | **OUR READ** | The release uses "super intelligence (SI)" as its own term and does not define it. It shows that the hackers used AI tools to make deepfakes, not that superintelligence exists |
| 7 | The FBI has seized victims' webcam recordings | **REAL** | DOJ: "Pursuant to a federal warrant, the FBI seized over 900 webcam videos of FaceStealer victims." |

Binance, quoted by The Block in [our Nov 17 check](https://morbiuslabs.org/p/2026-11-17-binance-hack-ai/), said it froze or intercepted about $2.85 billion. That is a different count from a different source than DOJ's $2.7 billion "collective" freeze, so we do not add or compare them. The FBI's resource page, www.fbi.gov/facestealer, was not opened for this check.

## Reproduce

```python
theft, frozen, seized = 6.0, 2.7, 1.2   # $ billions, all "more than" in the DOJ release
print(round(frozen / theft * 100))      # 45: share of the theft frozen, a lower bound
print(round(seized / theft * 100))      # 20: share of the theft seized or restrained
print(round(seized / frozen * 100))     # 44: share of the frozen amount seized or restrained
```

## What would change this page

An FBI or DOJ document that defines "SI", or one that links FaceStealer to the Binance breach.

## Corrections

None so far. If you find an error, open an issue with the source.
