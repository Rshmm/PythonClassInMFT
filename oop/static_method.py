class MyClass:

    @staticmethod
    def greet():
        print("Hello ! this is a static method")


MyClass.greet()



class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade


    @staticmethod
    def is_passing(grade):
        return  grade >= 10


s1= Student("Ali", 15)
s2= Student("Sara", 8)

print(Student.is_passing(s1.grade))
print(Student.is_passing(s2.grade))
print(Student.is_passing(16))