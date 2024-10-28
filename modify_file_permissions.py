import os
## Function to modify file permissions

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
