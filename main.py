#!/usr/bin/env python3
"""make.fun entry: The Word You'd Delete From the Dictionary.

Writes the single word to erase from the dictionary forever to
/output/entry.txt. No network, no input, no side effects.
"""

WORD = "moist"


def main() -> None:
    # Gate, mirrored from the competition rules: UTF-8 text, 1-77 chars,
    # not only whitespace, exactly one word.
    assert 1 <= len(WORD) <= 77, "word outside the 1-77 character gate"
    assert WORD.strip() == WORD and len(WORD.split()) == 1, "entry must be one word"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and verify what landed on disk is exactly the word.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == WORD, "read-back mismatch"


if __name__ == "__main__":
    main()
