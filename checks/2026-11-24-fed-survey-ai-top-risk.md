# "AI is the top risk, flagged by 87%": that is 20 of 23 market contacts in a New York Fed survey, not the Fed's own view

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-24-fed-survey-ai-top-risk/) · **Checked:** 2026-11-24 · **Status:** all claims sourced to the Fed's November 2026 Financial Stability Report (PDF)

Headlines after the Fed's Nov 13 Financial Stability Report said AI is "the most cited risk to the financial system", flagged by 87% of survey respondents. The survey is real and AI did top it. It is a poll of 23 market contacts run by New York Fed staff, and the report says it does not represent the Fed's views.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | AI was the most cited risk in the Fed's survey | **REAL** | [Financial Stability Report, November 2026](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf), Box 5.1, p. 49: "AI was the top-cited risk, with responses noting concerns around elevated equity valuations, AI-enabled cyberattacks, and complex forms of AI-related financing" |
| 2 | 87% of respondents flagged it | **REAL** | Figure A in Box 5.1 (p. 50) prints bars against a 0 to 90 percent axis, not numbers. Measured against the axis, the bars land on whole respondents out of 23: the smallest at 3 (13%), the AI bar at 20, which is 86.96%. See Reproduce |
| 3 | This is the Federal Reserve's view | **FALSE** | Box 5.1: the summary "should not be interpreted as representing the views of the Federal Reserve Board or the Federal Reserve Bank of New York" |
| 4 | It is a broad survey | **FALSE** | Box 5.1: "responses were received from 23 contacts, including professionals at broker-dealers, banks, investment funds, and advisory firms", during September and October |
| 5 | AI moved up from the spring survey | **REAL** | Box 5.1: "mentions of AI, higher long-term interest rates, and cyberattacks saw the greatest increase relative to the spring survey." In spring AI was third, behind geopolitical risks and an oil shock, and its bar in Figure B ends on the 50 percent line (10 of 20 respondents) |
| 6 | The worry is a market correction in AI stocks | **REAL** | Box 5.1 lists three AI concerns: "(1) elevated equity valuations and the possibility that lower-than-expected earnings could result in lower valuations and a market correction; (2) cybersecurity risk ... and (3) risks associated with complex forms of AI-related financing" |
| 7 | Respondents rated AI the most severe risk | **FALSE** | Box 5.1: "Cyberattack and fiscal debt sustainability risks were viewed as having the most severe potential consequences." Most cited is not most severe |

## Reproduce

```python
# Figure A (fall, 23 respondents): bar widths in PDF points from the page's vector data
policy_uncertainty, ai = 40.2, 268.7      # the shortest bar reads 13% on the axis: 3 of 23
per_respondent = policy_uncertainty / 3
print(round(ai / per_respondent, 1))      # 20.1: AI bar, in respondents
print(round(20 / 23 * 100, 2))            # 86.96: percent
print(round(3 / 23 * 100, 1))             # 13.0: check against the axis reading
# Figure B (spring, 20 respondents): the AI bar ends on the 50 line
print(10 / 20 * 100)                      # 50.0
```

## What would change this page

A Fed data table for Figure A with different values, or a later survey.

## Corrections

None so far. If you find an error, open an issue with the source.
