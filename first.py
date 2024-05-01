import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

command1 = """"CREATE TABLE IF NOT EXISTS
      stores (store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, 
FOREIGN KEY (store_id) 
REFERENCES stores(store_id))"""
cursor.execute(command2)

cursor.execute("INSERT INTO stores VALUES (21, 'Howick')")
cursor.execute("INSERT INTO stores VALUES (22, 'Pakuranga') ")
cursor.execute("INSERT INTO stores VALUES (23, 'Flatbush') ")
               
cursor.execute("INSERT INTO purchases VALUES (1, 66, 45.67)")
cursor.execute("INSERT INTO purchases VALUES (2, 86, 15.11)")
               
cursor.execute("SELECT * FROM purchases ")


results = cursor.fetchall()
print(results)
