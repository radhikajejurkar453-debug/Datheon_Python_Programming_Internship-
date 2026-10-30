# Hangman Game – Python

A simple, interactive, terminal-based Hangman game developed using Python as part of the **Datheon Python Programming Internship – Batch 01**.

## 📌 Project Overview

Hangman is a word-guessing game in which the player tries to guess a hidden word one letter at a time. The player has a maximum of **6 incorrect attempts** to guess the complete word before the hangman drawing is completed.

The game randomly selects a word from an external word list (`words.txt`) containing English words.

## 🎯 Objectives

- Develop a terminal-based word-guessing game using Python.
- Implement random word selection.
- Practice loops, conditional statements, functions, and sets.
- Handle user input and prevent repeated guesses.
- Apply basic game logic and problem-solving skills.

## ✨ Features

- Random word selection from `words.txt`.
- Letter-by-letter word guessing.
- Maximum of 6 incorrect attempts.
- ASCII hangman drawing updated after each incorrect guess.
- Displays correctly guessed letters and hidden letters.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Option to play multiple rounds.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Modules:** `random`
- **Concepts:** Functions, Loops, Conditional Statements, Lists, Sets, File Handling, and Exception Handling.

## 📂 Project Structure

```text
Datheon_Python_Programming_Internship/
│
├── hangman.py
├── words.txt
└── README.md
```

**File Description:**
- `hangman.py` – Contains the main game logic and functions.
- `words.txt` – Contains the English word list used for random word selection.
- `README.md` – Project documentation and instructions.

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your system.

### Step 2: Download or Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 3: Open the Project Folder

```bash
cd Datheon_Python_Programming_Internship
```

### Step 4: Run the Game

```bash
python hangman.py
```

**Note:** Keep `hangman.py` and `words.txt` in the same project folder.

## 🎮 How to Play

1. Run the Python program.
2. The game randomly selects a hidden English word.
3. Enter one alphabetic letter at a time.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses update the hangman drawing.
6. You can make up to 6 incorrect guesses.
7. Guess the complete word to win.
8. If you use all 6 attempts, the game ends and reveals the correct word.
9. Choose whether to play another round.

## 💻 Sample Output

```text
===== WELCOME TO HANGMAN =====
Guess the hidden word one letter at a time.
You have 6 incorrect attempts.

Word: _ _ _ _ _ _
Guessed letters:
Incorrect attempts: 0 / 6

Enter a letter: P
Correct guess!

Word: P _ _ _ _ _
Guessed letters: P
Incorrect attempts: 0 / 6

Enter a letter: Z
Wrong guess!

Incorrect attempts: 1 / 6
```

*Note: The actual word and output will vary because the game selects words randomly.*

## 📚 Python Concepts Used

| Concept | Application |
|---|---|
| Functions | Organizing the game into reusable blocks |
| Random Module | Selecting a random word |
| Lists | Storing hangman drawing stages |
| Sets | Tracking guessed letters |
| Loops | Repeating the game until it ends |
| Conditional Statements | Checking correct and incorrect guesses |
| File Handling | Reading words from `words.txt` |
| Input Validation | Accepting only one alphabetic letter |

## 🚀 Future Improvements

- Add Easy, Medium, and Hard difficulty levels.
- Add a scoring system.
- Display hints for difficult words.
- Add a graphical user interface (GUI).
- Track the player's winning streak.

## 👩‍💻 Internship Details

- **Organization:** Datheon
- **Program:** Python Programming Internship
- **Batch:** 01
- **Task:** Task 1 – Hangman Game
- **Duration:** 4 Weeks

## 👤 Author

**Radhika Jejurkar**  
B.Sc. Data Science Student

---

*This project was developed as part of the Datheon Python Programming Internship – Batch 01.*
