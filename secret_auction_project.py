#!/usr/bin/python3

import os

def add_to_dict(data_dict):
    name = input("Enter your name: ")
    bid = int(input("Whats your bid: "))
    data_dict[name] = bid

    def clear_s():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    clear_s()

user_data = {}
add_to_dict(user_data)
while True:
    choice = input("Is anyone else ready to bid, yes or no: ")
    if choice.lower() == 'y':
        add_to_dict(user_data)
    elif choice.lower() == 'n':
        break
    else:
        print("Invalid input please enter 'Y' or 'N'")


if user_data:
    higher_bidder = max(user_data, key=user_data.get)
    max_value = user_data[higher_bidder]
    print(f"Higher bidder is {higher_bidder} with {max_value}")
else:
    print("No one bid today")
