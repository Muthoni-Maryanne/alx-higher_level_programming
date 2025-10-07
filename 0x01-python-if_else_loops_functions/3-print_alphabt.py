#!/usr/bin/python3

# prints the ASCII alphabet, in lowercase, not followed by a new line
# Print all the letters except q and e
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

i = 97
while i <= 122:
    if i == 113 or i == 101:
        i += 1
        continue
  
    print("{:c}".format(i), end="")
    i += 1
