from distutils.util import execute
from multiprocessing import connection
import sqlite3

from colorama import Cursor

connection = sqlite3.connect('testDatabase.db')

cursor = connection.cursor()

try:
    create_table = "CREATE TABLE users(id int, username text, password text)"
    cursor.execute(create_table)
except sqlite3.OperationalError as e:
    user= (1,'user1','pass1')
    insert_query = "INSERT INTO users VALUES(?,?,?)"
    cursor.execute(insert_query,user)


    users = [
        (2,'user2','pass2'),
        (3,'user3','pass3'),
        (4,'user4','pass4'),
        (5,'user5','pass5'),
        (6,'user6','pass6')
    ]

    cursor.executemany(insert_query, users)

    select_query = "SELECT * FROM users"
    for row in cursor.execute(select_query):
        print(row)




    connection.commit()
    connection.close()