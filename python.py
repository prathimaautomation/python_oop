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

