import os
def remove_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Remove the file
        os.remove(file_path)
        print(f"CSV file '{file_path}' has been successfully removed.")
    else:
        print(f"CSV file '{file_path}' does not exist.")