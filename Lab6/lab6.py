import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user='root', password='')
my_cursor = mydb.cursor()
my_cursor.execute("USE ap")
# my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.fetchall())

#my_cursor.execute("CREATE TABLE ap_table_1 (pk1 INT PRIMARY KEY, description VARCHAR(50) NOT NULL)")
# my_cursor.execute("INSERT INTO ap_table_1 VALUES (1, 'test record 1'), (2, 'test record 2')");
mydb.commit()
my_cursor.execute("SELECT * FROM ap_table_1")
# print(my_cursor.fetchall())

for data in my_cursor.fetchall():
    print(data)