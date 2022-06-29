# formatting the string

# static
fname = "Supriya"
mname = "Sanjay"
lname = "Karkera"

print("My name is {}".format(fname))
print("This is my full name {} {} {}".format(fname,mname,lname))
print(f"This is my full name {fname} {mname} {lname}")

print()

# dynamic
fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")

print("My name is {}".format(fname))
print("This is my full name {} {} {}".format(fname,mname,lname))
print(f"This is my full name {fname} {mname} {lname}")
