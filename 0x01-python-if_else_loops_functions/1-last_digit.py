#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    digit = number % -10
else:
    digit = number % 10

variable = "Last digit of {:d} is {:d}"
if digit > 5:
    print(variable.format(number, digit) + " and is greater than 5")
elif digit <= 6 and digit != 0:
    print(variable.format(number, digit) + " and is less than 6 and not 0")
else:
    print(variable.format(number, digit) + " and is 0")
