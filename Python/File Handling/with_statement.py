# "with" statement is useful in the case of manipulating the files
# with open(filename, accessmode) as filePointer

# when you open a file with context "with statement" you dont have to close a file explicitly.
# with statement automatically closes the file when any issue

with open("princess_diaries.txt","r") as f:
    content = f.read()
    print(content)
