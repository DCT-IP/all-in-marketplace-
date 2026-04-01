USE marketplace;
INSERT INTO users (username, date_of_join, role)
VALUES 
('Alice', CURDATE(), 'buyer'),
('Bob', CURDATE(), 'seller');

INSERT INTO products 
(product_name, product_description, image_url, price, category, product_condition, stock, seller_id)
VALUES
('Laptop', 'Gaming Laptop', 'https://via.placeholder.com/150', 70000, 'Electronics', 'new', 5, 2),
('Phone', 'Smartphone', 'https://via.placeholder.com/150', 20000, 'Electronics', 'refurbished', 10, 2);

INSERT INTO products 
(seller_id, product_name, price, stock, category, condition_type, image_url)
VALUES
(1, 'iPhone 13', 50000, 10, 'Electronics', 'fresh', 'https://via.placeholder.com/150'),
(1, 'AirPods', 15000, 15, 'Electronics', 'fresh', 'https://via.placeholder.com/150'),

(2, 'Dell Laptop', 40000, 5, 'Computers', 'refurbished', 'https://via.placeholder.com/150'),
(2, 'Keyboard', 2000, 25, 'Accessories', 'fresh', 'https://via.placeholder.com/150'),

(3, 'Gaming Mouse', 1500, 30, 'Accessories', 'fresh', 'https://via.placeholder.com/150'),

(4, 'Samsung TV', 60000, 3, 'Electronics', 'refurbished', 'https://via.placeholder.com/150'),

(9, 'Demo Product', 999, 50, 'Test', 'fresh', 'https://via.placeholder.com/150');


INSERT INTO users (username, role, email, address, phone)
VALUES
('Rahul Mehta', 'seller', 'rahul@example.com', 'Mumbai', '9990000001'),
('Vikram Das', 'seller', 'vikram@example.com', 'Delhi', '9990000002'),
('Karan Patel', 'seller', 'karan@example.com', 'Ahmedabad', '9990000003'),
('Anita Sharma', 'seller', 'anita@example.com', 'Bangalore', '9990000004'),

('Amit Singh', 'buyer', 'amit@example.com', 'Lucknow', '9990000005'),
('Sneha Reddy', 'buyer', 'sneha@example.com', 'Hyderabad', '9990000006'),
('Rohit Verma', 'buyer', 'rohit@example.com', 'Pune', '9990000007'),
('Priya Nair', 'buyer', 'priya@example.com', 'Kochi', '9990000008'),

('demo1', 'seller', 'demo1@example.com', 'Test City', '9990000009'),
('demo2', 'buyer', 'demo2@example.com', 'Test City', '9990000010'),
('demon', 'buyer', 'demon@example.com', 'Test City', '9990000011');

INSERT INTO orders 
(user_id, product_id, quantity, total_price, phone, address, order_status)
VALUES
(5, 1, 1, 50000, '9990000005', 'Lucknow', 'Delivered'),
(6, 1, 2, 100000, '9990000006', 'Hyderabad', 'Delivered'),
(7, 2, 1, 15000, '9990000007', 'Pune', 'Shipped'),
(8, 3, 1, 40000, '9990000008', 'Kochi', 'Placed'),

(10, 4, 2, 4000, '9990000010', 'Test City', 'Delivered'),
(11, 5, 3, 4500, '9990000011', 'Test City', 'Placed');