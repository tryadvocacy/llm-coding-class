import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Ensure the repository root is on sys.path so tests can import the top-level modules.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import nato


class TestNato(unittest.TestCase):
    """Unit tests for nato.py using unittest module."""

    def test_spell_word_letters(self):
        """Test spelling individual letters."""
        result = nato.spell_word("Hi")
        self.assertEqual(result, ["Hotel", "India"])

    def test_spell_word_with_punctuation(self):
        """Test that punctuation is preserved."""
        result = nato.spell_word("Hi!")
        self.assertEqual(result, ["Hotel", "India", "!"])

    def test_spell_word_digits(self):
        """Test spelling digits."""
        result = nato.spell_word("A1B2")
        self.assertEqual(result, ["Alfa", "One", "Bravo", "Two"])

    def test_spell_word_mixed(self):
        """Test mixed letters, digits, and punctuation."""
        result = nato.spell_word("A1!")
        self.assertEqual(result, ["Alfa", "One", "!"])

    def test_spell_word_lowercase(self):
        """Test that lowercase letters are converted correctly."""
        result = nato.spell_word("abc")
        self.assertEqual(result, ["Alfa", "Bravo", "Charlie"])

    def test_spell_word_uppercase(self):
        """Test that uppercase letters are converted correctly."""
        result = nato.spell_word("ABC")
        self.assertEqual(result, ["Alfa", "Bravo", "Charlie"])

    def test_spell_text_single_word(self):
        """Test spelling a single word."""
        result = nato.spell_text("Hi!")
        self.assertEqual(result, "Hi!: Hotel India !")

    def test_spell_text_multiple_words(self):
        """Test spelling multiple words."""
        result = nato.spell_text("Hello world")
        lines = result.split("\n")
        self.assertEqual(len(lines), 2)
        self.assertIn("Hello:", lines[0])
        self.assertIn("world:", lines[1])

    def test_spell_text_empty(self):
        """Test spelling empty text."""
        result = nato.spell_text("")
        self.assertEqual(result, "")

    def test_main_with_args(self):
        """Test main function with command-line arguments."""
        test_args = ["nato.py", "Hello", "world"]
        with patch.object(sys, "argv", test_args):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                rc = nato.main()
                output = fake_out.getvalue()
                
                self.assertEqual(rc, 0)
                self.assertIn("Hotel Echo Lima Lima Oscar", output)
                self.assertIn("Whiskey Oscar Romeo Lima Delta", output)

    def test_main_with_single_arg(self):
        """Test main function with a single argument."""
        test_args = ["nato.py", "Hi"]
        with patch.object(sys, "argv", test_args):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                rc = nato.main()
                output = fake_out.getvalue()
                
                self.assertEqual(rc, 0)
                self.assertIn("Hotel India", output)

    def test_main_with_prompts(self):
        """Test main function with interactive input prompts."""
        test_args = ["nato.py"]
        with patch.object(sys, "argv", test_args):
            with patch("builtins.input", return_value="Hi"):
                with patch("sys.stdout", new=StringIO()) as fake_out:
                    rc = nato.main()
                    output = fake_out.getvalue()
                    
                    self.assertEqual(rc, 0)
                    self.assertIn("Hotel India", output)

    def test_nato_mapping_complete(self):
        """Test that NATO mapping contains all 26 letters."""
        self.assertEqual(len(nato.NATO), 26)
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertIn(letter, nato.NATO)

    def test_digits_mapping_complete(self):
        """Test that DIGITS mapping contains all 10 digits."""
        self.assertEqual(len(nato.DIGITS), 10)
        for digit in "0123456789":
            self.assertIn(digit, nato.DIGITS)


if __name__ == "__main__":
    unittest.main()
