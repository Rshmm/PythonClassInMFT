# controller.py
import model_sample

def add_student_controller(name, age):
    # اعتبارسنجی داده‌ها
    if len(name.strip()) < 2:
        return False, "❌ Name too short"
    if not str(age).isdigit():
        return False, "❌ Age must be a number"

    model.add_student(name.strip(), int(age))
    return True, "✅ Student added successfully"

def get_students_controller():
    return model.get_all_students()
