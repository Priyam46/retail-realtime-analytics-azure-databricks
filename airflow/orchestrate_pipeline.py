"""
Airflow DAG to orchestrate ADF -> Databricks
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "data-eng",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1)
}

def trigger_adf(**context):
    # Placeholder: in real deployment use AzureDataFactoryRunPipelineOperator
    print("Triggering ADF pipeline: ingest_historical (placeholder)")

def run_databricks_job(**context):
    # Placeholder: in real deployment use DatabricksRunNowOperator or REST API
    print("Running Databricks job: gold_aggregation (placeholder)")

def run_data_quality(**context):
    # Very small DQ check: ensure gold table exists and has rows (pseudo)
    print("Running Data Quality checks (placeholder). In real jobs, call Great Expectations or run queries.")

with DAG("retail_end_to_end_demo", schedule_interval="@hourly", default_args=default_args, catchup=False) as dag:
    t1 = PythonOperator(task_id="trigger_adf", python_callable=trigger_adf)
    t2 = PythonOperator(task_id="run_databricks_job", python_callable=run_databricks_job)
    t3 = PythonOperator(task_id="data_quality", python_callable=run_data_quality)

    t1 >> t2 >> t3
