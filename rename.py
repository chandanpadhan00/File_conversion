import os

folder_path = "path/to/your/folder"  # Replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        full_path = os.path.join(folder_path, filename)
        new_name = os.path.join(folder_path, os.path.splitext(filename)[0])
        os.rename(full_path, new_name)
