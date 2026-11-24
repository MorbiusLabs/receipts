# Nvidia's board brought Jensen Huang back 10 days after he resigned. The stock rose 31.5%, its best day since May 2003

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-24-nvidia-huang-reinstated/) · **Checked:** 2026-11-24 · **Status:** all claims sourced to Nvidia's SEC filing, Nasdaq and Yahoo price data, and Reuters

On Nov 22 Nvidia's board reinstated Jensen Huang as President, CEO and director, effective immediately. Nvidia announced it on Nov 23 and filed the release with the SEC. The stock closed up 31.5% that day. Five days earlier the board chair had said the board did not intend to bring him back.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Nvidia's board reinstated Jensen Huang as CEO | **REAL** | [Nvidia 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000090/nvda-20261122.htm), Item 5.02: "On November 22, 2026, the Board of Directors of NVIDIA Corporation reinstated Jen-Hsun Huang as NVIDIA's President, Chief Executive Officer and member of the Board of Directors, effective immediately." The [press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000090/nov23pressrelease.htm) is dated Nov 23 and says the board "voted unanimously" |
| 2 | It came 10 days after he resigned | **REAL** | Nvidia's [Nov 12 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm): "Jensen Huang has resigned as President, Chief Executive Officer, and a member of the Board, effective immediately." Nov 12 to Nov 22 is 10 days |
| 3 | Five days earlier the board said it would not bring him back | **REAL (their reporting)** | Board chair Harvey Jones on Nov 17, quoted by [Reuters](https://finance.yahoo.com/news/nvidia-board-forms-committee-national-102208048.html): "The Nvidia board unanimously accepted his resignation and does not intend to reinstate Jensen as CEO." See [our Nov 18 check](https://morbiuslabs.org/p/2026-11-18-nvidia-q3-without-huang/#claim-8) |
| 4 | Nvidia rose 31.5% on Nov 23 | **REAL** | [Nasdaq historical data](https://www.nasdaq.com/market-activity/stocks/nvda/historical): close $165.05 against $125.53 on Nov 20, up 31.48%, on 783 million shares. Yahoo Finance shows the same closes |
| 5 | It was Nvidia's best day since 2003 | **REAL** | Daily closes from [Yahoo Finance](https://finance.yahoo.com/quote/NVDA/history/) since 2001: the only bigger one-day gain was 33.06% on May 9, 2003. The next biggest after Nov 23 is 29.81% on Nov 11, 2016 |
| 6 | The day added about $952 billion in market value | **REAL** | Our math: 24.1 billion shares on the cover of Nvidia's [latest 10-Q](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001045810&type=10-Q) (as of Aug 21, 2026) times the $39.52 rise. The share count moves a little between filings, so treat it as an estimate |
| 7 | The stock has made back what it lost since Huang left | **FALSE** | The $165.05 close is 13.1% above the Nov 19 close of $145.98, before the SEC report, but still 5.0% below the Nov 11 close of $173.73, the day before the resignation, and 19.4% below the Oct 30 close of $204.64 |
| 8 | The US government cleared Huang | **NOT CLAIMED** | The release says the board "received input from senior levels of the United States government, and based on that input, the Board is confident that Mr. Huang's reinstatement poses no national security risk." That is the board's conclusion. We found no government statement |
| 9 | The investigations are over | **FALSE** | Release: the independent committee's investigation into reports that Huang was "the target of a foreign intelligence effort" "will proceed to conclusion", and "NVIDIA will continue to cooperate with ongoing government investigations and inquiries." See [our SEC probe check](https://morbiuslabs.org/p/2026-11-20-nvidia-sec-probe-report/) |
| 10 | Nvidia added new oversight with the return | **REAL** | Release: a "National Security and Export Control Committee comprised solely of independent directors", and a search for a new "Chief Compliance Officer" who will report to the Nominating and Corporate Governance Committee |
| 11 | Colette Kress goes back to being CFO only | **REAL** | 8-K: "Ms. Kress will continue to serve as NVIDIA's Executive Vice President and Chief Financial Officer." She had been interim CEO since Nov 12 |
| 12 | The Nasdaq rose 6.5% the same day | **REAL (their figures)** | Yahoo Finance index data: 24,089.56 against 22,617.73 on Nov 20, up 6.51%. FRED had not yet posted Nov 23 when we checked |

## Reproduce

```python
nov11, oct30, nov19, nov20, nov23 = 173.73, 204.64, 145.98, 125.53, 165.05
print(round((nov23 / nov20 - 1) * 100, 2))        # 31.48: the day's gain
print(round(24.1e9 * (nov23 - nov20) / 1e9, 1))   # 952.4: billions of dollars added
print(round((nov23 / nov19 - 1) * 100, 2))        # 13.06: above the pre-report close
print(round((nov23 / nov11 - 1) * 100, 2))        # -5.0: below the pre-resignation close
print(round((nov23 / oct30 - 1) * 100, 2))        # -19.35: below Oct 30
print(round((24089.56 / 22617.73 - 1) * 100, 2))  # 6.51: Nasdaq Composite
```

## What would change this page

The committee's findings, an SEC statement or an Nvidia 10-Q disclosure about the inquiries, or a revised share count that moves claim 6.

## Corrections

None so far. If you find an error, open an issue with the source.
