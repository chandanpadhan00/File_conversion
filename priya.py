from pyspark.sql.functions import col

# Get the distinct values from the source file
source_df = spark.read.format("csv").load("", header=True)
source_distinct_df = source_df.distinct()

# Define the list of tables
tables = ["table1", "table2", "table3"]  # Replace with your actual table names

# Loop through the tables
for table in tables:
    table_df = spark.sql(f"SELECT DISTINCT * FROM {table}_stview")

    # Select only the columns that are common to both the table and the source file
    common_columns = list(set(source_distinct_df.columns).intersection(table_df.columns))

    source_common_df = source_distinct_df.select(*common_columns)
    table_common_df = table_df.select(*common_columns)

    # Compare the distinct values from the source file and the table
    comparison_df = source_common_df.subtract(table_common_df)

    if comparison_df.count() == 0:
        print(f"The data in {table} table matches with the source file.")
    else:
        print(f"The data in {table} table does not match with the source file.")
