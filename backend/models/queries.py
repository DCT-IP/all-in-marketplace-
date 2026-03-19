# Central place for queries (use later if needed)

GET_ALL_PRODUCTS = "SELECT * FROM inventory"

GET_USER_CART = """
SELECT i.product_name, sc.quantity
FROM shopping_cart sc
JOIN inventory i ON sc.product_id = i.product_id
WHERE sc.user_id = %s
"""