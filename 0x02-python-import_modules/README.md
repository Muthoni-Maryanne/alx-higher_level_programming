# 0x02. Python - import & modules

This is a continuation of Python that looks at import and modules.

## Resources
1. [Modules](https://docs.python.org/3/tutorial/modules.html)
2. [Command Line Arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
   
## Summary
#### Modules
A module is a file containing Python definitions and statements. Definitions from a module can be imported into other modules or into the main module. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. Example:
```
# create a file called fibo.py
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
Import the module ```import fibo```

This does not add the names of the functions defined in fibo directly to the current namespace- where variables are stored(could be local, global, and built-in- it only adds the module name fibo there. To access the functions:
```
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

# can assign a local name for ease
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Modules can import other modules, place all import statements at the beginning of a module (or script). 

There is a variant of the import statement that imports names from a module directly into the importing module’s namespace. For example:
```
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
This does not introduce the module name from which the imports are taken in the local namespace (so in the example, fibo is not defined).

If the module name is followed by as, then the name following as is bound directly to the imported module. This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.
```
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Modules can be executed as scripts with ```python fibo.py <arguments>```. Code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". One just needs to add this code at the end of fibo.py:
```
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
then run:
```
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

**“Compiled” Python files:** To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc e.g __pycache__/spam.cpython-33.pyc. The module compileall can create .pyc files for all modules in a directory.

#### Standard modules
Some modules are built into the interpreter either for efficiency or to provide access to operating system primitives such as system calls. Example: sys
 ```
# sys.ps1 and sys.ps2 define the strings used as primary and secondary prompts
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
#### dir()
The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings. Example:
```
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```
Without arguments, dir() lists the names you have defined currently:
```
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module builtins:
```
import builtins
dir(builtins)
```
#### Packages
A collection of modules 

Example of possible structure for an example of a package:

![Screenshot 2024-04-11 204807](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/6dc45d22-e67e-40d8-8247-207c216e4784)

Users of the package can import individual modules from the package, for example: ```import sound.effects.echo```

This loads the submodule sound.effects.echo. It must be referenced with its full name.: ```sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)```

An alternative way of importing the submodule is: ```from sound.effects import echo```

This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows: ```echo.echofilter(input, output, delay=0.7, atten=4)```

Another variation is to import the desired function or variable directly: ```from sound.effects.echo import echofilter```

this loads the submodule echo, but this makes its function echofilter() directly available: ```echofilter(input, output, delay=0.7, atten=4)```

**Note:** When using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

## Tasks

**Task 0:**   [0-add.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/0-add.py)

Program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
![0](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/b063acc5-7496-464e-ac2f-13d58e45f5c1)

**Task 1:**   [1-calculation.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py)

Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
![1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/c6ffe70f-0bf8-4096-aa4e-9fcc53fa9a13)

**Task 2:**   [2-args.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/2-args.py)

Write a program that prints the number of and the list of its arguments.
![2](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/7ce93277-04ae-478c-b0e7-af5dc14a8394)

**Task 3:**   [3-infinite_add.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/3-infinite_add.py)

Write a program that prints the result of the addition of all arguments
![3](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/f7f7b874-befa-4b00-93e2-46d5cb7df731)

**Task 4:**   [4-hidden_discovery.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/4-hidden_discovery.py)

Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
![4](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/f584e1bd-eb28-44f7-bbfe-e3604a0c691b)

**Task 5:**   [5-variable_load.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/5-variable_load.py)

Write a program that imports the variable a from the file variable_load_5.py and prints its value.
![5](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/26e2720c-a56d-4a0b-9dd7-32f4ca6a6cf0)

**Task 6:**   [100-my_calculator.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/100-my_calculator.py)

Write a program that imports all functions from the file calculator_1.py and handles basic operations.
![6](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/a213a256-f909-4411-a8d8-14cbf794e323)

**Task 7:**   [101-easy_print.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/101-easy_print.py)

Write a program that prints #pythoniscool, followed by a new line, in the standard output.
![7](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/fdef8897-8492-449f-a7e5-e04ec42745ef)

**Task 8:**   []()

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
Resource- [Python bytecode](https://docs.python.org/3.4/library/dis.html)

**Task 9:**   [103-fast_alphabet.py](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/blob/main/0x02-python-import_modules/103-fast_alphabet.py)

Write a program that prints the alphabet in uppercase, followed by a new line.
![9](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/793b475f-66fa-4a07-bbd8-521ffb59b271)


