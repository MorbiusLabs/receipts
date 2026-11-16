# Banks froze today, "internet off" tomorrow

**Post:** [x.com/MorbiusLabs/status/2122439102033498395](https://x.com/MorbiusLabs/status/2122439102033498395) · **Checked:** 2026-11-16 · **Status:** all claims sourced

On Monday, Nov 16, 2026, customers of several large US banks reported problems at the same time. The same week, a rumor said the internet would go dark worldwide on Nov 17. We checked both.

| # | Claim | Verdict | Primary source |
|---|---|---|---|
| 1 | Chase, Bank of America, Wells Fargo and U.S. Bank customers reported problems on Nov 16 | **REAL** | Downdetector counts as reported by [Gizmodo](https://gizmodo.com/chase-bank-of-america-and-wells-fargo-are-experiencing-app-outages-2000840582) (updated 3:14 p.m. ET) |
| 2 | Chase passed 4,300 Downdetector reports | **REAL** | Same article: over 4,300 as of 1:27 p.m. ET. Bank of America passed 1,000. Wells Fargo, U.S. Bank and Zelle had hundreds each |
| 3 | Chase called it a technical issue, "not cyber related", and said customers can still reach their funds | **REAL** | Chase statement quoted by Gizmodo and others: "Due to a technical issue, some transactions are taking longer than usual to complete, but customers still have access to their accounts and funds." |
| 4 | Hackers will zero out bank accounts on Nov 17 | **FALSE** | The rumor started as one X post in Portuguese citing an unnamed dark web source. Its author said it was unconfirmed. No group, no technical detail, no evidence |
| 5 | The internet goes off for three months | **FALSE** | Same source. Nothing official supports it |
| 6 | A "super-powerful AI" will patch everything in the meantime | **FALSE** | Same source. Unexplained claim |
| 7 | What actually happens on Nov 17 is a nationwide Emergency Alert System test at 2:20 p.m. ET | **REAL** | [FCC public notice DA 26-989](https://docs.fcc.gov/public/attachments/DA-26-989A1.txt), released Sept 16, 2026. Backup date Dec 3 |
| 8 | The test runs on TV and radio, for about a minute, and does not involve the internet | **REAL** | Same notice lists EAS participants: radio, TV, cable, satellite, wireline video. FEMA describes about one minute, "This is only a test" |
| 9 | Fed governor Michael Barr said AI models have exploited the same weak spot human attackers use, many firms relying on one shared platform provider | **REAL** | [Speech, Nov 16, 2026, Milan](https://www.federalreserve.gov/newsevents/speech/barr20261116a.htm), section "AI and Cyber Risk" |
| 10 | That risk caused this outage | **NOT CLAIMED** | We did not link the two. Chase says the outage was not cyber related |
| 11 | Between noon and 3 p.m. ET, Bitcoin added 26 blocks and confirmed 135,656 transactions | **REAL** | mempool.space, blocks 976155 to 976180. Reproduce below |

## Reproduce claim 11

```bash
python3 scripts/btc_blocks_window.py 2026-11-16T17:00:00Z 2026-11-16T20:00:00Z
```

Output ends with `26 blocks (976155 to 976180), 135,656 transactions`. 17:00 to 20:00 UTC is noon to 3 p.m. Eastern. Block timestamps are set by miners and can be off by a few minutes.

## Corrections

None so far. If you find an error, open an issue with the source.
