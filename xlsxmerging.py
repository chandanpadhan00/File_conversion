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


# Function to concatenate .xlsx files for each class with NA preservation
def concat_with_na_preservation(df1, df2):
    # Concatenate DataFrames
    df_concat = pd.concat([df1, df2], ignore_index=True)

    # Replace empty strings with original "N/A" values (if present)
    for col in df_concat.columns:
        na_values = df1[col].loc[df1[col].isna()].tolist()  # Get original "N/A" values
        df_concat.loc[df_concat[col] == "", col] = na_values  # Replace empty strings

    return df_concat


# Concatenate .xlsx files for each class with NA preservation
for class_name in class_data.keys():
    # Loop through subfolders
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.startswith(f"{class_name}.xlsx"):
                # Read the .xlsx file into a dataframe with NA handling
                df = pd.read_excel(os.path.join(root, file), na_values=["N/A"])
                # Concatenate dataframe with existing data using NA preservation
                class_data[class_name] = concat_with_na_preservation(class_data[class_name], df)


# Write consolidated data to new .xlsx files in the output folder
for class_name, df in class_data.items():
    output_path = os.path.join(output_folder, f"{class_name}_consolidated.xlsx")
    df.to_excel(output_path, index=False)
