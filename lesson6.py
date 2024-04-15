import sqlite3
con = sqlite3.connect('ayhan.db')
cursor = con.cursor()
# cursor.execute('''CREATE TABLE people
#                (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                age INTEGER)''')
# person_1 = ('Gashish',17)
# people = [('Emir',15),('Vikka',16),('Medina',16)]
# cursor.executemany("INSERT INTO people (name,age) VALUES (?,?)",people)
# con.commit()
# cursor.execute("SELECT * FROM people")
# print(cursor.fetchall())
# for i in cursor.fetchall():
#     print(i)
# print(cursor.fetchmany(3))
# print(cursor.fetchone())
# nam = cursor.fetchone()
# print(nam[1])
# cursor.execute("UPDATE people SET name = 'Samir' WHERE name = 'Emir'")
# con.commit()
cursor.execute("DELETE FROM people WHERE name = 'Samir'")
con.commit()