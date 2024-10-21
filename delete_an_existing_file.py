import os

file_name = input("Enter file name here : ")
if os.path.exists(file_name):
  print(file_name, "was found!")
  print()
  sel1_YN = str(input("Do you wish to remove? [y/n]"))
  os.remove(file_name)
else:
  print("The file does not exist")