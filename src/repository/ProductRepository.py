import sqlite3
import pathlib
import uuid

from ..database.ManageDatabase import ManageDatabase

class ProductRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db
        self.connection = sqlite3.Connection
        self.cursor: sqlite3.Cursor

    def add_category(self, id: str, name: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        try:
            id = str(id)
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "INSERT INTO category (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()

    def get_category_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")
        
        query = "SELECT * FROM category WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_category_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "SELECT * FROM category WHERE name = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result if result else None

    def get_all_categories(self):
        query = "SELECT * FROM category"
        return self.db.fetchone(query)

    def update_category(self, id: str, name: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        try:
            id = str(id)
            name = str(name).upper()

        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "UPDATE category SET name = UPPER(?) WHERE id = ?"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_category_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id)
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM category WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_category_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "DELETE FROM category WHERE name = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()



    def add_product(self, id: str, name: str, category: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        assert isinstance(category, str), "category must be a string"
        try:
            id = str(id)
            name = str(name).upper()
            category = str(category).upper()
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")
        
        query = "INSERT INTO product (id, name, category) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, category))
        self.db.disconnect()

    def get_product_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "SELECT * FROM product WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "SELECT * FROM product WHERE name = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result if result else None

    def get_all_products(self):
        query = "SELECT * FROM product"
        return self.db.fetchone(query)

    def update_product(self, id: str, name: str, category: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        assert isinstance(category, str), "category must be a string"

        try:
            id = str(id)
            name = str(name).upper()
            category = str(category).upper()
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "UPDATE product SET id = ?, name = UPPER(?), category = ? WHERE id = ?"
        self.db.connection.execute(query, (name, category, id))
        self.db.disconnect()

    def delete_product_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id)
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM product WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")
        
        query = "DELETE FROM product WHERE name = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()



    def add_product_variant(self, id: str, product_id: str, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        id = str(uuid.uuid4())
        product_id = str(uuid.uuid4())
        external_id = str(uuid.uuid4())

        assert isinstance(id, str), "id must be a string"
        assert isinstance(product_id, str), "product_id must be a string"
        assert isinstance(external_id, str), "external_id must be a string"
        assert isinstance(variant_name, str), "variant_name must be a string"
        assert isinstance(model, str), "model must be a string"
        assert isinstance(color, str), "color must be a string"
        assert isinstance(size_height, float), "size_height must be a float"
        assert isinstance(size_width, float), "size_width must be a float"
        assert isinstance(weight, float), "weight must be a float"
        try:
            id = str(id)
            product_id = str(product_id)
            external_id = str(external_id)
            variant_name = str(variant_name).upper()
            model = str(model).upper()
            color = str(color).upper()
            size_height = float(size_height)
            size_width = float(size_width)
            weight = float(weight)
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "INSERT INTO product_variant (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight))
        self.db.disconnect()

    def get_product_variant_by_id(self, id: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_external_id(self, external_id: str):
        external_id = str(uuid.uuid4())
        assert isinstance(external_id, str), "external_id must be a string"
        try:
            external_id = str(external_id).upper()
        except Exception as e:  
            raise ValueError(f"external_id must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE external_id = ?"
        result = self.db.connection.execute(query, (external_id,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_variant_name(self, variant_name: str):
        variant_name = str(uuid.uuid4())
        assert isinstance(variant_name, str), "variant_name must be a string"
        try:
            variant_name = str(variant_name).upper()
        except Exception as e:
            raise ValueError(f"variant_name must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE variant_name = UPPER(?)"
        result = self.db.connection.execute(query, (variant_name,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_model(self, model: str):
        model = str(uuid.uuid4())
        assert isinstance(model, str), "model must be a string"
        try:
            model = str(model).upper()
        except Exception as e:
            raise ValueError(f"model must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE model = UPPER(?)"
        result = self.db.connection.execute(query, (model,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_color(self, color: str):
        color = str(uuid.uuid4())
        assert isinstance(color, str), "color must be a string"
        try:
            color = str(color).upper()
        except Exception as e:
            raise ValueError(f"color must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE color = UPPER(?)"
        result = self.db.connection.execute(query, (color,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_size_height(self, size_height: float):
        assert isinstance(size_height, float), "size_height must be a float"
        try: 
            size_height = float(size_height)
        except Exception as e:
            raise ValueError(f"size_height must be a float: {e}")

        query = "SELECT * FROM product_variant WHERE size_height = ?"
        result = self.db.connection.execute(query, (size_height,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_size_width(self, size_width: float):
        assert isinstance(size_width, float), "size_width must be a float"
        try:
            size_width = float(size_width)
        except Exception as e:
            raise ValueError(f"size_width must be a float: {e}")

        query = "SELECT * FROM product_variant WHERE size_width = ?"
        result = self.db.connection.execute(query, (size_width,))
        self.db.disconnect()
        return result if result else None

    def get_product_variant_by_weight(self, weight: float):
        assert isinstance(weight, float), "weight must be a float"
        try:
            weight = float(weight)
        except Exception as e:
            raise ValueError(f"weight must be a float: {e}")

        query = "SELECT * FROM product_variant WHERE weight = ?"
        result = self.db.connection.execute(query, (weight,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_variants(self):
        query = "SELECT * FROM product_variant"
        return self.db.fetchone(query)

    def update_product_variant(self, id: int, product_id: int, external_id: str, variant_name: str, model: str, color: str, size_height: float, size_width: float, weight: float):
        assert isinstance(id, int), "id must be an integer"
        assert isinstance(product_id, int), "product_id must be an integer"
        assert isinstance(external_id, str), "external_id must be a string"
        assert isinstance(variant_name, str), "variant_name must be a string"
        assert isinstance(model, str), "model must be a string"
        assert isinstance(color, str), "color must be a string"
        assert isinstance(size_height, float), "size_height must be a float"
        assert isinstance(size_width, float), "size_width must be a float"
        assert isinstance(weight, float), "weight must be a float"
        try:
            id = int(id)
            product_id = int(product_id)
            external_id = str(external_id).upper()
            variant_name = str(variant_name).upper()
            model = str(model).upper()
            color = str(color).upper()
            size_height = float(size_height)
            size_width = float(size_width)
            weight = float(weight)
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")
        
        query = "UPDATE product_variant SET id = ?, product_id = ?, external_id = ?, variant_name = UPPER(?), model = UPPER(?), color = UPPER(?), size_height = ?, size_width = ?, weight = ? WHERE id = ?"
        self.db.connection.execute(query, (id, product_id, external_id, variant_name, model, color, size_height, size_width, weight, id))
        self.db.disconnect()

    def delete_product_variant_by_id(self, id: int):
        assert isinstance(id, int), "id must be an integer"
        try:
            id = int(id)
        except Exception as e:
            raise ValueError(f"id must be an integer: {e}")

        query = "DELETE FROM product_variant WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_variant_by_external_id(self, external_id: str):
        assert isinstance(external_id, str), "external_id must be a string"
        try:
            external_id = str(external_id).upper()
        except Exception as e:
            raise ValueError(f"external_id must be a string: {e}")
        
        query = "DELETE FROM product_variant WHERE external_id = ?"
        self.db.connection.execute(query, (external_id,))
        self.db.disconnect()

    def delete_product_variant_by_variant_name(self, variant_name: str):
        assert isinstance(variant_name, str), "variant_name must be a string"
        try:
            variant_name = str(variant_name).upper()
        except Exception as e:
            raise ValueError(f"variant_name must be a string: {e}")

        query = "DELETE FROM product_variant WHERE variant_name = UPPER(?)"
        self.db.connection.execute(query, (variant_name,))
        self.db.disconnect()

    def delete_product_variant_by_model(self, model: str):
        assert isinstance(model, str), "model must be a string"
        try:
            model = str(model).upper()
        except Exception as e:
            raise ValueError(f"model must be a string: {e}")

        query = "DELETE FROM product_variant WHERE model = UPPER(?)"
        self.db.connection.execute(query, (model,))
        self.db.disconnect()

    def delete_product_variant_by_color(self, color: str):
        assert isinstance(color, str), "color must be a string"
        try:
            color = str(color).upper()
        except Exception as e:
            raise ValueError(f"color must be a string: {e}")

        query = "DELETE FROM product_variant WHERE color = UPPER(?)"
        self.db.connection.execute(query, (color,))
        self.db.disconnect()

    def delete_product_variant_by_size_height(self, size_height: float):
        assert isinstance(size_height, float), "size_height must be a float"
        try:
            size_height = float(size_height)
        except Exception as e:
            raise ValueError(f"size_height must be a float: {e}")
        
        query = "DELETE FROM product_variant WHERE size_height = ?"
        self.db.connection.execute(query, (size_height,))
        self.db.disconnect()

    def delete_product_variant_by_size_width(self, size_width: float):
        assert isinstance(size_width, float), "size_width must be a float"
        try:
            size_width = float(size_width)
        except Exception as e:
            raise ValueError(f"size_width must be a float: {e}")
        
        query = "DELETE FROM product_variant WHERE size_width = ?"
        self.db.connection.execute(query, (size_width,))
        self.db.disconnect()

    def delete_product_variant_by_weight(self, weight: float):
        assert isinstance(weight, float), "weight must be a float"
        try:
            weight = float(weight)
        except Exception as e:
            raise ValueError(f"weight must be a float: {e}")
        
        query = "DELETE FROM product_variant WHERE weight = ?"
        self.db.connection.execute(query, (weight,))
        self.db.disconnect()



    def add_product_price(self, id: str, price: float, price_date: str, manufacturer: str, marketplace: str, product_id: str):
        id = str(uuid.uuid4())
        manufacturer = str(uuid.uuid4())
        marketplace = str(uuid.uuid4())
        product_id = str(uuid.uuid4())

        assert isinstance(id, str), "id must be a string"
        assert isinstance(price, float), "price must be a float"
        assert isinstance(price_date, str), "price_date must be a string"
        assert isinstance(manufacturer, str), "manufacturer must be a string"
        assert isinstance(marketplace, str), "marketplace must be a string"
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            id = str(id)
            price = float(price)
            price_date = str(price_date)
            manufacturer = str(manufacturer)
            marketplace = str(marketplace)
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "INSERT INTO product_price (id, price, price_date, manufacturer, marketplace, product_id) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.connection.execute(query, (id, price, price_date, manufacturer, marketplace, product_id))
        self.db.disconnect(),

    def get_product_price_by_id(self, id: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "SELECT * FROM product_price WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_price(self, price: float):
        assert isinstance(price, float), "price must be a float"
        try:
            price = float(price)
        except Exception as e:
            raise ValueError(f"price must be a float: {e}")

        query = "SELECT * FROM product_price WHERE price = ?"
        result = self.db.connection.execute(query, (price,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_price_date(self, price_date: str):
        assert isinstance(price_date, str), "price_date must be a string"
        try:
            price_date = str(price_date)
        except Exception as e:
            raise ValueError(f"price_date must be a string: {e}")

        query = "SELECT * FROM product_price WHERE price_date = ?"
        result = self.db.connection.execute(query, (price_date,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_manufacturer(self, manufacturer: str):
        assert isinstance(manufacturer, str), "manufacturer must be a string"
        try:
            manufacturer = str(manufacturer)
        except Exception as e:
            raise ValueError(f"manufacturer must be a string: {e}")

        query = "SELECT * FROM product_price WHERE manufacturer = ?"
        result = self.db.connection.execute(query, (manufacturer,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_marketplace(self, marketplace: str):
        assert isinstance(marketplace, str), "marketplace must be a string"
        try:
            marketplace = str(marketplace)
        except Exception as e:
            raise ValueError(f"marketplace must be a string: {e}")
        
        query = "SELECT * FROM product_price WHERE marketplace = ?"
        result = self.db.connection.execute(query, (marketplace,))
        self.db.disconnect()
        return result if result else None

    def get_product_price_by_product_id(self, product_id: str):
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")

        query = "SELECT * FROM product_price WHERE product_id = ?"
        result = self.db.connection.execute(query, (product_id,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_prices(self):
        query = "SELECT * FROM product_price"
        return self.db.fetchone(query)

    def update_product_price(self, id: str, price: float, price_date: str, manufacturer: str, marketplace: str, product_id: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(price, float), "price must be a float"
        assert isinstance(price_date, str), "price_date must be a string"
        assert isinstance(manufacturer, str), "manufacturer must be a string"
        assert isinstance(marketplace, str), "marketplace must be a string"
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            id = str(id)
            price = float(price)
            price_date = str(price_date)
            manufacturer = str(manufacturer)
            marketplace = str(marketplace)
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"All parameters must be of the correct type: {e}")

        query = "UPDATE product_price SET price = ?, price_date = ?, manufacturer = ?, marketplace = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (price, price_date, manufacturer, marketplace, product_id, id))
        self.db.disconnect()

    def delete_product_price_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id)
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM product_price WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_price_by_price(self, price: float):
        assert isinstance(price, float), "price must be a float"
        try:
            price = float(price)
        except Exception as e:
            raise ValueError(f"price must be a float: {e}")

        query = "DELETE FROM product_price WHERE price = ?"
        self.db.connection.execute(query, (price,))
        self.db.disconnect()

    def delete_product_price_by_price_date(self, price_date: str):
        assert isinstance(price_date, str), "price_date must be a string"
        try:
            price_date = str(price_date)
        except Exception as e:
            raise ValueError(f"price_date must be a string: {e}")

        query = "DELETE FROM product_price WHERE price_date = ?"
        self.db.connection.execute(query, (price_date,))
        self.db.disconnect()

    def delete_product_price_by_manufacturer(self, manufacturer: str):
        assert isinstance(manufacturer, str), "manufacturer must be a string"
        try:
            manufacturer = str(manufacturer)
        except Exception as e:
            raise ValueError(f"manufacturer must be a string: {e}")

        query = "DELETE FROM product_price WHERE manufacturer = ?"
        self.db.connection.execute(query, (manufacturer,))
        self.db.disconnect()

    def delete_product_price_by_marketplace(self, marketplace: str):
        assert isinstance(marketplace, str), "marketplace must be a string"
        try:
            marketplace = str(marketplace)
        except Exception as e:  
            raise ValueError(f"marketplace must be a string: {e}")

        query = "DELETE FROM product_price WHERE marketplace = ?"
        self.db.connection.execute(query, (marketplace,))
        self.db.disconnect()

    def delete_product_price_by_product_id(self, product_id: str):
        product_id = str(uuid.uuid4())

        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")
        
        query = "DELETE FROM product_price WHERE product_id = ?"
        self.db.connection.execute(query, (product_id,))
        self.db.disconnect()

    def get_lowest_product_price(self, product_id: str):
        product_id = str(uuid.uuid4())

        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")
        
        query = "SELECT * FROM product_price WHERE product_id = ? ORDER BY price_date DESC"
        return self.db.fetchone(query, (product_id,))

    def get_all_product_variants(self, product_id: str):
        product_id = str(uuid.uuid4())

        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")

        query = "SELECT * FROM product_variant WHERE product_id = ?"
        return self.db.fetchone(query, (product_id,))

    def get_product_variant_with_prices(self, product_id: str):
        product_id = str(uuid.uuid4())

        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:  
            raise ValueError(f"product_id must be a string: {e}")

        query = """
            SELECT pv.*, pp.price, pp.price_date
            FROM product_variant pv
            LEFT JOIN product_price pp ON pv.id = pp.product_variant_id
            WHERE pv.product_id = ?
            ORDER BY pp.price_date DESC
        """
        return self.db.fetchone(query, (product_id,))



    def add_product_url(self, id : str, marketplace_id: str, external_product_id: str, product_id: str):
        id = str(uuid.uuid4())
        marketplace_id = str(uuid.uuid4())
        external_product_id = str(uuid.uuid4())
        product_id = str(uuid.uuid4())

        assert isinstance(id, str), "id must be a string"
        assert isinstance(marketplace_id, str), "marketplace_id must be a string"
        assert isinstance(external_product_id, str), "external_product_id must be a string"
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            id = str(id)
            marketplace_id = str(marketplace_id)
            external_product_id = str(external_product_id)
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"All parameters must be strings: {e}")

        query = "INSERT INTO product_url (id, marketplace_id, external_product_id, product_id) VALUES (?, ?, ?, ?)"
        self.db.connection.execute(query, (id, marketplace_id, external_product_id, product_id))
        self.db.disconnect()

    def get_product_url_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "SELECT * FROM product_url WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_product_url_by_marketplace_id(self, marketplace_id: str):
        assert isinstance(marketplace_id, str), "marketplace_id must be a string"
        try:
            marketplace_id = str(marketplace_id).upper()
        except Exception as e:
            raise ValueError(f"marketplace_id must be a string: {e}")

        query = "SELECT * FROM product_url WHERE marketplace_id = ?"
        result = self.db.connection.execute(query, (marketplace_id,))
        self.db.disconnect()
        return result if result else None


    def get_product_url_by_external_product_id(self, external_product_id: str):
        assert isinstance(external_product_id, str), "external_product_id must be a string"
        try:
            external_product_id = str(external_product_id).upper()
        except Exception as e:
            raise ValueError(f"external_product_id must be a string: {e}")

        query = "SELECT * FROM product_url WHERE external_product_id = ?"
        result = self.db.connection.execute(query, (external_product_id,))
        self.db.disconnect()
        return result if result else None

    def get_product_url_by_product_id(self, product_id: str):
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id).upper()
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")

        query = "SELECT * FROM product_url WHERE product_id = ?"
        result = self.db.connection.execute(query, (product_id,))
        self.db.disconnect()
        return result if result else None

    def get_all_product_urls(self):
        query = "SELECT * FROM product_url"
        return self.db.fetchone(query)

    def update_product_url(self, id: str, marketplace_id: str, external_product_id: str, product_id: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(marketplace_id, str), "marketplace_id must be a string"
        assert isinstance(external_product_id, str), "external_product_id must be a string"
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            id = str(id)
            marketplace_id = str(marketplace_id)
            external_product_id = str(external_product_id)
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"All parameters must be strings: {e}")

        query = "UPDATE product_url SET marketplace_id = ?, external_product_id = ?, product_id = ? WHERE id = ?"
        self.db.connection.execute(query, (marketplace_id, external_product_id, product_id, id))
        self.db.disconnect()

    def delete_product_url_by_id(self, id: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id)
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM product_url WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_product_url_by_marketplace_id(self, marketplace_id: str):
        marketplace_id = str(uuid.uuid4())
        assert isinstance(marketplace_id, str), "marketplace_id must be a string"
        try:
            marketplace_id = str(marketplace_id)
        except Exception as e:
            raise ValueError(f"marketplace_id must be a string: {e}")

        query = "DELETE FROM product_url WHERE marketplace_id = ?"
        self.db.connection.execute(query, (marketplace_id,))
        self.db.disconnect()

    def delete_product_url_by_external_product_id(self, external_product_id: str):
        external_product_id = str(uuid.uuid4())
        assert isinstance(external_product_id, str), "external_product_id must be a string"
        try:
            external_product_id = str(external_product_id)
        except Exception as e:
            raise ValueError(f"external_product_id must be a string: {e}")

        query = "DELETE FROM product_url WHERE external_product_id = ?"
        self.db.connection.execute(query, (external_product_id,))
        self.db.disconnect()

    def delete_product_url_by_product_id(self, product_id: str):
        product_id = str(uuid.uuid4())
        assert isinstance(product_id, str), "product_id must be a string"
        try:
            product_id = str(product_id)
        except Exception as e:
            raise ValueError(f"product_id must be a string: {e}")

        query = "DELETE FROM product_url WHERE product_id = ?"
        self.db.connection.execute(query, (product_id,))
        self.db.disconnect()


        
    

if __name__ == "__main__":
        db = ManageDatabase(db_file_path=str(pathlib.Path(__file__).parent / "database.db"), schema_file_path='./src/database/schema.sql')
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

