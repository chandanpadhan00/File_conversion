import os
import pandas as pd

# Path to the folder containing all product folders
base_folder = 'path_to_folder_containing_product_folders'

# Output folder path where merged Excel files will be stored
output_folder = 'path_to_output_folder'

# Function to merge data for each class into one DataFrame and write to Excel
def merge_and_write_class_data(product_folder_path, class_number):
    class_data = pd.DataFrame()
    for root, _, files in os.walk(product_folder_path):
        for file_name in files:
            if file_name.startswith(f'class_{class_number}') and file_name.endswith('.xlsx'):
                print(f"Found file: {file_name}")
                file_path = os.path.join(root, file_name)
                df = pd.read_excel(file_path)
                class_data = pd.concat([class_data, df], ignore_index=True)
    if not class_data.empty:
        output_file_path = os.path.join(output_folder, f'class_{class_number}.xlsx')
        print(f"Writing data to: {output_file_path}")
        class_data.to_excel(output_file_path, index=False)

# Iterate over each product folder
for root, _, product_folders in os.walk(base_folder):
    for product_folder_name in product_folders:
        product_folder_path = os.path.join(root, product_folder_name)
        print(f"Processing folder: {product_folder_path}")
        # Iterate over each class (assuming there are 6 classes)
        for class_number in range(1, 7):
            merge_and_write_class_data(product_folder_path, class_number)