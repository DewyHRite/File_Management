import os
import stat
import time

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
