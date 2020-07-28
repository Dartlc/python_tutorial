import pymysql

db = pymysql.connect("localhost", 'sudhagar', "sudhagar@1995", 'sample')

x = db.cursor()
x.execute("use sample")
try:
    x.execute("create table demo(name varchar(30), age int) ")
except Exception as e:
    print(e)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

x.execute("INSERT INTO demo(name, age) VALUES (%s, %s)", (name, age))
db.commit()
x.execute("select * from demo")
c = x.fetchall()
print(c)
db.close()

