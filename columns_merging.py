import pandas as pd

# Read the CSV file
df = pd.read_csv('Jomato.csv')

# Concatenate columns 'RestaurantType' and 'Rating' with "#" separator and create a new column
df['modified_column'] = df['RestaurantType'].astype(str) + '#' + df['Rating'].astype(str)

# Rename the last column to 'total_time_of_delivery'
df = df.rename(columns={'Delivery time': 'total_time_of_delivery'})

# Select columns to keep, ensuring 'RestaurantName' is before 'modified_column'
columns_to_keep = ['OrderId', 'RestaurantName', 'modified_column'] + [col for col in df.columns if col not in ['OrderId', 'RestaurantName', 'modified_column']]

# Create a new DataFrame with modified column order
new_df = df[columns_to_keep]

# Save the modified DataFrame to a new CSV file (change the path if needed)
new_df.to_csv('modified_file_1.csv', index=False)

print("CSV file created successfully with 'modified_column' after 'RestaurantName'.")
