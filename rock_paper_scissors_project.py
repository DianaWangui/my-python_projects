#!/usr/bin/python3

# This is an imported module for a random numberchoice
# that will be used to check the computer moves

import random

# Function for the computer move using the random imported module
def computers_choice():
    computer_choice = random.randrange(0, 3)
    print("Choices:\n0 for Rock\n1 for Paper\n2 for Scissor\n")
    print(f"Computers choice is: {computer_choice}.")
    return invalid_user_choice(computer_choice)


# Function for users invalid input (Not including characters) 
def invalid_user_choice(computer_choice):
    #print("Choices:\n1 for Rock\n2 for Paper\n3 for Scissor")
    user_choice = int(input("Users choice 0, 1, 2: "))
    if user_choice > 2 or user_choice < 0:
        print("\nInvalid input. Enter Choice again!!\n")
        return invalid_user_choice(computer_choice)
    else:
        return  valid_user_choice(user_choice, computer_choice)


# Function for users valid input, this will now play the game
# This is where computer choice and user choice are compared
def valid_user_choice(user_choice, computer_choice):

    if user_choice == 1 and computer_choice == 0:
        print("User wins")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer wins")
    elif user_choice == 0 and computer_choice ==1:
        print("Computer wins")
    elif user_choice == 0 and computer_choice == 2:
        print("User wins")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer wins")
    elif user_choice == 2 and computer_choice == 1:
        print("User wins")
    else:
        print("You draw")

# To be updated
# I will implement a function where the user input is not an integer
computers_choice()
