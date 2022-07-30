import pymysql
import bcrypt
from validation import Validate

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
                        dob = str(input("\nEnter your birth-date [yyyy-mm-dd]: "))
                        date = Validate.dobValidate(dob)
                        if date is not None:

                            # --------- GENERATING OTP ------------------
                            def otpgen():
                                otp=""
                                for i in range(4):
                                    otp+=str(r.randint(1,9))
                                return otp
                            # -------------------------------------------

                            otp = otpgen()
                            print("\nPlease check your email for verification code.\n")
                            # send user message: Successfully Registered:
                            
                            msg = MIMEMultipart()
                            msg['From'] = 'supriyakarkera29@gmail.com'
                            #msg['To'] = 'supria29.k@gmail.com'
                            msg['To'] = email
                            msg['Subject'] = 'simple email in python'
                            message = 'Verification code: {}'.format(otp)
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
                                if b == otp:
                                    print("\ncode is correct")
                                    cur.execute(insert_query,user_info)
                                    con.commit()
                                    print("\nSuccessfully Registered.\n")
                                    userMenu()
                                    break
                                else:
                                    x -= 1 
                                    print("Wrong code. {} attempt remaining".format(x))
                                    c += 1
                                    continue
                            if c > 3:
                                print("3 attempts over! Code expired!")
                                userMenu()


'''
        1. fname, lname
        2. email
        3. mobile
        4. username
        5. pwd, cpwd
        6. dob 
'''

