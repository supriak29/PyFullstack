import pymysql
import bcrypt
from validation import Validate
from menu import userMenu

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
cur = con.cursor()

def register():
    """
        user registration process takes place in this method
        successfully validated user gets to register
        else the user is sent back to menu to select his/her options
    """
    
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    name = Validate.nameValidate(fname,lname)
    if name is not None:
        email = input("Enter your email id: ")
        email = Validate.emailCheck(email)
        if email is not None:
            mobile = input("Enter your mobile no.: ")
            chk_mobile = Validate.mobileValidate(mobile)
            if chk_mobile is not None:
                username = input("Enter your username: ")
                uname = Validate.unameValidate(username)
                if uname is not None:
                    pwd = input("Set password: ")
                    cpwd = input("Confirm password: ")
                    password = Validate.pwdValidate(pwd,cpwd)
                    if password is not None:
                        #converting into hash value
                        hashpwd = bcrypt.hashpw(password,bcrypt.gensalt())
                        dob = input("\nEnter your birth-date [yyyy-mm-dd]: ")
                        if dob is not None:
                            print("good")
    
        

register()




'''
        1. fname, lname
        2. email
        3. mobile
        4. username
        5. pwd, cpwd
    6. dob 
'''




# Proper mobile validation pending
# email validation needs to be upgraded 



##from faker import Faker
##fake = Faker()
##
##print(fake.name(),"\n")
##print(fake.email(),"\n")
##print(fake.address())
