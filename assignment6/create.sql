########################################
# MySQL Crash Course
# http://www.forta.com/books/0672327120/
# Example table creation scripts
########################################

# Modified by mkzia@buffalo.edu to work with sqlite3


########################
# Create customers table
########################
CREATE TABLE customers
(
  cust_id      INTEGER       NOT NULL PRIMARY KEY,
  cust_name    TEXT  NOT NULL ,
  cust_address TEXT  NULL ,
  cust_city    TEXT  NULL ,
  cust_state   TEXT   NULL ,
  cust_zip     TEXT  NULL ,
  cust_country TEXT  NULL ,
  cust_contact TEXT  NULL ,
  cust_email   TEXT NULL 
);


#####################
# Create orders table
#####################
CREATE TABLE orders
(
  order_num  INTEGER      NOT NULL PRIMARY KEY,
  order_date TEXT NOT NULL ,
  cust_id    INTEGER      NOT NULL ,
  FOREIGN KEY (cust_id) REFERENCES customers (cust_id)
);



######################
# Create vendors table
######################
CREATE TABLE vendors
(
  vend_id      INTEGER    NOT NULL PRIMARY KEY,
  vend_name    TEXT NOT NULL ,
  vend_address TEXT NULL ,
  vend_city    TEXT NULL ,
  vend_state   TEXT  NULL ,
  vend_zip     TEXT NULL ,
  vend_country TEXT NULL
);

#######################
# Create products table
#######################
CREATE TABLE products
(
  prod_id    TEXT      NOT NULL PRIMARY KEY,
  vend_id    INTEGER   NOT NULL ,
  prod_name  TEXT      NOT NULL ,
  prod_price REAL     NOT NULL ,
  prod_desc  TEXT      NULL,
  FOREIGN KEY (vend_id) REFERENCES vendors (vend_id)
);

#########################
# Create orderitems table
#########################
CREATE TABLE orderitems
(
  order_num  INTEGER          NOT NULL ,
  order_item INTEGER          NOT NULL ,
  prod_id    TEXT     NOT NULL ,
  quantity   INTEGER          NOT NULL ,
  item_price REAL NOT NULL ,
  PRIMARY KEY (order_num, order_item),
  FOREIGN KEY (order_num) REFERENCES orders (order_num),
  FOREIGN KEY (prod_id) REFERENCES products (prod_id)
);


###########################
# Create productnotes table
###########################
CREATE TABLE productnotes
(
  note_id    INTEGER           NOT NULL PRIMARY KEY,
  prod_id    TEXT      NOT NULL,
  note_date  TEXT       NOT NULL,
  note_text  TEXT          NULL
);

