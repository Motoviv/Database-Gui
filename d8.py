#form design and take input
#fetch data from database -show all code
import sqlite3
db= sqlite3.connect('student.db')
cr=db.cursor()
r=cr.execute("select * from login ")
for r1 in r:
    print(r1[0],r1[1])
db.commit()
db.close()