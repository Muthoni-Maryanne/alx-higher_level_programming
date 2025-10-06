#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + ' ' + str[str.find('wi'):str.find(' ve')] + ' ' + str[0:6]
print(str)
