# starts with & ends with

# main_string.startswith(sub_string)

name = input("Enter your name: ")
substring = input("Enter the starting: ")

n = name.startswith(substring)
print(n) # returns either true or false

if name.startswith(substring):
    print("Yes")
else:
    print("No")

# understanding endswith
# main_string.endswith(sub_string)

name2 = input("Enter your name: ")
substring2 = input("Enter the sub_string: ")

if name2.endswith(substring2):
    print("yes")
else:
    print("No")
