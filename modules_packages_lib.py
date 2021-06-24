# Python's extensive documentation on docs.python.org
# We have used functions that we created as well as builtin

# import is the keyword that is used to import any module available in python.org
# Let's see that in action
# math
import math #to calculate values
#import random #to generate random number
from random import random # same as 'import random', but can avoid using 'random.random'
num1 = 23.44 # float

# in real life scenario, you have to round the figure depending on the value
# if the decimal value is less than .50 round it down and if more than or equal to 0.50 then round up
print(round(num1))
print(math.ceil(num1)) #regardless of decimal value rounds to higher
print(math.floor(num1)) #regardless of decimal value rounds to floor
print(math.pi)

# Random class/methods
#print(random.random()) # generates random number everytime the program is executed between 0.0 to 0.99 => we use when we import random

print(random()) #as we imported random from random