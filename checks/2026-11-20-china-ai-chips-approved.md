# 879,868 AI chips approved for China. Approved is not shipped

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-china-ai-chips-approved/) · **Checked:** 2026-11-20 · **Status:** the headline numbers are sourced to the House committee; the per-company and shipping details come from Hunterbrook's reading of the Commerce table, which we could not open. Hunterbrook's fund is short AMD

On Nov 19 the chair of the House Foreign Affairs Committee made public Commerce Department data on license requests to export Nvidia and AMD AI chips to China. Headlines turned "approved" into "sold".

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Requests covered 3.4 million AI chips for China, and Commerce approved more than 879,000 | **REAL** | [House Foreign Affairs Committee](https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china), Nov 19: "requested sales of 3.4 million AI chips to China, and the approval of more than 879,000 by BIS". [Hunterbrook](https://hntrbrk.com/breaking-news/amd-china-congress) gives the table's exact totals: 3,444,160 requested, 879,868 approved in 21 applications. That is 25.5% |
| 2 | Approvals include companies on the Pentagon's Chinese military companies list | **REAL (their claim)** | Committee: approvals include "Department of War-designated Chinese Military Companies like Alibaba and Tencent" |
| 3 | The US let Nvidia and AMD ship hundreds of thousands of AI chips to China | **NOT CLAIMED** | The committee release speaks of approvals. Hunterbrook, reading the table: "None of the approved chips had shipped as of May 11, the table shows." What happened after May 11 is not in the data |
| 4 | The data shows the current picture | **FALSE** | Hunterbrook: the table covers Nvidia H200 and AMD MI325X applications "as of May 11, 2026", six months before the release |
| 5 | AMD accounts for about a third of the approvals | **REAL (their reporting)** | Hunterbrook: eight AMD applications of 75,000 chips each; "BIS approved four of AMD's applications. They covered 300,000 chips, or 34% of all chips approved." 300,000 / 879,868 = 34.1% |
| 6 | Congress accused Nvidia or AMD of breaking the rules | **NOT CLAIMED** | The release flags Nvidia requests that "depend on possible chip-smuggling fronts". Hunterbrook: "The House Committee did not accuse AMD or Nvidia of specific wrongdoing." AMD told the New York Times it "complied with applicable U.S. laws and regulations" (via Hunterbrook) |

## Reproduce

```python
requested, approved, amd = 3_444_160, 879_868, 4 * 75_000
print(round(approved / requested * 100, 1))   # 25.5% of requested chips approved
print(round(amd / approved * 100, 1))         # 34.1% of approvals were AMD's
```

## What would change this page

The Commerce table itself (we could not open the committee's PDF), and any data on shipments after May 11.

**Update, 2026-11-23:** Nvidia's CFO commentary for its fiscal third quarter says "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion." It gives dollars, not chip counts, so it does not tell us how many approved chips shipped. See [our check](https://morbiuslabs.org/p/2026-11-23-nvidia-hopper-china-2-4b/).

## Corrections

None so far. If you find an error, open an issue with the source.
