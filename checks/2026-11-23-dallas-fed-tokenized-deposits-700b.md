# "Tokenized deposits could drain $700 billion from bank lending"? That is not what the Dallas Fed number measures

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-23-dallas-fed-tokenized-deposits-700b/) · **Checked:** 2026-11-23 · **Status:** all claims sourced to the Dallas Fed article

Two Dallas Fed economists, Rosie Levy and Srini Ramaswamy, published "Tokenized deposits could affect bank liquidity, maturity transformation" on Aug 25, 2026. Coverage ran under headlines like Decrypt's "Tokenized Deposits Could Drain $700 Billion From Bank Lending, Dallas Fed Warns". The paper matters for AI agents that move money, which is why we read it.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Tokenized deposits could weaken how banks fund long-term loans | **REAL (their analysis)** | [Dallas Fed](https://www.dallasfed.org/research/economics/2026/0825): "significant tokenized deposit adoption could meaningfully affect bank maturity transformation", the use of on-demand deposits to fund longer-term assets |
| 2 | Tokenized deposits could drain $700 billion from bank lending | **FALSE** | The $700 billion is not lending and not deposits leaving. The paper: "a 10 percent increase in the price sensitivity of deposits (deposit rate beta) would result in a reduction of $700 billion 10-year equivalents of duration risk appetite from banks (assuming a deposit WAL of four years)". It is a what-if on interest-rate risk capacity. [Decrypt](https://decrypt.co/376609/tokenized-deposits-bank-lending-dallas-fed)'s own article body says "interest-rate risk capacity"; its headline says "bank lending" |
| 3 | AI agents could move your deposits to another bank without you lifting a finger | **REAL (their analysis)** | "Development of agentic artificial intelligence, along with programmable features of deposit tokens (smart contracts), could theoretically allow this switching to occur without requiring direct action from the deposit holder." Note "theoretically" |
| 4 | Borrowing could get more expensive | **REAL (their analysis)** | If banks replace sticky deposits with term debt, that lending "would likely adversely impact the cost of credit for consumers and businesses" |
| 5 | Most of the interest-rate risk banks carry rests on deposits | **REAL (their figures)** | "about 80 percent of the duration risk taken by banks ($5.8 trillion 10-year equivalents out of $7 trillion total) in the aggregate is supported by the duration characteristics of deposits". A back-of-the-envelope estimate, in the authors' words |
| 6 | This is the Federal Reserve's view | **FALSE** | "The views expressed are those of the authors and should not be attributed to the Federal Reserve Bank of Dallas or the Federal Reserve System." |

## Reproduce

```python
print(round(5.8 / 7 * 100))   # 83: the "about 80 percent" of duration risk supported by deposits
```

## Corrections

None so far. If you find an error, open an issue with the source.
