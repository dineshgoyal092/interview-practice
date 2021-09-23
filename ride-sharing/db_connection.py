import sqlite3

db = sqlite3.connect("cab_data.db")
cursor = db.cursor()
create_users_table = " CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name TEXT, age INT, gender TEXT) "
cursor.execute(create_users_table)

# Insert Users
users = [
        ("Kishuk", 23, 'M'),
        ("Goyal", 23, 'M'),
        ("Divya", 22, 'M'),
        ("Rohan", 36, 'M')
        ]

cursor.executemany("INSERT INTO User(name, age, gender) VALUES(?,?,?)", users)
db.commit()
select_users_table = "SELECT * FROM  User"
for i in cursor.execute(select_users_table):
    print i
