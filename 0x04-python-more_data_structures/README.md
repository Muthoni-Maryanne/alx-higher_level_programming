# 0x04. Python - More Data Structures: Set, Dictionary
Continuation of python which looks at sets, dictionaries, looping through sequences, conditions, comparing sequences with other types, lambda, map, filter and reduce.
# Resources
1. [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
2. [Lambda Operator, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
3. [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)
# Summary
#### A. Sets
Unordered collection with no duplicates enclosed in curly braces. To create an empty set use set(). Examples:
```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
Similar to list comprehension there is set comprehension. Example:
```
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
#### B. Dictionaries
Key value pairs, enclosed in curly braces and separated by commas. They are indexed by keys,which are immutable so must have immutable values e.g. strings, numbers, or tuples and they must be unique: no duplicates. To create an empty dictionary use {} but dictionaries can also be built using dict().
```
# adding value to dictionary
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}

# accessing a value in a dictionary
>>> tel['jack']
>>> 4098

# deleting value in a dictionary
>>> del tel['sape']

# adding a new key-value pair to a dictionary
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}

# using list(d) on a dictionary which results in a list of the keys
>>> list(tel)
['jack', 'guido', 'irv']

# sorting a dictionary which sorts the keys
>>> sorted(tel)
['guido', 'irv', 'jack']

# checking if keys are in a dictionary or not
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

# creating dictionaries with dict()
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
There are also dictionary comprehensions. Example:
```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

#### C. Looping Techniques
Looping through dictionaries:
```
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
       print(k, v)

gallahad the pure
robin the brave
```
Looping through sequences to get position index and corresponding value:
```
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
       print(i, v)

0 tic
1 tac
2 toe
```
To loop over two or more sequences at the same time, the entries can be paired with the zip() function:
```
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
       print('What is your {0}?  It is {1}.'.format(q, a))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered:
```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
       print(i)

apple
apple
banana
orange
orange
pear
```
Using sorted() and set() on a sequence to get unique elements of the sequence in sorted order:
```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
       print(f)

apple
banana
orange
pear
```
**Note:** It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

#### D. Lambda, map, filter and reduce
**Lambda:** The general syntax of a lambda function: ```lambda argument_list: expression```. Example:
```
# x,y comma-separated list of arguments and x + y is the expression and function has been assigned to a variable
sum = lambda x, y : x + y 
sum(3,4)
```
**Map:**: Advantage of lambda seen when combined with map() function. Syntax: ```r = map(func, seq)```. Example:
```
>>> C = [39.2, 36.5, 37.3, 38, 37.8] #sequence/seq
>>> # lambda has been used to shorten the function.
>>> F = list(map(lambda x: (float(9)/5)*x + 32, C))
>>> print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]
```
If lambda had not been used and the function had been defined with a longer method:
```
>>> def Fahrenheit(T):
       return ((float(9)/5)*T + 32)
>>> temperatures = (39.2, 36.5, 37.3, 38, 37.8)
>>> F = map(Fahrenheit, temperatures)
>>> temperatures_in_Fahrenheit = list(map(Fahrenheit, temperatures))
>>> print(temperatures_in_Fahrenheit)
[97.7, 98.60000000000001, 99.5, 100.4, 102.2]
```
Mapping can be applied to more than one sequence at the same time and if one has fewer elements map will stop when the shortest list has been consumed e.g:
```
>>> a = [1, 2, 3]
>>> b = [17, 12, 11, 10]
>>> c = [-1, -4, 5, 9]
>>> list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
[37.5, 33.0, 24.5]
```
**Filter:** Syntax: ```filter(function, sequence)``` The function filter(f,l) needs a function f as its first argument. f has to return a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element be produced by the iterator, which is the return value of filter(function, sequence). Example:
```
>>> even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
```
**Reduce:** Syntax: ```reduce(func, seq)```. Reduce continually applies the function func() to the sequence seq. It returns a single value. If seq = [ s1, s2, s3, ... , sn ] this is an illustration of what happens:

![ex2](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/c06a42d8-cc53-4fd3-b911-42dbbf135d2b)
Example:
```
>>> import functools
>>> functools.reduce(lambda x,y: x+y, [47,11,42,13])
113
```
![ex1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/92978c3e-f7f0-4a29-be5f-6fc449fe0c45)

# Tasks
