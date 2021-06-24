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
- math
import math #to calculate values
- import random #to generate random number
from random import random # same as 'import random', but can avoid using 'random.random'
num1 = 23.44 # float

- in real life scenario, you have to round the figure depending on the value
- if the decimal value is less than .50 round it down and if more than or equal to 0.50 then round up
print(round(num1))
print(math.ceil(num1)) #regardless of decimal value rounds to higher
print(math.floor(num1)) #regardless of decimal value rounds to floor
print(math.pi)

- Random class/methods
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