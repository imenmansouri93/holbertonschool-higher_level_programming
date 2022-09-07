#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
A = number % 10
if (A > 5):
    print(f"Last digit of {number} is {A} and is greater than 5")
elif (A == 0):
    print(f"Last digit of {number} is {A} and is 0")
elif (A < 0 & A != 0):
    print(f"Last digit of {number} is {A} and is less than 6 and not 0")
