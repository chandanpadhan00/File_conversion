import os

folder_path = "path/to/your/folder"  # Replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        new_name = os.path.join(folder_path, filename.replace(".xlsx", ""))
        os.rename(os.path.join(folder_path, filename), new_name)