# Nvidia shipped $2.4 billion of Hopper chips to China last quarter, 2.2% of its data center revenue

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-23-nvidia-hopper-china-2-4b/) · **Checked:** 2026-11-23 · **Status:** the $2.4 billion and the outlook are sourced to Nvidia's SEC filings; the "halted shipments" remark is Yahoo Finance's account of the interim CEO, and we have not opened a transcript

Yahoo Finance reported on Nov 22 that interim CEO Colette Kress said Nvidia booked $2.4 billion from Hopper chip sales to China in its fiscal third quarter and has "halted shipments of those chips to Chinese firms". We read Nvidia's filed results. This adds a shipped figure to [our Nov 20 check on approved chips](https://morbiuslabs.org/p/2026-11-20-china-ai-chips-approved/).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Nvidia shipped $2.4 billion of Hopper data center chips to China in its fiscal third quarter | **REAL** | [Nvidia CFO commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27cfocommentary.htm), filed with the SEC: "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion." |
| 2 | China is a small part of Nvidia's data center business | **OUR READ** | The same filing: "Data Center revenue for the third quarter was a record $107.6 billion". $2.4 billion is 2.23% of that, and 2.07% of total revenue of $115.8 billion |
| 3 | Nvidia's outlook counts no China data center revenue | **REAL** | CFO commentary: "We are not assuming any Data Center compute revenue from China in our outlook." The [press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27pr.htm) says the same |
| 4 | Nvidia has halted Hopper shipments to Chinese firms | **WATCH** | [Yahoo Finance](https://finance.yahoo.com/markets/article/a-battered-stock-market-looks-for-the-bottom-what-to-watch-this-week-100000117.html) attributes it to Kress: the company "has halted shipments of those chips to Chinese firms". The filings we opened do not say "halted". They say only that the outlook assumes no China revenue |
| 5 | The $2.4 billion shows how many of the 879,868 approved chips were shipped | **NOT CLAIMED** | The filing gives dollars, not units, and does not mention the export license data |

## Reproduce

```python
china, dc, total = 2.4, 107.6, 115.8   # $ billions, Q3 fiscal 2027, Nvidia CFO commentary
print(round(china / dc * 100, 2))      # 2.23: share of data center revenue
print(round(china / total * 100, 2))   # 2.07: share of total revenue
```

## What would change this page

An earnings call transcript with Kress's exact words on halting shipments, or the 10-Q restating the figure.

## Corrections

None so far. If you find an error, open an issue with the source.
