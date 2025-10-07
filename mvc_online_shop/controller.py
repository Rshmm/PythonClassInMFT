# controller.py
import re
from mvc_online_shop.model import  add_products,show_all_products,remove_product,edit_product

def add_product_controller(name, brand, category, count):
    categories = ["phone", "laptop", "ipad"]

    try:
        # نرمال‌سازی ورودی‌ها
        name = str(name).strip()
        brand = str(brand).strip()
        category = str(category).strip()

        # validate name
        if not re.fullmatch(r"[A-Za-z0-9\+\s]{2,30}", name):
            return False, "Invalid name format (only letters and spaces, 2-30 chars)"

        # validate brand
        if not re.fullmatch(r"[A-Za-z0-9\s]{2,30}", brand):
            return False, "Invalid brand format (letters/numbers/spaces, 2-30 chars)"

        # validate count: قبول عدد یا رشته عددی
        try:
            count_int = int(count)
            if count_int < 0:
                return False, "Count must be non-negative"
        except (TypeError, ValueError):
            return False, "Count must be an integer"

        # validate category (درستی شرط اینجاست)
        if category not in categories:
            return False, f"Invalid category. Choose from: {', '.join(categories)}"

        # همه اوکیه — اینجا می‌تونی save کنی یا فقط برگردونی
        add_products(name, brand, category, count)
        return True, "✅ Product saved successfully"

    except Exception as e:
        return False, f"Unexpected error: {e}"


def show_all_products_controller():
    return show_all_products()


def remove_product_controller(name, count):

    name = str(name).strip()

    if not re.fullmatch(r"[A-Za-z0-9\+\s]{2,30}", name):
        return False, "Invalid name format (only letters and spaces, 2-30 chars)"

    try:
        count_int = int(count)
        if count_int < 0:
            return False, "Count must be non-negative"
    except (TypeError, ValueError):
        return False, "Count must be an integer"

    return True,remove_product(name, count)

def  edit_product_controller(name,new_name , new_brand, new_count):

    name = str(name).strip()
    new_name = str(new_name).strip()
    new_brand = str(new_brand).strip()
    new_count = str(new_count).strip()


    if not re.fullmatch(r"[A-Za-z0-9\+\s]{2,30}", name):
        return False, "Invalid name format (only letters and spaces, 2-30 chars)"


    if not re.fullmatch(r"[A-Za-z0-9\+\s]{2,30}", new_name):
        return False, "Invalid name format (only letters and spaces, 2-30 chars)"

    if not re.fullmatch(r"[A-Za-z0-9\s]{2,30}", new_brand):
        return False, "Invalid brand format (letters/numbers/spaces, 2-30 chars)"

    try:
        count_int = int(new_count)
        if count_int < 0:
            return False, "Count must be non-negative"
    except (TypeError, ValueError):
        return False, "Count must be an integer"

    return True, edit_product(name, new_name , new_brand, new_count)