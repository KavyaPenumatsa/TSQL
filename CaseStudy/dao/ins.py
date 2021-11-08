

def insertrec():
    con = db.connect(host="localhost", user="root", password="Sonata@123", database="casestudy")
    cur = con.cursor()
    s = "insert into task (1001,'python','simple syntax','completed',1, 'available' ,'link',4356,4356,2013,2014)"
    cur.execute(s)
    s="insert into task_track values (1002,'arrays','three dimesional','completed',2, 'available','link',4356,4356,2015,2019)"
    cur.execute(s)
    con.commit()
    cur.close()
    con.close()
    print("Records inserted successfully........")