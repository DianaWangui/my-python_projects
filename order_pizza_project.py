#!/usr/bin/python3
def welcome_menu():
    print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")
    small_pizza = 800
    medium_pizza = 1200
    large_pizza = 1800
    #  EXTRAS
    pepperoni = 30
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
    extras(choice)    
def extras(choice):
    pepperoni = 50
    cheese = 20

    total_small_pizza = 800 + 50
    total_medium_pizza = 1200 + 50
    total_large_pizza = 1800 + 50

    add_extra = input("Do you want to add extra Cheese and Pepperoni? Y/N ")
    if add_extra == 'Y':
        if choice == 1:
            print("Your new bill is now 850\n")
        elif choice == 2:
            print("Your new bill is now 1250\n")
        else:
            print("Your new bill is 1850\n")
    else:
        print("You did not add any extras")

        # Add function for checkout
welcome_menu()
