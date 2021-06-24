# Python OOP
## Four Pillars of OOP
### Functions and good practice of functions
## DRY DOn't Repeat Yourself
# Let's create a function
# Syntax def is used to declare followed by name of the function():
```python```
# First Iteration
```python
def greeting():
    print("Welcome on Board! enjoy your trip.")
    #pass  # pass keyword that allows the interpretor to skip this without errors

greeting() # if we didn't call the function it would execute the code with no error but no outcome
# DRY Don't Repeat Yourself by declaring functions and reusing code
```
```python
# Second Iteration using RETURN statement
def greeting():
    print("Good Morning")
    return "Welcome on board! Enjoy your trip!!"

print(greeting())

# Third Iteration with username as a String as an argument/args
def greeting(name):
    return "Welcome on board " + name


print(greeting("Prathima"))

# Fourth Iteration to prompt the user to enter their name and display the name back to user with greeting message

def greeting(name):
    return "Welcome on board " + name


print(greeting(input("Please give your name: ")))

```
```python
# Let's create a function with multiple args as an int

def add(num1, num2):
    return num1 + num2

print(add(9, 3))

# Code after the return statement doesn't get executed
def multiply(num1, num2):
    print("This functions multiplies 2 numbers ")
    return num1 * num2
    print(" this is the required outcome of 2 numbers ") # this line of code will not be executed as return statement is last line of code that function executes

print(multiply(3, 3))

```

```python
# Python's extensive documentation on docs.python.org
# We have used functions that we created as well as builtin

# import is the keyword that is used to import any module available in python.org
# Let's see that in action
# math
import math #to calculate values
# import random #to generate random number
from random import random # same as 'import random', but can avoid using 'random.random'
num1 = 23.44 # float

# in real life scenario, you have to round the figure depending on the value
# if the decimal value is less than .50 round it down and if more than or equal to 0.50 then round up
print(round(num1))
print(math.ceil(num1)) #regardless of decimal value rounds to higher
print(math.floor(num1)) #regardless of decimal value rounds to floor
print(math.pi)

# Random class/methods
print(random.random()) # generates random number everytime the program is executed between 0.0 to 0.99 => we use when we import random

print(random()) #as we imported random from random
```
```python
#Let's see how can we interact with our machine using python
import os # os used to get info about your OS
import math, datetime, sys # sys is used to get system specific information

work_dir = os.getcwd() # getcwd() provides the current location/path
print(work_dir)

# Linux/Mac
#print(os.getuid()) # works on linux and mac & AttributeError for Windows
print(os.cpu_count())
#print(os.uname()) #works on linux and mac & AttributeError for Windows
print(os.path)
print(datetime.date.today()) # today's date
# type() len()
```
# Let's install requests using pip

import requests # requests is a package to interact with an live API -
- we can make an API call to any we address using python requests packages
- pip is a package manager in python to install any packages >pip install requests
```python
import requests # requests is a package to interact with an live API -

requests_api = requests.get("https://www.bbc.co.uk")
if requests_api.status_code == 200: # 200 for success - 404 and above for failure
    print(requests_api.headers)
    print(requests_api.content)
    print(type(requests_api.status_code))
    print(type(requests_api.headers))
    print(type(requests_api.content))
```

## Four pillars of Object Oriented Programming
- Abstraction 
`showing only required features to the end user or hiding the implementation from the user`

- Inheritance (DRY - Don't Read Yourself)
`It is an OOPs concept where a child class inherits from parent class and reuse the code`

- Encapsulation (Securing)
`It is the process keeping the data secure like setting access controls`

- Polymorphism 
`It is concept of different forms/implementation using the Inheritance to override`


- step one create an Animal.py file to create parent class
- step two to create file called reptile.py to abstract data and inherit from animal.py
- step three is create a file called snake.py and inherit from reptile.py
- step four is to create a file called python.py and this point we should be able to utilise inheritance from multiple classes - everything available from animal class to python
```python
# Let's create an Animal class
class Animal: # follow the correct naming convention
    # we need to initialise with built in method called __init__(self)
    # self refers to current class
    def __init__(self): # we declare attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive! "

    def eat(self):
        return "time to eat "

    def move(self):
        return "move left and rigght to stay awake "

# we need to create an object of this class in order to use any methods
cat = Animal() # creating an object of Animal class
#for cat as a user the functionality inside Animal class and method breathe is abstracted
# print(cat.breathe())
# print(cat.eat())

# Let's move onto our step 2
```
```python
# Let's create reptiple class to inherit Animal class
from animal import Animal #importing Animal class
#absolute path of the class is needed to import
class Reptile(Animal): #inheriting from Animal class
    def __init__(self):
        super().__init__() # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "it's chilly looking have fun in the sun! "

    def hunt(self):
        return "keep working hard to find food "

    def use_venom(self):
        return "If I have it I will use it "

    #Let's create an object of Reptile class
smart_reptile = Reptile()
# print(smart_reptile.breathe()) #breathe method is inherited from Animal class
# print(smart_reptile.hunt()) # hunt() is availalbe in Reptile class
# print(smart_reptile.eat())
# print(smart_reptile.move())
# print(smart_reptile.use_venom())

#Let's move onto step 3
```
```python
# Let's create a class called Snake

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True

# Let's add some specific methods/behaviours

    def use_tongue_to_smell(self):
        return "If I can touch it I can smell it "

# Let's create an object of snake class
smart_snake = Snake()

# print(smart_snake.move()) # move() is available from animal class
# print(smart_snake.hunt()) # hunt() is available from reptile class
# print(smart_snake.use_tongue_to_smell()) # method from this class

# time to move on to our last step
```
```python
# Let's create python class
from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "I can digest anything without chewing "

    def climb(self):
        return "up we go......"

    def __shed_skin(self): # __ dunder for hiding
        return "I'm growing out of my skin now "

#Let's create an object of Python
fast_python = Python()
print(fast_python.breathe()) # from Animal class
print(fast_python.hunt()) # from Reptile class
print(fast_python.use_tongue_to_smell()) # from Snake class
print(fast_python.climb()) # from Python class


```