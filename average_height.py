#!/usr/bin/python3
def average_height():
    # initilaizing sum and count to 0
    sum1 = 0
    count = 0

    #Accepting user input
    list_height = input("Enter the heights separated by space: ")

    #spliting user input to store in a list
    list_height = list_height.split()

    # Looping through the list and changing string to int and priting the list
    for i in range(len(list_height)):
        list_height[i] = int(list_height[i])
    print(list_height)

    
    # looping through the int list to find sum and to count the number of element in the list
    # Finding the average with the sum and the count and then rounding it off
    for i in list_height:
        sum1 += i
        count += 1
    average = sum1 / count
    average = round(average, 2)
    print(average)
    return average


average_height()
