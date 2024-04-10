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

## Tasks
