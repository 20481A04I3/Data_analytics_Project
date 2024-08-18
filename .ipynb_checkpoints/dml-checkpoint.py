import mysql.connector
from mysql.connector import Error

def insert_customers(cursor, customers_values):
    """
    Inserts values into the Customers table.
    """
    query = """
    INSERT INTO Customers (customer_name, country, city)
    VALUES ( %s, %s, %s)
    """
    try:
        cursor.executemany(query, customers_values)
        print("Customers inserted successfully.")
    except Error as err:
        print(f"Error: {err}")

def insert_products(cursor, products_values):
    """
    Inserts values into the Products table.
    """
    query = """
    INSERT INTO Products (product_name, product_category)
    VALUES (%s, %s)
    """
    try:
        cursor.executemany(query, products_values)
        print("Products inserted successfully.")
    except Error as err:
        print(f"Error: {err}")

def insert_ecommerce_websites(cursor, ecommerce_websites_values):
    """
    Inserts values into the EcommerceWebsites table.
    """
    query = """
    INSERT INTO EcommerceWebsites (ecommerce_website_name)
    VALUES (%s)
    """
    try:
        cursor.executemany(query, ecommerce_websites_values)
        print("Ecommerce websites inserted successfully.")
    except Error as err:
        print(f"Error: {err}")

def insert_payment_types(cursor, payment_types_values):
    """
    Inserts values into the PaymentTypes table.
    """
    query = """
    INSERT INTO PaymentTypes (payment_txn_id, payment_txn_success, failure_reason)
    VALUES (%s, %s, %s)
    """
    try:
        cursor.executemany(query, payment_types_values)
        print("Payment types inserted successfully.")
    except Error as err:
        print(f"Error: {err}")


def insert_transactions(cursor, transactions_values):
    """
    Inserts values into the Transactions table.
    """
    query = """
    INSERT INTO Transactions (
        customer_id, product_id, qty, price, datetime,
        ecommerce_website_id, payment_txn_id
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.executemany(query, transactions_values)
        print("Transactions inserted successfully.")
    except Error as err:
        print(f"Error: {err}")



def update_customer_city(cursor, new_city, customer_id):
    """
    Updates the city for a given customer ID.
    """
    query = """
    UPDATE Customers
    SET city = %s
    WHERE customer_id = %s
    """
    try:
        cursor.execute(query, (new_city, customer_id))
        print(f"City updated successfully for customer ID {customer_id}.")
    except Error as err:
        print(f"Error: {err}")

def delete_failed_transactions(cursor):
    """
    Deletes transactions where payment was not successful.
    """
    query = """
    DELETE FROM Transactions
    WHERE payment_txn_success = FALSE
    """
    try:
        cursor.execute(query)
        print("Failed transactions deleted successfully.")
    except Error as err:
        print(f"Error: {err}")


# Existing insert and update functions go here...

def delete_customer(cursor, customer_id):
    """
    Deletes a customer with the specified customer_id.
    """
    query = """
    DELETE FROM Customers
    WHERE customer_id = %s
    """
    try:
        cursor.execute(query, (customer_id,))
        print(f"Customer with ID {customer_id} deleted successfully.")
    except Error as err:
        print(f"Error: {err}")

def delete_product(cursor, product_id):
    """
    Deletes a product with the specified product_id.
    """
    query = """
    DELETE FROM Products
    WHERE product_id = %s
    """
    try:
        cursor.execute(query, (product_id,))
        print(f"Product with ID {product_id} deleted successfully.")
    except Error as err:
        print(f"Error: {err}")

