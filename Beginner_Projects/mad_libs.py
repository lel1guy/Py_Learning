#Mad Libs Word Game
#Goal: Ask user random words to develop a funny Story
#Steps: 1. Great User
#       2. Request Words
#       3. Create Story With Words
#       4. Display Story
#       5. Save the Story (Optional)

import random


# 1. Great User
print("Welcome to Mad Libs Word Game!")
print("I'm going to ask you for some randoms words to creat a funny story!")
print("-"* 90 )

# 2. Request Words
print("Please prove the following words!")

noun1 = input("Enter a noun (person, place, thing): ")
noun2 = input("Enter a noun (person, place, thing): ")
adjective1 = input("Enter an adjective (descriptive word): ")
adjective2 = input("Enter an adjective (descriptive word): ")
verb = input("Enter a verb (Action word): ")
adverb = input("Enter a adverb (usually end with -ly): ")
number = input("Enter a number: ")
plural_noun = input("Enter a plural noun: ")
verb_ing = input("Enter a verb ending in -ing: ")
body_part = input("Enter a part of the body: ")
food = input("Enter a type of food: ")
sound = input("Enter a sound: ")

# 3. Creat Story With Words
print("-"* 90 )
story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb} all day.
One day, while {verb_ing}, the {noun1} met a {adjective2} {noun2} in the forest.
"I have a secret!" said the {noun2}, holding a piece of {food}.
"Really?" asked {noun1}. "Tell me {number} secrets!"
The {noun2} whispered something very {adverb} into the {noun1}'s {body_part}.
The {noun1} laughed so hard that they made a loud "{sound}!" and fell into the bushes
full of sharp {plural_noun}.
And that's how the {noun1} and {noun2} became best friends.
"""

# 4. Display Story
print("-"* 90 )
print("Here's your story:\n")
print(story)
print("-"* 90 )

# 5. Save the Story (Optional)
save_story = input("Would you like to save your story? (yes/no): ").lower()

if save_story == "yes":
    file_name = input("Enter a name for your story file (e.g., my_story.txt): ")
    with open(file_name, 'w') as file:
        file.write(story)
    print(f"Your story has been saved to {file_name}!")

print("Thanks for playing!")