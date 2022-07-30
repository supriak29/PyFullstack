import smtplib
import random as r
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# --------- GENERATING OTP ------------------
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    return otp
# -------------------------------------------

def verifyOtp(email):
    otp = otpgen()
    print("\nPlease check your email for verification code.\n")

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

    mailserver.sendmail('supriyakarkera29@gmail.com',email,msg.as_string())

    mailserver.quit()
        
    # -------- Sending Email ends here -------------------

    count = 1
    attempt = 3
    for count in range(1,4):
        chk_otp = input("\nEnter Verification code: ")
        if chk_otp == otp:
            return not None  
            break
        else:
            attempt -= 1 
            print("Wrong code. {} attempt remaining".format(attempt))
            count += 1
            continue
    if count > 3:
        print("3 attempts over! Code expired!")
        return None

