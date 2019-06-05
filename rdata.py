## Using SQL Fiddle

##  **PostgreSQL 9.3 Schema Setup**:

    CREATE TABLE customer (
      customer_id INT PRIMARY KEY,
      first_name VARCHAR(255),
      last_name VARCHAR(255),
      email VARCHAR(255),
      created_at TIMESTAMP WITH TIME ZONE NOT NULL
    );

    CREATE TABLE purchase (
      purchase_id INT PRIMARY KEY,
      purchase_time TIMESTAMP WITH TIME ZONE NOT NULL,
      customer_id INT NOT NULL,
      FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    );

    CREATE TABLE purchase_item (
      purchase_item_id INT PRIMARY KEY,
      purchase_id INT NOT NULL,
      sku VARCHAR(255),
      quantity INT NOT NULL,
      total_amount_paid DECIMAL(10,2) NOT NULL,
      FOREIGN KEY (purchase_id) REFERENCES purchase(purchase_id)
    );

    INSERT INTO customer (customer_id, first_name, last_name, email, created_at) VALUES
      (1, 'James', 'Smith', 'jamessmith@example.com', clock_timestamp()),
      (2, 'Mary', 'Johnson', 'maryjohnson@example.com', clock_timestamp()),
      (3, 'John', 'Williams', 'johnwilliams@example.com', clock_timestamp()),
      (4, 'Patricia', 'Brown', 'patriciabrown@example.com', clock_timestamp()),
      (5, 'Michael', 'Garcia', 'michaelgarcia@example.com', clock_timestamp());

    INSERT INTO purchase (purchase_id, purchase_time, customer_id) VALUES
      (100, clock_timestamp(), 1),
      (101, clock_timestamp(), 1),
      (102, clock_timestamp(), 1),
      (103, clock_timestamp(), 2),
      (104, clock_timestamp(), 3),
      (105, clock_timestamp(), 5);

    INSERT INTO purchase_item(purchase_item_id, purchase_id, sku, quantity, total_amount_paid) VALUES
      (200, 100, 'shoe_blk_42', 3, 300),
      (201, 100, 'shoe_lace_white', 3, 2.5),
      (202, 101, 'shorts', 1, 40),
      (203, 102, 'bike', 1, 1995),
      (204, 103, 'bike', 2, 3990),
      (205, 103, 'shoe_wht_39', 2, 200),
      (206, 104, 'shirt', 1, 60),
      (207, 105, 'headphones', 1, 400);
