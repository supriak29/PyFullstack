import pymysql
import bcrypt
from validation import Validate
from otp_email import *

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()

def register():
    """
        user registration process takes place in this method
        successfully validated user gets to register
        else the user is sent back to menu to select his/her options
    """
    
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fname = fname.title()
    lname = lname.title()
    
    name = Validate.nameValidate(fname,lname)
    if name is not None:
        email = input("Enter your email id: ")
        chkemail = Validate.emailCheck(email)
        if chkemail is None:
            mobile = input("Enter your mobile no.: ")
            chk_mobile = Validate.mobileValidate(mobile)
            if chk_mobile is not None:
                username = input("Create your username: ")
                uname = Validate.unameValidate(username)
                if uname is not None:
                    pwd = input("Set password: ")
                    cpwd = input("Confirm password: ")
                    password = Validate.pwdValidate(pwd,cpwd)
                    if password is not None:
                        #converting into hash value
                        hashpwd = bcrypt.hashpw(password,bcrypt.gensalt())
                        dob = str(input("\nEnter your birth-date [yyyy-mm-dd]: "))
                        date = Validate.dobValidate(dob)
                        if date is not None:
                            result = verifyOtp(email)
                            if result is not None:
                                print("\ncode is correct")
                                insert_query = """insert into user(fname, lname, username, email,
                                                                    mobile, password, date_of_birth)
                                                              values(%s, %s, %s, %s, %s, %s, %s)"""
                                user_info = (fname,lname,username,email,mobile,hashpwd,dob)
                                cur.execute(insert_query,user_info)
                                con.commit()
                                print("\nSuccessfully Registered.\n")
            else:
                print("\nInvalid mobile number!\n")

def viewData(email):
    select_query = "select * from user where email=%s"
    cur.execute(select_query,(email,))
    fname,lname,uname,email,mobile,password,dob = cur.fetchone()

    print("\n\n***** Your Credentials *****\n")
    print("1. First name: ", fname)
    print("2. Last name: ", lname)
    print("3. Username: ", uname)
    print("4. Email ID: ", email)
    print("5. Password(encrypted): ", password)
    print("6. Date of Birth: ", dob,"\n")


def updateData():
    result = not None
    email = input("Enter email:")
    chkemail = Validate.emailCheck(email)

    try:
        if chkemail is not None:
            otp = verifyOtp(email)
            if otp is not None:
                #viewData(email)
                
                select_query="select * from user where email = %s"
                cur.execute(select_query, (email,))
                fname, lname, uname, emailD, mobile, password, dob = cur.fetchone()

                
                print(""" Enter nos that you wanna modify:
            1. first name
            2. last name
            3. username
            4. email
            5. mobile
            6. password
            7. dob """)
                
                chstr = input("Enter your choice comma seperated: ")
                chlst = chstr.split(",")

                for i in chlst:
                    if int(i)==1:
                        fname = input("Enter first name: ")
                        fname = fname.title()
                        name = Validate.nameValidate(fname,"")
                        print("name: ",name)
                        if name is None:
                            result = None
                            break
                    elif int(i)==2:
                        lname = input("enter last Name: ")
                        lname = lname.title()
                        name = Validate.nameValidate("",lname)
                        if lname is None:
                            result = None
                            break
                    elif int(i)==3:
                        uname = input("enter username: ")
                        chk_uname = Validate.unameValidate(uname)
                        if chk_uname is None:
                            result = unameValidate(uname)
                            if result is None:
                                break
                    elif int(i)==4:
                        email = input("enter email: ")
                        chkemail = Validate.emailCheck(email)
                        if chkemail is False:
                            result = None
                            break
                    elif int(i)==5:
                        mobile = input("enter mobile no: ")
                        chk_mobile = Validate.mobileValidate(mobile)
                        if chk_mobile is None:
                            result=None
                            break
                    elif int(i)==6:
                        password = input("enter password: ")
                    elif int(i)==7:
                        dob = input("enter dob: ")

                if result is None:
                    print("Unable to update!")
                else:
                    update_query = """update user set fname = %s, lname =%s,
                    username=%s, email =%s, mobile=%s, password = %s, date_of_birth=%s
                        where email = %s;"""
                    update_values = (fname, lname, uname, email,mobile,password,dob,emailD)
                    cur.execute(update_query, update_values)
                    con.commit()
                    print("\nProfile Updated!")

                    # display updated credentials:
                    print("\n**** UPDATED CREDENTIALS ***\n")
                    print("1. First name: ", fname)
                    print("2. Last name: ", lname)
                    print("3. Username: ", uname)
                    print("4. Email ID: ", email)
                    print("5. Mobile No.: ",mobile)
                    print("6. Password(encrypted): ", password)
                    print("7. Date of Birth: ", dob,"\n")
                    
        else:
            print("user does not exist!")
    except:
        print("Update Failed!")

        
# ----------------------------------------------


# USER-MENU:

while True:
    print("""User Menu:
            1. Register
            2. Login
            3. Forgot Password
            4. Update Data
            5. View Data
            6. Quit""")
    try:
        ch = int(input("\nEnter your choice:"))
        if ch==1:
            register()
        elif ch==2:
            login()
        elif ch==3:
            forgotPwd()
        elif ch==4:
            updateData()
        elif ch==5:
            print("\nVerification required..\n")
            email = input("Enter your registered email id: ")
            chkemail = Validate.emailCheck(email)
            if email is not None:
                otp = verifyOtp(email)
                if otp is not None:
                    viewData(email)
        elif ch == 6:
            break
        else:
            print("\nelse: Wrong Input!\n") # this is when user enters a no. not mentioned above
    except:
        print("\ncatch: Wrong Input!\n") # this is when user enters something other than a no.

con.close() # close the database connection
