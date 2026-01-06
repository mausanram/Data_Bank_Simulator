# Data Bank Simulator & Fraud Detection Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Postgres](https://img.shields.io/badge/Postgres-15-336791)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Project Overview

This project is an end-to-end Data Engineering pipeline designed to simulate, process, and analyze bank transactions in real-time. 

Unlike standard datasets found on Kaggle, this project generates its own synthetic data stream, mimicking a real-world banking environment with normal transactions and injected fraud patterns (e.g., high amounts, suspicious locations). The goal is to build a robust infrastructure capable of ingesting raw data, storing it efficiently, and preparing it for Machine Learning fraud detection models.

## Tech Stack

* **Language:** Python 3.9+ (Faker for data generation).
* **Containerization:** Docker & Docker Compose.
* **Database:** PostgreSQL 15.
* **Database Management:** Adminer (Lightweight DB client).
* **Version Control:** Git & GitHub (GitFlow strategy).

## Key Features

* **Synthetic Data Generator:** A custom Python script that creates realistic user transactions (JSON format) with randomized attributes.
* **Fraud Injection:** Logic to deliberately inject anomalies (5% probability) to train future ML models.
* **Dockerized Infrastructure:** One-command setup for the Database and Management tools using `docker-compose`.

## Architecture & Roadmap

The project is currently in the **Ingestion Phase**.

- [x] **Phase 1: Infrastructure Setup** (Docker, PostgreSQL, Git Configuration).
- [ ] **Phase 2: Data Ingestion** (Python Script connecting to DB).
- [ ] **Phase 3: Orchestration** (Automating the flow with Apache Airflow).
- [ ] **Phase 4: Transformation** (Data cleaning and aggregation).
- [ ] **Phase 5: Visualization & ML** (Dashboarding and Fraud Prediction).

## Getting Started

Follow these steps to run the project locally.

### Prerequisites
* Docker Desktop installed and running.
* Python 3.9 or higher.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mausanram/Data_Bank_Simulator.git](https://github.com/mausanram/Data_Bank_Simulator.git)
    cd Data_Bank_Simulator
    ```

2.  **Start the Infrastructure:**
    ```bash
    docker-compose up -d
    ```

3.  **Access the Database:**
    * Open your browser at `http://localhost:8080` (Adminer).
    * **System:** PostgreSQL
    * **Server:** `postgres`
    * **User:** `admin`
    * **Password:** `admin_password`
    * **Database:** `bank_fraud_db`

4.  **Run the Simulation (Local Test):**
    ```bash
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
    
    # Install dependencies
    pip install faker
    
    # Run generator
    python transaction_generator.py
    ```

---
**Author:** Mauricio Sánchez  
**License:** MIT