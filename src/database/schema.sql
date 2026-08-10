CREATE TABLE IF NOT EXISTS marketplace (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    url VARCHAR(2500)
);

CREATE TABLE IF NOT EXISTS manufacturer (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    category INTEGER NOT NULL REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS product_variant (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES product(id),
    external_id VARCHAR(500) UNIQUE,
    variant_name VARCHAR(256) NOT NULL,
    model VARCHAR(256) NOT NULL,
    color VARCHAR(100),
    size_height DECIMAL(10, 2),
    size_width DECIMAL(10, 2),
    weight DECIMAL(10, 2),
    UNIQUE(product_id, variant_name, model, color, size_height, size_width, weight)
);

CREATE TABLE IF NOT EXISTS product_price (
    id INTEGER PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    price_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    manufacturer INTEGER NOT NULL REFERENCES manufacturer(id),
    marketplace INTEGER NOT NULL REFERENCES marketplace(id),
    product_id INTEGER NOT NULL REFERENCES product_variant(id)
);

CREATE TABLE IF NOT EXISTS product_url (
    id INTEGER PRIMARY KEY,
    marketplace_id INTEGER NOT NULL REFERENCES marketplace(id),
    external_product_id VARCHAR(500) NOT NULL REFERENCES product(external_id),
    product_id INTEGER NOT NULL REFERENCES product(id)
);

