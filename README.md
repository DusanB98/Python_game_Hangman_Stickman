# 🎮 Hangman Game

> 🖥️ This is a **console-based game**, designed to run in a terminal or command-line interface. No graphical interface is required.

Hangman is a classic word-guessing game where the player tries to uncover
a hidden word by guessing one letter at a time.
Each incorrect guess brings the stick figure closer to being "hanged".

## 🧠 Game Features

- **Letter-by-letter guessing**: Players input one letter per turn to reveal parts of the hidden word.
- **Visual hangman progress**: With each wrong guess, a new part of the hangman is drawn.
- **Used letters tracking**: All guessed letters are stored and displayed. Repeating a letter doesn't count as a new attempt.
- **Input validation**:
  - Only **single alphabetic characters** are accepted.
  - Inputs such as **numbers**, **symbols**, or **entire words** are rejected with a warning.
  - Invalid inputs do **not** reduce the number of remaining attempts.

## 🧩 Game Structure & Word Source

The vocabulary for the Hangman game is randomly selected from a curated
list of **200 English words**, primarily animal names.
This list is stored in a **separate Python module**, 
which also contains the ASCII art for the stickman drawing.

This modular design keeps the main game logic clean and focused, 
while allowing easy updates to the word list or visual elements.

### 📦 Modular Setup

- `hangman_assets.py`:  
  Contains:
  - The full word list (`words`)
  - Stickman drawing stages (`stickman_art`)

- `main.py`:  
  Imports from `hangman_assets.py` and handles:
  - Game loop and logic
  - Input validation
  - Displaying progress and results
