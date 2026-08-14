from ..database.ManageDatabase import ManageDatabase

class MarketplaceRepository:
    def __init__(self, db: ManageDatabase):
        self.db = db

    def add_marketplace(self, id: int, name: str, url: str):
        query = "INSERT INTO marketplace (id, name, url) VALUES (?, ?, ?)"
        self.db.connection.execute(query, (id, name, url))
        self.db.disconnect()

    def get_marketplace(self, id: int):
        query = "SELECT * FROM marketplace WHERE id = ?"
        result = self.db.connection.execute(query, (id,))
        self.db.disconnect()
        return result if result else None

    def get_all_marketplaces(self):
        query = "SELECT * FROM marketplace"
        return self.db.fetchall(query)

    def update_marketplace(self, id: int, name: str, url: str):
        query = "UPDATE marketplace SET name = ?, url = ? WHERE id = ?"
        self.db.connection.execute(query, (name, url, id))
        self.db.disconnect()

    def delete_marketplace(self, id: int):
        query = "DELETE FROM marketplace WHERE id = ?"
        self.db.connection.execute(query, (id,))
        self.db.disconnect()


if __name__ == "__main__":
    db = ManageDatabase(db_file_path='./src/database/database.db', schema_file_path='./src/database/schema.sql')
    marketplace_repo = MarketplaceRepository(db)

    marketplace_repo.add_marketplace(1234, "ExampleMarketplace", "https://www.example.com")
    marketplace = marketplace_repo.get_marketplace(1234)
    print(marketplace)