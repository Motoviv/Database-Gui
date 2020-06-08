#update page
import  sqlite3
db = sqlite3.connect('student.db')
cr = db.cursor() #create a cursor object then call its execute method
cr.execute("update login set UPASS='mital' where Uname='mohan'")
print("Data Updated")
db.commit()#call method
db.close()# close connection
