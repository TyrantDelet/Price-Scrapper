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
    print("Database schema applied (created tables if not present).")
except sqlite3.Error as e:
    print(f"An error occurred while applying schema: {e}")
    conn.close()
    raise


try:
    cur.execute(
        "INSERT INTO products (product_name, product_price, product_url) VALUES (?, ?, ?)",
        ("Personal Computer", 5.50, "https://example.com/computer")
    )

    products = [
        ("Pen", 1.20, "https://example.com/pen"),
        ("Backpack", 45.00, "https://example.com/backpack"),
        ("Eraser", 0.75, "https://example.com/eraser"),
    ]
    cur.executemany(
        "INSERT INTO products (product_name, product_price, product_url) VALUES (?, ?, ?)",
        products
    )

    conn.commit()
    print("Data inserted successfully.")
except sqlite3.Error as e:
    print(f"An error occurred while inserting data: {e}")


try:
    cur.execute(
        "INSERT INTO product_categories (product_model, product_sku, product_manufacturer, product_category, product_color) VALUES (?, ?, ?, ?, ?)",
        ("Model X", "SKU12345", "Manufacturer A", "Electronics", "Black")
    )

    products_categories = [
        ("Model Y", "SKU67890", "Manufacturer B", "Electronics", "White"),
        ("Model Z", "SKU54321", "Manufacturer C", "Home Appliances", "Silver"),
    ]
    cur.executemany(
        "INSERT INTO product_categories (product_model, product_sku, product_manufacturer, product_category, product_color) VALUES (?, ?, ?, ?, ?)",
        products_categories
    )
    conn.commit()
    print("Data inserted into products_categories successfully.")
except sqlite3.Error as e:
    print(f"An error occurred while inserting data into products_categories: {e}")
    conn.close()
    raise
finally:
    conn.close()
