
# atleast 8 digit
# upper case
# lower case
# number
# special character


def pwdVerify(pw,cp):
    l,u,p,d = 0,0,0,0
    pwd = pw
    cpwd = cp
    
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
            #cpwd = bytes(cpwd,'utf-8')
            return pwd
    else:
        print("Invalid Password")
