import pymysql
import bcrypt

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()
# -----------------------------------------------
##def checkPwd(p,cp):
##    # checking if the passwords match
##    if p == cp:
##        if len(p)>=8:
##            # checking validity
##            u,l,d,s = 0,0,0,0
##            for i in p:
##                if i.isupper():
##                    u+=1
##                if i.islower():
##                    l+=1
##                if i.isdigit():
##                    d+=1
##                if i=='@' or i=='$' or i=='_':
##                    s+=1
##            if(u<1):
##                print("Atleast 1 uppercase needed.")
##            if(l<1):
##                print("At least 1 lowercase needed.")
##            if(d<1):
##                print("Atleast 1 digit needed.")
##            if(s<1):
##                print("Atleast 1 special character needed")
##            if(u>0 and l>0 and d>0 and s)
##        else:
##            print("\nPassword should be of atleast 8 character.\n")
##    else:
##        print("\nPasswords don't match\n")

def emailCheck():
    if '@gmail.com' in email:
        print("email is valid")
    else:
        print("invalid email")


def register():

    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    username = input("Enter username: ")
    email = input("Enter email id: ")
    mobile = input("Enter mobile number: ")
    pwd = bytes(input("Enter password: "),'utf-8')
    cpwd = bytes(input("Confirm password: "),'utf-8')
    date = input("Enter date(yyyy-mm-dd): ")

    fname = fname.title()
    lname = lname.title()
    
    if "@gmail.com" in email:
        print("Valid Email")

        user_info = (fname,lname,username,email,mobile,pwd,date)
    ##
    ##
    ### select the row having that particular email id
        select_query = "select * from user where email=%s"
        cur.execute(select_query,(email,))

    # checking if the user already exists using email id
        try:
            fname,lname,username,emailD,mobile,password,reg_date = cur.fetchone()
            if emailD is not None:
                print("User already Exists!")
        except Exception as e:
            if pwd==cpwd:
                #converting into hash value
                hashpwd = bcrypt.hashpw(pwd.encode('ignore'),bcrypt.gensalt())
                insert_query = """insert into user
                    (fname, lname, username, email, mobile, password,reg_date)
                    values(%s, %s, %s, %s, %s, %s, %s)"""
                user_info = (fname,lname,username,email,mobile,hashpwd,date)
                cur.execute(insert_query,user_info)
                con.commit()
                print("Successfully Registered.")
            else:
                print("Password does not match.")
    else:
        print("Not a Valid Email")

##
def viewData():
    select_query = "select * from user"
    cur.execute(select_query)
##
##
##    def checkPwd():
##        length,lower,upper,digit,spcl = 0,0,0,0,0
##
##        if len(pwd) >= 8:
##            length = True
##            
##            if pwd.islower()==False:
##                print("Should contain atleast one alphabet as lower case")
##            elif pwd.isupper()==False:
##                print("Should contain atleast one aplhabet as upper case")
##            elif pwd.isdigit()==False:
##                print("Should contain atleast one alphabet as number/digit")
##            elif pwd.isalnum()==False:
##                print("Should contain at least one special character")
##            else:
##                if pwd==cpwd:
##                    print("Password set successfully.")
####                else:
##                    print("Passwords don't match") 
##    checkPwd()
    #check if pwd is same as cpwd
##    if pwd==cpwd:
##        print("Password set successfully.")
###        select_query = "select * from user where username=%s"
###        cur.execute(select_query,)
##    else:
##        print("Passwords don't match")

    
#    cur.execute(insert_query,user_info)
    con.commit()
#-------------------------------------------------
# update function
def updateData():
#    viewData()
    email = input("Enter email of the user you want to modify: ")
    select_query = "select * from user where email = %s"
    cur.execute(select_query,(email,))
    fname,lname,uname,emailD,mobile,password = cur.fetchone()

    print("""Enter nos. that you want to modify:
1. First Name
2. Last Name
3. Username
4. Email ID
5. Mobile No.
6. Password""")
    ch = input("Enter your choice comma seperated: ")
    chsplt = ch.split(', ')
    for i in chsplt:
        if int(i)==1:
            fname = input("Enter first name: ")
        elif int(i)==2:
            lname = input("Enter last name: ")
        elif int(i)==3:
            uname = input("Enter username: ")
        elif int(i)==4:
            email = input("Enter email id: ")
        elif int(i)==5:
            mobile = input("Enter mobile no.: ")
        elif int(i) == 6:
            password = input("Enter password: ")

    update_query = """update user set fname=%s, lname=%s,
username=%s, email=%s, mobile=%s, password=%s"""
    update_values = (fname,lname,username,email,mobile, password)
    cur.execute(update_query, update_values)
    con.commit()
# ----------------------------------------------

def login():
    email = input("Enter Email id: ")
    password = input("Enter Password: ")

    password = password
    
    # checking if the user already exists using email id
    try:
        select_query = "select * from user where email=%s"
        cur.execute(select_query,(email,))
        fname,lname,username,emailD,mobile,pwdD,reg_date = cur.fetchone()
        print(pwdD)
        print(password)
##        try:
##            a = bcrypt.checkpw(password,hashed)
##            print(a)
##        except Exception e:
##            print("Exception after bcrypt")
##
        if emailD is not None:
            if pwdD == password:
                print("\nLogged in successfullly!\n")
            else:
                print("Wrong Password")
    except Exception as e:
        print("You are not Registered! Please Signup.")

# ----------------------------------------------
while True:
        print("""Enter choice:
1. Register
2. Login
3. Forgot Password
4. Update Data
5. View Data
6. Quit""")
        ch = int(input("Enter your choice:"))
        if ch==1:
            register()
        elif ch==2:
            login()
        elif ch==3:
            forgotPwd()
        elif ch==4:
            updateData()
        elif ch==5:
            viewData()
        elif ch == 6:
            break
        else:
            print("Wrong Input")
con.close()


#-----------------------------    
