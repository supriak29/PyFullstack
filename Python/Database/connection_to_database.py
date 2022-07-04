# importing the mysql connection library
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root")

con.close()
