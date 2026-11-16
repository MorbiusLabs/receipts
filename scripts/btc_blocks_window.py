#!/usr/bin/env python3
"""Count Bitcoin blocks and transactions mined inside a time window.

Uses the public mempool.space API. No dependencies, no API key.

    python3 btc_blocks_window.py 2026-11-16T17:00:00Z 2026-11-16T20:00:00Z

prints every block in the window and the totals. Block timestamps are set by
miners and can be off by a few minutes, so treat edges of the window with care.
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone

API = "https://mempool.space/api"


def get(path):
    req = urllib.request.Request(API + path, headers={"User-Agent": "receipts-script"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())


def ts(s):
    return int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    start, end = ts(sys.argv[1]), ts(sys.argv[2])
    # the last block at or before each edge
    first = get(f"/v1/mining/blocks/timestamp/{start}")["height"] + 1
    last = get(f"/v1/mining/blocks/timestamp/{end}")["height"]
    blocks = {}
    h = last
    while h >= first:                       # /v1/blocks/{h} returns up to 15 blocks ending at h
        for b in get(f"/v1/blocks/{h}"):
            if first <= b["height"] <= last:
                blocks[b["height"]] = b
        h -= 15
    total = 0
    for height in sorted(blocks):
        b = blocks[height]
        t = datetime.fromtimestamp(b["timestamp"], timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        pool = b.get("extras", {}).get("pool", {}).get("name", "")
        print(f"{height}  {t}  {b['tx_count']:>6} tx  {pool}")
        total += b["tx_count"]
    print(f"\n{len(blocks)} blocks ({first} to {last}), {total:,} transactions")


if __name__ == "__main__":
    main()
