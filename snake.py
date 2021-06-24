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