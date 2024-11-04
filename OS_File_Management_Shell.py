# Operating System Custom Shell
# Members: Kyshauny Bailey, Kaciann Melbourne, Othneil Brown, Dwayne Wright, Khavar Facey

import os
import shlex
import sys
import stat
import time

#Create File
def display_prompt():
    # Display prompt and get user input
    return input(f"{os.getcwd()}> ")
def execute_command(command_args):
    cmds = [shlex.split(cmd) for cmd in command_args.split('|')] if '|' in command_args else [shlex.split(command_args)]
    prev_process = None

    for cmd in cmds:
        prev_process = subprocess.Popen(cmd, stdin=prev_process.stdout if prev_process else None, stdout=subprocess.PIPE)
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

#Delete File
def delete_file():
  file_name = input("Enter file name here : ")
  if os.path.exists(file_name):
    print(file_name, "was found!")
    print()
    sel1_YN = str(input("Do you wish to remove? [y/n]"))
    os.remove(file_name)
    print(f"\nFile {file_name} was deleted successfully")
  else:
    print("The file does not exist")

#Modify File Permissions
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

#List files and detailed file attributes
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
                print(f"{entry_permissions} {entry_links} {entry_owner} {entry_group} {entry_size} {entry_mtime} {entry}")
            except Exception as e:
                print(f"Error retrieving stats for {entry}: {e}")
    else:
        # Error message for invalid arguments
        print("Error: Invalid argument. Please use 'ls -l' for detailed file attributes.")

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
    9. help                               - Show this menu again
    10. exit                              - Exit the shell

    Please enter your command below:
    ------------------------------
    """
    print(menu_text)


# Main loop for the shell
def shell_loop():
    #print_menu()  # Show the menu at the beginning of the shell

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
                delete_file()

            elif command == "rename":
                rename_file(command_args[1], command_args[2])

            elif command == "make":
                create_directory(command_args[1])

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

            elif command == "help":
                print_menu()  # Show the menu again when the "help" command is used

            else:
                print(f"Invalid command: {command}")

        except Exception as e:
            print(f"Error: {e}")


# Call the main shell loop to start the program
if __name__ == "__main__":
    shell_loop()