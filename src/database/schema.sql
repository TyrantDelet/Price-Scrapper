CREATE TABLE IF NOT EXISTS marketplace (
    id TEXT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    url VARCHAR(2500)
);

CREATE TABLE IF NOT EXISTS manufacturer (
    id TEXT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
    id TEXT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS product (
    id TEXT PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    category TEXT NOT NULL REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS product_variant (
    id TEXT PRIMARY KEY,
    product_id TEXT NOT NULL REFERENCES product(id),
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
    id TEXT PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    price_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    manufacturer TEXT NOT NULL REFERENCES manufacturer(id),
    marketplace TEXT NOT NULL REFERENCES marketplace(id),
    product_id TEXT NOT NULL REFERENCES product_variant(id)
);

CREATE TABLE IF NOT EXISTS product_url (
    id TEXT PRIMARY KEY,
    marketplace_id TEXT NOT NULL REFERENCES marketplace(id),
    external_product_id VARCHAR(500) NOT NULL REFERENCES product(external_id),
    product_id TEXT NOT NULL REFERENCES product(id)
);

