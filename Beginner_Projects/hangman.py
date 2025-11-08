# Hangman Game
#Goal: The computer chooses a random 4 letter word from a category, Then the user must guess the letters of the word, only has 6 tries!
#Steps: 1. Great the User
#       2. The computer chooses the word
#       3. The player inputs letter by letter until it figueres put the word
#       4. After 6 Tries it looses 
#       5. Display the hangman different stages
#       6. Each wrong guess changes the hangman stage

import random

# 1. Great the User
print("="* 90)
print("Welcome to The Hangman Game!")
print("Here you are going have 6 tries to discover a 4 letter word in the animal world")
print("You can only guess one letter at a time!")
print("Good Luck!")
print("="* 90 )

# 2. The computer chooses the word

word_list = ["bear", "dove", "lion", "bird", "duck", "lynx", "bull", "fish", "mink", "calf", "flea", "mole", "toad"]
secret_word = random.choice(word_list)

guesses =[]
max_attempts = 6
hangman_stages = [
   """
       --------
       |      |
       |
       |
       |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """
]
word_completion = ["_" for _ in secret_word ]

# Game Logic

attempts_left = max_attempts
while attempts_left > 0 and "_" in word_completion:
    print("="* 90 )
    print(hangman_stages[max_attempts - attempts_left])
    print("Word: " + " ".join(word_completion))
    print("Guessed letters: " + ", ".join(guesses))
    guess = input("Guess a letter: ").lower()

    #Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. You Guess a letter at a time!!")
        continue
    elif guess in guesses:
        print("You alredy tried that one! Try Again!")
        continue

    guesses.append(guess)

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                word_completion[i] = guess
        print("Nice Guess! Keep Going!")
    else:
        attempts_left -=1
        print("Wrong Guess! Try Again!")
        print(f"You got {attempts_left} tries left!")

if "_" not in word_completion:
    print("=" * 50)
    print(f"Well done! You guesse the {secret_word}!")
else:
    print(hangman_stages[-1])
    print(f"It was a nice try! The word was {secret_word}")
    print("Better luck next time!")

  