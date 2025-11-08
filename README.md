# Py_Learning
Here I will document my Python learning journey form zero experience. I'll be focusing on project-based learning because I learn better by doing.   I'm also gonna be using AI to help me learn.  
I'm Using:  
python 3.14  
VS Code  
Gemini Code Assit  
NotebookLM  
Perplexity for projects ideas  
  
Progress:  
Day 1 (3/11/25):  
Project 1 - Mad Libs Word Game  
    I started by outlining the goal in comments: to ask a user for random words and use them to build a funny story. The steps I planned were: Greet User, Request Words, Create Story, Display Story, and an optional Save Story step.  
    First, I used print statements to welcome the user, explain the game, and print a separator line ("-"* 90).  
    Next, to request the words, I used a series of input functions. I prompted the user for various types of words (like nouns, adjectives, verbs, etc.) and stored each response in a dedicated variable, such as noun1, adjective1, verb, body_part, and so on.  
    Once I had all the user's words, I created the story itself. I used a multi-line f-string for this. This allowed me to write out the story template and embed the user's variables (like {noun1} and {adjective2}) directly into the text. This complete story was stored in the story variable.  
    After the story was created, I printed another separator line and then printed the story variable, showing the user their finished, funny story.  
    For the final, optional step, I wanted to let the user save their creation. I used input to ask if they wanted to save the story and stored their answer in save_story, using .lower() to make the check case-insensitive.  
    I used an if statement to check if save_story was equal to "yes". If it was, I prompted the user for a file_name using input. Then, I used a with open(file_name, 'w') as file: block. This opens the specified file in write mode ('w'). Inside this block, I used file.write(story) to write the contents of the story variable into the file. Finally, I printed a confirmation message showing them where the file was saved.  
    At the very end, I just printed a "Thanks for playing!" message to exit the program.  
    
Project 2 - Number guessing game  
   I started by outlining the goal in comments: the computer would pick a number from 1 to 100, and the user had to guess it within 10 tries.  
    First, I had to import random so the computer could pick a secret number.  
    Then, I used print statements to greet the user, explain the game, and print a separator line ("="* 90) to make it look clean.  
    To set up the game, I used random.randint(1, 100) to get the secret_number and stored it in a variable. I also created two variables to control the game: attempts (which I set to 0) and max_attempts (which I set to 10).  
    To handle all the guesses, I put the main logic inside a while loop. This loop keeps running as long as the attempts variable is less than max_attempts.  
    Inside this loop, I immediately started a try...except block. I did this to make sure the program wouldn't crash if the user entered text instead of a number.  
    Inside the try block, I used input to ask the user for their guess. I used int() to convert their answer into a number and store it in the guess variable. Right after, I added 1 to the attempts counter.  
    I then added a quick if statement to validate the input, checking if the guess was less than 1 or greater than 100. If it was, I printed a message and used continue to skip the rest of the loop and ask for a new guess.  
    Next, I used a main if, elif, and else series to handle the game logic:  
    For the if: I checked if the guess was equal to the secret_number. If it was, the user won. I printed a "Well done!" message, showed them the number and how many attempts it took, and then used the break command to exit the while loop and end the game.  
    For the elif: I checked if the guess was less than the secret_number. If it was, I printed "Try Higher!" and also showed them how many tries they had left.  
    For the else: This automatically catches any guess that is greater than the secret_number. It prints "Try Lower!" and the number of remaining tries.  
    The except ValueError: part of my try...except block just prints an error message if the user types invalid input.  
    Finally, I used a special feature by adding an else block to the while loop itself. This else block only runs if the loop finishes without a break. This is the "lose" condition. If the user runs out of tries, this block prints "GAME OVER" and tells them what the secret_number was.  
  
