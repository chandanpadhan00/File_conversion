import os

folder_path = "/path/to/your/folder"  # Replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".csv") and filename.lower().endswith(".xlsx.csv"):
        # Construct the new filename by removing the ".xlsx" part
        new_filename = os.path.join(folder_path, filename[:-5])
        
        # Rename the file
        os.rename(os.path.join(folder_path, filename), new_filename)
        print(f"Renamed: {filename} to {new_filename}")
