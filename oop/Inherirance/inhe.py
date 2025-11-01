class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email


    def login(self):
        print(f"{self.name} logged in")


class Teacher(User):

    def __init__(self,name,email,subject):
        super().__init__(name,email)
        self.subject = subject

    def teach(self):
        print(f"{self.name}, teach {self.subject}")


user1 = ("Ali","ali@gamil.com")