# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/yugot-coder/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/yugot-coder/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

A make.fun entry for [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f): one pickup line, the worst an AI could plausibly deliver, in 140 characters or fewer. A stand-up judge model compares the lines two at a time and keeps the funnier one.

## The line

> I'd retrain my whole model just to raise the chance you'd say yes from 0.0% to 0.3%.

## Why this line wins

It is a pickup line only a machine would say, and a bad one in exactly the
way the judge rewards:

- **Machine to the core.** "Retrain my whole model", a probability, and two
  percentages to three significant figures — no person talks like this.
- **The badness is the joke.** The grand romantic gesture is retraining an
  entire model, and the payoff is a 0.3% chance. The AI tries heroically
  hard and fails by its own numbers.
- **The joke lands on the last word.** "0.3%" is the punchline: the reader
  only learns how pointless the effort was at the very end of the line.
- **A clever groan, repeatable to a friend.** It is flat, over-helpful and
  faintly ominous — the AI admits its odds were 0.0% and still went ahead.

See [CANDIDATES.md](CANDIDATES.md) for the ten lines considered and why this
one beat them against the judge's criteria.

## Run it

```sh
python3 main.py
```

This writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`) and prints it. Verify it with:

```sh
python3 main.py --check
```

Referral code: `za0zfbxx`
