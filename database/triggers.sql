DELIMITER $$

CREATE TRIGGER check_stock_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE stock INT;

    SELECT item_count INTO stock
    FROM inventory
    WHERE product_id = NEW.product_id;

    IF stock <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Out of stock!';
    END IF;
END$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER reduce_stock_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE inventory
    SET item_count = item_count - 1
    WHERE product_id = NEW.product_id;
END$$

DELIMITER ;