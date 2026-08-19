import sqlite3

from ..database.ManageDatabase import ManageDatabase

class ProductRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db
        self.connection = sqlite3.Connection
        self.cursor: sqlite3.Cursor

    def fetchone(self, query, params=None):
            if params is None:
                params = []
            self.cursor.execute(query, params)
            row = self.cursor.fetchone()
            return dict(row) if row else None


    def add_category(self, id: int, name: str):
        query = "INSERT INTO category (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()

    def get_category_by_id(self, id: int):
        query = "SELECT * FROM category WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_category_by_name(self, name: str):
        query = "SELECT * FROM category WHERE name = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result if result else None

    def get_all_categories(self):
        query = "SELECT * FROM category"
        return self.db.fetchone(query)

    def update_category(self, id: int, name: str):
        query = "UPDATE category SET name = UPPER(?) WHERE id = UPPER(?)"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_category_by_id(self, id: int):
        query = "DELETE FROM category WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_category_by_name(self, name: str):
        query = "DELETE FROM category WHERE name = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()



    def add_product(self, id: int, name: str, category: int):
        query = "INSERT INTO product (id, name, category) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, category))
        self.db.disconnect()

    def get_product_by_id(self, id: int):
        query = "SELECT * FROM product WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_by_name(self, name: str):
        query = "SELECT * FROM product WHERE name = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result if result else None

    def get_all_products(self):
        query = "SELECT * FROM product"
        return self.db.fetchone(query)

    def update_product(self, id: int, name: str, category: int):
        query = "UPDATE product SET name = ?, category = ? WHERE id = ?"
        self.db.connection.execute(query, (name, category, id))
        self.db.disconnect()

    def delete_product_by_id(self, id: int):
        query = "DELETE FROM product WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_by_name(self, name: str):
        query = "DELETE FROM product WHERE name = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()



    def add_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        query = "INSERT INTO product_variant (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight))
        self.db.disconnect()

    def get_product_variant_by_id(self, id: int):
        query = "SELECT * FROM product_variant WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_external_id(self, external_id: str):
        query = "SELECT * FROM product_variant WHERE external_id = UPPER(?)"
        result = self.db.connection.execute(query, (external_id,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_variant_name(self, variant_name: str):
        query = "SELECT * FROM product_variant WHERE variant_name = UPPER(?)"
        result = self.db.connection.execute(query, (variant_name,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_model(self, model: str):
        query = "SELECT * FROM product_variant WHERE model = UPPER(?)"
        result = self.db.connection.execute(query, (model,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_color(self, color: str):
        query = "SELECT * FROM product_variant WHERE color = UPPER(?)"
        result = self.db.connection.execute(query, (color,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_size_height(self, size_height: float):
        query = "SELECT * FROM product_variant WHERE size_height = ?"
        result = self.db.connection.execute(query, (size_height,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_size_width(self, size_width: float):
        query = "SELECT * FROM product_variant WHERE size_width = ?"
        result = self.db.connection.execute(query, (size_width,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_weight(self, weight: float):
        query = "SELECT * FROM product_variant WHERE weight = ?"
        result = self.db.connection.execute(query, (weight,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_variants(self):
        query = "SELECT * FROM product_variant"
        return self.db.fetchone(query)

    def update_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        query = "UPDATE product_variant SET product_id = ?, external_id = ?, variant_name = ?, model = ?, color = ?, size_height = ?, size_width = ?, weight = ? WHERE id = ?"
        self.db.connection.execute(query, (product_id, external_id, variant_name, model, color, size_height, size_width, weight, id))
        self.db.disconnect()

    def delete_product_variant_by_id(self, id: int):
        query = "DELETE FROM product_variant WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_variant_by_external_id(self, external_id: str):
        query = "DELETE FROM product_variant WHERE external_id = UPPER(?)"
        self.db.connection.execute(query, (external_id,))
        self.db.disconnect()

    def delete_product_variant_by_variant_name(self, variant_name: str):
        query = "DELETE FROM product_variant WHERE variant_name = UPPER(?)"
        self.db.connection.execute(query, (variant_name,))
        self.db.disconnect()

    def delete_product_variant_by_model(self, model: str):
        query = "DELETE FROM product_variant WHERE model = UPPER(?)"
        self.db.connection.execute(query, (model,))
        self.db.disconnect()

    def delete_product_variant_by_color(self, color: str):
        query = "DELETE FROM product_variant WHERE color = UPPER(?)"
        self.db.connection.execute(query, (color,))
        self.db.disconnect()

    def delete_product_variant_by_size_height(self, size_height: float):
        query = "DELETE FROM product_variant WHERE size_height = ?"
        self.db.connection.execute(query, (size_height,))
        self.db.disconnect()

    def delete_product_variant_by_size_width(self, size_width: float):
        query = "DELETE FROM product_variant WHERE size_width = ?"
        self.db.connection.execute(query, (size_width,))
        self.db.disconnect()

    def delete_product_variant_by_weight(self, weight: float):
        query = "DELETE FROM product_variant WHERE weight = ?"
        self.db.connection.execute(query, (weight,))
        self.db.disconnect()



    def add_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        query = "INSERT INTO product_price (id, price, price_date, manufacturer, marketplace, product_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, price, price_date, manufacturer, marketplace, product_id))
        self.db.disconnect()

    def get_product_price_by_id(self, id: int):
        query = "SELECT * FROM product_price WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_price(self, price: float):
        query = "SELECT * FROM product_price WHERE price = ?"
        result = self.db.connection.execute(query, (price,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_price_date(self, price_date: str):
        query = "SELECT * FROM product_price WHERE price_date = ?"
        result = self.db.connection.execute(query, (price_date,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_manufacturer(self, manufacturer: int):
        query = "SELECT * FROM product_price WHERE manufacturer = ?"
        result = self.db.connection.execute(query, (manufacturer,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_marketplace(self, marketplace: int):
        query = "SELECT * FROM product_price WHERE marketplace = ?"
        result = self.db.connection.execute(query, (marketplace,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_product_id(self, product_id: int):
        query = "SELECT * FROM product_price WHERE product_id = ?"
        result = self.db.connection.execute(query, (product_id,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_prices(self):
        query = "SELECT * FROM product_price"
        return self.db.fetchone(query)

    def update_product_price(self, id: int, price: float, price_date: str, manufacturer: int, marketplace: int, product_id: int):
        query = "UPDATE product_price SET price = ?, price_date = ?, manufacturer = ?, marketplace = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (price, price_date, manufacturer, marketplace, product_id, id))
        self.db.disconnect()

    def delete_product_price_by_id(self, id: int):
        query = "DELETE FROM product_price WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_price_by_price(self, price: float):
        query = "DELETE FROM product_price WHERE price = ?"
        self.db.connection.execute(query, (price,))
        self.db.disconnect()

    def delete_product_price_by_price_date(self, price_date: str):
        query = "DELETE FROM product_price WHERE price_date = ?"
        self.db.connection.execute(query, (price_date,))
        self.db.disconnect()

    def delete_product_price_by_manufacturer(self, manufacturer: int):
        query = "DELETE FROM product_price WHERE manufacturer = ?"
        self.db.connection.execute(query, (manufacturer,))
        self.db.disconnect()

    def delete_product_price_by_marketplace(self, marketplace: int):
        query = "DELETE FROM product_price WHERE marketplace = ?"
        self.db.connection.execute(query, (marketplace,))
        self.db.disconnect()

    def delete_product_price_by_product_id(self, product_id: int):
        query = "DELETE FROM product_price WHERE product_id = ?"
        self.db.connection.execute(query, (product_id,))
        self.db.disconnect()

    def get_lowest_product_price(self, product_id: int):
        query = "SELECT * FROM product_price WHERE product_id = ? ORDER BY price_date DESC"
        return self.db.fetchone(query, (product_id,))

    def get_all_product_variants(self, product_id: int):
        query = "SELECT * FROM product_variant WHERE product_id = ?"
        return self.db.fetchone(query, (product_id,))

    def get_product_variant_with_prices(self, product_id: int):
        query = """
            SELECT pv.*, pp.price, pp.price_date
            FROM product_variant pv
            LEFT JOIN product_price pp ON pv.id = pp.product_variant_id
            WHERE pv.product_id = ?
            ORDER BY pp.price_date DESC
        """
        return self.db.fetchone(query, (product_id,))



    def add_product_url(self, id : int, marketplace_id: int, external_product_id: str, product_id: int):
        query = "INSERT INTO product_url (id, marketplace_id, external_product_id, product_id) VALUES (?, ?, ?, ?)"
        self.db.connection.execute(query, (id, marketplace_id, external_product_id, product_id))
        self.db.disconnect()

    def get_product_url_by_id(self, id: int):
        query = "SELECT * FROM product_url WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_url_by_marketplace_id(self, marketplace_id: int):
        query = "SELECT * FROM product_url WHERE marketplace_id = ?"
        result = self.db.connection.execute(query, (marketplace_id,))
        self.db.disconnect()
        return result if result else None


    def get_product_url_by_external_product_id(self, external_product_id: str):
        query = "SELECT * FROM product_url WHERE external_product_id = UPPER(?)"
        result = self.db.connection.execute(query, (external_product_id,))
        self.db.disconnect()
        return result if result else None

    def get_product_url_by_product_id(self, product_id: int):
        query = "SELECT * FROM product_url WHERE product_id = ?"
        result = self.db.connection.execute(query, (product_id,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_urls(self):
        query = "SELECT * FROM product_url"
        return self.db.fetchone(query)

    def update_product_url(self, id: int, marketplace_id: int, external_product_id: str, product_id: int):
        query = "UPDATE product_url SET marketplace_id = ?, external_product_id = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (marketplace_id, external_product_id, product_id, id))
        self.db.disconnect()

    def delete_product_url_by_id(self, id: int):
        query = "DELETE FROM product_url WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_url_by_marketplace_id(self, marketplace_id: int):
        query = "DELETE FROM product_url WHERE marketplace_id = ?"
        self.db.connection.execute(query, (marketplace_id,))
        self.db.disconnect()

    def delete_product_url_by_external_product_id(self, external_product_id: str):
        query = "DELETE FROM product_url WHERE external_product_id = UPPER(?)"
        self.db.connection.execute(query, (external_product_id,))
        self.db.disconnect()

    def delete_product_url_by_product_id(self, product_id: int):
        query = "DELETE FROM product_url WHERE product_id = ?"
        self.db.connection.execute(query, (product_id,))
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

        print("\nAll Product Variants:")
        for variant in product_repo.get_all_product_variants(1234):
            print(variant)

