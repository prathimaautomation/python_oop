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