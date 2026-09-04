#Importing sqlite3
import sqlite3 as sql

db_connection = sql.connect("stocks.db")
cursor = db_connection.cursor()

cursor.execute("select * from filtered_symbols where exchange = 'NYQ'")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n\n")

cursor.execute("select * from filtered_symbols where exchange = 'BSE'")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("Data notified!")