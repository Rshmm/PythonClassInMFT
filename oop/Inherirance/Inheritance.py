class Parent:
    def show_parent(self):
        print("This is the parent class.")

class Child(Parent):
    def show_child(self):
        print("This is the child class.")


obj = Child()
obj.show_parent()
obj.show_child()