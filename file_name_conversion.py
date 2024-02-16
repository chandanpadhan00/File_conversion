import os

folder_path = 'D:\Try'  # Replace with the path to your folder

# List all files in the folder
files = os.listdir(folder_path)

# Loop through each file and rename accordingly
for file_name in files:
    if file_name.endswith('.xlsx'):
        # Extract the class number from the file name
        class_number = file_name.split('_')[1]
        
        # Construct the new file name with the desired format
        new_file_name = f'79_{class_number}'
        
        # Create the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name + '.xlsx')
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("File names have been updated.")

