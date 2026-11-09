# Name Isam Zia Roll no: TRN-2026-00346 

import random

while True:
    secret = random.randint(1, 50)
    guesses = 0

    print("\nGuess a number between 1 and 50")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guesses += 1

        if guess > secret:
            print("Too high")
        elif guess < secret:
            print("Too low")
        else:
            print(f"Got it in {guesses} guesses!")
            break

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break