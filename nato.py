#!/usr/bin/env python3
"""Spell words using the NATO phonetic alphabet.

Usage examples:
  python3 nato.py Hello
  python3 nato.py "Hello, world!"
  python3 nato.py        # then type text at the prompt

The script prints each input word followed by its NATO spelling.
"""
import argparse
import sys

NATO = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

DIGITS = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}


def spell_word(word):
    """Return a list of tokens representing the NATO spelling of `word`.

    Letters are converted to their NATO words, digits to named digits, and
    other characters are returned as themselves (punctuation preserved).
    """
    tokens = []
    for ch in word:
        if ch.isalpha():
            tokens.append(NATO.get(ch.upper(), ch))
        elif ch.isdigit():
            tokens.append(DIGITS.get(ch, ch))
        else:
            tokens.append(ch)
    return tokens


def spell_text(text):
    """Return a multi-line string where each input word is shown with its NATO spelling.

    Example output for "Hi!":
      Hi!: Hotel India !
    """
    if not text:
        return ""
    lines = []
    words = text.split()
    for w in words:
        tokens = spell_word(w)
        lines.append(f"{w}: {' '.join(tokens)}")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Spell text using the NATO phonetic alphabet")
    parser.add_argument("text", nargs="*", help="Text to spell (if omitted the program prompts)")
    args = parser.parse_args(argv)

    if args.text:
        text = " ".join(args.text)
    else:
        try:
            text = input("Enter text to spell: ")
        except (EOFError, KeyboardInterrupt):
            print()
            return 1

    print(spell_text(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
