import sqlite3

with sqlite3.connect("edu.dB") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
pass VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO user(username, firstname, surname, pass)
VALUES("test_User", "Bob", "Smith", "MrBob")
""")

db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
