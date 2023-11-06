#!/usr/bin/python3

# Take input from user using input function
Height = float(input("Enter your Height here: "))
Weight = float(input("Enter your Weight here: "))

# Now lets calculate the BMI of the user
bmi = Weight /(Height * Height)
print(bmi)

# Checking the condition of the user
if bmi < 18.5:
    print("You are underweight you need to eat healthy")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight keep it up")
elif bmi >= 25 and bmi < 30:
    print("You are overweigth, please check your diet")
elif bmi >= 30 and bmi < 35:
    print("You are obese, kindly consider seeing a doctor")
elif bmi > 35:
    print("You are clinically obese!! Please see a doctor immediately")
