# model.py

students = []  # دیتابیس ساده (لیست)

def add_student(name, age):
    student = {"name": name, "age": age}
    students.append(student)

def get_all_students():
    return students
