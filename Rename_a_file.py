import os

file_name = "file.txt"

# Create the file
with open(file_name, 'w') as file:
    file.write("")  # Creates an empty file

print ("Name of file: ", file_name)

# Rename a file
new_name = input ("\nEnter new name for the file along with extension: ")

try:
# Renaming file directly in the OS
    os.rename(file_name, new_name)
    print(f"File renamed from {file_name} to {new_name}.")

# Updating file_name variable to reflect new file name
    file_name = new_name
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"Error renaming file: {e}")
