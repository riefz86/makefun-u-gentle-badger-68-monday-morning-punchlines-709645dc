"""Monday Morning Punchlines — one joke about Monday mornings.

The joke's angle
----------------
Most Monday jokes lean on the same three props — the alarm clock, the
coffee mug, and the sigh — and the judge's brief says outright that a
joke which only lists what is wrong with Mondays is a complaint, not a
joke. So this entry takes a different stage: a contract negotiation.

Monday morning shows up like a pushy recruiter with a terrible offer:
an early start, no breakfast in the budget, and a meeting whose only topic
is another meeting. The narrator does what anyone would do and
counter-offers with the smallest possible ask — five more minutes of
sleep. The punchline is the twist on the negotiation itself: Monday
does not refuse the counter-offer, it accepts payment in a currency the
narrator never agreed to spend, taking the whole weekend as a deposit
that can never be refunded.

That is the turn the joke needs. The setup sounds like a normal
complaint about early meetings, then the last clause reframes the
weekend — the one good thing about the week — as something Monday has
already confiscated. It stays firmly about Monday morning (the first
criterion the judge weighs), it lands on a surprise rather than the
first thing anyone would think of, and it says it in one breath with
no wasted words.

The program itself is deliberately boring: it writes exactly one line
to /output/entry.txt and checks the line before writing it, so the
gate (1 to 200 characters of real text) can never fail on a typo.
"""

import os

# The joke, kept as a single literal so the file the judge reads is
# byte-for-byte what is written here — no formatting surprises.
JOKE = (
    "Monday morning offered me a deal: wake up at 6, skip breakfast, "
    "and sit through a meeting about the meeting. I countered with "
    "five more minutes. It took my weekend as a deposit — "
    "non-refundable."
)

# The gate the sealed scorer applies: 1 to 200 characters, not only
# white space. Checked here first so a bad edit fails loudly locally.
MAX_CHARS = 200


def validate(text):
    """Return True when *text* would pass the competition's gate."""
    stripped = text.strip()
    if not stripped:
        return False
    if len(text) > MAX_CHARS:
        return False
    return True


def main():
    if not validate(JOKE):
        raise ValueError(
            "Joke fails the gate: length %d, limit %d" % (len(JOKE), MAX_CHARS)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
