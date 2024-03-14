import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='merge_script.log', level=logging.INFO)

# Base folder containing all product folders
base_folder = 'path_to_folder_containing_product_folders'
expected_files_per_class = 6  # Assuming 6 classes per product folder


def merge_and_write_class_data(product_folder_path):
    # Dictionary to store class data
    class_data = {}
    # Set to track processed files
    processed_files = set()

    for root, _, files in os.walk(product_folder_path):
        for file_name in files:
            if file_name.startswith('class_') and file_name.endswith('.xlsx'):
                # Extract class number from filename
                class_number = int(file_name.split('_')[1])
                file_path = os.path.join(root, file_name)
                df = pd.read_excel(file_path)

                # Add data to corresponding class and track processed file
                if class_number not in class_data:
                    class_data[class_number] = df
                else:
                    class_data[class_number] = pd.concat([class_data[class_number], df], ignore_index=True)
                processed_files.add(file_name)
                logging.info(f"Processed file: {file_name}")

    # Write data to separate Excel files for each class
    for class_number, df in class_data.items():
        if not df.empty:
            output_file_path = os.path.join(product_folder_path, f'class_{class_number}.xlsx')
            print(f"Writing data to: {output_file_path}")
            df.to_excel(output_file_path, index=False)


# Iterate over each product folder
for root, _, product_folders in os.walk(base_folder):
    for product_folder_name in product_folders:
        product_folder_path = os.path.join(root, product_folder_name)
        print(f"Processing folder: {product_folder_path}")
        merge_and_write_class_data(product_folder_path)

    # Check if all expected files were processed
    num_processed_files = len(processed_files)
    if num_processed_files != expected_files_per_class * len(product_folders):
        print(f"Warning: Expected {expected_files_per_class * len(product_folders)} files, found {num_processed_files}")
    else:
        print(f"All expected files for product folder {product_folder_name} seem to be generated.")
