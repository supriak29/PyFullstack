##from registration import register()
from registration import *

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

##def userMenu():
##    while True:
##            print("""Enter choice:
##    1. Register
##    2. Login
##    3. Forgot Password
##    4. Update Data
##    5. View Data
##    6. Quit""")
##            ch = int(input("Enter your choice:"))
##            if ch==1:
##                register()
##            elif ch==2:
##                login()
##            elif ch==3:
##                forgotPwd()
##            elif ch==4:
##                updateData()
##            elif ch==5:
##                viewData()
##            elif ch == 6:
##                break
##            else:
##                print("Wrong Input")
            
