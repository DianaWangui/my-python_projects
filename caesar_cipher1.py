#!/usr/bin/python3
a = ('a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def encryption(message, shift):
    cipher = ""
    len_a = len(a)
    for char in message:
        if char in a:
            position = a.index(char)
            new_position = (position + shift) % len_a
            cipher += a[new_position]
        else:
            cipher += char
    print(f"result: {cipher}")


def decryption(message, shift):
    cipher = ""
    len_a = len(a)
    for char in message:
        if char in a:
            position = a.index(char)
            new_position = (position - shift) % len_a
            cipher += a[new_position]
        else:
            cipher += char
    print(f"result: {cipher}")


while True:
    print("Welcome to an encyption program")
    
    choice = input("Enter 'e' for encryption and 'd' for decryption: ")
    text = input("Enter your message to decrypt or encrypt: ")
    try:
        shift_no = int(input("Enter the number of time you want to shift: "))
    except ValueError:
        print("Invalid shift value. Enter valid integer\n")
        continue
    
    if choice == "e":
        encryption(message = text,shift = shift_no)
    elif choice == "d":
        decryption (message = text, shift = shift_no)
    else:
        print("Error")


    cont = input("Type 'yes' if you want to do repeat, otherwise type 'no': ")
    if cont.lower() != "yes":
        print("See you soon")
        break
