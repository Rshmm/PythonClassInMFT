class Employee:
    company_name = "TechCo"
    total_employee = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.total_employee += 1


    def show_info(self):
        print(f"{self.name} works at {Employee.company_name} and earns ${self.salary}")


e1 = Employee("Arsham", 5000)
e2 = Employee("Nima", 4500)

e1.show_info()
e2.show_info()
print("total employee : ", Employee.total_employee)