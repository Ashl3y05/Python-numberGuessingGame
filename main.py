# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo


def set_life():
    difficulty = input("Set Difficulty 'easy','normal', or 'hard': ").lower()
    if difficulty == "easy":
        return 15
    elif difficulty == "normal":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("\n!!Please choose a valid input!!\n")
        return set_life()


def compare_numbers(guess, chosen):
    if guess > chosen:
        return "\nToo High\n"
    elif guess < chosen:
        return "\nToo Low\n"
    elif guess == chosen:
        return f"\nThe guess is correct! The answer is: {chosen}. You Won!\n"


print(logo)
print(
    "Welcome to 'Guess the Number' game\n-Computer will choose between 1 to 100\n-Input a number and computer will "
    "tell if it is 'Too high' or 'Too Low'\n-Number of guess depends on the difficulty chosen\n")

life = set_life()
chosenNumber = random.randint(1, 100)
gameEnd = False

while not gameEnd:
    print(f"Lives: {life}")
    guessNumber = int(input("Please choose a number: "))

    print(compare_numbers(guessNumber, chosenNumber))

    if guessNumber == chosenNumber:
        gameEnd = True
    elif guessNumber != chosenNumber:
        life -= 1
    if life <= 0:
        print("\n**Out of lives! You Lost!**\n")
        gameEnd = True
