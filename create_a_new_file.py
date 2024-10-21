import os

print("Please select an option below\n\n  1. Create New File\n\n  2. Append Existing File")
sel = int(input("\nPlease enter selection here: "))

if sel == 1:
    print("\nFile Creation.")
    # Get the file name from the user
    file_name = input("Enter File Name Here : ")
    file_content: str = input("Please enter file contents here: ")
    with open(file_name, 'w') as file:
        file.write('\n')
        file.write(file_content)
        file.close()

        #open and read the file after the appending:
        file = open(file_name, "r")
        print(file.read())
elif sel == 2:
    print("\nEdit/Append File.")
    # Get the file name from the user
    file_name = input("Enter File Name Here : ")
    file_content: str = input("Please enter file contents here: ")
    with open(file_name, 'a') as file:
        file.write('\n')
        file.write(file_content)
        file.close()

        #open and read the file after the appending:
        file = open(file_name, "r")
        print(file.read())
else:
    print ("Invalid Selection")
    exit()