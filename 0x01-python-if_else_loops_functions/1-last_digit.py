#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mystr = f"Last digit of {number} is"
if number < 0:
    number = -number
last_number = number % 10
if last_number > 5:
    print(f"{mystr} {last_number} and is greater than 5")
elif last_number == 0:
    print(f"{mystr} {last_number} and is 0")
elif last_number < 6 and  last_number != 0:
    print(f"{mystr} {last_number} and is less than 6 and not 0")