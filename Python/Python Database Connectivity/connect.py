# create the connection process more generalised
# I should be able to pass any credentials to connect to the database
# host
# user
# password
# database
###########################################

# importing mysql connection library
import mysql.connector
from mysql.connector import Error

h = input("Enter host name: ")
u = input("Enter username: ")
db = input("Enter database name: ")
pwd = input("Enter password: ")

try:
    con = mysql.connector.connect(host=h,user=u,database=db,password=pwd)

    if con.is_connected():
        print("Connection Established")

    con.close()
    
except Error as e:
    print(e)
