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
