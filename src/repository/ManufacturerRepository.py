import sqlite3
import pathlib
import uuid


from ..database.ManageDatabase import ManageDatabase

class ManufacturerRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db
        self.connection = sqlite3.Connection
        self.cursor: sqlite3.Cursor

    def add_manufacturer(self, id: str, name: str):
        id = str(uuid.uuid4())
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")

        query = "INSERT INTO manufacturer (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name, ))
        self.db.disconnect()

    def get_manufacturer_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")
        
        query = "SELECT * FROM manufacturer WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_manufacturer_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")
        
        query = "SELECT * FROM manufacturer WHERE UPPER(name) = UPPER(?)"
        result = self.db.connection.execute(query, (name,))
        self.db.disconnect()
        return result.fetchone() if result else None

    def get_all_manufacturers(self):
        query = "SELECT * FROM manufacturer"
        return self.db.fetchone(query)

    def update_manufacturer(self, id: str, name: str):
        assert isinstance(id, str), "id must be a string"
        assert isinstance(name, str), "name must be a string"
        try:
            id = str(id).upper()
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"id and name must be strings: {e}")

        query = "UPDATE manufacturer SET name = UPPER(?) WHERE id = ?"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_manufacturer_by_id(self, id: str):
        assert isinstance(id, str), "id must be a string"
        try:
            id = str(id).upper()
        except Exception as e:
            raise ValueError(f"id must be a string: {e}")

        query = "DELETE FROM manufacturer WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()

    def delete_manufacturer_by_name(self, name: str):
        assert isinstance(name, str), "name must be a string"
        try:
            name = str(name).upper()
        except Exception as e:
            raise ValueError(f"name must be a string: {e}")
        
        query = "DELETE FROM manufacturer WHERE UPPER(name) = UPPER(?)"
        self.db.connection.execute(query, (name,))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path=str(pathlib.Path(__file__).parent / "database.db"), schema_file_path='./src/database/schema.sql')
    manufacturer_repo = ManufacturerRepository(db)

    manufacturer_repo.add_manufacturer(1234, "ExampleManufacturer")
    manufacturer = manufacturer_repo.get_manufacturer_by_id(1234)
    print(manufacturer)
    