#!/usr/bin/python3
currentAge = input("Enter your current age: ")
currentAge = int(currentAge)
remainingYears = 90 - currentAge
remainingMonths = remainingYears * 12
remainingWeeks = remainingYears * 52
remainingDays = remainingYears * 356

print(f"You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months, and {remainingYears} left")
