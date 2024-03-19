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
**operations that can be done on lists:**
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
**List methods:** list.append(x), list.extend(iterable), list.insert(i, x), list.remove(x), list.pop([i]), list.clear(), list.index(x[, start[, end]]), list.count(x), list.sort(*, key=None, reverse=False), list.reverse() and list.copy(). Example:
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

# list.pop([i])- Remove the item at the given position in the list, and return it. If no position specified removes last item.
>>> fruits.pop()
'pear'
```
**Lists as stacks**: A stack is a data structure that follows the Last In, First Out (LIFO) principle. It's named "stack" because it resembles a stack of items, where you can only add or remove items from the top. list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop()
```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack
[3, 4, 5]
```
**Lists as queues**:  a queue is a linear data structure that follows the First In, First Out (FIFO) principle. It's named "queue" because it resembles a line of people waiting for a service, where the first person to join the line is the first one to be served. This works in lists through insert and pop at the beginning of the list but it's slow and lists are inefficient for this. To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends
```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
**List comprehensions:** provide a concise way to create lists. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list from evaluating the expression in the context of the for and if clauses that follow it.
```
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
**Nested list comprehensions:** The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.
```
# transpose matrix 
>>> matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
    ]

# list comprehension
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# long method
>>> transposed = []
>>> for i in range(4):
       # the following 3 lines implement the nested listcomp
       transposed_row = []
       for row in matrix:
           transposed_row.append(row[i])
       transposed.append(transposed_row)

>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#  built-in functions instead of complex flow statements
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

**del statement:** Removes items from a list using index, can remove slices, clear entire list and entire variables
```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
>>> del a
```
#### B. Tuples and sequences
Immutable collection of values separated by commas that can be in parentheses. Elements are accessed through unpacking or indexing.
```
# tuple packing - values packed together in a tuple
>>> t = 12345, 54321, 'hello!'
>>> t[0] #indexing
12345
>>> t
(12345, 54321, 'hello!')

# Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# Immutable but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

# tuple unpacking
>>> t = (12345, 54321, 'hello!')  # Tuple with three elements
>>> x, y, z = t  # Sequence unpacking: Assigns 12345 to x, 54321 to y, and 'hello' to z
>>> print(x)
12345
>>> print(y)
54321
>>> print(z)
hello!

```
Creating an empty tuple and one with a single element:
```
>>> empty = () # Empty tuples are constructed by an empty pair of parentheses
>>> singleton = 'hello',    # a tuple with one item is constructed by following a value with a comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
   

