<<<<<<< HEAD
"""
Author:Muskan , Date: 7/Feb/2022

--Rules in Rock Paper Scissors--
The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward;
and scissors is a fist with the index and middle fingers fully extended toward the opposing player.
Rock wins against scissors; paper wins against rock; and scissors wins against paper.

"""

import random


def play_game():
    rps_list = ['r', 'p', 's']

    rand = random.choice(rps_list)

    user = input("Enter -> r for Rock, s for scissors, p for Paper\n").lower()

    if (user == 'r' and rand == 's') or (user == 'p' and rand == 's') or user == 's' and rand == 'p':

        print("YOU WIN COMPUTER LOSE")
    elif user == rand:
        print("IT'S A TIE")


play_game()
=======
"""
Author:Muskan , Date: 7/Feb/2022

--Rules in Rock Paper Scissors--
The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward;
and scissors is a fist with the index and middle fingers fully extended toward the opposing player.
Rock wins against scissors; paper wins against rock; and scissors wins against paper.

"""

import random


def play_game():
    rps_list = ['r', 'p', 's']

    rand = random.choice(rps_list)

    user = input("Enter -> r for Rock, s for scissors, p for Paper\n").lower()

    if (user == 'r' and rand == 's') or (user == 'p' and rand == 's') or user == 's' and rand == 'p':

        print("YOU WIN COMPUTER LOSE")
    elif user == rand:
        print("IT'S A TIE")


play_game()
>>>>>>> facdd91d689b3f3f2b387c06ecaa174fcec61797
