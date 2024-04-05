from pyspark.sql import SparkSession
from pyspark import SparkFiles
import time
import boto3

# AWS credentials
aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID"
aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"

# Create a Boto3 session with your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Create a SparkSession
spark = (
    SparkSession.builder
    .appName("Export Tables to S3")
    .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id)
    .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key)
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
    .getOrCreate()
)

# ... (the rest of your code remains the same)