employees = {
    "E01" : {"name" : "Ali", "department" : "IT", "salary" : 1000},
    "E02" : {"name" : "Reza", "department" : "Finance", "salary" : 1300},
    "E03" : {"name" : "Maryam", "department" : "IT", "salary" : 1500},
    "E04" : {"name" : "Neda", "department" : "HR", "salary" : 1000},
    "E05" : {"name" : "Arsham", "department" : "HR", "salary" : 1600},
}

dept_salary = {}

for emp in employees.values():
    dept = emp['department']
    salary = emp['salary']
    dept_salary[dept] = dept_salary.get(dept, 0) + salary

print(dept_salary)