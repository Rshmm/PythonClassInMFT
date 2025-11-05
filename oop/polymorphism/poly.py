class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Animal(), Dog(), Cat()]
for a in animals:
    print(a)
    a.sound()
