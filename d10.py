#code for login page
import  sqlite3
db=sqlite3.connect('student.db')
cr= db.cursor()
x=input("Enter user Name = ")
y=input("Enter user Password = ")

r=cr.execute("select * from login where  UNAME ='"+x+"' AND UPASS ='"+y+"'")
for r1 in r :
    print("welcome")
    break
else:
    print("invalid username and password")
db.commit()
db.close()