# A bitcoin miner sold every coin for an AI data center and warns it may not have the cash to finish

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-19-hyperscale-btc-ai-cash/) · **Checked:** 2026-11-19 · **Status:** all claims sourced from the company's 10-Q

Hyperscale Data (NYSE American: GPUS) is turning a former mining site in Dowagiac, Michigan into an AI facility. Its quarterly report, filed Nov 18, explains the money.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The company warns of substantial doubt about continuing as a going concern | **REAL** | [Form 10-Q](https://www.sec.gov/Archives/edgar/data/896493/000121465926014565/hd111226110q.htm), Q3 2026: the conditions "raise substantial doubt about the Company's ability to continue as a going concern", and the doubt "has not been alleviated" |
| 2 | It sold all its bitcoin | **REAL** | Same filing: "On November 6, 2026, the Company sold all of its Bitcoin holdings, totaling approximately 211.6 Bitcoin, for gross proceeds of approximately $ 16.0 million". 208.4 of them were pledged for convertible notes it then repaid |
| 3 | It still needs $74.8 million to finish the AI build by March | **REAL** | Same filing: total cost about $122.1M, $47.3M paid through Oct 31, about $74.8M left: $27.4M in Nov and Dec, $47.4M in Q1 2027 |
| 4 | The AI deal is worth $1.2 billion | **REAL (only with extensions)** | Same filing: "assuming the Customer elects to exercise the two five-year extension options, the total contract value to the Provider is approximately $1.2 billion", subject to the company meeting its obligations |
| 5 | It had $17 million in cash against $231 million of current liabilities | **REAL** | Same filing, Sept 30 balance sheet: cash $17,295,000; total current liabilities $231,248,000; total current assets $103,154,000 |
| 6 | AI was behind the decision to sell | **OUR READ** | The filing ties the cash need to the Michigan AI build. It does not say the bitcoin was sold to fund it; part of the proceeds repaid the notes the coins secured |

## Reproduce

```python
print(round(122.1 - 47.3, 1))            # 74.8 left to pay
print(round(27.4 + 47.4, 1))             # 74.8, by period
print(round(16.0e6 / 211.6))             # ~75,614 USD per BTC on Nov 6
print(round((231_248_000 - 103_154_000) / 1e6, 1))  # 128.1M more current liabilities than current assets
```

## Corrections

None so far. If you find an error, open an issue with the source.
