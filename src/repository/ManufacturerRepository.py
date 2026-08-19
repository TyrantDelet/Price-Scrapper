import sqlite3

from ..database.ManageDatabase import ManageDatabase

class ManufacturerRepository:
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

    
    def add_manufacturer(self, id: int, name: str):
        query = "INSERT INTO manufacturer (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name, ))
        self.db.disconnect()

    def get_manufacturer_by_id(self, id: int):
        query = "SELECT * FROM manufacturer WHERE id = UPPER(?)"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_manufacturer_by_name(self, name: str):
        query = "SELECT * FROM manufacturer WHERE UPPER(name) = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_all_manufacturers(self):
        query = "SELECT * FROM manufacturer"
        return self.db.fetchone(query)

    def update_manufacturer(self, id: int, name: str):
        query = "UPDATE manufacturer SET name = UPPER(?) WHERE id = UPPER(?)"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_manufacturer_by_id(self, id: int):
        query = "DELETE FROM manufacturer WHERE id = UPPER(?)"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_manufacturer_by_name(self, name: str):
        query = "DELETE FROM manufacturer WHERE UPPER(name) = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path='./src/database/database.db', schema_file_path='./src/database/schema.sql')
    manufacturer_repo = ManufacturerRepository(db)

    manufacturer_repo.add_manufacturer(1234, "ExampleManufacturer")
    manufacturer = manufacturer_repo.get_manufacturer_by_id(1234)
    print(manufacturer)
    