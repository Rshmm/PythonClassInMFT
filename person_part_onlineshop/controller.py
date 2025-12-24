from model import save_person,remove_person,edit_person,get_all_persons
import re


def save_person_controller(name,lastName,age,city,addres):

    name = name.strip()
    lastName = lastName.strip()
    city = city.strip() 
    addres = addres.strip()
    age = age.strip()

    if not name or not lastName or not city or not addres:
        return False, "All fields are required"
    
    if not re.fullmatch("[A-Za-z\s]{2,30}", name):
        return False, "Name must contain only letters. use apace and for separation and be 2-30 characters long"

    if not re.fullmatch("[A-Za-z\s]{2,30}", lastName):
        return False, "Last Name must contain only letters. use apace  for separation and be 2-30 characters long"

    try:
        age = int(age)
        if age < 0:
            return False, "Age must be a positive number"
    except (ValueError, TypeError):
        return False, "Age must be a number"



    if not re.fullmatch("[A-Za-z0-9\s]{2,30}", city):
        return False, "City must contain only letters and be 2-30 characters long"

         
    if not re.fullmatch("[A-Za-z\s0-9]{2,50}", addres):
        return False, "Address must contain only letters and be 2-30 characters long"

    save_person(name,lastName,age,city,addres)
    return True, "Person saved successfully"


def remove_person_controller(person_code):
    person_code = person_code.strip()

    try:
        person_code = int(person_code)
        if person_code < 0:
            return False, "person_code must be a positive number"
    except (ValueError, TypeError):
        return False, "person_code must be a number"
    
    remove_person(person_code)
    return True, "Person removed successfully"



def edit_person_controller(person_code,name,lastName,age,city,addres):
    person_code = person_code.strip()
    name = name.strip()
    lastName = lastName.strip()
    age = age.strip()
    addres = addres.strip()
    city = city.strip() 

    if not name or not lastName or not city or not addres:
        return False, "All fields are required"

    if not re.fullmatch("[A-Za-z\s]{2,30}", name):
        return False, "Name must contain only letters. use apace and for separation and be 2-30 characters long"

    if not re.fullmatch("[A-Za-z\s]{2,30}", lastName):
        return False, "Last Name must contain only letters. use apace  for separation and be 2-30 characters long"

    try:
        age = int(age)
        if age < 0:
            return False, "Age must be a positive number"
    except (ValueError, TypeError):
        return False, "Age must be a number"

    if not re.fullmatch("[A-Za-z\s0-9]{2,30}", city):
        return False, "City must contain only letters and be 2-30 characters long"

    if not re.fullmatch("[A-Za-z\s0-9]{2,50}", addres):
        return False, "Address must contain only letters and be 2-50 characters long"

    edit_person(person_code,name,lastName,age,city,addres)
    return True, "Person edited successfully"

def get_all_persons_controller():
    return get_all_persons()