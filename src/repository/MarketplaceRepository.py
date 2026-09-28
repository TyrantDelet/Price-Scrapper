import sqlite3
import pathlib
import uuid

from ..database.ManageDatabase import ManageDatabase

class MarketplaceRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db
        self.connection = sqlite3.Connection
        self.cursor: sqlite3.Cursor
    
    def add_marketplace(self, id: str, name: str, url: str):
        id = str(uuid.uuid4())
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        assert isinstance(url, str), "url must be a string"
        try:
            id = str(id).upper()
            name = str(name).upper()
            url = str(url).upper()
        except Exception as e:
            raise ValueError(f"id, name, and url must be strings: {e}")
        
        query = "INSERT INTO marketplace (id, name, url) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, url))
        self.db.disconnect()

    def get_marketplace_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "SELECT * FROM marketplace WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_marketplace_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "SELECT * FROM marketplace WHERE UPPER(name) = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_marketplace_by_url(self, url: str):
        assert isinstance(url, str), "url must be a string"
        try:
            url = str(url).upper()
        except Exception as e:
            raise ValueError(f"url must be a string: {e}")

        query = "SELECT * FROM marketplace WHERE UPPER(url) = UPPER(?)"
        result = self.db.connection.execute(query, (url,))
        self.db.disconnect()
        return result.fetchone() if result else None
    
    def get_all_marketplaces(self):
        query = "SELECT * FROM marketplace"
        return self.db.fetchone(query)

    def update_marketplace(self, id: str, name: str, url: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        assert isinstance(url, str), "url must be a string"
        try:
            id = str(id).upper()
            name = str(name).upper()
            url = str(url).upper()
        except Exception as e:
            raise ValueError(f"id, name, and url must be strings: {e}")

        query = "UPDATE marketplace SET id = ?, name = UPPER(?), url = UPPER(?)"
        self.db.connection.execute(query, (id, name, url))
        self.db.disconnect()

    def delete_marketplace_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM marketplace WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_marketplace_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "DELETE FROM marketplace WHERE UPPER(name) = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()

    def delete_marketplace_by_url(self, url: str):
        assert isinstance(url, str), "url must be a string"
        try:
            url = str(url).upper()
        except Exception as e:
            raise ValueError(f"url must be a string: {e}")

        query = "DELETE FROM marketplace WHERE UPPER(url) = UPPER(?)"
        self.db.connection.execute(query, (url,))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path=str(pathlib.Path(__file__).parent / "database.db"), schema_file_path='./src/database/schema.sql')
    marketplace_repo = MarketplaceRepository(db)

    marketplace_repo.add_marketplace(1234, "ExampleMarketplace", "https://www.example.com")
    marketplace = marketplace_repo.get_marketplace_by_id(1234)
    print(marketplace)
