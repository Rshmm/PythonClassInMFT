# کلاس مربوط به اطلاعات کارمندان (سیستم HR)
class HumanResource:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_info(self):
        print(f"Employee: {self.name}, Department: {self.department}")


# کلاس مربوط به حقوق و دستمزد (سیستم Payroll)
class PayrollSystem:
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_payment(self, hours_worked):
        return self.hourly_rate * hours_worked


# کلاس ترکیبی (Multiple Inheritance)
class FreelancerEmployee(HumanResource, PayrollSystem):
    def __init__(self, name, department, hourly_rate, project):
        # باید سازنده‌های هر دو کلاس والد را صدا بزنیم
        HumanResource.__init__(self, name, department)
        PayrollSystem.__init__(self, hourly_rate)
        self.project = project

    def project_info(self):
        print(f"{self.name} is working on project: {self.project}")

    def pay(self, hours):
        payment = self.calculate_payment(hours)
        print(f"{self.name} earned ${payment} for {hours} hours.")


# تست برنامه
emp = FreelancerEmployee("Arsham", "AI Department", 50, "Chatbot Development")

emp.show_info()
emp.project_info()
emp.pay(30)



