import mysql.connector

class ProductModel:

    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
        # connect
        db = mysql.connector.connect(
                                    host = "localhost",
                                    database = "store",
                                    user="root",
                                    password="root123",
                                     )


        cursor = db.cursor()

        # operation
        cursor.execute("INSERT INTO store.products (name,brand,price) VALUES (%s,%s,%s)",
                       [name,brand,price])
        db.commit()

        # close
        cursor.close()
        db.close()


    @staticmethod
    def remove_product(code):
        # connect
        db = mysql.connector.connect(
            host="localhost",
            database="store",
            user="root",
            password="root123",
        )

        cursor = db.cursor()

        # operation
        cursor.execute("DELETE FROM store.products WHERE code =  (%s)", [code])
        db.commit()

        # close
        cursor.close()
        db.close()

    @staticmethod
    def edit_products(code,new_name,new_brand,new_price):
        # connect
        db = mysql.connector.connect(
            host="localhost",
            database="store",
            user="root",
            password="root123",
        )

        cursor = db.cursor()

        # operation
        cursor.execute("UPDATE products SET name=%s, brand=%s, price=%s WHERE code=%s", [new_name,new_brand,new_price,code])
        db.commit()

        # close
        cursor.close()
        db.close()



