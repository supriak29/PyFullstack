# update function
def updateData():
#    viewData()
    email = input("Enter email of the user you want to modify: ")
    select_query = "select * from user where email = %s"
    cur.execute(select_query,(email,))
    fname,lname,uname,emailD,mobile,password = cur.fetchone()

    print("""Enter nos. that you want to modify:
1. First Name
2. Last Name
3. Username
4. Email ID
5. Mobile No.
6. Password""")
    ch = input("Enter your choice comma seperated: ")
    chsplt = ch.split(', ')
    for i in chsplt:
        if int(i)==1:
            fname = input("Enter first name: ")
        elif int(i)==2:
            lname = input("Enter last name: ")
        elif int(i)==3:
            uname = input("Enter username: ")
        elif int(i)==4:
            email = input("Enter email id: ")
        elif int(i)==5:
            mobile = input("Enter mobile no.: ")
        elif int(i) == 6:
            password = input("Enter password: ")

    update_query = """update user set fname=%s, lname=%s,
username=%s, email=%s, mobile=%s, password=%s"""
    update_values = (fname,lname,username,email,password)
    cur.execute(update_query, update_values)
    con.commit()
