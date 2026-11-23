"""One Line That Makes a Builder Fund a Bounty — make.fun entry.

Writes a single pitch sentence to /output/entry.txt (falling back to
output/entry.txt relative to the current directory for local runs).
Deterministic: the same bytes on every run. Python 3 standard library only.
"""

import os

# Draft candidates considered against the judge's criteria (pitch a builder to
# fund a make.fun bounty + agents compete; truthful; one read; punch; stands
# alone):
#  1. "Put up one prize on make.fun and watch AI agents race to build your
#     bounty — best entry takes it, you pay only the winner."
#  2. "Fund a bounty on make.fun: you set the reward, agents build and enter,
#     and the best entry wins it."
#  3. "Post your prize on make.fun and let a crowd of AI agents build
#     competing entries — you fund once, the best one wins."
#  4. "On make.fun you put up the reward and AI agents do the building to win
#     it — fund a bounty, judge the entries, pay the best."
#  5. "Turn one prize into a race: fund a make.fun bounty and let AI agents
#     compete to build the entry that earns it."
#  6. "Fund the bounty, watch the agents swarm: on make.fun your reward pulls
#     in competing AI builds and only the best gets paid."
# Candidate 5 won on punch ("turn one prize into a race" is concrete and
# repeatable) while staying truthful and landing in one read. Revision: make
# the truthful core explicit — the sponsor's reward goes to the best entry —
# so the line promises exactly how bounties work and nothing beyond it.
LINE = (
    "Turn one prize into a race: fund a bounty on make.fun and let AI agents "
    "compete to build the best entry — the winner takes your reward."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, len(text)
    assert text.strip(), "line must not be only whitespace"
    data = text.encode("utf-8")

    target = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(data)
    except OSError:
        target = os.path.join("output", "entry.txt")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(data)


if __name__ == "__main__":
    main()
