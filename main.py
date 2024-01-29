#main

import sqlite3
import crud

db = sqlite3.connect("shop.db")

db.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
''')

db.execute('''CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE );''')

db.execute('''CREATE TABLE IF NOT EXISTS orders ( 
           order_id INTEGER PRIMARY KEY, 
           customer_id INT NOT NULL, 
           product_id INTEGER NOT NULL, 
           quantity INTEGER NOT NULL, 
           order_date DATE NOT NULL, 
           FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
           FOREIGN KEY (product_id) REFERENCES products(product_id) );''')


while True:
        print('''
Що ви хочете зробити?

1 - Додавання продуктів:
2 - Додавання клієнтів:
3 - Замовлення товарів:
4 - Сумарний обсяг продажів:
5 - Кількість замовлень на кожного клієнта:
6 - Середній чек замовлення:
7 - Найбільш популярна категорія товарів:
8 - Загальна кількість товарів кожної категорії:
9 - Оновлення цін категорії на 10% більші:
10 - Показати усіх користувачів
11 - Показати усі продукти
12 - Показати усі замовлення(Joined)
0 - Вийти:

        ''')
        command = int(input("Оберіть ваші дії: "))
        if command == 1:
            name = input("Input product's name")
            category = input("Input category")
            price = int(input("Input price"))
            crud.add_product(db, name, category, price)
            print(f"product {name} added successfully")

        if command == 2:
            first_name = input("f")
            last_name = input("a")
            email = input("p")
            crud.add_client(db, first_name, last_name, email)

        if command == 3:
            customer_id = int(input("Input customer id"))
            product_id = int(input("Input product id"))
            quantity = int(input("Input quantity"))
            crud.make_order(db, customer_id, product_id, quantity)

        if command == 4:
            print(crud.get_total_income(db))

        if command == 5:
            print(crud.count_orders_by_customer_id(db))

        if command == 6:
            print(crud.avg_bill(db))

        if command == 7:
            print(crud.the_most_popular_product_category(db))
        
        if command == 9:
            crud.increase_value_of_phones_by_10_percents(db)

        if command == 10:
            print(crud.show_all_customers(db))

        if command == 11:
            print(crud.show_all_products(db))

        if command == 12:
            print(crud.show_all_orders(db))