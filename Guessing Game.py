# Student name: Andrea Phan
# Due date: Jan 29, 2025

# Create a guessing game where the player to guess a secret number between 1 and 100. 
# The player have 5 chances
# Depend on the player guess, the answer can be too low, too high, or correct.
# If the answer is correct, the game done; if the answer is too low or too high, continue to guess.

import random

def integer_input(min,max):
     while True:
        try:
            while True:
                guess = int(input("Please guess a number between 1 and 100: "))

                if guess >= min and guess <= max:
                    return guess      
                
        except:
             print("Please enter a number between 1 and 100. Try again.")

def play():
     random.seed()
     random_number = random.randint(1,100)

     guess_times = 1
     guess_checker = False

     while guess_times <= 5:
          player_guess = integer_input(1,100)
          if player_guess < random_number: 
              print("Your guess is too low! Try again.")
          elif player_guess == random_number:
              print("Congratulations! You guessed the number!")
              guess_checker = True
              break
          else:
              print("Your guess is too high! Try again.")
          guess_times += 1
    
     if guess_checker == False:
         print(f"Uh oh ... You lost :( The correct number was {random_number}.")

     

def main():
# A welcome message 
    print("Welcome to the game\n")
    player_reply = input("Do you want to play the game? (yes/no) ")
    
    if player_reply == 'yes':
         play_again = 'yes'
         while play_again == 'yes':
            play()
            play_again = input("Do you want to play again ('yes' or anything else to quit)? ")
         print('Goodbye.')
         
    else:
        print("Goodbye. Thank you for playing.")
        

main()

