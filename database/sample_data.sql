INSERT INTO users (username, date_of_join, role)
VALUES 
('Alice', CURDATE(), 'buyer'),
('Bob', CURDATE(), 'seller');

INSERT INTO products 
(product_name, product_description, image_url, price, category, product_condition, stock, seller_id)
VALUES
('Laptop', 'Gaming Laptop', 'https://via.placeholder.com/150', 70000, 'Electronics', 'new', 5, 2),
('Phone', 'Smartphone', 'https://via.placeholder.com/150', 20000, 'Electronics', 'refurbished', 10, 2);