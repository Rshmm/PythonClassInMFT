students = []

while input("Do you want to add new student(y/n) :  ").lower() == "y":
    student = {
        "name" : input("Enter students name : "),
        "family" : input("Enter students family name : ")
    }
    course = {}
    while input("Do want to add new course(y/n) : ").lower() == "y":
        course_name = input("Enter course name : ")
        course_score = input("Enter course score : ")
        course[course_name] = course_score
    student['course'] = course
    students.append(student)

print(students)