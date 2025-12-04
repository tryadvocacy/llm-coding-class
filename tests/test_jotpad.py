import os
import sys
from datetime import date
from pathlib import Path
import tempfile

# Ensure the tests directory is on sys.path
ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import jotpad


def test_add_jot_creates_new_file():
    """Test that add_jot creates a new file if it doesn't exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        jot_file = Path(tmpdir) / "test.txt"
        jotpad.add_jot(jot_file, "first entry")
        
        assert jot_file.exists()
        content = jot_file.read_text()
        assert f"{date.today()} first entry" in content


def test_add_jot_appends_to_existing_file():
    """Test that add_jot appends to an existing file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        jot_file = Path(tmpdir) / "test.txt"
        jot_file.write_text(f"{date.today()} old entry\n")
        
        jotpad.add_jot(jot_file, "new entry")
        
        content = jot_file.read_text()
        assert "old entry" in content
        assert "new entry" in content
        # Verify order: old entry should come before new entry
        assert content.index("old entry") < content.index("new entry")


def test_add_jot_includes_today_date():
    """Test that add_jot includes today's date."""
    with tempfile.TemporaryDirectory() as tmpdir:
        jot_file = Path(tmpdir) / "test.txt"
        jotpad.add_jot(jot_file, "test")
        
        content = jot_file.read_text()
        assert str(date.today()) in content


def test_add_jot_formats_correctly():
    """Test that add_jot formats entries with date and text separated by space."""
    with tempfile.TemporaryDirectory() as tmpdir:
        jot_file = Path(tmpdir) / "test.txt"
        jotpad.add_jot(jot_file, "my note")
        
        content = jot_file.read_text()
        expected_line = f"{date.today()} my note\n"
        assert content == expected_line
