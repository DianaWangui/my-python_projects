#!/usr/bin/python3
import random
def head_tail():
    a = random.randrange(0, 2)
    if a < 1:
        print("Tail")
    else:
        print("Head")

head_tail()
