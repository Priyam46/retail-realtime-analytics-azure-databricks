# Real-Time Retail Analytics — Azure / Databricks Stack (Showcase)

Retail lakehouse that ingests simulated POS events (Kafka), processes streaming + batch in Databricks (PySpark), organizes a bronze→silver→gold Delta architecture, and is orchestrated with Airflow + ADF.


## What’s included
- Kafka producer script (simulated POS events)
- Databricks PySpark notebooks for streaming ingestion, transformations, and Gold aggregation
- Airflow DAG to orchestrate ADF + Databricks flows (placeholders for connection IDs)
- Example ADF pipeline JSON (pseudo-template)
- Great Expectations sample suite
- Sample data (products, stores, historical transactions)
- Architecture diagram (see `architecture.md`)
- Demo script and interview notes

---

## Quick file map & purpose
- `kafka/producer.py` — POS events  
- `databricks/notebooks/` — PySpark scripts  for Databricks notebooks
- `airflow/dags/orchestrate_pipeline.py` — orchestrator DAG 
- `adf/ingest_historical_pipeline.json` — sample pipeline export 
- `tests/great_expectations/` — simple data quality suite
- `sample_data/` — small CSVs to run quick demos

---


## Notes
- This repo is demonstrative. Files use placeholders for credentials and endpoints.
- If you want, I can generate a GitHub Actions workflow that lints and validates Python files before publishing.

---
