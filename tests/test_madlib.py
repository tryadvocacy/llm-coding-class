import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Ensure the workspace root is on sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import madlib


class TestMadlib(unittest.TestCase):
    """Unit tests for madlib.py using unittest module."""

    def test_madlib_output(self):
        """Test that madlib generates the correct story."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            madlib.madlib("cat", "fluffy", "jump", "quickly", "dog", "scary", "run", "slowly")
            output = fake_out.getvalue()
            
            self.assertIn("Once upon a time, there was a fluffy cat.", output)
            self.assertIn("It loved to jump quickly through the forest.", output)
            self.assertIn("One day, it encountered a scary dog.", output)
            self.assertIn("The dog challenged the cat to run slowly.", output)
            self.assertIn("And so, the fluffy cat and the scary dog became best friends.", output)
            self.assertIn("The end.", output)

    def test_madlib_contains_all_words(self):
        """Test that all input words appear in the output."""
        noun1, adj1, verb1, adv1 = "elephant", "purple", "dance", "gracefully"
        noun2, adj2, verb2, adv2 = "zebra", "striped", "sing", "loudly"
        
        with patch("sys.stdout", new=StringIO()) as fake_out:
            madlib.madlib(noun1, adj1, verb1, adv1, noun2, adj2, verb2, adv2)
            output = fake_out.getvalue()
            
            self.assertIn(noun1, output)
            self.assertIn(adj1, output)
            self.assertIn(verb1, output)
            self.assertIn(adv1, output)
            self.assertIn(noun2, output)
            self.assertIn(adj2, output)
            self.assertIn(verb2, output)
            self.assertIn(adv2, output)

    def test_main_with_args(self):
        """Test main function with command-line arguments."""
        test_args = [
            "madlib.py",
            "dog", "lazy", "bark", "softly",
            "cat", "clever", "meow", "loudly"
        ]
        with patch.object(sys, "argv", test_args):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                madlib.main()
                output = fake_out.getvalue()
                
                self.assertIn("lazy dog", output)
                self.assertIn("clever cat", output)

    def test_main_with_prompts(self):
        """Test main function with interactive input prompts."""
        inputs = [
            "bird", "small", "fly", "swiftly",
            "tree", "tall", "sway", "gently"
        ]
        with patch("builtins.input", side_effect=inputs):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                madlib.main()
                output = fake_out.getvalue()
                
                self.assertIn("small bird", output)
                self.assertIn("tall tree", output)


if __name__ == "__main__":
    unittest.main()
