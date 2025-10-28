from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self,name,family,age,national_code):
        self.name = name
        self.family = family
        self.age = age
        self.national_code = national_code


    @abstractmethod
    def get_support(self):
        pass


    def __repr__(self):
        return self.name + ' ' + self.family


class Passenger(Person):

    def get_support(self):
        print(f"{self} need support from Passenger section")

    def get_taxi(self,origin,destination):
        print(f"{self} need a taxi from {origin} to {destination}")

class Driver(Person):

    def __init__(self,name,family,age,national_code,is_online=False):
        super().__init__(name,family,age,national_code)
        self.is_online = is_online

    def get_support(self):
        print(f"{self} need support from Driver section")

    def get_trip(self):
        if self.is_online:
                print(f"{self} accept the trip")
        else:
            print("no driver available")

class Car: 
    pass

class Support(Person):
    def get_support(self):
        print(f"{self} need support from Support section")



# p = Person("arhsam", "hajeb", 22, 12345)
p1 = Passenger("artin", "zamani", 22, 12345)
p1.get_taxi("azadi st", "kaj sq")
d1 = Driver("ahoora", "hajeb", 22, 12345)
d1.is_online = True
d1.get_trip()
s1 = Support("armita", "hajeb", 22, 12345)

# s1.get_support()
# p1.get_support()
# d1.get_support()