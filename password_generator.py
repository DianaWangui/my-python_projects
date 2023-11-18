#!/usr/bin/python3

import random
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '£', '%', '^', '*', '&', '~', '¬']
    print("Welcome to a password generator, making it easier for you!")
    noOfLetters = int(input("Enter the number of letter you want to use: "))
    noOfNumbers = int(input("Enter the number of numbers you want to use: "))
    noOfSymbols = int(input("Enter the number of symbols you want to use: "))

    list_password = []

    for i in range(1, noOfLetters + 1):
        Letter = random.choice(letters)
        list_password += Letter
    
    for i in range(1, noOfNumbers + 1):
        num = random.choice(numbers)
        list_password += num

    for i in range(1, noOfSymbols + 1):
        symbol = random.choice(symbols)
        list_password += symbol

    random.shuffle(list_password)

    str_password = ""
    for i in list_password:
        str_password += i

    return str_password


str_password = password_gen()
print(f"password is {str_password}")
