# Membership Checking in string

# finding matchting substring from a string

full_name = input("Enter your full name: ")
sub = input("Enter the sub string to find: ")

if sub in full_name:
    print("The sub string exists: ",sub)
else:
    print("The given substring is not available.")


full_name = input("Enter your full name: ")
sub = input("Enter the sub string to find: ")

if sub not in full_name:
    print("The sub string does not exists: ",sub)
else:
    print("The given substring is available")
