#!/usr/bin/python3

import random

def computers_choice():
    computer_choice = random.randrange(0, 3)
    print("Choices:\n0 for Rock\n1 for Paper\n2 for Scissor\n")
    print(f"Computers choice is: {computer_choice}.")
    invalid_user_choice(computer_choice)
    #return computer_choice

def invalid_user_choice(computer_choice):
    #print("Choices:\n1 for Rock\n2 for Paper\n3 for Scissor")
    user_choice = int(input("Users choice 0, 1, 2: "))
    if user_choice > 2 or user_choice < 0:
        print("Invalid input")
        return computers_choice()
    else:
        return  valid_user_choice(user_choice, computer_choice)

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

computers_choice()
