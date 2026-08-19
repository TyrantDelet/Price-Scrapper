import sqlite3

from ..database.ManageDatabase import ManageDatabase

class MarketplaceRepository:
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

    
    def add_marketplace(self, id: int, name: str, url: str):
        query = "INSERT INTO marketplace (id, name, url) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, url))
        self.db.disconnect()

    def get_marketplace_by_id(self, id: int):
        query = "SELECT * FROM marketplace WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_marketplace_by_name(self, name: str):
        query = "SELECT * FROM marketplace WHERE UPPER(name) = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_marketplace_by_url(self, url: str):
        query = "SELECT * FROM marketplace WHERE UPPER(url) = UPPER(?)"
        result = self.db.connection.execute(query, (url,))
        self.db.disconnect()
        return result.fetchone() if result else None
    
    def get_all_marketplaces(self):
        query = "SELECT * FROM marketplace"
        return self.db.fetchone(query)

    def update_marketplace(self, id: int, name: str, url: str):
        query = "UPDATE marketplace SET id = UPPER(?), name = UPPER(?), url = UPPER(?)"
        self.db.connection.execute(query, (id, name, url))
        self.db.disconnect()

    def delete_marketplace_by_id(self, id: int):
        query = "DELETE FROM marketplace WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_marketplace_by_name(self, name: str):
        query = "DELETE FROM marketplace WHERE UPPER(name) = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()

    def delete_marketplace_by_url(self, url: str):
        query = "DELETE FROM marketplace WHERE UPPER(url) = UPPER(?)"
        self.db.connection.execute(query, (url,))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path='./src/database/database.db', schema_file_path='./src/database/schema.sql')
    marketplace_repo = MarketplaceRepository(db)

    marketplace_repo.add_marketplace(1234, "ExampleMarketplace", "https://www.example.com")
    marketplace = marketplace_repo.get_marketplace_by_id(1234)
    print(marketplace)
