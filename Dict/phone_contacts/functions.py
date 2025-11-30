contacts = []


def menu():
    print("1-Add contact")
    print("2-Remove contact")
    print("3-Edit contact")
    print("4-Show contact")
    print("0-Exit")


def add_contact(code,name,phone):
    for contact in contacts:
        if contact["code"] == code:
            return f"{code} already used"
    return contacts.append({"code" : code, "name" : name, "phone" : phone})



def remove_contact(code):
    for contact in contacts:
        if contact["code"] == code:
            contacts.remove(contact)
            return "contact removed successfully"

    else:
        print("code not found")


def edit_contact(code,new_name,new_phone):
    for contact in contacts:
        if contact["code"] == code:
            contact["name"] = new_name
            contact["phone"] = new_phone
        return "contact edited successfully"
    else:
        print("code not found")



def show_contacts():
    if contacts:
        for contact in contacts:
            print(f"code : {contact['code']} , name : {contact['name']} , phone : {contact['phone']}")
    else:
        print("there is no contacts")