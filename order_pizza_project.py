#!/usr/bin/python3
def welcome():
    print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")
    small = "small pizza = 800"
    medium = "medium pizza = 1200"
    large = "large pizza = 1600\n"

    print(small)
    print(medium)
    print(large)
    #print("Enter 1 , 2 or 3 \n")
    choice = int(input("Choose one number between 1 2 and 3\n"))
    my_Choice(choice)

def my_Choice(choice):
    #print("1 (Small Pizza)\n2 (Medium Pizza)\n3(Large Pizza)\n")
   # choice = int(input("Choose one number make your order between 1, 2 and 3: "))
    if choice == 1:
        print(f"You orders Small Pizza ")
    elif choice == 2:
        print(f"You ordered Medium Pizza ")
    elif choice == 3:
        print(f"You ordered Large Pizza")
    else:
        print("You entered an invalid choice please choose again\n!")
welcome()

