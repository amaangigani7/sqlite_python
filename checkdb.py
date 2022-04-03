import sqlite3

com = sqlite3.connect("contacts.sqlite")

name = input("Enter a name: ")

for row in com.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

com.close()
