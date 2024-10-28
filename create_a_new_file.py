import os

def createfile():

    print("Please select an option below\n\n  1. Create New File\n\n  2. Append Existing File\n\n  3. Exit")
    sel = int(input("\nPlease enter selection here: "))

    if sel == 1:
        print("\nFile Creation.")
        # Get the file name from the user
        file_name = input("Enter File Name (with file extenstion) Here : ")
        file_content: str = input("Please enter file contents here: ")
        sel_YN = input(f"\nDo you wish to create file: {file_name}? \nPlease enter selection here [y/n]: ")
        if sel_YN in ['y','Y']:
            print("\nFile ",file_name,'was created successfully' )
            with open(file_name, 'w') as file:
                file.write('\n')
                file.write(file_content)
                file.close()
                # open and read the file after the appending:
                file = open(file_name, "r")
                print(file.read())
                createfile()
        elif sel_YN in ['n','N']:
            createfile()
    elif sel == 2:
        print("\nEdit/Append File.")
        # Get the file name from the user
        file_name = input("Enter File Name (with file extenstion) Here : ")
        file_content: str = input("Please enter file contents here: ")
        print ("\nDo you wish to update file: ",file_name,'?')
        sel_YN = str(input("\nPlease enter selection here [y/n]: "))
        if sel_YN in ['y','Y']:
            print("\nFile ",file_name,'was updated successfully')
            with open(file_name, 'a') as file:
                file.write('\n')
                file.write(file_content)
                file.close()
                #open and read the file after the appending:
                file = open(file_name, "r")
                print(file.read())
                createfile()
        elif sel_YN in ['n','N']:
            createfile()
    elif sel == 3:
        exit()
    else:
        print ("Invalid Selection")
        createfile()
createfile()
b


import os
import sys

def help():
    print("""
Available commands:
help                      Display this help message
exit                      Exit the shell
set VAR=value             Set an environment variable
get VAR                   Get an environment variable
createfile                Create or append to a file
""")


def createfile():
    print("Please select an option below\n\n  1. Create New File\n\n  2. Append Existing File\n\n  3. Exit")
    sel = int(input("\nPlease enter selection here: "))

    if sel == 1:
        print("\nFile Creation.")
        file_name = input("Enter File Name (with file extension) Here: ")
        file_content = input("Please enter file contents here: ")
        sel_YN = input(f"\nDo you wish to create file: {file_name}? (y/n): ")

        if sel_YN.lower() == 'y':
            print(f"\nFile {file_name} was created successfully")
            with open(file_name, 'w') as file:
                file.write('\n')
                file.write(file_content)
            with open(file_name, "r") as file:
                print(file.read())
            createfile()
        elif sel_YN.lower() == 'n':
            createfile()

    elif sel == 2:
        print("\nEdit/Append File.")
        file_name = input("Enter File Name (with file extension) Here: ")
        file_content = input("Please enter file contents here: ")
        sel_YN = input(f"\nDo you wish to update file: {file_name}? (y/n): ")

        if sel_YN.lower() == 'y':
            print(f"\nFile {file_name} was updated successfully")
            with open(file_name, 'a') as file:
                file.write('\n')
                file.write(file_content)
            with open(file_name, "r") as file:
                print(file.read())
            createfile()
        elif sel_YN.lower() == 'n':
            createfile()

    elif sel == 3:
        exit()

    else:
        print("Invalid Selection")
        createfile()


def main():
    while True:
        try:
            cmd = input("> ").strip().split(' ')
            command = cmd[0]
            args = cmd[1:]

            if command == 'help':
                help()
            elif command == 'exit':
                exit()
            elif command == 'set':
                var, value = args[0].split('=')
                os.environ[var] = value
            elif command == 'get':
                var = args[0]
                print(os.getenv(var, ''))
            elif command == 'createfile':
                createfile()
            else:
                print(f"Invalid command: {command}")
                help()

        except Exception as e:
            print(f"Error: {e}")
            help()


if __name__ == "__main__":
    main()
