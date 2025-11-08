"""
Aggregate silver to gold hourly KPIs using MERGE
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import date_trunc, col

spark = SparkSession.builder.appName("GoldAggregations").getOrCreate()

silver_path = "/tmp/delta/silver/transactions"
gold_path = "/tmp/delta/gold/kpis_hourly"

# Create or attach table names as needed
silver = spark.read.format("delta").load(silver_path)
silver.createOrReplaceTempView("silver_transactions")

hourly = (spark.sql("""
SELECT date_trunc('hour', ts) as dt_hour,
       store_id,
       SUM(price * quantity) as revenue,
       SUM(quantity) as units_sold,
       AVG(price) as avg_price
FROM silver_transactions
GROUP BY 1,2
"""))

# In an actual Delta table MERGE into gold
# For demo we overwrite
hourly.write.format("delta").mode("overwrite").save(gold_path)
print("Wrote gold KPIs to", gold_path)
