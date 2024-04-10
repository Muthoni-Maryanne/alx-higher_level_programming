# 0x05. Python - Exceptions
This is a continuation of Python that looks at errors, exceptions and how to handle them.

## Resources
1. [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
2. [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)
   
## Summary
a. Syntax/parsing errors
```
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```
b. Exceptions

Errors detected during execution are called exceptions and are not unconditionally fatal. 

Most exceptions are not handled by programs, however, and result in error messages as shown here:
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

**Handling Exceptions**
1. try...except: most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well) e.g
```
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
2. try...except...else: The try … except statement has an optional else clause, which, when present, must follow all except clauses.

It is useful for code that must be executed if the try clause does not raise an exception e.g
```
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
**Raising exceptions:**

Allows the programmer to force a specified exception to occur. The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class.

Also exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause e.g.
```
def example_function():
    try:
        # Some code that might raise an exception
        x = int(input("Enter a number: "))
        if x < 0:
            raise ValueError("Number must be positive")
    except ValueError as e:
        # Handle the exception at this level
        print("Error:", e)
        # Reraise the exception to propagate it further
        raise

try:
    example_function()
except ValueError:
    print("An error occurred in the function.")
```
**Exception chaining**
```
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc    #indicate exception is direct consequence of another
```
can be disabled using None e.g
```
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
```
**User defined exceptions**
Programs may name their own exceptions by creating a new exception class. 

Exceptions should typically be derived from the Exception class, either directly or indirectly e.g
```
class DogNameError(Exception):               #inherit from Exception class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

try:
    dogName = input("What is your dog's name? ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print("Your dog's name cannot contain a number.")
```
**Defining clean-up actions**
1. finally: optional clause which is intended to define clean-up actions that must be executed under all circumstances e.g
```
>>> def divide(x, y):
       try:
           result = x / y
       except ZeroDivisionError:
           print("division by zero!")
       else:
           print("result is", result)
       finally:
           print("executing finally clause")

>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
As you can see, the finally clause is executed in any event. The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

**Predefined Clean-up Actions**

Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed.
```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly. After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

**Raising and Handling Multiple Unrelated Exceptions**
```
# Define an ExceptionGroup class
class ExceptionGroup(Exception):
    def __init__(self, message, exceptions):
        super().__init__(message)
        self.exceptions = exceptions

# Define a function that raises an ExceptionGroup
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('There were problems', excs)

try:
    f()
except Exception as e:
    print(f'Caught {type(e)}: {e}')
```
**Enriching Exceptions with Notes**
cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method add_note(note) that accepts a string and adds it to the exception’s notes list e.g
```
>>> try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note('Add some more information')
        raise

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
>>>
```

## Tasks

**Task 1:** [1-safe_print_integer.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py)

Write a function that prints an integer with "{:d}".format()

![1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/4953da62-0a3b-432b-84bb-3fb242e48db2)
