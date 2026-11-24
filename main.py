"""Real-Life Patch Notes: The Comedy Changelog - entry program.

Writes one line to /output/entry.txt: a software patch note for a bug
in real life, in the terse register of a real release note.

Pass 1 was the doorway bug (crossing a threshold wipes the reason you
crossed it): recognisable, but the joke was pure recognition.

Pass 2 (final): goosebumps - a vestigial reflex is a legacy routine
still running on hardware that dropped the feature it served. That is
a bug in human biology itself, told in the body's own release-note
register: version, terse fix, shipped. Every word works; nothing is
setup the punchline does not need.
"""

import os

ENTRY = (
    "v6.2.0: Fixed goosebumps running the fur-raising routine on "
    "hardware that no longer ships with fur."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
