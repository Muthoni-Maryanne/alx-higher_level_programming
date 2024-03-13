# 0x00. Python - Hello, World

This is the beginning of Python. Concepts looked at include: the python interpreter, numbers, strings, indexing, slicing and string interpolation using %, .format and fstrings.

## Resources

1. [The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)
2. [Python's F-String for String Interpolation and Formatting](https://realpython.com/python-f-strings/)
3. [Learn to Program](https://www.youtube.com/watch?v=nwjAHQERL08&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=1)
4. [Pycodestyle](https://pypi.org/project/pycodestyle/)

## Summary

#### Options when invoking python
```python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]```
#### Changing encoding from default UTF-8
``` # -*- coding: encoding -*-```
```
# -*- coding: cp1252 -*-
```
```
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```
#### Comments
```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```
#### Numbers
Python works with floats and ints.
```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17
>>> 5 ** 2  # 5 squared
25
```
#### Text (str)
Can be in single, double or triple quotes.
For multiple lines use triple quotes, can be single or double e.g
```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks.
```
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
```
Strings can be concatenated (glued together) with the + operator, and repeated with *
```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
Note: Does not work for variables or expressions. If you want to concatenate variables or a variable and a literal, use +
```
>>> text = ('Put several strings within parentheses '
        'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

>>>prefix + 'thon'
'Python'
```
#### Indexing and slicing
```
word = 'Python'
word[0]  # character in position 0
'P'
word[-1]  # character in position 5/Last character
'n'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'

```
One way to remember how slices work is to think of the indices as pointing between characters. 

![slicing](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/4054aa62-9f33-4e85-9ebc-bc514fb6a3f6)

The slice from i to j consists of all characters between the edges labeled i and j, respectively e.g [1:3] is y and t.

#### String Interpolation and Formatting
a. modulo operator
```
# one element
>>> name = "Jane"
>>> "Hello, %s!" % name
'Hello, Jane!'

# using a tuple
>>> age = 25
>>> "Hello, %s! You're %s years old." % (name, age)
'Hello, Jane! You're 25 years old.'

#using a dictionary
"Hello, %(name)s! You're %(age)s years old." % {"name": "Jane", "age": 25}
"Hello, Jane! You're 25 years old."

# format specifiers
>>> "Balance: $%.2f" % 5425.9292
'Balance: $5425.93'
>>> print("Name: %s\nAge: %5s" % ("John", 35))
Name: John
Age:    35
```
b. The str.format() Method
```
# empty brackets
>>> name = "Jane"
>>> age = 25
>>> "Hello, {}! You're {} years old.".format(name, age)
"Hello, Jane! You're 25 years old."

# using zero-based indices to specify interpolation order
>>> "Hello, {1}! You're {0} years old.".format(age, name)
"Hello, Jane! You're 25 years old."

#use keyword arguments in the call to the method and enclose the argument names in your replacement fields
>>> "Hello, {name}! You're {age} years old.".format(name="Jane", age=25)
"Hello, Jane! You're 25 years old."

# use dictionaries then dictionary unpacking operator (**) to provide the arguments to .format().
>>> person = {"name": "Jane", "age": 25}
>>> "Hello, {name}! You're {age} years old.".format(**person)
"Hello, Jane! You're 25 years old."

# format specifiers
>>> "Balance: ${:.2f}".format(5425.9292)
'Balance: $5425.93'
>>> "{:=^30}".format("Centered string")
'=======Centered string========'
```

c. F-strings
```
>>> name = "Jane"
>>> age = 25
>>> f"Hello, {name}! You're {age} years old."
'Hello, Jane! You're 25 years old.'

#embedding functions, list comprehensions with f strings.
>>> f"Hello, {name.upper()}! You're {age} years old."
"Hello, JANE! You're 25 years old."

>>> f"{[2**n for n in range(3, 9)]}"
'[8, 16, 32, 64, 128, 256]'

#format specifiers
>>> balance = 5425.9292
>>> f"Balance: ${balance:.2f}"
'Balance: $5425.93'

>>> heading = "Centered string"
>>> f"{heading:=^30}"
'=======Centered string========'

>>> integer = -1234567
>>> f"Comma as thousand separators: {integer:,}"
'Comma as thousand separators: -1,234,567'

>>> sep = "_"
>>> f"User's thousand separators: {integer:{sep}}"
'User's thousand separators: -1_234_567'

>>> floating_point = 1234567.9876
>>> f"Comma as thousand separators and two decimals: {floating_point:,.2f}"
'Comma as thousand separators and two decimals: 1,234,567.99'

>>> date = (9, 6, 2023)
>>> f"Date: {date[0]:02}-{date[1]:02}-{date[2]}"
'Date: 09-06-2023'

>>> from datetime import datetime
>>> date = datetime(2023, 9, 26)
>>> f"Date: {date:%m/%d/%Y}"
'Date: 09/26/2023'
```

#### Pycodestyle
```
$ pip install pycodestyle
$ pip install --upgrade pycodestyle
$ pip uninstall pycodestyle
```
Example usage: ```$ pycodestyle --first optparse.py```

Source code for each error: ```$ pycodestyle --show-source --show-pep8 testing/data/E40.py```

Error occurrence: ```$ pycodestyle --statistics -qq Python-2.5/Lib```

## Tasks
**Task 0:**  [0-run](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x00-python-hello_world/0-run)

Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE

![0](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/fef1da64-bc55-4a0b-bedf-4e0605145d5d)

**Task 1:**  [1-run_inline](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x00-python-hello_world/1-run_inline)

Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE

![1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/09fcb375-d896-43e3-9fd3-e5059368b212)

**Task 2:**  [2-print.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x00-python-hello_world/2-print.py)

Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
Use print.

![2](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/e5914c6e-b786-4131-9ef1-40d69b0c014f)

**Task 3:**  []()
Complete this source code:
```
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```
The output of the script should be: the number, followed by Battery street, followed by a new line.

You are not allowed to cast the variable number into a string. Your code must be 3 lines long.

You have to use [f-strings tips](https://realpython.com/python-f-strings/).

![3](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/e32dedad-bc05-47b0-b343-e53881b313d6)

