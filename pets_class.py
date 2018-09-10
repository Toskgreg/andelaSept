class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

class Dog:
    family = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def eat(self):
        self.is_hungry = False

my_doggies = []
my_doggies.append(Dog("Tom", 6))
my_doggies.append(Dog("Fletcher", 7))
my_doggies.append(Dog("Larry", 9))

all_pets = Pets(my_doggies)

# Output
print("I have {} dogs.".format(len(all_pets.dogs)))
for dog in all_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.family))

for dog in all_pets.dogs:
    if dog.is_hungry:
        dog.eat()
        print("My dogs are not hungry.")

