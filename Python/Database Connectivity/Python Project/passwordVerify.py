
# atleast 8 digit
# upper case
# lower case
# number
# special character

# ----------------- METHOD 1: -------------------------

##from password_validator import PasswordValidator
##
### Create a schema
##schema = PasswordValidator()
##
### Add properties to it
##schema\
##.min(8)\
##.max(100)\
##.has().uppercase()\
##.has().lowercase()\
##.has().digits()\
##.has().no().spaces()\
##
##x = schema.validate('validPASS123');
##print(x)

# ----------------- METHOD 2: -------------------------
def pwdVerify(password,cpassword):
    l,u,p,d = 0,0,0,0
    pwd = password
    cpwd = cpassword

        
    if pwd==cpwd:
        if (len(pwd) >= 8):
            for i in pwd:
                if (i.islower()):
                    l+=1           
                if (i.isupper()):
                    u+=1           
                if (i.isdigit()):
                    d+=1           
                if(i=='@'or i=='$' or i=='_'):
                    p+=1
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(pwd)):
            print("Valid Password")
            return pwd
    else:
        print("Invalid Password")
        return None

##l,u,p,d = 0,0,0,0
##pwd = input("Enter pwd: ")
##cpwd = input("Confirm pwd: ")
##        
##if pwd==cpwd:
##    if (len(pwd) >= 8):
##        for i in pwd:
##            if (i.islower()):
##                l+=1           
##            if (i.isupper()):
##                u+=1           
##            if (i.isdigit()):
##                d+=1           
##            if(i=='@'or i=='$' or i=='_'):
##                p+=1
##        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(pwd)):
##            print("Valid Password")
##        else:
##            print("Invalid password")


    
