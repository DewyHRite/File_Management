# Operating System Custom Shell
# Members: Kyshauny Bailey, Kaciann Melbourne, Othneil Brown, Dwayne Wright, Khavar Facey

import os
import shlex
import sys
import stat
import time
import subprocess


# Create File
def display_prompt():
    # Display prompt and get user input
    return input(f"{os.getcwd()}> ")


def execute_command(command_args):
    cmds = [shlex.split(cmd) for cmd in command_args.split('|')] if '|' in command_args else [shlex.split(command_args)]
    prev_process = None

    for cmd in cmds:
        prev_process = subprocess.Popen(cmd, stdin=prev_process.stdout if prev_process else None,
                                        stdout=subprocess.PIPE)
    output, _ = prev_process.communicate()
    print(output.decode())


def create_file():
    # Get file name and content from user input
    file_name = input("Enter File Name (with file extension) Here: ")
    file_content = input("Please enter file contents here: ")
    if input(f"\nDo you wish to create file: {file_name}? (y/n): ").lower() == 'y':
        # Create the file and write content to it
        with open(file_name, 'w') as file:
            file.write(file_content)
        print(f"\nFile {file_name} was created successfully")
        # Display the contents of the created file
        with open(file_name, "r") as file:
            print


# Delete File
def delete_file(file_name):
    if os.path.exists(file_name):
        print(file_name, "was found!")
        os.remove(file_name)
        print(f"\nFile {file_name} was deleted successfully")
    else:
        print("The file does not exist")

