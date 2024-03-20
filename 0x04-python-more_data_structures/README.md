# 0x04. Python - More Data Structures: Set, Dictionary
Continuation of python which looks at sets, dictionaries, looping through sequences, conditions, comparing sequences with other types, lambda, map, filter and reduce.
# Resources
1.[Data structures](https://docs.python.org/3/tutorial/datastructures.html)
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
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

gallahad the pure
robin the brave
```
Looping through sequences to get position index and corresponding value:
```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

0 tic
1 tac
2 toe
```
To loop over two or more sequences at the same time, the entries can be paired with the zip() function:
```
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered:
```
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
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
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

apple
banana
orange
pear
```
** Note: ** It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

# Tasks
