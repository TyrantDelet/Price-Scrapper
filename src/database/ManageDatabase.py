import sqlite3


class ManageDatabase:
    def __init__(self, db_file_path = 'database.db', schema_file_path = 'src/database/schema.sql'):
        self.db_file_path = db_file_path
        self.schema_file_path = schema_file_path

        self.connection = sqlite3.Connection
        self.cursor: sqlite3.Cursor
        self.row_factory = sqlite3.Row 
        self._connect()
        self._initialize_schema()


    def _connect(self):
        self.connection = sqlite3.connect(self.db_file_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def disconnect(self):
        try:
            if hasattr(self, 'connection') and self.connection:
                self.connection.commit()
        except sqlite3.ProgrammingError:
            pass

    def _initialize_schema(self):
        with open(self.schema_file_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()

            self.cursor.executescript(schema_sql)

    def fetchone(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        row = self.cursor.fetchone()
        return dict(row) if row else None