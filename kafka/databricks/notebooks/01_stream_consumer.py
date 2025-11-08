"""
read from Kafka, write to Delta Bronze.
Adapt connection options for Databricks or local Spark + Kafka.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType, TimestampType

spark = SparkSession.builder.appName("StreamConsumer").getOrCreate()

kafka_bootstrap = "localhost:9092"   
topic = "retail.transactions"
checkpoint = "/tmp/delta/checkpoints/retail/bronze"
bronze_path = "/tmp/delta/bronze/transactions"

schema = StructType() \
  .add("transaction_id", StringType()) \
  .add("store_id", StringType()) \
  .add("product_id", StringType()) \
  .add("ts", StringType()) \
  .add("quantity", IntegerType()) \
  .add("price", DoubleType()) \
  .add("payment_type", StringType()) \
  .add("loyalty_id", StringType())

kafka_df = (spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", kafka_bootstrap)
            .option("subscribe", topic)
            .option("startingOffsets", "latest")
            .load())

parsed = (kafka_df.selectExpr("CAST(value AS STRING) as json_str")
          .select(from_json(col("json_str"), schema).alias("data"))
          .select("data.*")
          .withColumn("ts", to_timestamp(col("ts"))))

# Simple dedupe with watermark + dropDuplicates on transaction_id
deduped = (parsed
           .withWatermark("ts", "10 minutes")
           .dropDuplicates(["transaction_id"]))

query = (deduped.writeStream
         .format("delta")
         .option("checkpointLocation", checkpoint)
         .outputMode("append")
         .option("path", bronze_path)
         .start())

print("Started streaming query to bronze path:", bronze_path)
query.awaitTermination()
