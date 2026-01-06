# Data Bank Simulator & Fraud Detection Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-orange)
![Spark](https://img.shields.io/badge/Apache%20Spark-Big%20Data-E25A1C)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Postgres](https://img.shields.io/badge/Postgres-15-336791)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Project Overview

This project is an end-to-end **Data Engineering & Data Science pipeline** designed to simulate, process, and analyze bank transactions in real-time.

Unlike standard datasets found on Kaggle, this project **generates its own synthetic data stream**, mimicking a real-world banking environment with injected fraud patterns (e.g., high amounts, suspicious locations). The goal is to build a robust infrastructure capable of ingesting raw data, orchestrating ETL workflows, performing Big Data analysis, and training Machine Learning models.

## Tech Stack

* **Language:** Python 3.10+
* **Orchestration:** Apache Airflow (DAGs & Scheduling).
* **Big Data Processing:** PySpark (SQL & MLlib).
* **Machine Learning:** Random Forest Classifier.
* **Containerization:** Docker & Docker Compose.
* **Database:** PostgreSQL 15.
* **Analysis & Viz:** Pandas, Matplotlib, Seaborn, Jupyter Notebooks.
* **Database Management:** Adminer.

## Key Features

* **Automated ETL Pipeline:** An Airflow DAG (`fraud_detection_dag`) that runs periodically to generate and load data.
* **Synthetic Data Generator:** Custom Python logic using `Faker` to create realistic transactions with a ~5% fraud injection rate.
* **Idempotent Architecture:** The pipeline automatically handles table creation and prevents duplicate runs.
* **Big Data Ready:** Integration of **PySpark** with JDBC drivers to process transaction logs efficiently.
* **ML Fraud Detection:** A persistent Random Forest model trained to detect anomalies in transaction patterns.
* **Dockerized Environment:** One-command setup for Airflow (Webserver/Scheduler), Postgres, and Adminer.

## Architecture & Roadmap

The project has completed the Engineering and Analysis phases.

- [x] **Phase 1: Infrastructure Setup** (Docker, Postgres, Airflow Containers).
- [x] **Phase 2: Data Ingestion Pipeline** (Airflow DAGs, PythonOperators, SQL Hooks).
- [x] **Phase 3: Robustness** (Error handling, Idempotency, GitFlow).
- [x] **Phase 4: Big Data Setup** (PySpark & JDBC Integration).
- [x] **Phase 5: Exploratory Data Analysis (EDA)** (Statistical analysis of fraud patterns).
- [x] **Phase 6: Machine Learning** (Training and saving a classifier model).

## Data Science Results

After ingesting data into PostgreSQL, we used **Apache Spark** for large-scale analysis and modeling.

### 1. Exploratory Data Analysis (EDA)
Using Spark SQL and Seaborn, we identified clear patterns distinguishing legitimate vs. fraudulent transactions:
- **Amount:** Fraudulent transactions consistently showed higher amounts (Avg ~13k MXN) compared to legitimate ones (<1k MXN).
- **Time:** A strict temporal pattern emerged; frauds occurred exclusively between **04:00 and 21:00**, with a peak in activity during early morning hours.

### 2. Fraud Detection Model
We trained a supervised Machine Learning model to automate detection.
- **Algorithm:** Random Forest Classifier (Spark MLlib).
- **Performance:** **~99% Accuracy** (on synthetic test data).
- **Features Used:** Transaction Amount, Hour of Day.
- **Outcome:** The model is serialized and saved in the `models/` directory for inference.

---

## Installation & Usage

Follow these steps to run the full pipeline locally.

### Prerequisites
* Docker Desktop installed and running.
* Python 3.9 or higher.
* Java (OpenJDK 11) - *Required for PySpark*.

### Step 1: Clone and Start Infrastructure
```bash
git clone [https://github.com/mausanram/Data_Bank_Simulator.git](https://github.com/mausanram/Data_Bank_Simulator.git)
cd Data_Bank_Simulator

# Start Postgres, Airflow, and Adminer
sudo docker-compose up -d
```
### Step 2: Setup Local Environment
This is required to run the Jupyter Notebooks and Spark driver locally.

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.tx
```

### Step 3: Generate Data (ETL)
1. Go to **Airflow UI**: `http://localhost:8080` (User: `admin` / Pass: `admin`).
2. Toggle the `fraud_detection_dag` to **ON**.
3. Trigger the DAG manually to generate the first batch of transactions.

### Step 4: Run Analysis & Machine Learning
Open the main notebook to execute the Spark analysis and train the model.

```bash
# Open the project in VS Code
code .
```
Navigate to notebooks/fraud_analysis_spark.ipynb and run all cells.

### Access Services
* **Airflow UI:** `http://localhost:8080`
* **Adminer (DB View):** `http://localhost:8081`
    * **System:** PostgreSQL | **Server:** `postgres` | **User:** `admin` | **Pass:** `admin_password` | **DB:** `bank_fraud_db`

---
**Author:** Mauricio Sánchez
**License:** MIT