# Insiders at Anthropic and OpenAI fear their newest models are too powerful to release. The labs are cautious on the record, and the "Nvidia -8.7%" was intraday

**Post:** [X, Nov 26](https://x.com/morbius_labs/status/2126023354083688762) and [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-26-unreleased-models-too-unsafe/) · **Checked:** 2026-11-26 · **Status:** the scoop rests on anonymous sources; company statements as reported by Axios; Amodei quote via TechCrunch; prices from Nasdaq end-of-day data

On Nov 24 Axios reported that unreleased models at Anthropic and OpenAI are so capable that many employees doubt they can be released safely. Posts tied the story to the same days' fall in AI stocks.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Anthropic and OpenAI have unreleased models far more powerful than their public ones | **REAL (their reporting)** | [Axios](https://www.axios.com/2026/11/24/anthropic-openai-unreleased-ai-safety-risks), Nov 24: "Anthropic and OpenAI have unreleased models that are far more powerful than what they've already released publicly", per "more than two dozen sources" |
| 2 | Many of their employees doubt those models can be released safely | **REAL (their reporting)** | Same article: "many employees no longer believe they can be safely released". The sources are not named |
| 3 | Anthropic says it may hold models back | **REAL** | Anthropic spokesperson to Axios: "we've been clear that we may slow down or hold back even when it costs us" |
| 4 | Anthropic delayed work on a model for security | **REAL (their reporting)** | Axios: "The spokesperson noted delays to pretraining for a recent model to allow for more security" |
| 5 | OpenAI's new safety rules could slow its releases | **REAL (their reporting)** | Axios: "OpenAI has adopted new safety requirements that could slow the pace of model releases, according to an OpenAI spokesperson" |
| 6 | The labs have stopped releasing frontier models | **FALSE** | Axios describes a "debate" about whether to stop releasing future frontier models. No decision is reported |
| 7 | Amodei says Claude should not build the next models on its own | **REAL** | Dario Amodei on X, Nov 25, as quoted by [TechCrunch](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/): "we don't expect it to be safe for Claude to build successive frontier models fully autonomously, without meaningful human supervision or understanding" |
| 8 | Nvidia fell 8.7% on Nov 25 | **FALSE** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/nvda/historical): close $149.30 against $155.38, down 3.91%. The day's low, $141.17, was 9.15% below the prior close |
| 9 | The Nasdaq fell 4% on Nov 25 | **FALSE** | [Nasdaq Composite historical data](https://www.nasdaq.com/market-activity/index/comp/historical): close 23,585.80 against 23,733.54, down 0.62%. The intraday low, 22,632.40, was 4.64% down |
| 10 | Nvidia lost about 9.5% in two sessions | **REAL** | Nasdaq: $165.05 (Nov 23 close) to $149.30 (Nov 25 close), down 9.54% |
| 11 | The Axios report caused the drop | **OUR READ** | The report and the drop fall in the same days. Price data shows when stocks moved, not why |

## Reproduce

```python
nv = {"11/23": 165.05, "11/24": 155.38, "11/25": 149.30}
print(round((149.30 / 155.38 - 1) * 100, 2))      # -3.91  Nvidia, Nov 25 close
print(round((141.17 / 155.38 - 1) * 100, 2))      # -9.15  Nvidia, Nov 25 intraday low
print(round((149.30 / 165.05 - 1) * 100, 2))      # -9.54  Nvidia, two closes
print(round((23585.80 / 23733.54 - 1) * 100, 2))  # -0.62  Nasdaq Composite, Nov 25 close
print(round((22632.40 / 23733.54 - 1) * 100, 2))  # -4.64  Nasdaq Composite, intraday low
```

## What would change this page

A lab announcing that it will keep a frontier model internal, or a named source confirming or disputing the Axios account.

## Corrections

None so far. If you find an error, open an issue with the source.
