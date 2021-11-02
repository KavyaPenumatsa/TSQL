import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Sonata@123",
database="training"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("kavya", "AP")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
print(myresult)
print("Name | Address")
for x in myresult:
    print(x[0] +" | " + x[1])
print(type(x))
mydb.close()