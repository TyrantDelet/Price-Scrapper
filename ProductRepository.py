import sqlite3

sql_file_path = 'src/database/schema.sql'
db_file_path = 'database.db'

conn = sqlite3.connect(db_file_path)

cur = conn.cursor()

with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
    sql_script = sql_file.read()


try:
    cur.executescript(sql_script)
    conn.commit()
    print("database was created")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()