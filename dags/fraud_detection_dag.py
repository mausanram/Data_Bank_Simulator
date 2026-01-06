from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import random
import psycopg2
from faker import Faker

# --- CONFIGURATION ---
DB_HOST = "postgres"        # We use "postgres" as the host because Airflow is running inside the Docker network.
DB_PORT = "5432"
DB_NAME = "bank_fraud_db"
DB_USER = "admin"
DB_PASSWORD = "admin_password"

# Default arguments for the DAG
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def generate_and_load_transactions():
    """
    Generates a batch of synthetic transactions and loads them into PostgreSQL.
    This function mimics a data ingestion process.
    """
    print("==== STARTING BATCH DATA GENERATION ====")
    fake = Faker()
    
    try:
        # Establish connection to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()

        ## We create the table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(50) PRIMARY KEY,
            client_id INTEGER,
            transaction_date TIMESTAMP,
            amount DECIMAL(10, 2),
            merchant VARCHAR(100),
            location VARCHAR(100),
            is_fraud BOOLEAN
        );
        """
        cur.execute(create_table_query)

        # Batch size: Generate 50 transactions per run
        # In a real scenario, this could be fetching data from an API
        for _ in range(50):
            # Fraud Logic: 5% probability
            is_fraud = random.random() < 0.05
            
            transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Simulate patterns: Fraudsters spend more, often in foreign countries
            if is_fraud:
                amount = round(random.uniform(5000.00, 20000.00), 2)
                location = fake.country()
            else:
                amount = round(random.uniform(10.00, 500.00), 2)
                location = "Mexico"
            
            # Prepare data dictionary
            data = {
                "transaction_id": fake.uuid4(),
                "client_id": fake.random_int(min=1000, max=9999),
                "date": transaction_date,
                "amount": amount,
                "merchant": fake.company(),
                "location": location,
                "is_fraud": is_fraud
            }
            
            # SQL Insert Query
            insert_query = """
                INSERT INTO transactions 
                (transaction_id, client_id, transaction_date, amount, merchant, location, is_fraud)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            # Execute insert
            cur.execute(insert_query, (
                data['transaction_id'], 
                data['client_id'], 
                data['date'], 
                data['amount'], 
                data['merchant'], 
                data['location'], 
                data['is_fraud']
            ))
        
        # Commit the transaction batch
        conn.commit()
        cur.close()
        conn.close()
        print(" Batch of 50 transactions inserted successfully.")
        
    except Exception as e:
        print(f" Critical Error: {e}")
        # Raising the exception ensures Airflow marks the task as FAILED
        raise e

# --- DAG DEFINITION ---
with DAG(
    dag_id='bank_fraud_simulation_pipeline',
    default_args=default_args,
    description='ETL pipeline to generate synthetic banking data every 2 minutes',
    # Start date is in the past so it can run immediately
    start_date=datetime(2023, 1, 1), 
    # CRON expression: Run every 2 minutes
    schedule_interval='*/2 * * * *', 
    catchup=False, 
    tags=['finance', 'simulation', 'etl'],
) as dag:

    # Define the task using PythonOperator
    run_simulation_task = PythonOperator(
        task_id='generate_mock_transactions',
        python_callable=generate_and_load_transactions
    )

    # Task flow (single task for now)
    run_simulation_task