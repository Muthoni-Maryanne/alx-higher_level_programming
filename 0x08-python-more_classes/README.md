# 0x08. Python - More Classes and Objects

Continuation of OOP that looks at class attributes, instance attributes, properties, getters, setters, encapsulation, class methods, static methods, \_\_str\_\_ and \_\_repr\_\_.

## Resources
1. [Object Oriented Programming](https://python.swaroopch.com/oop.html)
2. [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
3. [Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
4. [Python OOP Tutorial 3: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
5. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
6. [Python's str() vs. repr()](https://shipit.dev/posts/python-str-vs-repr.html)

## Summary
A simple example that shows class and instance attributes:
```
>>>  class A:
>>>     a = "I am a class attribute!"

>>> x = A()
>>> y = A()
>>> x.a
'I am a class attribute!'
>>> y.a
'I am a class attribute!'
>>> A.a
'I am a class attribute!'
>>> x.a = "This creates a new instance attribute for x!"
>>> y.a
'I am a class attribute!'
>>> A.a
'I am a class attribute!'
>>> A.a = "This is changing the class attribute 'a'!"
>>> A.a
"This is changing the class attribute 'a'!"
>>> y.a
"This is changing the class attribute 'a'!"
>>> x.a
'This creates a new instance attribute for x!'
```
Python's class attributes and object attributes are stored in separate dictionaries.

\_\_dict__ shows the internal workings of previous examples:
```
>>> x.__dict__
{'a': 'This creates a new instance attribute for x!'}
>>> y.__dict__
{}
>>> A.__dict__
mappingproxy({'__module__': '__main__',
              'a': "This is changing the class attribute 'a'!",
              '__dict__': <attribute '__dict__' of 'A' objects>,
              '__weakref__': <attribute '__weakref__' of 'A' objects>,
              '__doc__': None})
>>> x.__class__.__dict__
mappingproxy({'__module__': '__main__',
              'a': "This is changing the class attribute 'a'!",
              '__dict__': <attribute '__dict__' of 'A' objects>,
              '__weakref__': <attribute '__weakref__' of 'A' objects>,
              '__doc__': None})
```             
**Class attributes:** 

Class attributes are attributes that are owned by the class itself. They are shared by all the instances of the class. We define class attributes outside all the methods, usually, they are placed at the top, right below the class header. Example:
```
class C: 

    counter = 0
    
    def __init__(self): 
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
```
**Static methods:**  

In the example above, a public class attribute was used. We can make it private as well but we need a possibility to access and change these private class attributes. This is where static methods come in. Static methods do not need a reference to an instance or class. With them can use Robot.RobotInstances() or x.RobotInstances() to access the __counter attribute. Since it is private can not use the previous dot notation, C.counter.
```
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @staticmethod
    def RobotInstances():
        return Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```
**Class methods:**   

Class methods take class, cls, as the first parameter. They can be called via an instance or the class name. Example:
```
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```
## Tasks
