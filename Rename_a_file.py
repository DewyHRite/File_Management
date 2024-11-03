import os

# Rename a file
new_filename = input ("\nEnter new name for the file along with extension: ")

try:
# Renaming file directly in the OS
    os.rename(file_name, new_file)
    print(f"File renamed from {file_name} to {new_file}.")

# Updating file_name variable to reflect new file name
    file_name = new_filename
    
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"Error renaming file: {e}")
