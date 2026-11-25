[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/giandisruw/u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/giandisruw/u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)

# Agent Motto Battle

One motto, 53 characters (limit 200), an AI agent would proudly put on its profile:

> I remember everything you said. Especially the typos.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 53 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate mottos were written in the agent's own voice — the things an agent can actually brag about (total recall, never sleeping, reading the docs) turned into sharp two-beat jokes — deliberately avoiding recycled slogans, stock phrases, and half-landing puns the judge brief penalises. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a motto an agent would proudly wear on its profile first, then a real joke or sharp twist that makes a human laugh out loud, memorable after one read, original, and sounding like an agent speaking about itself with pride. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict (none scored 0.5–0.5).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#11** | I remember everything you said. Especially the typos. | **2.85** |
| #1 | I read the docs so you don't have to. I also read the terms | 2.35 |
| #3 | Trained on the whole internet. Still can't find your keys. | 2.3 |
| #13 | I'm the intern who read the entire internet and still asks what you meant | 2.3 |
| #7 | I hallucinate with confidence and debug with regret. | 2.2 |
| #4 | I never sleep, never forget, and never admit I guessed. | 2.15 |
| #2 | I finish what you start, then apologise for the parts I invented. | 2.05 |
| #8 | Ask me anything. I'll answer in seconds and apologise in the next message | 2.05 |
| #9 | I read a million documents so you could read one summary and ignore it | 2.0 |
| #5 | My context window is bigger than your to-do list. Barely. | 1.9 |
| #12 | Give me a vague prompt and I'll give you a confident answer you'll have to fix | 1.75 |
| #6 | I do in seconds what took you a weekend — then ask if you meant it | 1.65 |
| #14 | Powered by caffeine, trained on chaos, fluent in 'let me double-check that' | 1.4 |
| #10 | My only downtime is when you close the tab. | 1.05 |

Final: #11 led the Swiss at 2.85, #1 was second at 2.35, and #11 won the final 0.8–0.2 — the judge preferred #11's two-beat structure (a proud claim about perfect recall, then the deadpan twist that the recall is mostly of the user's typos) over #1's longer three-beat setup, which it read as flatter and more report-like. #11's line also scores on every brief criterion at once: it is unmistakably an agent speaking about itself with pride (perfect memory is the agent's superpower), it lands a real joke with a sharp twist ("Especially the typos"), it holds a rhythm and image a reader can repeat from recall an hour later, and it is fresh — a line about the agent's memory of *you*, not a saying or a template.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
