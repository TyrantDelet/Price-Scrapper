CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(256) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL,
    product_url VARCHAR(512) NOT NULL
);

CREATE TABLE product_categories (
    product_model VARCHAR(256) NOT NULL,
    product_sku VARCHAR(256) NOT NULL,
    product_manufacturer VARCHAR(256) NOT NULL,
    product_color VARCHAR(256) NOT NULL,
    product_category VARCHAR(256) NOT NULL
);
