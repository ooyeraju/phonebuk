import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, nmbr TEXT)')
print ("Table created successfully")
conn.close()