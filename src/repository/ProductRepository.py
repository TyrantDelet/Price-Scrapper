from ..database.ManageDatabase import ManageDatabase

class ProductRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db


    def add_category(self, id: int, name: str):
        query = "INSERT INTO category (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()

    def get_category(self, id: int, name: str):
        if id is not None and name is not None:
            query = "SELECT * FROM category WHERE id = UPPER(?) and UPPER(name) = UPPER(?)"
        elif id is not None:
            query = "SELECT * FROM category WHERE id = ?"
        elif name is not None:
            query = "SELECT * FROM category WHERE name = ?"
        else:
            raise ValueError("Either 'id' or 'name' must be provided.")
        result = self.db.connection.execute(query, (id or name,))
        self.db.disconnect()
        return result if result else None

    def get_all_categories(self):
        query = "SELECT * FROM category"
        return self.db.fetchall(query)

    def update_category(self, id: int, name: str):
        query = "UPDATE category SET name = ? WHERE id = ?"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_category(self, id: int, name: str):
        query = "DELETE FROM category WHERE id = ? AND name = ?"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()



    def add_product(self, id: int, name: str, category: int):
        query = "INSERT INTO product (id, name, category) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, category))
        self.db.disconnect()

    def get_product(self, id: int, name: str):
        if id is not None and name is not None:
            query = "SELECT * FROM product WHERE id = UPPER(?) and UPPER(name) = UPPER(?)"
        elif id is not None:
            query = "SELECT * FROM product WHERE id = ?"
        elif name is not None:
            query = "SELECT * FROM product WHERE name = ?"
        else:
            raise ValueError("Either 'id' or 'name' must be provided.")
        result = self.db.connection.execute(query, (id or name,))
        self.db.disconnect()
        return result if result else None

    def get_all_products(self):
        query = "SELECT * FROM product"
        return self.db.fetchall(query)

    def update_product(self, id: int, name: str, category: int):
        query = "UPDATE product SET name = ?, category = ? WHERE id = ?"
        self.db.connection.execute(query, (name, category, id))
        self.db.disconnect()

    def delete_product(self, id: int, name: str):
        query = "DELETE FROM product WHERE id = ? AND name = ?"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()



    def add_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        query = "INSERT INTO product_variant (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight))
        self.db.disconnect()

    def get_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        if id is not None:
            query = "SELECT * FROM product_variant WHERE id = ?"
            result = self.db.connection.execute(query, (id,))
        elif product_id is not None:
            query = "SELECT * FROM product_variant WHERE product_id = ?"
            result = self.db.connection.execute(query, (product_id,))
        elif external_id is not None:
            query = "SELECT * FROM product_variant WHERE external_id = ?"
            result = self.db.connection.execute(query, (external_id,))
        elif variant_name is not None:
            query = "SELECT * FROM product_variant WHERE variant_name = ?"
            result = self.db.connection.execute(query, (variant_name,))
        elif model is not None:
            query = "SELECT * FROM product_variant WHERE model = ?"
            result = self.db.connection.execute(query, (model,))
        elif color is not None:
            query = "SELECT * FROM product_variant WHERE color = ?"
            result = self.db.connection.execute(query, (color,))
        elif size_height is not None:
            query = "SELECT * FROM product_variant WHERE size_height = ?"
            result = self.db.connection.execute(query, (size_height,))
        elif size_width is not None:
            query = "SELECT * FROM product_variant WHERE size_width = ?"
            result = self.db.connection.execute(query, (size_width,))
        elif weight is not None:
            query = "SELECT * FROM product_variant WHERE weight = ?"
            result = self.db.connection.execute(query, (weight,))
        else:
            raise ValueError("At least one parameter must be provided.")
        
        self.db.disconnect()
        return result if result else None

    def get_all_product_variants(self):
        query = "SELECT * FROM product_variant"
        return self.db.fetchall(query)

    def update_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        query = "UPDATE product_variant SET product_id = ?, external_id = ?, variant_name = ?, model = ?, color = ?, size_height = ?, size_width = ?, weight = ? WHERE id = ?"
        self.db.connection.execute(query, (product_id, external_id, variant_name, model, color, size_height, size_width, weight, id))
        self.db.disconnect()

    def delete_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        query = "DELETE FROM product_variant WHERE id = ? AND product_id = ? AND external_id = ? AND variant_name = ? AND model = ? AND color = ? AND size_height = ? AND size_width = ? AND weight = ?"
        self.db.connection.execute(query, (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight))
        self.db.disconnect()



    def add_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        query = "INSERT INTO product_price (id, price, price_date, manufacturer, marketplace, product_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, price, price_date, manufacturer, marketplace, product_id))
        self.db.disconnect()

    def get_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        if id is not None:
            query = "SELECT * FROM product_price WHERE id = ?"
            result = self.db.connection.execute(query, (id,))
        elif price is not None:
            query = "SELECT * FROM product_price WHERE price = ?"
            result = self.db.connection.execute(query, (price,))
        elif price_date is not None:
            query = "SELECT * FROM product_price WHERE price_date = ?"
            result = self.db.connection.execute(query, (price_date,))
        elif manufacturer is not None:
            query = "SELECT * FROM product_price WHERE manufacturer = ?"
            result = self.db.connection.execute(query, (manufacturer,))
        elif marketplace is not None:
            query = "SELECT * FROM product_price WHERE marketplace = ?"
            result = self.db.connection.execute(query, (marketplace,))
        elif product_id is not None:
            query = "SELECT * FROM product_price WHERE product_id = ?"
            result = self.db.connection.execute(query, (product_id,))
        else:
            raise ValueError("At least one parameter must be provided.")
        
        self.db.disconnect()
        return result if result else None

    def get_all_product_prices(self):
        query = "SELECT * FROM product_price"
        return self.db.fetchall(query)

    def update_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        query = "UPDATE product_price SET price = ?, price_date = ?, manufacturer = ?, marketplace = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (price, price_date, manufacturer, marketplace, product_id, id))
        self.db.disconnect()

    def delete_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        query = "DELETE FROM product_price WHERE id = ? AND price = ? AND price_date = ? AND manufacturer = ? AND marketplace = ? AND product_id = ?"
        self.db.connection.execute(query, (id, price, price_date, manufacturer, marketplace, product_id))
        self.db.disconnect()

    def get_lowest_product_price(self, product_id: int):
        query = "SELECT * FROM product_price WHERE product_id = ? ORDER BY price_date DESC"
        return self.db.fetchall(query, (product_id,))

    def get_all_product_variants(self, product_id: int):
        query = "SELECT * FROM product_variant WHERE product_id = ?"
        return self.db.fetchall(query, (product_id,))

    def get_product_variant_with_prices(self, product_id: int):
        query = """
            SELECT pv.*, pp.price, pp.price_date
            FROM product_variant pv
            LEFT JOIN product_price pp ON pv.id = pp.product_variant_id
            WHERE pv.product_id = ?
            ORDER BY pp.price_date DESC
        """
        return self.db.fetchall(query, (product_id,))



    def add_product_url(self, id : int, marketplace_id: int, external_product_id: str, product_id: int):
        query = "INSERT INTO product_url (id, marketplace_id, external_product_id, product_id) VALUES (?, ?, ?, ?)"
        self.db.connection.execute(query, (id, marketplace_id, external_product_id, product_id))
        self.db.disconnect()

    def get_product_url(self, id: int, marketplace_id: int, external_product_id: str, product_id: int):
        if id is not None:
            query = "SELECT * FROM product_url WHERE id = ?"
            result = self.db.connection.execute(query, (id,))
        elif marketplace_id is not None:
            query = "SELECT * FROM product_url WHERE marketplace_id = ?"
            result = self.db.connection.execute(query, (marketplace_id,))
        elif external_product_id is not None:
            query = "SELECT * FROM product_url WHERE external_product_id = ?"
            result = self.db.connection.execute(query, (external_product_id,))
        elif product_id is not None:
            query = "SELECT * FROM product_url WHERE product_id = ?"
            result = self.db.connection.execute(query, (product_id,))
        else:
            raise ValueError("At least one parameter must be provided.")
        
        self.db.disconnect()
        return result if result else None

    def get_all_product_urls(self):
        query = "SELECT * FROM product_url"
        return self.db.fetchall(query)

    def update_product_url(self, id: int, marketplace_id: int, external_product_id: str, product_id: int):
        query = "UPDATE product_url SET marketplace_id = ?, external_product_id = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (marketplace_id, external_product_id, product_id, id))
        self.db.disconnect()

    def delete_product_url(self, id: int, marketplace_id: int, external_product_id: str, product_id: int):
        query = "DELETE FROM product_url WHERE id = ? AND marketplace_id = ? AND external_product_id = ? AND product_id = ?"
        self.db.connection.execute(query, (id, marketplace_id, external_product_id, product_id))
        self.db.disconnect()

    


if __name__ == "__main__":
        db = ManageDatabase(db_file_path='./src/database/database.db', schema_file_path='./src/database/schema.sql')
        product_repo = ProductRepository(db)

        product_repo.add_category(1234, "ExampleCategory")
        product_repo.add_product(1234, "ExampleProduct", 1234)
        product_repo.add_product_variant(1234, 1234, "EX1234", "ExampleVariant", "ModelX", "Red", 10.0, 5.0, 1.0)
        product_repo.add_product_price(1234, 99.99, "2023-01-01", 1234, 1234, 1234)
        product_repo.add_product_url(1234, 1234, "EX1234", 1234)


        print("All Products:")
        for product in product_repo.get_all_products():
            print(product)