def rename_file(old_name, new_name):
    try:
        # Renaming file directly in the OS
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}.")
    except FileNotFoundError:
        print(f"The file {old_name} does not exist.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def make_directory(dir_name):
    try:
        # Creating the directory directly in the OS
        os.mkdir(dir_name)
        print(f"Directory: '{dir_name}' created.")

    except FileExistsError:
        print(f"Directory: '{dir_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Modify File Permissions
def modify_permission(permissions, file_name):
    try:
        # Validate if the file exists
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' does not exist.")
            return

        # Validate if the permissions string is a valid octal number
        if not permissions.isdigit() or len(permissions) > 4:
            print(f"Error: '{permissions}' is not a valid octal permission.")
            return

        # Convert the octal string representation of permissions to an integer
        os.chmod(file_name, int(permissions, 8))
        print(f"Permissions for '{file_name}' changed to '{permissions}'.")
    except Exception as e:
        print(f"Error modifying permissions: {e}")


# List files and detailed file attributes
def list_files(arg=None):
    # Get the current directory
    current_dir = os.getcwd()

    # List all files and directories in the current directory
    entries = os.listdir(current_dir)

    # Check if the directory is empty
    if not entries:
        print("No files found in the current directory.")
        return

    # Sort entries alphabetically
    entries.sort()

    if arg is None:
        # List all entries (files and directories)
        for entry in entries:
            print(entry)
    elif arg == "-l":
        # List attributes of both files and directories
        for entry in entries:
            entry_path = os.path.join(current_dir, entry)
            try:
                entry_stat = os.stat(entry_path)

                # File permissions
                entry_permissions = stat.filemode(entry_stat.st_mode)

                # Number of links
                entry_links = entry_stat.st_nlink

                # File owner (user ID)
                entry_owner = entry_stat.st_uid

                # File group (group ID)
                entry_group = entry_stat.st_gid

                # File size
                entry_size = entry_stat.st_size

                # Last modified time
                entry_mtime = time.strftime("%b %d %H:%M", time.localtime(entry_stat.st_mtime))

                # Format output
                print(
                    f"{entry_permissions} {entry_links} {entry_owner} {entry_group} {entry_size} {entry_mtime} {entry}")
            except Exception as e:
                print(f"Error retrieving stats for {entry}: {e}")
    else:
        # Error message for invalid arguments
        print("Error: Invalid argument. Please use 'ls -l' for detailed file attributes.")


# Function to remove a specified directory
def remove_directory(dir_name):
    try:
        # Attempting to remove the directory specified by 'dir_name'
        os.rmdir(dir_name)
        # If successful, print a confirmation message
        print(f"Directory '{dir_name}' removed.")
    except FileNotFoundError:
        # If the directory doesn't exist, print an error message
        print(f"Error: The directory '{dir_name}' does not exist.")
    except OSError:
        # If the directory is not empty, print an error message
        print(f"Error: The directory '{dir_name}' is not empty")
    except Exception as e:
        # If any other exception occurs, print the exception details
        print(f"Error: {e}")

# Function to change the current working directory to 'dir_name'
def change_directory(dir_name):
    try:
        # Attempting to change the current working directory to 'dir_name'
        os.chdir(dir_name)
        # If successful, print a confirmation message
        print(f"Changed directory to '{dir_name}'.")
    except FileNotFoundError:
        # If the directory doesn't exist, print an error message
        print(f"Error: The directory '{dir_name}' does not exist.")
    except Exception as e:
        # If any other exception occurs, print the exception details
        print(f"Error: {e}")

# Set Environment Variable
def set_env_variable(var_name, value):
    os.environ[var_name] = value
    print(f"Environment variable '{var_name}' set to '{value}'.")


# Get Environment Variable
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is not None:
        print(f"{var_name}={value}")
    else:
        print(f"Environment variable '{var_name}' does not exist.")


# List All Environment Variables
def list_env_variables():
    for var_name, value in os.environ.items():
        print(f"{var_name}={value}")


# Function to display the menu
def print_menu():
    menu_text = """
    Welcome to the Custom Shell!

    Available Commands:
    ------------------------------
    1. create <file_name>                 - Create a new file
    2. delete <file_name>                 - Delete a file
    3. rename <old_name> <new_name>       - Rename a file
    4. make <dir_name>                    - Create a new directory
    5. remove <dir_name>                  - Remove a directory
    6. change <dir_name>                  - Change working directory
    7. modify <permissions> <file_name>   - Modify file permissions
    8. list [-l]                          - List files in the current directory (use -l for detailed view)
    9. set <var_name> <value>             - Set an environment variable
    10. get <var_name>                    - Get an environment variable
    11. env                               - List all environment variables
    12. help                              - Show this menu again
    13. exit                              - Exit the shell
    Please enter your command below:
    ------------------------------
    """
    print(menu_text)


# Main loop for the shell
def shell_loop():
    # print_menu()  # Show the menu at the beginning of the shell

    while True:
        try:
            # Display the prompt, using the current directory as a prompt
            cwd = os.getcwd()

            # Show prompt and get user input
            command_input = input(f"{cwd}> ")

            # Use shlex.split to properly handle quoted arguments
            command_args = shlex.split(command_input)

            # If no command was given (empty input), continue the loop
            if len(command_args) < 0:
                continue

            # Command dispatcher
            command = command_args[0]

            if command == "exit":
                sys.exit(0)  # Exit the shell

            elif command == "create":
                create_file()

            elif command == "delete":
                delete_file(command_args[1])

            elif command == "rename":
                rename_file(command_args[1], command_args[2])

            elif command == "make":
                make_directory(command_args[1])

            elif command == "remove":
                remove_directory(command_args[1])

            elif command == "change":
                change_directory(command_args[1])

            elif command == "modify":
                modify_permission(command_args[1], command_args[2])

            elif command == "list":
                if len(command_args) > 1:
                    list_files(command_args[1])
                else:
                    list_files()

            elif command == "set":
                if len(command_args) >= 3:
                    set_env_variable(command_args[1], command_args[2])
                else:
                    print("Error: 'set' requires both a variable name and a value.")

            elif command == "get":
                if len(command_args) >= 2:
                    get_env_variable(command_args[1])
                else:
                    print("Error: 'get' requires a variable name.")

            elif command == "env":
                list_env_variables()

            elif command == "help":
                print_menu()  # Show the menu again when the "help" command is used

            else:
                print(f"Invalid command: {command}")

        except Exception as e:
            print(f"Error: {e}")


# Call the main shell loop to start the program
if __name__ == "__main__":
    shell_loop()
