
import  sqlite3
db = sqlite3.connect('student.db')
x='anita'
y="22"
cr = db.cursor() #create a cursor object then call its execute method
cr.execute("insert into login(UNAME,UPASS)Values('"+x+"','"+y+"')")
db.commit()#call method
db.close()# close connection
print("Inserted Data")