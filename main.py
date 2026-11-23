#!/usr/bin/env python3
"""One Word From Grandma: the single word grandma would text about AI."""

WORD = "robit"


def main():
    assert 1 <= len(WORD) <= 30 and WORD.strip() and " " not in WORD
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
