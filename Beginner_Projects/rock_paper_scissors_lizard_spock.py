#Rock Paper Scissors
#Goal: Develop a game of rock paper scissors lizard spock between the computer and the user
#Steps: 1. Greet the user
#       2.The computer chosses between rock parper scissors
#       3.Ask the user which one he chooses
#       4.Check who wins or losses or if its a draw
#       5.Play best out of 5
#       6.Keep Score

import random

# 1. Greet the User
print("=" * 50 )
print("Welcome to Rock, Paper, Scissors, Lizard and Spock Game!!")
print("Today we will be playing a 'best of 5' game. Fisrt to 3! WINS!")
print("-" * 50 )
print("This version is inspired by The Big Bang Theory")
rules = """
"It's very simple.
Scissors cuts paper,
Paper covers rock,
Rock crushes lizard,
Lizard poisons Spock,
Spock smashes scissors,
Scissors decapitates lizard,
Lizard eats paper,
Paper disproves Spock,
Spock vaporizes rock,
And as it always has, rock crushes scissors."
"""
print(rules)
print("=" * 50)

# Starting score
player_score = 0
computer_score = 0
rounds_to_win = 3
round_counter = 0


#list of choices and win conditions
choices =["rock", "paper", "scissors", "lizard", "spock"]

win_conditions = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

# Game loop
while player_score < rounds_to_win and computer_score < rounds_to_win:
    round_counter += 1
    print(f"It's Round {round_counter}!")
    print(f"Score - You: {player_score}, Computer: {computer_score}")
    computer_choice = random.choice(choices)
    player_choice = input(f"Choose {choices}:").lower()
    if player_choice not in choices:
            print(f"Wrong Game! The only options {choices}!")
            print("Good Luck!")
            print("=" * 50)
            continue
    if player_choice == computer_choice:
        print("It's a draw!")
        print("It could be worse!")
        print("=" * 50)
    elif win_conditions[player_choice] == computer_choice:
        print("You win!")
        print("You got This")
        player_score += 1
        print("=" * 50)
    else:
        print("The Computer Won This One!")
        print("Better Luck Next Time!")
        computer_score += 1
        print("=" * 50)

# Display the Score
print(f"Score - You: {player_score}, Computer: {computer_score}")
print("=" * 50)

# Determine the winner
print("=" * 50)
print("GAME OVER!")

if player_score > computer_score:
    print("=" * 50)
    print("Well Done! You Won!")
    print("Thanks for playing!")
    print("=" * 50)
else:
    print("=" * 50)
    print("The Computer Won!")
    print("Better Luck Next Time!")
    print("Thanks for playing!")
    print("=" * 50)