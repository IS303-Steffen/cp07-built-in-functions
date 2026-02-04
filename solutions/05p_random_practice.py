from helper_functions import clear_screen
clear_screen()

# =========================
# RANDOM FUNCTIONS PRACTICE
# =========================


# 1. PRACTICE - GENERATING RANDOM NUMBERS
'''
1. Use the random library to generate a number from 1 to 50.
2. Ask the user to guess the number.
3. If their guess is too low or too high, tell them.
4. Keep asking them to enter a number until they get it right.
5. When they guess it, tell them how many tries it took.
'''

import random

secret = random.randint(1, 50)
guess = -1 # make guess something not equal to secret so the while loop can start.
tries = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 50: "))
    tries += 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print(f"You got it in {tries} tries! The number was {secret}.")