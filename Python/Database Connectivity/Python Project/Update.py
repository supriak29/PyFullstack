import pymysql
from validation import Validate
from otp_email import *
from user import viewData

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()

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

updateData()
