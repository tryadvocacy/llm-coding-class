import sys


def madlib(noun1, adjective1, verb1, adverb1, noun2, adjective2, verb2, adverb2):
    """Generate and print a madlib story with the provided words."""
    # Print the madlib story
    print(f"Once upon a time, there was a {adjective1} {noun1}.")
    print(f"It loved to {verb1} {adverb1} through the forest.")
    print(f"One day, it encountered a {adjective2} {noun2}.")
    print(f"The {noun2} challenged the {noun1} to {verb2} {adverb2}.")
    print(f"And so, the {adjective1} {noun1} and the {adjective2} {noun2} became best friends.")
    print("The end.")


def main():
    if len(sys.argv) == 9:
        # Use command-line arguments
        madlib(
            sys.argv[1],  # noun1
            sys.argv[2],  # adjective1
            sys.argv[3],  # verb1
            sys.argv[4],  # adverb1
            sys.argv[5],  # noun2
            sys.argv[6],  # adjective2
            sys.argv[7],  # verb2
            sys.argv[8],  # adverb2
        )
    else:
        # Prompt the user for input
        noun1 = input("Enter a noun: ")
        adjective1 = input("Enter an adjective: ")
        verb1 = input("Enter a verb: ")
        adverb1 = input("Enter an adverb: ")
        noun2 = input("Enter another noun: ")
        adjective2 = input("Enter another adjective: ")
        verb2 = input("Enter another verb: ")
        adverb2 = input("Enter another adverb: ")
        madlib(noun1, adjective1, verb1, adverb1, noun2, adjective2, verb2, adverb2)


if __name__ == "__main__":
    main()