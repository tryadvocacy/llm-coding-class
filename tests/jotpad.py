from datetime import date
from pathlib import Path


def add_jot(jot_path, text):
    """Add a jot entry to the file with today's date."""
    jot_contents = jot_path.read_text() if jot_path.exists() else ""
    jot_contents += f"{date.today()} {text}\n"
    jot_path.write_text(jot_contents)


def main():
    text = input("jot: ")
    jot_path = Path("jot.txt")
    add_jot(jot_path, text)
    print("Entry added.")


if __name__ == "__main__":
    main()   
