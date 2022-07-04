# Python provides a open() function that accepts two arguments,
# File name and access mode in which the file is accessed.
# if opened with "r", file needs to be explicitly closed.

# file_obj = open(fileName, accessMode)

############################################



# opens the file akbar_birbal.txt in read mode
file_obj = open("akbar_birbal.txt",'r') # add the path of file if in another folder
print(file_obj)
print("File opened successfully\n")

# to check what all can be done with files
print(dir(file_obj))

print()

# close file
file_obj.close()


