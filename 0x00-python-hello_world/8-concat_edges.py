#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find('object-oriented programming'):str.find(' language')] + str[str.find(' with'):str.find(' very')] + ' ' + str[0:6]
print(str)
