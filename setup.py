import sqlite3

conn = sqlite3.connect('Daten/database.db')

print(conn)

c = conn.cursor()

#c.execute("""CREATE TABLE passwords
#    (id INTEGER PRIMARY KEY AUTOINCREMENT,
#    website TEXT,
#    username TEXT,
#    password TEXT)""")

#c.execute("DROP TABLE passwords")
#conn.commit()
