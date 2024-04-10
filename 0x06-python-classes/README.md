# 0x06. Python - Classes and Objects

Continuation of Python.

## Resources
1. [Object Oriented Programming](https://python.swaroopch.com/oop.html)
2. [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
3. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
4. [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
5. [Python Classes and Objects || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=apACNr7DC_s)
6. [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Summary
We create a new class by:

a. using the class statement and the name of the class. 

b. This is followed by an indented block of statements which form the body of the class.
```
class Person:
    pass  # An empty block

p = Person()    # create an object/instance
print(p)
```
Objects and classes have variables- instance variables and class variables respectively.

Objects can have functionality using functions belonging to classes- methods. Methods are like normal functions but they take self/the object itself as an argument.
```
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
```
The __init__ method has special significance to Python. Run as soon as object is created. It is useful for passing initial values to your object.
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
Object and class variables
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
## Tasks
