# python provides the "readlines()", method, it is used for reading lines

# open file with "r" mode

##with open("akbar_birbal.txt","r") as f:
##    content = f.readlines()
##    print(content)

### file pointer position
##with open("akbar_birbal.txt","r") as f:
##    print("The file pointer is at: ",f.tell())
##    content = f.read(50)
##    print("The file position is at: ",f.tell())

# set the pointer location
# fileobj.seed(offset,from)
# offset: it refers to the new position of the pointer
# from: it indicates the reference position from where tje bytes are to be moved
# from = 0: it refers the beginning of the file
# from = 1: the current position
# from = 2: the end of the pointer is used as reference

with open("AkbarBirbal.docx",'rb') as f:
    print("The file pointer is at: ",f.tell())
    f.seek(10)
    print("The file pointer is at: ",f.tell())
    content = f.read(20)
    print("The file pointer is at: ",f.tell())
    print(content)
