import mysql.connector

def getdbconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Sonata@123",
        database="training"
    )
    return mydb