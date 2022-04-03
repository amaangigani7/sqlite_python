import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'sql@gmail.com'
phone = input("Please enter your phone no. : ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"

update_cursor = db.cursor()
# update_cursor.executescript(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updates.".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)
