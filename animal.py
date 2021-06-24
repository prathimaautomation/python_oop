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