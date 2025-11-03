#Number Guessing Game
#Goal: The pc selects a number bettween 1 and 100, and the user needs to guess
#steps: 1. Greet the user
#       2. Computer chosses a number between 1 and 100
#       3. User tries to Guess
#       4.The computer says if the number is higher or lower then the chosen number
#       5. Repeat step 4 until number is guessed or it has been 10 tries

import random

# 1. Greet The User
print("="* 90 )
print("Welcome to the Number Guessing Game!")
print("="* 90 )

# 2. Computer Chooses a Number
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("i'm thinking of a number between 1 and 100!")
print("Can you guess it?")
print("="* 90 )

# 3. User tires to Guess
while attempts < max_attempts:
    try:
        guess = int(input("Tell me your guess: "))
        attempts += 1
        
        # Validate the guess to check if its between 1 and 100
        if guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100!")
            continue
        # Checks if its right
        if guess == secret_number:
            print("="* 90 )
            print("Game Over!")
            print("Well done!")
            print(f"You were able to guess the number {secret_number} in {attempts} tries!")
            print("Thanks for playing!")
            print("="* 90 )
            break
        # Checks if its wrong
        elif guess < secret_number:
            print(f"Try Higher! You still got {max_attempts - attempts} tries left! DON'T GIVE UP!")
        else:
            print(f"Try Lower! You still got {max_attempts - attempts} tries left! DON'T GIVE UP!")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")
else:
    print("="* 90 )
    print("GAME OVER!")
    print(f"You have used all your {max_attempts} tries, the number was {secret_number}.")
    print("Better luck next time!")
    print("="* 90 )
    
