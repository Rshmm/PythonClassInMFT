class Person:
    def __init__(self,name,age):
        self.name = name
        # self.__dict__['name'] = name
        self.age = age
        # self.__dict__['age'] = name


p1 = Person(name = "Arsham", age = 22)
p2 = Person("ahoora", 15)
p3 = Person("Armita", 21)
print(p1.name)
print(p1.__dict__['name'])
p1.department = "AI"
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)