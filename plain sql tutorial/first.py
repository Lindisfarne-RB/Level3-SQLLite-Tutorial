import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
      stores (store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

#CREATE 
command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, 
FOREIGN KEY (store_id) REFERENCES stores(store_id))"""
cursor.execute(command2)

cursor.execute("INSERT INTO stores VALUES (21, 'Howick')")
cursor.execute("INSERT INTO stores VALUES (22, 'Pakuranga') ")
cursor.execute("INSERT INTO stores VALUES (23, 'Flatbush') ")
               
cursor.execute("INSERT INTO purchases VALUES (11, 66, 45.67)")
cursor.execute("INSERT INTO purchases VALUES (21, 86, 15.11)")
               
print ("---------------------------- \n Purchase Table")
cursor.execute("SELECT * FROM purchases ")

results = cursor.fetchall()
print(results)


#KITE AI coding assistance
#UPDATE
cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 11")

cursor.execute("SELECT * FROM purchases ")

results = cursor.fetchall()
print(results)

#Delete
'''
cursor.execute("DELETE FROM purchases WHERE purchase id = 21")
cursor.execute("SELECT * FROM purchases ")
'''