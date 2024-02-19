import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = r'D:\DE\Live_Classes\SQL\MS3'

# Iterate through each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Concatenate columns 'RestaurantType' and 'Rating' with "#" separator and create a new column
        df['modified_column'] = df['RestaurantType'].astype(str) + '#' + df['Rating'].astype(str)

        # Rename the last column to 'total_time_of_delivery'
        df = df.rename(columns={'Delivery time': 'total_time_of_delivery'})

        # Select columns to keep, ensuring 'RestaurantName' is before 'modified_column'
        columns_to_keep = ['OrderId', 'RestaurantName', 'modified_column'] + [col for col in df.columns if col not in ['OrderId', 'RestaurantName', 'modified_column']]

        # Create a new DataFrame with modified column order
        new_df = df[columns_to_keep]

        # Save the modified DataFrame to a new CSV file in the same folder
        new_filename = filename.replace('.csv', '_modified.csv')
        new_file_path = os.path.join(folder_path, new_filename)
        new_df.to_csv(new_file_path, index=False)

        print(f"CSV file '{filename}' processed successfully and saved as '{new_filename}'.")
