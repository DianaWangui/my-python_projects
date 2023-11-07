#!/usr/bin/python3
def welcome_menu():
    print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")
    small_pizza = 800
    medium_pizza = 1200
    large_pizza = 1800
    #  EXTRAS
    pepperone = 30
    cheese = 50

    print(f"Choose 1 for Small pizza = {small_pizza}\n")
    print(f"Choose 2 for Medium Pizza = {medium_pizza}\n")
    print(f"Choose 3 for Large pizza = {large_pizza}\n")
    choice = int(input("Enter Your Choice Here: "))
    my_Choice(choice)

def my_Choice(choice):
    if choice == 1:
        print("You ordered Small Pizza ")
    elif choice == 2:
        print("You ordered Medium Pizza ")
    elif choice == 3:
        print("You ordered Large Pizza")
    else:
        print("You entered an invalid choice!! Try again\n!")
        welcome_menu()
welcome()
