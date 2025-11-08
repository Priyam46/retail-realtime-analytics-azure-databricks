"""
Batch job to convert bronze -> silver: cleaning, typing, joins to master data.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder.appName("BronzeToSilver").getOrCreate()

bronze_path = "/tmp/delta/bronze/transactions"
silver_path = "/tmp/delta/silver/transactions"
products_path = "sample_data/products.csv"
stores_path = "sample_data/stores.csv"

# Read bronze (delta)
bronze = spark.read.format("delta").load(bronze_path)

# Load master data from CSVs (sample)
products = spark.read.option("header", True).csv(products_path)
stores = spark.read.option("header", True).csv(stores_path)

# Basic cleaning and typing
silver = (bronze
          .withColumn("product_id", trim(col("product_id")))
          .withColumn("store_id", trim(col("store_id")))
          .na.fill({"loyalty_id": None})
         )

# Join to enrich
silver_enriched = (silver
                   .join(products, on="product_id", how="left")
                   .join(stores, on="store_id", how="left"))

# Write silver Delta (overwrite small demo; in prod use MERGE for incremental)
silver_enriched.write.format("delta").mode("overwrite").save(silver_path)
print("Wrote silver to", silver_path)
