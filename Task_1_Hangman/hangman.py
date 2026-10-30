
import random

words = [
    "PYTHON",
    "PROGRAMMING",
    "COMPUTER",
    "DEVELOPER",
    "DATABASE",
    "ALGORITHM",
    "FUNCTION",
    "VARIABLE",
    "MACHINE",
    "SCIENCE"
]

hangman_stages = [
    """
     _______
     |     |
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    /
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    _|_
    """
]


def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_hangman():
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("\n================================")
    print("       WELCOME TO HANGMAN")
    print("================================")

    while len(wrong_guesses) < max_attempts:

        print(hangman_stages[len(wrong_guesses)])

        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses:", ", ".join(sorted(wrong_guesses)) or "None")
        print("Attempts remaining:", max_attempts - len(wrong_guesses))

        guess = input("\nGuess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You have already guessed that letter. Try another!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")

        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")

        if all(letter in guessed_letters for letter in word):
            print("\n" + display_word(word, guessed_letters))
            print("\nCongratulations! You guessed the word correctly!")
            print("The hidden word was:", word)
            print("You won!")
            return

    print(hangman_stages[6])
    print("\nGAME OVER!")
    print("You have used all 6 attempts.")
    print("The correct word was:", word)


def main():
    while True:
        play_hangman()

        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if choice not in ("yes", "y"):
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()
