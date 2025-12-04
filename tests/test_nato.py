import os
import sys

# Ensure the repository root is on sys.path so tests can import the top-level modules.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import nato


def test_spell_word_letters():
    assert nato.spell_word("Hi!") == ["Hotel", "India", "!"]


def test_spell_word_digits():
    assert nato.spell_word("A1B2") == ["Alfa", "One", "Bravo", "Two"]


def test_spell_text():
    assert nato.spell_text("Hi!") == "Hi!: Hotel India !"


def test_main_prints(capsys):
    rc = nato.main(["Hi!"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Hotel India" in captured.out


def test_main_with_phrase(capsys):
    rc = nato.main(["Hello,", "world!"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Whiskey Oscar Romeo Lima Delta" in captured.out
