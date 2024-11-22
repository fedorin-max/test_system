import sqlite3

conn = sqlite3.connect('db.sqlite')#приєдналися до БД
cursor = conn.cursor()#створили курсор

#отимали список таблиць
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = cursor.fetchall()
print(tables)

#вичитали дані із таблички user
cursor.execute("SELECT * FROM user;")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()