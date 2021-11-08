from dbconnection import getdbconnection
from service.tasks import *


def create_task(task):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "insert into tasks ( tid,tname, descr,tstatus,priori, note, bookmark, oid, cid, createdon, modifiedon) VALUES( %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)"
    val = (task.tid,task.tname,task.descr,task.tstatus,task.priori,task.note,task.bookmark,task.oid,task.cid,task.createdon,task.modifiedon)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def assign_task(oid,cid):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "update tasks set oid = %s where tid = %s"
    val = (oid,cid)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def assign_priority(tid,priori):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "update tasks set tid = %s where tid = %s "
    val = (tid,priori)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def searchtask(tname):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "select * from tasks where tname = %s "
    val = (tname)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def add_notes(note,bookmark):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "update tasks set note = %s,bookmark = %s where note = %s "
    val = (note,bookmark)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def track_status(tstatus,tname):
    mydb = getdbconnection()
    mycursor =mydb.cursor()
    sql =  "select * from tasks where tname = %s "
    val = (tstatus,tname)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()