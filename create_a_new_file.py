print("Please select an option below\n\n  1. Create New File\n\n  2. Append Existing File")

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
