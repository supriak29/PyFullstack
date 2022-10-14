import sqlite3

db = sqlite3.connect("bookstore.db")
cur = db.cursor()

total = 0

while True:
    title = input("Book Title:  ")
    sql = "SELECT * FROM books WHERE title=?"
    cur.execute(sql, (title,))
    var1,var2,var3, var4 = cur.fetchone()
    print(var1)
    print(var2)
    print(var3)
    
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
