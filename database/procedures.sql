DELIMITER $$

CREATE PROCEDURE place_order(IN p_user INT, IN p_product INT)
BEGIN
    INSERT INTO orders(user_id, product_id)
    VALUES (p_user, p_product);

    UPDATE users
    SET last_item_purchased = p_product
    WHERE user_id = p_user;
END$$

DELIMITER ;