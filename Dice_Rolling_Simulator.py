"""
Author:Muskan , Date: 15/Feb/2022

A dice simulator is a simple computer model that can roll a dice for us.
It functions same as a normal dice in which user rolls a dice and a random
number gets shown on the screen

Uncomment code to use
"""

from pygame import mixer  # mixer module imported from pygame module i to use the audio files in code
import random  # Python random module to give us random number


def Roll_Dice_Audio():
    mixer.init()
    mixer.music.load("roll.mp3")
    mixer.music.set_volume(0.9)
    mixer.music.play()
    Response = input("Dice rolled...Press Enter")
    print(Response)


def Roll_Dice():
    Roll_Dice_Audio()  # Roll dice function called which is defined above

    Random = random.randint(1,6)  # The randint() method returns an integer number selected element from the specified range.

    print("Your Dice number is: ", Random)


def start():
    tell = input("Press 1 to play, 2 for exit\n")

    if tell == "1":
        Roll_Dice()  # Roll_Dice function called

    elif tell == "2":
        print("You have chosen "'2'" which means No,Game Ends here!")


while True:
    start()  # start function called
    print("Do you want to roll your dice again?")

    play_again_YN = input(
        "Y for play again, N for Game Over\n").upper()  # upper() will convert all the input in UPPERCASe

    if play_again_YN == "Y":
        start()
    elif play_again_YN == "N":
        print("GAME OVER!")
        break
