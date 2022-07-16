import pymysql
import bcrypt
import smtplib
import random as r
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from registration import register
from update import updateData
#from Login import login
##from view import viewData
from validation import Validate

# connect with database
con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()

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
