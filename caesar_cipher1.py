#!/usr/bin/python3
#a = ('a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def shift_char(char, shift):
    if char.isalpha():
        start = ord('a') if char.islower else ord('A')
        position = ord(char) - start
        new_position = (position + shift) % 26
        return chr(new_position + start)
    else:
        return char


def encryption(message, shift):
    encrypt_list = []
    for char in message:
        encrypt_list.append(shift_char(char, shift))
    result = "".join(encrypt_list)
    print(f"Your encryption text is: {result}")


def decryption(message, shift):
    decrypt_list = []
    for char in message:
        decrypt_list.append(shift_char(char, -shift))
    cipher = "".join(decrypt_list)
    print(f"Your decryption text is: {cipher}")


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
        print("Invalid input please")


    cont = input("Type 'yes' if you want to do repeat, otherwise type 'no': ")
    if cont.lower() != "yes":
        print("See you soon")
        break