Project 3 - Rock, Paper, Scissors, Lizard, Spock  
   I started by outlining the goal in the comments: to create a "best of 5" game of Rock, Paper, Scissors, Lizard, Spock. To do this, I first had to import random so the computer could choose its move.  
    I used several print statements to welcome the user and explain the rules. I set it up as a "best of 5" game, clarifying that the first player to get 3 wins would be the overall winner. I also created a multi-line string variable called rules and printed it, showing the full "Big Bang Theory" explanation of what beats what. To set up the game state, I created variables for the player_score and computer_score, setting them both to 0. I also made a rounds_to_win variable and set it to 3.  
    For the game's core logic, I first created a list called choices that holds all the valid string inputs. Then, I created a dictionary called win_conditions. In this dictionary, each key is a move (like "rock") and its value is a list of the moves it beats (e.g., ["scissors", "lizard"]).  
    I put the entire game inside a main while loop. This loop keeps running as long as the player_score is less than rounds_to_win and the computer_score is also less than rounds_to_win.  
    Inside this loop, I first increment the round_counter and print the current round and score. Then, I used random.choice(choices) to get the computer_choice and stored it in a variable. I used input to ask the user for their move and used .lower() to make sure the case matched.  
    I added an if statement right after to handle validation. I checked if the player_choice was not in my choices list. If it was invalid, I printed an error and used the continue command to skip the rest of the loop and start the round over.  
    To determine the winner of the round, I used an if, elif, else block:  
    First, the if statement checks if player_choice is equal to computer_choice. If it is, I print "It's a draw!".  
    Next, the elif statement was my logic for the player winning. I used the player_choice as a key to get the list from my win_conditions dictionary and checked if that resulting list was equal to the computer_choice string. If it matched, I printed "You win!" and added 1 to the player_score.  
    Finally, the else block catches all other outcomes. This means the computer won, so I print a "Computer Won" message and add 1 to the computer_score.  
    After the while loop finishes (meaning one player has reached 3 wins), I print the final score and a "GAME OVER!" message.  
    I used one last if/else statement to check if the player_score was greater than the computer_score. This determines who is the overall winner, and I print a final congratulations or "Better luck next time" message.  
      
Day 2 (4/11/25):  
Project 4 - Hangman  
  I started by greeting the user and explaining the rules of the game, such as having 6 tries and guessing one letter at a time.  
  First, I used the import random module to be able to pick a random word.  
  Then I defined a word_list with all the possible 4-letter animal words. I also defined a list called hangman_stages that holds all the ASCII art for the different stages of the hangman.  
  After that, I set up the main game variables: I used random.choice to pick the secret_word from the list, set max_attempts to 6, created an empty list for guesses, and made a word_completion list (using underscores) to show the player's progress.  
  I used a while loop to run the game as long as attempts_left was greater than 0 and there were still underscores in the word_completion.
  Inside the loop, I print the current hangman_stage, the word_completion, and the list of guessed letters. Then I prompt the user for a guess.  
  I used if and elif statements to validate the input, checking if it was a single letter and if it had already been guessed.  
  If the guess was correct and in the secret_word, I used a for loop with enumerate to find all its positions and update the word_completion list. If it was wrong, I subtracted 1 from attempts_left.  
  After the while loop ends, I use one last if/else statement to check if the word was guessed (no underscores left) to print a congrats message, or else I print the final hangman stage and show the secret_word.  
    
Project 5 - To Do List  
    I started by defining an empty list called `tasks` which would be used to store all the tasks. To make the program keep running, I put everything inside a main `while True` loop.  
    Inside this loop, I first `print` a menu for the user, showing the 4 options: View Tasks, Add Task, Mark Task as Complete, and Quit. Then I used an `input` to get the user's `choice`.  
    I used a series of `if`, `elif`, and `else` statements to handle what to do based on the `choice`.  
    For choice '1', I first check if the `tasks` list is empty. If it is, I print a message. If not, I use a `for` loop with `enumerate` to print each task's number, status, and description. I store each task as a dictionary, so I check the 'completed' value to decide whether to print a checkmark '✓' or a blank space.  
    For choice '2', I use `input` to ask the user for a new task description. I then create a new dictionary for that task (e.g., `{"task": "description", "completed": False}`) and `append` it to the main `tasks` list.  
    For choice '3', I first show the user all the tasks again so they can see the numbers. I used a `try...except` block to make sure the user enters a valid number. If they do, I use their input (minus 1, to get the correct list index) to find the task in the `tasks` list and set its 'completed' value to `True`.  
    For choice '4', I just print a goodbye message and use the `break` command to exit the `while True` loop, which ends the program.  
    Finally, an `else` statement at the end catches any invalid menu choices and prompts the user to try again.  
  
