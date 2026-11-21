# Bitcoin touched $55,106 on Coinbase, its lowest since September 2024 and 56% below the peak

**Post:** site only, [morbiuslabs.org](https://morbiuslabs.org/p/2026-11-21-bitcoin-two-year-low/) · **Checked:** 2026-11-21 · **Status:** all claims sourced; prices are Coinbase Exchange BTC-USD candles (UTC days)

Bitcoin slid through Friday Nov 20 and into Saturday morning UTC. Outlets quote different lows because they use different venues and times. We used one venue, Coinbase Exchange, and its public candle data, so every number below can be pulled again.

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Bitcoin fell to its lowest level since September 2024 | **REAL** | [Coinbase Exchange hourly candles](https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=3600&start=2026-11-20T12:00:00Z&end=2026-11-21T16:00:00Z): low $55,106.00 in the 06:00 UTC hour on Nov 21. [Daily candles](https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=86400&start=2024-09-01T00:00:00Z&end=2024-09-30T00:00:00Z) from March 2024 on: the last day with a lower low was Sep 9, 2024 ($54,565.56) |
| 2 | It fell 5.10% to $55,830 | **REAL (their figures)** | Reuters, via [Global Banking & Finance Review](https://www.globalbankingandfinance.com/bitcoin-falls-3-57-56-814/): "It fell 5.10% to $55,830 by 11:13 p.m. ET on Friday (0413 GMT on Saturday), the lowest since September 2024." A snapshot on their venue; Coinbase went lower two hours later. [Trending Topics](https://www.trendingtopics.eu/bitcoin-55000-two-year-low-coinshares-capitulation/) says "about $55,300" |
| 3 | Bitcoin is down more than half from its peak | **REAL** | Coinbase daily candles: all-time high $126,296 on Oct 6, 2025. $55,106 is 56.37% below it |
| 4 | Friday's drop took bitcoin to its lowest since July | **OUR READ** | [Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-19-dow-sp-500-nasdaq-anthropic-nvidia-141644188.html) wrote it "dropped below $59,000 to trade at its lowest price since July", which fit the price at that moment. By the end of the UTC day the low was $57,655.17, below the Jul 1 low of $57,717.55, so Friday alone already reached a level last seen on Sep 17, 2024 ($57,620.27) |
| 5 | Worries over AI stock valuations drove the drop | **REAL (their analysis)** | Reuters: "worries over stretched valuations in artificial intelligence stocks rattled investors and weighed on other risk assets." Reuters' reading of the market, not flow data |
| 6 | Bitcoin fell about 5% on Friday | **REAL** | Reuters: "It fell 5.10%" (to its late-Friday snapshot). Coinbase: Nov 20 close $58,814.99 against $61,913.23 on Nov 19, down 5.00% for the UTC day. That close is 32.78% below the Dec 31, 2025 close of $87,497.94 |

## Reproduce

```python
import json, urllib.request, datetime as dt
def candles(start, end, gran=86400):
    u = f"https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity={gran}&start={start}&end={end}"
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})))
rows = {}
d = dt.datetime(2024, 3, 1)
while d < dt.datetime(2026, 11, 22):
    e = min(d + dt.timedelta(days=290), dt.datetime(2026, 11, 22))
    for c in candles(d.strftime("%Y-%m-%dT00:00:00Z"), e.strftime("%Y-%m-%dT00:00:00Z")):
        rows[c[0]] = c          # [time, low, high, open, close, volume]
    d = e
rs = sorted(rows.values())
day = lambda t: dt.datetime.utcfromtimestamp(t).date()
print(max(rs, key=lambda c: c[2])[2])                                          # 126296 (Oct 6, 2025)
print([(day(c[0]), c[1]) for c in rs if c[1] <= 55106 and day(c[0]) < dt.date(2026, 11, 21)][-1])     # 2024-09-09 54565.56
print([(day(c[0]), c[1]) for c in rs if c[1] <= 57655.17 and day(c[0]) < dt.date(2026, 11, 20)][-1])  # 2024-09-17 57620.27
print(round((55106 / 126296 - 1) * 100, 2))         # -56.37
print(round((58814.99 / 61913.23 - 1) * 100, 2))    # -5.0
print(round((58814.99 / 87497.94 - 1) * 100, 2))    # -32.78
```

## Corrections

None so far. If you find an error, open an issue with the source.
