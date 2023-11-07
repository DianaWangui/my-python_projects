#!/usr/bin/python3
print("Thank you for visiting Dianas Pizza Inn\nHere are the orders available\n")

small = "small pizza = 800"
medium = "medium pizza = 1200"
large = "large pizza = 1600\n"

print(small)
print(medium)
print(large)

print("1 (Small Pizza)\n2 (Medium Pizza)\n3(Large Pizza)\n")
choice = input("Choose one number make your order between 1, 2 and 3: ")
choice = int(choice)

if choice > 3:
    print("Your made an Invalid choice:")
elif choice == 1:
    print(f"You orders {small} ")
elif choice == 2:
    print(f"You ordered {medium} ")
elif choice == 3:
    print(f"You ordered {large} ")
