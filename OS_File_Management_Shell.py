# Operating System Custom Shell
# Members: Kyshauny Bailey, Kaciann Melbourne, Othneil Brown, Dwayne Wright, Khavar Facey

import os
import shlex
import sys

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
    8. list                               - List files in the current directory
    9. help                               - Show this menu again
    10. exit                              - Exit the shell

    Please enter your command below:
    ------------------------------
    """
    print(menu_text)

def list_files():
    try:
        # Stores all the files in the current directory
        files = os.listdir(os.getcwd())
        if files:
            print("Files in current directory:")
            for file in files:
                print(f"- {file}")
        else:
            print("No files found in the current directory.")
    except Exception as e:
        print(f"Error listing files: {e}")

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
            if len(command_args) == 0:
                continue

            # Command dispatcher
            command = command_args[0]

            if command == "exit":
                sys.exit(0)  # Exit the shell

            elif command == "create":
                create_file(command_args[1])

            elif command == "delete":
                delete_file(command_args[1])

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