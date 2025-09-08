# Pythone game Hangman/Stickman
# Author: DusanB98
# Date: 4.9.2025

from hangman_assets import words
from hangman_assets import stickman_art
import random

def show_art(wrong_guess):
    for stick in stickman_art[wrong_guess]:
        print(stick)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)                          # printing enough of _ acording to lenght of current word 
    wrong_guess = 0                                     # counting wrong guesses and showing current stage of stickman art
    used_letters = []
    stickman_running = True                             # while loop True

    while stickman_running:
        print()
        show_art(wrong_guess)                           # show in console stickman
        print()
        print(" ".join(hint))                           # list of _ need space between
        print()
        guess = input("Enter your guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:      # check if is in string is other signs than alphabet or whole word
            print("______________")
            print("Invalid input!")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print(f"Used letters: {', '.join(used_letters)}")       # showing used letters
            continue                                                # if this is not there then counter of wrong guesses will count
        
        if guess in used_letters:
            print("____________________")
            print("Already used letter!")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print(f"Used letters: {', '.join(used_letters)}")       # showing used letters
            continue

        used_letters.append(guess)                                  # adding to the end of list used letters
        print(f"Used letters: {', '.join(used_letters)}")           # printing used letters

        if guess in answer:                             # If guess is in answer
            for index in range(len(answer)):            # Check all index in range of word lenght
                if answer[index] == guess:              # If guessed letter is in index position
                    hint[index] = guess                 # Change instead of _ put there guessed letter
        else:
            wrong_guess += 1

        if "_" not in hint:                             #If there are not _ in hint, the we win!
            print()
            print("You WIN!")
            print(" ".join(hint))
            print(f"Number of wrong guesses: {wrong_guess}")
            print()
            stickman_running = False
        elif wrong_guess > 10:                          #If wrong guesses are more than 10, game over
            print()
            print("You LOST!")
            print(f"Right asnwer: {answer}")
            print()
            stickman_running = False                    # Stop while loop
    
if __name__ == '__main__':
    main()