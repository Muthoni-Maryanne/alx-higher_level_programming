#!/usr/bin/python3

# program that prints all numbers from 0 to 98 in decimal and in hexadecimal
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

for i in range(99):
    print("{:d} = {:#x}".format(i, i))
