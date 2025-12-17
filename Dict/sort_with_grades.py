students = [
    {"name" : "Ali", "grade" : "A"},
    {"name" : "Sara", "grade" : "B"},
    {"name" : "Reza", "grade" : "A"},
    {"name" : "Neda", "grade" : "C"},
    {"name" : "Maryam", "grade" : "B"}
]

grades = {}

for student in students:
    name = student['name']
    grade = student['grade']
    grades.setdefault(grade,[]).append(name)


print(grades)