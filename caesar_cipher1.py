#!/usr/bin/python3
a = ('a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def encryption(message, shift):
    cipher = ""
    for char in message:
        position = a.index(char)
        new_position = position + shift
        cipher += a[new_position]
    print(f"result: {cipher}")

def decryption(message, shift):
    cipher = ""
    for char in message:
        position = a.index(char)
        new_position = position - shift
        cipher += a[new_position]
    print(f"result: {cipher}")

def do():
    print("Welcome to an encyption program")
    choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption: ")
    text = input("Enter your message to decrypt or encrypt: ")
    shift_no = int(input("Enter the number of time you want to shift: "))
    if choice == "encrypt":
        encryption(message = text,shift = shift_no)
    elif choice == "decrypt":
        decryption (message = text, shift = shift_no)
    else:
        print("Error")

do()
cont = input("Type 'yes' if you want to do repeat again, otherwise type 'no': ")
if cont == "yes":
    do()
else:
    print("See you soon")

