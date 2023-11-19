#!/usr/bin/python3

#This function is used for shifting the element according to user input
def shift_char(char, shift):
    if char.isalpha():
        start = ord('a') if char.islower() else ord('A')  #initializing where to start
        position = ord(char) - start  #setting position of our charater
        new_position = (position + shift) % 26  #new position after shifting
        return chr(new_position + start)  # comverting new position to a character
    else:
        return char  # Return the char as it is if its not an alphabet


#This is the encrypting function it encrypt user message
def encryption(message, shift):
    encrypt_list = []  # a list to append all our element after encrption
    for char in message:
        encrypt_list.append(shift_char(char, shift))  #appending all element to the list
    result = "".join(encrypt_list) # creating a string from the list generated
    print(f"Your encryption text is: {result}")


# Function for decrypting user message
def decryption(message, shift):
    decrypt_list = []
    for char in message:
        decrypt_list.append(shift_char(char, -shift))  # using negative to shift to the right when decrypting
    cipher = "".join(decrypt_list)
    print(f"Your decryption text is: {cipher}")



# Where our program starts to execute and calling each function
while True:
    print("Welcome to an encyption program")
    
    choice = input("Enter 'e' for encryption and 'd' for decryption: ")
    text = input("Enter your message to decrypt or encrypt: ")

    # This will handle exception when user enters a non int shift value
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


    # this will ask if user want to repeat the process of encryption again    
    cont = input("Type 'yes' if you want to do repeat, otherwise type 'no': ")
    if cont.lower() != "yes":
        print("See you soon")
        break
