CREATE TABLE IF NOT EXISTS marketplace (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
);

CREATE TABLE IF NOT EXISTS manufracturer (
    id INTEGER PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    model VARCHAR(256) NOT NULL,
    color VARCHAR(100) NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    marketplace_id INTEGER NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufracturer(id),
    FOREIGN KEY (marketplace_id) REFERENCES marketplace(id)
);

CREATE TABLE IF NOT EXISTS product_price (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product(id),
    marketplace_id INTEGER NOT NULL,
    FOREIGN KEY (marketplace_id) REFERENCES marketplace(id),
    manufacturer_id INTEGER NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufracturer(id)
);

CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    url VARCHAR(2500) NOT NULL,
    sku VARCHAR(256) NOT NULL,
    marketplace_id INTEGER NOT NULL,
    FOREIGN KEY (marketplace_id) REFERENCES marketplace(id),
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id)
);