#!/usr/bin/python3
def welcome_menu():
    print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")
    small_pizza = 800
    medium_pizza = 1200
    large_pizza = 1800

    print(f"Choose 1 for Small pizza = {small_pizza}\n")
    print(f"Choose 2 for Medium Pizza = {medium_pizza}\n")
    print(f"Choose 3 for Large pizza = {large_pizza}\n")
    choice = int(input("Enter Your Choice Here: "))

    my_Choice(choice, small_pizza, medium_pizza, large_pizza)


def my_Choice(choice, small_pizza, medium_pizza, large_pizza):
    if choice == 1:
        print("You ordered Small Pizza ")
    elif choice == 2:
        print("You ordered Medium Pizza ")
    elif choice == 3:
        print("You ordered Large Pizza")
    else:
        print("You entered an invalid choice!! Try again\n!")
        welcome_menu()

    extras(choice, small_pizza, large_pizza, medium_pizza)


def extras(choice, small_pizza, large_pizza, medium_pizza):
    pepperoni = 50
    cheese = 20

    totalForSmall= small_pizza + pepperoni + cheese
    totalForMedium = medium_pizza + pepperoni + cheese
    totalForLarge = large_pizza + pepperoni + cheese

    add_extra = input("Do you want to add extra Cheese and Pepperoni? Y/N ")
    if add_extra == 'Y' or 'y':
        if choice == 1:
            print(f"Your new bill is now {totalForSmall}\n")
        elif choice == 2:
            print(f"Your new bill is now {totalForMedium}\n")
        else:
            print(f"Your new bill is {totalForLarge}\n")
        print("Lets now implement payment and checkout")
    else:
        print("You did not add any extras")
        add_extra_again = input("Do you still want to add extras? Y/N")
        if add_extra_again == 'y' or 'Y':
            extras(choice, small_pizza, large_pizza, medium_pizza)
        else:
            print("Now lets work on Payments")
            # Add function for payment and checkout


welcome_menu()
