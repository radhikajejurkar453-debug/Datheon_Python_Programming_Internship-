
import random


def load_words():
    with open("words.txt", "r") as file:
        words = [
            word.strip().upper()
            for word in file
            if word.strip().isalpha() and len(word.strip()) >= 4
        ]

    if not words:
        raise ValueError("No valid words found in words.txt")

    return words


hangman_stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def display_word(word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_hangman():
    words = load_words()
    word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("\n===== WELCOME TO HANGMAN =====")
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect attempts.")

    while len(wrong_guesses) < max_attempts:

        print(hangman_stages[len(wrong_guesses)])

        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Incorrect attempts:", len(wrong_guesses), "/", max_attempts)

        guess = input("\nEnter a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")

            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                print("You won the game!")
                return

        else:
            wrong_guesses.add(guess)
            print("Wrong guess!")

    print(hangman_stages[max_attempts])
    print("\nGame Over! You ran out of attempts.")
    print("The correct word was:", word)


def main():
    while True:
        play_hangman()

        play_again = input(
            "\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again not in ("yes", "y"):
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()
