import mysql.connector

class ProductModel:
    # get product info
    def __init__(self, name=None, brand=None, price=None):
        self.name = name
        self.brand = brand
        self.price = price

    # connect
    def _connect(self):
        return mysql.connector.connect(
            host="localhost",
            database="store",
            user="root",
            password="root123",
        )

    # --- CRUD Methods ---

    # add product
    def save(self):
        # connect
        db = self._connect()
        # operation
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO products (name, brand, price) VALUES (%s, %s, %s)",
            [self.name, self.brand, self.price]
        )
        db.commit()
        # disconnect
        cursor.close()
        db.close()

    # edit
    def update(self):
        # connect
        db = self._connect()
        # operation
        cursor = db.cursor()
        cursor.execute(
            "UPDATE products SET name=%s, brand=%s, price=%s WHERE code=%s",
            [self.name, self.brand, self.price, self.code]
        )
        db.commit()
        affected = cursor.rowcount
        # disconnect
        cursor.close()
        db.close()
        return affected > 0  # True یعنی محصولی واقعاً ویرایش شده

    # remove
    def delete(self):
        # connect
        db = self._connect()
        # operation
        cursor = db.cursor()
        cursor.execute("DELETE FROM products WHERE code=%s", [self.code])
        db.commit()
        affected = cursor.rowcount
        # disconnect
        cursor.close()
        db.close()
        return affected > 0

    