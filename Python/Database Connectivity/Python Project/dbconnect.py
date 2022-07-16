# connect with database

con = pymysql.connect(host="localhost",user="root", password="",
                      database="usermanagement")

print("Connected to Database")
      
cur = con.cursor()
