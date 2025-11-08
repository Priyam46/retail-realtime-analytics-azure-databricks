# 🧩 Real-Time Retail Analytics — Azure / Databricks Stack (Showcase)

![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-blue)
![PySpark](https://img.shields.io/badge/Framework-PySpark-orange)
![Airflow](https://img.shields.io/badge/Orchestrator-Airflow-lightgrey)
![Kafka](https://img.shields.io/badge/Stream-Kafka-red)

### 🚀 End-to-end data engineering project simulating real-time retail analytics using Azure Data Engineering tools.

This repository demonstrates how to build a **streaming + batch lakehouse** on Azure using **Databricks, PySpark, Kafka, ADF, and Airflow** — complete with data quality checks, orchestration, and gold-layer analytics.

---

## 🏁 Project Overview

The goal: process **real-time point-of-sale transactions** from Kafka alongside **historical batch data** using Databricks (PySpark).  
All raw data is refined through a **Bronze → Silver → Gold Delta Lake** pipeline, orchestrated with Airflow, validated with Great Expectations, and ready for BI consumption (Power BI / Synapse).

---

## 🧠 Architecture Diagram


**Data Flow Summary**
1. **Kafka Producer (Simulated POS)** → Streams JSON events (`retail.transactions`)
2. **Databricks Structured Streaming** → Consumes Kafka → Writes to Bronze Delta
3. **ADF Pipeline (Batch)** → Loads historical and master data into Bronze
4. **Databricks Batch Jobs (PySpark)** → Clean, join, aggregate → Silver & Gold
5. **Airflow DAG** → Orchestrates ADF + Databricks + DQ checks
6. **Great Expectations** → Validates Silver data quality
7. **Power BI / Synapse** → Visualize KPIs from Gold Delta

---

## 🧩 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Ingestion** | Kafka / Event Hubs | Real-time streaming |
| **Batch Load** | Azure Data Factory | Historical ingestion |
| **Processing** | Databricks (PySpark) | Stream & batch ETL |
| **Storage** | ADLS Gen2 + Delta Lake | Bronze / Silver / Gold |
| **Orchestration** | Apache Airflow | End-to-end automation |
| **Data Quality** | Great Expectations | Validation |
| **Analytics** | Power BI / Synapse | Reporting & KPIs |

---

