from pyspark.sql import SparkSession
from pyspark import SparkFiles
import time

# Create a SparkSession
spark = SparkSession.builder.appName("Export Tables to S3").getOrCreate()

# Replace with your S3 bucket name and folder path
s3_bucket_name = "your-s3-bucket-name"
s3_folder_path = "path/to/folder"

# List of table names
table_names = [
    "catalog.schema.table1",
    "catalog.schema.table2",
    # Add more table names here
]

for table_name in table_names:
    # Create a temporary view from the table
    spark.sql(f"CREATE OR REPLACE TEMP VIEW temp_table_view AS SELECT * FROM {table_name}")

    # Generate a timestamp for the file name
    timestamp = int(time.time())

    # Construct the output file name
    output_file_name = f"{table_name.split('.')[-1]}_{timestamp}.csv"

    # Create the S3 output path
    s3_output_path = f"s3://{s3_bucket_name}/{s3_folder_path}/{output_file_name}"

    # Write the data to S3 as CSV
    (
        spark.table("temp_table_view")
        .coalesce(1)  # Adjust the number of output files
        .write.format("csv")
        .mode("overwrite")
        .option("header", "true")
        .save(s3_output_path)
    )

    print(f"Data from {table_name} exported to {s3_output_path}")

# Stop the SparkSession
spark.stop()