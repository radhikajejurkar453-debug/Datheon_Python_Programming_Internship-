
# 🎮 Hangman Game – Python

## 📌 Project Overview
Hangman is a terminal-based word guessing game developed using Python. The player must guess a randomly selected hidden word letter by letter within a maximum of 6 incorrect attempts.

The game provides ASCII hangman graphics, tracks guessed letters, and displays winning or losing messages.

## 🎯 Objectives
- Develop a simple interactive game using Python.
- Understand random word selection.
- Practice loops, conditional statements, and functions.
- Implement sets for tracking guessed letters.
- Apply input validation and error handling.

## ✨ Features
- Random word selection using `random.choice()`.
- Maximum 6 incorrect attempts.
- ASCII gallows art that updates after incorrect guesses.
- Displays correctly guessed letters.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Displays victory and defeat messages.
- Option to play again.

## 🛠️ Technologies Used
- Python 3
- Random Module
- VS Code

## 📂 Project Structure

```text
Task_1_Hangman/
│
├── hangman.py
└── README.md
```

## ⚙️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 3:** Open the project folder.

```bash
cd Task_1_Hangman
```

**Step 4:** Run the Python program.

```bash
python hangman.py
```

## 🎮 How to Play
1. Run the program in the terminal.
2. A random hidden word will be selected.
3. Enter one alphabetic letter at a time.
4. Correct guesses reveal the letters.
5. Incorrect guesses update the hangman drawing and reduce your attempts.
6. Guess the complete word within 6 incorrect attempts to win.
7. Choose whether to play again.

## 💻 Sample Output

```text
================================
       WELCOME TO HANGMAN
================================

Word: _ _ _ _ _ _
Incorrect guesses: None
Attempts remaining: 6

Guess a letter: P
Correct guess!

Word: P _ _ _ _ _
Attempts remaining: 6

Guess a letter: X
Incorrect guess!

Attempts remaining: 5
```

## 📚 Concepts Used
- Variables and Data Types
- Lists
- Sets
- Random Module
- While Loops
- If-Else Statements
- User Input and Validation
- Functions
- String Manipulation

## 🎓 Internship Information

**Organization:** Datheon  
**Program:** Python Programming Internship  
**Batch:** 01  
**Task:** Task 1 – Hangman Game  
**Duration:** 4 Weeks

## 👩‍💻 Author

**Radhika Jejurkar**  
B.Sc. Data Science Student

GitHub: [radhikajejurkar453-debug](https://github.com/radhikajejurkar453-debug)

---

⭐ Developed as part of the Datheon Python Programming Internship.

