# 0x06. Python - Classes and Objects

Continuation of Python that looks at: Classes, methods, class variables, instance variables, methods, __init__, self, encapsulation and its methods: getters and setters, pythonic way of dealing with private attributes which includes @property and @<function_name>.setter, special operators e.g __add__, __sub__ etc.

## Resources
1. [Object Oriented Programming](https://python.swaroopch.com/oop.html)
2. [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
3. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
4. [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
5. [Python Classes and Objects || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=apACNr7DC_s)
6. [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Summary
We create a new class by:

a. Using the class statement and the name of the class. 

b. This is followed by an indented block of statements that form the body of the class.
```
class Person:
    pass  # An empty block

p = Person()    # create an object/instance
print(p)
```
**Methods**

Objects can have functionality using functions belonging to classes- methods. Methods are like normal functions but take self/the object itself as the first argument.
```
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
```
**The __init__ method**

Run as soon as object is created. It is useful for passing initial values to your object.
```
class Person:
    def __init__(self, name):      #define the __init__ method as taking a parameter name and self
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
```
**Object and class variables**

Objects and classes have variables- instance variables and class variables respectively.
```
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0               # population belongs to the Robot class and hence is a class variable.

    def __init__(self, name):
        """Initializes the data."""
        self.name = name         # name variable belongs to the object (it is assigned using self) and hence is an object variable
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1    # we refer to the population class variable as Robot.population and not as self.population

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1    # Instead of Robot.population, we could have also used self.__class__.population

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    '''how_many is actually a method that belongs to the class and not to the object

    we can define it as either a classmethod or a staticmethod decorator'''

    '''Decorators can be imagined to be a shortcut to calling a wrapper function

    (i.e. a function that "wraps" around another function so that it can do something before or after the inner function)'''
    @classmethod
    def how_many(cls):              
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```
**Encapsulation**

Bundling of data with the methods that operate on that data. 

The methods are getter methods for retrieving data and setter methods for changing the data.
```
class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name    
    def set_build_year(self, by):
        self.__build_year = by
    def get_build_year(self):
        return self.__build_year    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
```
**Properties**

Unfortunately, it is widespread belief that a proper Python class should encapsulate private attributes by using getters and setters. As soon as one of these programmers introduces a new attribute, he or she will make it a private variable and creates "automatically" a getter and a setter for this attribute. However, the Pythonic way to introduce attributes is to make them public.

The solution to encapsulation to public attributes is properties:
```
class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
```

**Destructor**

The method __del__. It is called when the instance is about to be destroyed and if there is no other reference to this instance.
```
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print ("Robot has been destroyed")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
```
## Tasks
