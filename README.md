# pocket-gambit

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ximing2026/pocket-gambit/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ximing2026/pocket-gambit/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4,093 bytes of Python: 0x88 board, negamax alpha-beta with iterative deepening under a fixed node budget, quiescence over captures, promotions and check evasions, a transposition table, and hand-tuned piece-square tables. Deterministic by construction — same position, same move, every replay. Practice gauntlet: 1191 and 1364 Elo across two trial fields against the house engines.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18081 MAKEFUN_PROMPT_FILE=prompt.txt python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sz0e39g7&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
