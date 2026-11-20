# Czech central bank: a model alone forecasts GDP about as well as its economists, not better

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-cnb-ai-gdp-forecast/) · **Checked:** 2026-11-20 · **Status:** all claims sourced from the speech; the CNB blog with the method was not opened

Aleš Michl, Governor of the Czech National Bank, spoke at Kyoto University on Nov 13. BIS posted the text on Nov 19 under the title "AI forecasts GDP as well as economists". The figures come from the bank's own contest, as he describes it.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | In the CNB's contest, economists missed GDP by 0.21 points on average and the model alone by 0.22 | **REAL (their figures)** | [BIS, speech by Aleš Michl](https://www.bis.org/speeches/20261119-ai-forecasts-gdp-well-economists): "the average error of our economists was 0.21 percentage points. The machine alone: 0.22." The task is a forecast for the current quarter |
| 2 | AI beats the economists | **FALSE** | By the bank's own numbers the economists are ahead by 0.01 points. Michl: "Today the machine alone is as good as our economists". "Soon, I bet, it will be better" is a bet, not a result |
| 3 | The test is live, not a backtest on old data | **REAL (their claim)** | Speech: running "since 2023", and "The fight takes place in practice, not on past data". Same quarter, same data, same day |
| 4 | It is a machine against a human | **OUR READ** | Not quite. The economists side uses "all our models plus the judgement of our economists". The other side is one Random Forest model "with no human touching it". In his words it is "machine alone against human plus machine" |
| 5 | The test shows how many quarters were compared | **NOT CLAIMED** | The speech gives no sample size and no spread of errors. Michl says the details are in a new CNB blog, which we did not open. With so few quarters since 2023, a 0.01-point gap says little either way |
| 6 | The Czech central bank holds bitcoin | **REAL (their claim)** | Speech: a test portfolio launched in November 2025 of "bitcoin, dollar stablecoins and a tokenised deposit". Size: "1 million dollars – 0.0006% of our assets", run by a lab separate from monetary policy |

## Reproduce

```python
print(round(0.22 - 0.21, 2))   # 0.01 percentage points, in the economists' favour
```

## Corrections

None so far. If you find an error, open an issue with the source.
