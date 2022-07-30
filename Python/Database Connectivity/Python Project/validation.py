# Validate

import phonenumbers
import pymysql
from datetime import datetime
import re

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
cur = con.cursor()

class Validate:
    '''
        This class performs validations functions on:
            Name of the user
            Email
            Mobile No.
            Username
            Password
            Date of Birth
    '''
    def nameValidate(first,last):
        fname = first
        lname = last
        name = fname+lname
        count=0
        for i in name:
            if i.isdigit() or i=='$' or i=='_' or i=='@' or i=='#':
                count+=1
        if count>0:
            print("\nDigits or special character not allowed in name.\n")
            #userMenu()
            return None
        else:
            return not None

    def emailCheck(email):
        if "@gmail.com" in email:
            # check if email present in db
            select_query = "SELECT *FROM user WHERE email=%s"
            result = cur.execute(select_query,(email,))
            if result==1:
                # user exists
                print("\nUser with {} email id exists...".format(email),"\n")
                #userMenu()
                return not None
            else:
                # user does not exist
                # needs registration
                count=0

                for i in email:
                    # validate
                    if i.isspace():
                        count+=1
                if count>0:
                    # invalid email
                    print("\nInvalid Email ID.")
                    return False
                    
                else:
                    # valid email, proceed with registration
                    return None
        else:
            print("\nInvalid Email ID.")
            #userMenu()
            return None
        
    def mobileValidate(num):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        return Pattern.match(num)


    def unameValidate(username):
        """
        Username criteria:
            Should not have more than 8 characters
            Should not have special characters like @ # $ %

            username >= 3 and username <= 10 characters
            Might contain _underscore or digits(0-9)
            Should have letters(a-z) - all small
            Convert the username to small letters if captital
        """
        uname = username
        uname = uname.lower()
        l = len(uname)

        if l>=3 and l<=15:
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
                        #userMenu()
                        return None
                else:
                    print("\nUsername cannot end with a period\n")
                    #userMenu()
                    return None
            else:
                print("\nUsername can only contain letters, numbers, underscore & period.\n")
                #userMenu()
                return None
        else:
            print("\nUsername length can vary from 3-15 only.\n")
            #userMenu()
            return None


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
                print("\nPassword should contain atleast 8 characters, 1 upper case, 1 lower case, 1 special character and 1 digit.\n")
                #userMenu()
                return None
        else:
            print("\nPasswords don't match!\n")
            #userMenu()
            return None


    def dobValidate(dob):
        '''
            format: YYYY-MM-DD
        '''
        try:
            date = dob
            my_date = datetime.strptime(date, "%Y-%m-%d")
            my_date=str(my_date)
            date=''
            for i in my_date:
                if i==' ':
                    break
                else:
                    date+=i
            return date
        except:
            print("\nInvalid date format!\n")
            #userMenu()
            return None
 

#---------------------------------------------------------------
# if name=1, TRUE [not in db]
# if name=0, FALSE [not in db]

