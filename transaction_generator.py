import time
import random
import os
import psycopg2
from faker import Faker
from datetime import datetime

# --- CONFIGURATION ---
DB_HOST = "localhost"
DB_PORT = "5434" # Target local port 5434 which maps to Docker's 5432
DB_NAME = "bank_fraud_db"
DB_USER = "admin"
DB_PASSWORD = "admin_password"

# Initialize Faker
fake = Faker()

def get_db_connection():
    """Establishes connection to PostgreSQL database"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f" Error connecting to DB: {e}")
        return None

def create_table_if_not_exists(conn):
    """Creates the transactions table structure if it doesn't exist"""
    try:
        cur = conn.cursor()
        # SQL to create the table
        sql_create = """
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id VARCHAR(50) PRIMARY KEY,
                client_id INT,
                transaction_date TIMESTAMP,
                amount DECIMAL(10, 2),
                merchant VARCHAR(100),
                location VARCHAR(100),
                is_fraud BOOLEAN
            );
        """
        cur.execute(sql_create)
        conn.commit()
        cur.close()
        print(" Table 'transactions' verified successfully.")
    except Exception as e:
        print(f" Error creating table: {e}")

def insert_transaction(conn, data):
    """Inserts a single row of data into the DB"""
    try:
        cur = conn.cursor()
        sql_insert = """
            INSERT INTO transactions 
            (transaction_id, client_id, transaction_date, amount, merchant, location, is_fraud)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql_insert, (
            data['transaction_id'], 
            data['client_id'], 
            data['date'], 
            data['amount'], 
            data['merchant'], 
            data['location'], 
            data['is_fraud']
        ))
        conn.commit()
        cur.close()
        print(f" Transaction inserted: {data['transaction_id']} | Fraud: {data['is_fraud']}")
    except Exception as e:
        print(f" Error inserting data: {e}")

def generate_fake_data():
    """Generates a dictionary with synthetic banking data"""

    is_fraud = random.random() < 0.05 # 5% probability of fraud
    
    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # If fraud, high amounts and suspicious locations. Else, normal amounts and Mexico.
    if is_fraud:
        amount = round(random.uniform(5000.00, 20000.00), 2)
        location = fake.country()
    else:
        amount = round(random.uniform(10.00, 500.00), 2)
        location = "Mexico"

    return {
        "transaction_id": fake.uuid4(),
        "client_id": fake.random_int(min=1000, max=9999),
        "date": transaction_date,
        "amount": amount,
        "merchant": fake.company(),
        "location": location,
        "is_fraud": is_fraud
    }

if __name__ == "__main__":
    print("==== STARTING BANKING SIMULATOR ===")
    conn = get_db_connection()
    
    if conn:
        create_table_if_not_exists(conn)
        
        try:
            while True:
                fake_data = generate_fake_data()
                insert_transaction(conn, fake_data)
                time.sleep(1) # Wait 1 second between transactions
        except KeyboardInterrupt:
            print("\n Simulator STOPPED by user.")
            conn.close()
    else:
        print("FAILED to connect to database. Is Docker running?")