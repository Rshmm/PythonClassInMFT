products = []
persons = []
cart = []

while True:
    print("\nMain Menu:")
    print("1- Add Product")
    print("2- Remove Product")
    print("3- Edit Product")
    print("4- Show All Products")
    print("5- Add Person")
    print("6- Remove Person")
    print("7- Edit Person")
    print("8- Show All Persons")
    print("9- Shop")
    print("10- Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":  # Add Product
            code = input("Enter product code: ")
            if any(code in product[0] for product in products):
                print("code already exists")
            else:
                name = input("Enter product name: ")
                brand = input("Enter brand: ")
                price = float(input("Enter price: "))
                if price < 0:
                    print("Price cannot be negative!")
                    continue
                count = int(input("Enter quantity: "))
                if count < 0:
                    print("Quantity cannot be negative!")
                    continue
                products.append([code, name, brand, price, count])
                print("Product added successfully!")

        case "2":  # Remove Product
            code = input("Enter product code to remove: ")
            removed = False
            for product in products:
                if product[0] == code:
                    products.remove(product)
                    removed = True
                    print("Product removed.")
                    break
            if not removed:
                print("Product not found.")

        case "3":  # Edit Product
            code = input("Enter product code to edit: ")
            found = False
            for product in products:
                if product[0] == code:
                    found = True
                    new_name = input(f"Enter new name ({product[1]}): ")
                    if new_name != "":
                        product[1] = new_name
                    new_brand = input(f"Enter new brand ({product[2]}): ")
                    if new_brand != "":
                        product[2] = new_brand
                    new_price = input(f"Enter new price ({product[3]}): ")
                    if new_price != "":
                        new_price = float(new_price)
                        if new_price >= 0:
                            product[3] = new_price
                        else:
                            print("Price cannot be negative!")
                    new_count = input(f"Enter new quantity ({product[4]}): ")
                    if new_count != "":
                        new_count = int(new_count)
                        if new_count >= 0:
                            product[4] = new_count
                        else:
                            print("Quantity cannot be negative!")
                    print("Product updated.")
                    break
            if not found:
                print("Product not found.")

        case "4":  # Show All Products
            if len(products) == 0:
                print("No products available.")
            else:
                print("\nProducts List:")
                for product in products:
                    print(f"Code:{product[0]}, Name:{product[1]}, Brand:{product[2]}, Price:{product[3]}, Qty:{product[4]}")

        case "5":  # Add Person
            code = input("Enter person code: ")
            if any(code == person[0] for person in persons):
                print("Person code already exists!")
                continue
            name = input("Enter name: ")
            national_code = input("Enter national code: ")
            if any(national_code == person[2] for person in persons):
                print("national code already exists")
                continue
            age = int(input("Enter age: "))
            if age < 18:
                print("Age must be 18 or older!")
                continue
            persons.append([code, name, national_code, age])
            print("Person added successfully!")

        case "6":  # Remove Person
            code = input("Enter person code to remove: ")
            removed = False
            for person in persons:
                if person[0] == code:
                    persons.remove(person)
                    removed = True
                    print("Person removed.")
                    break
            if not removed:
                print("Person not found.")

        case "7":  # Edit Person
            code = input("Enter person code to edit: ")
            found = False
            for person in persons:
                if person[0] == code:
                    found = True
                    new_name = input(f"Enter new name ({person[1]}): ")
                    if new_name != "":
                        person[1] = new_name
                    new_national = input(f"Enter new national code ({person[2]}): ")
                    if new_national != "":
                        exists_nc = False
                        for p in persons:
                            if p[2] == new_national and p[0] != code:
                                exists_nc = True
                                break
                        if not exists_nc:
                            person[2] = new_national
                        else:
                            print("National code already exists!")
                    new_age = input(f"Enter new age ({person[3]}): ")
                    if new_age != "":
                        new_age = int(new_age)
                        if new_age >= 18:
                            person[3] = new_age
                        else:
                            print("Age must be 18 or older!")
                    print("Person updated.")
                    break
            if not found:
                print("Person not found.")

        case "8":  # Show All Persons
            if len(persons) == 0:
                print("No persons available.")
            else:
                print("\nPersons List:")
                for p in persons:
                    print(f"Code:{p[0]}, Name:{p[1]}, National:{p[2]}, Age:{p[3]}")

        case "9":  # Shop
            if len(persons) == 0:
                print("No persons available. Please add persons first.")
                continue
            print("\nPersons List:")
            for p in persons:
                print(f"Code:{p[0]}, Name:{p[1]}, National:{p[2]}, Age:{p[3]}")
            buyer_code = input("Enter buyer code: ")
            buyer = ""
            for p in persons:
                if p[0] == buyer_code:
                    buyer = p
                    break
            if buyer == "":
                print("Buyer not found!")
                continue
            while True:
                if len(products) == 0:
                    print("No products available.")
                    break
                print("\nProducts List:")
                for pr in products:
                    print(f"Code:{pr[0]}, Name:{pr[1]}, Brand:{pr[2]}, Price:{pr[3]}, Qty:{pr[4]}")
                prod_code = input("Enter product code to buy: ")
                product = ""
                for pr in products:
                    if pr[0] == prod_code:
                        product = pr
                        break
                if product == "":
                    print("Product not found!")
                    continue
                qty = int(input("Enter quantity to buy: "))
                if qty > product[4]:
                    print("Not enough stock!")
                    continue
                product[4] -= qty
                cart.append([buyer[0], buyer[1], product[0], product[1], qty, qty*product[3]])
                more = input("Do you want to buy another product? (yes/no): ")
                if more.lower() != "yes":
                    break
            if len(cart) == 0:
                print("No items in cart.")
                continue
            print("\nCart Items:")
            for item in cart:
                print(f"Buyer:{item[1]}, Product:{item[3]}, Qty:{item[4]}, Total:{item[5]}")
            attempts = 0
            while attempts < 3:
                nc = input("Enter your national code to confirm purchase: ")
                if nc == buyer[2]:
                    print("Purchase completed successfully!")
                    cart.clear()
                    break
                else:
                    print("Incorrect national code!")
                    attempts += 1
            if attempts == 3:
                print("Purchase canceled.")
                cart.clear()

        case "10":
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please enter a number between 1-10.")
