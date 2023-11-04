#!/usr/bin/python3
num = input("Enter a number: ")
num = int(num)
if num == 0:
    print("You entered 0")
elif num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
