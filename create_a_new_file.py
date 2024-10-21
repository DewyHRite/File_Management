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