# Data Bank Simulator & Fraud Detection Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-orange)
![Spark](https://img.shields.io/badge/Apache%20Spark-Big%20Data-E25A1C)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Postgres](https://img.shields.io/badge/Postgres-15-336791)
![Status](https://img.shields.io/badge/Status-EDA%20Phase-yellow)

## Project Overview

This project is an end-to-end **Data Engineering & Data Science pipeline** designed to simulate, process, and analyze bank transactions in real-time.

Unlike standard datasets found on Kaggle, this project **generates its own synthetic data stream**, mimicking a real-world banking environment with injected fraud patterns (e.g., high amounts, suspicious locations). The goal is to build a robust infrastructure capable of ingesting raw data, orchestrating ETL workflows, and performing Big Data analysis.

## Tech Stack

* **Language:** Python 3.10+
* **Orchestration:** Apache Airflow (DAGs & Scheduling).
* **Big Data Processing:** PySpark (Local Standalone Cluster).
* **Containerization:** Docker & Docker Compose.
* **Database:** PostgreSQL 15.
* **Analysis & Viz:** Pandas, Matplotlib, Seaborn, Jupyter Notebooks.
* **Database Management:** Adminer.

## Key Features

* **Automated ETL Pipeline:** An Airflow DAG (`fraud_detection_dag`) that runs periodically to generate and load data.
* **Synthetic Data Generator:** Custom Python logic using `Faker` to create realistic transactions with a ~5% fraud injection rate.
* **Idempotent Architecture:** The pipeline automatically handles table creation and prevents duplicate runs.
* **Big Data Ready:** Integration of **PySpark** with JDBC drivers to process transaction logs efficiently.
* **Dockerized Environment:** One-command setup for Airflow (Webserver/Scheduler), Postgres, and Adminer.

## Architecture & Roadmap

The project has completed the Engineering Phase and is currently in the **Analysis Phase**.

- [x] **Phase 1: Infrastructure Setup** (Docker, Postgres, Airflow Containers).
- [x] **Phase 2: Data Ingestion Pipeline** (Airflow DAGs, PythonOperators, SQL Hooks).
- [x] **Phase 3: Robustness** (Error handling, Idempotency, GitFlow).
- [x] **Phase 4: Big Data Setup** (PySpark & JDBC Integration).
- [ ] **Phase 5: Exploratory Data Analysis (EDA)** (Statistical analysis of fraud patterns).
- [ ] **Phase 6: Machine Learning** (Training a classifier model).

## Getting Started

Follow these steps to run the project locally.

### Prerequisites
* Docker Desktop installed and running.
* Python 3.9 or higher.
* Java (OpenJDK 11) - *Required for PySpark*.

## Installation 
### Phase 1: Data Engineering Pipeline

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mausanram/Data_Bank_Simulator.git](https://github.com/mausanram/Data_Bank_Simulator.git)
    cd Data_Bank_Simulator
    ```

2.  **Start the Infrastructure:**
    This command spins up Postgres, Airflow (Webserver, Scheduler, Triggerer), and Adminer.
    ```bash
    docker compose up -d
    ```

3.  **Setup Local Environment (For Analysis):**
    ```bash
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

4.  **Access the Services:**
    * **Airflow UI:** `http://localhost:8080` (User: `admin` / Pass: `admin`) -> *Enable the DAG here to start generating data.*
    * **Adminer (DB View):** `http://localhost:8081`
        * **System:** PostgreSQL
        * **Server:** `postgres`
        * **User:** `admin`
        * **Password:** `admin_password`
        * **Database:** `bank_fraud_db`

5.  **Run Analysis:**
    Open the analysis notebook in VS Code or Jupyter:
    * `notebooks/fraud_analysis_spark.ipynb`

### Phase 2: Data Science & Machine Learning

After the data pipeline ingests transactions into PostgreSQL, we use **Apache Spark** for large-scale analysis and modeling.

1. Exploratory Data Analysis (EDA)
We connected PySpark to the database to analyze patterns:
- **Technique:** Spark SQL & DataFrame API.
- **Finding:** Detected strict patterns in transaction amounts and time-of-day for fraudulent activities.

2. Fraud Detection Model
We trained a Machine Learning model to classify transactions.
- **Algorithm:** Random Forest Classifier (Spark MLlib).
- **Performance:** ~99% Accuracy (Synthetic Data).
- **Features Used:** Transaction Amount, Hour of Day.

#### How to Run the Analysis
1. Ensure the Docker containers are running:
   ```bash
   docker compose up -d
   ````

2. Activate your local Python environment:
   ```bash
   source venv/bin/activate
   ```

3. Open the workspace in VS Code and open the fraud_analysis_spark.ipynb file:
   ```bash
   code .
   ```

4. Run all cells to perform ETL, Analysis, and Model Training.

---
**Author:** Mauricio Sánchez
**License:** MIT