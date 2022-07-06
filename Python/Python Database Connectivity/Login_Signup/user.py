import pymysql, datetime

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()

def register():
    insert_query = """insert into user
(Fname, Lname, Username, Email, Mobile, Password)
values(%s, %s, %s, %s, %s, %s)"""
    
##    fname = input("Enter first name: ")
##    lname = input("Enter last name: ")
##    username = input("Enter username: ")
##    email = input("Enter email id: ")
##    mobile = input("Enter mobile number: ")
##    pwd = input("Enter password: ")
##    cpwd = input("Confirm password: ")

##    def checkPwd():
##        length,lower,upper,digit,spcl = 0,0,0,0,0
##
##        if len(pwd) >= 8:
##            length = True
##            
##            if pwd.islower()==False:
##                print("Should contain atleast one alphabet as lower case [a-z]")
##            elif pwd.isupper()==False:
##                print("Should contain atleast one aplhabet as upper case(A-Z)")
##            elif pwd.isdigit()==False:
##                print("Should contain atleast one alphabet as number/digit")
##            elif pwd.isalnum()==False:
##                print("Should contain at least one special character")
##            else:
##                if pwd==cpwd:
##                    print("Password set successfully.")
##                else:
##                    print("Passwords don't match") 
##    checkPwd()
    #check if pwd is same as cpwd
##    if pwd==cpwd:
##        print("Password set successfully.")
###        select_query = "select * from user where username=%s"
###        cur.execute(select_query,)
##    else:
##        print("Passwords don't match")

#    user_info = (fname,lname,username,email,mobile,pwd,cpwd)

#-------------------------------------------------
# update function
#def updateData():
    

# ----------------------------------------------

while True:
        print("""Enter choice:
1. New User? Register
2. Existing User? Login
3. Forgot Password
4. Quit""")
        ch = int(input("Enter your choice:"))
        if ch==1:
            register()
        elif ch==2:
            login()
        elif ch==3:
            forgotPwd()
        elif ch == 4:
            break
        else:
            print("Wrong Input")
con.close()
