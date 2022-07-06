# to read a file using the python script, the python provides the read() method.
# read() method

### open file with "r" mode
##with open("princess_diaries.txt","r") as f:
##    content = f.read() # reads entire file
##    print(content)
##    print()
##    print(type(content)) # Now, content is in string format

# open file with 'r' mode
with open("princess_diaries.txt",'r') as f:
    content = f.read(25) # here you can stream the content
    print(content)
    print()
    print(type(content))
