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

                # Set all column names to uppercase
                df.columns = df.columns.str.upper()

                # Handle extra column for files ending with '_2.xlsx'
                if '_2.xlsx' in filename:
                    # Drop the last column
                    df = df.iloc[:, :-1]

                    # Rename the 2nd last column to 'AREA_CODES'
                    df.columns.values[-1] = 'AREA_CODES'
                else:
                    # Rename the last column to 'AREA_CODES'
                    df.columns.values[-1] = 'AREA_CODES'

                # Generate output filename (optional)
                base_name, extension = os.path.splitext(filename)
                output_filename = base_name.replace(".xlsx", "") + ".csv"

                # Save DataFrame to CSV
                df.to_csv(os.path.join(output_folder, output_filename), index=False, header=True)

                print(f"Converted '{filename}' to '{output_filename}'")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")

if __name__ == "__main__":
    input_folder = r'D:\Try\Class_1'
    output_folder = r'D:\Try\Class_2'

    convert_xlsx_to_csv(input_folder, output_folder)







