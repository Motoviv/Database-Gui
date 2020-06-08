import  sqlite3
db = sqlite3.connect('student.db')
cr = db.cursor() #create a cursor object then call its execute method
cr.execute("create table login(UNAME text,UPASS text)")
db.commit()#call method
db.close()# close connection
print("hi")