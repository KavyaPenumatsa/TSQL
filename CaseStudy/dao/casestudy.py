import mysql.connector as db
con=db.connect(host='localhost',user="root",password="Sonata@123")
cur=con.cursor()

def createdb():
    s="CREATE DATABASE  tasktrackingsystem"
    cur.execute(s)
    cur.close()
    con.close()
    print("Date base is cretaed successfully.....")
def createtable():
    con=db.connect(host="localhost",user="root",password="Sonata@123",database="tasktrackingsystem")
    cur=con.cursor()
    s="CREATE TABLE task_trac (taskid int,taskname varchar(20),descr varchar(20),status varchar(20),prior int,notes varchar(20),bookmark varchar(20),ownerid int,creatorid int,createdon int,modifidein int)"
    cur.execute(s)
    cur.close()
    con.close()
    print("Table created succesfully.....")
def insert():
    con = db.connect(host="localhost", user="root", password="Sonata@123", database="tasktrackingsystem")
    cur = con.cursor()
   # s = "insert into task_trac values (551,'createtable','tablecreation','inprogess',3, 'available' ,'bookmark1',55,55,2020,2021)"
   # cur.execute(s)
   # s="insert into task_trac values (552,'arrays','array operations','completed',2, 'available','bk2',56,56,2020,2020)"
    #cur.execute(s)
    s = "insert into task_trac values (553,'insert','inserting rows','completed',5, 'available','bk3',57,57,2020,2020)"
    cur.execute(s)
    con.commit()
    cur.close()
    con.close()
    print("Records inserted successfully..")
def update():
    con=db.connect(host='localhost',user="root",password="Sonata@123",database="tasktrackingsystem")
    cur=con.cursor()
    s="update task_trac set taskname='insert values' where  taskid=553 "
    cur.execute(s)
    con.commit()
    cur.close()
    con.close()
    print("Record updated successfully...")

def delete():
    con=db.connect(host='localhost',user="root",password="Sonata@123",database="tasktrackingsystem")
    cur=con.cursor()
    s="DELETE FROM task_trac where  taskname = 'insert' "
    cur.execute(s)
    con.commit()
    cur.close()
    con.close()
    print("Record deleted successfully...")

def display():
    con=db.connect(host='localhost',user="root",password="Sonata@123",database="tasktrackingsystem")
    cur=con.cursor()
    s="SELECT * FROM task_trac  "
    cur.execute(s)
    myresult = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    for s in myresult:
        print(s)

def search():
    con=db.connect(host='localhost',user="root",password="Sonata@123",database="tasktrackingsystem")
    cur=con.cursor()
    s="SELECT * FROM task_trac where taskid = 551 "
    cur.execute(s)
    myresult = cur.fetchall()
    if myresult:
        print(myresult)
    else:
        print("No record found")
    cur.close()
    con.close()
    print(s)



while True:
    print("1) Create Datebase")
    print("2) Create Table")
    print("3) Insert Record")
    print("4) Update Record")
    print("5) Delete Record")
    print("6) Display Table")
    print("7) Search From Table")
    print("9) Exit")
    ch=int(input("enter your choice:"))
    if (ch==1):
        createdb()
    elif (ch==2):
        createtable()
    elif (ch==3):
        insert()
    elif (ch==4):
        update()
    elif (ch==5):
        delete()
    elif (ch==6):
        display()
    elif (ch==7):
        search()
    else:
        break
