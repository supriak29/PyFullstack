# connect with database
# create cursor object
# execute create table:'books' query
# attributes - title, author, price
# sample entries 5 - take user input
# rollback if error occurs

import sqlite3

db = sqlite3.connect("bookstore.db")    # Connect with DB
cur = db.cursor()                       # Create cursor obj

# create table:books
cur.execute(""" CREATE TABLE IF NOT EXISTS books(
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT(50) NOT NULL,
                author TEXT(20),
                price REAL); """)

for x in range(1):
    title = input("Enter book title: ")
    author = input("Enter name of author: ")
    price = input("Enter price of book: ")

    # insert into DB
    sql = "INSERT INTO books(title,author,price) VALUES(?,?,?)"

    try:
        cur = db.cursor()
        cur.execute(sql,(title,author,price))
        db.commit()
        print("One record added successfully")
    except:
        print("Error in operation")
        db.rollback()

db.close()
