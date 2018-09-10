class Pets:
    
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    family = 'mammal'
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return "%s is walking!" % (self.name)

my_doggies = []
my_doggies.append(Dog("Tom"))
my_doggies.append(Dog("Fletcher"))
my_doggies.append(Dog("Larry"))

all_pets = Pets(my_doggies)

# Output
all_pets.walk()

