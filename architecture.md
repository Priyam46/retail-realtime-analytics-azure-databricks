# Architecture Diagram (ASCII / Mermaid)

This is the Architecture for the project
```mermaid
flowchart TD
  A[POS devices] -->|events| K(Kafka topic)
  K --> D[Databricks Structured Streaming]
  D --> ADLS[(ADLS Gen2)]
  ADLS --> DB_Silver[Databricks Silver Tables]
  DB_Silver --> DB_Gold[Databricks Gold / Delta Tables]
  DB_Gold --> Databricks[(Databricks SQL)]
  Airflow -->|orchestrates| ADF[Azure Data Factory]
  Airflow --> Databricks
  ADF --> ADLS
  subgraph Observability
    AirflowLogs --> Alerts[Email]
    DQ[Great Expectations] --> ADLS
  end
