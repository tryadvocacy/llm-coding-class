import os
import sys
from io import StringIO

# Ensure the workspace root is on sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import madlib


def test_madlib_output(capsys):
    """Test that madlib generates the correct story."""
    madlib.madlib("cat", "fluffy", "jump", "quickly", "dog", "scary", "run", "slowly")
    captured = capsys.readouterr()
    
    assert "Once upon a time, there was a fluffy cat." in captured.out
    assert "It loved to jump quickly through the forest." in captured.out
    assert "One day, it encountered a scary dog." in captured.out
    assert "The dog challenged the cat to run slowly." in captured.out
    assert "And so, the fluffy cat and the scary dog became best friends." in captured.out
    assert "The end." in captured.out


def test_madlib_contains_all_words(capsys):
    """Test that all input words appear in the output."""
    noun1, adj1, verb1, adv1 = "elephant", "purple", "dance", "gracefully"
    noun2, adj2, verb2, adv2 = "zebra", "striped", "sing", "loudly"
    
    madlib.madlib(noun1, adj1, verb1, adv1, noun2, adj2, verb2, adv2)
    captured = capsys.readouterr()
    output = captured.out
    
    assert noun1 in output
    assert adj1 in output
    assert verb1 in output
    assert adv1 in output
    assert noun2 in output
    assert adj2 in output
    assert verb2 in output
    assert adv2 in output


def test_main_with_args(capsys, monkeypatch):
    """Test main function with command-line arguments."""
    monkeypatch.setattr(sys, "argv", [
        "madlib.py",
        "dog", "lazy", "bark", "softly",
        "cat", "clever", "meow", "loudly"
    ])
    madlib.main()
    captured = capsys.readouterr()
    
    assert "lazy dog" in captured.out
    assert "clever cat" in captured.out


def test_main_with_prompts(capsys, monkeypatch):
    """Test main function with interactive input prompts."""
    inputs = iter([
        "bird", "small", "fly", "swiftly",
        "tree", "tall", "sway", "gently"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    madlib.main()
    captured = capsys.readouterr()
    
    assert "small bird" in captured.out
    assert "tall tree" in captured.out
