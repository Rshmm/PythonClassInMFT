import re
from model import add_info,remove_info,edit_info


def add_info_controller(code, name, family, age, national_code):
    code = str(code).strip()
    name = str(name).strip()
    family = str(family).strip()
    age = str(age).strip()
    national_code = str(national_code).strip()

    try:
        code = int(code)
        if code < 0:
            return False, f"{code} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{code} have problem, only use positive digits"

    if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", name):
        return False, f"{name} have problem, use lower and upper case letters, digits and space"

    if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", family):
        return False, f"{family} have problem, use lower and upper case letters, digits and space"

    try:
        age = int(age)
        if age < 0:
            return False, f"{age} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{age} have problem, only use positive digits"

    try:
        national_code = int(national_code)
        if national_code < 0:
            return False, f"{national_code} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{national_code} have problem, only use positive digits"


    result = add_info(code, name, family, age, national_code)

    if result == "code already used":
        return False, result
    else:
        return True, result

def remove_info_controller(code):

    code = str(code).strip()

    try:
        code = int(code)
        if code < 0:
            return False, f"{code} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{code} have problem, only use positive digits"

    result = remove_info(code)

    if result == "code not available":
        return False, result
    else:
        return True, result

def edit_info_controller(code, new_name, new_family, new_age, new_national_code):
    code = str(code).strip()
    new_name = str(new_name).strip()
    new_family = str(new_family).strip()
    new_age = str(new_age).strip()
    new_national_code = str(new_national_code).strip()

    try:
        code = int(code)
        if code < 0:
            return False, f"{code} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{code} have problem, only use positive digits"

    if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", new_name):
        return False, f"{new_name} have problem, use lower and upper case letters, digits and space"

    if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", new_family):
        return False, f"{new_family} have problem, use lower and upper case letters, digits and space"

    try:
        new_age = int(new_age)
        if new_age < 0:
            return False, f"{new_age} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{new_age} have problem, only use positive digits"

    try:
        new_national_code = int(new_national_code)
        if new_national_code < 0:
            return False, f"{new_national_code} have problem, only use positive digits"
    except (TypeError, ValueError):
        return False, f"{new_national_code} have problem, only use positive digits"

    result = edit_info(code, new_name, new_family, new_age, new_national_code)

    if result == "code not available":
        return False, result
    else:
        return True, result