Day 3 (5/11/25):  
Project 5 - to do list v2  
    To create to_do_list-v2.py, I started by taking all the logic that was grouped inside the single while True loop and refactoring it by organizing it into functions. This makes the code much cleaner and easier to read.  
    I created a main function that now holds the empty tasks list and the main while True loop. This main function is now the central part of the program.  
    Inside the main loop, I first call a new function I made, show_menu(), which just handles printing the 4 options for the user.
    The if, elif, and else statements that check the user's choice are still inside the while True loop, but now they are much simpler. Instead of containing all the logic, they just call other new functions based on the choice.  
    For choice '1', the loop now calls view_task(tasks). I moved all the logic for checking if the tasks list is empty and the for loop with enumerate into this new function. I have to pass the tasks list to it as an argument so it knows what to print.  
    For choice '2', it calls add_task(tasks). This function now handles getting the input for the new task description, creating the new task dictionary, and appending it to the tasks list.  
    For choice '3', it calls mark_task_complete(tasks). This is a big improvement. Instead of having to copy and paste the code to print all the tasks, this function can now just call view_task(tasks) first. After that, it uses the same try...except block as before to get the task number and set its "completed" value to True.  
    For choice '4', the break command and the final else statement for invalid choices remained inside the main loop's while True, as they control the loop itself.  
    Finally, at the very end of the file, I added an if __name__ == "__main__": block. This is a standard Python practice that tells the script to run the main() function only when the file is executed directly.  
      
Day 6 (7/11/25):  
Project 6 - Unit Converter (in Progress)  
    I started by outlining the goal in the comments: to create a program that can convert measurements from one type to another, handle multiple measurement types, and use a menu.  
    Following the pattern from my "to do list v2" project, I decided to build this program by organizing all the logic into functions right from the start.  
    At the very bottom of the file, I added the if __name__ == "__main__": block. This is the standard way to make the script run my main() function when the file is executed.  
    Inside the main() function, I first used print statements to welcome the user. I then put the main program flow inside a while True loop to make it keep running.  
    Inside this loop, I first call a function I made, show_menu(), which just handles printing the list of conversion options (Length, Weight, Temperature, etc.). Immediately after, I call another function, get_user_choice().  
    This get_user_choice() function is a reusable helper. It uses its own while True loop and a try...except ValueError block to make sure the user enters a valid integer (from 1 to 5). It won't let the program continue until it gets a valid choice.  
    Back in the main() loop, I used a series of if and elif statements to handle the choice returned from get_user_choice(). For choices '1' through '4', I just printed a confirmation message (like "Length Conversion Chossen") and added a #todo: comment to remember to implement the logic later. For choice '5', I printed a "GoodBye!" message.  
    To prepare for the conversion logic, I also built several other helper functions:  
    validate_numeric_input(): A general-purpose function that uses try...except to get a float (a number with decimals) from the user and reject invalid text.  
    get_conversion_value(): A simple function that uses validate_numeric_input() to ask for the number the user wants to convert.  
    get_unit_selection(): Another helper that takes a list of units and asks the user to pick one by its number.  
    Finally, I started building the actual logic for the first choice. I created a lenght_conversion() function (which would be called by main when choice == 1). This function defines a list of all the units (like "inches", "feet", etc.) and then calls my helper functions to get the value, the from_unit, and the to_unit.  
    To do the math, I created convert_length(). My plan here was to use a central base unit (meters). I created a dictionary called to_meters that holds the conversion factor to turn any unit into meters. I also created a from_meters dictionary to convert from meters into any other unit. This way, any conversion is a two-step process: [Original Unit] -> Meters -> [Target Unit]
