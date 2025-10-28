class Dog:

    species = "German"

    def __init__(self, name):
        self.name = name


d1 = Dog("Lucky")
d2 = Dog("Rocky")

# Dog.species = "schizo"
d1.species = "wolf"


print(d1.species)
print(d2.species)
print(Dog.species)