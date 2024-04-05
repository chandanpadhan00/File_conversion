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

# Create a SparkSession with the AWS credentials
spark = (
    SparkSession.builder
    .appName("Export Tables to S3")
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
    .getOrCreate()
)
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider")
spark.sparkContext._jsc.hadoopConfiguration().set("com.amazonaws.services.s3a.enableV4", "true")
spark.sparkContext._awsCredentialsProvider = session.get_credentials()

# ... (the rest of your code remains the same)