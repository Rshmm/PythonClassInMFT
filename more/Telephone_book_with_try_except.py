contacts = {}


# ---------------- Menu -----------------
def menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1-Add contact")
    print("2-Show all contacts")
    print("3-Remove contact")
    print("4-Edit contact")
    print("0-Exit")


def star():
    print("-------------------------------")


# --------------- Add contact -----------------
def add_contact(code, name, phone):
    try:
        if not name or not phone or not code:
            raise ValueError("Code, name, or phone cannot be empty!")
    except ValueError as e:
        print("❌ Error:", e)
    else:
        contacts[code] = {"code": code, "name": name, "phone": phone}
        print("Contact added successfully!")


# --------------- Show all contacts -----------------
def show_all_contacts():
    try:
        if not contacts:
            raise LookupError("No contacts found!")
    except LookupError as e:
        print("Error:", e)
    else:
        print("\nAll Contacts:")
        for code, info in contacts.items():
            print(f"Code: {info['code']} | Name: {info['name']} | Phone: {info['phone']}")


# --------------- Remove contact -----------------
def remove_contact():
    try:
        code = input("Enter contact code to remove: ")
        if code not in contacts:
            raise KeyError("Contact does not exist!")
    except KeyError as e:
        print("❌ Error:", e)
    else:
        del contacts[code]
        print("Contact removed successfully!")


# --------------- Edit contact -----------------
def edit_contact():
    try:
        code = input("Enter contact code to edit: ")
        if code not in contacts:
            raise KeyError("Contact does not exist!")
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone: ")
        if not new_name or not new_phone:
            raise ValueError("Name or phone cannot be empty!")
    except (KeyError, ValueError) as e:
        print("❌ Error:", e)
    else:
        contacts[code]["name"] = new_name
        contacts[code]["phone"] = new_phone
        print("Contact edited successfully!")


# ---------------- Main Loop -----------------
while True:
    menu()
    star()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match choice:
        case 1:
            code = input("Enter contact code: ")
            if code in contacts:
                print("Code already used!")
            else:
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                add_contact(code, name, phone)

        case 2:
            show_all_contacts()

        case 3:
            remove_contact()

        case 4:
            edit_contact()

        case 0:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Try again.")

    star()
