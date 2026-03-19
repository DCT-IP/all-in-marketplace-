USE marketplace;

INSERT INTO users (username, date_of_join)
VALUES ('Alice', CURDATE()), ('Bob', CURDATE());

INSERT INTO inventory (product_name, product_description, item_count)
VALUES 
('Laptop', 'Gaming Laptop', 5),
('Phone', 'Smartphone', 10),
('Headphones', 'Wireless', 3);