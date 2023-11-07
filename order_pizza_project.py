#!/usr/bin/python3

#  This welcome_menu is a function that welcome a user to the available menu in the pizza inn restaurant.
#  It allows user to see all the prices of the pizza and allows them to see how they 
#  Will make choices on the pizza type they want and also allows them to make a choice
#  It then call the next function which is the my_Choice function

def welcome_menu():
    print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")

    small_pizza = 800
    medium_pizza = 1200
    large_pizza = 1800

    print(f"Small pizza = {small_pizza}")
    print(f"Medium pizza = {medium_pizza}")
    print(f"Large pizza = {large_pizza}\n")

    print(f"Choose 1 for Small pizza")
    print(f"Choose 2 for Medium Pizza")
    print(f"Choose 3 for Large pizza\n")

#  This is a loop to check if a user has entered a non integer value
#  While making the choice of the pizza type they want
#  It will print an error message if they actually choose a non int value

    while True:
        try:
            choice = int(input("Enter Your Choice Here: "))
            break # if the input is an integer break out of the loop
        except ValueError:
            print("\nInvalid input. Please enter a number 1, 2 or 3\n")
        welcome_menu()  #  Call the function again for them to re enter the value

#  Otherwise call the my)Choice function to print what they ordered and the price 
    my_Choice(choice, small_pizza, medium_pizza, large_pizza)

#  This function, my_Choice is used to check the choice the user made when choosing the type of pizza they want.
#  It allows them to see what they ordered and the prices
#  This function also calls the extra function to ask if the user would want anything extra apart from the pizza

def my_Choice(choice, small_pizza, medium_pizza, large_pizza):
    if choice == 1:
        print(f"\nYou ordered small pizza = {small_pizza} ")
    elif choice == 2:
        print(f"You ordered medium pizza = {medium_pizza} ")
    elif choice == 3:
        print(f"You ordered large pizza = {large_pizza}")
    else:
        print("You entered an invalid choice!! Try again\n")
        welcome_menu()

    extras(choice, small_pizza, large_pizza, medium_pizza)

#  This function is used to add extras to the users already ordered pizza type
#  The function allows user to either add or not add any extra, if the user clicks no by mistakes,
#  It still confirms if they are sure they dont want any extras and procced to payment in both of the cases

def extras(choice, small_pizza, large_pizza, medium_pizza):
    pepperoni = 50
    cheese = 20

    totalForSmall= small_pizza + pepperoni + cheese
    totalForMedium = medium_pizza + pepperoni + cheese
    totalForLarge = large_pizza + pepperoni + cheese

#  Another loop to check if the user entered an integer value
#  If not it prints an error message and propmts them to choose extras again

    while True:
        try:
            add_extra = input("\nDo you want to add extra Cheese and Pepperoni? 1 for Yes 0 for No: ")
            add_extra = int(add_extra)
            break  #  Breaking out of loop incase the entered value is an integer
        except ValueError:
            print("Invalid input. Enter a Number e.g 1 or 0\n")
        extras(choice, small_pizza, large_pizza, medium_pizza)

#  Comparing what extras a user used and their initial choice of type of pizza ordered
#  This will now calculate the total of the order plus extras
#  If no extra was chosen prompt them to chose an extra again

    if add_extra == 1:
        if choice == 1:
            print(f"Your new bill is now {totalForSmall}\n")
        elif choice == 2:
            print(f"Your new bill is now {totalForMedium}\n")
        else:
            print(f"Your new bill is {totalForLarge}\n")
        print("Lets now implement payment and checkout")
    else:
        print("You did not add any extras")

#  A loop to check if the add extra again is an integer or not
#  If its not print error and prompt them to enetr an integer(number)

        while True:
            try:
                add_extra_again = input("\nDo you still want to add extras? 1 for Yes and 0 for No: ")
                add_extra_again = int(add_extra_again)
                break  #  Break out of the loop if the entered value is an integer(number)
            except ValueError:
                print("Invalid Input. Enter a number, 1 or 0\n")
            extras(choice, small_pizza, large_pizza, medium_pizza)

#  Check the choice made on the extras again if they made an error and clicked no
#  While they meant yes, prompt them to re enter again
#  Othewise go to payment

        if add_extra_again == 1:
            extras(choice, small_pizza, large_pizza, medium_pizza)
        else:
            print("Now lets work on Payments")
         #  Add function for payment and checkout


welcome_menu()
