infos = []


def add_info(code, name, family, age, national_code):
    for info in infos:
        if code == info['code']:
            return "code already used"
    else:
        infos.append({"code": code, "name": name, "family": family, "age": age, "national_code": national_code})
        return "infos added successfully"


def remove_info(code):
    global found
    for info in infos:
        found = False
        if code == info['code']:
            found = True
            infos.remove(info)
            return "info removed successfully"
    if not found:
        return "code not available"


def edit_info(code, new_name, new_family, new_age, new_national_code):
    global found
    for info in infos:
        found = False
        if code == info['code']:
            found = True
            info['name'] = new_name
            info['family'] = new_family
            info['age'] = new_age
            info['national_code'] = new_national_code
            return "info edited successfully"
    if not found:
        return "code not available"