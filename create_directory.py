import os

# Create a directory
dir_name = input ("\nEnter name of directory: ")

try:
  # Creating the directory directing in the OS
    os.mkdir(dir_name)
    print(f"Directory: '{dir_name}' created.")
  
except FileExistsError:
    print(f"Directory: '{dir_name}' already exists.")
except Exception as e:
    print(f"Error creating directory: {e}")
