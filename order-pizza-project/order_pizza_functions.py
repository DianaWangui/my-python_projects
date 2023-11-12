#!/usr/bin/python3

def my_Choice(choice, small_pizza, medium_pizza, large_pizza):
    if choice == 1:
        print(f"\nYou ordered small pizza = {small_pizza} ")
    elif choice == 2:
        print(f"You ordered medium pizza = {medium_pizza} ")
    elif choice == 3:
        print(f"You ordered large pizza = {large_pizza}")
    else:
        print("You entered an invalid choice!! Try again\n")
        user_input(choice, small_pizza, medium_pizza, large_pizza)

    extras(choice, small_pizza, medium_pizza, large_pizza)

#  This function is used to add extras to the users already ordered pizza type

def extras(choice, small_pizza, medium_pizza, large_pizza):
    pepperoni = 50
    cheese = 20

    totalForSmall= small_pizza + pepperoni + cheese
    totalForMedium = medium_pizza + pepperoni + cheese
    totalForLarge = large_pizza + pepperoni + cheese
