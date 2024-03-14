import os
import pandas as pd

# Define the path to the main folder
main_folder = "path/to/your/main/folder"
# Define the path to the output folder
output_folder = "path/to/your/output/folder"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a dictionary to store dataframes for each class
class_data = {f"class_{i}": pd.DataFrame() for i in range(1, 7)}

# Function to concatenate .xlsx files for each class
def concat_xlsx_files(class_name):
    # Loop through subfolders
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.startswith(f"{class_name}.xlsx"):
                # Read the .xlsx file into a dataframe
                df = pd.read_excel(os.path.join(root, file))
                # Concatenate the dataframe with existing data for the class
                class_data[class_name] = pd.concat([class_data[class_name], df])

# Concatenate .xlsx files for each class
for class_name in class_data.keys():
    concat_xlsx_files(class_name)

# Write consolidated data to new .xlsx files in the output folder
for class_name, df in class_data.items():
    output_path = os.path.join(output_folder, f"{class_name}_consolidated.xlsx")
    df.to_excel(output_path, index=False, na_rep='N/A')