# Validate username
import phonenumbers
import pymysql
import datetime
from menu import userMenu

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
cur = con.cursor()

class Validate:

    def nameValidate(first,last):
        fname = first
        lname = last
        fname = fname.title()
        lname = lname.title()
        name = fname+lname
        count=0
        for i in name:
            if i.isdigit():
                count+=1
        if count>0:
            print("\nDigits not allowed in name.\n")
            userMenu()
        else:
            return not None

    def emailCheck(email):
        if "@gmail.com" in email:
            # check if email present in db
            select_query = "SELECT *FROM user WHERE email=%s"
            result = cur.execute(select_query,(email,))
            if result==1:
                print("\nUser with {} email id already exists.".format(email),"\n")
                userMenu()
            else:
                count=0
                for i in email:
                    if i.isspace():
                        count+=1
                if count>0:
                    print("\nInvalid Email ID.\n")
                    userMenu()
                else:
                    # proceed with registration
                    return not None
        else:
            print("\nInvalid Email ID.\n")
            userMenu()
        
    def mobileValidate(num):
        mobile = num
        mobile = '+'+mobile
        try:
            contact = phonenumbers.parse(mobile)
            if phonenumbers.is_possible_number(contact):
                return not None
            else:
                print("\nInvalid mobile number\n")
                userMenu()
        except Exception as e:
            print("\nAn Error occured!\n")
            userMenu()


    def unameValidate(username):
        """
        Username criteria:
            Should not have more than 8 characters
            Should not have special characters like @ # $ %

            username >= 3 and username <= 8 characters
            Might contain _underscore or digits(0-9)
            Should have letters(a-z) - all small
            Convert the username to small letters if captital
        """
        uname = username
        uname = uname.lower()
        l = len(uname)

        if l>=3 and l<=20:
            if uname!='&' and uname!='@' and uname!='%' and uname!='*':
                if uname[-1]!='.':
                    uname = uname.lower()
                    # check if email present in db
                    select_query = "SELECT *FROM user WHERE username=%s"
                    result = cur.execute(select_query,(uname,))
                    if result==0:
                        print("\nUsername saved as: ",uname,"\n")
                        return uname
                    else:
                        print("\nusername already exists!\n")
                        userMenu()
                else:
                    print("\nUsername cannot end with a period\n")
                    userMenu()
            else:
                print("\nUsername can only contain letters, numbers, underscore & period.\n")
                userMenu()
        else:
            print("\nInvalid length of username\n")
            userMenu()


    def pwdValidate(password,cpassword):
        """
         atleast 8 digit
         upper case
         lower case
         number
         special character
        """
        l,u,p,d = 0,0,0,0
        pwd = password
        cpwd = cpassword
        
        if pwd==cpwd:
            if (len(pwd) >= 8):
                for i in pwd:
                    if (i.islower()):
                        l+=1           
                    if (i.isupper()):
                        u+=1           
                    if (i.isdigit()):
                        d+=1           
                    if(i=='@'or i=='$' or i=='_'):
                        p+=1
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(pwd)):
                password = bytes(pwd,'utf-8')
                return password
            else:
                print("Invalid password")
                userMenu()
        else:
            print("Passwords don't match.")
            userMenu()

    def dobValidate(dob):
        '''
            format: YYYY-MM-DD
        '''
        #dob = '2018-06-29'
        dob = dob.replace('-','/')
        dob = datetime.datetime.strptime(dob, '%Y/%m/%d')
        print(dob)
        if dob:
            birthdate = str(dob)
            count=0
            print(birthdate)
            
            for i in birthdate:
                if i.isalpha():
                    count+=1
            if count==0:
                # edit birthdate pending
                return birthdate
            else:
                print("Invalid date!")
                userMenu()

Validate.dobValidate("2002/09/08")
#---------------------------------------------------------------
##con = pymysql.connect(host="localhost",user="root", password="",
##                      database="usermanagement")
##print("Database connected.")
##cur = con.cursor()
##
##uname = input("Enter username: ")
##
##select_query = "select * from user where username=%s"
##name = cur.execute(select_query,(uname,))
##
### if name=1, TRUE [not in db]
### if name=0, FALSE [not in db]
##print(name)
