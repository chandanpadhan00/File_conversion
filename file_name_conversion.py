import os
import shutil

def organize_files(root_directory):
    output_directory = "/path/to/output"  # Specify your desired output directory

    for variant in os.listdir(root_directory):
        variant_path = os.path.join(root_directory, variant)
        if os.path.isdir(variant_path):
            for country in os.listdir(variant_path):
                country_path = os.path.join(variant_path, country)
                if os.path.isdir(country_path):
                    for product in os.listdir(country_path):
                        product_path = os.path.join(country_path, product)
                        if os.path.isdir(product_path):
                            for class_number in range(1, 7):
                                class_folder = os.path.join(output_directory, f"class_{class_number}")
                                os.makedirs(class_folder, exist_ok=True)

                                for filename in os.listdir(os.path.join(product_path, f"class_{class_number}")):
                                    source_file_path = os.path.join(product_path, f"class_{class_number}", filename)
                                    destination_file_path = os.path.join(class_folder, filename)
                                    shutil.copy(source_file_path, destination_file_path)

if __name__ == "__main__":
    root_directory = "/path/to/your/root/directory"
    organize_files(root_directory)
