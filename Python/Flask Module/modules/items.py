import sqlite3
from dbConfig import DatabaseConfig


class ItemModule:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def findItem(cls, name):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
    

    def insert(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "INSERT INTO  items VALUES(?, ?)" 
        cursor.execute(query, (self.name, self.price))
        connection.commit()
        connection.close()

    def update(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        query = "UPDATE items SET price=? WHERE name=?" 
        cursor.execute(query, (self.price, self.name))
        connection.commit()
        connection.close()