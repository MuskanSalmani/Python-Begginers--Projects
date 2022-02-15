<<<<<<< HEAD
"""
Author:Muskan , Date: 12/Feb/2022
Uncomment code to use this code
"""

import random
from Word_HangMan import word_list

def get_word():

 word = random.choice(word_list).upper()
 return word

def play_word(word):

 word_completion = '_'*len(word)
 guessed = False
 guessed_letters = []
 guessed_words = []
 tries = 6
 print("Hangman Started")
 print(display_hangman(tries))
 print(word_completion)
 print("......")
 while not guessed and tries >0:
     guess = input("Please guess a letter or word: ").upper()
     if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
             print("You already guessed the letter", guess)
         elif guess not in word:
             print(guess, "is not in the word.")
             tries -= 1
             guessed_letters.append(guess)
         else:
             print("Good job,", guess, "is in the word!")
             guessed_letters.append(guess)
             word_as_list = list(word_completion)
             indices = [i for i, letter in enumerate(word) if letter == guess]
             for index in indices:
                 word_as_list[index] = guess
             word_completion = "".join(word_as_list)
             if "_" not in word_completion:
                 guessed = True
     elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
             print("You already guessed the word", guess)
         elif guess != word:
             print(guess, "is not the word.")
             tries -= 1
             guessed_words.append(guess)
         else:
             guessed = True
             word_completion = word
     else:
         print("Not a valid guess.")
     print(display_hangman(tries))
     print(word_completion)
     print("\n")
 if guessed:
     print("Congrats, you guessed the word! You win!")
 else:
     print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = ["""
            -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        / \\
            -      
             """,
             """
             -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        /
            _   
             """,
            """
             -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        
            _        
            """,
             """
             -----------
            |         |
            |         o
            |       \\|
            |         |
            |        
            _        
             
             """,
             """
            -----------
            |         |
            |         o
            |         |
            |         |
            |        
            _        
           """,
             """
             -----------
            |         |
            |         o
            |         
            |         
            |        
            _        
            """,
             """
             ---------
            |         |
            |         
            |         
            |         
            |        
            _        
             
             """
           ]
    return stages[tries]



def main():
    word = get_word()
    play_word(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play_word(word)


if __name__ == "__main__":
    main()
=======
"""
Author:Muskan , Date: 12/Feb/2022
Uncomment code to use this code
"""

import random
from Word_HangMan import word_list

def get_word():

 word = random.choice(word_list).upper()
 return word

def play_word(word):

 word_completion = '_'*len(word)
 guessed = False
 guessed_letters = []
 guessed_words = []
 tries = 6
 print("Hangman Started")
 print(display_hangman(tries))
 print(word_completion)
 print("......")
 while not guessed and tries >0:
     guess = input("Please guess a letter or word: ").upper()
     if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
             print("You already guessed the letter", guess)
         elif guess not in word:
             print(guess, "is not in the word.")
             tries -= 1
             guessed_letters.append(guess)
         else:
             print("Good job,", guess, "is in the word!")
             guessed_letters.append(guess)
             word_as_list = list(word_completion)
             indices = [i for i, letter in enumerate(word) if letter == guess]
             for index in indices:
                 word_as_list[index] = guess
             word_completion = "".join(word_as_list)
             if "_" not in word_completion:
                 guessed = True
     elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
             print("You already guessed the word", guess)
         elif guess != word:
             print(guess, "is not the word.")
             tries -= 1
             guessed_words.append(guess)
         else:
             guessed = True
             word_completion = word
     else:
         print("Not a valid guess.")
     print(display_hangman(tries))
     print(word_completion)
     print("\n")
 if guessed:
     print("Congrats, you guessed the word! You win!")
 else:
     print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = ["""
            -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        / \\
            -      
             """,
             """
             -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        /
            _   
             """,
            """
             -----------
            |         |
            |         o
            |       \\|/
            |         |
            |        
            _        
            """,
             """
             -----------
            |         |
            |         o
            |       \\|
            |         |
            |        
            _        
             
             """,
             """
            -----------
            |         |
            |         o
            |         |
            |         |
            |        
            _        
           """,
             """
             -----------
            |         |
            |         o
            |         
            |         
            |        
            _        
            """,
             """
             ---------
            |         |
            |         
            |         
            |         
            |        
            _        
             
             """
           ]
    return stages[tries]



def main():
    word = get_word()
    play_word(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play_word(word)


if __name__ == "__main__":
    main()
>>>>>>> 061c9b85e4d0457cdbb61a8b7da5c6fb6d7ae88d
