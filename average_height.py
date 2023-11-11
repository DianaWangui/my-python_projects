#!/usr/bin/python3
def average_height():
    sum1 = 0
    count = 0
    list_height = input("Enter the heights separated by space: ")
    list_height = list_height.split()

    for i in range(len(list_height)):
        list_height[i] = int(list_height[i])

    print(list_height)
    for i in list_height:
        sum1 += i
        count += 1
    average = sum1 / count
    average = round(average, 2)
    print(average)
    return average


average_height()
