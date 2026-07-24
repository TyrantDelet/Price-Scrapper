CREATE TABLE IF NOT EXISTS marketplace (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    url VARCHAR(2500)
);

CREATE TABLE IF NOT EXISTS manufacturer (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    model VARCHAR(256) NOT NULL,
    manufacturer VARCHAR(256) NOT NULL,
    marketplace VARCHAR(256) NOT NULL,
    color VARCHAR(100) NOT NULL,
    category VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS product_price (
    id INTEGER PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    manufacturer VARCHAR(256) NOT NULL,
    marketplace VARCHAR(256) NOT NULL,
    product_id INTEGER
);

CREATE TABLE IF NOT EXISTS product_url (
    product_url VARCHAR(2500) NOT NULL,
    marketplace_url VARCHAR(2500) NOT NULL,
    product_sku VARCHAR(256) NOT NULL,
    product_id INTEGER NOT NULL
);
