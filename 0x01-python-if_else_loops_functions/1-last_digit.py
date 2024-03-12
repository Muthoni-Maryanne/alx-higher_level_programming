#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((-1 * number) % 10) * -1

print("Last digit of {} is {} and is ".format(number, last_digit), end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
else:
    print("0")
