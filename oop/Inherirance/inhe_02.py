class Employee:

    employees = []
    def __init__(self, name, emp_id, role="Employee"):
        self.name = name
        self.emp_id = emp_id
        Employee.employees.append({"name" : name, "emp_id" : emp_id, "role":role})

    def show_info(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name, emp_id,role="Manager")
        self.department = department

    def manage(self):
        print(f"{self.name} manages {self.department} department.")


class Director(Manager):
    def __init__(self, name, emp_id, department, budget):
        super().__init__(name, emp_id,department)
        self.role = "Director"
        self.budget = budget

    def approve_budget(self):
        print(f"{self.name} approved a budget of {self.budget}$ for {self.department}.")

e1 = Employee("Ali", 101)
m1 = Manager("Sara", 102, "IT")
d1 = Director("Reza", 103, "Finance", 500000)

for emp in Employee.employees:
    print(emp)

