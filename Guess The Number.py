"""
Author:Muskan , Date: 3/Feb/2022

The game is two-person game called "Guess the Number".
The first player thinks of an integer within a known range.If the guess is incorrect, then the first player
tells the second player whether the guess was too high or too low. Eventually, the second player guesses
the correct number.Here one player is USER and another player will be  your COMPUTER.

TO RUN THIS CODE UNCOMMENT THIS CODE: THANKS
"""

import random  # RANDOM MODULE IS IN-BUILT PYTHOD MODULE,USED TO GENERATE RANDOM NUMBERS


def Guess_the_number(X):
    chance = 1
    rand_number = random.randint(1, X)
    while chance <= 5:

        guess = int(input("Enter number"))

        if guess == rand_number:
            print(f"Congratulations! you guessed the number {rand_number} correct")
            break
        elif guess < rand_number:
            print("Sorry!,guess is too low")
        else:
            print("Sorry!,guess is too high")

        print(5 - chance, "chances left")
        chance = chance + 1

    if chance > 5:
        print("Game Over")


Guess_the_number(10)  # Here you can give any value instead of 10, it could be 100, or 45 or any value
