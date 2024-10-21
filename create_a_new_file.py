file_name = input(" Enter File Name Here : ")

with open(file_name, 'a') as file:
    file.write("Now the file has more content!")
    file.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
