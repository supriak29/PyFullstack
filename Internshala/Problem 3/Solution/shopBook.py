import sqlite3

db = sqlite3.connect("bookstore.db")
cur = db.cursor()

total = 0

while True:
    title = input("Book Title:  ")
    sql = "SELECT * FROM books WHERE title=?"
    result = cur.execute(sql,(title,))
    row = result.fetchone()
    if row:
        print(row)
        price = row[3]
        copies = int(input("\nNo. of copies: "))
        cost = price*copies
        total += cost
    else:
        print("'{}' is not available!".format(title))
    choice = input("Add more books[Y/N]?")
    if choice == 'N' or choice=='n':
        break
print("Total cost of purchsed books: ",total)
db.close()
