#!/usr/bin/python3

import os
# function to add input to a dictionary (data_dict): dictionary we are adding data
def add_to_dict(data_dict):
    name = input("Enter your name: ")
    bid = int(input("Whats your bid: "))

    # adding name as key and bid as key value of the dictionary
    data_dict[name] = bid


    # This is a function to clear the screen since next user should not see prev bider
    def clear_s():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    clear_s()

# initializing an empty dictionary
user_data = {}
# adding first user data to the dictionary
add_to_dict(user_data)

#test
print(user_data)

# creating an infinite loop to enter new bidders until user says no then it breaks out of the loop
while True:
    choice = input("Is anyone else ready to bid,enter 'y' for yes or 'n' for no: ")
    if choice.lower() == 'y':
        add_to_dict(user_data)
    elif choice.lower() == 'n':
        break
    else:
        print("Invalid input please enter 'y' or 'n'")


if user_data:
    higher_bidder = max(user_data, key=user_data.get)
    max_value = user_data[higher_bidder]
    print(f"Higher bidder is {higher_bidder} with {max_value}")
else:
    print("No one bid today")
