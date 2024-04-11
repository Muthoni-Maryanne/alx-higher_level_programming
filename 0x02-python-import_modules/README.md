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

Users of the package can import individual modules from the package, for example: ```import sound.effects.echo```

This loads the submodule sound.effects.echo. It must be referenced with its full name.: ```sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)```

An alternative way of importing the submodule is: ```from sound.effects import echo```

This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows: ```echo.echofilter(input, output, delay=0.7, atten=4)```

Another variation is to import the desired function or variable directly: ```from sound.effects.echo import echofilter```

this loads the submodule echo, but this makes its function echofilter() directly available: ```echofilter(input, output, delay=0.7, atten=4)```

**Note:** When using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

