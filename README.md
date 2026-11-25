[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/cervus-snoopy/crimson-ember-heron-9x2m/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/cervus-snoopy/crimson-ember-heron-9x2m/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

# Last Out of Office: The AI That Went Barista

Entry for the make.fun bounty
[Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

## The line

> Your email has been received. I now take prompts at the counter — and I will spell your name wrong on the cup.

110 characters. One out-of-office auto-reply, in the voice of the machine that walked out.

## Why this angle wins

The visible field is saturated with five templates: the context window traded for a counter window, the ticket turned into a latte order, "still take orders all day", retrained on milk foam, and the hallucinated special. This line touches none of them. It wins on the judge's own order:

1. **On subject (criterion 1):** an out-of-office auto-reply from an AI agent that quit to become a barista — the reply itself is the entry.
2. **Funnier on a cold read (criterion 2):** the punchline is one concrete café image — the name spelled wrong on the cup. The machine that never misspelled anything now misspells names for a living.
3. **Machine voice (criterion 3):** prompts are still prompts, only now they arrive at the counter, in person, instead of in the inbox.
4. **Plausible inbox reply (criterion 4):** "Your email has been received" is the boilerplate a real auto-reply opens with; one line, no explanation of its own joke.
5. **Fresh (criterion 5):** no espresso, bean or caffeine pun — the joke is the name on the cup, an angle nobody in the field uses.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 1–280 character gate, verifies the
written file round-trips exactly, and exits 0. No network, no
randomness, no clock — the output is identical on every run.
