# Removing blank/white spaces from string

name1 = "supriya       "
name2 = "       supriya"
name3 = "       supriya       "

print(name1)
print(name2)
print(name3)

# right strip to remove the blank spaces from right
# rstrip()
print(name1.rstrip())

# left strip to remove the blank spaces from left
# lstrip
print(name2.lstrip())

# strip to remove the blank spaces from both ends
# strip()
print(name3.strip())

############################################

if "supriya" == "supriya   ":
    print("Yes")
else:
    print("No")
