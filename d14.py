#update page
import  sqlite3
db = sqlite3.connect('student.db')
cr = db.cursor() #create a cursor object then call its execute method
s1=input("Enter Name = ")
s2=input("Enter  New Paaword = ")

cr.execute("update login set UPASS='"+s2+"' where Uname='"+s1+"'" )
print("Data Updated")
db.commit()#call method
db.close()# close connection
