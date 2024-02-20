import pandas as pd

# Read the CSV file
df = pd.read_csv('70_3.csv')

# Convert all column names to lowercase
df.columns = df.columns.str.lower()


df['value'] = df['col1'].astype(str) + '#' + df['col2'].astype(str)

# Rename the last column to 'previous_value'
last_column_name = df.columns[-1]
df = df.rename(columns={last_column_name: 'set_column_name'})

# Select columns to keep, ensuring positioning
columns_to_keep = ['col1', 'col2']

# Create a new DataFrame with modified column order
new_df = df[columns_to_keep]

# Save the modified DataFrame to a new CSV file (change the path if needed)
new_df.to_csv('my_file.csv', index=False)

print("CSV file created successfully with 'value' column and renaming.")
