# Fed Vice Chair Jefferson: AI is adding to demand and prices now, its productivity payoff is "limited" so far

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-jefferson-ai-prices-productivity/) · **Checked:** 2026-11-20 · **Status:** all claims sourced from the speech

Philip N. Jefferson, Vice Chair of the Federal Reserve, spoke at UC San Diego on Nov 13. BIS reposted the speech on Nov 19. He describes the AI boom as a demand story today and a productivity story that has not arrived yet.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The AI boom is pushing prices up now | **REAL (his analysis)** | [Fed speech](https://www.federalreserve.gov/newsevents/speech/jefferson20261113a.htm): much of the rise in stock prices is tied to AI, "That added wealth appears to be raising household spending." Along with data-center investment, "This spending is putting upward pressure on resource utilization and the general price level." |
| 2 | AI's contribution to productivity is small so far | **REAL (his analysis)** | "the evidence so far appears consistent with a contribution to aggregate productivity that is limited, but with the potential to grow quite substantially". The size and timing "remain highly uncertain" |
| 3 | AI lifted sales per employee by about 0.5% in three years | **REAL (their survey)** | Jefferson cites a survey of senior managers (NBER Working Paper 34836) that "estimated that AI has boosted sales per employee by just 1/2 percent over the past three years" |
| 4 | The Fed says AI caused the recent productivity jump | **FALSE** | Productivity "averaged 2.2 percent between 2020 and 2025", against "the modest 1.5 percent" in the previous cycle. But "it's too early to say what role AI played", and the surge "began before the debut of popular AI chatbots in 2022" |
| 5 | 95% of US firms use AI | **FALSE** | The Census survey he cites: "as of October 2026, roughly 25 percent of all U.S. firms" use it in at least one business function. The 95% in his footnote is an employment-weighted rate from one study, which counts big employers more |
| 6 | 40% to 50% of working adults use AI on the job | **REAL (their surveys)** | "40 to 50 percent of working adults are using the technology in their jobs". He adds that only "a modest fraction uses it every day" |
| 7 | Jefferson signaled a rate move because of AI | **NOT CLAIMED** | He says faster productivity would mean "the neutral rate would likely rise", then that predicting it "is challenging", and that inflation is "the more important signal". 12-month PCE inflation "was 3.6 percent in September" |
| 8 | This is the Fed's official view | **FALSE** | Footnote 1: the views "are my own and are not necessarily those of my colleagues" on the FOMC |
| 9 | He said it again a week later | **REAL** | [Jefferson, Nov 19](https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm): "Currently, the AI buildout is exerting upward pressure on demand and inflation." |

## Reproduce

```python
print(round(2.2 - 1.5, 1))   # 0.7 points a year faster productivity, 2020-2025 vs the prior cycle
print(round(3.6 - 2.0, 1))   # PCE inflation 1.6 points above the 2% target in September
```

## Corrections

None so far. If you find an error, open an issue with the source.
