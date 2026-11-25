# THE WORLD IN ONE DAY

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/AfrizalSek/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/AfrizalSek/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A make.fun entry for **news-image-20261125**: one picture that sums up the
world's news of Wednesday 25 November 2026.

## What the image shows

The image is a single-page newspaper, 1024 by 1024 pixels, holding 32
stories from 7 regions. The front page leads with three big stories:

- tankers on fire in the Strait of Hormuz after hitting naval mines;
- the United States putting new tariffs on 14 economies;
- Ukraine striking two Russian refineries overnight.

Under the headlines sit smaller stories from every region, a timeline of
the day in UTC, a world map with numbered pins for the main stories, and
a "DATE CHECK" strip at the foot of the page that states plainly that
every story on the page happened, or was first reported, on 25 November
2026 — along with the near-miss stories from other days that were left
out on purpose. A "HOW SURE" key marks each claim by how solid it is:
confirmed, official, reported, or a claim from one side only.

## How it works

The finished image is stored in this repository as `entry.png`. The
program `main.py` does one thing: it copies that file to
`/output/entry.png`. It uses only the Python standard library, never
touches the network, and writes the same bytes every time it runs.

## Running it

```sh
python3 main.py
```

The image lands at `/output/entry.png`. To send it somewhere else while
testing locally, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the newspaper image itself (1024×1024, 205,234 bytes).
- `main.py` — the entrypoint; copies `entry.png` to `/output/entry.png`.
- `SOURCES.md` — where each story came from.
- `LICENSE` — the MIT license.

## Verification

Running `main.py` twice writes the same bytes both times: the output
matches `entry.png` in this repository with sha256
`50084afb1a9510f28eadbc38d62f06701feb3e3394ff467e1d4583778bd326e4`.

## License

MIT. See `LICENSE`.
