import pymysql
import bcrypt
from validation import Validate
from otp_email import *

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()


##def login():
##    email = input("Enter Email id: ")
##    password = bytes(input("Enter Password: "),'utf-8')
##    
##    # checking if the user already exists using email id
##    try:
##        select_query = "select * from user where email=%s"
##        cur.execute(select_query,(email,))
##        fname,lname,username,emailD,mobile,pwdD,reg_date = cur.fetchone()
##        print("pwd db: ",pwdD)
##        print("user pwd",password)
##        try:
##            a = bcrypt.checkpw(password,pwdD)
##            print("try block: ",a)
##        except:
##            print("Exception after bcrypt")
####
##        if emailD is not None:
##            if pwdD == password:
##                print("\nLogged in successfullly!\n")
##            else:
##                print("Wrong Password")
##    except Exception as e:
##        print("You are not Registered! Please Signup.")
##
##login()
