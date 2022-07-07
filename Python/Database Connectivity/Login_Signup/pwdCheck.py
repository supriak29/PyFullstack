# ---------------------------------------------
# Check PASSWORD - 1

print("""Password must have atleast 8 characters.
Must contain at least 1 uppercase character,
1 lowercase character,
1 special character\n""")

pwd = input("Enter password: ")

print()

length,u,l,spcl = 0,0,0,0
if len(pwd) >= 8:
    length = True
else:
    print("Password should be of atleast 8 character")

if(pwd.isupper()):
    l = True
else:
    print("Upper case character missing.")
if(pwd.islower()):
    u = True
else:
    print("Lower case character missing.")
if(pwd=='@' or pwd=='$' or pwd=='_'):
    spcl = True
else:
    print("Special Character missing")
        
if(length and l and u and spcl):
    print("valid")
else:
    print("invalid")

print()
# --------------------------------------

# Check PASSWORD - 2

##pwd = input("Enter password: ")
##
##alnum,spcl = 0,0
##if len(pwd) >= 8:
##    for i in pwd:
##        # count alphabet/number
##        if(i.isalnum()):
##            alnum = True
##        # count special character
##        if(i=='@' or i=='$' or i=='_'):
##            spcl = True
##if(alnum or spcl):
##    print("Valid password")
##else:
##    print("Invalid password")




# --------------------------------------

# check FIRST NAME/LAST NAME

##name = (input("Enter First Name: "),
##        input("Enter Last Name: "))
##print(name)
##print(len(name))
##
##for i in len(name):
##    for j in range i:
##        print(i," ",j)

# ----------------------------------------
##
##fname = input("Enter First Name: ")
##lname = input("Enter Last Name: ")
##
##if(fname.isalpha() and lname.isalpha):
##    print("Valid Name")
##else:
##    print("Invalid Name.")
