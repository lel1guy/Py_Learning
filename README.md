# Py_Learning
Here I will document my Python learning journey form zero experience. I'll be focusing on project-based learning because I learn better by doing.   I'm also gonna be using AI to help me learn.  
I'm Using:  
python 3.14  
VS Code  
Gemini Code Assit  
NotebookLM  
Perplexity for projects ideas  
  
Progress:  
Day 1:  
Project 1 - Mad Libs Word Game  
    I started by greating the user by using print comands, after i went into to collecting words from the user, for this I defined each word as a variable and used a input to get the word from the user. after wars i used story= f"""...""" and i wrote the stpry using the variables now defined to develop the story. after wards i use print to display the story. After this I used gemini code assist to learn how to save the sotry as file in the pc.  
      
Project 2 - Number guessing game  
    I Started by greating the user!  
    I used the import random to be able to get a random number for us to find, Afterwards i defined the secret_number as a randint (random interger) between 1 and 100. Then I prompt the user to guess a number in a certain number of tries.
    Then I used a while loop as long the numbers of tires was under 10. Then i used a if statment to see if the number was correct, if it was I would give the user the congrats message and break the loop, if its higher or lower it says to try higher or lower and the number of tries left. then i use a else if it wasnt found in under 10 tries. that leads to the game over screen!  
  
Project 3 - Rock, Paper, Scissors, Lizard, Spock  
    I started by greating the user and explain that we are going to be playing this game.  
    the First thing i set up was the import random after that i Start by defining the player and computer scores, the number of rounds needed to win and the round counter.  
    I define the choices and win conditions, then i use a while loop for the game and if, elif and else stamentes to see who wins or if its a draw. after the all the rounds are done i also use a if else to show who wins.

Day 2:  
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
