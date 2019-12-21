import pymysql

db = pymysql.connect("localhost", "sudhagar", "Sudhagar@1995", "sample")
cur = db.cursor()
cur.execute("use sample")
try:
    cur.execute("create table hello (name varchar (40) NOT NULL)")
except Exception as e:
    print(e)
cur.execute("INSERT INTO hello(name) VALUES ('sudhagar')")
db.commit()
db.close()
