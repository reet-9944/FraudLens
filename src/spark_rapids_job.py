# Spark RAPIDS Fraud Detection Job

"""A Spark job that runs on Google Cloud Managed Spark (Dataproc) using the RAPIDS Accelerator.
It reads raw transaction CSV from Google Cloud Storage, performs the same feature‑engineering
steps as the pandas/RAPIDS benchmark, and writes the enriched table to BigQuery.

The job can be submitted with `spark-submit` (Dataproc) and the RAPIDS plugin must be
installed on the cluster (e.g., `--properties spark.plugins=org.apache.rapids:rapids-4-spark_2.12:23.12.0`).
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, hour, dayofweek, avg, stddev, max, count

# ------------------------------------------------------------
# Configuration (replace placeholders with your GCP values)
# ------------------------------------------------------------
GCS_INPUT = "gs://YOUR_BUCKET/raw/transactions.csv"  # <-- update
BQ_OUTPUT_DATASET = "fraud_dataset"
BQ_OUTPUT_TABLE = "transactions_enriched"

# ------------------------------------------------------------
# Spark session – the RAPIDS plugin provides GPU acceleration.
# ------------------------------------------------------------
spark = (
    SparkSession.builder.appName("FraudLensRAPIDS")
    # Enable RAPIDS accelerator (the Dataproc cluster should have it installed)
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")
    .getOrCreate()
)

# ------------------------------------------------------------
# Load the raw CSV (it can be huge; Spark will read it in parallel).
# ------------------------------------------------------------
raw_df = spark.read.option("header", "true").csv(GCS_INPUT)

# ------------------------------------------------------------
# Basic type casting
# ------------------------------------------------------------
df = (
    raw_df
    .withColumn("amount", col("amount").cast("double"))
    .withColumn("timestamp", col("timestamp").cast("timestamp"))
    .withColumn("user_id", col("user_id").cast("long"))
    .withColumn("merchant_id", col("merchant_id").cast("long"))
)

# ------------------------------------------------------------
# Feature engineering (mirrors the pandas pipeline)
# ------------------------------------------------------------
user_stats = (
    df.groupBy("user_id")
    .agg(
        avg("amount").alias("user_mean_amt"),
        stddev("amount").alias("user_std_amt"),
        max("amount").alias("user_max_amt"),
        count("transaction_id").alias("user_txn_count"),
    )
)

enriched = df.join(user_stats, on="user_id", how="left")

enriched = (
    enriched
    .withColumn("hour", hour(col("timestamp")))
    .withColumn("day_of_week", dayofweek(col("timestamp")))
)

# ------------------------------------------------------------
# Write the enriched data back to BigQuery (fast load). The
# Dataproc service account must have the BigQuery Data Editor role.
# ------------------------------------------------------------
(enriched.write.format("bigquery")
    .option("temporaryGcsBucket", "YOUR_TEMP_BUCKET")  # <-- update
    .option("table", f"{BQ_OUTPUT_DATASET}.{BQ_OUTPUT_TABLE}")
    .mode("overwrite")
    .save())

spark.stop()
