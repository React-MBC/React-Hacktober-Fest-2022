# Guessing Game
import random

win = random.randint(1, 10000)
guess_attempt_low = 0
guess_attempt_high = 0
guess = int(input("Enter any number: "))
gameover  = False
while (not gameover):
    if guess == win:
        print("You Win")
        print(f"""Attempted Guesses = {guess_attempt_low + guess_attempt_high}
    Attempted low guesses= {guess_attempt_low}
    Attempted high guesses= {guess_attempt_high}""")
        gameover = True
    elif win > guess:
        print("Low")
        guess = int(input("Guess Again: "))
        guess_attempt_low += 1
    else:
        print("High")
        guess = int(input("Guess Again: "))
        guess_attempt_high += 1