# view.py
from mvc_online_shop.controller import add_product_controller, show_all_products_controller, remove_product_controller,edit_product_controller

def show_all_products():
    products = show_all_products_controller()
    if not products:
        print("No product found")
    else:
        for product in products:
            print(
                f'name : {product["name"]}, brand : {product["brand"]}, category : {product["category"]}, count : {product["count"]}')


def menu():
    return "1-Add product\n2-Show all products\n3-Remove product\n4-Edit product"

def star():
    print("*" * 50)

while True:

    print(menu())
    star()
    choice = int(input("Enter your choice : "))
    star()

    match choice:
        case 1:
            categories = ["phone", "laptop", "ipad"]

            name = input("Enter your product name : ")
            brand = input("Enter your product brand : ")

            print("Available categories:")
            for c in categories:
                print(c)
            category = input("Choose your category from the list: ")

            count = int(input("Enter your product count: "))


            status, message = add_product_controller(name, brand, category, count)


            print(message)

        case 2:
            show_all_products()


        case 3:
                show_all_products()
                name = input("Enter product name that you wants to remove: ")
                count = int(input("Enter product count : "))

                status, msg = remove_product_controller(name, count)

                print(msg)

        case 4:
            name = input("Enter your product name : ")
            new_name = input("Enter your product new name : ")
            brand = input("Enter your product new brand : ")
            count = int(input("Enter your product new count: "))

            status, msg = edit_product_controller(name, new_name, brand, count)

            print(msg)