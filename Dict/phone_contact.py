contacts = {}

while True:


    print("1-Add contact")
    print("2-Remove contact")
    print("3-Edit contact")
    print("4-Show all contact")
    print("0-EXIT")

    choice = input("Enter your choice : ")

    match choice:

        # add contact
        case "1":
            code = input("Enter contacts code : ")
            if any(code == contact for contact in contacts.keys()):
                print("code already exits")
            else:
                name = input("Enter contacts name : ")
                phone = input("Enter contacts phone  :")
                contacts[code] = {"code" : code, "name" : name,"phone" : phone}
                print("contact added successfully")

        # Remove contact
        case "2":
            if contacts:
                for contact in contacts.values():
                    print(f"code : {contact['code']} | name : {contact['name']} | phone : {contact['phone']}")
            else:
                print("no contact found")

            code = input("Enter contacts code : ")
            found = False
            for contact in contacts.keys():
                if code == contact:
                    found = True
                    contacts.pop(contact)
                    print("contact edited successfully")
                    break

            if not found:
                print("no code found")

        # edit contact
        case "3":
            if contacts:
                for contact in contacts.values():
                    print(f"code : {contact['code']} | name : {contact['name']} | phone : {contact['phone']}")
            else:
                print("no contact found")

            code = input("Enter contacts code : ")
            found = False
            for contact in contacts.values():
                if code == contact['code']:
                    found = True
                    new_name = input("Enter new name :")
                    new_phone = input("Enter new phone :")
                    contact['name'] = new_name
                    contact['phone'] = new_phone
                    print("contact edited successfully")
                    break

            if not found:
                print("no code found")

        # show all contacts
        case "4":
            if contacts:
                for contact in contacts.values():
                    print(f"code : {contact['code']} | name : {contact['name']} | phone : {contact['phone']}")
            else:
                print("no contact found")

        case "0":
            exit()

        case _:
            pass