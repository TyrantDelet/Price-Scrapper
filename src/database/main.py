import sqlite3
from pathlib import Path


class CreateDatabase:
    def __init__(self, db_file_path = 'database.db', schema_file_path = 'schema.sql'):
        self.db_file_path = db_file_path
        self.schema_file_path = schema_file_path
        db_exists = Path(self.db_file_path).exists()

        self.connection = sqlite3.connect(self.db_file_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        with open(self.schema_file_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()

        self.cursor.executescript(schema_sql)
        self.connection.commit()

    def execute(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetchall(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def close(self):
        self.connection.close()

class ProductRepository:
    def __init__(self, db: CreateDatabase):
        self.db = db

    def add_marketplace(self, name: str, id: int, url: str):
        query = "INSERT INTO marketplace (name, id, url) VALUES (?, ?, ?)"
        self.db.execute(query, (name, id, url))
       
    def add_manufracturer(self, name: str, id: int):
        query = "INSERT INTO manufacturer (name, id) VALUES (?, ?)"
        self.db.execute(query, (name, id))

    def add_product(self, id: int, name: str, model: str, manufacturer: str, marketplace: str, color: str, category: str):
        query = "INSERT INTO product (id, name, model, manufacturer, marketplace, color, category) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.db.execute(query, (id, name, model, manufacturer, marketplace, color, category))

    def add_product_price(self, id: int, price: float, date: str, manufacturer: str, marketplace: str):
        query = "INSERT INTO product_price (id, price, date, manufacturer, marketplace) VALUES (?, ?, ?, ?, ?)"
        self.db.execute(query, (id, price, date, manufacturer, marketplace))

    def add_urls(self, product_url: str, marketplace_url: str, product_sku: str, product_id: int):
        query = "INSERT INTO product_url (product_url, marketplace_url, product_sku, product_id) VALUES (?, ?, ?, ?)"
        self.db.execute(query, (product_url, marketplace_url, product_sku, product_id))

    def add_url(self, product_url: str, marketplace_url: str, product_sku: str, product_id: int):
        return self.add_urls(product_url, marketplace_url, product_sku, product_id)

    def get_product_by_id(self, product_id: int):
        query = "SELECT * FROM product WHERE id = ?"
        result = self.db.fetchall(query, (product_id,))
        return result[0] if result else None

    def get_all_products(self):
        query = "SELECT * FROM product"
        return self.db.fetchall(query)

    def get_product_prices(self, product_id: int):
        query = "SELECT * FROM product_price WHERE id = ?"
        return self.db.fetchall(query, (product_id,))

    def get_product_urls(self, product_id: int):
        query = "SELECT * FROM product_url WHERE product_id = ?"
        return self.db.fetchall(query, (product_id,))

    def get_all_marketplaces(self):
        query = "SELECT * FROM marketplace"
        return self.db.fetchall(query)

    def get_all_manufacturers(self):
        query = "SELECT * FROM manufacturer"
        return self.db.fetchall(query)


if __name__ == "__main__":
        db = CreateDatabase(db_file_path='database.db', schema_file_path=str(Path(__file__).parent / 'schema.sql'))
        product_repo = ProductRepository(db)

        product_repo.add_marketplace(name="Example_MP", id=1, url="https://www.example.com")
        product_repo.add_manufracturer(name="Example_Manufacturer", id=1)
        product_repo.add_product(id=1, name="Example_Product", model="AQL123", manufacturer="Example_Manufracturer", marketplace="Example_MP", color="Black", category="Random")
        product_repo.add_product_price(id=1, price=999.99, date="2023-10-01", manufacturer="Example_Manufracturer", marketplace="Example_MP")
        product_repo.add_url(product_url="https://www.example.com", marketplace_url="https://www.example.com", product_sku="B09G9F5C6K", product_id=1)

        print("All Products:")
        for product in product_repo.get_all_products():
            print(product)

        db.close()