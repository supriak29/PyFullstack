import pymysql
import bcrypt
import smtplib
import random as r
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from Registration import register
from Update import updateData
#from Login import login
from View import viewData

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
print("Database connected.")
cur = con.cursor()
# ----------------------------------------------

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

    ### select the row having that particular email id
        select_query = "select * from user where email=%s"
        cur.execute(select_query,(email,))

    # checking if the user already exists using email id
        try:
            fname,lname,username,emailD,mobile,password,reg_date = cur.fetchone()
            if emailD is not None:
                print("User already Exists!")
        except Exception as e:
            # when user is not yet signed up, proceed with registration below: 
            if pwd==cpwd:
                #converting into hash value
                hashpwd = bcrypt.hashpw(pwd,bcrypt.gensalt())
                insert_query = """insert into user
                    (fname, lname, username, email, mobile, password,reg_date)
                    values(%s, %s, %s, %s, %s, %s, %s)"""
                user_info = (fname,lname,username,email,mobile,hashpwd,date)

                # --------- GENERATING OTP ------------------
                def otpgen():
                    otp=""
                    for i in range(4):
                        otp+=str(r.randint(1,9))
                    return otp
                # -------------------------------------------

                a = otpgen()
                print("\nPlease check your email for verification code.\n")
                # send user message: Successfully Registered:
                
                msg = MIMEMultipart()
                msg['From'] = 'supriyakarkera29@gmail.com'
                #msg['To'] = 'supria29.k@gmail.com'
                msg['To'] = email
                msg['Subject'] = 'simple email in python'
                message = 'Verification code: {}'.format(a)
                msg.attach(MIMEText(message))

                mailserver = smtplib.SMTP('smtp.mailtrap.io',587)
                # identify ourselves to smtp gmail client
                mailserver.ehlo()
                # secure our email with tls encryption
                mailserver.starttls()
                # re-identify ourselves as an encrypted connection
                mailserver.ehlo()
                mailserver.login('4a02cd1127338d', '0b937d713f0ae3')

                mailserver.sendmail('supriyakarkera29@gmail.com','supria29.k@gmail.com',msg.as_string())

                mailserver.quit()
                    
                # -------- Sending Email ends here -------------------
                
                c = 1
                x = 3
                for c in range(1,4):
                    b = input("\nEnter Verification code: ")
                    if b == a:
                        print("\ncode is correct")
                        cur.execute(insert_query,user_info)
                        con.commit()
                        print("\nSuccessfully Registered.\n")
                        break
                    else:
                        x -= 1 
                        print("Wrong code. {} attempt remaining".format(x))
                        c += 1
                        continue
                if c > 3:
                    print("3 attempts over! Code expired!")
                
            else:
                print("Password does not match.")
    else:
        print("Not a Valid Email")
        
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
