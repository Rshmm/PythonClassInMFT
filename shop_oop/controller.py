from model import ProductModel
import re

class ProductController:
    def add_product(self, name, brand, price):
        name, brand, price = name.strip(), brand.strip(), price.strip()

        if not re.fullmatch(r"[A-Za-z0-9\s]{2,32}", name):
            return False, f"Invalid name: {name}"
        if not re.fullmatch(r"[A-Za-z0-9\s]{2,32}", brand):
            return False, f"Invalid brand: {brand}"

        try:
            price = int(price)
            if price <= 0:
                return False, "Price must be positive"
        except:
            return False, "Price must be a number"

        # ساخت شیء محصول
        product = ProductModel(name=name, brand=brand, price=price)
        product.save()
        return True, f"Product '{name}' added successfully"

    def edit_product(self, code, name, brand, price):
        try:
            code = int(code)
        except:
            return False, "Invalid code"

        product = ProductModel(code=code, name=name, brand=brand, price=price)
        if not product.update():
            return False, f"No product found with code {code}"
        return True, f"Product {code} updated successfully"

    def remove_product(self, code):
        try:
            code = int(code)
        except:
            return False, "Invalid code"

        product = ProductModel(code=code)
        if not product.delete():
            return False, f"No product found with code {code}"
        return True, f"Product {code} deleted successfully"
