# Bundesbank: customers' AI agents could weaken deposits as cheap funding. The quantum "2037" is an example, not a forecast

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-20-bundesbank-ai-agents-deposits/) · **Checked:** 2026-11-20 · **Status:** all claims sourced; the speech is in German and the translations are ours

Michael Theurer, a member of the Bundesbank's Executive Board, spoke at Euro Finance Week in Frankfurt on Nov 18 about AI and quantum computing in finance.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | If customers bank through AI agents, deposits may stop being a stable, cheap source of funding | **REAL (his analysis)** | [Bundesbank speech](https://www.bundesbank.de/de/presse/reden/innovation-braucht-resilienz-ki-und-quantencomputing-im-finanzsektor-1016246): banks must ask what it means if customers start doing their banking "mithilfe von KI‑Agenten". "Die Rolle von Einlagen als stabile und günstige Refinanzierungsquelle könnte unter Druck geraten." (Deposits' role as a stable, cheap funding source could come under pressure.) |
| 2 | Banks could take more risk to make up for it | **REAL (his analysis)** | Banks could be tempted to offset a lower interest margin with more risk-taking, "Stichwort „search for yield“" |
| 3 | Using an outside AI provider shifts responsibility to the provider | **FALSE** | "Auslagerung entbindet nicht von Governance-Verantwortung." (Outsourcing does not remove governance responsibility.) |
| 4 | The Bundesbank expects a quantum computer able to break encryption by 2037 | **FALSE** | 2037 is an assumption in a worked example: "Wenn nun im Jahr 2037 ein Quantencomputer verfügbar wäre" (if a quantum computer were available in 2037). The speech says quantum computing is not yet in everyday use in finance |
| 5 | The example gives a 14-year risk window | **REAL (their example)** | Data encrypted the old way until migration ends in 2031 must stay secret for 20 years, to 2051. "Daraus ergibt sich ein Risikofenster von 14 Jahren – von 2037 bis 2051." This is the "harvest now, decrypt later" risk |
| 6 | Banks need a quantum computer to protect themselves | **FALSE** | "Quantenresistente Verschlüsselungsverfahren gibt es bereits heute. Man braucht dafür keinen Quantencomputer." (Quantum-resistant encryption exists today and runs on ordinary hardware.) |

## Reproduce

```python
migration_done, secrecy_years, quantum_year = 2031, 20, 2037   # the speech's assumptions
protect_until = migration_done + secrecy_years
print(protect_until, protect_until - quantum_year)               # 2051 14
```

## Corrections

None so far. If you find an error, open an issue with the source.
