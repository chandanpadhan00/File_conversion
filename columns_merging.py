import pandas as pd

# Read the CSV file
df = pd.read_csv('70_3.csv')

# Convert all column names to lowercase
df.columns = df.columns.str.lower()

# Concatenate columns 'source value' and 'value' with "#" separator and create a new column
df['value'] = df['source value'].astype(str) + '#' + df['value'].astype(str)

# Rename the last column to 'previous_value'
last_column_name = df.columns[-1]
df = df.rename(columns={last_column_name: 'previous_value'})

# Select columns to keep, ensuring positioning
columns_to_keep = ['ema data class', 'data class number', '1st level name', '1st level number', '2nd level name', '2nd level number', '3rd level name', '3rd level number', '4th level name', '4th level number', 'value', 'synthetic', 'derived', 'standardized', 'previous_value']

# Create a new DataFrame with modified column order
new_df = df[columns_to_keep]

# Save the modified DataFrame to a new CSV file (change the path if needed)
new_df.to_csv('70_3_modified.csv', index=False)

print("CSV file created successfully with 'value' column and renaming.")
