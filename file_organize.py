import os
import shutil

def organize_files(root_directory):
    """
    Organizes files with class information in their filenames within each product folder.

    Args:
        root_directory (str): Path to the root directory of your file structure.
    """

    for root, dirs, files in os.walk(root_directory):
        if "product" not in root:  # Skip non-product folders
            continue

        for file_name in files:
            if not file_name.endswith(".xlsx"):
                continue  # Skip non-xlsx files

            match = re.match(r"(\d+)_.+\.xlsx", file_name)  # Extract class from filename
            if match:
                class_number = int(match.group(1))

                destination_folder = os.path.join(root, f"class_{class_number}")
                os.makedirs(destination_folder, exist_ok=True)  # Create class folder if needed

                source_file_path = os.path.join(root, file_name)
                destination_file_path = os.path.join(destination_folder, file_name)

                shutil.copy(source_file_path, destination_file_path)  # Copy file to class folder

if __name__ == "__main__":
    root_directory = "<path/to/your/root/directory>"  # Replace with your actual path
    organize_files(root_directory)
    print("Files organized successfully!")
