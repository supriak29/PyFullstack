import pymysql
import bcrypt

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")
cur = con.cursor()

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
    ##
    ##
    ### select the row having that particular email id
        select_query = "select * from user where email=%s"
        cur.execute(select_query,(email,))

    # checking if the user already exists using email id
        try:
            fname,lname,username,emailD,mobile,password,reg_date = cur.fetchone()
            if emailD is not None:
                print("User already Exists!")
        except Exception as e:
            if pwd==cpwd:
                #converting into hash value
                hashpwd = bcrypt.hashpw(pwd,bcrypt.gensalt())
                insert_query = """insert into user
                    (fname, lname, username, email, mobile, password,reg_date)
                    values(%s, %s, %s, %s, %s, %s, %s)"""
                user_info = (fname,lname,username,email,mobile,hashpwd,date)
                cur.execute(insert_query,user_info)
                con.commit()
                print("Successfully Registered.")
            else:
                print("Password does not match.")
    else:
        print("Not a Valid Email")
