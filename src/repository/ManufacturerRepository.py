from ..database.ManageDatabase import ManageDatabase

class ManufacturerRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db

    def add_manufacturer(self, id: int, name: str):
        query = "INSERT INTO manufacturer (id, name) VALUES (?, ?)"
        self.db.connection.execute(query, (id, name, ))
        self.db.disconnect()

    def get_manufacturer(self, id: int, name: str):
        if id is not None and name is not None:
            query = "SELECT * FROM manufacturer WHERE id = UPPER(?) and UPPER(name) = UPPER(?)"
        elif id is not None:
            query = "SELECT * FROM manufacturer WHERE id = ?"
        elif name is not None:
            query = "SELECT * FROM manufacturer WHERE name = ?"
        else:
            raise ValueError("Either 'id' or 'name' must be provided.")
        result = self.db.connection.execute(query, (id or name,))
        self.db.disconnect()
        return result if result else None

    def get_all_manufacturers(self):
        query = "SELECT * FROM manufacturer"
        return self.db.fetchall(query)

    def update_manufacturer(self, id: int, name: str):
        query = "UPDATE manufacturer SET name = ? WHERE id = ?"
        self.db.connection.execute(query, (name, id))
        self.db.disconnect()

    def delete_manufacturer(self, id: int, name: str):
        query = "DELETE FROM manufacturer WHERE id = ? AND name = ?"
        self.db.connection.execute(query, (id, name))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path='./src/database/database.db', schema_file_path='./src/database/schema.sql')
    manufacturer_repo = ManufacturerRepository(db)

    manufacturer_repo.add_manufacturer(1234, "ExampleManufacturer")
    manufacturer = manufacturer_repo.get_manufacturer(1234, "ExampleManufacturer")
    print(manufacturer)