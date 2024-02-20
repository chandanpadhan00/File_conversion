import pandas as pd
import os
import openpyxl  # Additional library for handling filters

def convert_xlsx_to_csv(input_folder, output_folder):
    if not os.path.isdir(input_folder):
        raise ValueError(f"Input folder '{input_folder}' does not exist.")
    if not os.path.isdir(output_folder):
        raise ValueError(f"Output folder '{output_folder}' does not exist.")

    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):
            try:
                # Use openpyxl to handle filters and read all visible data
                workbook = openpyxl.load_workbook(os.path.join(input_folder, filename), data_only=True)
                sheet = workbook.active

                # Convert to DataFrame using openpyxl's read-only mode, skip the first row, and use the second row as header
                df = pd.DataFrame(sheet.values)
                df.columns = df.iloc[0]
                df = df.iloc[1:]

                # Generate output filename (optional)
                output_filename = os.path.splitext(filename)[0] + ".csv"

                # Save DataFrame to CSV
                df.to_csv(os.path.join(output_folder, output_filename), index=False, header=True)

                print(f"Converted '{filename}' to '{output_filename}'")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")

if __name__ == "__main__":
    input_folder = "D:\Try"
    output_folder = "D:\Try"

    convert_xlsx_to_csv(input_folder, output_folder)
