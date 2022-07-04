# create the connection process more generalised
# I should be able to pass any credentials to connect to the database
# host
# user
# password
# database
###########################################

# importing mysql connection library
import mysql.connector

def userConnect(h,u,db,pwd):
    con = mysql.connector.connect(h,u,db,pwd)
    con.close()
    print("Connection Established")

h = input("Enter host name: ")
u = input("Enter username: ")
db = input("Enter database name: ")
pwd = input("Enter password: ")

userConnect(h,u)
