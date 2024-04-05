from pyspark import SparkFiles

# Replace with your S3 bucket name and folder path
s3_bucket_name = "your-s3-bucket-name"
s3_folder_path = "path/to/folder"

# Create the S3 output path
s3_output_path = f"s3://{s3_bucket_name}/{s3_folder_path}"

# Write the data to S3 as CSV
(
    spark.table("temp_table_view")
    .coalesce(1)  # Adjust the number of output files
    .write.format("csv")
    .mode("overwrite")
    .option("header", "true")
    .save(s3_output_path)
)