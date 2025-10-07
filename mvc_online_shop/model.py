products = []
persons = []
cart = []



def add_products(name,brand,category,count):
    try:
        products.append({"name" : name,"brand": brand,"category": category,"count" : count})
    except Exception as e:
        f"Error : {e}"

def show_all_products():
    try:
        return products
    except Exception as e:
        return f"Error : {e}"

def remove_product(name, count):
    try:
        for product in products:
            if product['name'].lower() == name.lower():

                if count > product["count"]:
                    return f"Cannot remove {count} items — only {product['count']} in stock."

                if count < product["count"]:
                    product["count"] -= count
                    return f"{count} items removed from {name}. Remaining: {product['count']}"
                else:
                    products.remove(product)
                    return f" {name} completely removed from stock."
        return f"product not found"

    except Exception as e:
        return f"Error: {e}"

def edit_product(name,new_name , new_brand, new_count):
    try:
        for product in products:
            if product['name'].lower() == name.lower():
                product['name'] = new_name
                product['brand'] = new_brand
                product['count'] = new_count
                return f"product updated -> name : {product['name']}, brand : {product['brand']}, category : {product['category']}, count : {product['count']} "
        return f"product not found"

    except Exception as e:
        return f"Error: {e}"