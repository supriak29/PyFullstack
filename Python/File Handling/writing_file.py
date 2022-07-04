# to write some text to a file, we need to open the file using the open
# method with one of the following access mode

# w: overwrite the file if any file exists
# a: append the existing file. the file pointer is at the end of the file
# it creates a new file if no file exists

# open file with "w" mode
with open("python_write_example.txt","w") as f:
    f.write('''Python is the moderns day language. It is used for web development as well as for data science.''')

# open file with "a" mode
with open("python_write_example.txt","a") as f:
    f.write('''\nThis line will be appended to the existing file.''')
