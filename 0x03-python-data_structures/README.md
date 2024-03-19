# 0x03. Python - Data Structures: Lists, Tuples
This is the beginning of python data structures that looks at lists and tuples.
## Resources
1. [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
2. [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
3. [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
## Summary
#### A. Lists
Mutable collection of data of the same or different type in square braces separated by commas. 
```
#simple list
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

#can be nested
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
operations that can be done on lists:
```
# indexing
>>> squares[-1]
25

# slicing
>>> squares[-3:]
[9, 16, 25]
# Assignment to slice is also possible
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5] = ['C', 'D', 'E']    # replace some values
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []   # now remove them
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:] = []    # clear the list by replacing all the elements with an empty list
>>> letters
[]

# concatenation
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# mutable so can change values
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

#get length
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```
**Note:** When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it. In example changes made to rgba reflect to rgb.
```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]
```
List methods: list.append(x), list.extend(iterable), list.insert(i, x), list.remove(x), list.pop([i]), list.clear(), list.index(x[, start[, end]]), list.count(x), list.sort(*, key=None, reverse=False), list.reverse() and list.copy(). Example:
```
# list.extend(iterable)- Extend the list by appending all the items from the iterable
>>> fruits = ['orange', 'apple', 'pear']
>>> fruits2 = ['banana', 'kiwi', 'apple', 'banana']
>>> fruits.extend(fruits2)  # alt: fruits.extend(['banana', 'kiwi', 'apple', 'banana'])
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# list.append(x)- Add an item to the end of the list
>>> fruits.append('grape')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

# list.insert(i, x)- Insert an item at a given position
>>> fruits.insert(0, 'cherry')
>>> fruits
['cherry','orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

# list.remove(x)- Remove the first item from the list whose value is equal to x
>>> fruits.remove('cherry')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

# list.count(x)- Return the number of times x appears in the list.
>>> fruits.count('apple')
2

# list.index(x[, start[, end]])- Return zero-based index in the list of the first item whose value is equal to x
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6

# list.reverse()- Reverse the elements of the list in place
>>> fruits.reverse()
>>> fruits
['grape', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# list.sort(*, key=None, reverse=False)- Sort the items of the list in place
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# list.pop([i])- Remove the item at the given position in the list, and return it
>>> fruits.pop()
'pear'
```

Lists as stacks

