# # Python's extensive documentation on docs.python.org
# # We have used functions that we created as well as builtin
#
# # import is the keyword that is used to import any module available in python.org
# # Let's see that in action
# # math
# import math #to calculate values
# #import random #to generate random number
# from random import random # same as 'import random', but can avoid using 'random.random'
# num1 = 23.44 # float
#
# # in real life scenario, you have to round the figure depending on the value
# # if the decimal value is less than .50 round it down and if more than or equal to 0.50 then round up
# print(round(num1))
# print(math.ceil(num1)) #regardless of decimal value rounds to higher
# print(math.floor(num1)) #regardless of decimal value rounds to floor
# print(math.pi)
#
# # Random class/methods
# #print(random.random()) # generates random number everytime the program is executed between 0.0 to 0.99 => we use when we import random
#
# print(random()) #as we imported random from random

# #Let's see how can we interact with our machine using python
# import os # os used to get info about your OS
# import math, datetime, sys # sys is used to get system specific information
#
# work_dir = os.getcwd() # getcwd() provides the current location/path
# print(work_dir)
#
# # Linux/Mac
# #print(os.getuid()) # works on linux and mac & AttributeError for Windows
# print(os.cpu_count())
# #print(os.uname()) #works on linux and mac & AttributeError for Windows
# print(os.path)
# print(datetime.date.today()) # today's date
# # type() len()
#
# we can make an API call to any we address using python requests packages
# pip is a package manager in python to install any packages >pip install requests

import requests # requests is a package to interact with an live API -

requests_api = requests.get("https://www.bbc.co.uk")
if requests_api.status_code == 200: # 200 for success - 404 and above for failure
    print(requests_api.headers)
    print(requests_api.content)
    print(type(requests_api.status_code))
    print(type(requests_api.headers))
    print(type(requests_api.content))

