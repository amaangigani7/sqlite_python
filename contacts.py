import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Amaan', 1234, 'amaan35@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Faizan', 56412, 'fazain64')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchall())
print(cursor.fetchall())
print(cursor.fetchall())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()

db.commit()
db.close()
