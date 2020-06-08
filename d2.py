import  sqlite3
db = sqlite3.connect('student.db')
cr = db.cursor() #create a cursor object then call its execute method
cr.execute("insert into login(UNAME,UPASS)Values('anu','131')")
db.commit()#call method
db.close()# close connection
print("Inserted Data")