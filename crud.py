#crud

import sqlite3

def add_product(db, name: str, category: str, price: int):
    db.execute('''INSERT INTO products (name, category, price)
               VALUES(?, ?, ?);''', (name, category, price))
    db.commit()

def add_client(db, first_name: str, last_name: str, email: str):
    db.execute('''INSERT INTO customers (first_name, last_name, email)
               VALUES(?, ?, ?);''', (first_name, last_name, email))
    db.commit()

def make_order(db, customer_id: int, product_id: int, quantity: int):
    db.execute('''INSERT INTO orders (customer_id, product_id, quantity, order_date)
               VALUES(?, ?, ?, CURRENT_TIMESTAMP)''', (customer_id, product_id, quantity))
    db.commit()

def get_total_income(db):
    r = db.execute('''SELECT SUM(products.price * orders.quantity) AS total_bill
               FROM orders
               INNER JOIN products ON orders.order_id = products.product_id
               ''')
    return r.fetchone()

def count_orders_by_customer_id(db):
    r = db.execute('''SELECT customers.first_name AS customer_name, COUNT(orders.order_id) AS amount_of_orders
               FROM orders
               INNER JOIN customers ON customers.customer_id = orders.customer_id
               GROUP BY customers.first_name
               ORDER BY customers.customer_id ASC''')
    return r.fetchall()

def avg_bill(db):
    r = db.execute('''SELECT AVG(products.price * orders.quantity) AS avg_bill
                   FROM orders
                   INNER JOIN products ON orders.order_id = products.product_id
                   ''')
    return r.fetchone()

def the_most_popular_product_category(db):
    r = db.execute('''SELECT products.category, SUM(orders.quantity) AS total_order_quantity
                   FROM orders
                   INNER JOIN products ON orders.product_id = products.product_id
                   GROUP BY products.category
                   ORDER BY total_order_quantity DESC''')
    return r.fetchone()[0]

def increase_value_of_phones_by_10_percents(db):
    db.execute('''UPDATE products
                SET price = price * 1.1
                WHERE category = "Phones"''')
    
def show_all_customers(db):
    r = db.execute('''SELECT first_name, last_name FROM customers''')
    return r.fetchall()

def show_all_products(db):
    r = db.execute('''SELECT name FROM products''')
    return r.fetchall()

def show_all_orders(db):
    r = db.execute('''SELECT * FROM orders''')
    return r.fetchall()