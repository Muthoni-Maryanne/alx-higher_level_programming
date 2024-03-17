# 0x01. Python - if/else, loops, functions
This is a continuation of Python. Concepts looked at include: control flows, indentation error, string formatting and pycodestyle.
## Resources
1. [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
2. [Indentation error](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
3. [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
4. [Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
5. [Pycodestyle](https://pypi.org/project/pycodestyle/)

## Summary
#### Control flows
a. if statement
```
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```
b. for statement 

In python, for is for iterating over the items of any sequence (a list or a string), in the order that they appear in the sequence.
```
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```
c. range()

Use it with for to generate arithmetic progressions. Also can iterate over sequences.
```
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]

>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
       print(i, a[i])
0 Mary
1 had
2 a
3 little
4 lamb
```
d. break and continue statements.

Break breaks out of the innermost enclosing for or while loop while continue continues with the next iteration of the loop.
```
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```
```
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
```
e. pass

Does nothing, used when a statement is required syntactically but the program requires no action.
```
while True:
    pass
# creating minimal classes
class MyEmptyClass:
    pass
# place-holder for a function or conditional body when you are working on new code
def initlog(*args):
    pass
```

f. match

Similar to switch in C, takes an expression and compares its value to successive patterns given as one or more case blocks.
```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
g. Functions
```
>>> def fib2(n):    # return Fibonacci series up to n  # start with def keyword, function name then formal parameters
      """Return a list containing the Fibonacci series up to n."""     #documentation string
      result = []    # start of body of function, result variable introduced which is a list
      a, b = 0, 1    # local variables stored in function's local symbol table
      while a < n:
          result.append(a)    # list method to append value of a to end of list
          a, b = b, a+b
      return result           # function returns list value but if there was no return statement function returns None

>>> f100 = fib2(100)    # call function, new variable assigned also point to that same function object and can access function
>>> f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
h. Defining functions

1. Default argument values

Not all arguments need to be used when calling function, just the default standard one that can be positional or keyword. Example using positional arguments to call:
```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
can call this function:
giving only the mandatory argument: ask_ok('Do you really want to quit?')

giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)

or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

2. Keyword arguments

Functions can also be called using keyword arguments of the form kwarg=value e.g
```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
Function can be called in any of these ways:
```
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
when you have *name and **name in parameters, *name is a tuple type of positional argument and **name is a dictionary type of keyword argument. Example of definition and call:
```
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
3. Special parameters
   
Restrict way arguments are passed for readability and efficiency. Syntax:
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```
![special](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/ba7bd70d-2537-48a8-8b99-f79975ee8d6d)

How to define and call:
```
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(arg = 2)
standard_arg(2)

pos_only_arg(1)

kwd_only_arg(arg = 3)

combined_example(1, standard = 2, kwd_only = 3)
combined_example(1, 2, kwd_only = 3)
```
**NOTE**

keyword  arguments: argument preceded by an identifier e.g 'name =' or passed as a value in a dictionary preceded by **

positional arguments: appear at beginning of an argument list or be passed by elements of an iterable preceded by *
```
#keyword
complex(real = 3, imag = 5)
complex(**('real' : 3, 'imag' : 5)

#positional
complex(3,5)
complex(*(3,5)
```
## Tasks
**Task 0:**  [0-positive_or_negative.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py)

Complete the source code in order to print whether the number stored in the variable number is positive or negative.

![0](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/e19af7bd-a49d-4bda-98a0-9d8be99cc2ba)

**Task 1:**  [1-last_digit.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/1-last_digit.py)

Complete the source code in order to print the last digit of the number stored in the variable number.

![1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/9f7bdd45-2d88-4b03-bc39-65b1524e5e2a)
