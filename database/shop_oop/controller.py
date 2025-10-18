import re
from model import ProductModel


class ProductController:

    @staticmethod
    def add_product(name,brand,price):
        name = name.strip()
        brand = brand.strip()
        price = price.strip()


        if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", name):
            return False, f"{name}, only use letters and digits and space"

        if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", brand):
            return False, f"{brand}, only use letters and digits and space"


        try:
            price = int(price)
            if price < 0:
                return False, f"{price}, only use positive number"
        except(ValueError, TypeError):
            return False, f"{price}, only use digit"


        ProductModel(name,brand,price)
        return True, f"name : {name}, brand : {brand}, price : {price},product added successfully"


    @staticmethod
    def edit_product(code,new_name,new_brand,new_price):
            code = code.strip()
            name = new_name.strip()
            brand = new_brand.strip()
            price = new_price.strip()

            if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", new_name):
                return False, f"{new_name}, only use letters and digits and space"

            if not re.fullmatch("[a-zA-Z0-9\s]{2,32}", new_brand):
                return False, f"{new_brand}, only use letters and digits and space"

            try:
                new_price = int(new_price)
                if new_price < 0:
                    return False, f"{new_price}, only use positive number"
            except(ValueError, TypeError):
                return False, f"{new_price}, only use digit"

            try:
                code = int(code)
                if code < 0:
                    return False, f"{code}, only use positive number"
            except(ValueError, TypeError):
                return False, f"{code}, only use digit"


            ProductModel.edit_products(code, new_name, new_brand, new_price)
            return True, f"code : {code} ,name : {name}, brand : {brand}, price : {price},product edit successfully"


    @staticmethod
    def remove_product(code):

        code = code.strip()

        try:
            code = int(code)
            if code < 0:
                return False, f"{code}, only use positive number"
        except(ValueError, TypeError):
            return False, f"{code}, only use digit"

        ProductModel.remove_product(code)
        return True, f"product remove successfully"


