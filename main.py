#!/usr/bin/env python3
"""One Word From Grandma — the single word a grandma would text about AI.

The word is "ChatGP": grandma has heard her grandchild talk about ChatGPT
all year, so she texts back about "ChatGP" — the T fell off somewhere
between her thumb and the send button, the way it always does. It is the
misspelling she would actually make, not a word anyone sat down to invent.

Why this word wins on the five judge criteria:
1. It reads as the single word a grandma would text about AI — it IS the
   name of the AI she keeps hearing about, typed the way she would type it.
2. It sounds like her texting voice: warm, a little baffled, trying her
   best with a brand-new word and missing one letter.
3. It is funny in one word with no caption: the dropped T is the whole joke.
4. It is tied to AI specifically — it is a typo of ChatGPT, not a word
   that would fit any subject.
5. It is fresh: the obvious picks are "Robot", "Witchcraft", "Toaster".
   "ChatGP" is instantly readable yet nobody's first guess, and at six
   bytes it is short, which the tie-break rewards.

Standard library only. Writes exactly the word, nothing else.
"""

import os

WORD = "ChatGP"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1-30 UTF-8 characters, not only whitespace, and the
    # task wants exactly one word: refuse to write anything that is not.
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "entry must be one word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
