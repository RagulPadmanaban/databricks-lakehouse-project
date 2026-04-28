# Databricks notebook source
#Importing the packages

from pyspark.sql.functions import *
from pyspark.sql.functions import col, when, lit, max

# COMMAND ----------

#Creating dictionary for the columns need to add in the metadata.Only used for the first run alone.

data = [("1","customer_orders", "raw/customer_orders", "2024-01-01", "silver_customer_orders")]
cols=["Sno","table_name","source_path","last_processed_date","target_table"]
metadata=spark.createDataFrame(data, cols)
metadata.write.mode("overwrite").parquet("dbfs:/Volumes/workspace/default/my_volume/Metadata")

# COMMAND ----------

#Reading the metadata dataset

metadata=spark.read.parquet("dbfs:/Volumes/workspace/default/my_volume/Metadata")

# COMMAND ----------

#Collecting the metadata

row=metadata.collect()[0]

source_path=row["source_path"]
last_date=row["last_processed_date"]
target_table=row["target_table"]



# COMMAND ----------

#Reading the csv file and filtering the incremental data based on the last date.

df=spark.read.csv(f"dbfs:/Volumes/workspace/default/my_volume/{source_path}.csv", header=True, inferSchema=True)
df=df.filter(f"order_date> '{last_date}'")

# COMMAND ----------

#Writing the incremental data to the silver table

df.write.format("delta").mode("append").save(f"dbfs:/Volumes/workspace/default/my_volume/silver/{target_table}")

# COMMAND ----------

#Perform upsert on the target using merge statement to load the data incremental or update the data.

from delta.tables import DeltaTable

delta_table=DeltaTable.forPath(spark, f"dbfs:/Volumes/workspace/default/my_volume/silver/{target_table}")

delta_table.alias("t").merge(
    df.alias("s"),"t.order_id =s.order_id") \
        .whenMatchedUpdateAll() \
            .whenNotMatchedInsertAll() \
                .execute()

# COMMAND ----------

#Updating the metadata table

# Step 1: Check if incremental data exists
if df.count() > 0:

    # Step 2: Get max date from new data
    new_date = df.select(max("order_date")).collect()[0][0]

    # Step 3: Update only the required table row
    metadata_updated = metadata.withColumn(
        "last_processed_date",
        when(col("table_name") == "customer_orders", lit(new_date))
        .otherwise(col("last_processed_date"))
    )

    # Step 4: Overwrite metadata table
    metadata_updated.write.mode("overwrite") \
        .parquet("dbfs:/Volumes/workspace/default/my_volume/Metadata")

    print(f"Metadata updated with new date: {new_date}")

else:
    print("No new data found. Metadata not updated.")

# COMMAND ----------

